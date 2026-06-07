"""Bridge from a chat message to a Claude Code CLI session.

Instead of calling the Anthropic API per token, this shells out to the
`claude` CLI in print mode against the wiki repo. Claude Code already has
Read/Edit/Write/Bash tools, reads the repo's CLAUDE.md for conventions, runs
the strict build, and does the git commit + push itself — so this file is just
a thin wrapper that runs it, keeps a session id per chat for continuity, and
returns the final text.

Auth/billing: the CLI uses whatever credential is on the server. Set
CLAUDE_CODE_OAUTH_TOKEN (from `claude setup-token` on a machine with a browser)
to run on your Claude Pro subscription rather than pay-per-token API billing.
"""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

# The wiki clone the CLI operates in. Defaults to this repo; set in deployment.
REPO_DIR = Path(os.environ.get("WIKI_REPO_DIR", Path(__file__).resolve().parent.parent)).resolve()

# Pre-approved tools so the CLI can edit and publish without interactive prompts
# (which can't be answered in --print mode anyway). Anything outside this list
# is denied, not run — a safe default for an unattended bot.
ALLOWED_TOOLS = "Read,Edit,Write,Glob,Grep,Bash(git *),Bash(mkdocs *)"

# Edits + strict build + push can take a couple of minutes.
TIMEOUT = int(os.environ.get("CLAUDE_TIMEOUT", "600"))

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


class TravelAgent:
    """Drives the Claude Code CLI. One instance serves all chats."""

    def reply(self, session_id: str | None, message: str, author: str) -> tuple[str, str | None]:
        """Run one CLI turn. Returns (reply_text, session_id_to_store).

        If the stored session has vanished (e.g. it was created during a run that
        failed before persisting), transparently retry once with a fresh session
        instead of surfacing a confusing 'No conversation found' error.
        """
        text, new_session_id = self._run_once(session_id, message, author)
        if session_id and "No conversation found with session ID" in text:
            text, new_session_id = self._run_once(None, message, author)
        return text, new_session_id

    def _run_once(self, session_id: str | None, message: str, author: str) -> tuple[str, str | None]:
        """One CLI invocation; resumes session_id when provided."""
        cmd = [
            "claude", "-p", message,
            "--output-format", "json",
            "--permission-mode", "acceptEdits",
            "--allowedTools", ALLOWED_TOOLS,
            "--append-system-prompt", f"{PREAMBLE}\n\nYou are talking to {author}.",
        ]
        if session_id:
            cmd += ["--resume", session_id]

        try:
            proc = subprocess.run(
                cmd, cwd=REPO_DIR, capture_output=True, text=True, timeout=TIMEOUT
            )
        except subprocess.TimeoutExpired:
            return "That took too long and timed out — try breaking it into a smaller step.", session_id
        except FileNotFoundError:
            return "The `claude` CLI isn't installed on the server (see bot/README.md).", session_id

        if proc.returncode != 0:
            # On failure the CLI may still print a JSON envelope (e.g. for usage
            # / rate limits). Surface its human-readable message rather than the
            # raw blob, and flag a hit limit clearly.
            out = (proc.stdout or "").strip()
            try:
                data = json.loads(out)
            except json.JSONDecodeError:
                data = None
            if isinstance(data, dict):
                msg = (data.get("result") or "").strip()
                if data.get("api_error_status") == 429 or "limit" in msg.lower():
                    return f"⚠️ Claude usage limit reached — {msg or 'please try again later.'}", session_id
                if msg:
                    return f"⚠️ {msg}", session_id
            err = (proc.stderr or out or "unknown error").strip()
            return f"Claude Code failed: {err[:600]}", session_id

        try:
            data = json.loads(proc.stdout)
        except json.JSONDecodeError:
            # Fall back to raw text if the output wasn't the expected JSON envelope.
            return (proc.stdout.strip()[:3500] or "(no output)"), session_id

        text = (data.get("result") or "(done)").strip()
        if data.get("is_error"):
            text = f"⚠️ {text}"
        return text, data.get("session_id", session_id)
