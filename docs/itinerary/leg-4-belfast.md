# Leg 4 — Belfast (Jul 17–20)

3-night Belfast base at [Hampton by Hilton Belfast City Centre](../logistics/hampton-by-hilton-belfast.md) · £1,167.88 (2 rooms) · breakfast included ✅. Check-in from 15:00 on Jul 17; checkout by 11:00 on Jul 20.

**Period covered:** Jul 17 afternoon/evening (arrival from Drogheda — transit covered in [Leg 3](leg-3-northern-ireland.md)), Jul 18–19 (two full Belfast days), Jul 20 morning checkout + drive to Leixlip opens [Leg 5](leg-5-leixlip.md).

<style>
  #map-leg4 { height: 430px; margin: 1.5rem 0; border-radius: 8px; border: 1px solid #e0e0e0; }
  #map-leg4 .leaflet-routing-container { display: none !important; }
</style>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<div id="map-leg4"></div>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://unpkg.com/leaflet-routing-machine@3.2.12/dist/leaflet-routing-machine.min.js"></script>
<script>
(function () {
  var base = { ll: [54.59350, -5.93540], popup: '<b>Hampton by Hilton Belfast City Centre</b><br>Jul 17–20 · 3 nights · breakfast included' };
  var pois = [
    { ll: [54.60760, -5.91070], popup: '<b>Titanic Belfast</b><br>⭐ Must pre-book — sells out in summer' },
    { ll: [54.60710, -5.91080], popup: '<b>SS Nomadic</b><br>Titanic\'s tender ship · adjacent to Titanic Belfast' },
    { ll: [54.58470, -5.93400], popup: '<b>Ulster Museum</b><br>Free entry' },
    { ll: [54.62920, -5.79390], popup: '<b>Ulster Folk Museum</b><br>Open-air museum · ~20 min from city' },
    { ll: [54.60870, -5.90940], popup: '<b>W5 Science Centre</b><br>Great for kids' },
    { ll: [54.60140, -5.92890], popup: '<b>Belfast Cathedral (St Anne\'s)</b><br>City centre' },
    { ll: [54.62600, -5.96300], popup: '<b>Belfast Castle</b><br>Cave Hill · views over city' },
    { ll: [54.71550, -5.80760], popup: '<b>Carrickfergus Castle</b><br>~20 min north · well-preserved Norman castle' },
    { ll: [54.34780, -6.27820], popup: '<b>Game of Thrones Studio Tour</b><br>Banbridge · ~40 min drive · day trip option Jul 18' },
  ];

  var allPts = [base.ll].concat(pois.map(function (p) { return p.ll; }));
  var bounds = L.latLngBounds(allPts.map(function (ll) { return L.latLng(ll[0], ll[1]); }));

  var map = L.map('map-leg4', { scrollWheelZoom: false });
  map.fitBounds(bounds, { padding: [40, 40] });

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    maxZoom: 19
  }).addTo(map);

  L.marker(base.ll).bindPopup(base.popup).addTo(map);

  pois.forEach(function (p) {
    L.circleMarker(p.ll, {
      radius: 9, color: '#1565c0', fillColor: '#1976d2', fillOpacity: 0.85, weight: 2
    }).bindPopup(p.popup).addTo(map);
  });
})();
</script>

## Activities

