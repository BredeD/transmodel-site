#!/usr/bin/env python3
"""Sync the trusted sources listed in SOURCES.md into _references/.

Usage:
    python scripts/sync_sources.py [--dry-run]

What it does:
    1. Parses SOURCES.md and extracts every "Trusted source" entry with a URL.
    2. For each source:
       - If _references/<repo-name>/ doesn't exist yet: git clone it.
       - If it does exist: git pull --ff-only.
    3. Honours an optional `pinned_commit:` line per source to check out a specific SHA.
    4. Prints a summary at the end.

Sources listed under "Do NOT use" are ignored (they're on the list precisely so
we don't pull them in).

Kept dead simple on purpose. Requires only Python 3.9+ and git on PATH.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional


REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES_MD = REPO_ROOT / "SOURCES.md"
REFS_DIR = REPO_ROOT / "_references"


@dataclass
class Source:
    name: str          # e.g. "entur/nordic-netex-documentation"
    url: str
    pinned_commit: Optional[str] = None

    @property
    def local_dir(self) -> Path:
        # We use only the repo name (the part after the last slash) to avoid
        # nested owner folders like _references/entur/foo/. Flatter is easier.
        repo_name = self.url.rstrip("/").split("/")[-1]
        repo_name = repo_name.removesuffix(".git")
        return REFS_DIR / repo_name


def parse_sources(md_path: Path) -> List[Source]:
    """Read SOURCES.md and extract sources under the '## Trusted sources' heading."""
    if not md_path.exists():
        raise FileNotFoundError(f"{md_path} not found")

    text = md_path.read_text(encoding="utf-8")

    # Grab just the "Trusted sources" section (between "## Trusted sources" and
    # the next "## " heading).
    match = re.search(
        r"## Trusted sources\n(.+?)(?=\n## |\Z)",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise RuntimeError("No '## Trusted sources' section found in SOURCES.md")

    section = match.group(1)

    sources: List[Source] = []

    # Each entry is a "### name" block. We split on "### " to iterate over them.
    for block in re.split(r"\n### ", "\n" + section):
        block = block.strip()
        if not block:
            continue

        # First line is the name
        name = block.splitlines()[0].strip()
        if not name or name.startswith("<!--"):
            continue

        # Find URL: line — accept "**URL:**" or "- **URL:**" markdown
        url_match = re.search(r"\*\*URL:\*\*\s*<?(https?://\S+?)>?\s*$", block, re.MULTILINE)
        if not url_match:
            continue
        url = url_match.group(1).rstrip(".,)")

        # Optional pinned commit
        pin_match = re.search(r"pinned_commit:\s*([0-9a-f]{7,40})", block, re.IGNORECASE)
        pinned = pin_match.group(1) if pin_match else None

        sources.append(Source(name=name, url=url, pinned_commit=pinned))

    return sources


def run(cmd: List[str], cwd: Optional[Path] = None, dry_run: bool = False) -> int:
    print(f"  $ {' '.join(cmd)}" + (f"  (in {cwd})" if cwd else ""))
    if dry_run:
        return 0
    result = subprocess.run(cmd, cwd=str(cwd) if cwd else None)
    return result.returncode


def sync_one(source: Source, dry_run: bool) -> bool:
    """Clone or pull one source. Returns True on success."""
    print(f"\n→ {source.name}")
    print(f"  url: {source.url}")

    target = source.local_dir
    if target.exists():
        # existing clone: fetch + update
        if run(["git", "fetch", "--all", "--prune"], cwd=target, dry_run=dry_run) != 0:
            return False
        if source.pinned_commit:
            if run(["git", "checkout", source.pinned_commit], cwd=target, dry_run=dry_run) != 0:
                return False
        else:
            # try to fast-forward the current branch
            if run(["git", "pull", "--ff-only"], cwd=target, dry_run=dry_run) != 0:
                print(f"  ⚠️  Could not fast-forward {target.name} — local changes?")
                return False
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        if run(["git", "clone", source.url, str(target)], dry_run=dry_run) != 0:
            return False
        if source.pinned_commit:
            if run(["git", "checkout", source.pinned_commit], cwd=target, dry_run=dry_run) != 0:
                return False

    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--dry-run", action="store_true", help="Print git commands but don't run them")
    args = parser.parse_args()

    try:
        sources = parse_sources(SOURCES_MD)
    except (FileNotFoundError, RuntimeError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    if not sources:
        print("No trusted sources found in SOURCES.md.")
        return 0

    print(f"Found {len(sources)} trusted source(s) in SOURCES.md")
    print(f"Target directory: {REFS_DIR}")

    ok, failed = 0, 0
    for src in sources:
        if sync_one(src, dry_run=args.dry_run):
            ok += 1
        else:
            failed += 1

    print(f"\n{'=' * 40}")
    print(f"Synced: {ok}")
    if failed:
        print(f"Failed: {failed}")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
