---
original_title: "Explore NAP guidelines"
source: mediawiki
source_url: https://data4pt.org/wiki/Explore_NAP_guidelines
last_edited: 2025-04-28T14:27:12Z
status: raw
---

!!! warning "Raw, unwashed content"
    This page is in the review corpus — copied directly from the source site with only automatic conversion applied. It has not yet been edited for tone, structure, accuracy, or duplication. Do not treat as final.


A National Access Point (NAP) is a central internet resource from which transport data for a country can be obtained by operators and third parties.

  - A NAP may comprise a repository of reference data and/or a registry of available data services and real-time feeds.
  - Data can be of many different types, both static - operators, lines, stops, timetables, accessibility, etc. and real-time (vehicle locations, estimated arrival times, disruptions, etc.)
  - A NAP will hold metadata about the available data and feeds so as to be able to support search and discovery processes.

A number of standard formats and APIs, such as NeTEx, DatexII, SIRI are mandated.

Check the [DATA4PT website](https://data4pt-project.eu/) and [NAPCORE website](https://napcore.eu/) for additional information.

# How to make datasets for multimodal mobility systems interoperable across the EU

*Legal Disclaimer*

*The information in this document is provided “as is”, and no guarantee or warranty is given that the information is fit for any particular purpose. The referenced consortium members shall have no liability to third parties for damages of any kind including without limitation direct, special, indirect, or consequential damages that may result from the use of these materials subject to any liability which is mandatory due to applicable law. This document is published under the CC BY-SA 4.0 license<sup>\[1\]</sup>.* ----<sup>\[1\]</sup> See https://creativecommons.org/licenses/by-sa/4.0/deed.en

## Summary

This paper proposes some best practices for National Access Points (NAPs) to follow for a better implementation of MMTIS Delegated Regulation (EU 2017/1926 and its amendment EU/2024/490). Based on the exchanges with the different stakeholders and on the overall experience acquired in the framework of DATA4PT, its experts’ team presents the main reasons why interoperability is hard to achieve, and how NAPs need to move forward to achieve their goals (goals as set by the regulation). It provides recommendations on overcoming these issues and building a common implementation approach of the regulations across the EU for multimodal mobility services advancement.

NAPs need to be oriented beyond the local level and specific mobility mode. Integration from all perspectives (from city or region up to EU and worldwide, from one mobility mode to full inter-modality) is key. As the goal is more sustainable mobility in the long run (financially, environmentally, socially), complete and inclusive data standards to support all chains of data exchange from operations to end user/passenger are the main tools for this.

The target group of this paper is the NAP implementers and operators and the organisations regulating them in their country. This paper can be used as reference from stakeholders whenever it is relevant and to complement the work done in the framework of the NAPCORE Programme.

The most important aspects addressed in this paper could be summarised in the following recommendations:

●       The data in all NAPs is at least published according to one profile per standard required by the regulation. 

●       NAPs should also consume the data it shares. It also should encourage data producers to consume the data it produces (e.g. using digital twinning as a method. Also, the NAPs should collaborate within NAPCORE to make the interfaces generic (applicable to all NAP), open source and shared between NAPs).

●       A stop registry must be provided.

●       The NAPs should give incentives to data producers to provide correct data.

●       The following standards shall be used: NeTEx (schedules, stop registry, fares), SIRI (real-time), OJP (API towards a Journey Planner), OpRa and in general the ones based on Transmodel (CEN standard).<sup>\[1\]</sup>

●       The NAPs should maintain all neighboring NAP references so end-users can directly find the relevant datasets for cross-border operation.

●       The NAPs should actively register successful integrations, their products, and the source datasets that were used. This will automatically give a graph of importance. 

●       In addition, other formats/ specifications shall be shared in NAPs if useful by data consumers like GTFS/GBFS. The standards should have good governance<sup>\[2\]</sup>. ----<sup>\[1\]</sup> NeTEX = TS16614, SIRI = TS/EN 15531, OJP = TS 17118

<sup>\[2\]</sup> E.g. see ISO - Good Standardization Practices (GSP)

## What to expect from this paper

This paper proposes some best practices for National Access Points (NAPs) to follow for a better implementation of MMTIS Delegated regulation (EU 2017/1926 and the amendment EU/2024/490), NAPs need to focus on the data consumers and easy access to the data for them. Only complete, homogenised, integrated data sets are of interest. Quality assurance needs to be an integral part of all NAPs. NAPs need to be oriented beyond the local level and specific mobility mode. Relevant is integration from all perspectives (from city or region up to EU and worldwide, from one mobility mode to full inter-modality). As the goal is more sustainable mobility in the long run (financially, environmentally, socially), complete and inclusive data standards to support all chains of data exchange from operations to end user/passenger are the main tools for this.

Based on the exchanges with the different stakeholders and on the overall experience acquired in the framework of DATA4PT, its experts’ team presents the main reasons why interoperability is not yet achieved, and how NAPs need to move forward to achieve their goals (goals as set by the regulation). It provides recommendations on how to overcome these issues and build a common implementation approach of the regulations across the EU for multimodal mobility services advancement. This paper can be used as a reference for stakeholders whenever it is relevant and to complement the work done in the framework of NAPCORE Programme.

### To whom it addresses

The target group is the NAP implementers and operators and the organisations regulating them in their country.

### Objectives and expected outcome

The objectives of this paper can be summarised as follows:

  - Present the prerequisites and procedures to make datasets viable and interoperable.
  - Make it easy for consumers of MMTIS (EU/2024/490 and EU/1926/2017) data to fetch the same data types from different NAPs without additional cost.
  - Reflect on the work of other national and EU projects and initiatives (like NAPCORE).
  - Support NAP operators and other actors in decision-making for adapting implementation to the guidelines to implement the MMTIS DR.

The expected outcome of the following paper’s recommendations is that:

  - Make it simple to produce data to be published on a NAP.
  - Make seamless cross-border mobility services and passenger information systems possible, reliable and viable.
  - Data consumers can access the relevant data from all NAPs in a way that will promote the usage of NAP data for free.
  - NAP knows how to provide data in an easy standardised way, so that data consumers don’t need or can greatly reduce additional business logic in their connectors.

<!-- end list -->

  - Homogenise the usage of NeTEx/SIRI (and simpler standards for convenience like GTFS and GBFS).
  - Provide all necessary data on the national level according to MMTIS DR.

### Principles<sup>\[1\]</sup>

This guidance document is developed with some principles to help the industry navigate toward our interoperable future. The principles are statements of intent that lay out the MMTIS’s positive vision for the future of mobility data. Rooted in the philosophies of public service and personal empowerment that define the transit industry, the principles also highlight the efficiency, connectivity, and flexibility that interoperability will unlock for mobility data users.

1.  CEN-Standards: Interoperability should be achieved through the development, adoption, and widespread implementation of NeTEx and SIRI data that support the efficient exchange and portability of mobility data.
2.  Cross-border alignment: We seek collaboration within the NAPs and CEN to secure easy-to-use cross-border open data from the National Access Points; we align on as few profiles as possible.
3.  Interoperability: It is highly recommended that all systems creating, modifying, or consuming mobility data should be interoperable.
4.  Tools: Transit agencies and other mobility service providers should have access to tools that present high-quality mobility data accessibly, equitably, and in real time to assist travelers in meeting their mobility needs.
5.  Open technology: Transit agencies, other mobility service providers, and travelers should be able to select the transportation technology components that best meet their needs.
6.  High quality: All individuals and the public should be empowered through high-quality, always updated, well-distributed mobility data to find, access, and utilize high-quality mobility options that meet their needs as they see fit while maintaining their privacy.
7.  Self-utilization: The NAPs and data producers should, when possible, use the shared data themselves.

\----<sup>\[1\]</sup> Inspired by: https://www.interoperablemobility.org/

## What hinders interoperability

Interoperability is not an easy goal to achieve. On a national level, many of the countries harmonised their approaches to publish data in the NAP according to the regulation and they are developing services to use this data to provide country-based passengers’ services. However, in most cases, there are still challenges to overcome to make the available data useful for cross-regional or intermodal journeys, while cross-country services are still not possible due to the following parameters:

●       Master data management and strategies for stop identifiers (IDs) that ensures stable and unique IDs are not always in place.

●       Exported data is of poor quality (if available at all), as if the data itself was not used.

●       NAPs don’t always aggregate the data and take a role in quality assurance.

●       Data completeness is not documented.

●       The standards are still poorly implemented in some countries

●       The standards themselves are not strict enough. Even the profiles have too much ambivalence.

●       Different profiles are used in different countries and are not interoperable (i.e. NOT based on EU profiles).

●       IDs are not coherent between neighbouring regions of the dataset, within and across NAPs; for both the same data theme (i.e. public transport between countries) as well as across themes (i.e. street network to public transport).

●       Data processes in the NAPs are not documented.

●       Duplication in data content.

Chapters 4 and 5 address these points in detail. The MMTIS data dictionary, which is being developed in the framework of NAPCORE project<sup>\[1\]</sup>, will also help. The development of the NeTEx and SIRI European profiles will also help unlock interoperability. ----<sup>\[1\]</sup> MMTIS Data dictionary from NAPCORE project: https://github.com/NAPCORE/Data-dictionary/blob/main/DR%20(EU)%202024-490.md

## Most important points

The following points are important for all NAPs.

  - The data in all NAPs are at least published according to the relevant European profile per standard defined by the regulation (other additional data formats may help adoption in the field).
  - NAPs should also be prepared to consume the data they share. It also should encourage each data producer to consume the data it produces. E.g. a digital twin can be formed that consumes this data and presents it as an example to the user.
  - Access to consistent information on the European level for all stops (NeTEx: StopPlace) and quays (NeTEx: Quays). A stop registry on EU level should be the final goal.
  - The NAPs should incentivise data producers to provide correct data: complete, quality-assured, and valid on syntactic and semantic levels. E.g. by checking it themselves (as e.g. the French NAP does for GTFS).
  - The NAPs should maintain, in addition to their own data, some data or at least metadata for relevant adjacent NAPs so end-users may directly find the relevant datasets for cross-border operation.
  - The following standards shall be used: NeTEx (stop registry, schedules, fares), SIRI (real-time), OJP (API to a journey planner), and in general the ones based on Transmodel (CEN standard). Also OpRa as soon as it is available.
  - In addition, other formats/ specifications might be shared in NAPs if useful by data consumers like GTFS/GBFS
  - The standards should be open<sup>\[1\]</sup> and have good governance.
  - Work to harmonize the national profiles to become unified.

\----<sup>\[1\]</sup> This is related to the decision of the Court of Justice of the European Union (CURIA) about the access conditions to “harmonised standards adopted by CEN that form part of EU Regulations”. Link to the case law [here](https://curia.europa.eu/juris/documents.jsf?nat=or&mat=or&pcs=Oor&jur=C%2CT%2CF&num=C-588%252F21P&for=&jge=&dates=&language=en&pro=&cit=none%252CC%252CCJ%252CR%252C2008E%252C%252C%252C%252C%252C%252C%252C%252C%252C%252Ctrue%252Cfalse%252Cfalse&oqp=&td=%3BALL&avg=&lgrec=fr&page=1&lg=&cid=740237).

### Why Transmodel based standards in NAPs

The reference data model Transmodel is required by the MMTIS EU DR due to several reasons.

The most important parameter that makes Transmodel the choice of the regulation is the fact that it is a conceptual model which provides common language and  data structures to describe semantics of the Public Transport domain. It considers a number of public transport features for information and service management and it includes concepts, their characteristics and links between concepts. It  describes aspects covered by conventional public transport, including flexible transport and alternative modes​ and it allows interoperability between the information processing systems of transport operators without the need of conversion. Like this it facilitates the representation of multimodal trips, without the risk of losing information along the data chain and it can be used to design databases and/or data exchange formats. In fact, Transmodel has been used for many years to specify a number of CEN data exchange formats, such as CEN SIRI (for real-time data), CEN NeTEx(for planned data) and OpRa (for operational raw data) (Figure 1). It is published under the reference number EN12896 as series EN12896 1 to 10 (Figure 2).

![Figure 1 Illustration of the interactions between Transmodel SG4and WG3 subgroups SG7 for SIRI, SG8 for OJP, SG9 for NeTEx, SG10 for OpRa (Source:<https://transmodel-cen.eu/>).](Figure_1_Illustration_of_the_interactions_between_Transmodel_SG4_and_WG3_subgroups_SG7_for_SIRI,_SG8_for_OJP_SG9_for_NeTEx_SG10_for_OpRa_\(Source-https---transmodel-cen.eu-\)..jpg "Figure 1 Illustration of the interactions between Transmodel SG4and WG3 subgroups SG7 for SIRI, SG8 for OJP, SG9 for NeTEx, SG10 for OpRa (Source:https://transmodel-cen.eu/).")

![Figure 2 Transmodel Parts and relation with the different technical standards exchange formats and APIs (Source:<https://transmodel-cen.eu/>).](../../assets/images/wiki/Figure_2_Transmodel_Parts_and_relation_with_the_different_technical_standards_exchange_formats_and_APIs.jpg "Figure 2 Transmodel Parts and relation with the different technical standards exchange formats and APIs (Source:https://transmodel-cen.eu/).")

### How CEN European Standards are developed and how to contribute as NAP operator

Transmodel and its data exchange formats are developed under the aegis of CEN (Comité Européen de Normalisation). The development of the standards is based on the involvement of all relevant stakeholders for multimodality (beyond silos) and the official approval process is based on votes from representatives from all CEN members. European standards have also been developed to ease compliance with European rules and regulations such as EU legislation. Through Regulation (EU) No 1025/2012, the three European Standardisation Organisations (CEN, CENELEC and ETSI) may receive a request to produce European harmonised standards in support of EU legislation and policies (more here). Technically anyone can propose work items that will result in a European Standard. Actually, an expert (e.g. from a NAP) in the field can request through its CEN national standardisation body to be part of the group TC278/WG3, following the national rules. At CEN and CENELEC the work is usually channeled by the members (the CEN National Standardization Bodies and the CENELEC National Committees). In some cases, the request also comes from the European Commission or from other stakeholders. If enough CEN and/or CENELEC members are willing to be involved in the development process, the work is then assigned to the relevant Technical Committee (TC). At the same time, a “standstill” is enforced in all national work surrounding the same topic. Once the Technical Committee is established, mirror committees of stakeholders at national level decide on the national contributions regarding the development of the standard. In addition to the CEN and/or CENELEC members, Technical Committees also include several observers, such as ISO/IEC members, European Commission/EFTA, external European industry associations and other affiliate bodies.

![Figure 3 CEN Technical Committees TCs split into Working Groups (Source:<https://transmodel-cen.eu/>).](../../assets/images/wiki/Figure_3_CEN_Technical_Committees_TCs_split_into_Working_Groups.jpg "Figure 3 CEN Technical Committees TCs split into Working Groups (Source:https://transmodel-cen.eu/).")

Transmodel is developed by TC 278 WG3 (Public Transport). Its structure is presented in figure 4.

![Figure 4 TC 278 WG3 Public Transport structure (Source:<https://transmodel-cen.eu/>)](../../assets/images/wiki/Figure_4_TC_278_WG3_Public_Transport_structure.jpg "Figure 4 TC 278 WG3 Public Transport structure (Source:https://transmodel-cen.eu/)")

TC 278 WG3 splits on its turn into Sub-Groups (SGs) as shown in the picture below (Figure 5).

![Figure 5. TC 278 WG3\_Public Transport structure (Source: <https://transmodel-cen.eu/>)](../../assets/images/wiki/Figure_5._TC_278_WG3_Public_Transport_structure.jpg "Figure 5. TC 278 WG3_Public Transport structure (Source: https://transmodel-cen.eu/)")Once the proposal for a standard has been evaluated and approved, the proposal goes on to the drafting stage which is based on consensus-building. When the draft standard is finalised, it goes up to public inquiry and is open to all interested parties. When the enquiry is over, the votes and comments on the standard are evaluated and depending on the result, the draft standard is either published or additionally worked upon and subsequently submitted to a formal vote. Each of the Transmodel standards has a discussion forum on basecamp (by invitation). The physical standards NeTEx, SIRI and OJP have also an open GitHub-repository where questions and changes requests can be raised. The GitHub repositories are:

  - VDV/OJP: [Open API for distributed journey planning](https://github.com/VDVde/OJP)
  - NeTEx-CEN/NeTEx: [Network Timetable Exchange](https://github.com/NeTEx-CEN/NeTEx/)
  - SIRI-CEN/SIRI: [Service Interface for Real time Information (SIRI)](https://github.com/SIRI-CEN/SIRI)

Read more regarding CEN processes and standards development: <https://www.cencenelec.eu/european-standardization/european-standards/>

### How to acquire Transmodel based standards

The documentation of the standards is made available by the national standardisation bodies<sup>\[1\]</sup>, following their process and using the corresponding identification numbers of each document:

  - Transmodel standard (EN12896 1-10)
  - SIRI-Service interface for Real-time Information, CEN EN/TS 15531 1-7 (SG7)
  - NeTEx: Network, Timetables and Fare Exchange, CEN TS 16614 1-6 (SG9)
  - Open API for Distributed Journey Planning, CEN TS 17118 (SG8)
  - Data Communication on Vehicles, CEN TS 13149 7-11 (SG1)
  - OpRa: Operational Raw Data and Statistics, under development (SG10)

For the purposes that this document tries to promote, it would be an advantage if these standards were made available free of charge.               

There is an ongoing discussion if there is a legal obligation to provide free access to CEN standards that are referred to in laws and regulations according to the principle of “free access to all that is a law”.

The standards have related technical artifacts, like UML, XSD, libraries, profiles, and open source, that are available for free at various websites. These documents should cover the need when developing a software to support MMTIS. The websites where technical artifacts are available are:

  - https://transmodel-cen.eu/
  - https://github.com/NeTEx-CEN
  - https://github.com/SIRI-CEN/SIRI
  - https://github.com/VDVde/OJP

\----<sup>\[1\]</sup> To browse the documents, you may use this \[<https://standards.cencenelec.eu/dyn/www/f?p=CEN:105>::RESET:: tool\].Regulation (EC) No 1049/2001 of the European Parliament and of the Council of 30 May 2001 regarding public access to European Parliament, Council and Commission documents is available [here](https://eur-lex.europa.eu/eli/reg/2001/1049/oj).

## Recommendations

This chapter addresses specific areas to improve the interoperability and usefulness of NAPs according to chapters 2 and 3 and details parts of chapter 4.

### Focus on users

The NAPs should keep their data consumers in focus. The data and API that NAP provides need to fulfill the use cases of those consumers. It should also make life easier for data producers. Some points to consider are:

  - NAPs should provide easy and free access to the data for the users, including references to the documentation of the data standards and API used.
  - The integration of the data of a NAP should be straightforward and cheap for producers and consumers.
  - The same data pipelines of producers and consumers should work for all NAPs (no additional adaptation needed). This means that data, formats, and authorization must work straightforwardly.
  - The data should be integrated and harmonised within a NAP. This means e.g. that aggregated timetables are provided.

<!-- end list -->

  - The NAPs should be able to detect and inform about quality problems in the data flows (mistakes, incompleteness, delayed delivery).

<!-- end list -->

  - The NAPs should actively pursue registering successful integrations, their results, and the source datasets used. This will automatically give a graph of importance. And visibility for new products and innovations.
  - The NAPs should provide an open issue tracker to report data problems.
  - The NAPs should provide a Quality-of-Service statement for its operation.
  - The NAPs should provide cross-references to relevant other datasets that are temporal or spatial in nature. The new timetable of next year, the timetable of a neighbouring region, or an adjacent data theme.
  - Simple format output: Many use cases can be covered by simpler data formats. The NAPs should generate those from the input stream (e.g. provide a GTFS in addition to NeTEx).
  - Cross-border integration must be supported from the shared data. The NAP should keep in mind that cross-border integration will occur with their data sets. The way to do it should be documented. The best would be to use the same ID for lines, journeys and stops in all shared data and that it is supported in all local systems. Referencing is better than mapping.
  - No special data licenses should be used. The data should be open data with neither (mandatory) registration nor legal restrictions. A regular well documented open data license should be used.
  - Full metadata on each API and dataset should be provided (e.g. \[<https://napcore.eu/metadata/#>:\~:text=mobilityDCAT%2DAP%20provides%20precise%20and,for%20data%20portals%20in%20Europe. mobilityDCAT-AP\] )
  - Links to data usage description, tools, libraries and base information should be provided with the data. The description should be written for user consumption.

### General guidance for responsibilities of a NAP<sup>\[1\]</sup>

The NAP is not only a simple meta data catalogue. Otherwise, it will never fulfill the needs of a European mobility data space. Some essential issues NAP needs to address:

  - The NAP is responsible for delivering all necessary EU/1926/2017 data to consumers. The current situation should be shown.
  - The data is provided in a homogenised, quality-assured way in standard formats.
  - The NAP is responsible for upstream communication about quality issues.
  - The NAP makes quality issues with data sets public.
  - The NAP provides documentation about the data.
  - The NAP is responsible for the metadata of all data sets.
  - The NAP must provide a Quality of Service for the data.
  - The NAP gives guidance on the relevant ID and master data management.
  - The NAP is responsible for the governance of the mobility data space it spans.
  - The NAP should encourage and even require native NeTEx and SIRI from the source system.
  - When the source only provides GTFS, the NAP shall harmonize the ID structure to a national context and provide GTFS. The NAP should not convert GTFS to NeTEx, instead it should give incentives to the data producer to deliver native NeTEx.
  - From the collected NeTEx and SIRI data, the NAP should provide data on less comprehensive formats like GTFS and GTFS RT.

\----<sup>\[1\]</sup> This document, in general, reflects the point of view of DATA4PT experts’ team. Then NAPCORE role (and MS) can use this document or not to make decisions on how to align and improve a NAP.

### General guidance on standards and profiles

The updated Delegated Regulation (EU/2024/490) highlights the connection between profiles and data categories in Articles 4 and 5. It specifies that data should be represented using either minimum EU profiles or national profiles. This guide provides recommendations for parties interested in creating and implementing national profiles in alignment with the Delegated Regulations.

#### Key recommendations for developing national profiles

1\.    Align with the European profile:

○     National profiles must adhere to the European profile to ensure consistency and interoperability across countries.

2\.    Collaborate on a joint maximum profile:

○     National Access Points (NAPs) should work together to create a shared maximum profile for Europe.

○     The EU profile must be fully interoperable (1:1) with this joint maximum profile.

3\.    Avoid profile proliferation:

○     Check existing national profiles before creating a new one.

○     Collaborate with other countries to develop a profile that meets shared needs.

4\.    Process for developing a national profile: If a new national profile is necessary, follow these steps (see Section 5.5 for details):

○     Define the functional scope: Determine the essential requirements and exclude unnecessary elements.

○     Assess existing profiles: Check whether any European or national profiles already meet your needs. Contact CEN experts to explore collaboration opportunities.

○     Develop a new profile (if needed): If no existing profiles are suitable and collaboration is not possible, use the standard to create a new profile. If additional information is required beyond the European profile

  - Check if the needed elements already exist in the full standard. If so, add them to the national profile.
  - If the elements do not exist, propose and specify extensions to the European minimum profile. Coordinate with the organization responsible for the standard to integrate these extensions.

#### Practical considerations

1\.    Interoperability:

○     Ensure European profiles enable easy information exchange.

○     Extensions should allow seamless extraction of interoperable data.

2\.    Resolve ambiguities in profiles:

○     NAPs should provide clear guidance and coordinate with other NAPs to resolve ambiguities uniformly across Europe.

3\.    Expert consultation:

○     If unsure about profiles, consult expert groups responsible for the standards.

4\.    Roadmap and documentation:

○     Maintain a roadmap for profile development and adherence.

○     Clearly document any differences in the profiles and ensure the NAP’s output aligns with them.

By following these guidelines, countries can develop national profiles that align with European standards, fostering interoperability and reducing redundancy across profiles.

### Guidance for National NeTEx and SIRI profile

The data must be able to cover all possible use cases (UC):

  - UC1: Publish data in a NAP to support cross-borders seamless mobility
  - UC2: Publish data in a NAP to feed national operational or passenger information systems – to support interoperability at national level.
  - UC3: Third-party users using data from a NAP can have the need for elements not in the interest for data producers and an NAP. Such data must be provided through an NAP as long as it is part of MMTIS and data exists in a machine-readable format.

The data should be able to cover possible following use cases:

  - UC4: With added extra data, which is not needed for MMTIS, data producers can harvest positive outcomes by using richer data from the NAPs with increased quality in their internal systems.

NeTEx and Siri should be provided according to the relevant European profiles:

  - EPIP:  NeTEx Part 4
  - EPIAP: NeTEx Part 6
  - Fares: NeTEx Part 7 (under development)
  - SIRI European Profile: SIRI Part 7

Open data in the NAP should always follow the most recent or a tagged version from the GitHub repositories for SIRI and NeTEx.

Currently, EPIP is a minimal profile and holds the minimum of data needed for trip planning use, regards MMTIS DR.

There is a need for the NAPs to work towards having one single maximum profile in use<sup>\[1\]</sup>. If extensions in profile are needed, experts should be consulted so that all of Europe does the extension in the same way. If something is needed in EPIP an issue should be created in the issue tracker for EPIP<sup>\[2\]</sup>, NeTEx<sup>\[3\]</sup> or SIRI<sup>\[4\]</sup>. If changes in Transmodel are needed, the relevant CEN experts raise the question further to the Transmodel group.

Neither EPIP nor EPIAP define, if a single or multiple NeTEx files should be exported. The files should be structured for easy loading and validation.

Coverage: datasets should be as complete as possible for a given country or region. The degree of coverage/completeness should be declared per geographical region (e.g. country) in terms of percentages/fractions (e.g. “100 % of trains in country A are covered” and a description of which modes or operators that are missing).

The datasets must provide enough time into the future to allow for most use cases. For example, if tickets are sold up to 120 days in advance, then that is the time horizon that must always be available.

The data must be provided in a manner that allows for cross-region, cross-country integration (see also sections 1.5.7 and 1.5.9). The method of integration needs to be documented. The guidelines in the data dictionary should be followed as well. ----<sup>\[1\]</sup> Inspiration can be found in the Nordic Profile for NeTEx and SIRI, where Norway, Sweden, Finland and Denmark collaborate on one profile,  and datasets that we share is easy to use cross-border, while we add more data needed extending the EU-profile and MMTIS requirements or in the Swiss profile.

<sup>\[2\]</sup> See <https://github.com/NeTEx-CEN/NeTEx-Profile-EPIP/issues>

<sup>\[3\]</sup> See <https://github.com/NeTEx-CEN/NeTEx/issues>

<sup>\[4\]</sup> See <https://github.com/SIRI-CEN/SIRI/issues>

### Guidance for availability of the data in NAP

For NeTEx datasets:

  - Any changes of a timetable are available as soon as possible and at least before the day they start to apply.

For SIRI datasets:

  - Provide at least SIRI-ET, SIRI-SX, SIRI-FM, SIRI-VM.
  - Provide a simple easily accessible request/response API (without requiring filters or subscriptions). A recommendation for event based access to the SIRI data is being worked on in relevant CEN TC 278 WG3 SG7.

### Guidance for documentation

We clarify some points here:

  - A NAP has two target audiences:: PTA or PTO that shall deliver data to the NAP and developers who will use the data. Provide two different sets of documentation.
  - The meta information must be complete, and an evaluation must be made of whether the data will be useful for the use cases the users have in mind.
  - The documentation also includes all relevant information about standards, profiles, XSD etc.
  - Open API test environments should be provided.
  - The documentation does not only describe technical details, but also how to use those.
  - Example code/data is provided and explained.
  - Special cases are laid out.
  - Problems and workarounds should be addressed.
  - The documentation should be provided in an open way.
  - Documentation should provide best practices.
  - NAP should align documentation with other NAPs.
  - Documentation should be in English, other languages are optional.

### Guidance for interoperability

This is only a short note, as most information is addressed in the other sections. When planning the data structures, the NAP should consider:

  - The data sets should integrate with other data in the same NAP (id).
  - It should integrate with data from other NAPs and data domains outside MMTIS.
  - It should integrate cross-border data.

Referencing in those cases is always better than “mapping”. Therefore section 1.5.8 and 1.5.9 are rather important.

### Guidance for geo-referencing

Coordinates should be provided for all elements that can be located. Altitude or level needs to be considered as well when relevant.

The NAP should consider that multiple geo-bases may be used.

If a local map projection is used, WGS84 (latitude, longitude) should still be provided as signed decimal numbers as well.

WGS84 should be provided with 5-6 digits after the comma.

If references exist, they should be mentioned in NeTEx as well (national geo-base and OSM).

### Guidance for consistent IDs across datasets

To enable interoperability between datasets published in an NAP, consistent IDs for relevant elements (such as stop places) are needed. Then the elements can be referenced and there is no need for loss-full matching<sup>\[1\]</sup>. This approach results in the following best practices:

  - Core elements (also mentioned in the MMTIS data dictionary) must have stable IDs. E.g. operators/business units, stops, lines, quays, journey, situation, train number.
  - The ID should be globally unique, also between NAPs.
  - IDs should be stable over time.
  - Changes to the core elements referenced mentioned above should be versioned.
  - A unique and stable ID must be used in the NeTEx ID elements that refer to “real” objects (e.g. StopPlace, but not PassingTime). IDs or mapping tables relating to external systems should only be used *outside* the NeTEx data pipeline or be inserted as keyValue additional information..
  - IDs of other NAPs (when stable and unique) are used and not overwritten.
  - Data producers are responsible for keeping the master data updated (which means also the ID). The NAPs should be encouraged to provide a software platform to do so. The NAPs must do quality assurance and give feedback to the data producers.<sup>\[2\]</sup>
  - IDs must, as far as possible, be the same in all relevant published files (all formats, SIRI, NeTEx, GTFS etc.)​.
  - The NeTEx documentation provides ideas on how to build a unique ID.
  - Uniqueness of journey ID/train number is by operation day and across datasets and over time.
  - The unique ID provided in the data from the NAP should be available to the local source data and systems for easy enhancements by a NAP data consumer.

\----<sup>\[1\]</sup> Matching algorithms may do things wrongly. E.g. they can’t identify the correct line and create a new one or they match to the wrong stop (e.g. because the coordinates are not correct/ambiguous).

<sup>\[2\]</sup> E.g. national stop registry, operator registry, line registry and also a validation pipeline and other services.

### Improve collaboration by building ecosystem of coherent services

To enhance collaboration, data quality, and data usage in the common mobility data space, key software tools—such as validators, libraries, catalogs, and APIs—should be open-source. Since all NAPs face similar challenges, collaboration on software development is encouraged<sup>\[1\]</sup>, following guidelines like those from the Swiss government<sup>\[2\]</sup>.

Each NAP can choose how to develop its systems: by procuring software, hiring a team to develop open-source solutions, or developing open-source software in-house, or a combination of those. Regardless of the approach, procured and open-source systems should be able to work together.

Some countries, like Switzerland and Norway, believe that when this ecosystem is publicly funded, software and code—whether developed or procured— it should be openly available whenever possible<sup>\[3\]</sup>. They believe it ensures a cost-efficient, collaborative, and well-functioning system that provides high-quality open data, easily accessible across all NAPs in Europe. ----<sup>\[1\]</sup> <https://opensource.com/open-source-way>

<sup>\[2\]</sup> Swiss tools for open sourcing code in public administrations: <https://www.bk.admin.ch/bk/en/home/digitale-transformation-ikt-lenkung/bundesarchitektur/open_source_software/hilfsmittel_oss.html>

<sup>\[3\]</sup> See example from Entur <https://github.com/entur>

### Guidance for the usage of non-Transmodel standards

NAP should provide datasets and services for standards widely adopted by large communities. It is also essential that NAP follows European regulations, though using conversion tools is, of course, accepted. However, it is strongly recommended that providers natively support EU formats, with NAP converting to other formats for dissemination purposes.

In cases where providers use other widely supported formats, it can be accepted that the conversion process falls under NAP's responsibility rather than the operators. Such conversions should be considered temporary. For instance, there is a vast ecosystem for GTFS and, for the micro-mobility sector, GBFS is widely used. The adoption of NeTEx/SIRI for micro-mobility is still in its early stages and could be supported and funded by countries. Many software systems already support GBFS and should extend that support to NeTEx/SIRI in the future. Necessary conversion steps can and should be handled by NAP or through tools provided by NAP.

Ideally, the mapping between these standards and the Transmodel ecosystem should already be in place, which is the case for both GBFS and GTFS.

●  [Outline comparison and Mapping between NeTEx and GTFS – June 2024](https://transmodel-cen.eu/wp-content/uploads/2024/08/2024-June_DATA4PT_GTFS-NeTEx-Mapping_vf.pdf)

●  [Methodology for comparing data standards – January 2020](https://transmodel-cen.eu/wp-content/uploads/2024/08/Methodology-for-comparing-data-standards.pdf)

●  [Report on Standards Harmonisation including a GTFS to Transmodel / NeTEx mapping – September 2019](https://transmodel-cen.eu/wp-content/uploads/2024/07/StandardsHarmonisation-2019-njsk-v1.0-1.pdf)

●  [GBFS to NeTEx & SIRI v1.0-  A canonical mapping produced by MobilityData and DATA4PT](https://data4pt.org/w/images/5/5b/Canonical_mapping_-_NeTEx_and_SIRI_new_modes_with_GBFS.pdf)

## Abbreviations and Acronyms

|               |                                                                                     |
| ------------- | ----------------------------------------------------------------------------------- |
| DR            | Delegated Regulation                                                                |
| EPIAP         | European Passenger Information Accessibility Profile (NeTEx part 6)                 |
| EPIP          | European Passenger Information Profile (NeTEx part 4)                               |
| MMTIS         | MultiModal Travel Information Services (EU 2017/1926 and the amendment EU/2024/490) |
| MS            | Members States                                                                      |
| NAP           | National Access Point                                                               |
| NeTEx         | Network Timetable Exchange                                                          |
| OPRA          | OPerating RAw data and statistics exchange                                          |
| PTA           | Public Transport Authorities                                                        |
| PTO           | Public Transport Operators                                                          |
| SIRI          | Service interface for real-time information                                         |
| Source system | The system producing the data for the NAP.                                          |
| TRANSMODEL    | Public Transport Reference Data Model                                               |

## Guidelines Control Sheet

|                            |                                                     |
| -------------------------- | --------------------------------------------------- |
| Type of documentation:     | **Guidelines**                                      |
| Documentation responsible: | Information Technology for Public Transport (ITxPT) |
| Project/ Work package:     | DATA4PT/ WP3                                        |
| Main editor:               | Matthias Günter                                     |

|                              |                                                |
| ---------------------------- | ---------------------------------------------- |
| **Editors and contributors** | **Organisation**                               |
| **Matthias Günter**          | SBB and member of DATA4PT experts' team        |
| **Brede Dammen**             | Entur and member of DATA4PT experts' team      |
| **Anastasia Founta**         | ITxPT and DATA4PT project manager              |
| Ulf Bjersing                 | Hogia and member of DATA4PT experts' team      |
| Christophe Duquesne          | Consultant and member of DATA4PT experts' team |
| Emmanuel De Verdalle         | ITxPT and DATA4PT technical manager            |

|                                 |
| ------------------------------- |
| **Guidelines Revision History** |
| **Modifications Introduced**    |
| **Version**                     |
| **0.0**                         |
| **0.1**                         |
| **0.2**                         |
| **1.0**                         |

-----
