# How to use the standards

This section is a high-level guide only. It answers the question *"where do I start, and what do I need?"* without going into detail on any single standard.

## You don't have to buy anything

CEN Technical Specifications for NeTEx, SIRI, OJP and OpRa are formally published documents that can be purchased from national standardization bodies. **You do not need to.** The specifications are also available as open-source repositories on GitHub, and the practical material for implementation — schemas, examples, national profiles — is freely accessible.

Buy the formal specifications if you need them for reference in a tender document, regulatory filing, or academic citation. For everyday implementation work, you'll spend more time in the GitHub repositories and profile documentation than in the formal PDF.

## Which standard to use

Which standard applies to a given problem is described in the [standards summaries on the home page](../index.md) and in [How the standards are linked](how-standards-are-linked.md). In short:

- If you're publishing scheduled data — **NeTEx**.
- If you're publishing real-time data — **SIRI**.
- If you're offering a journey planning API — **OJP**.
- If you're sharing observed operational data — **OpRa**.

**Transmodel** sits beneath all four. It's the conceptual data model where the shared vocabulary, definitions, and relationships between concepts are defined. You don't choose Transmodel as an alternative to the exchange standards — it's the model they all implement, and whenever you work with one of them, you're working with Transmodel underneath.

If the problem doesn't obviously match one standard, it's usually because the problem spans several phases (planning + real-time, for instance). In that case you use several standards together — that's the whole point of a shared conceptual model.

## Where the technical detail lives

Details about each standard are in the standard's own section, not here. Follow the top-level tabs:

- [Transmodel](../standards/transmodel/index.md) — Overview + Adopters + FAQ + Resources
- [NeTEx](../standards/netex/index.md) — Overview + Implementations + FAQ + Resources
- [SIRI](../standards/siri/index.md) — Overview + Implementations + FAQ + Resources
- [OJP](../standards/ojp/index.md) — Overview + Implementations + FAQ + Resources
- [OpRa](../standards/opra/index.md) — Overview + Implementations + FAQ + Resources

Each standard's Implementations page lists the national profiles and where their authoritative documentation lives.

## When you need help

- Check the standard's **FAQ page** first — many common questions live there.
- For Nordic-specific NeTEx questions, the [Nordic profile documentation](https://github.com/entur/nordic-netex-documentation) is authoritative.
- For French-specific questions, the [French national portal](https://normes.transport.data.gouv.fr/) is authoritative.
- Deeper implementation guidance lives in the parallel [NeTEx Guides project](https://github.com/TransmodelEcosystem/NeTEx-Guides-Documentation).
- For questions that don't have a home yet, see [Contact](../contact/team.md).
