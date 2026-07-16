#!/usr/bin/env python3
"""One-off migration script for the About → Introduction restructure.

Updates existing open issues (board cards) so that:
- Titles referencing `about/*` are updated to reference `introduction/*` (or `contact/team.md`).
- Human title in the card is regenerated (e.g. "About the ecosystem" → "Overview").
- Live-URL in the body is regenerated to point at the new deployed path.

Only issues that currently match the old path pattern are touched — safe to
run once. Aggregate cards (Clean up, Hand-off) are skipped.

Prerequisites: gh CLI authenticated, run from repo root.

Usage:
    python scripts/migrate_cards_restructure.py --dry-run
    python scripts/migrate_cards_restructure.py
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys

REPO = "BredeD/transmodel-site"
BASE_URL = "https://breded.github.io/transmodel-site/"
LIVE_URL_MARKER = "**Live page:**"


# old path → (new path, new human title)
MAPPING = {
    "about/index.md":                        ("introduction/index.md",                        "Overview"),
    "about/purpose.md":                      ("introduction/purpose.md",                      "Purpose"),
    "about/governance.md":                   ("introduction/governance.md",                   "Governance"),
    "about/legal-context.md":                ("introduction/legal-context.md",                "Legal context"),
    "about/history.md":                      ("introduction/history.md",                      "History"),
    "about/transmodel-at-a-glance.md":       ("introduction/transmodel-at-a-glance.md",       "Transmodel at a glance"),
    "about/napcore.md":                      ("introduction/napcore.md",                      "NAPCORE"),
    "about/conformity/index.md":             ("introduction/conformity/index.md",             "Conformity overview"),
    "about/conformity/harmonisation.md":     ("introduction/conformity/harmonisation.md",     "Conformity: Harmonisation"),
    "about/conformity/comparison.md":        ("introduction/conformity/comparison.md",        "Conformity: Comparison"),
    "about/conformity/certification.md":     ("introduction/conformity/certification.md",     "Conformity: Certification"),
    # Team moves to a different top-level folder
    "about/team.md":                         ("contact/team.md",                              "Team"),
}


def gh(args, check=True):
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"gh failed: {r.stderr.strip()}")
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def live_url(target: str) -> str:
    """Compute the deployed URL from a docs-relative path."""
    t = target.strip()
    if t.startswith("docs/"):
        t = t[len("docs/"):]
    if t.endswith(".md"):
        t = t[:-3]
    if t.endswith("/index"):
        t = t[:-len("/index")]
    elif t == "index":
        t = ""
    if not t:
        return BASE_URL
    return BASE_URL + t + "/"


def replace_live_url_in_body(body: str, new_url: str) -> str:
    """Update or insert the live-URL line."""
    link_line = f"{LIVE_URL_MARKER} [{new_url}]({new_url})"
    lines = body.split("\n") if body else []
    for i, line in enumerate(lines):
        if line.startswith(LIVE_URL_MARKER):
            lines[i] = link_line
            return "\n".join(lines)
    if lines and lines[0].strip():
        return link_line + "\n\n" + body
    return link_line + ("\n\n" + body if body else "")


def new_title(current_title: str) -> tuple[str, str] | None:
    """If the title references an old path, return (new_title, new_path). Else None."""
    for old_path, (new_path, new_human) in MAPPING.items():
        # Match with word boundary — look for " — old_path" at the end
        pattern = re.compile(r" — " + re.escape(old_path) + r"$")
        if pattern.search(current_title):
            return f"{new_human} — {new_path}", new_path
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    args = parser.parse_args()

    rc, out, _ = gh([
        "issue", "list",
        "--repo", REPO,
        "--state", "open",
        "--limit", "500",
        "--json", "number,title,body",
    ])
    issues = json.loads(out)
    print(f"Scanning {len(issues)} open issues.\n")

    updated = 0
    skipped = 0

    for issue in issues:
        num = issue["number"]
        title = issue["title"]
        body = issue.get("body") or ""

        result = new_title(title)
        if not result:
            skipped += 1
            continue

        new_t, new_path = result
        new_body = replace_live_url_in_body(body, live_url(new_path))

        if args.dry_run:
            print(f"  #{num}:")
            print(f"    was: {title}")
            print(f"    now: {new_t}")
            print(f"    URL: {live_url(new_path)}")
        else:
            gh([
                "issue", "edit", str(num),
                "--repo", REPO,
                "--title", new_t,
                "--body", new_body,
            ])
            print(f"  ✓ #{num}: {new_t}")
        updated += 1

    print(f"\n{'Would update' if args.dry_run else 'Updated'} {updated} issues. Skipped {skipped}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
