---
original_title: "FAQ NeTEx"
source: wordpress
source_url: https://transmodel-cen.eu/index.php/faq-netex/
slug: faq-netex
parent_id: 0
published: 2024-02-23 15:02:55
status: raw
---

# NeTEx General FAQ

<span>Why to use NeTEx rather than the other similar standards?​</span>

In general, Transmodel family of standards, including NeTEx, are very strongly placed, in that they have a uniform, joined up, modular model that offer several key benefits:

**On the technical front**

Ιt is a multimodal model built of reusable components that are rich enough to cover both upstream and downstream requirements. It provides a way to have a consistent description of all modes (including Vehicle Sharing and Pooling), and their relations (connection, bus station at train station, vehicle sharing station close to bus station, etc. etc.), where all other standards are unrelated silos.

It is designed to be extensible. It has a model driven design that allows impact analysis to be done properly and has a modular implementation framework that can be further subtyped and otherwise added to.

Τhe use of uniform components reduces complexity, giving headroom to add further capability. 

It is designed to be customizable via profiles. With the definition of profiles NeTEx fit to national/local needs.

Ιt is developed and checked by gathering the knowledge of experts from most EU countries, reaching high quality and consistency, overcoming the risk of shortcoming and mistakes that a locally defined data exchange protocol may encompasses.

**On the business front**

The statutory requirements for NAPs provide a driving business case. Transmodel ecosystem is the regulated standard to be used in EU territory, based on the ITS Directive 2017/1926.

The support of the European commission to develop supporting resources is helpful for reducing the barriers to entry and building critical mass.

The development of open-source components and tools \[ch3\] further improve the economics.

NeTEx can be standalone with no dependencies with SIRI, and vice versa but it is highly recommended to combine them.

NeTEx can be applied in many different use cases that surpass the passenger information, like the operational data (AVMS), fares data, scheduling and production plan. Note: There is available training material where NeTEx functional scope and use cases are presented, [here](https://data4pt-project.eu/knowledge-database/training-material/).

<span>What is the recommended process for developing or reviewing the national NeTEx profiles?​</span>

A profile is a subset of the standard defined to be used for a specific use case. For the countries that are now under the development of their first NeTEx national profile, we recommend staying as close as possible to the European Passenger Information Profile which includes the minimum information to be shared across countries for passenger information. More EU minimum profiles regarding Accessibility elements and Fares are now under development in the framework of DATA4PT project and will be published soon with the aim to support the countries in enhancing the type of the information that can be exchanged.

**Key steps to follow**

1.    Use as basis the EU official minimum profiles. More specifically start with the EPI Profile and the relevant documentation. In the DATA4PT website you will find the graphic documentation, the XSD and an XML example regarding EPIP (https://data4pt-project.eu/knowledge-database/ stay). Moreover, we recommend you to watch the dedicated to EPIP webinar available [here](https://data4pt-project.eu/knowledge-database/training-material/).

2.    Clearly identify the national specific needs to be managed and added to the EPIP profile in order to fulfill country’s requirements.

3.    Learn from others by analyzing their profiles and checking their examples. Currently, a list of countries with available national profiles is available [here](https://data4pt.org/wiki/NeTEX#National_profiles) . Examine which of the functionalities applied in other countries also fit to your needs and they can be adopted.

4.    Check the full NeTEx XSD and what elements/objects are included and reply to your needs. In case there is no available element, there is a possibility of providing the information under other elements. It is often possible to add more info to an element by using the keyList/KeyValue construction.

5.    Create examples and perform a first level validation by using XML validators such as Oxygen, SPY and other commercial tools.

6.    Ask for feedback from [DATA4PT experts’ team.](https://data4pt-project.eu/requests-requirements/)

Also keep in mind that conversion from an existing format is always possible, but if it looks like an easy first step, that may not be the easiest way to collect all the needed information (needs or increasing very fast).

<span>How widely NeTEx is used currently?​</span>

Given that many countries already have their own Transmodel based national standards for exchanging timetable data, there wasn’t initially much of a business case for most countries to start using NeTEx in earnest. So, in the first instance what we mainly saw was tools just adding NeTEx timetable export which is relatively simple to do if you are Transmodel based in the first place. 

A real business case is the **example of Norway** where they wanted to rebuild their entire national transport data infrastructure. The standard has been adopted with notable success and speed. The **EU directives for National Access Points (NAPs)** are of course changing this picture by creating a statutory requirement and you can already find initial NeTEx stop and timetable data sets on many countries’ National Access Points.

But there is still some way to go. A standard needs a whole ecology to be in widespread use so there is inevitably a bootstrapping problem, and for a new subdomain such as fare data. XML also presents a challenge to some developers.

Examples of countries that currently provide their data in NeTEx format are:

  -   -   - [Norway](https://data.transportportal.no/datasets?lang=en)
          - [Luxembourg](https://data.public.lu/en/datasets/)
          - [Sweden](https://www.trafiklab.se/api/trafiklab-apis/netex-regional/)
          - [France](https://transport.data.gouv.fr/?locale=en)
          - [Austria](https://www.mobilitydata.gv.at/en)
          - [Netherlands](http://data.ndovloket.nl/)

Full list of European National Access Points regarding MMTIS Delegated Regulation 1926/2017 (action ‘a’) is available [here](https://ec.europa.eu/transport/sites/default/files/its-national-access-points.pdf).

<span>Can NeTEx describe journey connection times?</span>

In order to provide accurate journey plans, it is valuable to be able to specify realistic connection times between journeys at interchanges that take into account the mode of transport, the detailed topology of the interchange and even the mobility of the user (for example a path suitable for a wheelchair using a lift may take longer). NeTEx allows both default and specific transfers time to be specified for any connection.

NeTEx also permits complex operational rules about journey interchanges to be described so that planned and guaranteed connections can be managed and so that real time systems and real-time journey planners can give accurate advice to users.

<span>Does NeTEx support accessibility?</span>

Yes, NeTEx supports the specification of accessibility attributes on both the fixed infrastructure (drawn from the CEN IFOPT standard) and on vehicle types used for specific journeys, so that full accessibility aware journey planning can be provided, including micro-navigation through interchanges. Both accessibility properties and equipment for different disabilities (e.g. wheelchair spaces, navigability, tactile strips etc) and accessibility services (e.g. boarding assistance) can be defined. Furthermore, NeTEx defines a set of user needs (e.g.  wheelchair, blindness, push chairs, etc) that a journey planning engine can use to set criteria to find the optimal journey for a given set of accessibility criteria. 

<span>Can I integrate data from different countries with NeTEx?</span>

Yes, one of the strengths of NeTEx is that it takes a global view of data identification, allowing data elements from different name spaces to be exchanged in the same schema.

For more technical information about the different standards of transmodel check the FAQ pages of the [DATA4PT wiki](https://data4pt.org/w/index.php?title=FAQ_NeTEX).
