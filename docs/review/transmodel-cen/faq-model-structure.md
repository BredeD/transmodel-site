---
original_title: "FAQ Model Structure"
source: wordpress
source_url: https://transmodel-cen.eu/index.php/faq-model-structure/
slug: faq-model-structure
parent_id: 0
published: 2024-05-24 14:32:05
status: raw
---

!!! warning "Raw, unwashed content"
    This page is in the review corpus — copied directly from the source site with only automatic conversion applied. It has not yet been edited for tone, structure, accuracy, or duplication. Do not treat as final.


## Model Structure

<span>What means “Common Concepts”?</span>

Several concepts are shared by the different functional domains covered by Transmodel. This data domain is called “Common Concepts”.

<span>What types of “Common Concepts” are taken into account?</span>

“Reference Data Model – Common Concepts” domain incorporates data structures used by all other data domains of Transmodel. It is composed of the following data packages:

  - Versions and Validity: describes the successive versions of data elements and the conditions to be attached to elements to precisely know when they should be used;
  - Responsibility: describes the type of responsibility or role the different organisations may have over the data;
  - Generic Framework: describes a number of generic objects and representational mechanisms that are not specific to transport but which are specialized or used by Transmodel transport related objects.
  - Reusable Components: certain common low-level components, for example TRANSPORT MODE, SERVICE CALENDAR, DAY TYPE, etc. are not specific to any particular functional part of Transmodel but are widely used in several different functional areas.
  - Explicit Frames referring to generic data: describes the mechanisms useful to build coherent sets of versioned data. Part 1 presents explicit frames for data referring to the Common Concepts domain.

<span>What aspects of “Network Topology” are represented in Transmodel?</span>

Public Transport Network incorporates data structures which form the network topology description of Transmodel V5.1 and the major part of the fixed objects model of IFOPT. It is composed of three data packages:

  - Network Description: routes, lines, journey patterns, flexible routes and lines, specific point types;
  - Fixed Objects: sites, stop places, equipment, parking places;
  - Tactical Planning Components: journey patterns, timing patterns, service patterns, connections, common sections.

<span>What aspects of “Timing Information” are represented in Transmodel?</span>

  - Vehicle Journeys , Service Journeys, Coupled Journeys, Flexible Service,
  - Journey Times and Journey Patterns Times, Interchanges and Interchange Rules,
  - Dated Journeys, Timetables Passing Times, Dated Passing Times.

<span>What aspects of “Vehicle Scheduling” are represented in Transmodel?</span>

Based on the Timing Information model, Vehicle service, i.e. the workplan for a vehicle for a whole day, planned for a specific DAY TYPE is described in terms of BLOCKs, i.e. of the work of a vehicle from the time it leaves a PARKING POINT after parking until its next return to park at a PARKING POINT.

<span>What is the purpose of the “frames” of Transmodel?</span>

In order to facilitate the management of information, data in an information system may be associated in groups of data, which share the same validity conditions. Such a group of data is described by a VERSION FRAME.
