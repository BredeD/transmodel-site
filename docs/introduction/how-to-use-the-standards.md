# Using the standards

A public transport service moves through four phases, and each has a matching standard.

| Phase | Question the phase answers | Standard |
| --- | --- | --- |
| **Planning the service** | What runs when, where, at what price? | **NeTEx** |
| **Running the service** | Where is it right now, and is anything unusual happening? | **SIRI** |
| **Helping a passenger get somewhere** | How do I get from A to B, across operators and borders? | **OJP** |
| **Learning from what happened** | Did it run as planned, and what should we improve? | **OpRa** |

Underneath all four sits **[Transmodel](../standards/transmodel/index.md)** — the conceptual model that gives every one of them the same vocabulary. When your technical team says "Transmodel underneath", they mean the shared definitions that make information from one standard translate cleanly into another.

## Shared vocabulary in practice

A *ServiceJourney* published in NeTEx is the same *ServiceJourney* that SIRI reports on in real time. The *Operator* running that journey is the same *Operator* the journey planner names in OJP. The stop being planned is the stop being monitored is the stop being counted in the after-the-fact analysis.

That is what lets a passenger see one journey when the data behind it comes from many organisations. It is also what lets an authority procure four systems from four suppliers and have them talk to each other without custom integration work.

## Which standard do I need?

- Scheduled data (routes, stops, timetables, fares) → **NeTEx**
- Real-time data (vehicle positions, delays, alerts) → **SIRI**
- A journey planning API that talks to other planners → **OJP**
- Observed or historical operational data for analysis → **OpRa**

If your problem obviously matches one phase, that standard is the answer. If it spans several phases — a passenger-facing app, a national platform, a large tender — you use several standards together. That's the whole point of the shared model underneath.

You don't choose Transmodel as an alternative to the four exchange standards. Every one of them implements Transmodel; whenever you work with NeTEx, SIRI, OJP or OpRa, you're already working with Transmodel underneath.

## Formal specifications and open resources

The formal Technical Specifications for NeTEx, SIRI, OJP and OpRa are published by CEN and can be purchased through national standardization bodies. That is the right choice when you need an authoritative reference to cite in a tender document, regulatory filing or academic work.

Alongside the published specifications, the same material — schemas, examples and national profile documentation — is available in open GitHub repositories. For day-to-day implementation, most time is spent there rather than in the printed PDF.

## Where the technical detail lives

Each standard has its own section on this site:

- [Transmodel](../standards/transmodel/index.md) — the conceptual model
- [NeTEx](../standards/netex/index.md) — scheduled data
- [SIRI](../standards/siri/index.md) — real-time data
- [OJP](../standards/ojp/index.md) — distributed journey planning
- [OpRa](../standards/opra/index.md) — observed operational data

Each standard's page lists its national profiles and where their authoritative documentation lives.

## Where to get help

- Start with the standard's **FAQ page** — many common questions live there.
- For Nordic-specific NeTEx questions, the [Nordic profile documentation](https://github.com/entur/nordic-netex-documentation) is authoritative.
- For French-specific questions, the [French national portal](https://normes.transport.data.gouv.fr/) is authoritative.
- Deeper implementation guidance lives in the parallel [NeTEx Guides project](https://github.com/TransmodelEcosystem/NeTEx-Guides-Documentation).
- For questions that don't have a home yet, see [Contact](../contact/team.md).
