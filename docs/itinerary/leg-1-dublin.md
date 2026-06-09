# Leg 1 — Dublin (Jul 13–16)

3-night base in Dublin city. Both families arrive Jul 13 (~5h apart). [Hendrick Smithfield](../logistics/hendrick-smithfield.md) in Smithfield — €1,634.38 · breakfast included.

**Period covered:** Jul 13 (arrival) through Jul 15 evening. Jul 16 checkout + drive to Drogheda opens [Leg 2](leg-2-drogheda.md).

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
- Hotel check-in from ~14:00. **Leave bags at reception on arrival** — both families.

## Day Plan

**Jul 13 — arrival day:**

| Time | Action |
|------|--------|
| 08:10 | Wilhelmsen land. Take the Airlink 747 bus or taxi to Smithfield (~35 min). Leave bags at hotel reception. |
| ~09:00–13:00 | Wilhelmsen wait (~5 h): walk to **Phoenix Park** (~15 min from hotel) — free, vast, deer roam freely; or explore Smithfield Square and the Jameson Distillery quarter |
| 13:00 | Madsen land. Airlink or taxi to Smithfield (~35 min). |
| ~14:00 | Both families check in together |
| Afternoon | Light walk around Smithfield — settle in, recover from travel |
| Evening | **The Cobblestone** (2 min walk, Smithfield) — nightly trad sessions, no cover charge. Casual dinner at The Church Café & Bar or Gallagher's Boxty House |

**Jul 14 — EPIC + Guinness:**

| Time | Action |
|------|--------|
| ~10:00–12:30 | **[EPIC Irish Emigration Museum](https://epicchq.com/)** (Docklands) — interactive, great for all ages; 2–2.5 h. Family ticket (2 adults / 1 child) **€47** — **not yet booked** (×2 for our group of 4 adults + 2 children, ~€94) |
| ~13:00 | Lunch near the Docklands / CHQ, then head to St James's Gate (~20 min) |
| Afternoon (booked slot) | [Guinness Storehouse](../activities.md#guinness-storehouse) — allow 2–2.5 h. **~€132 for the group — needs booking; Jenna will book** |
| Evening | Temple Bar area — **The Brazen Head** (Dublin's oldest pub, nightly music from 9 pm, food all day) or [Gallagher's Boxty House](../activities.md#restaurants-dublin). **Pre-book.** |

**Jul 15 — Viking Dublin + Butlers Chocolate:**

| Time | Action |
|------|--------|
| ~10:00–12:00 | [Dublinia](../activities.md#dublinia) — Viking & medieval Dublin museum. **Not open for July bookings yet (as of Jun 7) — book later.** Christ Church Cathedral exterior (free) is right beside it |
| ~13:00 | Lunch in the city, then head to the Butlers Chocolate Experience (Clonshaugh, ~20 min north) |
| 15:30 | **Butlers Chocolate Experience — factory tour ✅ booked** (4 adults + 2 children, €108, ref D7PKHSRM1). 📎 [Booking confirmation](https://drive.google.com/file/d/1yOhk-hWh8lY8DhFuIEtMIvUYb4cY5tMs/view) |
| Evening | Sit-down dinner — pre-book in advance. Recommendations: [The Winding Stair](../activities.md#restaurants-dublin), [Bison Bar & BBQ](../activities.md#restaurants-dublin), or [Bunsen](../activities.md#restaurants-dublin) for a family-casual option. (Optional earlier: **National Museum – Natural History**, "The Dead Zoo", free) |

**Jul 16:** Checkout ~10:00 → drive to Drogheda. See [Leg 2](leg-2-drogheda.md).

## Activities

| Activity | Notes |
|----------|-------|
| [EPIC Irish Emigration Museum](https://epicchq.com/) | Jul 14 morning — family ticket €47 (2 adults/1 child); **not booked yet** |
| [Guinness Storehouse](../activities.md#guinness-storehouse) | ⭐ Jul 14 afternoon — **needs booking** (~€132); Jenna to book |
| [Dublinia (Viking Museum)](../activities.md#dublinia) | Jul 15 morning — July bookings not open yet (as of Jun 7) |
| Butlers Chocolate Experience | Jul 15 15:30 — ✅ **booked** (€108, ref D7PKHSRM1) |
| National Museum – Natural History | Optional Jul 15 — free, no booking needed |
| [National Leprechaun Museum](../activities.md#national-leprechaun-museum) | Swap in if kids prefer; 15 min walk from hotel |
| ~~Dublin Castle~~ | **CLOSED** — do not plan |

See also: [full Dublin activities & alternatives](../activities.md#leg-1-dublin-jul-1316), including [Dublin trad sessions & restaurants](../activities.md#evening-trad-sessions-irish-dance).

## Driving / Transport

No driving needed in Dublin. Public transport or taxi to Smithfield.

- **Airport → Smithfield:** Airlink 747 bus (€7 pp, ~35 min) or taxi (~€35, ~30 min)
- **Within Dublin:** Luas Red Line (Smithfield stop) and taxis

## Open Questions

- **Guinness Storehouse (Jul 14 afternoon):** ~€132 — **Jenna to book**; July sells out weeks ahead
- **EPIC (Jul 14 morning):** family ticket €47 (2 adults/1 child) — **not booked yet**; ~€94 for our group of 4 adults + 2 children
- **Dublinia (Jul 15 morning):** July bookings weren't open as of Jun 7 — check and book once they open
- **Butlers Chocolate Experience (Jul 15 15:30):** ✅ booked — no action
- **Restaurant bookings:** pre-book The Brazen Head (Jul 14) and a sit-down dinner (Jul 15) — summer Dublin books out 2–3 weeks ahead
