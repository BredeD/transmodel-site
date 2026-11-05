# Model Artifacts

Transmodel exists in several machine-readable forms. Each is produced from the same underlying model, but each serves a different purpose — from "I just want to understand the structure" to "I want to reason over the model programmatically". This page lists what's available and when to use each.

## UML diagrams — browsable online

A visual, clickable rendering of the Transmodel v6.2 model as UML class diagrams. Open in a browser; no installation.

**Use this when** you want to understand how Transmodel entities fit together — what a *ServiceJourney* relates to, which attributes a *StopPlace* carries, how *FareProduct* and *TariffZone* interact.

[Browse the full model online →](https://kgpi.fgpa.um.si/napcore-helpdesk/transmodel/index.htm)

Each Transmodel part is documented in its own section of the UML model:

| Part | Domain |
| --- | --- |
| [Part 1](https://kgpi.fgpa.um.si/napcore-helpdesk/transmodel/EARoot/EA2/EA480.htm) | Common Concepts (shared across all other parts) |
| [Part 2](https://kgpi.fgpa.um.si/napcore-helpdesk/transmodel/EARoot/EA3/EA2011.htm) | Public transport network — routes, lines, journey patterns, stops, parking |
| [Part 3](https://kgpi.fgpa.um.si/napcore-helpdesk/transmodel/EARoot/EA4/EA2717.htm) | Timing information and vehicle scheduling |
| [Part 4](https://kgpi.fgpa.um.si/napcore-helpdesk/transmodel/EARoot/EA5/EA3104.htm) | Operations monitoring and control |
| [Part 5](https://kgpi.fgpa.um.si/napcore-helpdesk/transmodel/EARoot/EA6/EA3493.htm) | Fare management |
| [Part 6](https://kgpi.fgpa.um.si/napcore-helpdesk/transmodel/EARoot/EA7/EA5032.htm) | Passenger information (planned and real-time) |
| [Part 7](https://kgpi.fgpa.um.si/napcore-helpdesk/transmodel/EARoot/EA8/EA5568.htm) | Driver management — scheduling, rostering, personnel disposition |
| [Part 8](https://kgpi.fgpa.um.si/napcore-helpdesk/transmodel/EARoot/EA9/EA5759.htm) | Management information and statistics |
| Part 9 | Didactic and informative documentation (not part of the UML model) |
| [Part 10](https://kgpi.fgpa.um.si/napcore-helpdesk/transmodel/EARoot/EA10/EA6038.htm) | Alternative modes — vehicle sharing, pooling, rental, taxi |

## Enterprise Architect source — editable model

The raw model in its native format. Opens in Sparx Enterprise Architect.

**Use this when** you want to edit, extend, inspect at source level, or export the model into another format yourself.

**Prerequisite:** Sparx Enterprise Architect v16.

- [Transmodel v6.2 Enterprise Architect project (QEA)](https://transmodel-cen.eu/model6.2/TransmodelEcoSystem2024-EAv16-nk84_OpRa-v13.qea)

## XML export

A machine-readable serialisation of the UML model as XML. Lossless export of entities, attributes and relationships.

**Use this when** you want to import the model into another modelling tool, script against its structure, generate documentation automatically, or build derived artifacts (like the ontology below).

**Prerequisite:** any XML parser.

- [Transmodel v6.2 XML export](https://transmodel-cen.eu/model6.2/Transmodel_v6.2_XML_2026.xml)

## Ontology (RDF/OWL)

A semantic-web representation of Transmodel — entities as OWL classes, relationships as object properties. **Generated from the XML export above**, so it stays aligned with the UML model as it evolves.

**Use this when** you want to:

- Run SPARQL queries over the model ("which entities relate to Quay?")
- Reason automatically about transitive relationships and class hierarchies
- Map Transmodel concepts to other ontologies (geospatial, mobility, accessibility)
- Build knowledge graphs that integrate public transport data with other domains

**Prerequisite:** an RDF/OWL toolchain — Protégé, Apache Jena, RDF4J, or similar.

- [Transmodel ontology — generator and output](https://entur.github.io/transmodel-ontology-generator/) — the working tool that produces the ontology from the Transmodel XML export, together with the resulting ontology files.

## Which one should I use?

Short decision guide:

| I want to… | Use |
| --- | --- |
| Understand how the model is structured | **UML diagrams** |
| Edit the model, or inspect it at source level | **Enterprise Architect QEA** |
| Automate against the model's structure (scripts, derived documentation, format generators) | **XML export** |
| Query, reason over, or map the model semantically | **Ontology (RDF/OWL)** |

## Related artifacts on other standards

For the XSD schemas that *implement* Transmodel for data exchange — the actual formats carried between systems — see the individual standard pages:

- [NeTEx → Resources](../netex/resources.md)
- [SIRI → Resources](../siri/resources.md)
- [OJP → Resources](../ojp/resources.md)
- [OpRa → Resources](../opra/resources.md)
