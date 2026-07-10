# Sara kick-off — meeting agenda

**Duration:** ~90 minutes
**Attendees:** Sara (lead going forward), Brede (in tandem)
**Goal:** hand off the working setup so Sara can start driving the content work — Cowork installed, repo cloned, one card claimed by the end of the meeting.

## Prerequisites

Sara needs before the meeting:

- Windows PC with **Pro / Enterprise / Education** edition (not Home — Cowork needs Hyper-V)
- Admin rights to install software
- Existing paid Claude subscription (Pro or higher). Handled at the start if not.

Optional prep — verify Windows edition beforehand by opening PowerShell and running:

```powershell
systeminfo | findstr /B /C:"OS Name"
```

---

## 1. Kick-off & roles (5 min)

- Confirm: Sara leads the content programme. Brede stays in tandem — supporting, tool-building, available for questions.
- More collaborators invited when it feels right — after Sara has run the workflow once herself.
- Quick check-in on availability and preferred cadence.

## 2. Verify Windows edition (2 min)

- Confirm Sara's Windows is Pro / Enterprise / Education.
- If Home: fall back to Claude.ai in browser (as documented in `WASH-GUIDE.md`).

## 3. Install Claude Desktop + Cowork (10 min)

- Sara goes to `claude.com`, downloads Claude Desktop for Windows.
- Install (admin password required).
- Launch, sign in with her Claude account.
- Verify paid subscription is active — upgrade to Pro if not.
- Open the **Cowork** tab inside the app.
- Test: ask Cowork to do something simple (e.g. "list files in my Documents folder").

## 4. GitHub access (concurrent with 5)

- Brede sends collaborator invitation from `github.com/BredeD/transmodel-site/settings/access`.
- Sara accepts via GitHub notifications.
- Verify: Sara can see the repo and open a file in the browser.
- Brede also invites Sara to the project board at `github.com/users/BredeD/projects/4` → Settings → Manage access → Invite collaborators.

## 5. Install GitHub Desktop + clone the repo (10 min)

- Sara downloads GitHub Desktop from `desktop.github.com`.
- Install, sign in with her GitHub account (same one that got the invite).
- **File → Clone repository** → select `BredeD/transmodel-site` from the list.
- Save location: her Documents folder (e.g. `C:\Users\Sara\Documents\transmodel-site`).
- Wait for the clone to finish (~1 minute, ~250 MB with images).

## 6. Point Cowork at the local repo (5 min)

- In Cowork, connect the folder Sara just cloned to (`C:\Users\Sara\Documents\transmodel-site`).
- Verify: Cowork can read `CLAUDE.md` and other files.
- Note: Cowork automatically picks up the project briefing from `CLAUDE.md` — no manual pasting needed.

## 7. Optional: sync trusted reference sources (5 min)

If Python is installed and time allows:

```powershell
cd C:\Users\Sara\Documents\transmodel-site
python scripts\sync_sources.py
```

This pulls Nordic NeTEx documentation and Entur ontology into `_references/` — so Cowork can consult them directly for NeTEx and Nordic-profile-specific questions.

If Python isn't installed, skip and defer. Cowork still works fine without it — just without local reference material for deep NeTEx questions.

## 8. Tour of the live website (10 min)

Open `https://breded.github.io/transmodel-site/` and walk through:

- **Home page** — five standards on equal footing (Transmodel, NeTEx, SIRI, OJP, OpRa), the "conceptual foundation" framing, profiles section with the NAPCORE-led EU-wide profile alignment note.
- **About section** — the ecosystem-level material (Purpose, Governance, Legal context, Team with filter).
- **Standards → Transmodel** — the conceptual-model overview with the Adopters section.
- **Standards → NeTEx** — the fully washed overview, including the Alternative Modes callout (GBFS/TOMP/MDS) and the Nordic profile paragraph. Highlight the politically-sensitive framing.
- **Stubs** — click into SIRI, OJP, OpRa overviews to show the "Placeholder" callouts explaining what will land there.
- **Review corpus** — briefly mention it's the raw pulled content, temporary until the wash is complete.

## 9. Tour of the GitHub repo (10 min)

