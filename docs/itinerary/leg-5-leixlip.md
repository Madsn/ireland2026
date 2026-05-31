# Leg 5 — Leixlip / Emerald Park (Jul 20–21)

Originally planned as a Donegal leg — replaced with Leixlip to be close to Emerald Park. [Court Yard Hotel, Leixlip](../logistics/courtyard-leixlip.md) · €388.80 · breakfast included.

**Period covered:** Jul 20 (Belfast checkout, Carlingford lunch, Leixlip arrival) and Jul 21 (Emerald Park full day + evening drive to Druids Glen). Jul 21 evening arrival at Druids Glen opens [Leg 6](leg-6-wicklow.md).

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
    { ll: [53.51780, -6.57200], popup: '<b>Emerald Park, Ashbourne</b><br>Jul 21 · arrive at open ~10:00 · stay until close ~17:30 · drive direct to Druids Glen' },
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
Belfast (Ormeau Park, checkout before 10:00) → A1/M1 south → Carlingford (lunch) → Leixlip
```

Belfast → Leixlip direct: ~2 h (165 km). With Carlingford stop: allow ~3.5–4 h total.

## Day Plan

**Jul 20 — transit from Belfast (Belfast checkout covered in [Leg 4](leg-4-belfast.md)):**

| Time | Action |
|------|--------|
| Before 10:00 | Checkout Ormeau Park Residence |
| ~10:00 | Drive south (~2 h via A1/M1) |
| ~12:00–13:30 | Lunch: **[Carlingford](../activities.md#carlingford)** — medieval harbour village on the Cooley Peninsula, Norman castle ruins (King John's Castle), views across to the Mourne Mountains. Directly on the route. |
| ~14:30 | Continue south (~45 min to Leixlip) |
| ~16:00 | Check in Court Yard Hotel, Leixlip |
| Evening | **Book Emerald Park tickets online tonight** (20% early-booking discount). Quiet rest evening — optional short walk in [St Catherine's Park](../activities.md#st-catherines-park) beside the hotel. |

**Jul 21 — Emerald Park full day:**

| Time | Action |
|------|--------|
| ~09:00 | Breakfast (included at hotel) |
| ~09:30 | Drive to Emerald Park, Ashbourne (~25 min) |
| ~10:00 | **Arrive Emerald Park at opening** — maximize time in the park |
| ~10:00 until close (~17:30) | [Emerald Park](../activities.md#emerald-park) — full day; no departure constraint, stay until closing |
| ~18:30 | Drive direct from Emerald Park to Druids Glen Resort (~50 min via N2/M50/N11) |
| ~19:15 | Check in Druids Glen Resort → [Leg 6](leg-6-wicklow.md) |

## Key Action: Emerald Park Tickets

⚠️ **Book on the evening of July 20** to get the 20% early-booking discount. Verify Emerald Park's opening and closing times when booking — summer hours are typically 10:00–17:30 but confirm on their website.

## Connections

- Place: [Emerald Park](../places/emerald-park.md) · [Activity details](../activities.md#emerald-park)
- Carlingford lunch: [Activity details](../activities.md#carlingford)
- Next: [Leg 6 — Wicklow](leg-6-wicklow.md)
