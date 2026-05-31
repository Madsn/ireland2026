# Leg 4 — Belfast / Ulster (Jul 18–20)

2-night Belfast base at [Ormeau Park Residence](../logistics/ormeau-park-residence.md) · £729.10 · 4-bed house · no meals included. Checkout before 10:00 on Jul 20.

**Period covered:** Jul 18 (arrival from Gelilah House + Titanic afternoon) and Jul 19 (full Belfast day). Jul 20 morning checkout + Carlingford drive opens [Leg 5](leg-5-leixlip.md).

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
  var route = [
    { ll: [54.24760, -6.25260], name: 'Gelilah House (Loughbrickland)',  popup: '<b>Gelilah House</b><br>Check-out Jul 18' },
    { ll: [54.58200, -5.93000], name: 'Belfast (Ormeau Park Residence)', popup: '<b>Ormeau Park Residence</b><br>Check-in Jul 18 · 2 nights' },
  ];
  var pois = [
    { ll: [54.60760, -5.91070], popup: '<b>Titanic Belfast</b><br>⭐ Must pre-book — sells out in summer' },
    { ll: [54.60710, -5.91080], popup: '<b>SS Nomadic</b><br>Titanic\'s tender ship · adjacent to Titanic Belfast' },
    { ll: [54.58470, -5.93400], popup: '<b>Ulster Museum</b><br>Free entry' },
    { ll: [54.62920, -5.79390], popup: '<b>Ulster Folk Museum</b><br>Open-air museum · ~20 min from city' },
    { ll: [54.60870, -5.90940], popup: '<b>W5 Science Centre</b><br>Great for kids' },
    { ll: [54.60140, -5.92890], popup: '<b>Belfast Cathedral (St Anne\'s)</b><br>City centre' },
    { ll: [54.62600, -5.96300], popup: '<b>Belfast Castle</b><br>Cave Hill · views over city' },
    { ll: [54.71550, -5.80760], popup: '<b>Carrickfergus Castle</b><br>~20 min north · well-preserved Norman castle' },
  ];

  var allPts = route.map(function (r) { return r.ll; }).concat(pois.map(function (p) { return p.ll; }));
  var bounds = L.latLngBounds(allPts.map(function (ll) { return L.latLng(ll[0], ll[1]); }));

  var map = L.map('map-leg4', { scrollWheelZoom: false });
  map.fitBounds(bounds, { padding: [40, 40] });

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    maxZoom: 19
  }).addTo(map);

  L.Routing.control({
    waypoints: route.map(function (s) { return L.latLng(s.ll[0], s.ll[1]); }),
    routeWhileDragging: false,
    addWaypoints: false,
    draggableWaypoints: false,
    fitSelectedRoutes: false,
    show: false,
    lineOptions: { styles: [{ color: '#2e7d32', weight: 5, opacity: 0.85 }] },
    createMarker: function (i, wp) {
      return L.marker(wp.latLng, { title: route[i].name }).bindPopup(route[i].popup);
    }
  }).addTo(map);

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
| [Ulster Museum](../activities.md#ulster-museum) | Free entry |
| [Ulster Folk Museum](../activities.md#ulster-folk-museum) | Open-air museum, ~20 min from city |
| [W5](../activities.md#w5) | Science centre — great for kids |
| [Belfast Cathedral (St Anne's)](../activities.md#belfast-cathedral-st-annes) | City centre |
| [Belfast Castle](../activities.md#belfast-castle) | Cave Hill, views over city |
| [Carrickfergus Castle](../activities.md#carrickfergus-castle) | ~20 min north — well-preserved Norman castle |

## Day Plan

**Jul 18 — arrival from Gelilah House (checkout covered in [Leg 3](leg-3-northern-ireland.md)):**

| Time | Action |
|------|--------|
| ~11:30 | Arrive Belfast, drop luggage at Ormeau Park Residence |
| ~12:00–16:00 | [Titanic Belfast](../activities.md#titanic-belfast) + [SS Nomadic](../activities.md#ss-nomadic) (pre-booked, allow 3–4 h) |
| Evening | Settle in, dinner — see [Belfast restaurants](../activities.md#restaurants--belfast) |

**Jul 19 — full day Belfast:**

| Time | Action |
|------|--------|
| ~09:00–10:30 | Optional: [Belfast Black Cab Tour](../activities.md#belfast-black-cab-tour) — political murals on the Falls Rd and Shankill Rd (~1.5 h, £35–50/cab, city centre pick-up). Highly recommended for adults and older kids (12+). |
| ~09:00 (alternative) | Drive 20 min north to [Carrickfergus Castle](../activities.md#carrickfergus-castle) — Norman castle on the lough shore, 45 min–1 h walk-around. Then continue toward Cultra. |
| ~10:30–13:00 | [Ulster Folk Museum](../activities.md#ulster-folk-museum) — open-air museum in Cultra, half day; costumed interpreters, farmhouses, forge |
| ~14:00–17:00 | [W5 Science Centre](../activities.md#w5) — Odyssey complex, beside Titanic Quarter; best Belfast family attraction for kids 5–12 |
| Evening | **Cathedral Quarter** for dinner — try [The Duke of York](../activities.md#trad-sessions-outside-dublin), The Dirty Onion, or [Mourne Seafood Bar](../activities.md#restaurants--belfast). Trad music sessions some nights from ~9 pm. |

**Jul 20:** Checkout before 10:00 → Carlingford lunch → drive to Leixlip. See [Leg 5](leg-5-leixlip.md).

## Driving Notes

Gelilah House → Belfast: ~30 min.  
Carrickfergus Castle is a short day trip (20 min north of Belfast city).

## Open Questions

- **Titanic Belfast:** pre-book — summer peak season, sells out. Include SS Nomadic in the same booking.
- **Black Cab Tour:** book in advance via a local operator (e.g. Original Belfast Black Cab Tours). Decide whether Jul 19 morning or an alternative start for the day.
- **Cathedral Quarter dinner (Jul 19):** The Duke of York and Mourne Seafood Bar both benefit from a reservation — book ahead.
