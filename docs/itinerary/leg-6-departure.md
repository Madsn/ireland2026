# Leg 6 — Departure (Jul 22–23)

Final leg. [Premier Inn Dublin Airport](../logistics/premier-inn-dublin-airport.md) · €445.80 · breakfast included. This is the last night together for both families.

**Period covered:** Jul 22 (Druid's Glen checkout + one Wicklow activity en route — see [Leg 5](leg-5-wicklow.md), arrive Premier Inn, folk evening) and Jul 23 (departures).

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
    { ll: [53.07260, -6.10610], name: 'Druids Glen Resort',         popup: '<b>Druids Glen Resort</b><br>Check-out Jul 22 ~10:00' },
    { ll: [53.01140, -6.32780], name: 'Glendalough',                popup: '<b>Glendalough</b><br>Jul 22 morning · monastic site + Upper Lake trail · ~2 h' },
    { ll: [53.42700, -6.23990], name: 'Premier Inn Dublin Airport', popup: '<b>Premier Inn Dublin Airport</b><br>Final night together · Jul 22–23 · arrive ~14:00' },
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

**Jul 22 — Wicklow activity, then arrive Premier Inn:**

| Time | Action |
|------|--------|
| ~08:30 | Breakfast at Druid's Glen (children: €12.50 extra per child) |
| ~10:00 | Checkout Druid's Glen (by 12:00) |
| Late morning | **Chosen Jul 22 activity en route** — pick from the options in [Leg 5](leg-5-wicklow.md). If Glendalough: ~20 min from the resort, allow 2–2.5 h ([Glendalough](../activities.md#glendalough) — Round Tower, monastic ruins, Upper Lake trail; free to walk, parking fee) |
| ~13:00 | Drive to Premier Inn Dublin Airport (~55 min via N11/M50) |
| ~14:00 | Check in Premier Inn — check-in from 14:00, near-perfect timing |
| Afternoon | Settle in; last afternoon together |
| Evening | **Traditional Irish music evening** — see below |

**Jul 23 — departure day:**

| Time | Action |
|------|--------|
| ~07:00 | Breakfast (included) |
| ~08:00 | Leave hotel — Premier Inn is a short walk to the terminal |
| ~08:30 | Airport — allow time for bag drop, security, and getting to gates |
| 11:25 | Madsen depart **FR632** (Ryanair) → **Terminal 1** |
| 12:00 | Wilhelmsen depart **EI164** (Aer Lingus) → **Terminal 2** |

!!! note "Terminals"
    Dublin Airport has two adjacent terminals — T1 (Ryanair) and T2 (Aer Lingus). They are connected by a short indoor walkway. Both families can check in together before separating at the gates.

## Traditional Music Evening (Jul 22)

**Recommended: [The Cobblestone](https://www.cobblestonepub.ie/), Smithfield** — nightly trad sessions, no cover charge, starts ~9 pm. Ironically the same pub a 2-min walk from the Leg 1 hotel. Taxi from Premier Inn Dublin Airport: ~25 min, ~€25–30 each way.

Alternatives:
- **[O'Donoghue's](https://www.odonoghues.ie/)**, Merrion Row — nightly trad from 8 pm, walk-ins welcome, famous venue
- **[Irish Dance Party, Merchants Arch](../activities.md#evening-trad-sessions-irish-dance)** — family-friendly 2-hour show (3–5 pm slot — fits better as an afternoon option if departing for dinner after)
- **[Celtic Nights, Arlington Hotel](../activities.md#evening-trad-sessions-irish-dance)** — trad show + 3-course dinner, book ahead; closer to city centre than airport

For any city-centre venue, use a taxi or rideshare both ways (hotel → venue → hotel) — do not drive after an evening out.
