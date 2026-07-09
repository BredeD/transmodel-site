# Purpose

Public transport services rely increasingly on information systems to keep operations running and to give passengers accurate, accessible information. Behind the scenes, those systems do a lot of very different jobs: setting schedules and timetables, managing vehicle fleets and driving personnel, defining who is entitled to travel and validating their tickets, publishing real-time updates when things change, and calculating the best trip for a passenger based on their preferences.

Each of those jobs used to be handled by systems that spoke their own language. Data would move between them only after custom translation — expensive to build, brittle to maintain, and impossible to scale across borders.

Transmodel exists to fix that.

## What Transmodel does

Transmodel — the short name for the European Standard **EN 12896, Public Transport Reference Data Model** — is a common data model for the whole public transport domain. It gives every one of those systems the same vocabulary: matching entity definitions, matching structures, matching meanings.

That common vocabulary makes interoperability possible on two levels:

- **Within an organisation.** A scheduling system, a fleet management system, and a ticketing system, all built by different vendors, can exchange data because they refer to the same underlying concepts.
- **Between organisations.** A public authority and a transport operator, or two operators, or an operator and a journey planner, can integrate their data because they aren't guessing about what each other means.

![](../assets/images/transmodel-cen/I7BSAO1KT8-1-768x512-1.jpg)

## Why it matters

Transmodel provides a framework for defining and agreeing data models across the whole area of public transport. That has practical consequences:

- **Interoperability becomes the default**, not something built one integration at a time.
- **Operators, authorities and software suppliers can work together more easily** — they're starting from a shared model instead of negotiating one for every project.
- **Future systems have room to grow.** Because Transmodel covers the whole domain rather than a single use case, extensions and new applications can be added without breaking what already works.

The concrete implementations that carry Transmodel data between systems — [NeTEx](../standards/netex/index.md) for schedules, [SIRI](../standards/siri/index.md) for real-time, [OJP](../standards/ojp/index.md) for journey planning, [OpRa](../standards/opra/index.md) for observed data — are all derived from it. Working with any of them means working with Transmodel underneath.
