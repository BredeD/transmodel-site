---
original_title: "NeTEx software"
source: mediawiki
source_url: https://data4pt.org/wiki/NeTEx_software
last_edited: 2021-01-11T13:33:23Z
status: raw
---

The following list of software is known to support NeTEx. We distinguish between different categories that may later receive a list of key performance indicators.

## Conversion of NeTEx between other formats

| Name                                                                  | Availability | Description                                                                                   | Profile             | License  | URL                                                                 |
| --------------------------------------------------------------------- | ------------ | --------------------------------------------------------------------------------------------- | ------------------- | -------- | ------------------------------------------------------------------- |
| [gtfs2netexfr](gtfs2netexfr "wikilink")                               | Available    | Export GTFS data to NeTEx.                                                                    | French              |          | <https://github.com/CanalTP/transit_model/tree/master/gtfs2netexfr> |
| [hastus](hastus "wikilink")                                           | Available    | Giro Hastus OIG script to export NeTEx from a system, in addition can export crew operations. | Dutch, Norwegian(?) | AGPL-3.0 | <https://github.com/skinkie/hastus>                                 |
| [josm-plugin-netex-converter](josm-plugin-netex-converter "wikilink") | Available    | Export OpenStreetMap pedestrian routing information into NeTEx.                               |                     | GPL 2.0  | <https://gitlab.com/labiangashi/josm-plugin-netex-converter/>       |
|                                                                       |              |                                                                                               |                     |          |                                                                     |

## Data Validation tools

| Name                          | Availability | Description                                                           | Profile | License | URL                       |
| ----------------------------- | ------------ | --------------------------------------------------------------------- | ------- | ------- | ------------------------- |
| [XMLlint](XMLlint "wikilink") | Available    | XML syntax validation, XSD schema validation and constraint checking. | All     | MIT     | <http://www.xmlsoft.org/> |
|                               |              |                                                                       |         |         |                           |

## Language bindings and software development aids

| NeTEx XML bindings                                  |
| --------------------------------------------------- |
| Name                                                |
| [netex-java-model](netex-java-model "wikilink")     |
| [netex-csharp-model](netex-csharp-model "wikilink") |
|                                                     |

## Editing /Management & visuallisation tools for NeTEx data

| Name                                    | Availability   | Description                                                                                        | Profile          | License    | URL                                                                                  |
| --------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------- | ---------------- | ---------- | ------------------------------------------------------------------------------------ |
| [Chouette](Chouette "wikilink")         | Available      | Java based NeTEx tools, transforms between profiles and standards (NeTEx, GTFS, Neptune).          | EPIP             | Apache 2.0 | <https://enroute.mobi/produits/chouette/>                                            |
| [mobilitx](mobilitx "wikilink")         | Available      |                                                                                                    |                  |            | <https://mobilitx.diginext.fr/>                                                      |
| [mobiref](mobiref "wikilink")           | Available      |                                                                                                    |                  |            | <https://www.lumiplan.com/produit/mobiref/>                                          |
| [NeTEx Reader](NeTEx_Reader "wikilink") | In Development | C\# based XML tool, based on Giro Hastus XSD.                                                      | Dutch            |            | <https://www.youtube.com/watch?v=mpb_1Y9uR5k>                                        |
| [netexconv2](netexconv2 "wikilink")     | In Development | Java based NeTEx tools, transforms between profiles and standards (NeTEx, DINO, HAFAS, KV1, GTFS). | Dutch, Norwegian |            |                                                                                      |
| [IVU.cloud](IVU.cloud "wikilink")       | Available      |                                                                                                    | EPIP             |            | <https://www.ivu.com/news/news/article/delfi-successfully-migrates-to-ivucloud.html> |
|                                         |                |                                                                                                    |                  |            |                                                                                      |

## NeTEx data enabled

| Name                                          | Availability | Description                                                                                                    | Profile   | License    | URL                                                        |
| --------------------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------- | --------- | ---------- | ---------------------------------------------------------- |
| [OpenTripPlanner](OpenTripPlanner "wikilink") | Available    | Timetable and shortest path journey planner supporting reading various input formats including GTFS and NeTEx. | Norwegian | Apache 2.0 | <http://docs.opentripplanner.org/en/dev-2.x/Netex-Norway/> |
|                                               |              |                                                                                                                |           |            |                                                            |
