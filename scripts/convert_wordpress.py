#!/usr/bin/env python3
"""Convert a WordPress WXR export into one markdown file per page.

Usage:
    python convert_wordpress.py <input.xml> <output_dir>

Requires:
    - pandoc on PATH
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List
from xml.etree import ElementTree as ET


NS = {
    "wp": "http://wordpress.org/export/1.2/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "excerpt": "http://wordpress.org/export/1.2/excerpt/",
    "dc": "http://purl.org/dc/elements/1.1/",
}


@dataclass
class Page:
    post_id: int
    parent_id: int
    title: str
    slug: str
    link: str
    date: str
    status: str
    body_html: str
    children: List["Page"] = field(default_factory=list)


def parse_wxr(xml_path: Path) -> Dict[int, Page]:
    tree = ET.parse(str(xml_path))
    root = tree.getroot()
    channel = root.find("channel")
    if channel is None:
        raise RuntimeError("No <channel> element found — is this really a WXR file?")

    pages: Dict[int, Page] = {}
    for item in channel.findall("item"):
        post_type = item.findtext("wp:post_type", "", NS)
        status = item.findtext("wp:status", "", NS)
        if post_type != "page" or status != "publish":
            continue

        try:
            post_id = int(item.findtext("wp:post_id", "0", NS))
            parent_id = int(item.findtext("wp:post_parent", "0", NS))
        except ValueError:
            continue

        pages[post_id] = Page(
            post_id=post_id,
            parent_id=parent_id,
            title=(item.findtext("title", "") or "").strip(),
            slug=(item.findtext("wp:post_name", "", NS) or "").strip(),
            link=(item.findtext("link", "") or "").strip(),
            date=(item.findtext("wp:post_date", "", NS) or "").strip(),
            status=status,
            body_html=(item.findtext("content:encoded", "", NS) or "").strip(),
        )

    for page in pages.values():
        if page.parent_id and page.parent_id in pages:
            pages[page.parent_id].children.append(page)

    return pages


def html_to_markdown(html: str) -> str:
    proc = subprocess.run(
        ["pandoc", "--from=html", "--to=gfm", "--wrap=none"],
        input=html,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"pandoc failed: {proc.stderr}")
    return proc.stdout


def path_for_page(page: Page, pages: Dict[int, Page]) -> Path:
    parts: List[str] = [page.slug or f"page-{page.post_id}"]
    current = page
    while current.parent_id and current.parent_id in pages:
        current = pages[current.parent_id]
        parts.insert(0, current.slug or f"page-{current.post_id}")
    return Path(*parts[:-1]) / f"{parts[-1]}.md"


def convert_pages(xml_path: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    pages = parse_wxr(xml_path)
    written = 0

    for page in pages.values():
        if not page.body_html.strip():
            continue

        rel_path = path_for_page(page, pages)
        out_path = out_dir / rel_path
        out_path.parent.mkdir(parents=True, exist_ok=True)

        md_body = html_to_markdown(page.body_html)
        frontmatter = (
            "---\n"
            f'original_title: "{page.title}"\n'
            f'source: wordpress\n'
            f'source_url: {page.link}\n'
            f'slug: {page.slug}\n'
            f'parent_id: {page.parent_id}\n'
            f'published: {page.date}\n'
            f'status: raw\n'
            "---\n\n"
        )
        out_path.write_text(frontmatter + md_body, encoding="utf-8")
        written += 1

    print(f"Wrote {written} pages to {out_dir}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("xml", type=Path, help="WordPress WXR XML file")
    parser.add_argument("out", type=Path, help="Output directory for markdown files")
    args = parser.parse_args()

    if not args.xml.exists():
        print(f"ERROR: {args.xml} does not exist", file=sys.stderr)
        return 1

    convert_pages(args.xml, args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
