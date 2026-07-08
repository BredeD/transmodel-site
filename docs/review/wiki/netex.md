---
original_title: "NeTEX"
source: mediawiki
source_url: https://data4pt.org/wiki/NeTEX
last_edited: 2026-03-23T13:19:38Z
status: conversion-failed
---

!!! warning "Raw, unwashed content"
    This page is in the review corpus — copied directly from the source site with only automatic conversion applied. It has not yet been edited for tone, structure, accuracy, or duplication. Do not treat as final.


> **⚠️ Pandoc could not convert this page cleanly.**  
> Error: `Error at "source" (line 65, column 1):`  
> Raw wikitext preserved below for manual cleanup.

```mediawiki

= NeTEx overview 🔍 =
== What is NeTEx? ==

[[File:NeTEx.png|250px|right|]]

NeTEx (Network Exchange format) is a standard for exchanging public transport network, schedules, and related data. It is a general-purpose XML format designed for the efficient exchange of complex transport data among distributed systems.

It has been developed under the aegis of CEN (Comité Européen de Normalisation) and is the most recent development stage in over fifteen years work to systemise and harmonize European passenger information data.

NeTEx can be used to collect and integrate data from many different stakeholders, and to reintegrate it as it evolves through successive versions. It is used by public transport operators and IT providers across Europe to support a wide range of passenger information and operational applications.

== Benefits of using NeTEx ==

NeTEx offers a number of benefits, including:

* '''Flexibility''': NeTEx can be used to represent a wide range of public transport data, including networks, schedules, fares, and real-time information.
* '''Extensibility''': NeTEx can be extended to support new types of data and functionality.
* '''Interoperability''': NeTEx is a standard format, which means that data can be exchanged between different systems without the need for custom development.
* '''Support for modern web services architectures''' : NeTEx can be used to develop modern, web-based passenger information and operational applications.

== Examples of NeTEx in use ==

NeTEx is used in a variety of ways across the public transport industry. For example:

*'''Passenger information''': NeTEx can be used to provide real-time arrival and departure information to passengers, generate timetables and journey planners, and develop mobile apps for passengers.
*'''Operational applications''': NeTEx can be used to manage fleet operations, integrate public transport data with other systems, such as traffic management systems and navigation apps, and support planning and analysis.


ℹ️ To find out more about the NeTEX data model, visit the [https://transmodel-cen.eu/ Transmodel website].

= NeTEx European Passenger Information Profile 🇪🇺 =

{| class="wikitable"
!
! Description
! Documentation
|-
|width="150px" style="text-align:center |'''NeTEx EPIP'''|| Ideally, all member states will provide NeTEx files according to the European Passenger Information Profile (EPIP) on their respective National Access Point. Data4PT provides some artefacts to simplify producing and quality assure such information. EPIP-adapted version of the full NeTEx XML schema has been produced.
Moreover, since the official NeTEx schema is too large and complex for C# code generation tools to handle, a simplified version was created for application development. This schema has been reduced to only match the scope of the EPIP Profile (European Passenger Information Profile). It is compliant with the main NeTEx schema, but does not contain constraint checks and should not be used for validation.
| The documentation is available at the NeTEx GitHub repository [https://github.com/NeTEx-CEN/NeTEx-Profile-EPIP here]
|}


= Software & tools 🧰 =

An ecosystem of NeTEx XML tools is under development, including both open-source and commercial products.

The following list of software is known to support NeTEx. We distinguish between different categories that may later receive a list of key performance indicators.

== XML tools ==
General purpose XML tools can be used to work with the NeTEx XML schema and XML documents that conform to it.

{| class="wikitable" style="width : 10%"
|-
!  width="80px"|XML tools
!  width="80px"|Description
|-
|[http://www.altova.com/xmlspy.html XML SPY] || commercial
|-
|[http://www.oxygenxml.com/ Oxygen]|| commercial
|-
|[http://www.garshol.priv.no/download/xmltools/ List of tools] || open-source
|-
{| class="wikitable"

== Conversion tools ==

{| class="wikitable" style="width:80%"
! colspan="1" | Name
! Availability
! width="40%" | |Description
! colspan="1" |Profile
!width="20%"| License
|-
| style="text-align:center |'''[https://github.com/entur/netex-protobuf netex-protobuf]''' ||style="text-align:center |✅ || NeTEx to protobuf converter || All ||EUPL
|-
|style="text-align:center | '''[https://github.com/CanalTP/transit_model/tree/master/gtfs2netexfr gtfs2netexfr]''' || style="text-align:center |✅ ||Export GTFS data to NeTEx. ||French    ||    
|-
| style="text-align:center |'''[https://github.com/skinkie/hastus hastus]''' || style="text-align:center |✅ ||Giro Hastus OIG script to export NeTEx from a system, in addition can export crew operations. ||Dutch, Nordic(?) || AGPL-3.0
|-
| style="text-align:center |'''[https://gitlab.com/labiangashi/josm-plugin-netex-converter/ josm-plugin-netex-converter]''' ||style="text-align:center |✅ || Export OpenStreetMap pedestrian routing information into NeTEx.||    || GPL 2.0   
|-
| style="text-align:center |'''[https://github.com/entur/netex-gtfs-converter-java netex-gtfs-converter-java]''' ||style="text-align:center |✅ || Export NeTEx data to GTFS ||Nordic ||EUPL
|-
|style="text-align:center |'''[https://github.com/cefriel/chimera Chimera]''' ||style="text-align:center |✅ || Chimera is a framework for semantic data transformation pipelines. A converter between GTFS and NeTEx has been implemented adopting an intermediate Transmodel representation. ||Nordic (ready), EPIP/Italian (ongoing) || Framework – Apache License 2.0, Mapping GTFS-NeTEx – Proprietary license
|-
|style="text-align:center |'''[https://www.openmove.com/ OpenMove ATLAS]''' || style="text-align:center |✅ || The management platform OpenMove ATLAS allows import and editing of data in GTFS format and export also in GTFS or NeTEx format (currently the Italian Profile is supported, other profiles can be implemented on request). || EPIP Italian ||Proprietary license
|-
|style="text-align:center |'''[https://developers.italia.it/it/software/a4c48ddf-7156-4327-a62b-66fc15f1c6f3 GTFS2NeTEx-converter]''' ||style="text-align:center |✅ || Converts GTFS data in NeTEx Italian Profile. || EPIP Italian Profile  ||EUPL 1.2
|}

== Data validation tools ==

{| class="wikitable" style="width:40%;"
! width="25%" | Name
!width="10%" | Availability
! width="40%"|  Description
!width="10%" | Profile
!width="10%" | License
|-
| style="text-align:center |'''[http://www.xmlsoft.org/ XMLlint]''' || style="text-align:center |✅ ||XML syntax validation, XSD schema validation and constraint checking. ||All ||MIT  
|-
|style="text-align:center | ''' The Data4PT Validation tool''' ||style="text-align:center |✅||The tool is under maintenance in the framework of [https://napcore.eu/ NAPCORE]. ||All ||
|-
| style="text-align:center |'''[https://github.com/entur/netex-validator-java NeTEx validator java]''' ||style="text-align:center |✅|| Validation library for NeTEx data, analyzing and reporting schema compliance. ||Nordic ||
|-
| style="text-align:center |'''[https://github.com/entur/antu Antu]''' ||style="text-align:center |✅|| Validate NeTEx datasets against the Nordic NeTEx Profile. ||Nordic || 	
|}

== Language bindings ==
{| class="wikitable" style="width: 45%;"
! Name
! Availability
! Description
! Profile
! License
|-
| style="text-align:center |'''[https://github.com/entur/netex-java-model netex-java-model]''' || style="text-align:center |✅ ||NeTEx XML bindings for Java, with additions to map temporal types to native objects. ||All ||EUPL
|-
|style="text-align:center | '''netex-csharp-model''' ||style="text-align:center |❌ || NeTEx XML bindings for C#. Currently being researched with a variety of tools.<br>Contact DATA4PT if you have questions or have found the golden egg. ||All ||
|-
|style="text-align:center | '''[https://github.com/entur/netex-parser-java netex-parser-java]''' ||style="text-align:center |✅||Parse NeTEx files and lookup entities in an index ||Nordic ||EUPL
|-
|}

== Editing /Management & visualisation tools ==

{| class="wikitable" style="width: 75%;"
! Name
! Availability
! Description
! Profile
! License
! URL
|-
| style="text-align:center | '''Nplan''' ||style="text-align:center | ✅|| Java backend / TypeScript frontend for create/edit/export of NeTEx data (Support both Timetable based and On-demand polygon based services) ||Nordic ||EUPL ||backend - https://github.com/entur/uttu <br> frontend - https://github.com/entur/enki
|-
|style="text-align:center |'''NSR''' ||style="text-align:center | ✅|| Java backend / JavaScript frontend for import/creation/edit/export for NeTEx stops data. (Act as a National Stops Register for the whole of Norway) || Nordic ||EUPL ||backend - https://github.com/entur/tiamat <br> frontend - https://github.com/entur/abzu
|-
| style="text-align:center |'''Chouette'''|| style="text-align:center |✅|| Java backend / Ruby frontend for import/validation/edit/export of NeTEx data. Highly modified version of the old AFIMB version of Chouette. NOTE: Legacy software not recommended for new implemetations ||Nordic ||CeCILL-B ||backend - https://github.com/entur/chouette <br> frontend -  https://github.com/entur/chouette2
|-
|style="text-align:center |'''[https://enroute.mobi/produits/chouette/ Chouette]''' ||style="text-align:center | ✅|| Java based NeTEx tools, transforms between profiles and standards (NeTEx, GTFS, Neptune). ||EPIP ||Apache 2.0 ||
|-
|style="text-align:center |'''[https://mobilitx.diginext.fr/ mobilitx]''' || style="text-align:center |✅|| || || ||
|-
|style="text-align:center |'''[https://www.lumiplan.com/produit/mobiref/ mobiref]''' ||style="text-align:center | ✅ || || || ||
|-
|style="text-align:center |'''NeTEx Reader''' ||style="text-align:center | ⏳ ||C# based XML tool based on Giro Hastus XSD || Dutch || ||https://www.youtube.com/watch?v=mpb_1Y9uR5k
|-
|style="text-align:center |'''netexconv2''' || style="text-align:center |⏳ ||Java based NeTEx tools, transforms between profiles and standards (NeTEx, DINO, HAFAS, KV1, GTFS). || Dutch, EPIP, Nordic, VDV462 || ||
|-
|style="text-align:center | '''[https://www.ivu.com/news/news/article/delfi-successfully-migrates-to-ivucloud.html IVU.cloud]''' || style="text-align:center |✅|| ||EPIP || ||
|-
|style="text-align:center |'''[https://www.pluservice.net/it/soluzioni/gestione-rete-e-turni Motus]''' ||style="text-align:center | ✅|| 4Motus is the Fleet Scheduling Management System provided by Pluservice. The application is designed by independent and integrated modules which can be activated according to specific operational needs. <br> One of the latest module created and already available is the generation of NeTEx datasets starting from the operational data collected by public transport operators. For this purpose, Motus receives the input data starting from a GTFS and it is able to enrich  these data with further relevant information such as contracts, vehicles. Then Motus transforms these data into the NeTEx Italian profile.<br> '''Data model:''' the database is designed according to Transmodel specifications, European reference standard (EN12896) for public  transport. ||Italian || ||
|-
|}

== Journey planning engine ==

{| class="wikitable" style="width: 60%;"
!  Name
! Availability
! Description
! Profile
! License
|-
| style="text-align:center | '''[http://docs.opentripplanner.org/en/dev-2.x/Netex-Norway/ OpenTripPlanner]''' || style="text-align:center |✅||Timetable and shortest path journey planner supporting reading various input formats including GTFS and NeTEx. || Nordic || Apache 2.0
|-
| style="text-align:center | '''[https://openmove.com/technology/trip-planning/ OpenMove]''' ||style="text-align:center | ✅ ||Multimodal, intermodal trip planner with real-time capabilities, step-by-step instructions, fare system, and compatibility with market standards. ||  ||
|-
|}

==Planning system supporting native NeTEx export ==

{| class="wikitable" style="width: 25%;"
!Name
!Availability
!Developped by
!Profile
!Additional documentation
|-
|style="text-align:center | [https://www.giro.ca/en-ca/our-solutions/segments/public-transport/ Hastus] || style="text-align:center |✅ || Giro || Nordic <br> Dutch || Dutch patch: https://github.com/skinkie/hastus 
|-
|style="text-align:center |  [https://www.trapezegroup.com.au/solutions/intelligent-transport-systems-bus Intelligent Transport Systems (ITS) for Bus]  || style="text-align:center |✅|| Trapeze  ||EPIP Nordic  || Blog post: https://www.trapezegroup.com.au/blog/its-netex-bus-data-transfer-exchange 
|-
| style="text-align:center | [https://www.datagrafikk.no/?tag=dgbuss  DG Buss] || style="text-align:center |✅ || Datagrafikk  || Nordic || 
|-
| style="text-align:center | [https://www.trapezegroup.com.au/solutions/planning-and-scheduling-rail  Planning & Scheduling for Train]  ||style="text-align:center |✅ || Trapeze ||Nordic ||
|-
| style="text-align:center | [https://www.ivu.com/solutions#c4826  IVU.suite] || style="text-align:center |⏳ || IVU for public transport ||Nordic ||Blog post: https://www.ivu.com/all-references/references/delfi-migrates-to-ivucloud
|-
| style="text-align:center | [https://turnit.com/ Turnit Ride] ||style="text-align:center |✅ ||Turnit for public transport ||Nordic ||
|-
|style="text-align:center | Nplan ||style="text-align:center |✅ ||Entur for public transport ||Nordic || backend: https://github.com/entur/uttu  <br> frontend: https://github.com/entur/enki 
|-
| style="text-align:center | [https://www.hacon.de/en/portfolio/timetable-construction-disposition/  TPs Suite] ||style="text-align:center | ✅ ||Hacon ||Nordic ||
|}

= NeTEx part 5 for 🆕 modes =

NeTEx Part 5 is an extension to the NeTEx data exchange format that is specifically designed for publishing data about "alternative modes" of transportation, such as car sharing, cycle sharing, carpooling, and car/cycle rental. It is primarily oriented towards static data, such as the service that is offered and the associated infrastructure.

''NeTEx Part 5 is now available as '''CEN/TS 16614-5:2022 (E)'''''
[[File:NeTEx-part5.png|400px|right|]]

{| class="wikitable" style="width: 50%;"
|-
!
!Description
|-
| '''[https://github.com/NeTEx-CEN/NeTEx/tree/master/xsd/netex_part_5 Technical artefacts]''' || The XML schema (XSD) for NeTEx Part 5 New Modes. Examples are also provided, along with other useful documentation.
|-
| '''[https://data4pt.org/w/images/5/5b/Canonical_mapping_-_NeTEx_and_SIRI_new_modes_with_GBFS.pdf Canonical mapping with GBFS]'''
| The EU-funded project DATA4PT and MobilityData experts have released a high-level mapping between the General Bikeshare Feed Specification (GBFS) and Transmodel to support better interoperability of shared mobility data feeds.
|-
|}

= References =

{| class="wikitable" style="width: 35%;"
|-
!Name
!Description
|-
| '''[https://github.com/NeTEx-CEN/NeTEx NeTEx-CEN GitHub]'''
| Find xsd, examples and relevant documentation on NeTEx schema
|-
| '''[https://github.com/NeTEx-CEN/NeTEx-Profile-EPIP NeTEx EPIP profile GitHub]'''
| Find xsd and relevant documentation dedicated on NeTEx EPIP schema
|-
| '''[https://netex-cen.eu/ NeTEx Website]'''
| Find general information on NeTEx project
|-
|}
```
