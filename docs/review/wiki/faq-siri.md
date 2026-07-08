---
original_title: "FAQ SIRI"
source: mediawiki
source_url: https://data4pt.org/wiki/FAQ_SIRI
last_edited: 2023-11-03T14:36:58Z
status: raw
---

!!! warning "Raw, unwashed content"
    This page is in the review corpus — copied directly from the source site with only automatic conversion applied. It has not yet been edited for tone, structure, accuracy, or duplication. Do not treat as final.


## How to best model the logic "AND" of GTFS- RT in SIRI SX (Situation Exchange)?

SIRI technical standard offers to also have publications of diversified information (with the possibility of having variants depending on the communication channels and also their location), in addition to allowing the management of multiple consequences. For example when referring to a line, we do not inform the same way upstream and downstream of the disturbance.

In the following example of GTFS'RT message,

"informed\_entity": \[ { "route\_id": "13", "stop\_id": "quay11" }, { "route\_id": "13", "stop\_id": "quay12" } \], where for route 13 and 2 platforms 11 and 12 are impacted,

the "informed\_entity" of GTFS-RT a priori concerns PublishingActions in SIRI which via PublishAtScope-\>Affects-\>StopPoints makes it possible to point as well the stops concerned (with the possibility of specifying the Quay number, see StopPointType).

The PublishingActions are described in SIRI Situation Exchange (Part 5 - CEN/TS 15531-5:2022) and is also included in the EU profile.

## Is it possible to use JSON/REST interface instead of XML for NeTEx and SIRI data exchange?

In general, JSON should be in addition to XML, so it means you need anyway XML. JSON is working in different way than XML. If the data to exchange is huge, this fact can break JSON. For large files is better to use XML that parses only the part you want to access, line per line and within a time window.  

Regarding SIRI, IDFM (Ile de France Mobilité -Authority from Paris Area) provides a REST/JSON access point by simply converting the original XML to JSON. Others are also doing REST but still using the XML data (REST does not imply JSON, and a lot of REST services are XML based).

It is also recommended to check SIRI Part 2 for further insights, as well as the following report <http://www.normes-donnees-tc.org/wp-content/uploads/2017/01/Proposition-Profil-SIRI-Lite-initial-v1-2.pdf>. (available in French).
