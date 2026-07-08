---
original_title: "SIRI"
source: mediawiki
source_url: https://data4pt.org/wiki/SIRI
last_edited: 2024-03-29T13:21:29Z
status: conversion-failed
---

!!! warning "Raw, unwashed content"
    This page is in the review corpus — copied directly from the source site with only automatic conversion applied. It has not yet been edited for tone, structure, accuracy, or duplication. Do not treat as final.


> **⚠️ Pandoc could not convert this page cleanly.**  
> Error: `Error at "source" (line 65, column 1):`  
> Raw wikitext preserved below for manual cleanup.

```mediawiki

= SIRI overview 🔍 =
== What is SIRI? ==

SIRI is a European standard that enables '''real-time information''' about public transportation to be shared between different '''computer systems'''. It is used by many different organizations, including public transportation operators, traffic management agencies, and travel information providers.

SIRI was established as European standard in October 2006. It is a CEN (Comité Européen de Normalisation) and Technical Standard

== SIRI formats ==

SIRI is a protocol for data exchange between two '''IT systems for real-time information'''. Data can be exchanged via: 

*'''XML files''' (over TCP/IP or via SOAP/WSDL) 

*'''REST/JSON''' (over HTTP) using SIRI-Lite interface 

''Note: SIRI-Lite is a subset of SIRI focusing on the most frequently requested information for open data feeds.''

== What can SIRI be used for? ==

SIRI can be used for a variety of purposes, such as:

*Providing real-time arrival information at bus stops and train stations
*Tracking the progress of individual vehicles
*Managing the movement of buses between different areas
*Synchronizing connections between different services
*Exchanging planned and real-time timetable updates
*Distributing status messages about the operation of services
*Providing performance information to operational history and other management systems

== Benefits of SIRI ==

SIRI has made a significant contribution to improving the efficiency and reliability of public transportation across Europe. It is now used by millions of people every day to plan their journeys and get real-time information about the services they are using.

For example, SIRI can help you to:

*Avoid missing a bus or train
*Plan your journey more efficiently
*Get real-time information about disruptions to services
*Find the best way to travel between different locations


ℹ️ To find out more about the '''SIRI data model''', please visit the [http://www.transmodel-cen.eu/standards/siri/ Transmodel page] and [https://siri-cen.eu/ SIRI page].



= Software & tools 🧰 =

The following list of software is known to support NeTEx. We distinguish between different categories that may later receive a list of key performance indicators.

== XML tools ==
General purpose XML tools can be used to work with the SIRI XML schema and XML documents that conform to it.

{| class="wikitable" style="width : 10%"
|-
! XML tools
! Description
|-
|[http://www.altova.com/xmlspy.html XML SPY] || commercial
|-
|[http://www.oxygenxml.com/ Oxygen]|| commercial
|-
|[http://www.garshol.priv.no/download/xmltools/ List of tools] || open-source
|-
{| class="wikitable"

== Conversion and connectors tools ==

{| class="wikitable" style="width :60%"
! colspan="1" | Name
! Availability
! colspan="1" |Description
! colspan="1" |Profile
! colspan="1" |License
|-
| style="text-align:center |'''[https://github.com/entur/anshar Anshar]''' ||style="text-align:center |✅ || Java based tool to connect, validate and redistribute SIRI. (Act as a national aggreagation hub for all SIRI feeds in Norway)  || Norwegian ||EUPL
|-
|style="text-align:center | '''[https://github.com/OneBusAway/onebusaway-siri OneBusAway SIRI]''' || style="text-align:center |✅ ||A set of tools to connect to and convert SIRI.  ||  ||Apache-2.0
|-
|style="text-align:center | [https://bitbucket.org/enroute-mobi/ara/src/master/ ara] || style="text-align:center |✅ ||A set of tools to connect, convert and store SIRI, SIRI-Lite. || ||Apache-2.0
|-
|style="text-align:center | [https://github.com/afimb/irys irys] ||style="text-align:center |✅ ||A set of tools to connect and redistribute SIRI. || || CeCILL-B
|-
|[https://mobilitx.diginext.fr/ Diginext/CS-Group] ||style="text-align:center |✅ || || ||
|-
|style="text-align:center | [https://www.lumiplan.com/produit/mobiflux/ Soridis/Lumiplan] || style="text-align:center |✅ || || ||
|-
|style="text-align:center | [https://qommute.com Qommute] ||style="text-align:center |✅ || || ||
|-
|}

== Data validation tools ==

{| class="wikitable" style="width : 30%"
!  Name
! Availability
!  Description
! Profile
! License
|-
| style="text-align:center |'''[https://github.com/department-for-transport-BODS/bods BODS]''' || style="text-align:center |✅ ||Validator of TransXChange and SIRI-VM ||All ||Open Source  
|-
|}

==Producers from CAD/AVL==

{| class="wikitable" style="width : 30%"
!colspan="1"|Name
!colspan="1"|Availability
!colspan="1"|Description
!colspan="1"|Profile
!colspan="1"|License
|-
|style="text-align:left;" rowspan="1"|[https://www.ivu.com/products-and-solutions/ivusuite/passenger-information.html IVU.realtime] ||style="text-align:center;"  |✅ ||Producer of realtime data. || ||Commercial
|-
|style="text-align:left;" rowspan="1"|[https://www.initse.com/fileadmin/user_upload/Content/3_Solutions/3_Operations/MOBILE-ITCS_us.pdf Mobile-ITCS] ||style="text-align:center;"  |✅ ||Producer of realtime data. || ||Commercial
|-
|style="text-align:left;" rowspan="1"|INEO ||style="text-align:center;"  |✅ || || ||
|-
|style="text-align:left;" rowspan="1"|Navocap ||style="text-align:center;"  |✅ || || ||
|-
|style="text-align:left;" rowspan="1"|[https://zenbus.fr/ ZenBus] ||style="text-align:center;"  |✅ ||Producer of realtime data. || ||Commercial
|-
|style="text-align:left;" rowspan="1"|[https://www.ratpsmartsystems.com/hopen-go/ IXXI/RATP Smart System] ||style="text-align:center;"  |✅ ||Producer of realtime data. || ||Commercial
|-
|style="text-align:left;" rowspan="1"|Alstom ||style="text-align:center;"  |✅ ||Producer of realtime data. || ||Commercial
|-
|}

= SIRI extension for 🆕 Modes =
In line with '''NeTEx Part 5''', corresponding extensions are made in SIRI for real time data such as current number of available vehicles, current number of spaces available to bring back a vehicle or to park, etc. SIRI also provide updates of positions (typically for free floating vehicles). The SIRI Facility Monitoring (FM) service is extended to provide this counted information

{| class="wikitable" style="width: 40%;"
|-
!
!Description
|-
| '''[https://www.netex-cen.eu/wp-content/uploads/2021/03/NeTEx-extension-for-New-Modes-Detailed-Scope-v04.pdf NeTEx extension for New Modes]''' || Scope and overview
|-
| '''[https://data4pt.org/w/images/5/5b/Canonical_mapping_-_NeTEx_and_SIRI_new_modes_with_GBFS.pdf Canonical mapping with GBFS]'''
| The EU-funded project DATA4PT and MobilityData experts have released a high-level mapping between the General Bikeshare Feed Specification (GBFS) and Transmodel to support better interoperability of shared mobility data feeds.
|-
|}

= References =

{| class="wikitable" style="width : 30%"
|-
!Name
!Description
|-
| '''[https://github.com/SIRI-CEN/SIRI SIRI-CEN GitHub]'''
| Find xsd, examples and relevant documentation on SIRI schema
|-
| '''[https://www.transmodel-cen.eu/ Transmodel website]'''
| European data model for public transport information
|-
| '''[https://www.siri-cen.eu/ SIRI website]'''
| Official SIRI website
|-
|}
```
