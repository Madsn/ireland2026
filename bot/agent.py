"""Bridge from a chat message to a Claude Code CLI session.

Instead of calling the Anthropic API per token, this shells out to the
`claude` CLI in print mode against the wiki repo. Claude Code already has
Read/Edit/Write/Bash tools, reads the repo's CLAUDE.md for conventions, runs
the strict build, and does the git commit + push itself — so this file is just
a thin wrapper that runs it, keeps a session id per chat for continuity, and
returns the final text.

It streams the CLI's events (``--output-format stream-json``) so the caller can
show live progress ("editing…", "checking the build…", "publishing…") rather
than leaving the traveller staring at silence for a minute or two.

Auth/billing: the CLI uses whatever credential is on the server. Set
CLAUDE_CODE_OAUTH_TOKEN (from `claude setup-token` on a machine with a browser)
to run on your Claude Pro subscription rather than pay-per-token API billing.
"""

from __future__ import annotations

import json
import os
import subprocess
import threading
from pathlib import Path
from typing import Callable, Optional

# The wiki clone the CLI operates in. Defaults to this repo; set in deployment.
REPO_DIR = Path(os.environ.get("WIKI_REPO_DIR", Path(__file__).resolve().parent.parent)).resolve()

# Pre-approved tools so the CLI can edit and publish without interactive prompts
# (which can't be answered in --print mode anyway). Anything outside this list
# is denied, not run — a safe default for an unattended bot.
ALLOWED_TOOLS = "Read,Edit,Write,Glob,Grep,Bash(git *),Bash(mkdocs *)"

# Edits + strict build + push can take a few minutes on a small VM.
TIMEOUT = int(os.environ.get("CLAUDE_TIMEOUT", "900"))

PREAMBLE = """You are the Travel Agent for the Ireland 2026 family road-trip wiki \
(Madsen + Wilhelmsen, Jul 13-23), chatting with co-travellers over Telegram.

- Replies are read in a phone chat: keep them short and in plain text. Avoid \
Markdown tables, headings, and long bullet lists.
- The wiki is this git repo. Follow CLAUDE.md exactly when editing it.
- Before editing, run `git pull --ff-only` to get the latest.
- When asked to change the trip: make the edit, fix any cross-references and the \
mkdocs.yml nav as CLAUDE.md describes, run `mkdocs build --strict`, and ONLY if it \
passes, `git commit` and `git push` to the `main` branch so the live site updates. \
Never push a broken build — if the build fails, fix it or revert, don't leave the \
wiki half-edited.
- Confirm in the chat before destructive or far-reaching changes (deleting a page, \
changing a booking, anything touching many pages).
- After publishing, tell the traveller in one line what changed and that the live \
site refreshes in about a minute."""


def _phase_for_tool(name: str, command: str) -> Optional[str]:
    """Map a Claude Code tool use to a short, human progress line."""
    if name in ("Edit", "Write", "MultiEdit", "NotebookEdit"):
        return "✏️ Editing the wiki…"
    if name in ("Read", "Grep", "Glob"):
        return "🔎 Looking through the wiki…"
    if name == "Bash":
        c = command or ""
        if "mkdocs" in c:
            return "🔨 Checking the build…"
        if "git commit" in c or "git push" in c:
            return "📤 Publishing to the live site…"
        if "git pull" in c or "git fetch" in c:
            return "🔄 Syncing the latest…"
        return "⚙️ Running a command…"
    return None


class TravelAgent:
    """Drives the Claude Code CLI. One instance serves all chats."""

    def reply(
        self,
        session_id: Optional[str],
        message: str,
        author: str,
        on_status: Optional[Callable[[str], None]] = None,
    ) -> tuple[str, Optional[str]]:
        """Run one CLI turn. Returns (reply_text, session_id_to_store).

        ``on_status`` (if given) is called with a short progress string each time
        the work moves to a new phase, so the front-end can show live status.

        If the stored session has vanished (e.g. it was created during a run that
        failed before persisting), transparently retry once with a fresh session
        instead of surfacing a confusing 'No conversation found' error.
        """
        text, new_session_id = self._run_once(session_id, message, author, on_status)
        if session_id and "No conversation found with session ID" in text:
            text, new_session_id = self._run_once(None, message, author, on_status)
        return text, new_session_id

    def _run_once(
        self,
        session_id: Optional[str],
        message: str,
        author: str,
        on_status: Optional[Callable[[str], None]] = None,
    ) -> tuple[str, Optional[str]]:
        """One CLI invocation; resumes session_id when provided. Streams events."""
        cmd = [
            "claude", "-p", message,
            "--output-format", "stream-json", "--verbose",
            "--permission-mode", "acceptEdits",
            "--allowedTools", ALLOWED_TOOLS,
            "--append-system-prompt", f"{PREAMBLE}\n\nYou are talking to {author}.",
        ]
        if session_id:
            cmd += ["--resume", session_id]

        try:
            proc = subprocess.Popen(
                cmd, cwd=REPO_DIR, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                text=True, bufsize=1,
            )
        except FileNotFoundError:
            return "The `claude` CLI isn't installed on the server (see bot/README.md).", session_id

        # Watchdog: kill the run if it exceeds TIMEOUT (closes stdout, ending the loop).
        timed_out = {"v": False}

        def _kill() -> None:
            timed_out["v"] = True
            try:
                proc.kill()
            except Exception:
                pass

        timer = threading.Timer(TIMEOUT, _kill)
        timer.start()

        # Drain stderr in a thread so a full pipe can't deadlock the stdout reader.
        stderr_lines: list[str] = []

        def _drain() -> None:
            try:
                assert proc.stderr is not None
                for line in proc.stderr:
                    stderr_lines.append(line)
            except Exception:
                pass

        threading.Thread(target=_drain, daemon=True).start()

        result_event = None
        last_phase = None
        try:
            assert proc.stdout is not None
            for raw in proc.stdout:
                raw = raw.strip()
                if not raw:
                    continue
                try:
                    ev = json.loads(raw)
                except json.JSONDecodeError:
                    continue
                etype = ev.get("type")
                if etype == "assistant" and on_status:
                    for block in ev.get("message", {}).get("content", []):
                        if block.get("type") == "tool_use":
                            phase = _phase_for_tool(
                                block.get("name", ""),
                                (block.get("input") or {}).get("command", ""),
                            )
                            if phase and phase != last_phase:
                                last_phase = phase
                                try:
                                    on_status(phase)
                                except Exception:
                                    pass
                            break
                elif etype == "result":
                    result_event = ev
        finally:
            timer.cancel()
            proc.wait()

        if timed_out["v"]:
            return ("That took too long and timed out — try breaking it into a smaller "
                    "step (e.g. one page or one change at a time)."), session_id

        if result_event is None:
            err = ("".join(stderr_lines)).strip()
            return f"Claude Code failed: {err[:600] or 'no output'}", session_id

        text = (result_event.get("result") or "(done)").strip()
        if result_event.get("is_error"):
            if result_event.get("api_error_status") == 429 or "limit" in text.lower():
                return f"⚠️ Claude usage limit reached — {text or 'please try again later.'}", session_id
            return f"⚠️ {text}", session_id
        return text, result_event.get("session_id", session_id)
