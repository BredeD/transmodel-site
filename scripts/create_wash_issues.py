#!/usr/bin/env python3
"""Create one GitHub Issue per source page listed in STATUS.md.

Reads STATUS.md, parses the wiki and WordPress tables, and creates one issue
per row. Each issue gets labels for source (wiki / wp) and disposition
(keep / merge / rewrite / guides / delete) so they can be filtered and
grouped in the project board.

Requires:
  - The `gh` CLI installed and authenticated. One-time setup on Mac:
        brew install gh
        gh auth login   (choose HTTPS, browser auth)
  - Run from the repo root.

Usage:
    python scripts/create_wash_issues.py             # create for real
    python scripts/create_wash_issues.py --dry-run   # preview only, no changes

After the script runs, enable "Auto-add to project" in your GitHub Project's
Workflows settings so all created issues automatically appear on the board.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STATUS_PATH = REPO_ROOT / "STATUS.md"
REPO_SLUG_DEFAULT = "BredeD/transmodel-site"

# Label name → (hex colour without #, description)
LABELS: dict[str, tuple[str, str]] = {
    "source: wiki":         ("c5def5", "Content from data4pt.org/wiki (MediaWiki)"),
    "source: wp":           ("c5def5", "Content from transmodel-cen.eu (WordPress)"),
    "disposition: keep":    ("0e8a16", "Move to docs/ with light editing"),
    "disposition: merge":   ("1d76db", "Combine with another page"),
    "disposition: rewrite": ("fbca04", "Substantial cleanup or restructure"),
    "disposition: guides":  ("5319e7", "Belongs in the CEN Guides project"),
    "disposition: delete":  ("b60205", "Remove entirely"),
}


# --- STATUS.md parsing --------------------------------------------------------

_TABLE_ROW = re.compile(
    r"^\|\s*"
    r"`([^`]+)`\s*\|\s*"                # source file (in backticks)
    r"([^|]+?)\s*\|\s*"                 # title
    r"(\d+)\s*\|\s*"                    # word count
    r"([a-z]+)\s*\|\s*"                 # disposition
    r"([^|]+?)\s*\|\s*"                 # target
    r"([^|]*?)\s*\|\s*"                 # notes
    r"([^|]*?)\s*\|\s*"                 # owner
    r"([^|]+?)\s*\|",                   # status
    re.MULTILINE,
)


def parse_status(md_text: str) -> list[dict]:
    """Return a list of entries parsed from STATUS.md table rows."""
    entries: list[dict] = []
    for m in _TABLE_ROW.finditer(md_text):
        source_file = m.group(1).strip()
        status_field = m.group(8).strip().lower()

        # Skip anything already done — no point creating an issue for it.
        if "done" in status_field:
            continue

        entries.append({
            "source_file": source_file,
            "title": m.group(2).strip(),
            "words": int(m.group(3)),
            "disposition": m.group(4).strip().lower(),
            "target": m.group(5).strip(),
            "notes": m.group(6).strip(),
            "owner": m.group(7).strip(),
            "status": status_field,
        })
    return entries


# --- gh CLI helpers -----------------------------------------------------------

def _run_gh(args: list[str]) -> tuple[int, str, str]:
    """Run `gh <args>`, return (returncode, stdout, stderr)."""
    result = subprocess.run(["gh", *args], capture_output=True, text=True)
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def check_gh_auth() -> bool:
    rc, _, err = _run_gh(["auth", "status"])
    if rc != 0:
        print("ERROR: `gh` CLI is not authenticated.", file=sys.stderr)
        print("Fix: run `gh auth login` and choose HTTPS + browser.", file=sys.stderr)
        if err:
            print(err, file=sys.stderr)
        return False
    return True


def ensure_label(name: str, colour: str, desc: str) -> None:
    """Create the label if it doesn't exist. Idempotent."""
    _run_gh([
        "label", "create", name,
        "--color", colour,
        "--description", desc,
        "--force",
    ])


