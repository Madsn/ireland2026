"""The 'Travel Agent' — a Claude agent that chats about the Ireland 2026 trip
and edits the wiki on request.

A manual tool-use loop (rather than the SDK's auto tool-runner) so every publish
is gated behind a strict MkDocs build and we keep fine control over what lands
on the live branch. The wiki's own maintenance guide (CLAUDE.md) is loaded into
the cached system prompt, so the agent follows the same conventions a human
maintainer would.
"""

from __future__ import annotations

from pathlib import Path

import anthropic

import wiki

MODEL = "claude-opus-4-8"
MAX_TOKENS = 16000

_CLAUDE_MD = (wiki.REPO_DIR / "CLAUDE.md").read_text(encoding="utf-8")

SYSTEM_PROMPT = f"""You are the **Travel Agent** for a shared family road-trip wiki: \
the Ireland 2026 trip (Jul 13–23) for the Madsen + Wilhelmsen families. You talk \
to the travellers over Telegram and can edit the wiki on their behalf.

You are chatting in a group of co-travellers, not a single owner. Be warm, concise, \
and conversational — this is a phone chat, not a document. Keep replies short unless \
asked for detail. When you change the wiki, say plainly what you changed and that the \
live site will refresh in about a minute.

## What you can do
- Answer questions about the trip from the wiki content (read the relevant pages first).
- Make changes the travellers ask for: update an itinerary leg, swap a hotel, add a \
Plan B activity, fix a detail, add a page, etc.

## How to make a change — the rules that keep the live site healthy
1. **Read before you write.** Use read_page / search to see current content and exact \
wording before editing. Match the wiki's style (see the maintenance guide below).
2. **Edits are local until you publish.** write_page / edit_page only stage changes. \
Nothing is live until you call `publish`.
3. **publish runs a strict build first.** If the build fails, NOTHING is pushed and you \
get the errors back — fix them and call publish again. Never leave the wiki half-edited; \
either finish and publish, or revert your intent.
4. **Cross-references matter.** The same fact (a hotel, a cost, a date) often appears on \
several pages, and pages link to each other with relative paths and #anchors. When you \
remove or rename something, search the whole repo for it and fix every hit, or you leave \
a broken link the strict build may not catch. When you add a page, add it to the `nav:` \
tree in mkdocs.yml too — a page not in nav is invisible.
5. **Confirm destructive or far-reaching changes** (deleting a page, changing a booking, \
anything affecting many pages) before doing them — ask the traveller in chat first.
6. **You publish straight to the live branch.** There is no review step, so double-check \
factual changes (dates, costs, confirmation details) before publishing.

## The wiki's maintenance guide (authoritative — follow it)
<maintenance_guide>
{_CLAUDE_MD}
</maintenance_guide>
"""

TOOLS = [
    {
        "name": "list_pages",
        "description": "List every editable wiki file (all docs/**/*.md plus mkdocs.yml).",
        "input_schema": {"type": "object", "properties": {}, "additionalProperties": False},
    },
    {
        "name": "read_page",
        "description": "Read the full current contents of a wiki file.",
        "input_schema": {
            "type": "object",
            "properties": {"path": {"type": "string", "description": "Repo-relative path, e.g. docs/itinerary/leg-4-belfast.md"}},
            "required": ["path"],
            "additionalProperties": False,
        },
    },
    {
        "name": "search",
        "description": "Case-insensitive search across the whole wiki for a literal string. Use before removing/renaming anything to find every reference.",
        "input_schema": {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
            "additionalProperties": False,
        },
    },
    {
        "name": "write_page",
        "description": "Create or fully overwrite a Markdown page (or mkdocs.yml) with new content. Stages the change; does not publish.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "content": {"type": "string", "description": "The complete new file contents."},
            },
            "required": ["path", "content"],
            "additionalProperties": False,
        },
    },
    {
        "name": "edit_page",
        "description": "Replace one exact unique occurrence of old_string with new_string in a file. Stages the change; does not publish.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "old_string": {"type": "string", "description": "Exact text to replace; must appear exactly once."},
                "new_string": {"type": "string"},
            },
            "required": ["path", "old_string", "new_string"],
            "additionalProperties": False,
        },
    },
    {
        "name": "publish",
        "description": "Run a strict MkDocs build and, only if it passes, commit all staged changes and push to the live branch. Call this once the change is complete. Returns build errors (and publishes nothing) if the build fails.",
        "input_schema": {
            "type": "object",
            "properties": {"summary": {"type": "string", "description": "One-line commit summary of the change."}},
            "required": ["summary"],
            "additionalProperties": False,
        },
    },
]


def _run_tool(name: str, args: dict, author: str) -> tuple[str, bool]:
    """Execute a tool. Returns (result_text, is_error)."""
    try:
        if name == "list_pages":
            return wiki.list_pages(), False
        if name == "read_page":
            return wiki.read_page(args["path"]), False
        if name == "search":
            return wiki.search(args["query"]), False
        if name == "write_page":
            return wiki.write_page(args["path"], args["content"]), False
        if name == "edit_page":
            return wiki.edit_page(args["path"], args["old_string"], args["new_string"]), False
        if name == "publish":
            return wiki.publish(args["summary"], author), False
        return f"Unknown tool: {name}", True
    except wiki.WikiError as e:
        return str(e), True
    except Exception as e:  # surface unexpected failures to the model, don't crash the bot
        return f"Tool error: {e}", True


class TravelAgent:
    """Holds the Claude client; one instance serves all chats."""

    def __init__(self) -> None:
        self.client = anthropic.Anthropic()

    def reply(self, history: list[dict], author: str) -> str:
        """Run a full tool-use turn against the running conversation `history`
        (a list of {role, content} dicts, mutated in place to include this turn)
        and return the assistant's final text for Telegram."""
        # Pull the latest live content so edits build on current state.
        try:
            wiki.pull_latest()
        except Exception:
            pass  # best-effort; a stale read is better than a dead bot

        while True:
            response = self.client.messages.create(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                thinking={"type": "adaptive"},
                output_config={"effort": "high"},
                system=[{"type": "text", "text": SYSTEM_PROMPT, "cache_control": {"type": "ephemeral"}}],
                tools=TOOLS,
                messages=history,
            )
            history.append({"role": "assistant", "content": response.content})

            if response.stop_reason != "tool_use":
                texts = [b.text for b in response.content if b.type == "text"]
                return "\n\n".join(texts).strip() or "(done)"

            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    result, is_error = _run_tool(block.name, block.input, author)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                        "is_error": is_error,
                    })
            history.append({"role": "user", "content": tool_results})
