# STATUS — the master content backlog

Every page pulled from the two source sites, with a proposed disposition. This is the working document that drives the wash — pick a row that's `raw` and unclaimed, put your name in `owner`, open a `wash/<slug>` branch, do the work, then update the row.

**Disposition legend:**

- `keep` — move to `docs/` with light editing; content is mostly good.
- `merge` — combine with another page (see notes); update this row to point at the surviving page.
- `rewrite` — substantial cleanup or restructure needed.
- `guides` — deep technical content that belongs in the CEN Guides project; leave in `_staging/`, we may keep a thin summary + link on this site.
- `delete` — nothing worth saving on the new site.

**Status legend:**

- `raw` — as pulled from source, no work done.
- `conversion-failed` — pandoc couldn't parse a wikitable; raw wikitext preserved inside a fenced block for manual conversion.
- `in-progress` — someone has claimed this and is working on it.
- `done` — merged to `main`; page is in `docs/` (or deleted).

**Overall picture:** 66 pages total (25 wiki + 41 WP). Rough distribution of proposed dispositions: ~35 keep, ~10 merge, ~5 rewrite, ~10 guides, ~6 delete.

---

## Wiki pages (from data4pt.org)

| Source file | Original title | Words | Disposition | Target | Notes | Owner | Status |
| --- | --- | ---:| --- | --- | --- | --- | --- |
| `data4pt-wiki/main-page.md` | Main Page | 178 | delete | — | Replaced by our own `docs/index.md`. | | raw |
| `data4pt-wiki/transmodel.md` | Transmodel | 187 | delete | — | One paragraph stub. Content already exists on WP site (`about.md`, `transmodel-at-a-glance.md`). | | raw |
| `data4pt-wiki/netex.md` | NeTEX | 1811 | rewrite | `standards/netex.md` | **conversion-failed** — wikitable didn't parse. Also duplicates WP `netex.md`. Merge best bits; use WP page as base. | Brede | **done (POC 2, merged into standards/netex.md)** |
| `data4pt-wiki/siri.md` | SIRI | 876 | rewrite | `standards/siri.md` | **conversion-failed** — same table issue. Merge with WP `siri.md`. | | conversion-failed |
| `data4pt-wiki/netex-software.md` | NeTEx software | 450 | merge | `standards/tools.md` | Merge with `siri-software.md` into one "Software & tools" page. | | raw |
| `data4pt-wiki/siri-software.md` | SIRI software | 327 | merge | `standards/tools.md` | See above. | | raw |
| `data4pt-wiki/explore-nap-guidelines.md` | Explore NAP guidelines | 6082 | keep | `implementations/nap-guidelines.md` | Substantial. Wiki has the definitive NAP guidance. | | raw |
| `data4pt-wiki/national-implementations.md` | National Implementations | 4373 | keep | `implementations/national-profiles.md` | The huge profile-per-country matrix. Landing table for country pages below. | | raw |
| `data4pt-wiki/australia.md` | Australia | 352 | keep | `implementations/countries/australia.md` | | | raw |
| `data4pt-wiki/austria.md` | Austria | 674 | keep | `implementations/countries/austria.md` | | | raw |
| `data4pt-wiki/belgium.md` | Belgium | 90 | rewrite | `implementations/countries/belgium.md` | Very thin — either expand or fold into national-profiles table. | | raw |
| `data4pt-wiki/croatia.md` | Croatia | 991 | keep | `implementations/countries/croatia.md` | | | raw |
| `data4pt-wiki/denmark.md` | Denmark | 622 | keep | `implementations/countries/denmark.md` | | | raw |
| `data4pt-wiki/france.md` | France | 633 | keep | `implementations/countries/france.md` | | | raw |
| `data4pt-wiki/italy.md` | Italy | 1143 | keep | `implementations/countries/italy.md` | | | raw |
| `data4pt-wiki/portugal.md` | Portugal | 451 | keep | `implementations/countries/portugal.md` | | | raw |
| `data4pt-wiki/slovenia.md` | Slovenia | 782 | keep | `implementations/countries/slovenia.md` | | | raw |
| `data4pt-wiki/sweden.md` | Sweden | 747 | keep | `implementations/countries/sweden.md` | | | raw |
| `data4pt-wiki/switzerland.md` | Switzerland | 481 | keep | `implementations/countries/switzerland.md` | | | raw |
| `data4pt-wiki/draftczech-republic.md` | Draft Czech Republic | 31 | delete | — | 31-word stub. Ask Sara if we want a Czech placeholder or just wait for real content. | | raw |
| `data4pt-wiki/faq.md` | FAQ | 1997 | merge | `faq/index.md` | Merge with WP `faq-general.md`; substantial overlap. | | raw |
| `data4pt-wiki/faq-transmodel.md` | FAQ Transmodel | 1235 | merge | `faq/transmodel.md` | Merge with WP `faq-transmodel.md`. Take unique questions from each. | | raw |
| `data4pt-wiki/faq-netex.md` | FAQ NeTEX | 4579 | merge | `faq/netex.md` | Merge with WP `faq-netex.md`. Big and useful — wiki version has more Q&A. | | raw |
| `data4pt-wiki/faq-siri.md` | FAQ SIRI | 321 | keep | `faq/siri.md` | No corresponding WP page. Standalone. | | raw |
| `data4pt-wiki/support-request.md` | Support Request | 171 | keep | `support.md` | How to request help. Small, keep on the site. | | raw |

