# Sources — trusted and untrusted reference material

This is the canonical list of external repositories and documents that AI assistants (Cowork, Claude Code, etc.) and human contributors should consult when working on content in this project. Editing this file is how we keep everyone — human and AI — aligned on what counts as authoritative.

**How AI assistants use this:**
`CLAUDE.md` at the repo root tells any AI assistant to prefer material from the trusted sources below over its own training data or web results, and to actively reject material that matches the "Do not use" list.

**How humans use this:**
When you're washing a page and need to check a fact (a NeTEx element name, a Nordic profile convention, an ontology term), grep the `_references/` folder locally instead of trusting an internet search. It's up to date with the sources here.

---

## Trusted sources

Sources on this list are treated as authoritative by AI assistants working in this repo.

### entur/nordic-netex-documentation

- **URL:** https://github.com/entur/nordic-netex-documentation
- **What it is:** The official documentation for the Nordic NeTEx profile — the common NeTEx profile agreed between Norway, Sweden, Finland, and Denmark.
- **Why we trust it:** Maintained by Entur (Norway's national NeTEx implementation team) with input from the Nordic partner countries. This is the reference for anything Nordic-profile-specific.
- **Local path after sync:** `_references/nordic-netex-documentation/`
- **Scope:** Nordic profile only. Do not treat as authoritative for other national profiles (French, Italian, Croatian, etc.).

### entur/entur-netex-ontology

- **URL:** https://github.com/entur/entur-netex-ontology
- **What it is:** A machine-readable ontology of NeTEx concepts and their relationships, produced by Entur.
- **Why we trust it:** Produced by the same team as the Nordic profile documentation; useful for reasoning about how NeTEx entities relate to each other.
- **Local path after sync:** `_references/entur-netex-ontology/`
- **Scope:** Terminology and relationships. Not a substitute for the NeTEx standard itself when it comes to XSD conformance.

<!-- Add new trusted sources below this line. Include URL, what it is, why we trust it, local path, scope. -->

---

## Do NOT use

Sources on this list contain outdated, incorrect, or misleading NeTEx/Transmodel content. AI assistants must actively reject material from these sources even if it appears in search results or in the AI's training data.

*This list is empty for now. It will grow as we identify sources to avoid.*

Candidates to review with the team when colleagues return from holiday:

- Old NeTEx tutorials from before EN12896 v6.2 (concept renames)
- Draft profiles that never made it to publication
- Any content that predates the 2020 clarifications on stop assignments

<!-- Add anti-sources below this line. Include URL/identifier and one-sentence reason. -->

---

## How to update this list

1. Open a PR editing this file.
2. For a new trusted source, include: URL, one-paragraph description, why the team trusts it, scope caveats.
3. For a "do not use" entry, include: URL or identifier, and one sentence on what's wrong with it.
4. Tag at least one reviewer (ideally a NeTEx subject expert).
5. When merged, contributors run `python scripts/sync_sources.py` to pull the new source (or remove a rejected one).

## Sync behaviour

Sources are cloned (not vendored) into `_references/` which is gitignored. This means:

- The `_references/` folder is not committed. Each contributor pulls their own local copy.
- Sources stay reasonably fresh — running the sync script does a `git pull` on each existing clone.
- If we ever need to pin a specific version of a source (e.g. because a change breaks our references), we add a `pinned_commit:` line under the source entry and the sync script honours it.

## Open questions to resolve when the team is back from holiday

- Which additional Nordic-focused repos should be on the trusted list? (candidates below)
- Which other national profiles (French, Italian) do we want as trusted sources for cross-profile comparison?
- Is there an official CEN document repository or Enterprise Architect model we should include?
- Which historical/legacy content sources are known to be misleading and belong on the "Do not use" list?

**Candidates to evaluate:**

- `NeTEx-CEN/NeTEx` (the official CEN NeTEx repo with XSDs and examples)
- `SIRI-CEN/SIRI` (the official SIRI repo)
- `TransmodelEcosystem/NeTEx-Guides-Documentation` (the CEN Guides work in progress — trusted once it stabilises)
- French profile: `normes.transport.data.gouv.fr` (mentioned in the wiki content)
- Italian profile: `5Tsrl/netex-italian-profile`
- OJP: relevant repos when known

These are placeholders — do not treat as trusted until the team confirms.
