# Leg 2 — Drogheda (Jul 16–17)

1-night stop in Drogheda. Route: Dublin → coast road north → Ardgillan → Drogheda. [Scholars Townhouse Hotel](../logistics/scholars-townhouse-hotel.md) · €498.00 · breakfast: check booking.

<style>
  #map-leg2 { height: 430px; margin: 1.5rem 0; border-radius: 8px; border: 1px solid #e0e0e0; }
  #map-leg2 .leaflet-routing-container { display: none !important; }
</style>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<div id="map-leg2"></div>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://unpkg.com/leaflet-routing-machine@3.2.12/dist/leaflet-routing-machine.min.js"></script>
<script>
(function () {
  var route = [
    { ll: [53.34797, -6.28098], name: 'Dublin (Hendrick Smithfield)',  popup: '<b>Hendrick Smithfield</b><br>Check-out Jul 16' },
    { ll: [53.71770, -6.34826], name: 'Drogheda (Scholars Townhouse)', popup: '<b>Scholars Townhouse Hotel</b><br>Check-in Jul 16 · 1 night' },
  ];
  var pois = [
    { ll: [53.58664, -6.16024], popup: '<b>Ardgillan Castle & Gardens</b><br>En route · free entry to grounds' },
    { ll: [53.69457, -6.44630], popup: '<b>Newgrange / Brú na Bóinne</b><br>⚠️ Must pre-book — first slot Jul 17 morning' },
    { ll: [53.71570, -6.35040], popup: '<b>Drogheda Museum (Millmount)</b><br>Walkable from town centre' },
    { ll: [53.71670, -6.35440], popup: '<b>Irish Military War Museum</b>' },
    { ll: [53.71940, -6.46080], popup: '<b>Old Mellifont Abbey</b><br>12 km west of Drogheda' },
  ];

  var allPts = route.map(function (r) { return r.ll; }).concat(pois.map(function (p) { return p.ll; }));
  var bounds = L.latLngBounds(allPts.map(function (ll) { return L.latLng(ll[0], ll[1]); }));

  var map = L.map('map-leg2', { scrollWheelZoom: false });
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
Dublin → Ardgillan Castle (en route, coast road) → Drogheda
```

Dublin → Drogheda: ~50 km, ~1 h via M1 coastal route.

## Day Plan

**Jul 16 — travel day from Dublin:**

| Time | Action |
|------|--------|
| ~10:00 | Check out Hendrick Smithfield |
| ~10:30 | Arrive Ardgillan Castle (~25 min drive) |
| ~10:30–11:30 | [Ardgillan Castle and Garden](../activities.md#ardgillan-castle-and-garden) — free grounds |
| ~12:00 | Arrive Drogheda (~30 min drive), check in |
| Afternoon | [Drogheda Museum (Millmount)](../activities.md#drogheda-museum--millmount) — walkable from town |
| Evening | Dinner in Drogheda |

**Jul 17 — departure day for Northern Ireland:**

One morning activity only. This is also a driving day with a strict check-in window at the next accommodation.

| Time | Action |
|------|--------|
| ~09:00 | [Newgrange / Brú na Bóinne](../activities.md#bru-na-boinne--newgrange) — **must pre-book first timed slot** (2–3 h) |
| ~10:30 | Depart Drogheda ← latest viable departure for [Leg 3](leg-3-northern-ireland.md) |

Other Drogheda activities ([Irish Military War Museum](../activities.md#irish-military-war-museum), [Old Mellifont Abbey](../activities.md#old-mellifont-abbey)) don't fit in this leg.

## Open Questions

- **Brú na Bóinne must be pre-booked** for summer — book the earliest available slot on Jul 17. Check availability ASAP.