## WordPress pages (from transmodel-cen.eu)

| Source file | Original title | Words | Disposition | Target | Notes | Owner | Status |
| --- | --- | ---:| --- | --- | --- | --- | --- |
| `transmodel-cen/homepage.md` | Homepage | 406 | delete | — | Replaced by our own `docs/index.md`. Steal any good tagline. | | raw |
| `transmodel-cen/elementor-12.md` | Contact | 50 | delete | — | Elementor template placeholder. If contact info matters, capture separately. | | raw |
| `transmodel-cen/events.md` | Events | 38 | delete | — | Empty. | | raw |
| `transmodel-cen/news-article.md` | News | 21 | delete | — | Empty. Decide with Sara whether we want a news section at all. | | raw |
| `transmodel-cen/about.md` | About (What is Transmodel?) | 630 | keep | `about/index.md` | The core "About" page. | Brede | **done (POC 1)** |
| `transmodel-cen/purpose.md` | Purpose | 255 | keep | `about/purpose.md` | Could fold into `about/index.md`; ask Sara. | Brede | **done** |
| `transmodel-cen/transmodel-at-a-glance.md` | Transmodel at a glance | 2601 | keep | `about/transmodel-at-a-glance.md` | Substantial overview. Good for decision-makers. | | raw |
| `transmodel-cen/governance.md` | Governance | 727 | keep | `about/governance.md` | | Brede | **done** |
| `transmodel-cen/legal-context.md` | Legal context | 427 | keep | `about/legal-context.md` | | Brede | **done** |
| `transmodel-cen/history.md` | History | 2771 | keep | `about/history.md` | Rich history material. | | raw |
| `transmodel-cen/team.md` | Team | 205 | keep | `about/team.md` | Two portrait images were missing from the export — regenerate. | Brede | **done** |
| `transmodel-cen/standards-for-implementation.md` | Standards for implementation | 733 | keep | `standards/index.md` | Overview landing for standards. | | raw |
| `transmodel-cen/from-transmodel-to-data-file.md` | From Transmodel to data file | 743 | keep | `standards/from-model-to-data.md` | | | raw |
| `transmodel-cen/existing-implementation.md` | Existing implementation | 523 | keep | `standards/existing-implementations.md` | | | raw |
| `transmodel-cen/netex.md` | NeTEx | 882 | keep | `standards/netex.md` | Merges with wiki `netex.md` (see above). Use this as base since it converted cleanly. | Brede | **done (POC 2)** |
| `transmodel-cen/siri.md` | SIRI | 1153 | keep | `standards/siri.md` | Merges with wiki `siri.md`. | | raw |
| `transmodel-cen/ojp.md` | OJP | 460 | keep | `standards/ojp.md` | No wiki equivalent. | | raw |
| `transmodel-cen/opra.md` | OPRA | 564 | keep | `standards/opra.md` | No wiki equivalent. | | raw |
| `transmodel-cen/conformity.md` | Conformity | 403 | keep | `conformity/index.md` | Landing page. | | raw |
| `transmodel-cen/standards-harmonisation.md` | Standards harmonisation | 265 | keep | `conformity/harmonisation.md` | | | raw |
| `transmodel-cen/standards-comparison.md` | Standards comparison | 568 | keep | `conformity/comparison.md` | | | raw |
| `transmodel-cen/certification.md` | Certification | 150 | rewrite | `conformity/certification.md` | Thin — likely needs expansion or a "coming soon" note. Check with CEN. | | raw |
| `transmodel-cen/documentation-center.md` | Documentation center | 138 | merge | `documentation/index.md` | Merge with `tutorials.md`, `presentations.md` etc. into one landing. | | raw |
| `transmodel-cen/tutorials.md` | Tutorials | 142 | merge | `documentation/index.md` | Same as above. Just a landing with links. | | raw |
| `transmodel-cen/presentations.md` | Presentations | 134 | keep | `documentation/presentations.md` | Links to PDFs; PDFs are in `docs/assets/files/`. | | raw |
| `transmodel-cen/videos-webinars.md` | Videos & Webinars | 131 | keep | `documentation/videos.md` | | | raw |
| `transmodel-cen/uml-documents.md` | UML documents | 253 | keep | `documentation/uml.md` | | | raw |
| `transmodel-cen/papers.md` | Papers | 324 | keep | `documentation/papers.md` | | | raw |
| `transmodel-cen/common-concepts.md` | Common concepts tutorial | 4030 | guides | — | Deep technical tutorial. Belongs in CEN Guides. Keep in `_staging/` as raw material for Guides authors. | | raw |
| `transmodel-cen/network-description-tutorial.md` | Network description tutorial | 1074 | guides | — | Same. | | raw |
| `transmodel-cen/timing-information-tutorial.md` | Timing information tutorial | 1168 | guides | — | Same. | | raw |
| `transmodel-cen/vehicle-scheduling-tutorial.md` | Vehicle scheduling tutorial | 423 | guides | — | Same. | | raw |
| `transmodel-cen/oper.md` | Operations monitoring and control | 3043 | guides | — | Same. | | raw |
| `transmodel-cen/fare-managementen-tutorial.md` | Fare management tutorial | 4720 | guides | — | Same — the fares tutorial. Big. | | raw |
| `transmodel-cen/passenger-information-tutorial.md` | Passenger information tutorial | 3194 | guides | — | Same. | | raw |
| `transmodel-cen/driver-management-tutorial.md` | Driver management tutorial | 1855 | guides | — | Same. | | raw |
| `transmodel-cen/management-information-and-statistics-tutorial.md` | Management information & statistics | 2027 | guides | — | Same. | | raw |
| `transmodel-cen/faq-general.md` | FAQ General | 1074 | merge | `faq/index.md` | Merge with wiki `faq.md`. | | raw |
| `transmodel-cen/faq-transmodel.md` | FAQ Transmodel | 905 | merge | `faq/transmodel.md` | Merge with wiki `faq-transmodel.md`. | | raw |
| `transmodel-cen/faq-netex.md` | FAQ NeTEx | 1209 | merge | `faq/netex.md` | Merge with wiki `faq-netex.md`. | | raw |
| `transmodel-cen/faq-model-structure.md` | FAQ Model structure | 448 | keep | `faq/model-structure.md` | No wiki equivalent. | | raw |

