# Changelog

Modifications made to the itinerary across planning sessions, most recent first.

---

## 2026-06-02

### Hotel swap — Gelilah House + Ormeau Park → Hampton by Hilton Belfast City Centre

**Canceled:** Gelilah House (Loughbrickland, Jul 17–18, 1 night, £324) and Ormeau Park Residence (Belfast, Jul 18–20, 2 nights, £729.10).

**Booked:** Hampton by Hilton Belfast City Centre (15 Hope Street, BT12 5EE) · Jul 17–20 · 3 nights · 2 rooms (Queen Family Room each) · breakfast included · £583.94/room = **£1,167.88 total** · conf 5339666085 + 5122775279.

**Net effect:**
- Belfast stay extended from 2 nights to 3, now starting Jul 17 (was Jul 18)
- Breakfast now included across all NI nights (was 3 days without breakfast)
- No more narrow 15:00–18:00 check-in window (Hampton is standard hotel check-in from 15:00)
- Accommodation total revised from ~€4,664 to ~€4,800
- GoT Studio Tour: can now be done as a relaxed day trip from Belfast on Jul 18, or en route on Jul 17

**Pages updated:** Leg 3, Leg 4, Leg 5, accommodation.md, budget/overview.md, index.md, activities.md, places/belfast.md, todo.md, mkdocs.yml. Gelilah House and Ormeau Park Residence hotel pages deleted.

---

## 2026-05-31

### Itinerary rework — all 7 legs

**Convention change:** Added a `**Period covered:**` note to every leg, explicitly stating which dates that leg's day plan owns. The rule: the checkout/departure morning opens the *next* leg, so no date appears in two legs' day plans.

**Leg 1 — Dublin**

- Added structured day plans for all three activity days (previously Jul 15 was blank):
  - Jul 13: Wilhelmsen 5h arrival gap addressed — bag storage at reception, Phoenix Park walk while waiting for Madsen
  - Jul 14: Guinness Storehouse (morning, pre-booked) → Dublinia (afternoon); Temple Bar / The Brazen Head evening
  - Jul 15: EPIC Irish Emigration Museum (morning) + National Museum – Natural History "Dead Zoo" (afternoon); sit-down dinner evening
- Added specific trad music and restaurant recommendations for all three Dublin evenings, drawing on the existing activities catalog
- Updated Open Questions to include actionable restaurant pre-booking reminders

**Leg 2 — Drogheda**

- Removed the duplicate Jul 17 day plan (Newgrange + departure). Jul 17 content now lives entirely in Leg 3 where it belongs.
- Added Jul 16 evening suggestion: post-dinner walk to St Laurence Gate and the old town walls (free, walkable from hotel)
- Removed stale "latest viable departure ~10:30" note; Leg 3 holds the correct 11:30 departure

**Leg 3 — Northern Ireland**

- Newgrange is now fully documented in this leg's day plan (no longer a cross-reference to Leg 2)
- Jul 18 Gelilah House checkout section clarified: detail stays in Leg 3, Leg 4 no longer duplicates it

**Leg 4 — Belfast**

- Removed duplicate Gelilah House checkout line from the Jul 18 opening (it belongs in Leg 3)
- Jul 19 afternoon decided: **W5 Science Centre** (best family option for kids 5–12)
- Jul 19 morning: **Black Cab Tour** added as a highlighted option (mural tour of Falls Rd / Shankill Rd, ~1.5h); **Carrickfergus Castle** added as an alternative morning extension
- Jul 19 evening: **Cathedral Quarter** called out (The Duke of York / Dirty Onion / Mourne Seafood Bar)
- Jul 20 transit section (checkout + Carlingford + drive to Leixlip) moved out of Leg 4 and into Leg 5 where it belongs

**Leg 5 — Leixlip / Emerald Park**

- **Emerald Park maximised:** arrive at opening (~10:00), stay until close (~17:30). The previous forced 15:00 departure existed only to accommodate a Glendalough stop — that stop has been moved.
- Brought in Jul 20 transit content from Leg 4: Belfast checkout + Carlingford lunch detail now lives here
- Jul 20 evening: quiet rest night noted; St Catherine's Park (beside hotel) flagged for a short walk
- Map popup updated to remove the stale "leave by 15:00" note
- Glendalough removed from this leg

**Leg 6 — Wicklow**

- Glendalough visit moved from Jul 21 evening to Jul 22 morning (now in Leg 7). Previously the visit was squeezed into a 1-hour window at 16:15 — too rushed for one of Ireland's best heritage sites.
- Jul 21 is now just an arrival evening: drive from Emerald Park (~50 min), check in, dinner at Hugo's Restaurant
- Map popup updated accordingly

**Leg 7 — Departure**

- **Glendalough added as the Jul 22 morning anchor:** checkout Druids Glen ~10:00 → 20 min drive → 2h visit → 55 min drive to Premier Inn, arriving ~14:00 (check-in opens at 14:00 — timing is near-perfect). The previous 3-hour unaddressed gap at the Premier Inn is eliminated.
- **Folk music evening resolved:** The Cobblestone (Smithfield, 2 min from the Leg 1 hotel) recommended — nightly trad sessions, no cover, taxi from airport ~25 min. Alternatives listed for a pre-booked dinner-show option.
- **Terminal info added for Jul 23:** Ryanair FR632 (Madsen) → Terminal 1; Aer Lingus EI164 (Wilhelmsen) → Terminal 2. T1 and T2 are connected by an indoor walkway.
- Map updated: route now goes Druids Glen → Glendalough → Premier Inn.

---

## Earlier sessions

### Interactive maps — all 7 legs

Added Leaflet.js interactive maps to every itinerary leg:

- Green route line between departure and destination accommodations (via Leaflet Routing Machine)
- Blue circle markers for all POIs with popup descriptions
- Auto-fit bounds to include route + all POIs
- Fixed 7 incorrect POI coordinates on the index overview map

### Full-trip overview map — index page

Added an interactive Leaflet overview map to `index.md` showing all 7 accommodation stops and the overall route across Ireland and Northern Ireland.

### Plan B activities catalog

Built `docs/activities.md` — a full-trip reference covering every planned and alternative activity, organised by leg/region. Includes cost, duration, age range, booking notes, Google Maps links, and admonition warnings for must-pre-book items. Also includes restaurant tables and trad music venue lists for each leg.

### Google Maps links

Added Google Maps links to all activities across all legs and places pages.

### Geographic and timing feasibility review

- Removed Carrickmacross from Leg 2 (it was a 40 km wrong-direction detour off the Dublin → Drogheda route)
- Tightened Leg 2/3 day plan: Newgrange only on Jul 17 morning, depart by 10:30 (later revised to 11:30)
- Added Leg 3 timing schedule; fixed "full day" at Emerald Park (leave by 15:00 — later revised to full day)
- Corrected "Navan" → "Ashbourne" for Emerald Park in Leg 6
- Added Carlingford as a lunch stop on the Jul 20 Belfast → Leixlip drive
