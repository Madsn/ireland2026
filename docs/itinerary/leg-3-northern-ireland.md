# Leg 3 — Northern Ireland (Jul 17–18)

First Northern Ireland night. [Gelilah House](../logistics/gelilah-house.md) villa near Loughbrickland · £324 · no meals included — budget for food. Narrow check-in window: 15:00–18:00.

<style>
  #map-leg3 { height: 430px; margin: 1.5rem 0; border-radius: 8px; border: 1px solid #e0e0e0; }
  #map-leg3 .leaflet-routing-container { display: none !important; }
</style>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<div id="map-leg3"></div>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://unpkg.com/leaflet-routing-machine@3.2.12/dist/leaflet-routing-machine.min.js"></script>
<script>
(function () {
  var route = [
    { ll: [53.71770, -6.34826], name: 'Drogheda (Scholars Townhouse)',   popup: '<b>Scholars Townhouse Hotel</b><br>Check-out Jul 17' },
    { ll: [54.24760, -6.25260], name: 'Loughbrickland (Gelilah House)', popup: '<b>Gelilah House</b><br>Check-in Jul 17 · 15:00–18:00 window' },
  ];
  var pois = [
    { ll: [54.17640, -6.33940], popup: '<b>Bagenal Castle, Newry</b>' },
    { ll: [54.34780, -6.27820], popup: '<b>Game of Thrones Studio Tour</b><br>⭐ £64/family · must pre-book<br>Arrive ~12:40 · depart ~15:40' },
    { ll: [54.32700, -5.70090], popup: '<b>Downpatrick</b><br>Contingency if GoT Studio unavailable<br>St Patrick\'s Cathedral · Down County Museum' },
  ];

  var allPts = route.map(function (r) { return r.ll; }).concat(pois.map(function (p) { return p.ll; }));
  var bounds = L.latLngBounds(allPts.map(function (ll) { return L.latLng(ll[0], ll[1]); }));

  var map = L.map('map-leg3', { scrollWheelZoom: false });
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

## Route

```
Drogheda → (M1 north, border crossing) → Newry/Downpatrick area → Gelilah House
```

Note: border crossing — no passport control but road changes to UK signs and mph speed limits.

## Activities

| Activity | Notes |
|----------|-------|
| [Bagenal Castle, Newry](../activities.md#bagenal-castle-newry) | |
| [Game of Thrones Studio Tour](../activities.md#game-of-thrones-studio-tour) | ⭐ £64/family for general admission — **must pre-book** |

## Day Plan

**Jul 17 — transit day from Drogheda:**

| Time | Action |
|------|--------|
| 09:00 | Newgrange first timed slot (see [Leg 2](leg-2-drogheda.md)) |
| ~11:30 | Depart Drogheda north (~85 km, ~1 h 10 min) |
| ~12:40 | Arrive GoT Studio Tour (Banbridge) |
| ~15:40 | Depart (~10 km south to Gelilah House) |
| ~15:55 | Check in Gelilah House ✓ — within 15:00–18:00 window |

No slack in this schedule — do not add stops.

**Jul 18 — drive to Belfast:**

| Time | Action |
|------|--------|
| 08:00–11:00 | Checkout Gelilah House (checkout window) |
| ~30 min | Drive to Belfast |
| Morning | Arrive Belfast — drop luggage at Ormeau Park, head to Titanic Quarter |

## Driving Notes

Drogheda → GoT Studio Tour (Banbridge): ~85 km, ~1 h 10 min.  
GoT Studio Tour → Gelilah House (Loughbrickland): ~10 km south (~15 min). Banbridge is only 10 km north of the accommodation.

## Contingency

GoT Studio Tour is the anchor here — if unavailable, [Downpatrick](https://maps.google.com/?q=Downpatrick+Northern+Ireland) ([St Patrick's Cathedral](https://maps.google.com/?q=Down+Cathedral+Downpatrick+Northern+Ireland), [Down County Museum](https://maps.google.com/?q=Down+County+Museum+Downpatrick+Northern+Ireland)) is nearby.

## Open Questions

- GoT Studio Tour: check availability for Jul 17. Pre-book — £64/family.
- Currency is GBP in Northern Ireland — bring cards.
