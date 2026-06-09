# Leg 5 — Wicklow / Druid's Glen (Jul 20–22)

2-night base at [Druid's Glen Resort](../logistics/druids-glen-resort.md), Co. Wicklow (Jul 20–22) · €981 · conf. 6134.713.340 · breakfast included for adults (children's breakfast extra). This new 2-night booking replaced the original 1-night Druid's Glen stay and the cancelled Court Yard, Leixlip.

**Period covered:** Jul 20 evening (arrival from Belfast — the drive is covered at the end of [Leg 4](leg-4-belfast.md)), Jul 21 (golf + relax / Wicklow Mountains), and Jul 22 morning (checkout + one activity on the way to Dublin), which opens [Leg 6](leg-6-departure.md).

<style>
  #map-leg5 { height: 430px; margin: 1.5rem 0; border-radius: 8px; border: 1px solid #e0e0e0; }
</style>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<div id="map-leg5"></div>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
(function () {
  var hotel = { ll: [53.07260, -6.10610], popup: '<b>Druid\'s Glen Resort</b><br>Base · Jul 20–22 · 2 nights' };
  var pois = [
    { ll: [53.01140, -6.32780], popup: '<b>Glendalough</b><br>Wicklow Mountains NP · monastic site + Upper Lake trail' },
    { ll: [53.12460, -6.29640], popup: '<b>Wicklow Mountains National Park</b>' },
    { ll: [53.18460, -6.19000], popup: '<b>Powerscourt House & Gardens</b><br>+ Powerscourt Waterfall nearby' },
    { ll: [53.20260, -6.10110], popup: '<b>Bray</b><br>Seafront, cliff walk, SEA LIFE aquarium' },
    { ll: [52.97890, -6.03400], popup: '<b>Black Castle, Wicklow</b><br>Coastal ruined castle · free' },
  ];

  var allPts = [hotel.ll].concat(pois.map(function (p) { return p.ll; }));
  var bounds = L.latLngBounds(allPts.map(function (ll) { return L.latLng(ll[0], ll[1]); }));

  var map = L.map('map-leg5', { scrollWheelZoom: false });
  map.fitBounds(bounds, { padding: [40, 40] });

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    maxZoom: 19
  }).addTo(map);

  L.marker(hotel.ll).bindPopup(hotel.popup).addTo(map);

  pois.forEach(function (p) {
    L.circleMarker(p.ll, {
      radius: 9, color: '#1565c0', fillColor: '#1976d2', fillOpacity: 0.85, weight: 2
    }).bindPopup(p.popup).addTo(map);
  });
})();
</script>

## Route

Belfast → Druid's Glen (Jul 20): ~210 km, ~2.5–3 h via A1 / M1 / M50 / N11 (optional [Carlingford](../activities.md#carlingford) break just south of the border). The Jul 20 drive itself is in [Leg 4](leg-4-belfast.md).

## Day Plan

**Jul 20 — arrival from Belfast (drive covered in [Leg 4](leg-4-belfast.md)):**

| Time | Action |
|------|--------|
| ~18:00 | Arrive Druid's Glen Resort, check in, settle |
| Evening | Dinner — **Hugo's Restaurant** at the resort (book directly with the resort). *Tentative: we may do Hugo's tonight instead of Jul 21.* |

**Jul 21 — Druid's Glen day:**

| Time | Action |
|------|--------|
| Morning | **Andy & Mikkel: golf** at Druid's Glen |
| Daytime | Everyone else: [Wicklow Mountains National Park](../activities.md#wicklow-mountains-national-park) / [Glendalough](../places/glendalough.md) (~20 min), **or** just relax at the resort (pool, spa, grounds) |
| Evening | **Hugo's Restaurant** dinner (if not done Jul 20) — book directly with the resort |

**Jul 22 — checkout + one activity on the way to Dublin:**

Checkout by 12:00, then pick **one** of these en route to Dublin (the drive to the airport hotel is in [Leg 6](leg-6-departure.md)):

| Option | Notes |
|--------|-------|
| [Wicklow Mountains NP / Glendalough](../places/glendalough.md) | Monastic site + Upper Lake trail; free to walk, parking fee |
| Powerscourt House & Gardens | One of Ireland's great gardens; Powerscourt Waterfall nearby |
| Bray | Seafront + cliff walk, or the SEA LIFE aquarium |
| Zipit Forest Adventures | High-ropes course — if Marius & Martin are feeling brave |
| Black Castle, Wicklow | Coastal ruined castle, free, quick stop |

## Connections

- Lodging: [Druid's Glen Resort](../logistics/druids-glen-resort.md)
- Place: [Glendalough](../places/glendalough.md)
- Next: [Leg 6 — Departure](leg-6-departure.md)
