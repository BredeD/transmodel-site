---
original_title: "Conformity"
source: wordpress
source_url: https://transmodel-cen.eu/index.php/conformity/
slug: conformity
parent_id: 0
published: 2024-03-01 15:48:52
status: raw
---

!!! warning "Raw, unwashed content"
    This page is in the review corpus — copied directly from the source site with only automatic conversion applied. It has not yet been edited for tone, structure, accuracy, or duplication. Do not treat as final.


# Conformity with Transmodel as reference

![](../../assets/images/transmodel-cen/JP6R27HS8P-1.jpg)

A specification which cites Transmodel needs to include comparisons of the specification against the Transmodel reference data model in at least two conformance levels:

  - level 1 (the global level) identifies which **data domains** within the specification are drawn from the Transmodel data domains, and which are not;
  - level 2 (the detailed level) compares the **data model** within the specification against the Transmodel entities.

**The level 1 **conformance statement should be presented as a table based on:

  - the list of Transmodel data/functional domains: This covers the description of the network, timing information and vehicle scheduling, operations monitoring and control, passenger information, fare collection, personnel management, management information, alternative modes, completed by list of the concerned data model packages ([see the data model structure](https://mockuptm.itforpt.be/model/)); or
  - the list of sub-packages and/or UML diagrams concerned, as presented in the standard documentation of Transmodel (or [here](https://mockuptm.itforpt.be/model/))

**The level 2** conformance statement consists in a detailed comparison of data elements of a source specification to Transmodel (target specification) and shall be presented as a mapping table (see*** [Mapping Methodology](../../assets/files/Methodology-for-comparing-data-standards.pdf)***) in which the data elements used in the source specification are qualified  as:

  - Exact correspondence of a source concept to a Transmodel class
  - Exact correspondence of a source attribute to a Transmodel attribute
  - Source-specific concept without contradiction to any of the Transmodel elements
  - Source-specific attribute without contradiction to any of the Transmodel elements

The following table shows the different qualification of correspondence, that can be marked with "X".

\[table id=7 /\]

This qualification allows to evaluate the degree of compliance of the source specification to Transmodel (target).

**IMPORTANT**: The [Mapping Methodology](../../assets/files/Methodology-for-comparing-data-standards.pdf) concerns conceptual data model. Compare what is comparable\!\!\!

For concrete formats of any real size, the creation of a full mapping of every attribute and relationship between two standards is very time consuming.

For many purposes it will suffice only to map the entities (“simple” level 2 entity mapping), to ensure the equivalence of their semantics by examining their definitions and primary attributes.

To be noted as well: the conformity evaluation as described above is a first step to a certification process.

Certification requires more than that: the existence of an approved certification body, the description of certification process, etc. Find out more about it on [CERTIFICATION](https://mockuptm.itforpt.be/index.php/certification/).
