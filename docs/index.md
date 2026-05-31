# Ireland Trip 2026

Two families (Madsen + Wilhelmsen) traveling together through Ireland, July 13–23, 2026 (10 nights). All 7 legs booked. Original Donegal leg replaced with Leixlip/Emerald Park stop.

<style>
  #map-overview { height: 520px; margin: 1.5rem 0; border-radius: 8px; border: 1px solid #e0e0e0; }
</style>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<div id="map-overview"></div>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
(function () {
  // Hotels in leg order — connected by green polyline
  var hotels = [
    { ll: [53.34797, -6.28098], popup: '<b>Leg 1 — Hendrick Smithfield, Dublin</b><br>Jul 13–16 · 3 nights' },
    { ll: [53.71770, -6.34826], popup: '<b>Leg 2 — Scholars Townhouse, Drogheda</b><br>Jul 16–17 · 1 night' },
    { ll: [54.24760, -6.25260], popup: '<b>Leg 3 — Gelilah House, Loughbrickland</b><br>Jul 17–18 · check-in 15:00–18:00' },
    { ll: [54.58200, -5.93000], popup: '<b>Leg 4 — Ormeau Park Residence, Belfast</b><br>Jul 18–20 · 2 nights' },
    { ll: [53.36370, -6.48400], popup: '<b>Leg 5 — Court Yard Hotel, Leixlip</b><br>Jul 20–21 · 1 night' },
    { ll: [53.07260, -6.10610], popup: '<b>Leg 6 — Druids Glen Resort, Wicklow</b><br>Jul 21–22 · 1 night' },
    { ll: [53.42700, -6.23990], popup: '<b>Leg 7 — Premier Inn Dublin Airport</b><br>Jul 22–23 · 1 night' },
  ];

  // Planned activities ✅
  var planned = [
    // Leg 1 — Dublin
    { ll: [53.3415, -6.2862], popup: '<b>Guinness Storehouse</b> · Leg 1 · ⭐ pre-book' },
    { ll: [53.3438, -6.2697], popup: '<b>Dublinia (Viking Museum)</b> · Leg 1' },
    { ll: [53.3472, -6.2641], popup: '<b>National Leprechaun Museum</b> · Leg 1' },
    // Leg 2 — Drogheda
    { ll: [53.5866, -6.1602], popup: '<b>Ardgillan Castle & Gardens</b> · Leg 2 · en route' },
    { ll: [53.9784, -6.7253], popup: '<b>Carrickmacross Workhouse</b> · Leg 2' },
    { ll: [53.6946, -6.4463], popup: '<b>Newgrange / Brú na Bóinne</b> · Leg 2 · ⭐ pre-book' },
    { ll: [53.7182, -6.3576], popup: '<b>Drogheda Museum (Millmount)</b> · Leg 2' },
    { ll: [53.7212, -6.3498], popup: '<b>Irish Military War Museum</b> · Leg 2' },
    { ll: [53.7400, -6.4600], popup: '<b>Old Mellifont Abbey</b> · Leg 2' },
    // Leg 3 — Northern Ireland
    { ll: [54.3478, -6.2782], popup: '<b>Game of Thrones Studio Tour</b> · Leg 3 · ⭐ pre-book' },
    { ll: [54.1764, -6.3394], popup: '<b>Bagenal Castle, Newry</b> · Leg 3' },
    { ll: [54.3239, -5.6315], popup: '<b>Downpatrick</b> · Leg 3 · contingency' },
    // Leg 4 — Belfast
    { ll: [54.6076, -5.9093], popup: '<b>Titanic Belfast</b> · Leg 4 · ⭐ pre-book' },
    { ll: [54.6084, -5.9098], popup: '<b>SS Nomadic</b> · Leg 4' },
    { ll: [54.5725, -5.9326], popup: '<b>Ulster Museum</b> · Leg 4 · free' },
    { ll: [54.6292, -5.7939], popup: '<b>Ulster Folk Museum (Cultra)</b> · Leg 4' },
    { ll: [54.6061, -5.9123], popup: '<b>W5 Science Centre</b> · Leg 4' },
    { ll: [54.5977, -5.9293], popup: '<b>Belfast Cathedral (St Anne\'s)</b> · Leg 4' },
    { ll: [54.5971, -5.9735], popup: '<b>Belfast Castle</b> · Leg 4' },
    { ll: [54.7154, -5.8066], popup: '<b>Carrickfergus Castle</b> · Leg 4' },
    // Leg 5 — Leixlip
    { ll: [53.5178, -6.5720], popup: '<b>Emerald Park, Ashbourne</b> · Leg 5 · ⭐ book on Jul 20 for 20% off' },
    // Leg 6 — Wicklow
    { ll: [53.0114, -6.3278], popup: '<b>Glendalough</b> · Leg 6' },
    { ll: [53.1246, -6.2964], popup: '<b>Wicklow Mountains National Park</b> · Leg 6' },
  ];

  // Plan B / alternative activities 🔄
  var planb = [
    // Leg 1
    { ll: [53.3434, -6.2641], popup: '<b>World of Illusion</b> · Leg 1 · Plan B' },
    { ll: [53.3432, -6.2686], popup: '<b>Chester Beatty Library</b> · Leg 1 · Plan B · free' },
    { ll: [53.3375, -6.2598], popup: '<b>National Museum — Archaeology</b> · Leg 1 · Plan B · free' },
    { ll: [53.3479, -6.2610], popup: '<b>Dream Point Experience</b> · Leg 1 · Plan B' },
    { ll: [53.3433, -6.2656], popup: '<b>The Ark</b> · Leg 1 · Plan B' },
    { ll: [53.3877, -6.3663], popup: '<b>Aquazone National Aquatic Centre</b> · Leg 1 · Plan B · Blanchardstown' },
    // Leg 2
    { ll: [53.7176, -6.3456], popup: '<b>Funtasia Drogheda</b> · Leg 2 · Plan B' },
    { ll: [53.6894, -6.3745], popup: '<b>Battle of the Boyne (Oldbridge)</b> · Leg 2 · Plan B' },
    { ll: [54.0297, -6.1885], popup: '<b>Carlingford</b> · Leg 2/5 · Plan B · lunch stop' },
    { ll: [53.7189, -6.1845], popup: '<b>Laytown / Bettystown Beach</b> · Leg 2 · Plan B' },
    // Leg 3
    { ll: [54.1913, -5.9043], popup: '<b>Tollymore Forest Park</b> · Leg 3 · Plan B · GoT filming location' },
    { ll: [54.1295, -6.4374], popup: '<b>Slieve Gullion Forest Park</b> · Leg 3 · Plan B' },
    { ll: [54.1069, -6.1966], popup: '<b>Narnia Trail, Kilbroney Park</b> · Leg 3 · Plan B · Rostrevor' },
    { ll: [54.3852, -5.5542], popup: '<b>Delamont Country Park</b> · Leg 3 · Plan B · Strangford Lough' },
    // Leg 4
    { ll: [54.5975, -5.9700], popup: '<b>Belfast Black Cab Tour</b> · Leg 4 · Plan B · Falls Road' },
    { ll: [54.5733, -5.9331], popup: '<b>Botanic Gardens</b> · Leg 4 · Plan B · free' },
    { ll: [54.6070, -5.9110], popup: '<b>Titanic Quarter Self-Guided Walk</b> · Leg 4 · Plan B · free' },
    { ll: [54.5974, -5.9285], popup: '<b>Lost City Adventure Golf</b> · Leg 4 · Plan B' },
    { ll: [54.3597, -5.5664], popup: '<b>Exploris Aquarium (Portaferry)</b> · Leg 4 · Plan B' },
    { ll: [54.3634, -5.6098], popup: '<b>Mount Stewart (National Trust)</b> · Leg 4 · Plan B' },
    { ll: [54.6217, -5.9624], popup: '<b>Cave Hill Country Park</b> · Leg 4 · Plan B' },
    // Leg 5
    { ll: [53.3645, -6.4896], popup: '<b>St Catherine\'s Park, Leixlip</b> · Leg 5 · Plan B · beside hotel' },
    { ll: [53.3591, -6.4434], popup: '<b>Fort Lucan Adventureland</b> · Leg 5 · Plan B' },
    { ll: [53.3863, -6.5892], popup: '<b>Clonfert Pet Farm, Maynooth</b> · Leg 5 · Plan B' },
    { ll: [53.3017, -6.7559], popup: '<b>Kildare Maze (Prosperous)</b> · Leg 5 · Plan B' },
    { ll: [53.3513, -6.3105], popup: '<b>Dublin Zoo & Phoenix Park</b> · Leg 5 · Plan B' },
    // Leg 6
    { ll: [53.1701, -6.1933], popup: '<b>Powerscourt Estate & Gardens</b> · Leg 6 · Plan B' },
    { ll: [52.8607, -6.2017], popup: '<b>Avoca Handweavers</b> · Leg 6 · Plan B' },
    { ll: [52.8617, -6.1962], popup: '<b>Vale of Avoca — Meeting of the Waters</b> · Leg 6 · Plan B' },
    { ll: [52.9811, -6.0452], popup: '<b>Wicklow Gaol</b> · Leg 6 · Plan B' },
    { ll: [53.1976, -6.0966], popup: '<b>Bray Seafront & Cliff Walk</b> · Leg 6 · Plan B' },
    { ll: [53.1695, -6.1920], popup: '<b>Powerscourt Distillery</b> · Leg 6 · Plan B' },
  ];

  var allPts = hotels.map(function (h) { return h.ll; })
    .concat(planned.map(function (p) { return p.ll; }))
    .concat(planb.map(function (p) { return p.ll; }));
  var bounds = L.latLngBounds(allPts.map(function (ll) { return L.latLng(ll[0], ll[1]); }));

  var map = L.map('map-overview', { scrollWheelZoom: false });
  map.fitBounds(bounds, { padding: [30, 30] });

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    maxZoom: 19
  }).addTo(map);

  // Route polyline
  L.polyline(hotels.map(function (h) { return h.ll; }), {
    color: '#2e7d32', weight: 3, opacity: 0.8
  }).addTo(map);

  // Hotel markers
  hotels.forEach(function (h) {
    L.marker(h.ll).bindPopup(h.popup).addTo(map);
  });

  // Planned activity markers
  planned.forEach(function (p) {
    L.circleMarker(p.ll, {
      radius: 7, color: '#1565c0', fillColor: '#1976d2', fillOpacity: 0.85, weight: 2
    }).bindPopup(p.popup).addTo(map);
  });

  // Plan B activity markers
  planb.forEach(function (p) {
    L.circleMarker(p.ll, {
      radius: 5, color: '#546e7a', fillColor: '#78909c', fillOpacity: 0.6, weight: 1.5
    }).bindPopup(p.popup).addTo(map);
  });
})();
</script>

