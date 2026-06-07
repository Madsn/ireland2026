# Leg 2 — Drogheda (Jul 16–17)

1-night stop in Drogheda. Route: Dublin → coast road north → Ardgillan → Newgrange → Drogheda. [Scholars Townhouse Hotel](../logistics/scholars-townhouse-hotel.md) · €498.00 · breakfast: check booking.

**Period covered:** Jul 16 (Dublin checkout, Ardgillan, lunch Skerries, Newgrange afternoon, Drogheda check-in after 17:00). Jul 17 (checkout → GoT Studio Tour Banbridge → Belfast) opens [Leg 3](leg-3-northern-ireland.md).

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
    { ll: [53.69457, -6.44630], popup: '<b>Newgrange / Brú na Bóinne</b><br>⚠️ Must pre-book — afternoon slot Jul 16 (window opens Jun 16)' },
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
Dublin → Ardgillan Castle (coast road) → Skerries (lunch) → Newgrange → Drogheda
```

Dublin → Ardgillan: ~25 km, ~25 min. Ardgillan → Newgrange: ~55 km, ~50 min. Newgrange → Drogheda: ~12 km, ~15 min.

## Day Plan

**Jul 16 — travel day from Dublin:**

| Time | Action |
|------|--------|
| ~09:30 | Check out Hendrick Smithfield |
| ~10:00 | Arrive [Ardgillan Castle and Garden](../activities.md#ardgillan-castle-and-garden) — free grounds, sea views |
| ~10:00–11:00 | Explore Ardgillan grounds |
| ~11:00–12:30 | Lunch at a pub in Skerries village (~5 min from Ardgillan) |
| ~12:30 | Drive to Brú na Bóinne Visitor Centre (~50 min, 55 km) |
| ~13:30 | Arrive — pre-booked afternoon slot at [Brú na Bóinne / Newgrange](../activities.md#bru-na-boinne-newgrange) |
| ~13:30–17:00 | Newgrange visit (2.5–3 h) |
| ~17:15 | Drive 12 km to Drogheda, check in Scholars Townhouse |
| Evening | Dinner in Drogheda · short walk to **St Laurence Gate** (5 min from hotel) and old town walls |

**Jul 17:** Check out → GoT Studio Tour Banbridge (confirmed) → Belfast check-in. See [Leg 3](leg-3-northern-ireland.md).

Other Drogheda activities ([Drogheda Museum (Millmount)](../activities.md#drogheda-museum-millmount), [Irish Military War Museum](../activities.md#irish-military-war-museum), [Old Mellifont Abbey](../activities.md#old-mellifont-abbey)) don't fit in this leg.

## Open Questions

- **Brú na Bóinne must be pre-booked** — book an afternoon slot (targeting ~13:30) on Jul 16. Booking window opens **Jun 16** (9 days away). July slots sell out within hours of release — set a reminder.
