# Legal context

Transmodel isn't just a technical model — it sits inside a specific European legal framework that shapes what public transport data is expected to look like, who publishes it, and to what timescales.

![](../assets/images/transmodel-cen/Embleme-UE_base_BD_2.jpg)

## The ITS Directive

Transmodel is referenced in the context of the European **[ITS Directive 2010/40/EU](http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32010L0040)** — in particular Priority Action A, which supplements the Directive with regard to the provision of EU-wide multimodal travel information services. The role Transmodel plays under this directive is to define the requirements that make travel information services accurate, complete, and available across borders to ITS users.

The Public Transport Reference Data Model covers the same domains reflected in the directive's scope: network topology, scheduling, operations monitoring and control, fare management, passenger information, driver management, management information and statistics, and alternative modes.

## The MMTIS Regulation

The **Multimodal Travel Information Services Regulation** — usually called MMTIS — is the operational instrument that makes these obligations concrete. It requires data holders to provide, via national access points, access to the static, historic, and observed travel and traffic data listed in the annex of the Regulation.

For public transport modes, MMTIS requires that data be published in one of the following standards (or in any digital machine-readable format that can be demonstrated fully compatible and interoperable with them — for example via automatic converters and validators):

- **NeTEx** (CEN/TS 16614 and subsequent versions).
- The technical specifications set out in **Regulation (EU) No 454/2011** — dedicated to the trans-European rail network.
- The technical documents published under the authority of the **IATA Passenger Services Conference** — for air.
- **Transmodel EN 12896** where there is no reference exchange protocol.

For the spatial network, the requirements set out in Article 7 of Directive 2007/2/EC — the **INSPIRE Directive** — also have to be taken into account.

The Regulation provides a detailed calendar for the publication obligation of each data category listed.

## How Transmodel fits in

Transmodel is the conceptual layer beneath all this. [NeTEx](../standards/netex/index.md), [SIRI](../standards/siri/index.md), [OpRa](../standards/opra/index.md) and [OJP](../standards/ojp/index.md) are the data formats derived from Transmodel that MMTIS names as usable exchange formats. Where these formats are used, Transmodel is used underneath.

## In detail

The current MMTIS text was updated in 2024, which introduced specific changes to Articles 1, 2, 3, 4, 5, 6 and 9. Both the amendment and the underlying regulation are available in full:

- **[Commission Delegated Regulation (EU) 2024/490](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32024R0490)** of 29 November 2023 — amending Delegated Regulation (EU) 2017/1926.
- **[Commission Delegated Regulation (EU) 2017/1926](https://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1510306588364&uri=CELEX:32017R1926)** of 31 May 2017 — the original MMTIS regulation.
