---
original_title: "Austria"
source: mediawiki
source_url: https://data4pt.org/wiki/Austria
last_edited: 2024-12-11T12:26:28Z
status: raw
---

!!! warning "Raw, unwashed content"
    This page is in the review corpus — copied directly from the source site with only automatic conversion applied. It has not yet been edited for tone, structure, accuracy, or duplication. Do not treat as final.


## Overview in the National Level

For many implementations, the VDV standards (incl. VDV736) are preferred over other options, for them being tailored to the regional specifics.

[MVO](https://data.mobilitaetsverbuende.at/en) publishes NeTEx data and preferably uses VDV736 (SIRI-SX) for situation information.

## Use cases

### Description

**Wiener Linien** (Viennese Lines) is the company running most of the public transit network in the city of Vienna, Austria. Thus, it is responsible for managing the city's extensive network of buses, trams, and metro systems. It was established in 1978, and is part of the city corporation Wiener Stadtwerke.

For the purposes of operating and maintaining customer information channels (such as the WienMobil app, digital signage and departure boards, the website, on-board information, etc.), Wiener Linien has introduced an API gateway as a middleware component. This ensures that all customer-facing channels source their information from a single system (the API gateway), providing consistent information across all available platforms.

### Architecture

Since the data sources connected to the API Gateway may provide different formats, or the data required for "customer information" may be scattered across various independent sources, Wiener Linien has implemented SIRI and/or NeTEx as the canonical data formats within the API Gateway. This approach facilitates the consolidation of information within the API Gateway, ensuring it serves as the single point of truth for all customer information channels.

The API Gateway can provide customer information channels with data in the canonical format (SIRI or NeTEx) or transform the data into any format required by the consuming system.

For specific use cases, the data can be enriched before being provided to the customer information channels:

  - Automatic translation of SIRI-SX Situation Descriptions
  - Generation of sign language videos
  - Creation of workload or delay estimates using machine learning

### Implementation

The following use cases illustrate how Wiener Linien utilizes the API Gateway and data standards to operate and maintain customer information channels:

  - **FIS+** involves on-board information screens in the latest subway rolling stock (X-Wagen). The necessary data, including station departures and current situations, is retrieved from internal data sources, transformed into the SIRI-SM and SIRI-SX canonical formats, and then converted into a proprietary format that contains only the most relevant information. This format is extremely lightweight due to limited bandwidth, and the information is subsequently forwarded to the rolling stock.

<!-- end list -->

  - For the **WienMobil App and WienMobil Monitor**, the relevant information (station departures and current situations) is pulled from multiple data sources, including external sources from other transport operators like ÖBB. This data is transformed into the canonical SIRI-SM and SIRI-SX formats, cached within the API Gateway, and then delivered on demand to the app backend. The format is optimized by omitting redundant overhead to improve efficiency.
  - The **e-Paper timetable** follows a similar process. Station departure and current situation data are pulled from internal data sources, transformed into SIRI-SM and SIRI-SX, cached within the API Gateway, and sent to the e-Paper backend as needed.
  - For the generation of sign language videos, current situation data is regularly retrieved from internal sources, transformed into SIRI-SX, and sent a third party API. The thrid party system processes the situation descriptions, generating a sign language video for each relevant entry. A link to the video is returned and can be added as a custom field in any subsequent SIRI-SX messages.
  - In the case of the WienMobil Alexa Skill, the required information (station departures) is sourced from internal and external data sources (such as ÖBB), transformed into SIRI-SM, cached in the API Gateway, and provided on demand to the backend system of the Alexa Skill.

### Outcome

The chosen data standard framework is highly robust, accommodating virtually any use case. However, this flexibility introduces significant complexity, which can be challenging for some colleagues and implementers. Despite this, it is well-suited as a canonical data format for these reasons. With this framework in place, Wiener Linien is well-prepared to meet the requirements of EU Regulation 2017/1926.
