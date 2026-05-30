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

## [2026-05-30] ingest | ireland-trip | Ireland 2026 Planning Document (Google Drive)

Source: raw/ireland-trip/ireland-2026-planning-doc.md
Two families: Madsen + Wilhelmsen · Jul 13–23, 2026 · 10 nights

Pages created (24):
- wiki/ireland-trip/sources/ireland-2026-planning-doc.md
- wiki/ireland-trip/overview.md (updated)
- wiki/ireland-trip/logistics/flights.md (updated)
- wiki/ireland-trip/logistics/accommodation.md (updated)
- wiki/ireland-trip/logistics/hendrick-smithfield.md
- wiki/ireland-trip/logistics/scholars-townhouse-hotel.md
- wiki/ireland-trip/logistics/gelilah-house.md
- wiki/ireland-trip/logistics/ormeau-park-residence.md
- wiki/ireland-trip/logistics/highlands-hotel-glenties.md
- wiki/ireland-trip/logistics/druids-glen-resort.md
- wiki/ireland-trip/logistics/premier-inn-dublin-airport.md
- wiki/ireland-trip/itinerary/leg-dublin.md
- wiki/ireland-trip/itinerary/leg-drogheda.md
- wiki/ireland-trip/itinerary/leg-northern-ireland.md
- wiki/ireland-trip/itinerary/leg-belfast.md
- wiki/ireland-trip/itinerary/leg-donegal.md
- wiki/ireland-trip/itinerary/leg-wicklow.md
- wiki/ireland-trip/itinerary/leg-dublin-departure.md
- wiki/ireland-trip/places/dublin.md
- wiki/ireland-trip/places/drogheda.md
- wiki/ireland-trip/places/newgrange.md
- wiki/ireland-trip/places/ardgillan.md
- wiki/ireland-trip/places/carrickmacross.md
- wiki/ireland-trip/places/belfast.md
- wiki/ireland-trip/places/emerald-park.md
- wiki/ireland-trip/places/glendalough.md

Key flags raised:
- Donegal leg (Jul 20–21) flagged for cancellation — replacement near Emerald Park needed
- Brú na Bóinne / Newgrange: must pre-book
- GoT Studio Tour: must pre-book (£64/family)
- Titanic Belfast: must pre-book
- Emerald Park: book by Jul 20 for 20% discount

---

## [2026-05-30] ingest | ireland-trip | Booking confirmation PDFs (4 hotels)

Source files: Confirmation_courtyard-leixlip_5057021351.pdf, Confirmation_gelilah-house_600100422.pdf, Confirmation_druids-glen_5388585982.pdf, Confirmation_ormeau-park_6178496251.pdf

Key findings:
- Court Yard Hotel, Leixlip (5057021351) confirmed — resolves Donegal/Emerald Park open question
- Druids Glen booking number corrected: 5388585982 (planning doc had typo 538858982)
- Gelilah House cancellation deadline: July 15 (free)
- Ormeau Park Residence cancellation deadline: July 12 (free)
- Druids Glen cancellation deadline: July 17 (free)
- Ormeau Park checkout before 10:00 on Jul 20 (early)
- Gelilah House checkout 08:00-11:00 on Jul 18 (early)
- Druids Glen: children's breakfast EUR 12.50 extra; Hugo's dinner must be booked directly

Pages updated (8): courtyard-leixlip.md (created), gelilah-house.md, ormeau-park-residence.md, druids-glen-resort.md, highlands-hotel-glenties.md, accommodation.md, leg-donegal.md, overview.md

---
