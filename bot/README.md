# Travel Agent — Telegram bot (Claude Code bridge)

A chat bot that lets the whole travelling group talk to the trip's "travel
agent" AI and have it **update the wiki**. Message it like a person — ask about
the plan, or tell it to change something ("move Glendalough to the afternoon",
"add a rainy-day option near Belfast", "the Drogheda hotel is now €520") — and
it edits the Markdown, runs a strict build, and pushes to `main`. The live site
([madsn.github.io/ireland2026](https://madsn.github.io/ireland2026/)) refreshes
about a minute later.

It is **not gated to one person**: anyone whose Telegram chat ID is on the
allow-list can use it.

## Why this design

Rather than calling an LLM API per token, the bot drives the **Claude Code CLI**.
That has two big payoffs:

- **It runs on your Claude Pro subscription, not pay-per-token API billing.**
  Authenticate the CLI with a `claude setup-token` (from your Pro plan) and the
  bot's usage draws on your subscription. No API key, no surprise bills.
- **Almost nothing to build.** Claude Code already has file + bash tools, reads
  this repo's `CLAUDE.md` for conventions, runs `mkdocs build --strict`, and does
  the `git commit` + `push` itself. The bot is just a ~110-line bridge.

```
Traveller (Telegram) → bot (long-polling) → `claude -p --resume` in the repo
                                               │ edits docs/*.md per CLAUDE.md
                                               │ mkdocs build --strict   ← gate
                                               │ git commit + push main
                                               ▼
                                          GitHub Pages redeploys
```

## Files

- `telegram_bot.py` — long-polling front-end; allow-list; one Claude Code session
  per chat; `/help` and `/reset`.
- `agent.py` — the bridge: builds and runs the `claude -p` command, keeps the
  session id, returns the reply. Holds the persona + publish rules.

## One-time setup (~15 min)

1. **Create the bot.** In Telegram, message **@BotFather** → `/newbot`, copy the token.
2. **Install Claude Code** on the server:
   ```sh
   npm install -g @anthropic-ai/claude-code
   claude --version
   ```
3. **Get a subscription token** (on a machine with a browser, logged into your
   Claude Pro account):
   ```sh
   claude setup-token        # → prints sk-ant-oat01-...  (valid ~1 year)
   ```
   Copy that token to the server as `CLAUDE_CODE_OAUTH_TOKEN` (step 6).
4. **Clone the wiki** on the server with push access to `main` — simplest is a
   token-embedded remote using a GitHub fine-grained PAT (Contents: read & write,
   this repo only):
   ```sh
   git clone https://x-access-token:<GITHUB_TOKEN>@github.com/Madsn/ireland2026.git
   git config --global user.email "travel-bot@example.com"
   git config --global user.name  "Ireland 2026 travel bot"
   ```
5. **Install Python deps** (gives Claude Code `mkdocs` to validate edits):
   ```sh
   cd ireland2026/bot
   python -m venv .venv && . .venv/bin/activate
   pip install -r requirements.txt
   ```
6. **Configure.** `cp .env.example .env` and fill it in. For `ALLOWED_CHAT_IDS`:
   each traveller messages the bot once, then open
   `https://api.telegram.org/bot<TOKEN>/getUpdates` and read `message.chat.id`.
7. **Run:**
   ```sh
   set -a; . .env; set +a
   python telegram_bot.py
   ```
   You should see `Travel Agent online`. Message the bot `/help`.

## Commands

- `/help` — what the bot does.
- `/reset` — start a fresh Claude Code session for that chat.

## Billing notes (Claude Pro)

- The CLI bills against your **Pro plan**, not the API. As of mid-2026, headless
  `claude -p` usage on a subscription draws from a separate ~$20/mo Agent-usage
  credit on Pro — ample for a family chat, and it can't run up an API bill.
- If `ANTHROPIC_API_KEY` is set in the environment, Claude Code uses **that**
  (pay-per-token) instead — so don't set it unless you want API billing.
- The `setup-token` is valid ~1 year. When it eventually expires the bot will
  start failing auth; re-run `claude setup-token` and update the env var.

## Running it for real

Run under a process manager so it restarts on reboot/crash. Minimal **systemd**:

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

`sudo systemctl enable --now travel-agent`. Any small VM, Raspberry Pi, or
container host works — no inbound ports needed.

## Safety notes

- **`ALLOWED_CHAT_IDS` is the access control.** The bot can publish to the live
  site; an empty list makes it refuse to start. Keep it to people you trust.
- **Pre-approved tools only.** The bridge passes `--permission-mode acceptEdits`
  and an allow-list (`Read,Edit,Write,Glob,Grep,Bash(git *),Bash(mkdocs *)`).
  Anything outside that is denied (it can't be approved in non-interactive mode),
  so the bot can't run arbitrary shell. It never uses `--dangerously-skip-permissions`.
- **Direct-to-`main`.** Changes go live without a review step (your choice). Every
  change is a git commit, so reverting is `git revert`. To add a review gate
  later, tell it (in `agent.py`'s preamble) to push a branch and open a PR instead.
- **Secrets stay in `.env`** (git-ignored) — never commit the bot token, the
  Claude token, or a token-embedded remote URL.

## WhatsApp later

`agent.py` is platform-agnostic. To add WhatsApp, write a `whatsapp_bot.py` that
receives messages via the WhatsApp Cloud API and calls
`TravelAgent.reply(session_id, text, author)` exactly as `telegram_bot.py` does —
everything downstream is unchanged. (Codex CLI on a ChatGPT Plus plan is also a
drop-in: swap the command built in `agent.py`.)
