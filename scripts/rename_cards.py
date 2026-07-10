#!/usr/bin/env python3
"""Rename existing issue titles to human-friendly format.

Existing cards were named after their target path (e.g. `standards/netex/index.md`).
That's precise but hard to match to the page title a reader sees in the browser.
This script rewrites each open issue title to `<Human title> — <path>`.

Examples:
    standards/netex/index.md            → NeTEx overview — standards/netex/index.md
    standards/netex/faq.md              → NeTEx FAQ — standards/netex/faq.md
    faq/netex.md                        → NeTEx FAQ (general merge) — faq/netex.md
    implementations/countries/norway.md → Country: Norway — implementations/countries/norway.md
    docs/index.md                       → Home page — docs/index.md

Aggregate cards (which already have human titles like "Clean up: delete legacy pages")
are left untouched.

Prerequisites: gh CLI authenticated.

Usage:
    python scripts/rename_cards.py            # rename all
    python scripts/rename_cards.py --dry-run  # preview only
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys

REPO = "BredeD/transmodel-site"


# Display names for standards
STANDARDS = {
    "netex": "NeTEx",
    "siri": "SIRI",
    "ojp": "OJP",
    "opra": "OpRa",
    "transmodel": "Transmodel",
}


def gh(args: list[str], check: bool = True) -> tuple[int, str, str]:
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"gh failed: {r.stderr.strip()}")
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def looks_like_path(title: str) -> bool:
    """Detect if the title is a bare file path (as our rebuild script emits)."""
    return bool(re.match(r"^[a-z][a-z0-9/_.-]+\.md$", title.strip()))


def human_title(target: str) -> str:
    """Convert a target path into a human-readable title."""
    # Normalise
    t = target.strip()
    if t.startswith("docs/"):
        t = t[len("docs/"):]

    if t == "index.md" or t == "":
        return "Home page"

    parts = t.replace(".md", "").split("/")

    # about/
    if parts[0] == "about":
        if len(parts) == 1 or parts[-1] == "index":
            return "About the ecosystem"
        # about/conformity/harmonisation etc.
        if len(parts) == 3 and parts[1] == "conformity":
            if parts[-1] == "index":
                return "Conformity overview"
            return "Conformity: " + parts[-1].replace("-", " ").capitalize()
        # about/purpose, about/team, about/history, ...
        return parts[-1].replace("-", " ").capitalize()

    # standards/
    if parts[0] == "standards":
        if len(parts) == 2:
            if parts[1] == "index":
                return "Standards overview"
            # standards/tools.md, standards/from-model-to-data.md, standards/netex.md (legacy)
            if parts[1] in STANDARDS:
                return f"{STANDARDS[parts[1]]} overview"
            return "Standards: " + parts[1].replace("-", " ").capitalize()
        if len(parts) == 3:
            std = STANDARDS.get(parts[1], parts[1].capitalize())
            sub = parts[2]
            if sub == "index":
                return f"{std} overview"
            sub_readable = sub.replace("-", " ").capitalize()
            return f"{std}: {sub_readable}"

    # implementations/
    if parts[0] == "implementations":
        if parts[-1] == "index":
            return "Implementations overview"
        if len(parts) == 3 and parts[1] == "countries":
            country = parts[2].replace("-", " ").title()
            return f"Country: {country}"
        return "Implementations: " + parts[-1].replace("-", " ").capitalize()

    # faq/
    if parts[0] == "faq":
        if parts[1] == "index":
            return "FAQ (general)"
        topic = parts[1]
        if topic in STANDARDS:
            return f"{STANDARDS[topic]} FAQ"
        return f"FAQ: {topic.replace('-', ' ').capitalize()}"

    # documentation/
    if parts[0] == "documentation":
        if parts[1] == "index":
            return "Documentation overview"
        return "Documentation: " + parts[1].replace("-", " ").capitalize()

    # conformity/ (in case it's top-level, not under about)
    if parts[0] == "conformity":
        if parts[-1] == "index":
            return "Conformity overview"
        return "Conformity: " + parts[-1].replace("-", " ").capitalize()

    # Top-level singleton files like support.md
    if len(parts) == 1:
        return parts[0].replace("-", " ").capitalize()

    # Fallback
    return target.replace(".md", "").replace("/", " → ")


def new_title(current_title: str) -> str | None:
    """Return the new title, or None if we shouldn't rename this issue."""
    t = current_title.strip()

    # Leave aggregate issues alone
    if t.startswith("Clean up") or t.startswith("Hand-off") or t.startswith("Aggregate"):
        return None

    # Skip anything that already has our em-dash separator
    if " — " in t:
        return None

    if looks_like_path(t):
        return f"{human_title(t)} — {t}"

    # Not sure what this issue is — leave alone
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    args = parser.parse_args()

    rc, out, _ = gh([
        "issue", "list",
        "--repo", REPO,
        "--state", "open",
        "--limit", "500",
        "--json", "number,title",
    ])
    issues = json.loads(out)
    print(f"Found {len(issues)} open issues.\n")

    changed = 0
    skipped = 0
    for issue in issues:
        num = issue["number"]
        current = issue["title"]
        proposed = new_title(current)

        if proposed is None:
            print(f"  skip #{num}: {current}")
            skipped += 1
            continue

        if args.dry_run:
            print(f"  #{num}:  {current}")
            print(f"    →   {proposed}")
        else:
            gh([
                "issue", "edit", str(num),
                "--repo", REPO,
                "--title", proposed,
            ])
            print(f"  ✓ #{num}: {proposed}")
        changed += 1

    print(f"\n{'Would rename' if args.dry_run else 'Renamed'} {changed} issues. Skipped {skipped}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
