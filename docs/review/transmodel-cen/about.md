---
original_title: "About"
source: wordpress
source_url: https://transmodel-cen.eu/index.php/about/
slug: about
parent_id: 0
published: 2024-02-23 15:11:26
status: raw
---

!!! warning "Raw, unwashed content"
    This page is in the review corpus — copied directly from the source site with only automatic conversion applied. It has not yet been edited for tone, structure, accuracy, or duplication. Do not treat as final.


## What is Transmodel?

### **“Transmodel” is the short name for the European Standard “Public Transport Reference Data Model” **(EN 12896).** **

Transmodel is a conceptual data model providing a specification of : 

  - data elements: entities,  
  - data definitions: clear semantics of the entities,  
  - main characteristics of the entities: main attributes,  
  - data structures: relationships between entities,  

dedicated to describe the public transport domain and underpin public transport information systems. 

Transmodel gives a semantic interoperability this mean, that a concept bears the same and unique semantics for any Transmodel domain, any Transmodel-based application.

![Figure 1: Transmodel keyword is semantic interoperability.](../../assets/images/transmodel-cen/TransmodelSemanticInteroperability-768x631.png)

### **Transmodel covers all Public Transport modes **

'Public transport' has to be understood as services advertised and available for use by the general public, carried out by any mean of transport.  

The 'transport means' on their turn may be characterised in terms of types of operation (methods/modes of operation). Transmodel coverage is described in terms of 'modes of operation' rather than in terms of 'transport means'.  

EN12896 v6.2 distinguishes the following types of 'mode of operation': 

  - **conventional mode of operation**: the legacy method of operation which is provided as a scheduled and/or flexible publicly advertised flexible transport offer. This method of operation is either following a fixed schedule and fixed routes or linked to a fixed network/schedule but offering flexibility, in order for instance, to optimise the service or to satisfy passenger demand; 
  - **alternative mode of operation**: any publicly advertised mode of operation different from the conventional mode of operation, in particular vehicle sharing, vehicle rental and vehicle pooling; and 
  - personal mode of operation: a private mode of transport excluding any publicly advertised use.  

### **Transmodel V 6.2 is dedicated to the conventional and the alternative mode of operation.  **

![Figure 2: Example of the different mode of operation for NeTEx](../../assets/images/transmodel-cen/NeTEx-part5-768x541.png)

### **Transmodel is a European norm **

Transmodel is recognised since 2009 as a European norm and is published in 10 parts under the reference number EN12896-Part 1 to 10. 

### **Transmodel covers most of the Public Transport sub-domains **

Transmodel considers a subdivision of the public transport into the following data domains: 

  - public transport network definition: routes, lines, journey patterns, timing patterns, service patterns, scheduled stop points and stop places, but also parking (EN 12896-Part 2) 
  - timing information and vehicle scheduling: runtimes, vehicle journeys, day type-related vehicle schedules (EN 12896 - Part 3) 
  - operations monitoring and control: operating day-related data, vehicle follow-up, control actions (EN 12896 - Part 4)  
  - fare management: fare structure and access rights definition, sales, validation, control (N 12896 – Part 5) 
  - passenger information (planned and real-time) (N 12896 - Part 6) 
  - driver management (N 12896 - Part 7):
      - driver scheduling (day-type related driver schedules); 
      - rostering (ordering of driver duties into sequences according to some chosen methods); 
      - driving personnel disposition (assignment of logical drivers to physical drivers and recording of driver performance). 
  - management information and statistics (including data dedicated to service performance indicators) (N 12896 - Part 8); 
  - management of the alternative modes of operation: vehicle pooling, vehicle sharing, vehicle rental, taxi (N 12896 - Part 10). 

The data modules dedicated to cover most functions of the above domains are specified.  

Several concepts are shared by the different functional domains. This data domain is called 'Common Concepts' (N 12896 - Part 1). 

Part 9 contains didactic and informative documentation.  

The different parts are related to the implementations NeTEx (scheduled data), SIRI (real-time data), OpRa (historical/observed data), OJP (Trip planning API) as shown in the figure below: 

![Figure 3: Architecture of the different Parts of Transmodel](../../assets/images/transmodel-cen/BubbleChartTransmodelUpdate0724-1024x576.jpg)

[Purpose](https://transmodel-cen.eu/index.php/purpose/) [Transmodel at a glance](https://transmodel-cen.eu/index.php/transmodel-at-a-glance/) [Governance](https://transmodel-cen.eu/index.php/governance/)
