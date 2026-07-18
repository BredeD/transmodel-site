# Purpose

Public transport in Europe is delivered by hundreds of authorities and thousands of operators, spread across thirty-plus countries and served by dozens of vendors. Behind the scenes, they all work with the same underlying reality — routes, stops, schedules, fares, passenger journeys — but for a long time each system described that reality in its own way.

Data could move between systems only after custom translation, one integration at a time. Expensive to build. Brittle to maintain. Impossible to scale across borders. Cross-border journey planning, national access points, integrated ticketing — all held back by the same fragmentation.

The Transmodel Ecosystem exists to fix that.

## A family of standards, built on one shared model

At the heart of the ecosystem is **Transmodel** (EN 12896) — a conceptual reference data model that defines the vocabulary, entities, and relationships of the public transport domain. Every other standard in the family is built on this common foundation.

Around it sit four exchange standards:

- **NeTEx** for scheduled data (network, stops, timetables, calendars, fares, vehicle scheduling)
- **SIRI** for real-time data (vehicle positions, delays, alerts, facility availability)
- **OJP** for distributed journey planning APIs
- **OpRa** for observed and historical operational data

Each covers a different phase in the life of a public transport service, and because they all share Transmodel's vocabulary, information can flow between them without translation. A *ServiceJourney* published in NeTEx is the same *ServiceJourney* referenced by SIRI. An *Operator* returned by an OJP query is the same *Operator* known to the scheduling system.

For an overview of which standard handles what, see [How the standards are linked](how-standards-are-linked.md).

![](../assets/images/transmodel-cen/I7BSAO1KT8-1-768x512-1.jpg)

## Why this matters

- **Interoperability becomes the default**, not something built one integration at a time. Systems from different vendors, different agencies, different countries can exchange data because they refer to the same underlying concepts.
- **Cross-border passenger information becomes practical.** A journey planned in Norway can appear in a Dutch travel app without custom mapping at every hop.
- **The public sector can procure with confidence.** Tenders can require Transmodel-based standards without locking themselves in to any single vendor.
- **The ecosystem is designed to grow.** New modes of transport, new use cases, and new national profiles can be added without breaking what already works.

The rest of this section explains [how the standards work together](how-standards-are-linked.md), [how to use them](how-to-use-the-standards.md), and how the whole family is [governed](governance.md) and [coordinated across Europe](napcore.md).
