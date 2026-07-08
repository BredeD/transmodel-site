#!/usr/bin/env python3
"""Extract images from the source zips and rewrite image references in the staging markdown.

Usage:
    python scripts/extract_images.py

Assumes it's run from the repo root.

What it does:
    1. Scans _staging/**/*.md for image references (both bare filenames from wiki,
       and full URLs from WordPress).
    2. Extracts only the needed image files from:
       - _source-exports/data4pt-images.zip (small — extracts all originals + flattens)
       - _source-exports/transmodel-cen-uploads.zip (large — extracts only matched files)
    3. Puts them under docs/assets/images/wiki/ and docs/assets/images/transmodel-cen/.
    4. Rewrites the markdown to point at the new local paths (relative to _staging/).

Design notes:
    - Wiki zip has a hash-based directory layout (e.g. 0/00/SERVICE_PATTERN_1.png).
      We flatten it: docs/assets/images/wiki/<filename>. If there are filename
      collisions we log them but keep the first occurrence.
    - WP zip has a mix of flat files and year/month folders. Files are matched by
      basename since the WordPress URLs sometimes reference sized variants
      (e.g. -768x631.png). We extract every matching filename found in the zip
      (including all size variants) so links don't break.
    - After running, PDFs referenced in markdown are extracted too (they go into
      docs/assets/files/).
"""

from __future__ import annotations

import re
import shutil
import sys
import zipfile
from pathlib import Path
from typing import Dict, List, Set, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
STAGING = REPO_ROOT / "_staging"
WIKI_ZIP = REPO_ROOT / "_source-exports" / "data4pt-images.zip"
WP_ZIP = REPO_ROOT / "_source-exports" / "transmodel-cen-uploads.zip"
IMG_WIKI = REPO_ROOT / "docs" / "assets" / "images" / "wiki"
IMG_WP = REPO_ROOT / "docs" / "assets" / "images" / "transmodel-cen"
FILES_DIR = REPO_ROOT / "docs" / "assets" / "files"


IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}
FILE_EXTS = {".pdf", ".zip", ".xlsx", ".xls", ".pptx", ".ppt", ".docx", ".doc"}


def find_wiki_references(md_dir: Path) -> Set[str]:
    """Find bare-filename image references in wiki markdown.

    Wiki pandoc conversion produces things like:
        ![alt](Australia_architecture.jpg "title")
        ![alt](Stop_assignment_model.png "title")
    We collect the filename part.
    """
    refs: Set[str] = set()
    # Match ![...](filename.ext) or ![...](filename.ext "title")
    # Only bare filenames (no slash, no http)
    pattern = re.compile(
        r'!\[[^\]]*\]\(([^)/\s]+\.(?:png|jpg|jpeg|gif|svg|pdf|webp))(?:\s+"[^"]*")?\)',
        re.IGNORECASE,
    )
    for md_path in md_dir.glob("*.md"):
        text = md_path.read_text(encoding="utf-8")
        for match in pattern.finditer(text):
            refs.add(match.group(1))
    return refs


def find_wp_references(md_dir: Path) -> Set[str]:
    """Find full-URL image/file references in WordPress markdown.

    Returns just the basenames since the WP zip is mostly flat.
    """
    refs: Set[str] = set()
    pattern = re.compile(
        r'https?://[^)"\s]*/wp-content/uploads/[^)"\s]+\.(?:png|jpg|jpeg|gif|svg|pdf|webp|zip|xlsx|xls|pptx|ppt|docx|doc)',
        re.IGNORECASE,
    )
    for md_path in md_dir.rglob("*.md"):
        text = md_path.read_text(encoding="utf-8")
        for match in pattern.finditer(text):
            refs.add(Path(match.group(0)).name)
    return refs


