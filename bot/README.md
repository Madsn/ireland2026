# Travel Agent — Telegram bot

A chat bot that lets the whole travelling group talk to the trip's "travel
agent" AI and have it **update the wiki**. Message it like a person — ask about
the plan, or tell it to change something ("move Glendalough to the afternoon",
"add a rainy-day option near Belfast", "the Drogheda hotel is now €520") — and
it edits the Markdown, runs a strict build, and pushes to `main`. The live site
([madsn.github.io/ireland2026](https://madsn.github.io/ireland2026/)) refreshes
about a minute later.

It is **not gated to one person**: anyone whose Telegram chat ID is on the
allow-list can use it.

## How it works

```
Traveller (Telegram)  →  this bot (long-polling)  →  Claude (Anthropic API)
                                                        │  reads/edits docs/*.md
                                                        │  mkdocs build --strict   ← gate
                                                        │  git commit + push main
                                                        ▼
                                                   GitHub Pages redeploys
```

- The bot **long-polls** Telegram, so there's no public webhook/HTTPS endpoint to
  host — it runs anywhere with outbound internet.
- Claude runs a tool loop (`bot/agent.py`) with tools to list/read/search/edit
  pages and `publish`. **`publish` runs `mkdocs build --strict` and pushes only
  if it passes** — broken Markdown never reaches the live site.
- It edits a normal clone of this repo and pushes to `main`, so every change is
  an ordinary git commit you can review, revert, or `git blame`.

## One-time setup (~15 min)

1. **Create the bot.** In Telegram, message **@BotFather** → `/newbot`, follow the
   prompts, copy the token.
2. **Get an Anthropic API key** at <https://console.anthropic.com/>.
3. **Clone the wiki** somewhere the bot will run, with push access to `main`.
   The simplest auth is a token-embedded remote:
   ```sh
   git clone https://x-access-token:<GITHUB_TOKEN>@github.com/Madsn/ireland2026.git
   ```
   Use a GitHub fine-grained PAT (or deploy key) with **Contents: read & write**
   on this repo only.
4. **Install deps:**
   ```sh
   cd ireland2026/bot
   python -m venv .venv && . .venv/bin/activate
   pip install -r requirements.txt
   ```
5. **Configure.** `cp .env.example .env` and fill it in. For `ALLOWED_CHAT_IDS`:
   each traveller messages the bot once, then open
   `https://api.telegram.org/bot<TOKEN>/getUpdates` and read `message.chat.id`.
   Add the 4 adults' IDs (comma-separated).
6. **Run:**
   ```sh
   set -a; . .env; set +a
   python telegram_bot.py
   ```
   You should see `Travel Agent online`. Message the bot `/help`.

## Commands

- `/help` — what the bot does.
- `/reset` — clear the conversation history for that chat.

## Running it for real

For an always-on bot, run it under a process manager so it restarts on reboot
or crash. A minimal **systemd** unit:

```ini
# /etc/systemd/system/travel-agent.service
[Service]
WorkingDirectory=/srv/ireland2026/bot
EnvironmentFile=/srv/ireland2026/bot/.env
ExecStart=/srv/ireland2026/bot/.venv/bin/python telegram_bot.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

`sudo systemctl enable --now travel-agent`. Any small VM, Raspberry Pi, or a
container host (Fly.io / Railway / Render worker) works — no inbound ports
needed. Free-tier hosting is plenty for a family-sized chat.

## Safety notes

- **`ALLOWED_CHAT_IDS` is the access control.** The bot has write access to the
  wiki; an empty list makes it refuse to start. Keep the list to people you
  trust with the site.
- **Direct-to-`main`.** Changes go live without a review step (your choice). Every
  change is a git commit, so reverting is `git revert`. To add a review gate
  later, point `GIT_BRANCH` at a branch and open PRs instead.
- **Secrets stay in `.env`** (git-ignored) — never commit the API key, bot token,
  or a token-embedded remote URL.

## WhatsApp later

The wiki-editing core (`wiki.py`) and the agent (`agent.py`) are platform-
agnostic. To add WhatsApp, write a `whatsapp_bot.py` that receives messages via
the WhatsApp Cloud API and calls `TravelAgent.reply(...)` exactly as
`telegram_bot.py` does — everything downstream is unchanged.
