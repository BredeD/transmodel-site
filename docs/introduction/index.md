# Introduction

Public transport in Europe is delivered by hundreds of authorities and thousands of operators, spread across thirty-plus countries and served by dozens of vendors. Behind the scenes, they all work with the same underlying reality — routes, stops, schedules, fares, passenger journeys — but for a long time each system described that reality in its own way.

Data could move between systems only after custom translation, one integration at a time. Expensive to build. Brittle to maintain. Impossible to scale across borders. Cross-border journey planning, national access points, integrated ticketing — all held back by the same fragmentation.

The Transmodel Ecosystem exists to fix that.

## A family of five standards

The Transmodel Ecosystem is a family of five European public transport data standards. Together they cover the full lifecycle of a service — planning, operating, journey planning, and analysis:

- **Transmodel** — the reference data model. Defines the shared vocabulary of entities, definitions, and relationships that the other standards use.
- **NeTEx** — the XML format for scheduled data (network, stops, timetables, calendars, fares, vehicle scheduling).
- **SIRI** — the XML format for real-time data (vehicle positions, delays, service alerts, facility availability).
- **OJP** — the API for distributed journey planning across borders.
- **OpRa** — the format for observed and historical operational data.

All five are open, maintained under CEN/TC 278 Working Group 3, and designed to work together. Because they share Transmodel's vocabulary, information can flow between them without translation — a *ServiceJourney* published in NeTEx is the same *ServiceJourney* referenced by SIRI.

The details of each standard live in their own top-level sections above. This Introduction covers the ecosystem as a whole — how the standards fit together, how to use them, how they're governed.

![Transmodel as the conceptual data model beneath NeTEx, SIRI, OJP and OpRa](../assets/images/transmodel-cen/governance_fig.3_standards-relate-updated.svg)

## Why this ecosystem matters

- **Interoperability becomes the default**, not something built one integration at a time. Systems from different vendors, different agencies, different countries can exchange data because they refer to the same underlying concepts.
- **Cross-border passenger information becomes practical.** A journey planned in Norway can appear in a Dutch travel app without custom mapping at every hop.
- **The public sector can procure with confidence.** Tenders can require Transmodel-based standards without locking themselves in to any single vendor.
- **The ecosystem is designed to grow.** New modes of transport, new use cases, and new national profiles can be added without breaking what already works.

## In this section

The rest of the Introduction goes deeper on the ecosystem as a whole:

- [How the standards are linked](how-standards-are-linked.md) — the phases of a public transport service and which standard covers each.
- [How to use the standards](how-to-use-the-standards.md) — a high-level guide to where to start, what you need, and what you don't.
- [Governance](governance.md) — CEN, TC 278, WG3, and the process from proposal to published standard.
- [How to contribute](how-to-contribute.md) — paths for raising change requests, contributing to profiles, and joining working groups.
- [NAPCORE](napcore.md) — the coordination programme connecting National Access Points across Europe.
- [Legal context](legal-context.md) — how the standards connect to EU regulations (ITS Directive, MMTIS).
- [History](history.md) — how the ecosystem evolved.

For **team contacts**, see the [Contact](../contact/team.md) tab.
