"""Telegram front-end for the Travel Agent.

Long-polls Telegram, restricts to an allow-list of chat IDs, and hands each
message to a Claude Code session (one per chat) that can edit the wiki and push
to the live branch. No public webhook to host — the bot reaches out to Telegram,
so it runs anywhere with outbound HTTPS.
"""

from __future__ import annotations

import os
import sys
import time

import requests

from agent import TravelAgent

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
API = f"https://api.telegram.org/bot{TOKEN}"

# Comma-separated Telegram chat IDs allowed to use the bot. The bot can edit and
# publish the wiki, so this MUST be set — empty means "nobody".
ALLOWED = {
    int(x) for x in os.environ.get("ALLOWED_CHAT_IDS", "").replace(" ", "").split(",") if x
}

# One Claude Code session id per chat, so conversations stay coherent across
# messages. Cleared by /reset. (In-memory: a process restart starts fresh
# sessions — fine for a family bot.)
_sessions: dict[int, str] = {}


def _send(chat_id: int, text: str) -> None:
    # Telegram caps messages at 4096 chars; chunk long replies. Plain text
    # (no parse_mode) so any stray Markdown shows literally rather than erroring.
    for i in range(0, len(text) or 1, 4000):
        requests.post(f"{API}/sendMessage", json={"chat_id": chat_id, "text": text[i:i + 4000] or " "}, timeout=30)


def _typing(chat_id: int) -> None:
    requests.post(f"{API}/sendChatAction", json={"chat_id": chat_id, "action": "typing"}, timeout=10)


def main() -> None:
    if not ALLOWED:
        sys.exit("Set ALLOWED_CHAT_IDS (comma-separated) — refusing to run open to everyone.")

    agent = TravelAgent()
    print(f"Travel Agent online. Serving chat IDs: {sorted(ALLOWED)}", flush=True)
    offset = None

    while True:
        try:
            resp = requests.get(
                f"{API}/getUpdates",
                params={"timeout": 30, "offset": offset, "allowed_updates": '["message"]'},
                timeout=40,
            ).json()
        except requests.RequestException:
            time.sleep(3)
            continue

        for update in resp.get("result", []):
            offset = update["update_id"] + 1
            msg = update.get("message") or {}
            chat_id = msg.get("chat", {}).get("id")
            text = msg.get("text")
            if chat_id is None or not text:
                continue

            if chat_id not in ALLOWED:
                _send(chat_id, "Sorry — this travel-agent bot is private to the Ireland 2026 group.")
                continue

            # Strip a trailing @BotName so group autocomplete (/help@Jenna3000_bot) still matches.
            cmd = text.strip().split("@")[0]
            if cmd in ("/start", "/help"):
                _send(chat_id, "I'm the Ireland 2026 travel agent. Ask me about the plan, or tell me a change "
                               "to make — I'll update the wiki and it goes live in about a minute. /reset starts a fresh chat.")
                continue
            if cmd == "/reset":
                _sessions.pop(chat_id, None)
                _send(chat_id, "Fresh start — what would you like to do?")
                continue

            sender = msg.get("from", {})
            author = sender.get("username") or sender.get("first_name") or str(chat_id)

            try:
                _typing(chat_id)
                reply, session_id = agent.reply(_sessions.get(chat_id), text, author)
                if session_id:
                    _sessions[chat_id] = session_id
            except Exception as e:
                reply = f"Something went wrong handling that: {e}"
            _send(chat_id, reply)


if __name__ == "__main__":
    main()
