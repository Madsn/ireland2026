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
  var stops = [
    { ll: [53.34797, -6.28098],   name: 'Dublin (start)',           popup: '<b>Dublin — start of leg 2</b><br>Hendrick Smithfield Hotel<br>Check-out Jul 16' },
    { ll: [53.586642, -6.160243], name: 'Ardgillan Castle',         popup: '<b>Ardgillan Castle & Gardens</b><br>En route · free entry to grounds' },
    { ll: [53.97840, -6.72532],   name: 'Carrickmacross Workhouse', popup: '<b>Carrickmacross Workhouse</b><br>⭐ Must-see for kids · ~30 min detour' },
    { ll: [53.7177, -6.34826],    name: 'Drogheda (overnight)',     popup: '<b>Scholars Townhouse Hotel</b><br>Check-in Jul 16 · 1 night' },
  ];

  var map = L.map('map-leg2', { scrollWheelZoom: false }).setView([53.65, -6.45], 9);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    maxZoom: 19
  }).addTo(map);

  L.Routing.control({
    waypoints: stops.map(function (s) { return L.latLng(s.ll[0], s.ll[1]); }),
    routeWhileDragging: false,
    addWaypoints: false,
    draggableWaypoints: false,
    fitSelectedRoutes: true,
    show: false,
    lineOptions: { styles: [{ color: '#2e7d32', weight: 5, opacity: 0.85 }] },
    createMarker: function (i, wp) {
      return L.marker(wp.latLng, { title: stops[i].name }).bindPopup(stops[i].popup);
    }
  }).addTo(map);

  L.circleMarker([53.694567, -6.4463], {
    radius: 9, color: '#1565c0', fillColor: '#1976d2', fillOpacity: 0.85, weight: 2
  }).bindPopup('<b>Newgrange / Brú na Bóinne Visitor Centre</b><br>⚠️ Must pre-book — sells out in summer').addTo(map);
})();
</script>

## Route

```
Dublin → Ardgillan Castle (en route) → Carrickmacross Workhouse (~30min detour) → Drogheda
```

## Activities

| Stop | Activity | Notes |
|------|----------|-------|
| En route | [Ardgillan Castle and Garden](../places/ardgillan.md) | Free entry to grounds |
| En route | [Carrickmacross Workhouse](../places/carrickmacross.md) | ⭐ **Must see for kids** |
| Drogheda | [Newgrange / Brú na Bóinne](../places/newgrange.md) | ⚠️ **Must pre-book** — sells out in summer |
| Drogheda | Drogheda Museum | |
| Drogheda | Irish Military War Museum | |
| Drogheda | Old Mellifont Abbey | |

## Driving Notes

Dublin → Drogheda: ~45 min (50 km). Don't overload this day — it's also a driving day.

## Open Questions

- **Brú na Bóinne must be pre-booked** for summer. Check availability ASAP.
- Carrickmacross is a ~30 min detour off the main N2/M2 route — worth it per the planning doc.
