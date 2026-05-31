# Leg 2 — Drogheda (Jul 16–17)

1-night stop in Drogheda. Route: Dublin → coast road north → Ardgillan → Drogheda. [Scholars Townhouse Hotel](../logistics/scholars-townhouse-hotel.md) · €498.00 · breakfast: check booking.

!!! warning "Carrickmacross removed from this leg"
    Carrickmacross Workhouse is 40 km northwest of Drogheda (off the M2), making the Dublin → Ardgillan → Carrickmacross → Drogheda route a 1.5 h round-trip detour in the wrong direction. It has been removed. The Workhouse is worth visiting on a dedicated stop if routing ever goes Dublin → Monaghan, but it does not fit the coast road.

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
    { ll: [53.34797, -6.28098],   name: 'Dublin (start)',       popup: '<b>Dublin — start of leg 2</b><br>Hendrick Smithfield Hotel<br>Check-out Jul 16' },
    { ll: [53.586642, -6.160243], name: 'Ardgillan Castle',     popup: '<b>Ardgillan Castle & Gardens</b><br>En route · free entry to grounds' },
    { ll: [53.7177, -6.34826],    name: 'Drogheda (overnight)', popup: '<b>Scholars Townhouse Hotel</b><br>Check-in Jul 16 · 1 night' },
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
Dublin → Ardgillan Castle (en route, coast road) → Drogheda
```

Dublin → Drogheda: ~50 km, ~1 h via M1 coastal route.

## Day Plan

| Time | Activity | Notes |
|------|----------|-------|
| Morning | Depart Dublin, drive M1 north | Check out Hendrick Smithfield |
| En route | [Ardgillan Castle and Garden](../activities.md#ardgillan-castle-and-garden) | Free entry to grounds · genuinely en route |
| Afternoon | Arrive Drogheda, check in | Millmount is a short walk from town centre — good for the afternoon |
| Evening | [Drogheda Museum (Millmount)](../activities.md#drogheda-museum--millmount) | In-town, walkable |

## Jul 17 Morning (departure day)

⚠️ **Jul 17 is a driving day to Northern Ireland.** One morning activity only before the NI drive.

| Priority | Activity | Notes |
|----------|----------|-------|
| ⭐ Do | [Newgrange / Brú na Bóinne](../activities.md#bru-na-boinne--newgrange) | **Must pre-book** first timed slot (~09:00) — 2–3 h total |
| If time | [Irish Military War Museum](../activities.md#irish-military-war-museum) | Only if Newgrange finishes early |
| Skip | [Old Mellifont Abbey](../activities.md#old-mellifont-abbey) | 12 km west of Drogheda — no time on this leg |

Depart Drogheda by **10:30 at latest** to reach GoT Studio Tour and make Gelilah House's 15:00–18:00 check-in window (see [Leg 3](leg-3-northern-ireland.md)).

## Open Questions

- **Brú na Bóinne must be pre-booked** for summer — book the earliest available slot on Jul 17. Check availability ASAP.
