# CLAUDE.md — maintenance guide for this wiki

You are editing the **Ireland 2026 trip wiki**: a 10-night road trip (Jul 13–23,
2026) for two families (Madsen + Wilhelmsen). It's a static site built with
**MkDocs + Material theme** and published to **GitHub Pages**.

- **Live site:** https://madsn.github.io/ireland2026/
- **Repo:** https://github.com/Madsn/ireland2026 (canonical branch: `main`)
- This git repo is the **single source of truth**. Edit Markdown here, push, done.

## The 30-second model

Everything is Markdown in `docs/`. One config file, `mkdocs.yml`, defines the
site settings **and** the entire navigation tree. Pushing to `main` deploys.
That's the whole system — there is no database, no CMS, no build step you run by
hand.

## Repo layout

```
mkdocs.yml                        ← site config + the nav: tree (read this first)
requirements.txt                  ← just mkdocs-material
.github/workflows/deploy.yml      ← auto-deploys on every push to main
docs/
  index.md                        ← Overview / hub page
  itinerary/   leg-1-dublin.md … leg-7-departure.md   (the day-by-day plan)
  logistics/   flights.md, accommodation.md + one page per hotel
  places/      dublin.md, newgrange.md, belfast.md, …  (attractions)
  budget/      overview.md
```

29 content pages today. The page count and exact filenames drift over time —
trust `docs/` and `mkdocs.yml`, not this list.

## How to update an existing page

1. Edit the `.md` file under `docs/`.
2. Commit and push to `main`. That's it — the page is already in the nav.

## How to add a new page

Two steps. **Both are required** — MkDocs does **not** auto-discover pages.

1. Create the `.md` file in the right `docs/` subdirectory.
2. Add an entry to the `nav:` tree in `mkdocs.yml`, under the correct section.

A file that isn't in `nav:` still builds and is reachable by URL, but it appears
nowhere in the sidebar — so for this wiki, "not in nav" means "invisible."

To remove a page: delete the file **and** its `nav:` line.

## Navigation

`mkdocs.yml` → `nav:` is the only thing that controls the sidebar, order, and
section grouping. Display labels live there (e.g.
`'Leg 1 — Dublin (Jul 13–16)': itinerary/leg-1-dublin.md`), so you can rename
what a page is called in the menu without touching the file. Sections are
`Itinerary`, `Logistics`, `Places`, plus top-level `Overview` and `Budget`.

## Link conventions

Internal links are **relative paths to the `.md` file** (MkDocs rewrites the
extension at build). Never use absolute paths or a `/ireland2026/` prefix.

| Linking from | To | Write |
|---|---|---|
| `docs/index.md` | a section page | `itinerary/leg-1-dublin.md` |
| a page in a subdir | a page in **another** subdir | `../logistics/flights.md` |
| a page in a subdir | a page in the **same** subdir | `flights.md` |

When in doubt, copy a link that already works in a sibling page.

## Content conventions

- Every page opens with a single `# H1` title.
- Lead with key facts as bold key–value lines (`**Base:** …`, `**Dates:** …`).
- Use **tables** for anything structured (day plans, costs, hotel details).
- Cross-link generously: itinerary legs link to their hotel (logistics) and the
  attractions (places) for that leg, and back.
- Enabled Markdown extras: `tables`, `footnotes`, `admonition` (`!!! note`),
  and `toc` with permalinks. Material handles search automatically.

## Deployment

Push to `main` → `.github/workflows/deploy.yml` runs `mkdocs gh-deploy --force`
→ live in ~1 minute. No manual deploy step.

**Never push broken Markdown.** If `mkdocs` is installed locally, sanity-check
with `mkdocs build --strict` (flags broken internal links and bad nav refs)
before pushing. A bad build fails the Action and the site stays on the last good
version.

## Known intentional oddity

`logistics/highlands-hotel-glenties.md` is labelled
`⚠️ Highlands Hotel (CANCEL)` on purpose — it's a standing reminder to cancel
booking `6425169088`. Don't "fix" or delete it until that booking is cancelled.

## Historical note: llmwiki.app

A parallel copy of this content lives in llmwiki.app (KB `ireland2026`, via the
`fa4d8b4e` MCP connector). It was the original authoring tool but is **no longer
the source of truth** — don't sync changes back to it. This git repo wins.
