# Leg 3 — Transit to Belfast (Jul 17)

Transit day from Drogheda to Belfast via the [Game of Thrones Studio Tour](../activities.md#game-of-thrones-studio-tour) at Banbridge. Drive north to [Hampton by Hilton Belfast City Centre](../logistics/hampton-by-hilton-belfast.md) — check-in from 15:00. No overnight stop en route.

**Period covered:** Jul 17 (Drogheda checkout, GoT Studio Tour Banbridge, drive to Belfast check-in). Belfast activities from [Leg 4](leg-4-belfast.md).

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
    { ll: [53.71770, -6.34826], name: 'Drogheda (Scholars Townhouse)',      popup: '<b>Scholars Townhouse Hotel</b><br>Check-out Jul 17' },
    { ll: [54.59350, -5.93540], name: 'Belfast (Hampton by Hilton)',         popup: '<b>Hampton by Hilton Belfast City Centre</b><br>Check-in Jul 17 · from 15:00' },
  ];
  var pois = [
    { ll: [54.34780, -6.27820], popup: '<b>Game of Thrones Studio Tour</b><br>Banbridge · ✅ booked · 10:40 shuttle Jul 17' },
    { ll: [54.17640, -6.33940], popup: '<b>Bagenal Castle, Newry</b>' },
    { ll: [54.32700, -5.70090], popup: '<b>Downpatrick</b><br>Contingency · St Patrick\'s Cathedral · Down County Museum' },
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
Drogheda → (M1 north, border crossing) → Newry → Banbridge (GoT Studio) → Belfast
```

Note: border crossing — no passport control but road changes to UK signs and mph speed limits.

## Day Plan

**Jul 17 — transit from Drogheda to Belfast:**

| Time | Action |
|------|--------|
| ~08:45 | Check out Scholars Townhouse, depart north (~90 km, allow ~1 h 15 min incl. border) |
| ~10:25 | Arrive the **ticket-collection / shuttle point** — collect tickets **at least 10 min before** the 10:40 shuttle ([meeting point](https://maps.app.goo.gl/Snw3qDm7aZpRP8fn6)) |
| 10:40 | **Shuttle bus departs to the studio** (~10 min ride) — parking & shuttle are included in the booking |
| ~10:55–14:00 | [Game of Thrones Studio Tour](../activities.md#game-of-thrones-studio-tour) — allow ~3 h (**no audio guides booked**) |
| ~14:40 | Drive to Belfast (~35 km, ~40 min) — drop bags at Hampton by Hilton (check-in from 15:00, luggage storage available) |
| 15:00 | Official check-in |
| Evening | Dinner in Belfast — see [Belfast restaurants](../activities.md#restaurants-belfast) |

📎 **GoT Studio Tour — ✅ booked** (4 adults + 2 children, ref AASVV3TZ): [Booking confirmation](https://drive.google.com/file/d/1BJAkxbUONqkFuemkohVUTXuiWoVfXZCA/view)

## Driving Notes

Drogheda → Banbridge (GoT Studio): ~90 km, ~1 h 15 min. Banbridge → Belfast: ~35 km, ~40 min.

## Contingency

If GoT Studio Tour is unavailable, [Downpatrick](https://maps.google.com/?q=Downpatrick+Northern+Ireland) ([St Patrick's Cathedral](https://maps.google.com/?q=Down+Cathedral+Downpatrick+Northern+Ireland), [Down County Museum](https://maps.google.com/?q=Down+County+Museum+Downpatrick+Northern+Ireland)) is a worthwhile stop on the way.

## Open Questions

- **GoT Studio Tour — ✅ booked.** 10:40 shuttle (the booked time is the *shuttle departure* time, not the tour start). Collect tickets at the [meeting point](https://maps.app.goo.gl/Snw3qDm7aZpRP8fn6) by ~10:25. Parking + shuttle included; no audio guides booked.
- Currency is GBP in Northern Ireland — bring cards.
