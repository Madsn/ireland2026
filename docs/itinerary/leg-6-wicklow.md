# Leg 6 — Wicklow (Jul 21–22)

1-night at [Druids Glen Resort](../logistics/druids-glen-resort.md) · €454.50 · breakfast included (adults; children €12.50 extra).

**Period covered:** Jul 21 evening (arrival from Emerald Park). Jul 22 morning (checkout, Glendalough, drive to Premier Inn) opens [Leg 7](leg-7-departure.md).

<style>
  #map-leg6 { height: 430px; margin: 1.5rem 0; border-radius: 8px; border: 1px solid #e0e0e0; }
  #map-leg6 .leaflet-routing-container { display: none !important; }
</style>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<div id="map-leg6"></div>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://unpkg.com/leaflet-routing-machine@3.2.12/dist/leaflet-routing-machine.min.js"></script>
<script>
(function () {
  var route = [
    { ll: [53.36370, -6.48400], name: 'Leixlip (Court Yard Hotel)',   popup: '<b>Court Yard Hotel, Leixlip</b><br>Check-out Jul 21' },
    { ll: [53.07260, -6.10610], name: 'Wicklow (Druids Glen Resort)', popup: '<b>Druids Glen Resort</b><br>Check-in Jul 21 from 16:00' },
  ];
  var pois = [
    { ll: [53.51780, -6.57200], popup: '<b>Emerald Park, Ashbourne</b><br>Jul 21 — full day until close ~17:30 · drive direct to Druids Glen' },
    { ll: [53.01140, -6.32780], popup: '<b>Glendalough</b><br>Jul 22 morning — monastic site + Upper Lake trail · 2–3 h · free to walk' },
  ];

  var allPts = route.map(function (r) { return r.ll; }).concat(pois.map(function (p) { return p.ll; }));
  var bounds = L.latLngBounds(allPts.map(function (ll) { return L.latLng(ll[0], ll[1]); }));

  var map = L.map('map-leg6', { scrollWheelZoom: false });
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
Emerald Park (Ashbourne, close ~17:30) → direct drive → Druids Glen Resort (~50 min)
```

## Day Plan

**Jul 21 — arrival from Emerald Park (see [Leg 5](leg-5-leixlip.md)):**

| Time | Action |
|------|--------|
| ~18:30 | Arrive Druids Glen Resort (from Emerald Park, ~50 min drive) |
| Evening | Dinner at **Hugo's Restaurant** — book directly with the resort in advance |

**Jul 22:** Breakfast → checkout → Glendalough → Premier Inn. See [Leg 7](leg-7-departure.md).

## Activities

| Activity | Notes |
|----------|-------|
| [Glendalough](../activities.md#glendalough) | Visited Jul 22 morning — see [Leg 7](leg-7-departure.md) for the day plan |
| [Wicklow Mountains National Park](../activities.md#wicklow-mountains-national-park) | The drive from Druids Glen to Glendalough passes through the national park |