Open `github.com/BredeD/transmodel-site` and explain the folders:

- **`docs/`** — the published site
- **`_staging/`** — raw content from the two legacy sites (Sara's raw material)
- **`_source-exports/`** — the original XML dumps (never touch)
- **`_references/`** — cloned trusted sources (Nordic profile, ontology)
- **`scripts/`** — one-off tooling

Key files to bookmark:

- **`WASH-GUIDE.md`** — how to wash a page
- **`CLAUDE.md`** — AI briefing (Cowork reads this automatically)
- **`SOURCES.md`** — trusted / rejected sources
- **`STATUS.md`** — original planning table

Branch convention: `wash/<slug>` for content work. PR flow with `Closes #<issue-number>`.

## 10. Tour of the project board (10 min)

Open `github.com/users/BredeD/projects/4` and explain:

- Columns: **Backlog | In progress | In review | Done | Needs input**
- Cards: human title + file path (`Purpose — about/purpose.md`), disposition colour, live-URL link at the top of the body.
- **Disposition field** — filter or group by it (keep / merge / rewrite / guides / delete).
- How Sara claims a card: assign herself → drag into In progress.
- How the flow works: In progress → PR opens → In review → PR merges → Done.
- **Needs input** column — where to park cards blocked on expert review or missing material.
- Aggregate cards for "delete legacy pages" and "guides hand-off" — visible tracking of decisions already made.

## 11. Things to remember (10 min)

Non-negotiables to internalise:

- **AI-first workflow.** Don't hand-write. Brief Cowork with the prompt template from `WASH-GUIDE.md`, review the draft, then commit.
- **`Data4PT` naming rule.** Historical / attributional only — never present-tense. Documented in `CLAUDE.md`.
- **Politically sensitive topics** — the Alternative Modes note, the EU-wide profile alignment, the Nordic profile description. All worded to be factual without picking sides. Preserve that tone in future edits.
- **Trusted sources** — for anything Nordic-profile or NeTEx-relationship-specific, Cowork should consult `_references/nordic-netex-documentation` first. `CLAUDE.md` reminds it to do this.
- **The board is the source of truth for state.** Not `STATUS.md` — Assignees / Status / Disposition on the board are authoritative now.
- **Don't push to `main` directly.** Everything through `wash/<slug>` → PR → review → merge.

## 12. First hands-on with Cowork (10–15 min)

Pick one small card together — for example `Purpose — about/purpose.md` (small, already washed, safe to iterate) or a fresh stub. Walk through:

1. Claim the card on the board (assign Sara, move to In progress).
2. In Cowork, open a new chat pointed at the local repo.
3. Paste the prompt template from `WASH-GUIDE.md`, filled in with target + specifics.
4. Watch what Cowork produces — it reads `CLAUDE.md`, `_staging/`, and `_references/` automatically.
5. Review together — discuss what to change or push back on.

Not aiming to finish a page in the meeting — just so Sara has run the loop once and knows what it feels like with Cowork specifically.

## 13. Open questions to raise together (as time permits)

Any Sara has already picked up from CEN leaders? Any that need decisions to unblock work?

1. Is five standards as equal top-level tabs the right structure? Or should Transmodel get more prominence?
2. News section — currently not planned. Do we want one?
3. Country pages — one page per country, or fold into the profiles matrix?
4. Belgium (90 words) and draft Czech Republic (31 words) — expand, fold, or delete?
5. Certification page is thin — more content, or "coming soon"?
6. Support page — keep as-is or update contact channels?
7. Does Sara agree with the Data4PT historical-only naming rule?
8. When do we invite the next collaborators, and who first?
9. What needs to be in place before transferring the repo to the `TransmodelEcosystem` organisation?

## 14. Next steps & cadence

- Sara picks her first real card and completes it before the next check-in.
- Brede on standby for questions during the week.
- Schedule next check-in — 3–5 days out.
- Agree on what "ready for wider collaborator onboarding" looks like (probably: 3–5 more pages washed + Sara comfortable running the loop solo in Cowork).

---

**One-liner for Sara after the meeting:**
*"Cowork installed, repo cloned locally, one card claimed. See you next week."*
