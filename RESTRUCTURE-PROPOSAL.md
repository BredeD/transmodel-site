# Site restructure — proposal

**Author:** Brede (with Claude in tandem)
**Status:** For discussion with Sara, then wider extended group
**Goal:** simplify the site's front door and clarify what belongs where.

## What this site is for

Before we discuss structure, a clear statement of purpose, audience, and problem-space:

### Purpose

A single, current, authoritative entry point to the **Transmodel Ecosystem** — the family of European public transport data standards (Transmodel, NeTEx, SIRI, OJP, OpRa).

CEN publishes the specifications; vendors write product documentation; national access points publish their own profiles. This site sits between: **explaining what the standards are, who runs them, how they fit together, and how to get started with them — without duplicating any of those layers.**

It replaces two legacy sites (`transmodel-cen.eu` and `data4pt.org/wiki`) that had drifted, were maintained in silos, and had lost the ability to clearly signal what is current vs. historical.

### Who it's for

Three audiences share the same starting point here:

- **People new to the ecosystem.** Someone told them "you'll need NeTEx" (or SIRI, or OJP), and they need to know what that means. Public officials, product managers, journalists, junior engineers. They need context first, technical detail later.
- **Decision-makers and procurers.** Writing tenders, planning national services, advising on standards adoption. They need to know which standard covers which need, what the legal context is, and how the pieces fit together — enough to make informed choices, not enough to build systems.
- **Implementers and vendors.** Need pointers to schemas, profiles, examples, and the people to talk to. This site sends them into deeper material rather than trying to be that material.

