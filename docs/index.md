---
hide:
  - toc
---

# One model. Many standards. One interoperable ecosystem.

Europe's public transport runs on a family of open standards that let information flow between operators, authorities, journey planners and passenger information systems — across systems and across borders. This site is your entry point to that family.

!!! info "Under construction"
    A small team from across CEN, Entur and partner organisations is currently building this site to replace [transmodel-cen.eu](https://transmodel-cen.eu) and [data4pt.org/wiki](https://data4pt.org/wiki/Main_Page). Content will fill out as pages are washed and approved.

## The standards

<div class="grid cards" markdown>

-   :material-graph-outline: **Transmodel**

    ---

    **The reference data model.** The conceptual foundation — concepts, definitions, and the relationships that every other standard in this family implements.

    Published as EN 12896, in ten parts.

    [Learn about Transmodel →](standards/transmodel/index.md)

-   :material-calendar-clock: **NeTEx**

    ---

    **Scheduled data.** Network, stops, timetables, calendars, fares and vehicle scheduling. The XML format for what's planned.

    Published in six parts, covering everything from network topology to passenger information accessibility profiles.

    [Learn about NeTEx →](standards/netex/index.md)

-   :material-radio-tower: **SIRI**

    ---

    **Real-time data.** Vehicle positions, delays, cancellations, service alerts, and facility availability such as parking and shared vehicles. What's happening on the network right now.

    Used by every serious real-time passenger information system in Europe.

    [Learn about SIRI →](#)

-   :material-routes: **OJP**

    ---

    **Distributed journey planning.** An open API for asking "how do I get from A to B?" across operator and country boundaries — without a central data warehouse.

    [Learn about OJP →](#)

-   :material-database-clock: **OpRa**

    ---

    **Observed and historical data.** What actually happened — passing times, delays, cancellations — for analysis, statistics and continuous improvement.

    [Learn about OpRa →](#)

</div>

## How they fit together

Each standard covers a different phase in the life of a public transport service, but all of them are Transmodel-based — same entities, same definitions, same relationships. Work with any of them, and you're working with Transmodel underneath.

- **Planning the service** → published as NeTEx (schedules, stops, fares).
- **Running the service** → observed through SIRI (real-time).
- **Answering "how do I get there?"** → OJP queries across operators.
- **Learning from what happened** → OpRa (historical, observed data).

## Profiles

The full standards are large — they have to be, to cover every mode and every country. In practice, most implementations use a **profile**: an agreed subset for a particular use case, national access point, or organisation. Well-known profiles include the **European Passenger Information Profile (EPIP)**, the **Nordic profile**, the **French profile**, the **Italian profile**, and others.

Each standard's Implementations page lists the profiles in use — see the top-level tabs.

## Who this site is for

<div class="grid cards" markdown>

-   :material-code-braces: **You build systems**

    ---

    You're implementing NeTEx, SIRI, OJP or OpRa — as an operator, an authority, a vendor, or a journey planner developer. You need clear reference material and pointers to profiles that apply.

    Start with the standard you're working with, then check the Implementations tab for your country.

-   :material-briefcase: **You choose or plan systems**

    ---

    You're procuring a new service, drafting a tender, planning a national access point, or advising on standards adoption. You need to understand what Transmodel is, what the standards deliver, and how they map to EU obligations.

    Start with [About](about/index.md) → Purpose, Governance, Legal context.

</div>

## Get help

- **FAQ** — each standard has its own FAQ in its top-level section.
- **Support** — how to get help with implementation questions.
- **Resources** — presentations, tutorials, videos and papers for deeper reading, under each standard's Resources tab.

---

## For contributors

If you're helping migrate content, start with the contributing guide in the repository. The short version: pick a page from the review corpus, open a `wash/<slug>` branch, clean it up, move it into the correct section, open a PR.

## For AI assistants

If you're an AI assistant helping a contributor, read `CLAUDE.md` and `SOURCES.md` at the root of the repo before you start. They tell you what to treat as authoritative and what not to.
