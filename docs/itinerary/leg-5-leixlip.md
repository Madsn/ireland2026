# Leg 5 — Leixlip / Emerald Park (Jul 20–21)

Originally planned as a Donegal leg — replaced with Leixlip to be close to Emerald Park. [Court Yard Hotel, Leixlip](../logistics/courtyard-leixlip.md) · €388.80 · breakfast included.

<style>
  #map-leg5 { height: 430px; margin: 1.5rem 0; border-radius: 8px; border: 1px solid #e0e0e0; }
  #map-leg5 .leaflet-routing-container { display: none !important; }
</style>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<div id="map-leg5"></div>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://unpkg.com/leaflet-routing-machine@3.2.12/dist/leaflet-routing-machine.min.js"></script>
<script>
(function () {
  var route = [
    { ll: [54.58200, -5.93000], name: 'Belfast (Ormeau Park Residence)', popup: '<b>Ormeau Park Residence</b><br>Check-out Jul 20 before 10:00' },
    { ll: [53.36370, -6.48400], name: 'Leixlip (Court Yard Hotel)',      popup: '<b>Court Yard Hotel, Leixlip</b><br>Check-in Jul 20 from 16:00' },
  ];
  var pois = [
    { ll: [54.04220, -6.18670], popup: '<b>Carlingford</b><br>Medieval harbour village · Norman castle ruins · lunch stop en route' },
    { ll: [53.51780, -6.57200], popup: '<b>Emerald Park, Ashbourne</b><br>Jul 21 · leave by 15:00 for Druids Glen check-in' },
  ];

  var allPts = route.map(function (r) { return r.ll; }).concat(pois.map(function (p) { return p.ll; }));
  var bounds = L.latLngBounds(allPts.map(function (ll) { return L.latLng(ll[0], ll[1]); }));

  var map = L.map('map-leg5', { scrollWheelZoom: false });
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
Belfast (Ormeau Park, checkout before 10:00) → ~2h drive south → Leixlip
```

Belfast → Leixlip: ~2 h (165 km via A1/M1). See [Leg 4](leg-4-belfast.md) for the Carlingford lunch stop on this drive.

## Day Plan

**Jul 20 — arrival from Belfast:** *(see [Leg 4](leg-4-belfast.md) for full drive timing)*

| Time | Action |
|------|--------|
| ~16:00 | Check in Court Yard Hotel, Leixlip |
| Evening | **Book Emerald Park tickets online for Jul 21** — 20% discount if booked night before |

**Jul 21 — Emerald Park day:**

| Time | Action |
|------|--------|
| ~09:30 | Breakfast (included) |
| ~10:00 | Drive to Emerald Park, Ashbourne (~25 min) |
| ~10:30–15:00 | [Emerald Park](../activities.md#emerald-park) |
| **15:00** | ⚠️ **Depart by 15:00** — 1 h 15 min drive to Glendalough en route to Druids Glen |

## Key Action: Emerald Park Tickets

⚠️ **Book on July 20 for July 21** to get the 20% early-booking discount. Drive from hotel to Emerald Park (Ashbourne): ~25 min.

## Connections

- Place: [Emerald Park](../places/emerald-park.md) · [Activity details](../activities.md#emerald-park)
- Next: [Wicklow Leg](leg-6-wicklow.md)
