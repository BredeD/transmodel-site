#!/usr/bin/env python3
"""Mirror the _staging/ folder into docs/review/ for preview, fixing image paths.

Usage:
    python scripts/mirror_staging_to_review.py

Why:
    _staging/ holds raw, unwashed content. MkDocs only serves what's under docs/.
    To preview the raw corpus in the browser (so contributors can browse it before
    washing), we copy the files into docs/review/ and rewrite the image paths
    accordingly. Also generates an index.md per source folder.

Path rewriting:
    _staging/data4pt-wiki/foo.md contains: ![](../../docs/assets/images/wiki/X.png)
    docs/review/wiki/foo.md needs:         ![](../../assets/images/wiki/X.png)

Also prepends a small banner to each mirrored page indicating that it's raw
review content.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STAGING = REPO_ROOT / "_staging"
REVIEW = REPO_ROOT / "docs" / "review"

BANNER = (
    "!!! warning \"Raw, unwashed content\"\n"
    "    This page is in the review corpus — copied directly from the source "
    "site with only automatic conversion applied. It has not yet been edited "
    "for tone, structure, accuracy, or duplication. Do not treat as final.\n\n"
)


def rewrite_paths(text: str) -> str:
    """Rewrite ../../docs/assets/... to ../../assets/... (works from docs/review/*/foo.md)."""
    text = text.replace("../../docs/assets/", "../../assets/")
    return text


def mirror_folder(src_dir: Path, dst_dir: Path, section_title: str) -> int:
    """Copy every .md from src_dir into dst_dir, fixing paths and prepending banner."""
    dst_dir.mkdir(parents=True, exist_ok=True)
    files_written = 0
    entries = []

    for md in sorted(src_dir.rglob("*.md")):
        rel = md.relative_to(src_dir)
        target = dst_dir / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        text = md.read_text(encoding="utf-8")
        # If the file starts with frontmatter, insert the banner AFTER the frontmatter
        if text.startswith("---\n"):
            fm_end = text.find("\n---\n", 4)
            if fm_end != -1:
                fm = text[:fm_end + 5]
                body = text[fm_end + 5:]
                text = fm + "\n" + BANNER + body
            else:
                text = BANNER + text
        else:
            text = BANNER + text
        text = rewrite_paths(text)
        target.write_text(text, encoding="utf-8")
        files_written += 1
        entries.append((str(rel), text.split("\n")[0]))

    # Write an index.md for this section listing all pages
    index_lines = [
        f"# {section_title}\n",
        f"Raw, unwashed content pulled from the source site.  \n",
        f"**{files_written} pages.** Contributors should pick from this list and open a `wash/<slug>` branch to clean up.\n",
        "",
    ]
    for rel, _ in entries:
        # Skip index itself
        if rel == "index.md":
            continue
        name = Path(rel).stem.replace("-", " ").title()
        index_lines.append(f"- [{name}]({rel})")
    (dst_dir / "index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    return files_written


def main() -> int:
    # Clean any previous mirror to avoid stale files
    if REVIEW.exists():
        import shutil
        shutil.rmtree(REVIEW)
    REVIEW.mkdir(parents=True)

    # Write the top-level review index
    (REVIEW / "index.md").write_text(
        "# Review corpus\n\n"
        "This section holds every page pulled from the two legacy sites, "
        "converted to markdown but not yet edited. It exists so contributors "
        "can browse the raw material before deciding what to wash, merge, or delete.\n\n"
        "!!! note\n"
        "    Nothing under `Review corpus` is considered publishable. As pages "
        "are cleaned up they move out of this section into their proper home.\n\n"
        "## Sources\n\n"
        "- [From data4pt.org/wiki](wiki/index.md) — content pulled from the DATA4PT MediaWiki\n"
        "- [From transmodel-cen.eu](transmodel-cen/index.md) — content pulled from the Transmodel WordPress site\n",
        encoding="utf-8",
    )

    n1 = mirror_folder(STAGING / "data4pt-wiki", REVIEW / "wiki", "From data4pt.org/wiki")
    n2 = mirror_folder(STAGING / "transmodel-cen", REVIEW / "transmodel-cen", "From transmodel-cen.eu")

    print(f"Mirrored {n1} wiki pages and {n2} WordPress pages into {REVIEW.relative_to(REPO_ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
