# Leg 7 — Departure (Jul 22–23)

Final leg. [Premier Inn Dublin Airport](../logistics/premier-inn-dublin-airport.md) · €445.80 · breakfast included. This is the last night together for both families.

<style>
  #map-leg7 { height: 430px; margin: 1.5rem 0; border-radius: 8px; border: 1px solid #e0e0e0; }
  #map-leg7 .leaflet-routing-container { display: none !important; }
</style>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<div id="map-leg7"></div>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://unpkg.com/leaflet-routing-machine@3.2.12/dist/leaflet-routing-machine.min.js"></script>
<script>
(function () {
  var route = [
    { ll: [53.07260, -6.10610], name: 'Druids Glen Resort',         popup: '<b>Druids Glen Resort</b><br>Check-out Jul 22 morning' },
    { ll: [53.42700, -6.23990], name: 'Premier Inn Dublin Airport', popup: '<b>Premier Inn Dublin Airport</b><br>Final night together · Jul 22–23' },
  ];

  var allPts = route.map(function (r) { return r.ll; });
  var bounds = L.latLngBounds(allPts.map(function (ll) { return L.latLng(ll[0], ll[1]); }));

  var map = L.map('map-leg7', { scrollWheelZoom: false });
  map.fitBounds(bounds, { padding: [60, 60] });

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
})();
</script>

## Day Plan

**Jul 22 — arrival from Druids Glen:**

| Time | Action |
|------|--------|
| ~10:45 | Arrive Premier Inn Dublin Airport (from Druids Glen, ~45 min drive) |
| Afternoon | Check in from 14:00; settle in, last afternoon together |
| Evening | Folk dance & traditional Irish food — **book in advance** (research venue near airport or city) |

**Jul 23 — departure day:**

| Time | Action |
|------|--------|
| ~07:00 | Breakfast (included) |
| ~08:30 | Leave hotel — Premier Inn is walking distance or short shuttle to terminal |
| ~09:00 | Airport check-in desks open |
| 11:25 | Madsen depart **FR632** (Ryanair) |
| 12:00 | Wilhelmsen depart **EI164** (Aer Lingus) |

## Open Questions

- Folk dance venue: research traditional music/dance evenings near Dublin Airport or city
