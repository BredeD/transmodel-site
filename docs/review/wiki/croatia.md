---
original_title: "Croatia"
source: mediawiki
source_url: https://data4pt.org/wiki/Croatia
last_edited: 2024-09-25T13:01:00Z
status: raw
---

!!! warning "Raw, unwashed content"
    This page is in the review corpus — copied directly from the source site with only automatic conversion applied. It has not yet been edited for tone, structure, accuracy, or duplication. Do not treat as final.


## Overview in the National Level

The national NeTEx profile of Croatia was created within the project of Implementation of NAP for multimodal traffic information and development of a local journey planner which took place in 2022 from March to November.

The following documents were used to implement the Croatian national profile for NeTEx (also available via Croatian Institute for Standards).

  - CEN/TS 16614-1:2020 Public transport - Network and Timetable Exchange (NeTEx) - Part 1: Public transport network topology exchange format.
      - “white paper” NeTEx-Network-WhitePaper\_1.08 which describes NeTEx network concept in a non-expert way.
  - CEN/TS 16614-2:2020 Public transport - Network and Timetable Exchange (NeTEx) - Part 2: Public transport scheduled timetables exchange.
      - “white paper” 09.NeTEx-Timetable-WhitePaper\_1.05 which describes NeTEx timetable in a non-expert way.
  - CEN/TS 16614-4:2020 Public transport - Network and Timetable Exchange (NeTEx) - Part 4: Passenger Information European Profile.

Within the project of Implementation of NAP for multimodal traffic information and development of a local journey planner, an internal tool was created to convert GTFS files to NeTEx due to the lack of PTA/PTO providers that have a machine-readable format.

Some of the PTA/PTO providers are on the national and some on regional level, and due to various completeness of data provided we had issues with compliance.

Besides city centres, Croatia can be divided in three areas, central, maritime, and mountainous regions. From the perspective of data quality and available applications, central and maritime areas are more covered with quality data than mountainous region since they are driven by greater touristic demand.

Level of digitalization of PTA/PTO data is rather low. Where exist, different standards are used, with GTFS prevailing as the most used data format. Further activities must be made in order to raise the level of data digitalisation within stakeholders, to hold the stakeholders to recognize benefits of data sharing and to ensure provision in EU support and recommended formats. Croatia has already started several projects in order to fulfil goals, with results already being visible with inclusion of more data sources in standardized format in Croatian NAP.

The basic concepts for EPIP are described in the data dictionary in CEN/TS 16614-4: 2020 Public transport - Network and Timetable Data Exchange (NeTEx) - Part 4: Passenger Information European Profile.

The main terminology used to describe the topology of the public transport network are:

  - ROUTE: an ordered list of discrete locations as a route point that geographically defines a single route passing through a road (or rail) network.  ROUTE can pass through the same point of the route multiple times. ROUTE LINK can be used to connect ROUTE POINT points along the way.
  - JOURNEY PATTERN: defined as an organized SCHEDULED STOP POINT (e.g. **teyes** where passengers enter and exit) and TIMING POINTS (i.e.  information on the time required for the preparation of timetables) on each ROUTE describing the pattern of operation of public transport vehicles. Journey Pattern can go through the same point multiple times.
  - TIMING PATTERN: redo sequence TIMING POINTS for each JOURNEY PATTERN determined by TIMING PATTERN.  The sequence scheduled stop points (from journey pattern) is determined by the SERVICE PATTERN.  Service Pattern (= variant ROUTE) is a subset of a JOURNEY PATTERN consisting of a stop point sequence.

A line (LINE) is usually defined as the sum of multiple ROUTEs with a public label (name, number).  From a topological point of view ROUTS are usually very similar because the versions are basic ROUTE with some deviations. Two routes that share the same infrastructure path (or parallel path), but with the opposite orientation usually belong to the same LINE.

An XML document is a physical record of public passenger transport data used for the exchange between sender and recipient of EPIP-compliant data.

It is recommended that the XML document name be written as follows:

  - The name of the document (prefix) is NETEX\_PI
  - The main version of EPIP; currently 01
  - ISO 3166-2 Country Code
  - Sender name (use NAP if data comes from National access point)
  - Document type (LINE, NETWORK , or STOP)
      - LINE: The document contains a description of one line: line number or name if no number is available (short name, fewer than 15 characters, made only of letters (uppercase and lowercase), numbers and "-")
      - NETWORK: Document contains a description of two or more lines
      - STOP: Document contains a description of all stops

<!-- end list -->

  - Date Created (YYMMDD)

<!-- end list -->

  - All fields are separated by a "\_" character.

## Use cases

During the implementation of the NAP for multimodal traffic information and the development of a local journey planner, GTFS files were primarily transposed into NeTEx files. Currently, at NAP, data from several PTA/PTO providers (GPP Osijek, ZET, Pulapromet – bus, HŽ – train, and Jadrolinija – ferry) are available in the NeTEx standard. Additionally, the LJP was developed with all available PTA/PTO data. More information are accessible [here](https://www.promet-info.hr/ljp/?lang=en).

In Croatia, the following projects utilize NeTEx and Datex standards:

  - **Smart City Rijeka, City of Rijeka - CEKOM Project**: Application of NeTEx and Datex standards for traffic management and passenger information.
  - **OLGA Green and Holistic Airport, City of Zagreb**: Application of NeTEx and Datex standards for traffic management and public transport optimization.
  - **Traffic Management System, City of Split**: Application of NeTEx and Datex standards for traffic management and passenger information.

### Outcome

Most NAP users have expressed a strong interest in accessing PTA/PTO data, making it essential to ensure that all data available on NAP is updated in a timely manner, which is not always the case currently.

The implementation results have facilitated easier data exchange among various stakeholders. The harmonization of standards has led to the development of uniform applications, reducing the need for integrating non-standard data from third-party providers. This has decreased application development costs and increased the reusability of applications.