<p style="font-size: 0.8em; color: #666; margin: -0.5rem 0 1.5rem;">
  📍 Hotel &nbsp;·&nbsp;
  <span style="display:inline-block;width:10px;height:10px;background:#1976d2;border-radius:50%;vertical-align:middle;margin-right:3px;"></span>Planned activity &nbsp;·&nbsp;
  <span style="display:inline-block;width:8px;height:8px;background:#78909c;border-radius:50%;vertical-align:middle;margin-right:3px;"></span>Plan B / alternative
</p>

## Key Findings

- All 7 accommodation legs confirmed and booked.
- **Critical pre-bookings still needed:** Brú na Bóinne/Newgrange, GoT Studio Tour, Titanic Belfast, Guinness Storehouse.
- **Book Emerald Park on July 20** for July 21 visit — 20% early-booking discount.
- Early checkout alerts: Gelilah House before 11:00 on Jul 18; Ormeau Park before 10:00 on Jul 20.
- Accommodation total: approx. **€4,664** (GBP converted at ~1.18).

## Trip at a Glance

| Leg | Dates | Location | Hotel | Breakfast | Cost |
|-----|-------|----------|-------|-----------|------|
| 1 | Jul 13–16 | Dublin | [Hendrick Smithfield](logistics/hendrick-smithfield.md) | ✅ | €1,634.38 |
| 2 | Jul 16–17 | Drogheda | [Scholars Townhouse](logistics/scholars-townhouse-hotel.md) | — | €498.00 |
| 3 | Jul 17–18 | Northern Ireland | [Gelilah House](logistics/gelilah-house.md) | ❌ | £324 |
| 4 | Jul 18–20 | Belfast | [Ormeau Park Residence](logistics/ormeau-park-residence.md) | ❌ | £729.10 |
| 5 | Jul 20–21 | Leixlip | [Court Yard Hotel](logistics/courtyard-leixlip.md) | ✅ | €388.80 |
| 6 | Jul 21–22 | Wicklow | [Druids Glen Resort](logistics/druids-glen-resort.md) | ✅ | €454.50 |
| 7 | Jul 22–23 | Dublin Airport | [Premier Inn](logistics/premier-inn-dublin-airport.md) | ✅ | €445.80 |

## Flights

| Family | Direction | Flight | Time |
|--------|-----------|--------|------|
| Wilhelmsen | Arrive Dublin | Aer Lingus EI80 | 08:10, Jul 13 |
| Madsen | Arrive Dublin | Pegasus PC1157 | 13:00, Jul 13 |
| Wilhelmsen | Depart Dublin | Aer Lingus EI164 | 12:00, Jul 23 |
| Madsen | Depart Dublin | Ryanair FR632 | 11:25, Jul 23 |

## Action Items

- [ ] **Book Emerald Park tickets** on July 20 for July 21 (20% off)
- [ ] Pre-book: Brú na Bóinne/Newgrange · GoT Studio Tour · Titanic Belfast · Guinness Storehouse
- [ ] Book Hugo's Restaurant at Druids Glen directly with hotel
- [ ] Notify Ormeau Park Residence of expected arrival time (required)

**Shared map:** https://maps.app.goo.gl/GKdBy42FMzYMUj9b8
