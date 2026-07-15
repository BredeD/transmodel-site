# How the standards are linked

The Transmodel family covers five standards that each handle a different phase in the life of a public transport service. Together they cover the full journey — from planning a service to observing what actually happened.

## The phases

Each standard has a distinct job:

- **Planning the service** → published as **NeTEx** (network, stops, timetables, calendars, fares, vehicle scheduling).
- **Running the service in real time** → observed through **SIRI** (vehicle positions, delays, cancellations, service alerts, facility availability).
- **Answering "how do I get there?"** → **OJP** queries across operators and country borders.
- **Learning from what happened** → **OpRa** (historical, observed operational data for analysis).

Underpinning all four exchange standards is the **[Transmodel](../standards/transmodel/index.md)** conceptual model — the shared vocabulary of entities, definitions, and relationships that every exchange standard implements.

## Why the common conceptual model matters

Because all four exchange standards share Transmodel underneath, the same concepts translate across them. A *ServiceJourney* in NeTEx means the same thing as a *ServiceJourney* referenced by SIRI. An *Operator* in NeTEx is the same *Operator* returned by an OJP journey plan. A stop planned in NeTEx is the stop being monitored in SIRI.

This is what makes it practical for information to flow between the phases without custom translation at each step.

## What each standard covers, in one line

| Standard | Type of data | Typical use case |
| --- | --- | --- |
| [Transmodel](../standards/transmodel/index.md) | Conceptual model | The reference every exchange standard is built on |
| [NeTEx](../standards/netex/index.md) | Scheduled / static | Publish timetables, stops, fares to a National Access Point |
| [SIRI](../standards/siri/index.md) | Real-time | Feed live vehicle positions, delays, alerts to passenger information systems |
| [OJP](../standards/ojp/index.md) | Journey planning API | Query journey plans across borders without a central data warehouse |
| [OpRa](../standards/opra/index.md) | Observed / historical | Analyse what actually happened for KPI reporting and improvement |
