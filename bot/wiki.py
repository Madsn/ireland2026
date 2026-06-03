"""Filesystem + git operations on the Ireland 2026 wiki, scoped and safe.

Everything the Telegram travel-agent bot does to the wiki goes through here:
listing/reading/writing Markdown, building with --strict, and committing +
pushing to the live branch. Paths are confined to the repo; only Markdown and
mkdocs.yml are writable; a publish never lands if the strict build fails.
"""

from __future__ import annotations

import os
import subprocess
import time
from pathlib import Path

# Repo root = the clone the bot operates on. Defaults to this file's parent's
# parent (i.e. the wiki repo) but is overridable for deployment.
REPO_DIR = Path(os.environ.get("WIKI_REPO_DIR", Path(__file__).resolve().parent.parent)).resolve()
DOCS_DIR = REPO_DIR / "docs"
BRANCH = os.environ.get("GIT_BRANCH", "main")
REMOTE = os.environ.get("GIT_REMOTE", "origin")

# Only these may be written. mkdocs.yml lives at the root; everything else is
# Markdown under docs/.
_WRITABLE_SUFFIXES = {".md"}


class WikiError(Exception):
    """Raised for any disallowed or failed wiki operation."""


def _resolve(rel_path: str) -> Path:
    """Resolve a repo-relative path, refusing anything outside the repo."""
    p = (REPO_DIR / rel_path).resolve()
    if REPO_DIR not in p.parents and p != REPO_DIR:
        raise WikiError(f"Path escapes the repo: {rel_path}")
    return p


def _check_writable(p: Path) -> None:
    rel = p.relative_to(REPO_DIR)
    if p.name == "mkdocs.yml" and p == REPO_DIR / "mkdocs.yml":
        return
    if DOCS_DIR in p.parents and p.suffix in _WRITABLE_SUFFIXES:
        return
    raise WikiError(
        f"Refusing to write {rel}: only docs/**/*.md and mkdocs.yml are editable."
    )


def _git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=REPO_DIR,
        capture_output=True,
        text=True,
        check=check,
    )


# ── read-side operations ────────────────────────────────────────────────────

def list_pages() -> str:
    """Return every Markdown page plus mkdocs.yml, repo-relative, sorted."""
    pages = sorted(
        str(p.relative_to(REPO_DIR)) for p in DOCS_DIR.rglob("*.md")
    )
    return "\n".join(["mkdocs.yml", *pages])


def read_page(rel_path: str) -> str:
    p = _resolve(rel_path)
    if not p.is_file():
        raise WikiError(f"No such file: {rel_path}")
    return p.read_text(encoding="utf-8")


def search(query: str) -> str:
    """Case-insensitive fixed-string search across the wiki (git grep)."""
    proc = _git("grep", "-n", "-i", "-F", query, "--", "docs", "mkdocs.yml", check=False)
    if proc.returncode not in (0, 1):  # 1 = no matches, which is fine
        raise WikiError(f"search failed: {proc.stderr.strip()}")
    return proc.stdout.strip() or "(no matches)"


# ── write-side operations (staged in the working tree, not yet published) ────

def write_page(rel_path: str, content: str) -> str:
    p = _resolve(rel_path)
    _check_writable(p)
    existed = p.is_file()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content if content.endswith("\n") else content + "\n", encoding="utf-8")
    return f"{'Updated' if existed else 'Created'} {rel_path} ({len(content)} chars). Not yet published."


def edit_page(rel_path: str, old: str, new: str) -> str:
    p = _resolve(rel_path)
    _check_writable(p)
    text = read_page(rel_path)
    count = text.count(old)
    if count == 0:
        raise WikiError(f"old_string not found in {rel_path}. Read the page and match exactly.")
    if count > 1:
        raise WikiError(f"old_string appears {count}× in {rel_path}; make it unique.")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")
    return f"Edited {rel_path}. Not yet published — call publish when the change is complete."


# ── publish: build-gate, then commit + push to the live branch ───────────────

def has_pending_changes() -> bool:
    return bool(_git("status", "--porcelain", check=False).stdout.strip())


def pull_latest() -> str:
    """Fast-forward the local branch to the remote before editing."""
    _git("fetch", REMOTE, BRANCH, check=False)
    proc = _git("merge", "--ff-only", f"{REMOTE}/{BRANCH}", check=False)
    return proc.stdout.strip() or proc.stderr.strip() or "up to date"


def _strict_build() -> tuple[bool, str]:
    proc = subprocess.run(
        ["mkdocs", "build", "--strict", "--quiet"],
        cwd=REPO_DIR,
        capture_output=True,
        text=True,
    )
    out = (proc.stdout + proc.stderr).strip()
    return proc.returncode == 0, out


def publish(summary: str, author: str) -> str:
    """Validate with a strict build, then commit and push. No push on failure."""
    if not has_pending_changes():
        return "Nothing to publish — no pending changes."

    ok, build_out = _strict_build()
    if not ok:
        # Leave the working tree as-is so the agent can fix and retry.
        raise WikiError(
            "Strict build FAILED — nothing was published. Fix these and retry:\n"
            + (build_out[-2000:] or "(no output)")
        )

    _git("add", "-A")
    message = f"{summary}\n\nVia travel-agent bot, requested by {author}."
    _git("commit", "-m", message)

    last_err = ""
    for attempt in range(4):
        proc = _git("push", "-u", REMOTE, BRANCH, check=False)
        if proc.returncode == 0:
            sha = _git("rev-parse", "--short", "HEAD", check=False).stdout.strip()
            return f"Published as {sha} → {BRANCH}. The live site rebuilds in ~1 minute."
        last_err = proc.stderr.strip()
        time.sleep(2 ** (attempt + 1))
    raise WikiError(f"Build passed and change is committed, but push failed: {last_err}")
