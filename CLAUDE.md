# CLAUDE.md — LLM Wiki Schema
# Ireland 2026 Trip Planning Knowledge Base
# Maintained by Claude Code · 2026

---

## Overview

This is a **single-domain LLM Wiki** for planning a trip to Ireland in 2026.
The human sources documents, links, and notes. You do all the writing, filing,
cross-referencing, and bookkeeping.

Active domains:

| Domain ID      | Name         | Root folder             |
|----------------|--------------|-------------------------|
| `ireland-trip` | Ireland Trip | `wiki/ireland-trip/`    |

---

## Directory Structure

```
ireland2026/
├── raw/                          # IMMUTABLE. Never modify. Source documents.
│   └── ireland-trip/             # Drop articles, guides, booking confirmations here
│
├── wiki/                         # Your knowledge base. Create and update freely.
│   ├── index.md                  # Master catalog — update on EVERY ingest
│   ├── log.md                    # Append-only chronological record
│   ├── overview.md               # High-level trip overview and status
│   └── ireland-trip/
│       ├── overview.md           # Trip summary, dates, key decisions
│       ├── places/               # Towns, regions, attractions, restaurants
│       ├── logistics/            # Flights, accommodation, car rental, ferries
│       ├── itinerary/            # Day-by-day or week-by-week schedule pages
│       └── budget/               # Cost estimates, actuals, category breakdowns
│
├── sessions/                     # AUTO-EXPORTED session transcripts (never edit manually)
│   ├── exports/
│   ├── confidential/
│   └── wiki-digests/
│
├── .claude/
│   ├── settings.json
│   └── scripts/
│       ├── export-session.py
│       ├── index-sessions.sh
│       └── recall.sh
│
├── .exportignore
├── .gitignore
├── sessions.db                   # SQLite FTS5 index (local only, gitignored)
└── CLAUDE.md                     # This file.
```

---

## SESSION EXPORT SYSTEM
## The layer that makes memory survive context compression

Every Claude Code session is automatically exported to markdown before the context
compresses. Exports are indexed in SQLite FTS5 — full-text searchable with no API
calls, no embeddings, no vector database. Just markdown and SQL.

### Three hooks

**PreCompact** — fires before context compression triggered by manual `/compact`.
**Does not fire for automatic context compression** (when the context limit is hit
mid-session). For auto-compacted sessions, SessionEnd is the only automatic safety net.

**SessionEnd** — fires when the session exits normally.
Catches short sessions that never triggered PreCompact.

**SessionStart** — fires when a new session begins.
Indexes any unindexed exports, prints last 3 sessions so you know where you left off.

### Manual recovery — when a session wasn't captured

```bash
# Export all unexported sessions from the last 7 days
python3 .claude/scripts/sweep-sessions.py --days 7

# Or check what would be exported first:
python3 .claude/scripts/sweep-sessions.py --days 7 --dry-run
```

**Single session recovery:**
```bash
python3 .claude/scripts/export-session.py \
  --trigger manual \
  --transcript ~/.claude/projects/<project-slug>/<session-id>.jsonl
bash .claude/scripts/index-sessions.sh
```

Check `.claude/hooks.log` for a timestamped record of when hooks ran.

### Shell aliases (add to ~/.zshrc or ~/.bashrc)

```bash
export WIKI_ROOT="$HOME/path/to/ireland2026"

wikiexit() {
    python3 "$WIKI_ROOT/.claude/scripts/export-session.py" --trigger manual
    python3 "$WIKI_ROOT/.claude/scripts/sweep-sessions.py" --days 7
}

wikisweep() {
    python3 "$WIKI_ROOT/.claude/scripts/sweep-sessions.py"
}
```

---

### Confidentiality controls

**Control 1 — Sentinel file** (skip export entirely):
```bash
touch .claude/no-export   # before starting a sensitive session
# or say "This session is confidential" at the first prompt
```

**Control 2 — .exportignore** (export to disk but exclude from search index):
Add filename patterns to `.exportignore`.

**Control 3 — GPG encryption:**
```bash
python3 .claude/scripts/export-session.py --trigger manual --label confidential
```

---

## Page Formats

### places/SLUG.md — one page per place (town, region, attraction, restaurant)
```markdown
---
title: "Place Name"
place_type: town | region | attraction | restaurant | pub | accommodation | landmark
county: [Cork | Kerry | Galway | Clare | etc.]
domain: ireland-trip
tags: []
last_updated: YYYY-MM-DD
---

# [Place Name]

## What It Is
Brief description.

## Why We're Interested
What caught our attention / why it's on the list.

## Key Facts
- Opening hours / admission / booking required?
- Distance from [nearest hub]
- Best time to visit

## Notes & Tips
Practical notes from guides, reviews, or past sessions.

## Sources
- [[sources/slug]] — where this info came from

## Connections
- Near [[places/other-place]]
- On [[itinerary/day-N]] itinerary
```

### logistics/SLUG.md — one page per booking or logistical item
```markdown
---
title: "Logistics: [Item Name]"
logistics_type: flight | accommodation | car_rental | ferry | transfer | insurance | other
status: researching | booked | confirmed | cancelled
domain: ireland-trip
tags: []
last_updated: YYYY-MM-DD
---

# [Item Name]

## Summary
What's booked / what we're researching.

## Key Details
- Dates:
- Provider:
- Cost:
- Confirmation #:
- Cancellation policy:

## Options Considered
If still researching, list the options and trade-offs.

## Notes
```