---

## Roll-up

**By disposition:**

| Disposition | Count | Notes |
| --- | ---:| --- |
| keep | 36 | Straight moves with light editing |
| merge | 11 | Pairs to combine (mostly FAQ + software) |
| rewrite | 4 | belgium (too thin), certification (too thin), wiki netex + siri (conversion-failed + duplication) |
| guides | 9 | All the WP tutorials — hand off to CEN Guides project |
| delete | 6 | Landing pages we replace, empty stubs, empty news |

**By target section (for kept/merged pages that land in `docs/`):**

| Section | Pages | Effort |
| --- | ---:| --- |
| `about/` | 7 | Light |
| `standards/` | 8 (incl. tools) | Medium — merge NeTEx and SIRI across sources |
| `conformity/` | 4 | Light |
| `implementations/` | 13 (11 countries + 2 overview) | Medium — the big matrix on national-profiles |
| `faq/` | 5 (with merges) | Medium — dedupe and organise Q&As |
| `documentation/` | 5 | Light |
| `support.md`, `index.md` | 2 | Light |

## Suggested first pages to wash (proof-of-concept round)

Good candidates to do first — small enough to finish in one sitting, representative enough to test the workflow:

1. **`about/index.md`** — from `transmodel-cen/about.md`. Establishes the tone and the section landing pattern.
2. **`standards/netex.md`** — the meaty merge case (wiki + WP), tests the merge workflow.
3. **`faq/netex.md`** — the biggest merge candidate, tests dedupe + Q&A restructuring.
4. **`implementations/countries/denmark.md`** — representative country page.

If those four go well, we've validated the workflow and can parallelise the rest.

## Open questions for Sara / the team

1. Should we keep separate country pages, or fold country content into the `national-profiles.md` matrix?
2. Do we want a **News** section at all? WP had one but the content is empty.
3. Do the WP tutorials (`common-concepts`, `network-description`, etc.) get a **thin summary** on this site with a link to the Guides, or do they disappear from here entirely once the Guides exist?
4. For **Belgium** (only 90 words) and **Draft Czech Republic** (31 words): expand, fold into the matrix, or delete?
5. **Team page** — two portraits (Andrej, Sara) were missing from the export. Should we regenerate, or drop the page?
6. **Certification** page is thin — do we have more content, or add a "coming soon" placeholder?
7. Do we keep the **Support Request** page as-is, or update the contact channels?