| Activity | Notes |
|----------|-------|
| [Titanic Belfast](../activities.md#titanic-belfast) | ⭐ Major attraction — **pre-book**, sells out in summer |
| [SS Nomadic](../activities.md#ss-nomadic) | Titanic's tender ship, adjacent to Titanic Belfast |
| [Game of Thrones Studio Tour](../activities.md#game-of-thrones-studio-tour) | Banbridge, ~40 min drive — ⭐ **pre-book**, £64/family |
| [Ulster Museum](../activities.md#ulster-museum) | Free entry |
| [Ulster Folk Museum](../activities.md#ulster-folk-museum) | Open-air museum, ~20 min from city |
| [W5](../activities.md#w5) | Science centre — great for kids |
| [Belfast Cathedral (St Anne's)](../activities.md#belfast-cathedral-st-annes) | City centre |
| [Belfast Castle](../activities.md#belfast-castle) | Cave Hill, views over city |
| [Carrickfergus Castle](../activities.md#carrickfergus-castle) | ~20 min north — well-preserved Norman castle |

## Day Plan

**Jul 17 afternoon/evening — arrival (transit from Drogheda in [Leg 3](leg-3-northern-ireland.md)):**

| Time | Action |
|------|--------|
| ~13:00 | Arrive Belfast, drop bags at Hampton by Hilton |
| Afternoon | Explore city centre on foot — Cathedral Quarter, St Anne's Cathedral, Victoria Square |
| 15:00+ | Official check-in |
| Evening | Dinner in Belfast — see [Belfast restaurants](../activities.md#restaurants--belfast) |

**Jul 18 — GoT Studio day trip or full Belfast day:**

*Option A — GoT Studio Tour day trip (recommended if pre-booked):*

| Time | Action |
|------|--------|
| ~09:00 | Drive to [Game of Thrones Studio Tour](../activities.md#game-of-thrones-studio-tour) (Banbridge, ~40 min) |
| ~09:40–13:00 | GoT Studio Tour (allow 3–3.5 h) |
| ~13:30 | Return to Belfast (~40 min) |
| Afternoon | [Ulster Museum](../activities.md#ulster-museum) (free, Botanic Gardens area) or city stroll |
| Evening | Cathedral Quarter dinner |

*Option B — Full Belfast day (if GoT is skipped or moved):*

| Time | Action |
|------|--------|
| ~09:00–10:30 | [Belfast Black Cab Tour](../activities.md#belfast-black-cab-tour) — political murals on Falls Rd and Shankill Rd (~1.5 h, £35–50/cab). Highly recommended for adults and older kids (12+). |
| ~10:30–13:00 | [Ulster Folk Museum](../activities.md#ulster-folk-museum) — open-air museum in Cultra, half day |
| ~14:00–17:00 | [W5 Science Centre](../activities.md#w5) — Odyssey complex, beside Titanic Quarter; best Belfast family attraction for kids 5–12 |
| Evening | **Cathedral Quarter** for dinner — The Duke of York, The Dirty Onion, or [Mourne Seafood Bar](../activities.md#restaurants--belfast). Trad sessions from ~9 pm. |

**Jul 19 — full Belfast day:**

| Time | Action |
|------|--------|
| ~09:00–10:30 | [Belfast Black Cab Tour](../activities.md#belfast-black-cab-tour) (if not done Jul 18) — or drive north 20 min to [Carrickfergus Castle](../activities.md#carrickfergus-castle) |
| ~10:30–14:00 | [Titanic Belfast](../activities.md#titanic-belfast) + [SS Nomadic](../activities.md#ss-nomadic) — pre-booked, allow 3–4 h |
| ~14:00–17:00 | [W5 Science Centre](../activities.md#w5) (if not done Jul 18) or [Ulster Museum](../activities.md#ulster-museum) |
| Evening | Cathedral Quarter or Titanic Quarter dinner |

**Jul 20:** Checkout by 11:00 → Carlingford lunch → drive to Leixlip. See [Leg 5](leg-5-leixlip.md).

## Driving Notes

Hampton by Hilton is in Belfast city centre (15 Hope Street, BT12 5EE).  
GoT Studio Tour (Banbridge): ~40 km, ~40 min each way.  
Carrickfergus Castle day trip: ~20 min north.  
Ulster Folk Museum (Cultra): ~15 min east.

## Open Questions

- **GoT Studio Tour:** decide on Jul 17 en-route (if pre-booked for ~12:40 slot) vs Jul 18 day trip. Pre-book — £64/family. See [Leg 3](leg-3-northern-ireland.md) for the en-route option timing.
- **Titanic Belfast:** pre-book — summer peak season, sells out. Include SS Nomadic in the same booking.
- **Black Cab Tour:** book in advance via a local operator (e.g. Original Belfast Black Cab Tours).
- **Cathedral Quarter dinner (Jul 18 or 19):** The Duke of York and Mourne Seafood Bar both benefit from a reservation.
