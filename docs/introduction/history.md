# History

The Transmodel Ecosystem grew out of European research projects in the late 1980s and early 1990s, and has evolved through more than three decades of standardisation work under CEN and successive European Commission programmes. This page traces the main milestones — how a data model conceived to link fragmented national transit systems became the reference vocabulary for public transport across Europe, and the family of exchange standards (NeTEx, SIRI, OJP, OpRa) that build on it today.

## Origins: DRIVE and Cassiope (1989–1994)

Transmodel began with the **Cassiope** project (1989–1991), funded under the European Commission's first DRIVE programme. Building on Cassiope's results, the **EuroBus** work area and the **Harpist** taskforce — both part of DRIVE II — expanded the model between 1992 and 1994, drawing on Germany's ÖPNV data model for public transport. The joining of the Transmodel and Harpist kernel teams led directly to the formation of Subgroup 4 (SG4) of CEN/TC 278 WG3, which has stewarded Transmodel ever since.

## From pre-standard to EN 12896 (1995–2002)

The results were consolidated into the **pre-standard ENV 12896**, published in May 1997. The EU project **Titan** (1996–1998) validated the model in pilot deployments across Lyon, Hanover and Salzburg. In France, the successive **SITP** and **SITP2** projects (1999–2002) developed extensions that fed directly into the formal European standard.

## Transmodel v5.1 and the arrival of SIRI (2002–2006)

Between 2002 and 2003, CEN/TC 278 WG3 SG4 consolidated the previous drafts together with the German VDV specifications and several inputs from the United Kingdom. The result was **Transmodel v5.1**, adopted as EN 12896 in 2006. During the same period, work began on **SIRI** (Service Interface for Real-time Information), the first Transmodel-derived exchange standard for live operational data. Three parts of SIRI were later published as EN 15531-1 to -3, with further parts remaining as Technical Specifications.

## IFOPT and NeTEx (2006–2014)

The **IFOPT** project (Identification of Fixed Objects in Public Transport) used Transmodel v5.1 as an input to model stops and points of interest. It was published as EN 28701:2009 and later folded back into Transmodel v6.

The **NeTEx** project ran from 2009 to 2014 under CEN/TC 278 WG3 SG9, led by France, with participation from the UK, Germany and others. It combined the Transmodel v5.1 timetable model with the IFOPT fixed-objects model into a single conceptual base, and defined an XML exchange format on top. Version 1.0 was published in 2014 as **CEN/TS 16614**, and the final part followed in 2015. NeTEx was designed to serve a broad set of stakeholders across the European rail and public transport sector, including the European Union Agency for Railways (ERA) and the International Union of Railways (UIC).

## National adoption: UK, France, Norway (2014–2018)

Before MMTIS made European-wide adoption a regulatory requirement, the first practical NeTEx implementations grew out of a small number of national initiatives.

The **United Kingdom** produced one of the earliest NeTEx profiles — narrow in scope, covering the specific data needs of UK bus and rail information systems.