### itinerary/SLUG.md — one page per day or leg of the trip
```markdown
---
title: "Itinerary: [Day N or Leg Name]"
date: YYYY-MM-DD
status: draft | confirmed
domain: ireland-trip
---

# [Day N — Location]

## Plan
| Time | Activity | Notes |
|------|----------|-------|
| Morning | | |
| Afternoon | | |
| Evening | | |

## Accommodation
[[logistics/accommodation-slug]]

## Driving / Transport
Approximate driving time from previous stop.

## Contingency
Bad weather / backup plan.

## Open Questions
```

### budget/SLUG.md — one page per budget category or snapshot
```markdown
---
title: "Budget: [Category or Snapshot]"
budget_type: category | snapshot | actual
domain: ireland-trip
last_updated: YYYY-MM-DD
---

# Budget: [Category]

## Estimate
| Item | Low | High | Booked |
|------|-----|------|--------|

## Notes
Assumptions, exchange rate used, what's included/excluded.
```

### sources/SLUG.md — one per ingested document
```markdown
---
title: "Full Title of Source"
domain: ireland-trip
date_ingested: YYYY-MM-DD
source_type: article | guide | blog | booking | forum | video | other
tags: []
raw_path: raw/ireland-trip/filename.md
---

# [Title]

## Summary
2–4 sentence plain-English summary.

## Key Claims / Recommendations
- Item 1
- Item 2

## Places Mentioned
- [[places/slug]] — context

## Wiki Pages Updated
List every wiki page touched during this ingest.
```

---

## Special Files

### wiki/index.md
Master catalog. **Update on every ingest — no exceptions.**
```
| [[path/to/page]] | One-line description | domain | date |
```
Organized by page type. The LLM reads this first on every query.

### wiki/log.md
Append-only. **Never edit past entries.**
```
## [YYYY-MM-DD] ingest | ireland-trip | Source Title
## [YYYY-MM-DD] query | ireland-trip | Question answered + filed
## [YYYY-MM-DD] update | ireland-trip | Page updated from chat
```
Parseable: `grep "^## \[" wiki/log.md | tail -10`

---

## Operations

### INGEST — `> ingest ireland-trip raw/ireland-trip/file.md`
1. Read the source from `raw/`
2. Brief 2–3 sentence takeaway
3. Create `wiki/ireland-trip/sources/SLUG.md`
4. Update or create any places, logistics, or itinerary pages touched
5. Update `wiki/index.md`
6. Append to `wiki/log.md`
7. Report: files created/modified

### QUERY — `> [question]`
1. Check past sessions: `bash .claude/scripts/recall.sh "[keywords]"`
2. Read `wiki/index.md` to find relevant pages
3. Read those pages, drill into linked pages as needed
4. Synthesize answer with inline citations: `[[wiki/ireland-trip/path]]`
5. Ask: *"Should I file this answer as a wiki page?"*

### RECALL — `> recall: [what you're looking for]`
```bash
bash .claude/scripts/recall.sh "your search terms"
bash .claude/scripts/recall.sh --recent 5
bash .claude/scripts/recall.sh --date 2026-03
```

### DIGEST — `> digest sessions`
Scan `sessions/exports/` for undigested sessions. Extract structured knowledge.
File as wiki pages. Move processed files to `sessions/wiki-digests/`.

### LINT — `> lint`
Check for orphan pages, stale info, missing cross-references, unlinked places.
Suggest: gaps in itinerary, unresearched places, missing logistics.

### UPDATE — `> update ireland-trip [path]`
Update a specific wiki page from information provided in chat (no raw file needed).

---

## Domain Conventions

### ireland-trip — Ireland Trip Planning

**Purpose**: Everything needed to plan and execute a 2026 trip to Ireland — places to visit,
logistics (flights, accommodation, car rental), a day-by-day itinerary, and budget tracking.

**Key pages to create early**:
- `wiki/ireland-trip/overview.md` — trip dates, rough route, key constraints
- `wiki/ireland-trip/logistics/flights.md` — flight options / booked flights
- `wiki/ireland-trip/logistics/accommodation.md` — accommodation overview
- `wiki/ireland-trip/budget/overview.md` — total budget estimate

**Page type conventions**:
- **places/**: One page per named place. Slug = kebab-case name (e.g. `dingle-peninsula.md`, `cliffs-of-moher.md`).
- **logistics/**: One page per booking category or specific booking (e.g. `flights.md`, `car-rental.md`, `killarney-hotel.md`).
- **itinerary/**: One page per day or named leg (e.g. `day-01.md`, `day-02.md`, or `leg-ring-of-kerry.md`).
- **budget/**: One overview page plus per-category breakdowns as needed.

**Special rules**:
- When a place is mentioned in any source, check whether a places/ page exists and create or update it.
- When a logistics item changes status (researching → booked → confirmed), update the page status field.
- When itinerary days are drafted or revised, check driving times between stops and flag if a day looks overloaded (>3h driving + multiple stops).
- Always note the county for place pages — useful for grouping by region.
- Cross-reference: if a place is on a draft itinerary day, link it from the itinerary page and vice versa.

---

## Tone and Judgment

- Write for a traveler who is organized but not obsessive. Be practical and specific.
- Flag things that need booking in advance (popular restaurants, tours, accommodation in peak season).
- Surface contradictions — e.g. if one source says a road is closed seasonally and another doesn't mention it.
- Short pages with good links beat long sprawling pages.
- The log and session exports are sacred — never edit history.

---

## Co-Evolution Note

This schema is a starting point. As planning progresses, update this file.
If a new page type is needed (e.g. `packing/` or `restaurants/`), add it here and note
the change in `wiki/log.md`.

---

*Ireland 2026 Trip Wiki · Built on LLM Wiki Template · MIT License*
