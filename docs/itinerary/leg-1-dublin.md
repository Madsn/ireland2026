# Leg 1 — Dublin (Jul 13–16)

3-night base in Dublin city. Both families arrive Jul 13 (~5h apart). [Hendrick Smithfield](../logistics/hendrick-smithfield.md) in Smithfield — €1,634.38 · breakfast included.

<style>
  #map-leg1 { height: 430px; margin: 1.5rem 0; border-radius: 8px; border: 1px solid #e0e0e0; }
</style>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<div id="map-leg1"></div>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
(function () {
  var hotel = { ll: [53.34797, -6.28098], popup: '<b>Hendrick Smithfield</b><br>Base hotel · Jul 13–16 · 3 nights' };
  var pois = [
    { ll: [53.3419, -6.2867], popup: '<b>Guinness Storehouse</b><br>⭐ Pre-book — sells out in summer' },
    { ll: [53.3441, -6.2679], popup: '<b>Dublinia (Viking Museum)</b>' },
    { ll: [53.3472, -6.2641], popup: '<b>National Leprechaun Museum</b><br>Good for kids' },
  ];

  var map = L.map('map-leg1', { scrollWheelZoom: false }).setView([53.345, -6.273], 15);

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

## Arrival Notes

- **Wilhelmsen** arrive Aer Lingus EI80 at 08:10
- **Madsen** arrive Pegasus PC409 at 13:00 (~5h later)
- Wilhelmsen can drop bags / explore Smithfield area during the wait

## Day Plan

| Day | Rough Timing | Plan |
|-----|-------------|------|
| Jul 13 (arrival) | 08:10 Wilhelmsen land · 13:00 Madsen land | Drop bags at hotel, explore Smithfield area together once both families arrive — light afternoon, early dinner |
| Jul 14 | Morning (pre-booked slot) | Guinness Storehouse · afternoon: Dublinia or Leprechaun Museum |
| Jul 15 | Flexible | Remaining Dublin activities; book an evening restaurant |
| Jul 16 | ~10:00 checkout | → Leg 2 departs |

## Activities

| Activity | Notes |
|----------|-------|
| [Dublinia (Viking Museum)](../activities.md#dublinia) | |
| [Guinness Storehouse](../activities.md#guinness-storehouse) | ⭐ Popular — **pre-book** in summer |
| [National Leprechaun Museum](../activities.md#national-leprechaun-museum) | Good for kids |
| ~~Dublin Castle~~ | **CLOSED** — do not plan |

## Driving / Transport

Arriving by plane — no driving needed within Dublin. Public transport or taxi to Smithfield.

## Open Questions

- Guinness Storehouse: pre-book tickets (gets very busy in summer)
- Restaurant bookings for the 3 Dublin evenings?
