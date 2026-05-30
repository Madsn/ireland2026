# Wiki Log

Append-only chronological record of all wiki operations.
**Never edit past entries.** The history of how this knowledge base evolved is itself valuable.

Maintained by the LLM agent. Do not edit manually.

---

## Format

```
## [YYYY-MM-DD] operation | domain | description
```

Operations: `ingest` | `query` | `lint` | `digest` | `update` | `bootstrap`

Parseable with:
```bash
grep "^## \[" wiki/log.md | tail -10   # last 10 entries
grep "ingest" wiki/log.md | wc -l      # total ingests
grep "2026-05" wiki/log.md             # all entries from May 2026
```

---

## [2026-05-30] bootstrap | ireland-trip | Initial wiki structure created

Wiki initialized from LLM Wiki Template.
Domain: ireland-trip (single domain)
Page types: places, logistics, itinerary, budget, sources
Tool: Claude Code

Seed pages created:
- wiki/ireland-trip/overview.md
- wiki/ireland-trip/logistics/flights.md
- wiki/ireland-trip/logistics/accommodation.md
- wiki/ireland-trip/budget/overview.md

---
