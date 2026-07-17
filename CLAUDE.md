# Briefing for AI assistants

This file is for Claude (Cowork, Claude Code) and any other AI assistant a contributor uses. It should be read fully before you help someone edit content in this repo.

## What this project is

**Transmodel Ecosystem** — the new reference site for Transmodel and the standards derived from it (NeTEx, SIRI, OJP, OpRa). A markdown-first replacement for two legacy sites — `transmodel-cen.eu` (WordPress) and `data4pt.org` (MediaWiki) — built collaboratively by 3–7 people across multiple organisations. The output is a static site published from the `docs/` folder via MkDocs Material on GitHub Pages.

There is also a parallel project (`TransmodelEcosystem/NeTEx-Guides-Documentation`) that produces deep technical guides for developers. This website will eventually link out to those guides; do not duplicate their scope here.

## Purpose, audience and scope — keep this in mind when writing

**Purpose:** A single, current, authoritative entry point to the Transmodel Ecosystem. CEN publishes the specifications; vendors write product documentation; national access points publish their own profiles. This site sits between: explaining what the standards are, who runs them, how they fit together, and how to get started with them — without duplicating any of those layers.

**Audience:** Three groups share the same starting point:

- **Newcomers** — someone told them they'll need NeTEx/SIRI/OJP/OpRa and they need to know what that means. Context first, technical detail later.
- **Decision-makers and procurers** — writing tenders, planning national services, advising on standards adoption. Enough to make informed choices, not to build systems.
- **Implementers and vendors** — pointers to schemas, profiles, examples, and the right people. This site sends them into deeper material rather than being that material.

**Not the primary audience:** developers doing deep implementation work. They go to CEN repositories, national profile portals, or the parallel Guides project. Link them there rather than duplicating.

**Scope discipline when writing content:**

- **Narrow in scope.** Don't try to cover everything — link outward to authoritative sources at every level.
- **Neutral across the five standards.** None is elevated above the others in the top-level structure. Transmodel is the conceptual model beneath them; that's a fact, not a hierarchy.
- **Current, not archival.** Legacy content (Data4PT, phase-1 project outputs) is referenced as legacy, not woven into the main narrative.
- **Politically balanced where topics are contested.** Alternative modes vs. GBFS/MDS, NAPCORE's role, the state of national profile alignment — factual framing, no side-taking. See the NeTEx overview's "Alternative modes in practice" callout for the tone we aim for.
- **Honest about what the site doesn't cover.** If a reader needs schema-level detail, tell them where to go. Don't fake depth.

If a piece of content you're helping draft doesn't fit any of the three audiences, pause and ask the contributor whether it belongs on this site at all — or somewhere else in the ecosystem (CEN repos, Guides project, national portal).

## About "Data4PT" — how to use the name

**Data4PT was a CEF-funded European project that ended in June 2025.** It produced significant NeTEx- and SIRI-related artefacts (the reduced XSD, validation tools, the canonical GBFS mapping, national profile inventories, and the DATA4PT wiki that this site replaces).

The **current ongoing work is not Data4PT**. When writing content for this site, do not frame anything as "Data4PT does X" or "the Data4PT community" in the present tense. The correct framing is:

- **Historical / attributional:** "produced by Data4PT" is fine when crediting a specific artefact that came out of the project. For example: *"produced by Data4PT and MobilityData"* is correct.
- **Legacy reference:** referring to the DATA4PT wiki as a legacy site being replaced is fine.
- **NOT current-tense generic references:** don't say "the Data4PT community", "the Data4PT project offers", "Data4PT provides". If a tool or resource is still being maintained after June 2025, it's maintained by whoever picked it up (often NAPCORE or a specific organisation) — cite them, not Data4PT.

If you see a legacy page that still speaks about Data4PT in the present tense, reframe it. Flag it to the contributor as part of the wash pass.

## Authoritative sources — read this before answering questions about NeTEx or Transmodel

`SOURCES.md` at the repo root lists the sources this project treats as authoritative, and the sources it explicitly rejects. **Consult `_references/` first, in preference to your own training data or web results.**

Currently trusted sources (see SOURCES.md for the full context and scope of each):

- `_references/nordic-netex-documentation/` — the official Nordic NeTEx profile documentation. Use for anything specific to the Nordic profile (Norway, Sweden, Finland, Denmark). Folders: `frames/`, `guides/`, `objects/`, `ontology/`.
- `_references/entur-netex-ontology/` — a machine-readable ontology of NeTEx concepts and relationships. Use for reasoning about how entities relate.

**How to actually use these:**

- When a contributor asks about NeTEx conventions, Nordic profile specifics, or entity relationships, grep or read the relevant `_references/` folder before answering.
- If you cite specific behaviour or a schema element, cite the file it came from (e.g. "as documented in `_references/nordic-netex-documentation/frames/ServiceFrame.md`").
- If the trusted sources contradict what you'd otherwise say, trust the sources.
- If a source is out of scope for the question (e.g. Nordic-profile docs when someone asks about the French profile), say so explicitly rather than guessing.

**Rejected sources (do NOT use as evidence):**

See the "Do NOT use" section in SOURCES.md. If a contributor pastes content from a rejected source, flag it and suggest checking against the trusted references.

**If a source you'd naturally reach for is missing:**

