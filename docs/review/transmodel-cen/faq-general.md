---
original_title: "FAQ General"
source: wordpress
source_url: https://transmodel-cen.eu/index.php/faq-general/
slug: faq-general
parent_id: 0
published: 2024-02-23 15:02:19
status: raw
---

!!! warning "Raw, unwashed content"
    This page is in the review corpus — copied directly from the source site with only automatic conversion applied. It has not yet been edited for tone, structure, accuracy, or duplication. Do not treat as final.


# General FAQ

<span>Why so many standards?​</span>

We can find explanations for why there are many and divers PT standards in both the functional scope involved, some specific technology needs, and of course history.

**Functional scope  
**

Public transport encompasses many functions and many stakeholders; from the very small to very large; and operating in quite different modes, so naturally its data requirements span many different categories of data and many different use cases. **Superficial discussion on the subject often tends to focus on a few specific categories of data that people are familiar **with from their own use of using public transport, such as timetables, or real time departures, **but they are of course only part of the wider picture**. There are many other aspects to running a transport system, from **managing the network infrastructure to planning and scheduling**, through to the **collecting of fares**, each needing the exchange of data. **Informing the public with passenger information requires just a few categories out of many others.**

**Technology needs  
**

An important point to note is that the different functions have an evolving temporal dimension – with different process taking place, before, during and after travel and this means that **different technologies are needed to handle the real-time and dynamic aspects of a system as opposed to the static aspects.**

**Each different category of information thus has its own inherent submodel** (for example for, stops, timetables, tariff structures, control, etc), and in most legacy formats has had different formats. Furthermore, the protocols that are efficient for the occasional bulk exchange of static or slow changing reference data are quite different from the protocols best suited for dynamic APIs, so we need two separate families of standards for gathering and for delivering data.

**History**

History is also instructive. If you look at what has been happening over the past 20 years, we see that in the late 1990’s we started out with numerous separate national formats as well as quite a few proprietary formats, mostly mode specific (predominately rail), not all very well documented and not all open or easy to extend. Over time, thanks to **Transmodel, a gradual alignment of terminology and concepts **allowed a common conceptual model to emerge in the early 2000’s, which in turn allowed a** new generation of European national timetable standards to be developed** that adopted the common terminology and took advantage of the reusable concepts that had been developed to simplify their representations.

By the end of the decade, the various national timetable formats were close enough to consider creating a common XML format, to cover the network and timetables. This was done creating NeTEx, though there wasn’t actually a pressing business case for anyone to move to it and most countries concentrated on the uptake of their own still quite new national standards. On the API front , an early win was the development of the SIRI real-time API which was based on the German VDV 453 , harmonised to use the Transmodel terminology. This replaced a number of different national standards and is by now in widespread use in many European countries. APIs are of course easier and quicker to implement than bulk exchange formats since they are views over existing data sets and data feeds and SIRI was . New data sets requiring a much bigger investment in database and tools to create data.

No country has a standard format for exchanging multimodal fare data, yet alone one that can describe the sophisticated new types of electronic fare product made possible by smartcards and mobile devices. The Transmodel fare model was implemented as a further module of NeTEx to cover this gap. Although it is a distinct module   of NeTEx and has a large submodel of its own , it reuses existing NeTEx components for example stops, zones and lines and operators , where ever possible

So even if there are still a confusingly number of PT standards out there, there are a great deal fewer than there would be if we hadn’t already made progress in standardisation.

<span>What is the difference between the different standards/formats?​</span>

Standardisations can take many flavours. You may have standardised designs, standards for protocols at different levels in the technology stack, standard formats for exchanging data, or even meta standards, that is standards for writing standards or for using a particular technology. Thus, **different standards may apply at different levels of abstraction.**

An important case in point is Transmodel itself: Transmodel isn’t a concrete format. It operates at a more abstract level, providing a common set of concepts and data structures with which to describe public transport entities and their relationships. As such it has a **critical role as a unifying framework from which to develop concrete standards**. But it means that when we consider a given format we are actually dealing with two standards at the same time. The good news is that Transmodel spans the entire domain – there is only one conceptual standard\!

**Concrete exchange formats and protocols necessarily have a smaller scope**. And can be placed within the “bigger picture” A standard with relatively broad scope, such as NeTEx, actually needs to be carefully modularised so that it can be used selectively.

Considering the wider context of what we are really aiming at, that of **gathering information from many sources to build useful applications,** we see that **we need exchange formats not just for the “downstream” processes that deliver information to the passenger**. But also, for the** “upstream” processes that create and manage the data in the first place**.

Although there are many common components, these** upstream processes contain additional concepts that don’t need to be in the downstream data sets**. For example, when you are creating schedules, you need to know the times over the links of a network in order to work out the timings that will ultimately be shown to the passenger in the finalised timetable. Downstream formats may use simplified views.  However, with the massive growth in mobile devices and smart mobility apps, **the long-term trend is to want more sophisticated function in the downstream systems too.** It is therefor **attractive to have a richer format than can be used selectively in multiple different use cases.**

For more technical information about the different standards of transmodel check the FAQ pages of the [DATA4PT wiki](https://data4pt.org/w/index.php?title=FAQ_NeTEX).