def extract_wiki_images(zip_path: Path, needed: Set[str], out_dir: Path) -> Dict[str, Path]:
    """Extract wiki images that are actually referenced.

    Returns {basename: local_path_relative_to_repo_root}.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    extracted: Dict[str, Path] = {}
    collisions: List[Tuple[str, str]] = []

    with zipfile.ZipFile(zip_path) as zf:
        for info in zf.infolist():
            if info.is_dir():
                continue
            name = info.filename
            basename = Path(name).name
            # Skip the sized thumbnails — we want originals
            # The originals live at "0/00/File.png", thumbnails at "thumb/0/00/File.png/300px-File.png"
            if name.startswith("thumb/"):
                # Thumbnail: skip UNLESS we specifically want it AND no original exists
                continue
            if name.startswith("temp/") or name.startswith("archive/") or name.startswith("deleted/"):
                continue
            if basename in needed and basename not in extracted:
                target = out_dir / basename
                with zf.open(info) as src, open(target, "wb") as dst:
                    shutil.copyfileobj(src, dst)
                extracted[basename] = target.relative_to(REPO_ROOT)
            elif basename in extracted:
                collisions.append((basename, name))

    # For any needed image we didn't find as an "original", try to fall back to
    # the largest thumbnail available.
    still_missing = needed - set(extracted.keys())
    if still_missing:
        with zipfile.ZipFile(zip_path) as zf:
            for info in zf.infolist():
                if info.is_dir() or not info.filename.startswith("thumb/"):
                    continue
                # Path format: thumb/X/YY/OriginalName.png/300px-OriginalName.png
                parts = info.filename.split("/")
                if len(parts) >= 5:
                    original = parts[3]  # OriginalName.png
                    if original in still_missing and original not in extracted:
                        target = out_dir / original
                        with zf.open(info) as src, open(target, "wb") as dst:
                            shutil.copyfileobj(src, dst)
                        extracted[original] = target.relative_to(REPO_ROOT)

    if collisions:
        print(f"  (skipped {len(collisions)} filename collisions — first occurrence kept)")

    return extracted


def extract_wp_files(zip_path: Path, needed: Set[str], img_dir: Path, files_dir: Path) -> Dict[str, Path]:
    """Extract WordPress images/files matching the needed basenames.

    Returns {basename: local_path_relative_to_repo_root}.
    """
    img_dir.mkdir(parents=True, exist_ok=True)
    files_dir.mkdir(parents=True, exist_ok=True)
    extracted: Dict[str, Path] = {}

    with zipfile.ZipFile(zip_path) as zf:
        for info in zf.infolist():
            if info.is_dir():
                continue
            basename = Path(info.filename).name
            if basename not in needed:
                continue
            if basename in extracted:
                continue
            ext = Path(basename).suffix.lower()
            if ext in IMAGE_EXTS:
                target = img_dir / basename
            elif ext in FILE_EXTS:
                target = files_dir / basename
            else:
                continue
            with zf.open(info) as src, open(target, "wb") as dst:
                shutil.copyfileobj(src, dst)
            extracted[basename] = target.relative_to(REPO_ROOT)

    return extracted


def rewrite_wiki_markdown(md_dir: Path, extracted: Dict[str, Path]) -> int:
    """Rewrite image references in wiki markdown to point at local paths."""
    n_changed = 0
    for md_path in md_dir.glob("*.md"):
        original = md_path.read_text(encoding="utf-8")
        text = original
        for basename, local_path in extracted.items():
            # From _staging/data4pt-wiki/foo.md the relative path is:
            # ../../docs/assets/images/wiki/<basename>
            rel = Path("../..") / local_path
            # Replace bare filename in ![alt](name.ext) pattern
            pattern = re.compile(
                r'(!\[[^\]]*\]\()' + re.escape(basename) + r'((?:\s+"[^"]*")?\))',
                re.IGNORECASE,
            )
            text = pattern.sub(lambda m: f'{m.group(1)}{rel}{m.group(2)}', text)
        if text != original:
            md_path.write_text(text, encoding="utf-8")
            n_changed += 1
    return n_changed


def rewrite_wp_markdown(md_dir: Path, extracted: Dict[str, Path]) -> int:
    """Rewrite WP URLs to local paths."""
    n_changed = 0
    for md_path in md_dir.rglob("*.md"):
        original = md_path.read_text(encoding="utf-8")
        text = original
        # For each extracted file, replace any full URL that ends with that basename
        for basename, local_path in extracted.items():
            depth = len(md_path.relative_to(md_dir).parts) - 1  # number of subfolders
            rel = Path("/".join([".."] * (depth + 2))) / local_path
            # Match http(s)://.../wp-content/uploads/.../<basename>
            pattern = re.compile(
                r'https?://[^)"\s]*/wp-content/uploads/[^)"\s]*/' + re.escape(basename),
                re.IGNORECASE,
            )
            text = pattern.sub(str(rel), text)
        if text != original:
            md_path.write_text(text, encoding="utf-8")
            n_changed += 1
    return n_changed


def main() -> int:
    print("Scanning _staging/ for image references...")
    wiki_refs = find_wiki_references(STAGING / "data4pt-wiki")
    wp_refs = find_wp_references(STAGING / "transmodel-cen")
    print(f"  wiki: {len(wiki_refs)} unique filenames referenced")
    print(f"  WP:   {len(wp_refs)} unique filenames referenced")

    print("\nExtracting wiki images...")
    wiki_extracted = extract_wiki_images(WIKI_ZIP, wiki_refs, IMG_WIKI)
    missing_wiki = wiki_refs - set(wiki_extracted.keys())
    print(f"  extracted: {len(wiki_extracted)}")
    if missing_wiki:
        print(f"  MISSING (referenced but not in zip): {len(missing_wiki)}")
        for m in sorted(missing_wiki)[:10]:
            print(f"    - {m}")

    print("\nExtracting WP files...")
    wp_extracted = extract_wp_files(WP_ZIP, wp_refs, IMG_WP, FILES_DIR)
    missing_wp = wp_refs - set(wp_extracted.keys())
    print(f"  extracted: {len(wp_extracted)}")
    if missing_wp:
        print(f"  MISSING: {len(missing_wp)}")
        for m in sorted(missing_wp)[:10]:
            print(f"    - {m}")

    print("\nRewriting wiki markdown...")
    n1 = rewrite_wiki_markdown(STAGING / "data4pt-wiki", wiki_extracted)
    print(f"  files changed: {n1}")

    print("\nRewriting WP markdown...")
    n2 = rewrite_wp_markdown(STAGING / "transmodel-cen", wp_extracted)
    print(f"  files changed: {n2}")

    print("\nDone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