**France**, which had led the NeTEx project itself, then built a broader national profile. Working through the AFNOR BNTRA/CN03/GT7 group, the French profile expanded the number of supported use cases and was later published as the reference format under a March 2022 decree. It is maintained on [normes.transport.data.gouv.fr](https://normes.transport.data.gouv.fr/) and used by the French National Access Point [transport.data.gouv.fr](https://transport.data.gouv.fr/).

**Norway** entered in 2016 when [**Entur**](https://entur.no) was established to run the national journey planner as part of the Norwegian rail reform. Entur took the French profile as a starting point and significantly expanded its scope. By 2017, half of all Norwegian Public Transport Authorities were producing valid NeTEx; by 2018, the national journey planner was live. The Norwegian work then evolved through close cooperation with Sweden, Finland and Denmark into the **Nordic NeTEx Profile**, coordinated with the wider CEN community.

The **European Passenger Information Profile (EPIP)** — first published as CEN/TS 16614-PI — was subsequently developed as a common European subset drawing on the Nordic profile and inputs from other early adopters. It represents the agreed minimum needed to satisfy MMTIS obligations. From 2017 onward, the MMTIS Regulation (2017/1926) turned NeTEx from a voluntary standard used by a few pioneers into a de facto requirement across every EU member state.

## Transmodel v6: modularisation (2016–2019)

To make the standard easier to adopt and maintain, Transmodel was restructured as a modular series. **Parts 1 to 3** — Common Concepts, Network Topology, and Timing and Vehicle Scheduling — were published as EN 12896-1, -2 and -3 in 2016. Between 2017 and 2019, the CEN Project Team PT0302 completed **Parts 4 to 9**: Operations Monitoring and Control, Fare Management, Passenger Information, Driver Management, Management Information and Statistics, and Informative Documentation.

## Alternative modes and v6.2 (2020–2025)

Work on the so-called "new modes" or "alternative modes" — vehicle sharing, pooling, rental — was initiated in CEN WG17 (Mobility Integration) and published as CEN/TS 17413:2020. In a second step, WG3 took the specification over and published it as **Part 10: Alternative modes** in 2021 (EN 12896-10). Alongside, informal liaison with MobilityData — the organisation maintaining the General Bike Sharing Specification (GBFS) — under the aegis of the Data4PT project established a mapping between GBFS core elements and a subset of Transmodel/NeTEx.

The update to **Transmodel v6.2** ran from 2023, aimed at consolidating Part 1, adding functional extensions, and improving coherence between Transmodel and its derived standards.

## Rail alignment and the Telematics Applications TSI (2017 onward)

From 2017, work under the European Union Agency for Railways compared TAP TSI rail data formats with NeTEx and produced mappings for fares and station/timetable data. The **CoRoM** project (started 2023) continued this on the fare side, comparing OSDM (Open Sales and Distribution Model) with Transmodel/NeTEx. This body of work ran in parallel with the drafting of the **Telematics Applications TSI**, adopted 6 February 2026, which formally requires railway data to be exchanged using NeTEx and SIRI — see [Legal context](legal-context.md).

## Timeline

| Year | Milestone |
| --- | --- |
| 1989–1991 | Cassiope project (DRIVE I) |
| 1992–1994 | EuroBus and Harpist taskforce (DRIVE II) |
| 1995 | CEN/TC 278 WG3 SG4 established |
| 1996–1998 | Titan validation project |
| 1997 | Pre-standard ENV 12896 published |
| 1999–2002 | SITP and SITP2 |
| 2004–2005 | Transmodel/SIRI harmonisation |
| 2006 | EN 12896 (v5.1) adopted |
| 2009 | IFOPT published as EN 28701 |
| 2009–2013 | NeTEx project |
| 2014 | NeTEx v1.0 (CEN/TS 16614) published |
| 2016 | Transmodel v6 Parts 1–3 |
| 2017 | MMTIS Regulation (2017/1926) adopted |
| 2017–2019 | Transmodel v6 Parts 4–9 |
| 2020 | CEN/TS 17413 (Alternative modes) |
| 2021 | Transmodel Part 10 published |
| 2023 | Transmodel v6.2 work begins; CoRoM project launched |
| 2026 | Telematics Applications TSI (rail) adopted |

## Sponsors and contributors

The Transmodel Ecosystem is the product of sustained European public investment and a small international expert community. Financial support has come from the European Commission (through the DRIVE programme, DG XIII, and later the Connecting Europe Facility), the French Ministry of Transport, the Dutch and German ministries of transport, and CEN itself through successive grant agreements. Technical contributions have come from public transport operators, national access-point authorities, consulting firms and academic partners across France, Germany, the United Kingdom, the Netherlands, Italy, Sweden, Slovenia, Denmark, Norway and beyond — many of whom continue in the community today.

Much of the day-to-day standardisation work across Europe still depends on individual specialists contributing on their own time, without dedicated funding for the ongoing maintenance of the standards. In 2025, Norway began directly funding experts working on the Transmodel Ecosystem to help address this gap. Broader participation from more countries in sustaining this work would strengthen the Ecosystem for everyone who depends on it.

!!! note "Full attribution"
    Named individuals and full organisation lists for each project phase are preserved in the legacy source material and can be reproduced on request. See also [Governance](governance.md) for how the standards are maintained today.
