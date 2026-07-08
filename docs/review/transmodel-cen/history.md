---
original_title: "History"
source: wordpress
source_url: https://transmodel-cen.eu/index.php/history/
slug: history
parent_id: 0
published: 2024-02-23 14:58:47
status: raw
---

!!! warning "Raw, unwashed content"
    This page is in the review corpus — copied directly from the source site with only automatic conversion applied. It has not yet been edited for tone, structure, accuracy, or duplication. Do not treat as final.


# History

Transmodel has been developed within a range of European projects from several European Programmes (Drive I, Drive II, TAP), with the support of the European Commission (DGXIII), national public institutions, in particular of the French Ministry of Transport (Direction des Transports Terrestres), and private companies.

More details about last Transmodel udpates [here](https://mockuptm.itforpt.be/index.php/2024/07/17/what-is-new-in-transmodel/).

## 2023: New developments​

The projects  

  - CoRoM (Coordination & standardisation for Rail & Mobility)  dedicated to Fares and Sales Transactions , and  
  - OpRa+ for the development of data exchange format of operational observed raw data 

Are considering Transmodel v6.2 and may bring further enhancements or requirements in particular as regards Transmodel Part 6 (queries), 8 (operational raw data) or 9 (informative documentation). 

![](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image-520x1024.png)

## 2023 - ...: Transmodel v 6.2

The update of Transmodel v6 (mostly for the Parts 1 to 8) has been undertaken by CEN TC278 WG3:

  - to proceed to a simplification of the documentation, a consolidation of Part 1 (common concepts, spread through several documents),
  - to provide a range of functional extensions (additional models) and
  - to enhance the coherence within the Transmodel ecosystem in particular between Transmodel and its derived implementations NeTEx, SIRI, OJP, OpRa.

The CEN publication is foreseen by 2025.

**Harmonisation and Interopability.** The CoRoM project (Coordination & standardisation for Rail & Mobility) funded by the European Commission is undertaking work on fare data with the objective of recommendations  to achieve interoperability of fare data in OSDM for rail with Transmodel-based and other formats mainly in the context of distribution APIs.

The project work on comparing OSDM and other formats will lead to the publication of a Technical Report for the building of Purchase (including basic after sales) interfaces using Transmodel. It should also result in updates for Transmodel Parts 5 and 6. 

![](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image-520x1024.png)

## 2020 - 2021: Transmodel v6 – Part 10

Based on the grant agreements between CEN and the European Commission, work on Transmodel continued. One of the main tasks for the work was the integration of data structures for the so called "new modes" or "alternative modes" (such as car-pooling or cycle sharing).

The project Team 1711 of CEN TC278 WG17 (Mobility Integration) published by 2020 the CEN/TS 17413 entitled "Intelligent transport systems - Urban ITS - Models and definitions for new modes". This specification provided a first model to represent the data structures related to vehicle pooling, vehicle sharing, vehicle rental.

In a second step, this input has been enhanced by CEN TC278 WG3 which took it over to publish it by 2021 as EN12986 - Part 10: Alternative modes (with the reference EN12896-10).

![](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image-520x1024.png)

## 2020 - 2021: Harmonisation and Interoperability

**UIC / CEN working group.** A working group with UIC (*Union Internationale des chemins de fer*, International Union of railways) and CEN compared the OSDM (Open Sales and Distribution Model) data format for rail timetables with Transmodel/NeTEx and established a mapping of data elements.

In the domain of fares management, the working group provided a report providing an analysis of the two approaches demonstrating that mappings were possible between two approaches and that a certain level of interoperability was possible. The report identified differences which require further harmonisation work in the future.

The main identified gap is related to the management of combined fare products (transparency, openness and completeness). Transmodel allows for the publication through NeTEx of the available combined access rights (fare products) together with all parameters related to them. OSDM provides the end user with the combined fare product on-line i.e. after a "combination process" by the allocator. The combinations are not published in advance. Not all the rules and restrictions are published in machine readable form.

To continue work in this field, the European Commission provided funding for the project CoRoM,  whichstarted in 2023.

**MobilityData / CEN informal liaison.** Informal liaison with MobilityData, the organisation maintaining the General Bike Sharing Specification (GBFS), established a mapping of core data elements used by GBFS to a subset of Transmodel / NeTEx.

The informal liaison between MobilityData and CEN experts was conducted under the aegis of the European project Data4PT in the context of the publication of NeTEx Part 5 as a direct implementation of Transmodel Part 10.

![](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image-520x1024.png)

## 2019 - 2020: Mobility Integration group and Alternative modes

The description of the data structures related to the so called “new modes” or “alternative modes” has been initiated in the CEN working Group 17 (Mobility Integration).

A first data model based on Transmodel v6.1 has been published in 2020 as CEN/TS 17413:2020 under the title Intelligent transport systems — Urban ITS — Models and definitions for new modes. 

This specification constituted the basis of Transmodel Part 10: Public transport –Reference data model: Alternative modes: 2023

![](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image-520x1024.png)

## OJP (Open API for Distributed Journey Planning) ​

OJP specification published as CEN TS 17118 and developed by 2017 has been implemented in several locations. This version diverged at least as regards the part representing the Trip structure from Transmodel Part 6- Public transport – Reference Data model – Passenger Information (V6.1).  At the occasion of the development of OJP v2.0, an effort of alignment of Transmodel Part 6 (Trip model) and the OJP data structures took place (2022-2023)   

The result of this effort is present in Transmodel-Part 6 v6.2 and OJP v2.0. 

![](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image-520x1024.png)

## 2017 – 2020: Harmonisation and Interoperability

A further study commissioned by the European Rail Authority (ERA) in 2017 compared the contents of the TAP TSI B.1, B.2 and B.3 data formats for standard domestic rail fares with the NeTEx fare management models and established a mapping of rail data. It also looked at published urban fare products for bus, local rail and metro in over 20 European countries to ascertain whether all commonly found products could be expressed with the Transmodel/NeTEx representation. It identified a small number of gaps in Transmodel/NeTEx which were subsequently addressed in Transmodel 6.0 and 6.2 (for example, deck and seating plans)

As part of the initiative to harmonise European data standards, a comparison of Transmodel with the relevant parts of the INSPIRE family geospatial standards to ensure interoperability of address and location data.

A European Profile for exchanging timetables in NeTEx (European Passenger Information Profile, EPIP) using a subset of the Transmodel/NeTEx representation was developed for the use of European National Access Points.

Informal liaison with the General Transit Feed Specification (GTFS) group established a mapping of GTFS Schedule content to a subset of Transmodel / NeTEx for basic timetables.

![](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image-520x1024.png)

## 2017 – 2019: Transmodel v6 – Part 4 to 9

**Inputs.** The Project Team 0302 (also referred to as PT0302) of CEN took over the functional extensions of Transmodel v5.1 provided by the NeTEx project and continued the work. This led to the publication of the rest of the Transmodel series of normative documents:

  - EN12986 - Part 4: Operations Monitoring and Control (with the reference EN12896-4),
  - EN12986 - Part 5: Fare Management (with the reference EN12896-5),
  - EN12986 - Part 6: Passenger Information (with the reference EN12896-6),
  - EN12986 - Part 7: Driver Management (with the reference EN12896-7),
  - EN12986 - Part 8: Management Information and Statistics (with the reference EN12896-8).

The Project team also published an informative document as part of the Transmodel series: TR12986 - Part 9: informative documentation ((with the reference EN12896-9). It is a Technical Report that gathers all informative documentation needed for organisations looking into implementing Transmodel as their reference data model.

The project also delivered several tutorials, position papers, and presentations published on the Transmodel official website ([www.transmodel-cen.eu](http://www.transmodel-cen.eu)). To be noted that the website was created by the Project team and is still active to this date.

**Contributors and Sponsors.** The Project team 0302 was composed of a group of experts from:

  - France: Kasia Bourée, Christophe Duquesne,
  - Italy: Fabrizio Arneodo,
  - Slovenia: Andrej Tibaut,
  - Sweden: Ulf Bjersing,
  - United Kingdom: Nicholas Knowles, Stuart Reynolds.

The work organisation and funding were based on a Specific Agreement between CEN and the European Commission (Grant Agreement for an Action SA/CEN/GROW/EFTA/000/2015-06) which assigned the tasks to the Project Team 0302. They provided input to the CEN standardization work via their participation in the CEN TC278 WG3.

![](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image-520x1024.png)

## 2016: Transmodel v6 – Part 1 to 3

**Inputs.** The extensions of Transmodel v5.1 brought by the NeTEx project, in particular the integration of the Fixed Objects model (IFOPT) were the main inputs for this series of changes made to Transmodel. To facilitate its understanding, it has been decided to modularise the model.

It resulted in the 2016 publication of Transmodel as a series of documents with:

  - EN12986 - Part 1: Common Concepts (with the reference EN12896-1),
  - EN12986 - Part 2: Public Transport Network Topology (with the reference EN12896-2),
  - EN12986 - Part 3: Timing Information and Vehicle Scheduling (with the reference EN12896-3).

It can be seen as the first step of having a modular reference data model as it is known today.

**Contributors and Sponsor.** The 2016 publication was partly supported by the French Ministry of Transport.

![](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image-520x1024.png)

## Legal adoption

Transmodel was legally recognised as the reference data model for public transport in the European Union when mentioned in its legal framework for Intelligent Transport Systems (ITS). The latter are recognised as vital to increase safety and tackle Europe's growing emission and congestion problems. They can make transport safer, more efficient and more sustainable by applying various information and communication technologies to all modes of passenger and freight transport.

For all modes of passenger transport, the legal framework comprises of:

  - Directive 2010/40/EU of the European Parliament and of the Council of 7 July 2010 on the framework for the deployment of Intelligent Transport Systems in the field of road transport and for interfaces with other modes of transport, referred to as the “ITS Directive”;
  - Commission Delegated Regulation (EU) 2017/1926 of 31 May 2017 supplementing Directive 2010/40/EU of the European Parliament and of the Council with regard to the provision of EU-wide multimodal travel information services, referred to as the “MMTIS Delegated Regulation”.

It is the latter that directly references Transmodel in its introduction. Direct references to Transmodel derived implementation standards NeTEx and SIRI can be found in the subsequent article of the MMITS Delegated Regulation.

![](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image-520x1024.png)

## 2008 – 2019: Harmonisation and Interoperability

A study commissioned by the European Rail Authority (ERA) under the aegis of Stefan Jugelt compared the contents of UIC and TAP station and timetable standards with Transmodel/NeTEx timetable models. It resulted in a mapping of UIC and TAP rail formats.

![](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image-520x1024.png)

## 2009 - 2014: NeTEx (Network Timetable Exchange)

The project defining NeTEx ran between 2009 and 2013. It was designed to develop standard interfaces between systems aiming at the exchanges of network topology and timetable data based on the models EN12896:2006 and EN28701:2009.

One of NeTEx project main deliverables was to bring together both models (Transmodel v5.1 and IFOPT). It resulted is one single conceptual model covering the domains network topology, timing information, and information on fares.

![](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image-520x1024.png)

## 2006 - 2016: IFOPT

The [**IFOPT**](https://www.transmodel-cen.eu/standards/ifopt/) (Identification of Fixed Objects in Public Transport) project used EN12896:2006 as an input to develop a logical data model for the fixed objects relevant for public transport, in particular for stops and points of interest. IFOPT has established an implicit link to EN12896:2006 and has been published as EN28701:2009. IFOPT has been revised and incorporated (withdrawn from the list of standards) into Transmodel v6 (EN12896:2016) and the subsequent versions.

![](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image-520x1024.png)

## 2006 - ...: SIRI

The [SIRI](https://www.transmodel-cen.eu/standards/siri/) (Standard Interface for Real-time Information) project used EN12896:2006 as an input to develop standard interfaces for the exchange of real-time data for passenger information. Three parts of [SIRI](https://www.transmodel-cen.eu/standards/siri/) have been updated in 2013/14 and published as the Standard EN15531-1 to 3, whilst a further parts remain as the Technical Specifications TS15531-4, 5 and 6. The extensions formulated by the [SIRI](https://www.transmodel-cen.eu/standards/siri/) group are intended to be taken into account in the relevant parts of the update to Transmodel.

![](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image-520x1024.png)

## 2006: Publication of Transmodel v5.1

This period of work was dedicated to the harmonisation of Transmodel with SIRI (Service Interface for Real-time Information), which is a derived implementation of Transmodel designed to facilitate the exchange of real-time information in Public Transport systems.

![](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image-520x1024.png)

## 2004 - 2005: Harmonisation and Interoperability

This period of work was dedicated to the harmonisation of Transmodel with SIRI (Service Interface for Real-time Information), which is a derived implementation of Transmodel designed to facilitate the exchange of real-time information in Public Transport systems.

![](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image-520x1024.png)

## 2002 - 2003: Transmodel v5.1

Inputs. During the years 2002 and 2003, the CEN kept on convening TC278 WG3 SG4, mostly to work on how the data model should be taken forward. It considered the following inputs for consolidation:

  - Previous drafts of Transmodel,
  - Deliverables of the projects SITP and SITP2,
  - The German VDV specifications, and
  - A range of projects conducted in the United Kingdom.

They covered all the work required for Transmodel v5.1 to be adopted as EN12896. Further documentation of their work can be found, in French, at <http://www.billettique.fr/spip.php?rubrique18>.

Contributors and sponsors. The TC278 WG3 SG4 was led by the Department for Transport (United Kingdom) with participants from:

  - VDV (Germany),
  - RATP (France),
  - HÜR (Denmark),
  - Setec ITS (France),
  - TRUST E.E.I.G. (Transmodel Users’ Support Team) (France and Germany), and
  - Centaur Consulting (United Kingdom).

![](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image-520x1024.png)

## 1999 - 2002: SITP 1 and 2 projects

Inputs. The French-led project SITP (Système d'Information Transport Public) built on the pre-standard ENV 12896 (issued May 1997) and the results of the EC project Titan. It was conducted from 1996 to 1997. It was tasked to produce the required extension of ENV 12896. The project results were approved between 1999 and 2000.

A successor project, SITP2, developed the standard further between 2001 and 2002.

Contributors and sponsors. The SITP project and its successor were sponsored by:

  - The French Ministry of Transport (Direction des Transports Terrestres – DTT),
  - The companies
      - Gemplus (France)
      - Setec ITS (France),
  - The Transmodel Users’ Support Team EEIG (France and Germany).

![](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image-520x1024.png)

## 1996 - 1998: Titan project

Inputs. The EU-project Titan focused on validation, real-scale implementation and further development of the pre-standard ENV 12896.

Contributors and sponsors. The organisations listed below have technically contributed to the Titan project:

  - CETE-Méditerranée (France),
  - Üstra (Germany),
  - OASA (Greece),
  - RATP (France),
  - SLTC (France),
  - Salzburger Stadtwerke AG (Austria),
  - TransExpert (France),
  - TransTeC (Germany),
  - Synergy (Greece),
  - TRUST EEIG (Germany).

The sponsoring partner of the project was the French Ministry of Transport (DTT/SAE). The project was co-funded by the European Communities and some of the partners, in particular the pilot sites – Lyon (France), Hanover (Germany) and Salzburg (Austria).

![](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image-520x1024.png)

## 1992 - 1994: Transmodel v4.1

**Inputs.** The pre-standard ENV 12896 was drafted by both:

  - The “Transmodel” work area of the EU-project EuroBus (1992-1994);
  - The “Harpist” taskforce of the EU-project DRIVE II (1995).

The joining of both the Transmodel and Harpist kernel team resulted in the establishment of the Subgroup 4 (SG4) of CEN TC278 Working Group 3 (WG3). It was led by TransExpert (from France).

The results of these projects were based upon earlier results delivered by the Drive I Cassiope project (1989-1991) and the existing ÖPNV data model for public transport, a German national standard.

The pre-standard reflected the contents of deliverable C1 of the Harpist taskforce, published in May 1995, with modifications resulting from the discussion process in CEN TC278/WG3 between May and October 1995.

Contributors and sponsors. The organisations listed below have technically contributed to the preparation of the pre-standard ENV 12896. They were the consortium partners involved in both the EuroBus project/Transmodel work area and the DRIVE II project/Harpist taskforce. 

They are:

  - Beachcroft Systems (UK),
  - CETE-méditerranée (France),
  - CTA Systems (Netherlands),,
  - Ingénieur Conseil Bruno Bert (France),
  - Koninklijk Nederlands Vervoer (Netherlands),
  - Leeds University (UK),
  -  Régie des Transports de Marseille (France),
  - SNV Studiengesellschaft Verkehr (Germany),
  - Stuttgarter Straßenbahnen AG (Germany),
  - TransExpert (France),
  - TransTeC (Germany), and
  - VSN Groep (Netherlands).

The sponsors of the project were:

  - The European Communities (EC, DG XIII, F/5, Drive Programme, 1992-94),
  - The French Ministry of Transportation,
  - The Dutch Ministry of Transportation, and
  - The German Federal Ministry of Research and Technology.

![Vertical-Line-PNG-HD-Image](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image.png "Vertical-Line-PNG-HD-Image")

## 1989 - 1991: Cassiope

**Transmodel** development started with the [**Cassiope**](https://www.transmodel-cen.eu/overview/history/cassiope/) project (1989-1991, Drive I programme). Cassiope results were then considerably enriched by the [**EuroBus**](https://www.transmodel-cen.eu/overview/history/eurobus/) and [**Harpist**](https://www.transmodel-cen.eu/overview/history/harpist/) projects (Drive II).

![Vertical-Line-PNG-HD-Image](../../assets/images/transmodel-cen/Vertical-Line-PNG-HD-Image.png "Vertical-Line-PNG-HD-Image")
