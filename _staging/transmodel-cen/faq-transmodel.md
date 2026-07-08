---
original_title: "FAQ Transmodel"
source: wordpress
source_url: https://transmodel-cen.eu/index.php/faq-transmodel/
slug: faq-transmodel
parent_id: 0
published: 2024-02-23 15:02:41
status: raw
---

# Transmodel FAQ

<span>What is Transmodel?​</span>

Transmodel is the European Reference Data Model for public transport and constitutes a data structure specification dedicated to public transport companies and other providers of services related to the process of passenger transportation (planning, operation and information), to suppliers of software products supporting these processes, and to consultants and other experts acting in the field of public transport in the widest sense.

The reference data model, developed at conceptual level, can support the development of software applications, their interaction or combination in an integrated information system, and the system‘s organisation and information management which rules the utilisation of the existing telematics environment in a company (or group of companies) running computer applications supporting the different functional areas of public transport.

<span>Who are the potential users of Transmodel?</span>

Transmodel may prove of value to:

  - *organisations within the public transport industry that specify, acquire and operate *information systems: Transmodel may be distilled, refined, or adapted to form a comprehensive data model for the organisation. This will enable the organisation to specify its *database structures and/or its system interfaces*, in such a way that separate modules can be openly tendered but will still integrate easily.

<!-- end list -->

  - *organisations that design, develop and supply* information systems for the public transport industry: Transmodel may be adapted to form a comprehensive *data model for the product suite*. This will enable the organisation to develop its products in such a way that separate modules will integrate easily, but also so that they may be sold separately to clients seeking Transmodel-compliant systems.

<span>What help does Transmodel provide?​</span>

As a reference standard, it is not necessary for individual systems or specifications to implement Transmodel as a whole. It is possible to describe for those elements of systems, interfaces and specifications which fall within the scope of Transmodel:

  - the aspects of Transmodel that they have adopted;
  - the aspects of Transmodel that they have chosen NOT to adopt.

<span>In what situations is Transmodel useful?​</span>

Transmodel may be applied to any framework for information systems within the public transport industry, but there are three circumstances to which it is particularly suited:

  - specification of an organisation’s ‘information architecture’;
  - specification of a database;
  - specification of a data exchange interface.

<span>What functional areas are covered by Transmodel?​</span>

The Reference Data Model (Transmodel) covers the following data domains:

  - Network Description: routes, lines, journey patterns, timing patterns, service patterns, scheduled stop points and stop places, navigation paths, equipment and facilities;
  - Timing Information and Vehicle Scheduling: passing times, runtimes, vehicle journeys, day type-related vehicle schedules;
  - Fare Management: fare structure and access rights definition, sales, validation, control of access rights and/or travel documents; 
  - Passenger Information: planned and real time, passenger trips;
      - Operations Monitoring and Control: data related to operating days, vehicle follow-up, control actions;
  - Driver Management:
      - Driver Scheduling: definition of day-type related driver schedules,
      - Rostering: ordering of driver duties into sequences according to some chosen methods,
      - Driving Personnel Disposition: assignment of logical drivers to physical drivers and recording of driver performance.
  - Management Information and Statistics: registered, observed raw data dedicated to the calculation of service performance indicators; 
  - Alternative modes management: data specific to vehicle pooling (i.e. ride sharing), vehicle sharing, vehicle rental. 

<span>How to get the latest version of the model for work with modern tools?​</span>

Transmodel is a conceptual model, developed and presented in UML. It may be used for the tackle the definition of a data base schema or data exchange messages, however, Transmodel task is not implementation but the definition of a conceptual based on UML (Enterprise Architect was used to create it) of the different public transport domains. The UML model is available from the Transmodel Web Site.

<span>What are the main implementations of the Transmodel?​</span>

Here are two standardized data exchange formats derived from Transmodel: SIRI and NeTEx. These projects have used submodels of Transmodel to generate physical models and xml schemas. One more implementation using Transmodelhas also been published as a CEN standard: Open API for Distributed Planing Systems. Another implementation related to the observed operational data is under development: Operational Raw Data exchange.

As regards the concrete locations where the different implementations of the Transmodel-derived standards NeTEx, SIRI, OJP have taken place. It can be consulted [here](https://transmodel-cen.eu/index.php/existing-implementation/).

<span>Is there a scheduled date for the document's release of the updated Transmodel parts?​</span>

Yes, there is a staged approach in the Transmodel update process.

Part 1- Common Concepts, Part 2- Public transport Network and Part 3 – Timing Information & Vehicle scheduling documents have already been published.

Part 4: Operations Monitoring and Control and Part 5: Fare Management documents have been released end of 2017.

Part 6: Passenger Information and Part 7: Driver Management early Part 8 – Management Information and Statistics have been published mid 2018.

Part 9: Informative Documentation has been published in 2019, and Part 10: Alternative Modes, in 2023.

<span>What do I need to do in order to get a copy of the complete documentation for v5.1 and v6?​</span>

Since Transmodel is a CEN standard, to get the documentation you have to contact your national standardisation body.

<span>Is Transmodel free of charge?</span>

Transmodel documentation is distributed by national standardisation bodies which determine documentation price.  
A further use is free of charge.
