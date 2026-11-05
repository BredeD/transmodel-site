# Model Artifacts

Transmodel exists in several machine-readable forms. Each is produced from the same underlying model, but each serves a different purpose — from *"I just want to understand the structure"* to *"I want to reason over the model programmatically"*.

<div class="grid cards" markdown>

-   :material-sitemap: **UML diagrams**

    ---

    **Use it when** you want to understand how the model is structured — classes, attributes, relationships.

    No tools needed; opens in a browser.

    [Browse the model →](https://kgpi.fgpa.um.si/napcore-helpdesk/transmodel/index.htm)

-   :material-file-document-edit: **Enterprise Architect source**

    ---

    **Use it when** you want to edit the model, or inspect it at source level.

    Needs Sparx Enterprise Architect v16.

    [Download QEA →](https://transmodel-cen.eu/model6.2/TransmodelEcoSystem2024-EAv16-nk84_OpRa-v13.qea)

-   :material-code-tags: **XML export**

    ---

    **Use it when** you want to automate against the model — scripts, format generators, derived documentation, or building other artifacts (like the ontology).

    Any XML parser.

    [Download XML →](https://transmodel-cen.eu/model6.2/Transmodel_v6.2_XML_2026.xml)

-   :material-graph: **Ontology (RDF/OWL)**

    ---

    **Use it when** you want to query or reason over the model semantically — SPARQL, knowledge graphs, mappings to other ontologies.

    Generated from the XML export above, so it stays aligned with the UML. Needs an RDF/OWL toolchain (Protégé, Apache Jena, RDF4J).

    [Open the ontology project →](https://entur.github.io/transmodel-ontology-generator/)

</div>

## UML model — part by part

Each Transmodel part has its own section of the browsable UML model:

- [Part 1 — Common Concepts](https://kgpi.fgpa.um.si/napcore-helpdesk/transmodel/EARoot/EA2/EA480.htm) — shared across all other parts
- [Part 2 — Public transport network](https://kgpi.fgpa.um.si/napcore-helpdesk/transmodel/EARoot/EA3/EA2011.htm) — routes, lines, journey patterns, stops, parking
- [Part 3 — Timing information and vehicle scheduling](https://kgpi.fgpa.um.si/napcore-helpdesk/transmodel/EARoot/EA4/EA2717.htm)
- [Part 4 — Operations monitoring and control](https://kgpi.fgpa.um.si/napcore-helpdesk/transmodel/EARoot/EA5/EA3104.htm)
- [Part 5 — Fare management](https://kgpi.fgpa.um.si/napcore-helpdesk/transmodel/EARoot/EA6/EA3493.htm)
- [Part 6 — Passenger information](https://kgpi.fgpa.um.si/napcore-helpdesk/transmodel/EARoot/EA7/EA5032.htm) — planned and real-time
- [Part 7 — Driver management](https://kgpi.fgpa.um.si/napcore-helpdesk/transmodel/EARoot/EA8/EA5568.htm) — scheduling, rostering, personnel disposition
- [Part 8 — Management information and statistics](https://kgpi.fgpa.um.si/napcore-helpdesk/transmodel/EARoot/EA9/EA5759.htm)
- Part 9 — Didactic and informative documentation (not part of the UML model)
- [Part 10 — Alternative modes](https://kgpi.fgpa.um.si/napcore-helpdesk/transmodel/EARoot/EA10/EA6038.htm) — vehicle sharing, pooling, rental, taxi

## Related artifacts on other standards

For the XSD schemas that *implement* Transmodel for data exchange — the actual formats carried between systems — see the individual standard pages:

- [NeTEx → Resources](../netex/resources.md)
- [SIRI → Resources](../siri/resources.md)
- [OJP → Resources](../ojp/resources.md)
- [OpRa → Resources](../opra/resources.md)
