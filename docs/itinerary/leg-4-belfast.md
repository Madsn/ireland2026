# Leg 4 — Belfast (Jul 17–20)

3-night Belfast base at [Hampton by Hilton Belfast City Centre](../logistics/hampton-by-hilton-belfast.md) · £1,167.88 (2 rooms) · breakfast included ✅. Check-in from 15:00 on Jul 17; checkout by 11:00 on Jul 20.

**Period covered:** Jul 17 afternoon/evening (arrival from Drogheda — transit covered in [Leg 3](leg-3-northern-ireland.md)), Jul 18–19 (two full Belfast days), Jul 20 (checkout, W5 in the morning, then drive south to Druid's Glen) opens [Leg 5](leg-6-wicklow.md).

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
    { ll: [55.24080, -6.51160], popup: '<b>Giant\'s Causeway</b><br>Jul 19 option · Causeway Coast · ~1 h each way' },
    { ll: [54.34780, -6.27820], popup: '<b>Game of Thrones Studio Tour</b><br>Banbridge · visited Jul 17 en route from Drogheda' },
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
| [Titanic Belfast](../activities.md#titanic-belfast) + [SS Nomadic](../activities.md#ss-nomadic) | ✅ **booked Jul 18 09:40** (4 adults + 2 children, + 6 multimedia guides) |
| [W5](../activities.md#w5) | Science centre — **Jul 20 morning**; great for kids 5–12 |
| [Giant's Causeway](https://maps.google.com/?q=Giant%27s+Causeway) | Jul 19 option — Causeway Coast day trip (~1 h each way); stones free |
| [Belfast Black Cab Tour](../activities.md#belfast-black-cab-tour) | Jul 18 afternoon option — political murals, ~1.5 h |
| [Ulster Museum](../activities.md#ulster-museum) | Free entry — Jul 18/19 option |
| [Ulster Folk Museum](../activities.md#ulster-folk-museum) | Open-air museum, ~15 min from city — Jul 19 option |
| [Belfast Cathedral (St Anne's)](../activities.md#belfast-cathedral-st-annes) | City centre — Jul 19 option |
| [Belfast Castle](../activities.md#belfast-castle) | Cave Hill, views over city — Jul 19 option |
| [Carrickfergus Castle](../activities.md#carrickfergus-castle) | ~20 min north — well-preserved Norman castle — Jul 19 option |

## Day Plan

**Jul 17 afternoon/evening — arrival (transit from Drogheda via GoT Studio in [Leg 3](leg-3-northern-ireland.md)):**

| Time | Action |
|------|--------|
| ~14:25 | Arrive Belfast, drop bags at Hampton by Hilton |
| Afternoon | Explore city centre on foot — Cathedral Quarter, St Anne's Cathedral, Victoria Square |
| 15:00+ | Official check-in |
| Evening | Dinner in Belfast — see [Belfast restaurants](../activities.md#restaurants-belfast) |

**Jul 18 — Titanic Belfast:**

| Time | Action |
|------|--------|
| 09:40 | **[Titanic Belfast](../activities.md#titanic-belfast) ✅ booked** (4 adults + 2 children, ref WPMATHZG) + [SS Nomadic](../activities.md#ss-nomadic). **Multimedia guides booked (6).** Allow 3–4 h. 📎 [Booking confirmation](https://drive.google.com/file/d/1NiEtquiNvUekIC0fgT2cI0GF4IZHiB0a/view) |
| ~13:30 | Lunch in the Titanic Quarter |
| Afternoon | [Belfast Black Cab Tour](../activities.md#belfast-black-cab-tour) (political murals, ~1.5 h) **or** [Ulster Museum](../activities.md#ulster-museum) (free) / Cathedral Quarter walk. *(W5 is saved for Jul 20 — it's right next door to Titanic but we're not doing both the same day.)* |
| Evening | **Cathedral Quarter** dinner — The Duke of York, The Dirty Onion, or [Mourne Seafood Bar](../activities.md#restaurants-belfast). Trad sessions from ~9 pm. |

**Jul 19 — open day (pick from these — none need advance booking):**

| Option | Notes |
|--------|-------|
| **Giant's Causeway day trip** | The big day out — ~1 h each way along the Causeway Coast. Stones free; visitor centre + parking paid. Allow a full day |
| [Carrickfergus Castle](../activities.md#carrickfergus-castle) | ~20 min north — well-preserved Norman castle |
| [Ulster Folk Museum](../activities.md#ulster-folk-museum) | Open-air living-history museum, Cultra (~15 min) |
| [Ulster Museum](../activities.md#ulster-museum) | Free; Botanic Gardens right beside it |
| [Belfast Castle](../activities.md#belfast-castle) | Cave Hill — views over the city |
| [Belfast Cathedral (St Anne's)](../activities.md#belfast-cathedral-st-annes) | City centre |

Evening: Cathedral Quarter or Titanic Quarter dinner.

**Jul 20 — W5, then drive south to Druid's Glen:**

| Time | Action |
|------|--------|
| By 11:00 | Checkout Hampton by Hilton (store luggage at the hotel) |
| ~10:30–14:30 | [W5 Science Centre](../activities.md#w5) — Odyssey complex, beside the Titanic Quarter; best Belfast attraction for kids 5–12 |
| ~15:00 | Collect luggage and **drive south to [Druid's Glen Resort](../logistics/druids-glen-resort.md), Co. Wicklow** (~2.5–3 h; optional lunch / leg-stretch at [Carlingford](../activities.md#carlingford) just south of the border) |
| Evening | Arrive Druid's Glen → [Leg 5](leg-6-wicklow.md) |

## Driving Notes

Hampton by Hilton is in Belfast city centre (15 Hope Street, BT12 5EE).  
Carrickfergus Castle day trip: ~20 min north.  
Ulster Folk Museum (Cultra): ~15 min east.

## Open Questions

- **Titanic Belfast:** ✅ booked Jul 18 09:40 (incl. SS Nomadic + 6 multimedia guides) — no action.
- **Giant's Causeway (Jul 19 option):** the stones need no booking; book visitor-centre/parking on the day or skip.
- **Black Cab Tour (Jul 18 afternoon option):** book in advance via a local operator (e.g. Original Belfast Black Cab Tours).
- **Cathedral Quarter dinner (Jul 18 or 19):** The Duke of York and Mourne Seafood Bar both benefit from a reservation.
