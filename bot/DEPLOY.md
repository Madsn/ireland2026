# Deploying the bot on an Oracle Cloud Always Free VM

This is the setup runbook for getting the Telegram travel-agent bot (see
`README.md`) running 24/7 on Oracle Cloud's Always Free tier.

**It must be executed from a machine with a browser and unblocked network**
(a local Claude Code session or you at a terminal). The Claude Code *web*
sandbox cannot do it — it has no browser, can't reach Oracle/Telegram (network
policy returns 403), and has no OCI credentials. A ready-to-paste prompt for a
local Claude Code session is at the end.

> All real secrets live ONLY in `/opt/ireland2026/bot/.env` on the VM
> (`chmod 600`). Never commit them — this repo is public.

## What you'll create

| Secret | How |
|---|---|
| `TELEGRAM_BOT_TOKEN` | @BotFather → `/newbot`; display name **Jenna3000**, username `Jenna3000_bot` (or next free variant) |
| `CLAUDE_CODE_OAUTH_TOKEN` | `claude setup-token` on a machine logged into Claude Pro (≈1-yr token) |
| `GITHUB_TOKEN` | GitHub fine-grained PAT, repo `Madsn/ireland2026` only, Contents: Read & write |
| `ALLOWED_CHAT_IDS` | each adult messages the bot once → read `message.chat.id` from `https://api.telegram.org/bot<TOKEN>/getUpdates` |

## 1. Create the VM

Oracle Console → Compute → Instances → Create:
- Image **Ubuntu 22.04**.
- Shape **VM.Standard.A1.Flex** (1 OCPU / 6 GB — Always Free) or
  **VM.Standard.E2.1.Micro** (Always Free) if ARM capacity is unavailable. Arch
  is irrelevant (Claude Code is Node, MkDocs is Python).
- Add your SSH public key.
- Default VCN is fine: the bot is **outbound-only**, so no inbound rule beyond
  SSH is needed. Note the public IP.

## 2. Provision (SSH in as `ubuntu`, run with sudo)

```sh
apt-get update && apt-get install -y git python3 python3-venv python3-pip curl
curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && apt-get install -y nodejs
npm install -g @anthropic-ai/claude-code && claude --version
useradd --create-home --shell /bin/bash botuser
git clone https://github.com/Madsn/ireland2026.git /opt/ireland2026
chown -R botuser:botuser /opt/ireland2026
sudo -u botuser python3 -m venv /opt/ireland2026/bot/.venv
sudo -u botuser /opt/ireland2026/bot/.venv/bin/pip install -r /opt/ireland2026/bot/requirements.txt
```

(The venv installs `mkdocs-material` so `mkdocs` is on PATH for Claude Code's
strict-build step, plus `requests` for the bot.)

## 3. Secrets + git push auth

Create `/opt/ireland2026/bot/.env` (owner `botuser`, `chmod 600`):

```sh
TELEGRAM_BOT_TOKEN=...
CLAUDE_CODE_OAUTH_TOKEN=sk-ant-oat01-...
ALLOWED_CHAT_IDS=11111111,22222222
WIKI_REPO_DIR=/opt/ireland2026
```

Configure the clone to push to `main` with the PAT, and set the bot's git identity:

```sh
git -C /opt/ireland2026 remote set-url origin https://x-access-token:<GITHUB_TOKEN>@github.com/Madsn/ireland2026.git
git -C /opt/ireland2026 config pull.ff only
sudo -u botuser git config --global user.name  "Ireland 2026 bot"
sudo -u botuser git config --global user.email "travel-bot@users.noreply.github.com"
sudo -u botuser git config --global --add safe.directory /opt/ireland2026
```

## 4. Smoke-test Claude Code auth (also clears the first-run trust prompt)

```sh
sudo -u botuser env HOME=/home/botuser CLAUDE_CODE_OAUTH_TOKEN=sk-ant-oat01-... \
  claude -p "reply with OK" --output-format json
```

Expect JSON with a `result`. If it asks to trust the directory, run `claude`
once interactively as `botuser` inside `/opt/ireland2026` to accept, so headless
runs don't block.

## 5. systemd service

`/etc/systemd/system/travel-agent.service`:

```ini
[Unit]
Description=Ireland 2026 Telegram travel-agent bot
After=network-online.target
Wants=network-online.target

[Service]
User=botuser
WorkingDirectory=/opt/ireland2026/bot
EnvironmentFile=/opt/ireland2026/bot/.env
Environment=HOME=/home/botuser
Environment=PATH=/opt/ireland2026/bot/.venv/bin:/usr/local/bin:/usr/bin:/bin
ExecStart=/opt/ireland2026/bot/.venv/bin/python /opt/ireland2026/bot/telegram_bot.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```sh
systemctl daemon-reload && systemctl enable --now travel-agent
journalctl -u travel-agent -f   # expect "Travel Agent online…"
```

## 6. End-to-end test

From Telegram: `/help`, then a read ("what's the plan for Leg 4?"), then a tiny
edit ("add a note to the Dublin page that the bot is live"). Confirm the reply,
the commit on `main`, and the live site updating within ~1 min. Revert the test edit.

## Notes

- The bot pushes straight to `main` (no review gate, by design). Reverting a bad
  edit is `git revert`.
- `claude setup-token` is ~1-year; note the renewal date.
- Keep `ANTHROPIC_API_KEY` **unset** — it would override the subscription token
  and switch to pay-per-token API billing.
- Keep outbound internet open (default); no inbound rule needed except SSH.

---

## Paste-into-local-session prompt

Copy the block below into a fresh **local** Claude Code session (run from a clone
of this repo, on a machine logged into Telegram, Claude, GitHub, and Oracle):

```
Deploy the Ireland 2026 Telegram bot per bot/DEPLOY.md in this repo. The bot code
is on `main` under bot/. Execute the runbook end to end: create the Telegram bot
via @BotFather (display name Jenna3000, username Jenna3000_bot or next free),
run `claude setup-token` for the Claude Pro auth token, make a GitHub fine-grained
PAT (Contents R/W on Madsn/ireland2026), create an Oracle Always Free VM
(Ubuntu 22.04, A1.Flex or E2.1.Micro, region EMEA — account: noptech /
mikkel3@gmail.com), provision it, put all secrets in /opt/ireland2026/bot/.env on
the VM (never in the repo), install the systemd service, and run the smoke test +
end-to-end test. Pause and ask me for any step needing my login/MFA. When done,
report the bot username, the VM public IP, and that the end-to-end test passed.
```
