# NeTEx (SG9)

**NeTEx** (**Ne**twork **T**imetable **Ex**change) is the CEN Technical Standard for exchanging *scheduled* public transport data — network, stops, timetables, calendars, fares and vehicle scheduling — between different computer systems in a way that lets that data flow across organisational, geographical or administrative borders without custom translation.

It is a direct implementation of the [Transmodel](../../about/index.md) conceptual data model, expressed as a set of W3C XML schemas.

!!! tip "Watch a short introduction"
    A [3-minute overview video](https://youtu.be/KXSI-iRuNfc) covers what NeTEx is and where it fits.

## What NeTEx is

NeTEx has been developed under the CEN standardisation process (Comité Européen de Normalisation) as the most recent stage of more than fifteen years of European work to harmonise passenger information data. It provides:

- A **conceptual foundation** — the same entities and relationships defined by Transmodel.
- A **W3C XML schema** — a formal, machine-readable specification of what a valid NeTEx document looks like.
- A **UML data model** — the conceptual model in visual form, available for design tools.
- **Example XML documents** — reference implementations covering different data sets.
- **Documentation and guidelines** — practical use-case guides being developed in parallel at [TransmodelEcosystem/NeTEx-Guides-Documentation](https://github.com/TransmodelEcosystem/NeTEx-Guides-Documentation) *(under construction)*.

Because NeTEx is a standard rather than a proprietary format, data can move between systems from different vendors and different countries without bespoke integrations. This is what makes cross-border journey planning, national access points, and multi-operator ticketing practical.

The NeTEx schema is freely usable under a GPL licence and its development is controlled by the CEN standards process. Source, XSDs and examples live in the [NeTEx CEN GitHub repository](https://github.com/NeTEx-CEN/NeTEx).

## The six parts of NeTEx

NeTEx is divided into six parts, each covering a specific subset of the CEN Transmodel for public transport information:

| Part | Scope | CEN reference |
| --- | --- | --- |
| Part 1 | Public transport network topology | CEN/TS 16614-1:2014 |
| Part 2 | Scheduled timetables | CEN/TS 16614-2:2014 |
| Part 3 | Fare information | CEN/TS 16614-3:2015 |
| Part 4 | European Passenger Information Profile (EPIP) | CEN/TS 16614-4:2017 |
| Part 5 | Alternative modes exchange format | CEN/TS 16614-5:2022 |
| Part 6 | European Passenger Information Accessibility Profile (EPIAP) | CEN/TS 16614-6:2024 |

All six parts share the same framework — reusable components, versioning mechanisms, validity conditions, global identifier rules — defined in Part 1.

## What NeTEx can exchange

The NeTEx schema is designed for the efficient, updatable exchange of complex transport data. In practical terms, a NeTEx dataset can carry:

- **Network** — lines, routes and journey patterns with complex topology (circular routes, cloverleaf and lollipop patterns, short workings, express variants).
- **Stops** — stop places, quays, and physical infrastructure, including accessibility information for passengers with restricted mobility.
- **Timetables** — service journeys with departure times and frequencies. Composite journeys are supported, e.g. trains that merge or split.
- **Calendars** — day types, operating periods, exceptions and public holidays.
- **Fares** — structures (flat, point-to-point, zonal), products (single, return, day pass, season), and prices valid on specific dates.
- **Vehicle scheduling** — blocks, positioning runs, garages, layovers, and vehicle-to-journey assignments.
- **Operators and organisations** — the responsibility structure behind the service.
- **Alternative modes** — car sharing, cycle sharing, rental and pooling, covered by Part 5.
- **Versioned data** — with management metadata that allows updates to propagate across distributed systems.

!!! note "Alternative modes in practice"
    NeTEx Part 5 and SIRI's Facility Monitoring service cover alternative modes within the Transmodel family. Alongside these, many countries and cities have chosen to use **GBFS** (General Bikeshare Feed Specification) — often combined with **TOMP** (Transport Operator Mobility-as-a-Service Provider) and **MDS** (Mobility Data Specification) — for e-scooters, shared bikes and car sharing. GBFS covers the MMTIS passenger-information use cases for these modes, and MDS, adopted by most European cities to regulate street use by these mobility forms, covers a regulatory use case currently out of scope for NeTEx and SIRI. Adoption of one path or the other is a national and local decision.

    A [canonical mapping between GBFS and NeTEx](../../assets/files/Canonical_mapping_-_NeTEx_and_SIRI_new_modes_with_GBFS.pdf) exists to help bridge the two approaches where needed.

## How NeTEx is used

Data in NeTEx format is encoded as XML documents that must conform exactly to the schema. Conformance can be checked automatically by standard XML validators. The schema can also be used to generate language bindings so that software can produce and consume NeTEx documents without manually writing parsing code.

A NeTEx service only needs to implement the elements that are relevant to its business objectives — the schema is designed so that extraneous elements can be ignored. Parties using NeTEx for a particular purpose typically define a **profile** to specify which elements must be present and which code sets to use. Before defining a new profile, check whether an existing one (Nordic, EPIP, French, Italian, and others) already fits your use case — reusing an established profile saves effort and improves interoperability.

### Exchange between systems

NeTEx documents are XML files and can be exchanged by any protocol that carries files — HTTP, FTP, email, portable media. The dominant pattern in practice is **publication documents**: bulk exchange of complete datasets (for example, all the timetables for an operator), typically published on a schedule and ingested by downstream systems.

## Profiles

The full NeTEx schema is large — deliberately so, because it must model the entire public transport domain across many countries and modes. In practice, no individual implementation uses the whole schema. A **profile** is an agreed subset: which elements must be present, which are optional, which code sets to use, and how identifiers should be structured.

Profiles exist at three levels:

- **European profiles** — such as [EPIP](#the-european-passenger-information-profile-epip) for basic passenger information, and EPIAP for accessibility. These are agreed at CEN level.
- **National profiles** — most countries with a National Access Point have defined a profile. The Nordic countries share the **Nordic profile**; France, Italy, Germany, the Netherlands, Switzerland, the UK and others have their own.
- **Organisational profiles** — some large operators or authorities layer additional constraints on top of a national profile.

Work is ongoing at CEN/TC 278, in collaboration with **NAPCORE** (the coordination programme for European National Access Points), to align the various national profiles into a **single EU-wide NeTEx profile** — motivated in part by MMTIS's requirement for smooth cross-border data flow. Progress will be reflected on the [Implementations](implementations.md) page as it moves through the standards process.

See [Implementations](implementations.md) for the full inventory of published NeTEx profiles.

### The European Passenger Information Profile (EPIP)

The idea behind EPIP is straightforward: if every member state publishes NeTEx data on their National Access Point using the same profile, then journey planners can consume data from any of them without country-specific handling.

An **EPIP-adapted version of the NeTEx XML schema** exists. It also has a **simplified variant** without constraint checks, produced because the official NeTEx schema is too large for some code generation tools (notably C#) to handle. The simplified variant is compliant with the main schema but is intended for application development, not validation.

Documentation and schema live in the [NeTEx EPIP profile repository](https://github.com/NeTEx-CEN/NeTEx-Profile-EPIP).

### The Nordic profile

The Nordic NeTEx profile is one of the largest deployed profiles by volume, used by the Nordic countries. It is documented at [entur/nordic-netex-documentation](https://github.com/entur/nordic-netex-documentation), which this site treats as an authoritative reference.

Unlike most other national profiles — which are typically scoped to MMTIS journey-planning requirements — the Nordic profile covers additional user needs such as operational information and train composition. This is what lets Nordic public transport authorities (PTAs) and operators (PTOs) use NeTEx to build **shared datasets** for their internal data flows as well — from planning systems into real-time information systems, into ticketing systems, and across the different vendors each authority works with. The same dataset then serves MMTIS obligations, internal operations and third-party use without duplication.

!!! todo "Other national profiles"
    This overview covers EPIP and Nordic as illustrative examples. The [Implementations](implementations.md) page — currently a stub — will hold short descriptions and links for the other published national profiles: French, Italian, Swiss, Dutch, Belgian, Portuguese, Slovenian, Austrian, Croatian, Danish, Czech, UK, Irish, Australian and others.

## Software and tools

An ecosystem of open-source and commercial NeTEx tools exists — XML editors and validators, converters (**NeTEx→GTFS** being the most common conversion direction), language bindings for Java, C# and others, editing and management platforms, journey planning engines, and planning systems with native NeTEx export.

See **[Software & tools](../tools.md)** for the current inventory.

## References

- **[NeTEx CEN GitHub](https://github.com/NeTEx-CEN/NeTEx)** — the canonical source of XSD schemas, examples and supporting documentation.
- **[NeTEx EPIP profile GitHub](https://github.com/NeTEx-CEN/NeTEx-Profile-EPIP)** — schema and documentation for the European Passenger Information Profile.
- **[NeTEx website](https://netex-cen.eu/)** — the CEN-hosted portal for NeTEx.
- **[Nordic profile documentation](https://github.com/entur/nordic-netex-documentation)** — trusted reference for the Nordic profile.
- **[DATA4PT wiki](https://data4pt.org/wiki/Main_Page)** — legacy site being replaced by this one; still useful for historical context.
