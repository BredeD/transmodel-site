---
original_title: "Vehicle scheduling tutorial"
source: wordpress
source_url: https://transmodel-cen.eu/index.php/vehicle-scheduling-tutorial/
slug: vehicle-scheduling-tutorial
parent_id: 0
published: 2024-07-11 13:29:35
status: raw
---

!!! warning "Raw, unwashed content"
    This page is in the review corpus — copied directly from the source site with only automatic conversion applied. It has not yet been edited for tone, structure, accuracy, or duplication. Do not treat as final.


*You can check the online version or download the pdf version [TUTORIAL-Part1-3: 2016](../../assets/files/TUTORIAL-Part1-3-v0.2-1.pdf). Note that the pdf includes also other two tutorials, also available in online version ([Common ](https://mockuptm.itforpt.be/index.php/common-concepts/)[Concepts EN12896 -1](https://mockuptm.itforpt.be/index.php/common-concepts/) and [Public Transport Network EN12896 – 2](https://mockuptm.itforpt.be/index.php/network-description-tutorial/)).*

# Tutorial: Vehicle scheduling

<span>What does the Vehicle Scheduling domain cover?</span>

Chaining vehicle journeys into blocks of vehicle operations is one of the main functions of vehicle scheduling.

The corresponding entities and relationships included in the reference data model allow a comprehensive description of the data needs associated with this functionality, independently of the particular methods and algorithms applied by the different software systems.

<span>What is Vehicle Service?</span>

A VEHICLE SERVICE is the workplan for a vehicle for a whole day, planned for a specific DAY TYPE

<span>What is a Block?</span>

A BLOCK is the work of a vehicle from the time it leaves a PARKING POINT after parking until its next return to park at a PARKING POINT. Any subsequent departure from a PARKING POINT after parking marks the start of a new BLOCK.

A BLOCK includes, in particular, all VEHICLE JOURNEYs (SERVICE JOURNEYs and DEAD RUNs) planned for this period. It also may include SPECIAL SERVICEs. A pause may be added between two journeys or services. Linked to this concept is the concept of COURSE OF JOURNEYS: a part of a BLOCK composed of consecutive VEHICLE JOURNEYs defined for the same DAY TYPE, all operated on the same LINE.

<span>How does Transmodel represent vehicle services for rail operation?</span>

Vehicles of the type TRAIN or COMPOUND TRAIN may be coupled or separated. For the corresponding journeys, COUPLED JOURNEYs or JOURNEY PARTs are created.

A BLOCK PART is a part of a BLOCK corresponding to the different JOURNEY PARTs of the VEHICLE JOURNEYs in a BLOCK.

One or several vehicle BLOCKs may be coupled together for a while. The entity COMPOUND BLOCK represents the work of a vehicle during the time it is coupled to one or more vehicles. If two different vehicles are coupled at a certain point (e.g. a terminus), a COMPOUND BLOCK is created from that instant on. If this COMPOUND BLOCK is joined by a third BLOCK, coupled later at another point, a new COMPOUND BLOCK is formed from that instant on. If one of the BLOCKs is separated before the COMPOUND BLOCK returns to the GARAGE, another COMPOUND BLOCK is formed, composed of the two BLOCKs corresponding to the coupled vehicles.
