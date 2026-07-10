#!/usr/bin/env python3
"""Add a live-URL link to the top of each issue body.

For each open issue that looks like a page card (title format
"<Human title> — <path>"), computes the live GitHub Pages URL from
the path and prepends it to the issue body. Idempotent — running
twice replaces the existing link rather than duplicating it.

Path → URL rules (MkDocs "directory URLs"):
    docs/index.md              → https://breded.github.io/transmodel-site/
    about/index.md             → https://breded.github.io/transmodel-site/about/
    about/purpose.md           → https://breded.github.io/transmodel-site/about/purpose/
    standards/netex/index.md   → https://breded.github.io/transmodel-site/standards/netex/
    standards/netex/faq.md     → https://breded.github.io/transmodel-site/standards/netex/faq/

Aggregate cards (Clean up, Hand-off) are skipped because they don't
correspond to a single page.

Prerequisites: gh CLI authenticated.

Usage:
    python scripts/add_live_url.py            # apply for real
    python scripts/add_live_url.py --dry-run  # preview only
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


def gh(args, check=True):
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"gh failed: {r.stderr.strip()}")
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def target_from_title(title: str) -> str | None:
    """Titles look like 'Human title — path/to/file.md'."""
    m = re.search(r" — ([a-z][a-z0-9/_.-]+\.md)$", title.strip())
    return m.group(1) if m else None


def target_from_body(body: str) -> str | None:
    """Body has a line like: **Target:** `docs/about/purpose.md`."""
    m = re.search(r"\*\*Target:\*\*\s*`docs/([a-z][a-z0-9/_.-]+\.md)`", body)
    return m.group(1) if m else None


def live_url(target: str) -> str:
    """Convert a target path into an MkDocs-style live URL."""
    t = target.strip()
    if t.startswith("docs/"):
        t = t[len("docs/"):]
    # drop .md
    if t.endswith(".md"):
        t = t[:-3]
    # drop trailing /index (MkDocs serves the directory)
    if t.endswith("/index"):
        t = t[:-len("/index")]
    elif t == "index":
        t = ""
    if not t:
        return BASE_URL
    return BASE_URL + t + "/"


def is_page_card(title: str) -> bool:
    """Aggregate/chore cards are skipped."""
    t = title.strip()
    for skip_prefix in ("Clean up", "Hand-off", "Aggregate"):
        if t.startswith(skip_prefix):
            return False
    return True


def update_body(current_body: str, url: str) -> str:
    """Prepend or replace the live-URL line at the top of the body."""
    link_line = f"{LIVE_URL_MARKER} [{url}]({url})"

    lines = current_body.split("\n") if current_body else []

    # Existing marker anywhere? Replace it.
    for i, line in enumerate(lines):
        if line.startswith(LIVE_URL_MARKER):
            lines[i] = link_line
            return "\n".join(lines)

    # Prepend
    if lines and lines[0].strip():
        return link_line + "\n\n" + current_body
    return link_line + ("\n\n" + current_body if current_body else "")


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

        if not is_page_card(title):
            skipped += 1
            print(f"  skip #{num} (aggregate): {title}")
            continue

        target = target_from_title(title) or target_from_body(body)
        if not target:
            skipped += 1
            print(f"  skip #{num} (no target found): {title}")
            continue

        url = live_url(target)
        new_body = update_body(body, url)

        if args.dry_run:
            print(f"  #{num}: {title}")
            print(f"    → {url}")
        else:
            gh([
                "issue", "edit", str(num),
                "--repo", REPO,
                "--body", new_body,
            ])
            print(f"  ✓ #{num}: {url}")
        updated += 1

    print(f"\n{'Would update' if args.dry_run else 'Updated'} {updated} issues. Skipped {skipped}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