def ensure_all_labels() -> None:
    for name, (colour, desc) in LABELS.items():
        ensure_label(name, colour, desc)


# --- Issue building -----------------------------------------------------------

def slug_from_source(source_file: str) -> str:
    """e.g. 'data4pt-wiki/main-page.md' -> 'wiki/main-page'."""
    p = Path(source_file).with_suffix("")
    parts = list(p.parts)
    # Trim the source prefix if it's the standard folder name
    if parts and parts[0] == "data4pt-wiki":
        parts[0] = "wiki"
    elif parts and parts[0] == "transmodel-cen":
        parts[0] = "wp"
    return "/".join(parts)


def issue_title(entry: dict) -> str:
    return f"wash: {slug_from_source(entry['source_file'])} ({entry['disposition']})"


def issue_body(entry: dict, repo_slug: str) -> str:
    source_url = (
        f"https://github.com/{repo_slug}/blob/main/_staging/{entry['source_file']}"
    )
    notes = entry["notes"] or "—"
    return f"""**Source:** `_staging/{entry['source_file']}` — [open on GitHub]({source_url})

- **Original title:** {entry['title']}
- **Word count:** {entry['words']}
- **Proposed disposition:** `{entry['disposition']}`
- **Proposed target:** `{entry['target']}`
- **Current status:** `{entry['status']}`

**Notes:** {notes}

---

## Workflow

1. Assign this issue to yourself.
2. Create a branch: `wash/{slug_from_source(entry['source_file'])}`.
3. Follow [WASH-GUIDE.md](https://github.com/{repo_slug}/blob/main/WASH-GUIDE.md) — brief the AI, review the draft, commit.
4. Open a PR referencing this issue with `Closes #<issue-number>`.
5. When merged, update `STATUS.md` (mark row as `done`) and close this issue.
"""


def labels_for(entry: dict) -> str:
    source = "source: wiki" if "data4pt-wiki" in entry["source_file"] else "source: wp"
    disposition = f"disposition: {entry['disposition']}"
    return f"{source},{disposition}"


def create_issue(entry: dict, repo_slug: str, dry_run: bool) -> None:
    title = issue_title(entry)
    body = issue_body(entry, repo_slug)
    labels = labels_for(entry)

    if dry_run:
        print(f"  would create: {title}")
        print(f"    labels: {labels}")
        return

    rc, out, err = _run_gh([
        "issue", "create",
        "--title", title,
        "--body", body,
        "--label", labels,
    ])
    if rc != 0:
        print(f"  ERROR ({title}): {err}", file=sys.stderr)
    else:
        print(f"  ✓ {out} — {title}")


# --- main ---------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview what would be created without changing anything.")
    parser.add_argument("--repo", default=REPO_SLUG_DEFAULT,
                        help=f"Repo slug (default: {REPO_SLUG_DEFAULT})")
    args = parser.parse_args()

    if not check_gh_auth():
        return 1

    if not STATUS_PATH.exists():
        print(f"ERROR: {STATUS_PATH} not found", file=sys.stderr)
        return 1

    entries = parse_status(STATUS_PATH.read_text(encoding="utf-8"))
    print(f"Parsed {len(entries)} entries from STATUS.md "
          f"(skipping any marked done).\n")

    if not args.dry_run:
        print("Ensuring labels exist...")
        ensure_all_labels()
        print()

    print(f"{'Previewing' if args.dry_run else 'Creating'} issues:")
    for entry in entries:
        create_issue(entry, args.repo, args.dry_run)

    print()
    print(f"{'Would create' if args.dry_run else 'Created'} {len(entries)} issues.")

    if not args.dry_run:
        print()
        print("Next step:")
        print("  Enable 'Auto-add to project' in your Project's Workflows tab so")
        print("  these issues appear on the board automatically.")
        print(f"  See https://github.com/{args.repo}/issues")

    return 0


if __name__ == "__main__":
    sys.exit(main())
