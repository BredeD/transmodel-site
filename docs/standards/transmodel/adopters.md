# Transmodel — Adopters

Because Transmodel is a conceptual model and not a file format or an API, no one "installs" it. Instead it is adopted indirectly, through the standards and systems that build on it. In practice, this means that **every organisation using NeTEx, SIRI, OJP or OpRa is also a Transmodel adopter** — their systems share the same vocabulary, definitions and relationships that Transmodel defines.

This page describes the three ways Transmodel is adopted today, and points to where the concrete lists live.

## Three ways to adopt Transmodel

### 1. Through the four exchange standards

This is by far the most common form of adoption. Every public transport authority, operator, journey planner and vendor that uses one of the Transmodel-derived standards is working with Transmodel underneath — whether they think of it that way or not.

For who uses what, the detailed inventories live on each standard's own page:

- [**NeTEx — Implementations**](../netex/implementations.md) — national profile inventory (currently covers Austria, Belgium, Croatia, Czech Republic, Denmark, France, Ireland, Italy, Netherlands, Nordic, Portugal, Slovenia, Switzerland, UK)
- [**SIRI — Implementations**](../siri/implementations.md) — real-time operator and authority deployments
- [**OJP — Implementations**](../ojp/implementations.md) — distributed journey planning deployments
- [**OpRa — Implementations**](../opra/implementations.md) — observed-data pilots

NeTEx is being actively developed and deployed across Europe. Coordination between national efforts remains uneven, however — much of the work happens country by country, often without a strong view of the wider European picture. The ambition is a shared European baseline; the practice today is still largely national.

### 2. Projects and workstreams building on Transmodel

A number of ecosystem-level projects use Transmodel as the foundation for their own domain-specific work, extending its coverage or aligning it with adjacent standards:

- **Entur national mobility infrastructure (Norway)** — Entur operates Norway's national mobility infrastructure, covering the full chain from data collection to passenger-facing services. This includes the national stops registry, the national journey planner (which consumes NeTEx and SIRI from the Norwegian public transport authorities), and a national ticket distribution system for cross-operator sales. Entur also maintains the Nordic NeTEx profile in cooperation with Sweden, Finland and Denmark, and contributes to open-source tooling (such as OpenTripPlanner) used across the Nordic region and beyond.
- **EUDIT** — the successor to CoRoM, continuing work on cross-European ticketing and sales interoperability. Both projects take a multimodal view: although rail is the backbone of long-distance travel, very few passengers travel station-to-station. Most need one or more forms of mobility at each end of a rail trip, so EUDIT (like CoRoM before it) looks at the whole journey — rail working seamlessly with bus, tram, metro, ferry, shared mobility, flights and other modes. CoRoM was proposed by Entur to prepare the ground for cross-European ticketing once NeTEx deployments across Europe reach the maturity needed to support it; EUDIT extends this work with a broader scope.
- **Italian NeTEx and OpRa work, led by 5T (Turin)** — 5T has been part of the European NeTEx and OpRa work from the start, and continues to lead several current workstreams: the Italian NeTEx profile at the national access point, the OpRa specification for exchanging observed operational data, and the NeTEx extension for alternative modes. In the Piedmont region, 5T also runs **BIP** (Biglietto Integrato Piemontese), an integrated multimodal ticketing system covering public transport, rail and other modes across the region.
- **MobilityData / GBFS mapping** — a mapping between the General Bike Sharing Specification (GBFS) and the alternative-modes subset of Transmodel/NeTEx.
- **NEMU** — a Nordic project led by **ITS Nordic+**, where **Matkahuolto** and **Entur** are developing Nordic travel search and booking across operators and modes. Several routes are already in production, with new operators and regions being added on an ongoing basis.
- **TSI Telematics (TSI TEL)** — the EU Technical Specification for Interoperability on Telematics for rail, adopted 6 February 2026 and in force since 2 March 2026. Requires NeTEx (scheduled) and SIRI (real-time) for cross-border rail data exchange, bringing rail into alignment with the exchange standards already used for the wider public transport sector.

### 3. Direct use as a reference data model

Some organisations use Transmodel directly — not to exchange data via NeTEx/SIRI, but as the conceptual starting point for designing their own internal databases, system architectures, or interfaces.

This kind of adoption is less visible and less common, but it is a legitimate use. Transmodel's role here is as a well-defined, interoperable vocabulary that an organisation can reuse rather than invent from scratch. Typical cases:

- An authority specifying its own operational data model to be internally consistent and future-ready for NeTEx export
- A vendor designing a product's internal schema in a way that stays close to Transmodel entities, simplifying later NeTEx/SIRI integration
- An academic or research project needing a published reference model to anchor its own work

There is no public inventory of this kind of adopter today. If your organisation uses Transmodel directly in this way and would like to be listed, see *Add an entry* below.

## Vendors and tooling

For software products with declared Transmodel/NeTEx/SIRI support — converters, validators, editors, visualisation tools — see each standard's **Resources** page or the vendor material referenced from the [NeTEx Implementations](../netex/implementations.md) page. A consolidated vendor directory is on the backlog but not yet published here.

## Add an entry

To add your organisation, product, or project to any of these lists — either here or on one of the standard-specific Implementations pages — see [How to contribute](../../introduction/how-to-contribute.md) or raise an issue in the [site repository](https://github.com/BredeD/transmodel-site).
