---
original_title: "France"
source: mediawiki
source_url: https://data4pt.org/wiki/France
last_edited: 2024-10-08T12:54:24Z
status: raw
---

## Overview in the National Level

### Current Situation

Many datasets based on NeTEx and SIRI standard are available in [French National Access Point](https://transport.data.gouv.fr/?locale=en) .

  - **Mass transit**: 114 datasets in NeTEx – French Profile format are available (excluding tariff and accessibility data) out of 421 total mass transit datasets.
  - **Mass transit (Real-time)**: 25 SIRI datasets are available compared to 159 GTFS-RT datasets.
  - **Pedestrian accessibility**: 2 datasets in NeTEx – French Profile format have been provided.

### Upcoming Developments

For several months, towns and regions have been collecting accessibility-related data and plan to publish it in NeTEx – French Profile. A decree issued in May has strengthened the collection of this data.

In connection with the single-ticketing experiment, the French NAP team is assisting data producers, particularly in 2 regions, in providing their tariff data in NeTEx – French Profile.

More NeTEx and SIRI mass transit datasets are expected to be published in the coming months, as stakeholders are now ready to produce them. The French NAP team is actively supporting these efforts.

A French Profile for new mobility modes (such as free-floating services) is currently in development, although the release date is still unknown.

The French NAP is also working on implementing a NeTEx validation tool to help providers comply with the standard.

## Use cases

### Description

More information regarding the implementation of public transport standards can be found at the following link: [Public Transport Format Statistics](https://transport.data.gouv.fr/stats#public-transport-format). This includes data from regions such as **Nouvelle-Aquitaine**, **Pays de la Loire**, and **Île-de-France**.

In **Paris** and some surrounding towns, NeTEx accessibility datasets have been provided through an experimental project that involved converting data from OpenStreetMap into the NeTEx format. Further details on this initiative can be found here: [Jungle Bus Datasets](https://transport.data.gouv.fr/datasets?q=jungle+bus).

European regulations require transport authorities to provide datasets in the NeTEx format. As a result, an increasing number of local authorities and digital service providers recognize the utility of this standard, especially for establishing a multimodal information system. French law mandates that these multimodal systems must cover every region in the country.

Despite the growing acceptance of NeTEx, many transport authorities and private transport operators find the standard to be overly complex. While some digital service providers have mastered certain aspects of NeTEx, the intricate nature of the standard presents challenges for broader adoption.

To support the transition, the French Ministry of Transport has invested in developing specific tools that assist producers in collecting accessibility data and publishing it in the NeTEx format. This financial backing aims to simplify the process and encourage compliance with the standard among local authorities.

### Architecture

The implementation of public transport standards follows the guidelines set forth in the French Profile, which can be accessed [here](https://normes.transport.data.gouv.fr/). This profile is compatible with the EPIP (Échange de données pour l'Information et la Planification des Transports) standard, ensuring that data exchanges meet established interoperability requirements.

### Implementation

Many transport authorities use SIRI for their own purposes, although the exact extent of this usage is unclear. The multimodal information system in **Nouvelle-Aquitaine** (Modalis) utilizes NeTEx, or there are plans to implement it. Similarly, **Île-de-France** (IDFM) is also expected to adopt NeTEx for its multimodal information system.

### Outcome

Currently, it is too early to observe the benefits of the NeTEx implementation, as the process is still ongoing.

In the future, there are expectations for two key improvements:

1.  The availability of more detailed information, including tariffs and accessibility of locations;
2.  Datasets with a higher level of quality.

However, it is likely that in the coming years, a gap will emerge between the most advanced transport authorities and operators and those that are less advanced in their implementation of the NeTEx standard and multimodal information systems.