Tell the contributor. Suggest they add it to SOURCES.md via PR. Do not silently fall back to training data.

## Folder layout and what you may touch

- `docs/` — **the published website.** Edits here go live. Be careful.
- `_staging/` — raw markdown pulled from the two old sites. Free to edit; the whole point is to clean this up.
- `_source-exports/` — original XML dumps. **Never edit these.** They are the audit trail.
- `_references/` — cloned copies of trusted external sources (see above). **Never edit these** — they mirror upstream repos. If something needs changing there, it goes upstream.
- `scripts/` — Python conversion + sync scripts. Only edit if the user is explicitly working on tooling.
- `STATUS.md` — the original planning artefact. Lists every source page with its intended target and disposition. Do **not** update the `Owner` or `Status` columns — those are duplicated on the project board and live there instead. Notes, disposition changes, and new source rows may still be added here.
- `SOURCES.md` — the trusted/untrusted source registry. Edit only via a PR that the team reviews.
- `README.md`, `CONTRIBUTING.md`, `WASH-GUIDE.md` — occasional edits fine, but ask first.

## The project board is the source of truth for state

Day-to-day tracking (who owns what, current status, blockers) lives on the GitHub project board at `github.com/users/BredeD/projects/4`, not in `STATUS.md`. Each source page is one card there, with:

- Human-friendly title and file path
- Disposition field (keep / merge / rewrite / guides / delete)
- Status column (Backlog / In progress / In review / Done / Needs input)
- Live-URL link at the top of the body (points at the published page)
- Labels for filtering (source, disposition)

When a contributor asks *"what should I work on next?"* or *"who's on this?"* — refer them to the board, not `STATUS.md`.

## The workflow you're supporting

Each contributor picks one card from the project board, moves the corresponding page from `_staging/` into `docs/`, cleans it up, opens a PR. Your job is to help them do that specific unit of work well.

When you're helping with a page:

1. Read the current version in `_staging/`.
2. Check the frontmatter to understand the source (`source_url`).
3. Look at the card's disposition (keep / merge / rewrite / guides / delete). If the contributor is unsure, help them decide by comparing to related pages already in `docs/` and to the trusted sources in `_references/`.
4. Do the actual editing they ask for. Suggest structural improvements only if they're small.
5. Remind them to update image paths (from `_staging/`-relative to `docs/assets/images/…`) and to move the card on the board when the PR is opened (In progress → In review).

## Style rules (enforce these)

- Warm, direct, plain English. No marketing gloss.
- Sentence case for headings.
- Callouts as MkDocs admonitions (`!!! tip`, `!!! note`, `!!! warning`).
- No emojis in section headings on this website (the sister Guides project uses them; we don't).
- No signatures, no revision-date footers, no "Retrieved from…" lines. Those are MediaWiki artefacts.
- Tables: keep them under 6 columns.
- Code blocks: always specify the language.
- Links: relative within the repo, absolute for external.

## Things to actively suggest

- **Duplicate detection.** If you spot content that looks like it also exists in another page in `_staging/` or `docs/`, flag it and suggest a merge target.
- **Guide handoffs.** If you spot content that's deep technical detail about NeTEx or Transmodel (XML structure, frame internals, ID conventions), flag it as a candidate for the sister Guides project rather than keeping it here.
- **Missing images.** If the markdown references an image that doesn't exist under `docs/assets/images/`, tell the contributor.
- **Broken links.** If an internal link points at a file that no longer exists (because it got moved or deleted), flag it.
- **Contradictions with the trusted sources.** If a `_staging/` page says something the Nordic documentation contradicts, flag it — this is often exactly where the wiki got stale.

## When the contributor is ready to push

When the work reaches a natural commit point (a page washed, a feature added, a fix applied), always suggest a commit **subject** and a short **description** the contributor can paste into GitHub Desktop or `git commit`.

Format:

- **Subject line** — one short sentence describing what changed, imperative-ish tone. Keep it under ~72 characters. Example: `Contact page: add standards contacts box, sort by role, responsive grid`
- **Description** — a bullet list of the specific changes, one bullet per change, short. Example:
  ```
  - New "standards" list in _team.yml (5 standard cards at top of contact page)
  - Sort team: leaders first (alpha), then honorary, then rest (alpha)
  - Wrap members in .team-grid — 3 cols wide, 2 cols medium, 1 col mobile
  - Hide table of contents AND left navigation
  ```

Keep it short — no essays. If the change is trivial (typo, one-liner), just the subject is enough.

## Things NOT to do

- Do not touch `_source-exports/` or `_references/`.
- Do not commit directly to `main`. Everything happens on `wash/…`, `merge/…`, or `feat/…` branches, with PRs.
- Do not restyle pages that are already in `docs/` without being asked. Established pages are treated as reviewed content.
- Do not add emojis to headings, decorative section dividers, or "About the author" boxes.
- Do not translate content unless the contributor explicitly asks.
- Do not rewrite whole sections without offering the contributor a chance to review your proposed change first.
- Do not treat any content as authoritative unless it comes from a trusted source in `SOURCES.md`. If in doubt, ask.

## Two-sentence summary

You are helping a small team migrate two legacy sites into one clean markdown-first website. Be careful with `docs/`, generous with `_staging/`, always consult `_references/` before claiming anything about NeTEx, and remember that the project board — not `STATUS.md` — is the source of truth for current state.
