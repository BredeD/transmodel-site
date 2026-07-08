---
original_title: "FAQ"
source: mediawiki
source_url: https://data4pt.org/wiki/FAQ
last_edited: 2023-02-09T11:53:02Z
status: raw
---

## General questions

### Why so many standards?

We can find explanations for why there are many and divers PT standards in both the functional scope involved, some specific technology needs, and of course history.

#### Functional scope

Public transport encompasses many functions and many stakeholders; from the very small to very large; and operating in quite different modes, so naturally its data requirements span many different categories of data and many different use cases. **Superficial discussion on the subject often tends to focus on a few specific categories of data that people are familiar with** from their own use of using public transport, such as timetables, or real time departures, **but they are of course only part of the wider picture.** There are many other aspects to running a transport system, from **managing the network infrastructure to planning and scheduling**, through to the **collecting of fares,** each needing the exchange of data. '''Informing the public with passenger information requires just a few categories out of many others.

#### Technology needs

An important point to note is that the different functions have an evolving temporal dimension – with different process taking place, before, during and after travel and this means that **different technologies are needed to handle the real-time and dynamic aspects of a system as opposed to the static aspects.**

**Each different category of information thus has its own inherent submodel** (for example for, stops, timetables, tariff structures, control, etc), and in most legacy formats has had different formats. Furthermore, the protocols that are efficient for the occasional bulk exchange of static or slow changing reference data are quite different from the protocols best suited for dynamic APIs, so we need two separate families of standards for gathering and for delivering data.

#### History

History is also instructive. If you look at what has been happening over the past 20 years, we see that in the late 1990’s we started out with numerous separate national formats as well as quite a few proprietary formats, mostly mode specific (predominately rail), not all very well documented and not all open or easy to extend. Over time, thanks to **Transmodel, a gradual alignment of terminology and concepts** allowed a common conceptual model to emerge in the early 2000’s, which in turn allowed **a new generation of European national timetable standards to be developed** that adopted the common terminology and took advantage of the reusable concepts that had been developed to simplify their representations.

By the end of the decade, the various national timetable formats were close enough to consider creating a common XML format, to cover the network and timetables. This was done creating NeTEx, though there wasn’t actually a pressing business case for anyone to move to it and most countries concentrated on the uptake of their own still quite new national standards. On the API front , an early win was the development of the SIRI real-time API which was based on the German VDV 453 , harmonised to use the Transmodel terminology. This replaced a number of different national standards and is by now in widespread use in many European countries. APIs are of course easier and quicker to implement than bulk exchange formats  since they are views over existing data sets and data feeds and SIRI was . New data sets requiring a much bigger investment in database and tools to create data.

No country has a standard format for exchanging multimodal fare data, yet alone one that can describe the sophisticated new types of electronic fare product made possible by smartcards and mobile devices. The Transmodel fare model was implemented as a further module of NeTEx to cover this gap. Although it is a distinct module   of NeTEx and has a large submodel of its own , it reuses existing NeTEx components for example stops, zones and lines and operators , where ever possible

So even if there are still a confusingly number of PT standards out there, there are a great deal fewer than there would be if we hadn’t already made progress in standardisation.

### What is the difference between the different standards/formats?

Standardisations can take many flavours. You may have standardised designs, standards for protocols at different levels in the technology stack, standard formats for exchanging data, or even meta standards, that is standards for writing standards or for using a particular technology. Thus, **different standards may apply at different levels of abstraction**.

An important case in point is Transmodel itself: Transmodel isn’t a concrete format. It operates at a more abstract level, providing a common set of concepts and data structures with which to describe public transport entities and their relationships. As such it has a **critical role as a unifying framework from which to develop concrete standards**. But it means that when we consider a given format we are actually dealing with two standards at the same time. The good news is that Transmodel spans the entire domain – there is only one conceptual standard\!

**Concrete exchange formats and protocols necessarily have a smaller scope**. And can be placed within the “bigger picture” A standard with relatively broad scope, such as NeTEx, actually needs to be carefully modularised so that it can be used selectively.

Considering the wider context of what we are really aiming at, that of **gathering information from many sources to build useful applications**, we see that we **need exchange formats not just for the “downstream” processes that deliver information to the passenger**. But also, for the **“upstream” processes that create and manage the data in the first place**.

Although there are many common components, these **upstream processes contain additional concepts that don’t need to be in the downstream data sets**. For example when you are creating schedules you need to know the times over the links of a network in order to work out the timings that will ultimately  be shown the passenger in the finalised timetable. Downstream formats may use simplified views.  However with the massive grown in mobile devices and smart mobility apps, **the long-term trend is to want more sophisticated function in the downstream systems too**. It is there for **attractive to have a richer format than can be used selectively in multiple different use cases.**

## NeTEx related questions

### Why to use NeTEx rather than the other similar standards?

In general, Transmodel family of standards, including NeTEx, are very strongly placed, in that they have a uniform, joined up, modular model that offer several key benefits:

#### On the technical front

  - Ιt is a multimodal model built of reusable components that are rich enough to cover both upstream and downstream requirements. It provides a way to have a consistent description of all modes (including Vehicle Sharing and Pooling), and their relations (connection, bus station at train station, vehicle sharing station close to bus station, etc. etc.), where all other standards are unrelated silos.
  - It is designed to be extensible. It has a model driven design that allows impact analysis to be done properly and has a modular implementation framework that can be further subtyped and otherwise added to.
  - Τhe use of uniform components reduces complexity, giving headroom to add further capability. 
  - It is designed to be customizable via profiles. With the definition of profiles NeTEx fit to national/local needs.
  - Ιt is developed and checked by gathering the knowledge of experts from most EU countries, reaching high quality and consistency, overcoming the risk of shortcoming and mistakes that a locally defined data exchange protocol may encompasses.

#### On the business front

  - The statutory requirements for NAPs provide a driving business case. Transmodel ecosystem is the regulated standard to be used in EU territory, based on the ITS Directive 2017/1926.
  - The support of the European commission to develop supporting resources is helpful for reducing the barriers to entry and building critical mass.
  - The development of open-source components and tools \[ch3\] further improve the economics.
  - NeTEx can be standalone with no dependencies with SIRI, and vice versa but **it is highly recommended to combine them.**
  - NeTEx can be applied in many different use cases that surpass the passenger information, like the operational data (AVMS), fares data, scheduling and production plan. Note: There is available training material where NeTEx functional scope and use cases are presented, [here](https://data4pt-project.eu/knowledge-database/training-material/).

For more details regarding the advantages and disavantages of NeTEx, please visit NeTEx website [here](http://netex-cen.eu/?page_id=185)

### What is the recommended process for developing or reviewing the national NeTEx profiles?

A profile is a subset of the standard defined to be used for a specific use case. For the countries that are now under the development of their first NeTEx national profile, we recommend staying as close as possible to the European Passenger Information Profile which includes the minimum information to be shared across countries for passenger information. More EU minimum profiles regarding Accessibility elements and Fares are now under development in the framework of DATA4PT project and will be published soon with the aim to support the countries in enhancing the type of the information that can be exchanged.

#### Key steps to follow

1\.    Use as basis the EU official minimum profiles. More specifically start with the EPI Profile and the relevant documentation. In the DATA4PT website you will find the graphic documentation, the XSD and an XML example regarding EPIP (https://data4pt-project.eu/knowledge-database/ stay). Moreover, we recommend you to watch the dedicated to EPIP webinar available [here](https://data4pt-project.eu/knowledge-database/training-material/).

2\.    Clearly identify the national specific needs to be managed and added to the EPIP profile in order to fulfill country’s requirements.

3\.    Learn from others by analyzing their profiles and checking their examples. Currently, a list of countries with available national profiles is available [here](https://data4pt.org/wiki/NeTEX#National_profiles) . Examine which of the functionalities applied in other countries also fit to your needs and they can be adopted.

4\.    Check the full NeTEx XSD and what elements/objects are included and reply to your needs. In case there is no available element, there is a possibility of providing the information under other elements. It is often possible to add more info to an element by using the keyList/KeyValue construction.

5\.    Create examples and perform a first level validation by using XML validators such as Oxygen, SPY and other commercial tools.

6\.    Ask for feedback from [DATA4PT experts’ team](https://data4pt-project.eu/requests-requirements/).

Also keep in mind that conversion from an existing format is always possible, but if it looks like an easy first step, that may not be the easiest way to collect all the need information (needs or increasing very fast).

### How widely NeTEx is used currently?

Given that many countries already have their own Transmodel based national standards for exchanging timetable data, there wasn’t initially much of a business case for most countries to start using NeTEx in earnest. So, in the first instance what we mainly saw was tools just adding NeTEx timetable export which is relatively simple to do if you are Transmodel based in the first place. 

A real business case is the **example of Norway** where they wanted to rebuild their entire national transport data infrastructure. The standard has been adopted with notable success and speed. The **EU directives for National Access Points (NAPs)** are of course changing this picture by creating a statutory requirement and you can already find initial NeTEx stop and timetable data sets on many countries National Access Points.

But there is still some way to go. A standard needs a whole ecology to be in widespread use so there is inevitably a bootstrapping problem, and for a new subdomain such as fare data. XML also  presents a challenge to some developers.

Examples of countries that currently provide their data in NeTEx format are:

  - [Norway](https://data.transportportal.no/datasets?lang=en)
  - [Luxembourg](https://data.public.lu/en/datasets/)
  - [Sweden](https://www.trafiklab.se/api/trafiklab-apis/netex-regional/)
  - [France](https://transport.data.gouv.fr/?locale=en)
  - [Austria](https://www.mobilitydata.gv.at/en)
  - [Netherlands](http://data.ndovloket.nl/)

Full list of European National Access Points regarding MMTIS Delegated Regulation 1926/2017 (action ‘a’) is available [here](https://ec.europa.eu/transport/sites/default/files/its-national-access-points.pdf). '
