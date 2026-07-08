#!/usr/bin/env python3
"""Convert a MediaWiki Special:Export XML dump into one markdown file per page.

Usage:
    python convert_mediawiki.py <input.xml> <output_dir>

Example:
    python convert_mediawiki.py _source-exports/data4pt-wiki-export.xml _staging/data4pt-wiki/

Requires:
    - pandoc on PATH (install with: brew install pandoc)
    - No Python packages (uses only the standard library)
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from xml.etree import ElementTree as ET


def _strip_ns(tag: str) -> str:
    return tag.split("}", 1)[-1] if "}" in tag else tag


def slugify(title: str) -> str:
    s = title.strip().lower()
    s = s.replace(" ", "-")
    s = re.sub(r"[^a-z0-9\-_]", "", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "untitled"


def is_content_page(title: str) -> bool:
    skip_prefixes = (
        "Talk:", "User:", "User talk:", "File:", "File talk:",
        "MediaWiki:", "Template:", "Help:", "Category:",
        "Special:", "Media:", "DATA4PT WIKI:",
    )
    return not any(title.startswith(p) for p in skip_prefixes)


def wikitext_to_markdown(wikitext: str) -> tuple[str, str | None]:
    """Return (markdown, error). If error is not None, markdown falls back to raw wikitext in a code block."""
    proc = subprocess.run(
        ["pandoc", "--from=mediawiki", "--to=gfm", "--wrap=none"],
        input=wikitext,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        # Fallback: emit raw wikitext in a fenced block, plus a warning banner
        fallback = (
            "> **⚠️ Pandoc could not convert this page cleanly.**  \n"
            f"> Error: `{proc.stderr.strip().splitlines()[0] if proc.stderr.strip() else 'unknown'}`  \n"
            "> Raw wikitext preserved below for manual cleanup.\n\n"
            "```mediawiki\n"
            f"{wikitext}\n"
            "```\n"
        )
        return fallback, proc.stderr.strip()
    return proc.stdout, None


def convert_dump(xml_path: Path, out_dir: Path, wiki_base_url: str) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    kept, skipped_redirect, skipped_ns, failed = 0, 0, 0, 0
    failures: list[tuple[str, str]] = []

    for _, elem in ET.iterparse(str(xml_path), events=("end",)):
        if _strip_ns(elem.tag) != "page":
            continue

        title = None
        wikitext = ""
        timestamp = None
        is_redirect = False

        for child in elem:
            tag = _strip_ns(child.tag)
            if tag == "title":
                title = (child.text or "").strip()
            elif tag == "redirect":
                is_redirect = True
            elif tag == "revision":
                for rev_child in child:
                    rtag = _strip_ns(rev_child.tag)
                    if rtag == "text":
                        wikitext = rev_child.text or ""
                    elif rtag == "timestamp":
                        timestamp = (rev_child.text or "").strip()

        elem.clear()

        if not title:
            continue
        if is_redirect:
            skipped_redirect += 1
            continue
        if not is_content_page(title):
            skipped_ns += 1
            continue
        if not wikitext.strip():
            continue

        md_body, err = wikitext_to_markdown(wikitext)
        conversion_status = "raw"
        if err:
            failed += 1
            failures.append((title, err.splitlines()[0] if err else "unknown"))
            conversion_status = "conversion-failed"

        frontmatter = (
            "---\n"
            f'original_title: "{title}"\n'
            f'source: mediawiki\n'
            f'source_url: {wiki_base_url}/{title.replace(" ", "_")}\n'
            f'last_edited: {timestamp or ""}\n'
            f'status: {conversion_status}\n'
            "---\n\n"
        )

        out_path = out_dir / f"{slugify(title)}.md"
        out_path.write_text(frontmatter + md_body, encoding="utf-8")
        kept += 1

    print(f"Wrote {kept} pages to {out_dir}")
    print(f"Skipped: {skipped_redirect} redirects, {skipped_ns} non-content pages")
    if failures:
        print(f"\n{failed} pages had conversion issues (raw wikitext preserved):")
        for title, err in failures:
            print(f"  - {title}: {err}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("xml", type=Path, help="MediaWiki Special:Export XML file")
    parser.add_argument("out", type=Path, help="Output directory for markdown files")
    parser.add_argument(
        "--wiki-base-url",
        default="https://data4pt.org/wiki",
        help="Base URL used to reconstruct source URLs in frontmatter",
    )
    args = parser.parse_args()

    if not args.xml.exists():
        print(f"ERROR: {args.xml} does not exist", file=sys.stderr)
        return 1

    convert_dump(args.xml, args.out, args.wiki_base_url)
    return 0


if __name__ == "__main__":
    sys.exit(main())