Notably **not** the primary audience: developers doing deep implementation work. They go to the CEN NeTEx/SIRI repositories, the national profile portals, or the parallel [NeTEx Guides project](https://github.com/TransmodelEcosystem/NeTEx-Guides-Documentation). This site links them there, doesn't try to compete.

### The problem it addresses

Information about the Transmodel Ecosystem is scattered across at least four kinds of sources:

- CEN repositories — authoritative but formal, hard to navigate for a newcomer
- National access points and profile portals — each in its own language, with local conventions
- Legacy project sites — outdated, mixed with historical content, unclear what still applies
- Vendor and community documentation — useful but unavoidably biased toward one product or one implementation

A newcomer can't tell which source is current, which is authoritative, which applies to their situation. There is no "start here" — and there hasn't been for a long time.

This site is that "start here". Narrow in scope, honest about what it doesn't cover, neutral across the five standards, current, and politically balanced where topics are contested.

## The problem with the current setup

The Home page is trying to do too many jobs at once:

- Welcome
- Describe what Transmodel and its family of standards is
- Link to the five standards
- Explain how they fit together
- Introduce national profiles
- Address different audiences (implementers vs. decision-makers)
- Provide help pointers

That's eight distinct sections on one page. Readers landing there have to work harder than they should to figure out what this site is, and where they should go next.

Meanwhile, the **About** section overlaps in scope and doesn't have a clear identity.

## Proposed structure

Clear separation of responsibilities across the top-level navigation:

```
Home | Introduction | Transmodel | NeTEx | SIRI | OJP | OpRa | Contact | Review corpus (temporary)
```

### Home — the launchpad

A short, focused entry point. Two things only:

1. One or two sentences explaining what the Transmodel ecosystem is.
2. Five cards linking to the five standards, each with a one-line description.
3. A single, prominent "New here? Start with the Introduction →" call to action.

Everything else moves out. Kept minimal so that first-time visitors immediately see the family of standards without being overwhelmed.

The **"Under construction"** banner stays here until the extended group has reviewed the site and agreed on the shape.

### Introduction — the educational section

Where anyone new to Transmodel goes to understand the ecosystem. High-level, aimed at newcomers and non-specialists.

Structure:

- **Overview** — what this section covers, who it's for
- **How the standards are linked** — the phases of a public-transport service (planning → NeTEx, running → SIRI, journey planning → OJP, learning → OpRa) and how the standards cover different use cases
- **How to use the standards** — a high-level guide only:
  - You find the technical artefacts on each standard's own section (NeTEx, SIRI, OJP, OpRa)
  - You can buy the standard from national standardization bodies if you want — but you don't need to
  - Which standard to use is described in the standards summaries here and on the home page
  - Details about each standard are in the standard's own section
- **How standardization works** — CEN, TC 278, WG3, how a European Standard is developed (moved and expanded from today's Governance page)
- **How to contribute** — how to raise change requests, get involved in CEN sub-groups, coordinate through NAPCORE and similar programmes
- **NAPCORE** — short note about the National Access Point Coordination Organisation for Europe and its remit (already added as a small standalone page before Legal context)
- **Purpose** (existing)
- **Legal context** (existing)
- **History** (existing, stub for now)

### Standards — deep material lives here

The five top-level standard tabs (Transmodel, NeTEx, SIRI, OJP, OpRa) each have their own section with:

- **Overview** — what the standard is
- **Adopters or Implementations** — who uses it
- **FAQ** — questions and answers
- **Resources** — presentations, guides, videos, papers, XSD locations, etc.

Everything specific to a standard lives here. The Introduction should never duplicate this — it can only summarise and point.

### Contact — top-level tab

The **Team** page moves out of About/Introduction and becomes its own top-level tab called **Contact**. It's not conceptual material — it's practical (who to reach out to). Deserves its own place.

Will hold:

- Team members (with the standards filter we've built)
- General contact channels
- How to reach the working groups

### Review corpus — temporary

Unchanged from today. Removed when the wash is complete.

## Content moves

| Currently in… | Moves to… |
| --- | --- |
| Home → "How they fit together" | Introduction → "How the standards are linked" |
| Home → "Profiles" | Introduction → possibly under "How to use the standards", or its own sub-page |
| Home → "Who this site is for" | Introduction → likely absorbed into the Overview |
| Home → "Get help" | Distributed — FAQ links per standard, Contact for general help |
| About → Overview | Introduction → Overview |
| About → Governance | Introduction → "How standardization works" |
| About → NAPCORE (new) | Introduction → NAPCORE (short standalone paragraph) |
| About → Team | Contact (new top-level tab) |
| About → Purpose, Legal context, History | Introduction (unchanged, just renamed section) |
| About → Conformity | Introduction → own sub-section (as today) |

## What stays the same

- Five standards as equal top-level tabs
- Each standard's own Overview / Implementations (or Adopters for Transmodel) / FAQ / Resources
- Board and workflow (nothing changes there)
- Trusted sources setup
- WASH-GUIDE workflow

## Consequences

**Positive:**

- Home becomes immediately understandable. First-time visitor sees five standards and one call to action.
- Introduction becomes a real destination — a coherent story someone new to Transmodel can read start-to-finish.
- Contact tab makes it clear who to reach out to.
- Cleaner mental model for contributors: educational content in Introduction, specifics per standard.

**Costs:**

- URL change: `docs/about/*` → `docs/introduction/*`. Around ten internal links must be rewritten in already-washed pages. Board cards that reference these paths need updating.
- Two new stub pages to be washed in Introduction: "How to use the standards" and "How to contribute".
- One new top-level tab (Contact) instead of Team under About.
- The extended group needs time to review before we lock this in.

## Suggested execution plan

Two steps.

**Step 1 — This week:**

- Move existing content:
  - `docs/about/` → `docs/introduction/`
  - Rename all references and update navigation.
  - Move Team to `docs/contact/team.md` and create the Contact tab.
- Rewrite `docs/index.md` to the minimal launchpad version, keeping the under-construction banner.
- Create stubs for the two new Introduction pages ("How the standards are linked", "How to use the standards", "How to contribute").
- Update board cards to point to the new paths.

**Step 2 — Next 1–2 weeks:**

- Wash "How the standards are linked" (mostly lifted from current Home content).
- Wash "How to use the standards" (new, based on Brede's high-level framing).
- Wash "How to contribute" (new, based on CEN and NAPCORE processes).
- Move remaining content between sections as needed after review.

## Open questions for the extended group

- Is the five-standards-equal structure right, or should Transmodel be given more prominence than the others?
- Is Contact the right label for the team+reach-out tab? Alternatives: **People**, **Community**, **Team & Contact**.
- Should the Under-construction banner be visible from day one to visitors outside our group, or hidden until the site is ready to launch?
- Timing: when do we lock in the structure and start onboarding wider contributors?

## Decision needed

Sara and the extended group's endorsement of:

1. The Home / Introduction split as described.
2. The Contact tab (with Team moving out of Introduction).
3. The two-step execution plan.

Once endorsed, Brede and Claude execute Step 1 in a single working session.
