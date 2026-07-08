# How to wash a page

The way we work on this repo is different from typical documentation editing. Instead of hand-editing prose, contributors **brief an AI assistant**, let it draft the improved content, review the draft, then commit.

The reason is consistency. Six people rewriting six pages by hand will produce six voices. Six people briefing an AI with the same conventions and the same trusted sources produce one voice. Final polish is easy from there.

## The core loop

1. **Pick a page** from `STATUS.md` that's `raw` or `conversion-failed` and unclaimed.
2. **Update `STATUS.md`** with your name in the `owner` column and status `in-progress`.
3. **Open the source in `_staging/`** and read it. Get a sense of what's there.
4. **Brief the AI** using the template below. The AI does the writing.
5. **Review the draft.** Push back if anything's wrong.
6. **Commit** the washed page to the appropriate location under `docs/`.
7. **Update `STATUS.md`** to `done`.

Final small polish (typo, one-word fix, link fix) can happen directly in GitHub's web editor after commit.

## The standard prompt template

Copy this, fill in the blanks, paste into your AI tool of choice.

```
I'm washing a page in the Transmodel Ecosystem repo.

# What I want washed

Source file: _staging/<folder>/<file>.md
Target location: docs/<section>/<slug>.md
Disposition: <keep | merge | rewrite | delete>

<Specific things you want changed. Examples:
- Reorganize into three sections: history, current state, future direction.
- Cut the Data4PT present-tense references.
- Include a Nordic-profile example for the stop assignment.
- Remove the wiki signature footer.
- Keep it under 800 words.>

# Context you must use

- Follow the style rules in CLAUDE.md at the repo root.
- Follow the Data4PT naming rules in CLAUDE.md (historical only).
- If you make claims about NeTEx conventions, Nordic profile specifics, or
  entity relationships, check _references/nordic-netex-documentation/ first.
- If you touch cross-standard governance / EU regulations, check the About
  section pages already in docs/about/.

# What I want in return

- The finished markdown, ready to paste into the target file.
- A short bullet list of what you changed vs. the source and why.
- Any concerns or open questions you spotted while writing.
```

Adjust the middle section to your page — the rest stays the same across all wash operations.

## What "good input" looks like

Three things separate a useful prompt from a hand-wavy one:

**1. Be specific about disposition.** "Rewrite" is too vague. "Rewrite as a decision-maker-oriented intro with technical detail below" is better. "Cut to three sections, drop the software-tools table, cross-link to Adopters" is best.

**2. Point at concrete sources.** If a page is about the Nordic profile, tell the AI where to look in `_references/nordic-netex-documentation/`. Don't make it guess.

**3. Say what you want in return.** The AI defaults to giving you everything. Tell it what output shape you want — full markdown ready to paste, a diff of proposed changes, or an outline first for approval.

## Tool-specific setup

### Cowork (Mac) or Claude Code (Mac/Linux/Windows via WSL)

These tools auto-read `CLAUDE.md` and can see `_references/` on disk. Setup:

1. Clone the repo locally.
2. Run `python scripts/sync_sources.py` once to pull `_references/`.
3. Open the tool pointed at your local clone.
4. Paste the prompt template. The AI already knows the conventions and can grep the sources itself.

### Claude.ai in the browser (all platforms — no install)

The AI can't see your local files. You paste what it needs:

1. Open `https://claude.ai`.
2. In your first message, paste **the entire `CLAUDE.md` file** as project briefing.
3. Paste the source page from `_staging/`.
4. If you're touching a Nordic-profile topic, grab the relevant guide from `_references/nordic-netex-documentation/` and paste that too.
5. Then paste the prompt template with your specifics.

Slightly more manual, but works everywhere.

### VS Code with Copilot / Cursor / other AI editors

These read files in the workspace and generally pick up `CLAUDE.md` automatically. Follow the tool's usual conventions.

### ChatGPT or other AI tools

Same pattern as Claude.ai — paste CLAUDE.md, paste source, paste prompt. The prompt template is deliberately model-agnostic, so it works.

## Reviewing the AI's draft

Before committing:

- **Fact-check the specifics.** AI can hallucinate — especially about NeTEx element names, CEN reference numbers, and country-specific details. If in doubt, grep `_references/`.
- **Check the tone.** Warm, direct, plain English. Not marketing-speak.
- **Check the links.** Do internal links point at pages that exist?
- **Check the image paths.** From a page at `docs/standards/netex/faq.md`, images live at `../../assets/images/...`.
- **Sanity-check any lists or tables.** If the AI expanded a list, is every item accurate?

If anything's wrong, push back:

> The Nordic profile section says X, but I want it to say Y because of Z. Rewrite that section only, keep the rest.

Iterate until it's right.

## Final polish in GitHub

Once the file's committed, small tweaks can happen directly in the GitHub web editor:

1. Open the file in GitHub.
2. Click the pencil icon top-right.
3. Edit.
4. Scroll down, write a short commit message, **Commit changes**.

Suitable for: typos, one-word fixes, adding a missing link. Not suitable for: rewrites, restructuring — those go back through the AI loop.

## Why this approach

- **Consistency.** Same briefing across contributors produces similar-sounding output. Merges cleanly, feels coherent to readers.
- **Speed.** Six people drafting for six hours makes 36 hours of content. Six people briefing AI for one hour each makes six hours of content plus review time.
- **Quality control.** Trusted sources in `_references/` are the AI's authoritative context. If it's not in a trusted source, it's not asserted with confidence.
- **Auditability.** The prompt is the change instruction. If we later question a passage, we can look at the prompt that produced it and the source it drew from.

## What not to do

- **Don't skip the trusted sources.** If the AI draft asserts something about NeTEx and you don't know if it's right, don't commit until you've verified against `_references/nordic-netex-documentation/` or the official CEN specs.
- **Don't accept the first draft blindly.** Read it. Push back if it's off.
- **Don't ignore the style rules.** If the AI produces something with emoji headings or marketing-speak, tell it to redo per CLAUDE.md style.
- **Don't hand-rewrite whole paragraphs after the fact.** If a page needs substantial changes after commit, take it back to the AI with a new prompt. Small polish only, in GitHub.
