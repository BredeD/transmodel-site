#!/usr/bin/env python3
"""Rebuild the wash board with target-focused issues.

Reads STATUS.md, groups source pages by their target new-site path,
and creates one GitHub Issue per target. Special aggregate cards for
'delete' and 'guides' dispositions to keep those visible on the board.

Also sets the custom "Disposition" field on each project item via
GraphQL, so board can be grouped/filtered by disposition.

Prerequisites:
    brew install gh
    gh auth login
    gh auth refresh -s project

Usage:
    python scripts/rebuild_board.py --dry-run          # preview only
    python scripts/rebuild_board.py --close-existing   # close old + create new
    python scripts/rebuild_board.py                    # just create new
    python scripts/rebuild_board.py --skip-project     # skip project bits

Notes:
    - Rows already marked done in STATUS.md are skipped.
    - The Disposition field must exist in the project as a Single-select
      with options: keep, merge, rewrite, guides, delete.
      Names are lowercased for matching.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STATUS_PATH = REPO_ROOT / "STATUS.md"

# Adjust if repo or project changes
REPO = "BredeD/transmodel-site"
OWNER = "BredeD"
PROJECT_NUMBER = 4
DISPOSITION_FIELD_NAME = "Disposition"


# Labels to ensure exist
LABELS = {
    "source: wiki":         ("c5def5", "Content from data4pt.org/wiki"),
    "source: wp":           ("c5def5", "Content from transmodel-cen.eu"),
    "source: multi":        ("c5def5", "Aggregated card covering multiple sources"),
    "disposition: keep":    ("0e8a16", "Move to docs/ with light editing"),
    "disposition: merge":   ("1d76db", "Combine multiple sources into one target"),
    "disposition: rewrite": ("fbca04", "Substantial cleanup or restructure"),
    "disposition: guides":  ("5319e7", "Hand off to CEN Guides project"),
    "disposition: delete":  ("b60205", "Remove entirely"),
}


# Matches one STATUS.md table row: | `file` | title | words | disp | target | notes | owner | status |
_TABLE_ROW = re.compile(
    r"^\|\s*"
    r"`([^`]+)`\s*\|\s*"
    r"([^|]+?)\s*\|\s*"
    r"(\d+)\s*\|\s*"
    r"([a-z]+)\s*\|\s*"
    r"([^|]+?)\s*\|\s*"
    r"([^|]*?)\s*\|\s*"
    r"([^|]*?)\s*\|\s*"
    r"([^|]+?)\s*\|",
    re.MULTILINE,
)


# --- gh CLI wrapper ----------------------------------------------------------

def gh(args: list[str], check: bool = True) -> tuple[int, str, str]:
    result = subprocess.run(["gh", *args], capture_output=True, text=True)
    if check and result.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args[:3])}...\n  {result.stderr.strip()}")
    return result.returncode, result.stdout.strip(), result.stderr.strip()


# --- STATUS.md parsing -------------------------------------------------------

def parse_status() -> list[dict]:
    text = STATUS_PATH.read_text(encoding="utf-8")
    entries = []
    for m in _TABLE_ROW.finditer(text):
        entries.append({
            "source_file": m.group(1).strip(),
            "title": m.group(2).strip(),
            "words": int(m.group(3)),
            "disposition": m.group(4).strip().lower(),
            "target": m.group(5).strip().strip("`").strip(),
            "notes": m.group(6).strip(),
            "owner": m.group(7).strip(),
            "status": m.group(8).strip().lower(),
        })
    return entries


# --- Grouping ----------------------------------------------------------------

def group_entries(entries: list[dict]) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = defaultdict(list)
    for entry in entries:
        # Skip already-done rows — no card needed
        if "done" in entry["status"]:
            continue
        if entry["disposition"] == "delete":
            groups["__delete__"].append(entry)
        elif entry["disposition"] == "guides":
            groups["__guides__"].append(entry)
        else:
            target = entry["target"]
            if not target or target in ("—", "-"):
                groups["__unknown__"].append(entry)
            else:
                groups[target].append(entry)
    return groups


# --- Issue building ----------------------------------------------------------

def source_kind(source_file: str) -> str:
    if "data4pt-wiki" in source_file:
        return "wiki"
    if "transmodel-cen" in source_file:
        return "wp"
    return "unknown"


def source_link(source_file: str) -> str:
    return f"https://github.com/{REPO}/blob/main/_staging/{source_file}"


def branch_name(target: str) -> str:
    """faq/netex.md -> wash/faq-netex"""
    slug = target.replace("/", "-").replace(".md", "")
    return f"wash/{slug}"


def build_regular_issue(target: str, entries: list[dict]) -> tuple[str, str, str]:
    """Return (title, body, disposition) for one target."""
    dispositions = {e["disposition"] for e in entries}
    disposition = "merge" if len(entries) > 1 or len(dispositions) > 1 else next(iter(dispositions))

    lines = [
        f"**Target:** `docs/{target}`",
        "",
        f"**Disposition:** `{disposition}`",
        "",
    ]

    if len(entries) == 1:
        e = entries[0]
        lines += [
            f"**Source:** `_staging/{e['source_file']}` — [open on GitHub]({source_link(e['source_file'])})",
            "",
            f"- Original title: {e['title']}",
            f"- Word count: {e['words']}",
        ]
        if e["notes"]:
            lines += ["", f"**Notes:** {e['notes']}"]
    else:
        lines += ["**Sources to combine:**", ""]
        for e in entries:
            lines.append(
                f"- `_staging/{e['source_file']}` ([open]({source_link(e['source_file'])})) — "
                f"{e['title']} ({e['words']} words)"
            )
        notes = [f"- from `{e['source_file']}`: {e['notes']}" for e in entries if e["notes"]]
        if notes:
            lines += ["", "**Notes:**"] + notes

    lines += [
        "",
        "---",
        "",
        "## Workflow",
        "",
        "1. Assign this issue to yourself.",
        f"2. Create branch `{branch_name(target)}`.",
        f"3. Follow [WASH-GUIDE.md](https://github.com/{REPO}/blob/main/WASH-GUIDE.md) — brief the AI, review, commit.",
        "4. Open PR referencing this issue with `Closes #<issue-number>`.",
        "5. When merged, update `STATUS.md` and close.",
    ]

    return target, "\n".join(lines), disposition


def build_delete_issue(entries: list[dict]) -> tuple[str, str, str]:
    title = "Clean up: delete legacy pages"
    lines = [
        "**Aggregate task.** Delete the legacy source pages that don't have a target on the new site.",
        "",
        f"**Count:** {len(entries)} pages.",
        "",
        "## Pages to delete",
        "",
    ]
    for e in entries:
        lines.append(
            f"- `_staging/{e['source_file']}` ({e['title']}, {e['words']} words) — {e['notes'] or 'no notes'}"
        )
    lines += [
        "",
        "---",
        "",
        "## Workflow",
        "",
        "1. Assign this issue to yourself.",
        "2. Create branch `chore/delete-legacy-pages`.",
        "3. Delete each `_staging/…` file listed above.",
        "4. Update `STATUS.md` — mark rows as `deleted`.",
        "5. Open PR, `Closes #<issue-number>`.",
    ]
    return title, "\n".join(lines), "delete"


def build_guides_issue(entries: list[dict]) -> tuple[str, str, str]:
    title = "Hand-off: tutorials for the CEN Guides project"
    lines = [
        "**Aggregate task.** These tutorials belong in the [CEN Guides project](https://github.com/TransmodelEcosystem/NeTEx-Guides-Documentation), not on this site. Track hand-off progress here.",
        "",
        f"**Count:** {len(entries)} pages.",
        "",
        "## Pages to hand off",
        "",
    ]
    for e in entries:
        lines.append(
            f"- `_staging/{e['source_file']}` — {e['title']} ({e['words']} words)"
        )
    lines += [
        "",
        "---",
        "",
        "## Workflow",
        "",
        "1. When the Guides team is ready to work on a topic, they can pull raw material from `_staging/`.",
        "2. When a Guide is published covering the topic, add its URL here and check off the entry.",
        "3. Close this issue when all hand-offs are complete or archived.",
    ]
    return title, "\n".join(lines), "guides"


# --- Labels ------------------------------------------------------------------

def ensure_labels() -> None:
    for name, (colour, desc) in LABELS.items():
        gh([
            "label", "create", name,
            "--color", colour,
            "--description", desc,
            "--force",
        ], check=False)


def labels_for(entries: list[dict], disposition: str) -> str:
    sources = {source_kind(e["source_file"]) for e in entries}
    if len(sources) > 1:
        source_label = "source: multi"
    else:
        source_label = f"source: {next(iter(sources))}"
    return f"{source_label},disposition: {disposition}"


# --- Close existing ----------------------------------------------------------

def close_existing_issues() -> None:
    rc, out, _ = gh([
        "issue", "list",
        "--repo", REPO,
        "--state", "open",
        "--limit", "500",
        "--json", "number",
    ])
    numbers = [str(n["number"]) for n in json.loads(out)]
    print(f"Closing {len(numbers)} existing open issues...")
    for num in numbers:
        gh(["issue", "close", num, "--repo", REPO,
            "--comment", "Superseded by target-focused board."], check=False)
    print(f"  closed {len(numbers)} issues\n")


# --- Project (GraphQL) -------------------------------------------------------

def get_project_metadata() -> tuple[str, str | None, dict[str, str]]:
    """Return (projectId, dispositionFieldId, {optionName: optionId})."""
    query = """
    query($owner: String!, $number: Int!) {
      user(login: $owner) {
        projectV2(number: $number) {
          id
          fields(first: 50) {
            nodes {
              ... on ProjectV2SingleSelectField {
                id
                name
                options { id name }
              }
            }
          }
        }
      }
    }
    """
    rc, out, _ = gh([
        "api", "graphql",
        "-f", f"owner={OWNER}",
        "-F", f"number={PROJECT_NUMBER}",
        "-f", f"query={query}",
    ])
    data = json.loads(out)["data"]["user"]["projectV2"]
    project_id = data["id"]
    field_id = None
    options: dict[str, str] = {}
    for f in data["fields"]["nodes"] or []:
        if f and f.get("name") == DISPOSITION_FIELD_NAME:
            field_id = f["id"]
            options = {o["name"].lower(): o["id"] for o in f.get("options", [])}
            break
    return project_id, field_id, options


def add_item_to_project(issue_url: str) -> str | None:
    """Add issue to project, return item ID (or None if fails)."""
    rc, out, err = gh([
        "project", "item-add", str(PROJECT_NUMBER),
        "--owner", OWNER,
        "--url", issue_url,
        "--format", "json",
    ], check=False)
    if rc != 0:
        return None
    try:
        return json.loads(out)["id"]
    except (json.JSONDecodeError, KeyError):
        return None


def set_disposition(project_id: str, item_id: str, field_id: str, option_id: str) -> None:
    query = """
    mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $optionId: String!) {
      updateProjectV2ItemFieldValue(input: {
        projectId: $projectId
        itemId: $itemId
        fieldId: $fieldId
        value: { singleSelectOptionId: $optionId }
      }) {
        projectV2Item { id }
      }
    }
    """
    gh([
        "api", "graphql",
        "-f", f"projectId={project_id}",
        "-f", f"itemId={item_id}",
        "-f", f"fieldId={field_id}",
        "-f", f"optionId={option_id}",
        "-f", f"query={query}",
    ], check=False)


# --- Main --------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview what would be created without changing anything.")
    parser.add_argument("--close-existing", action="store_true",
                        help="Close all currently open issues before creating new ones.")
    parser.add_argument("--skip-project", action="store_true",
                        help="Don't add to project or set the Disposition field.")
    args = parser.parse_args()

    rc, _, _ = gh(["auth", "status"], check=False)
    if rc != 0:
        print("ERROR: gh not authenticated. Run: gh auth login && gh auth refresh -s project", file=sys.stderr)
        return 1

    if not STATUS_PATH.exists():
        print(f"ERROR: {STATUS_PATH} not found", file=sys.stderr)
        return 1

    # Get project metadata upfront
    project_id = field_id = None
    options: dict[str, str] = {}
    if not args.skip_project and not args.dry_run:
        try:
            project_id, field_id, options = get_project_metadata()
            if not field_id:
                print(f"WARNING: '{DISPOSITION_FIELD_NAME}' field not found in project — will skip field updates.\n")
        except Exception as e:
            print(f"WARNING: could not fetch project metadata: {e}", file=sys.stderr)
            print("Continuing without setting Disposition field.\n")

    entries = parse_status()
    groups = group_entries(entries)

    print(f"Parsed {len(entries)} rows from STATUS.md.")
    print(f"Grouped into {len(groups)} cards:")
    for k in sorted(groups.keys()):
        marker = "[aggregate]" if k.startswith("__") else ""
        print(f"  {k}: {len(groups[k])} source(s) {marker}")
    print()

    if args.dry_run:
        print("[DRY-RUN] Not creating anything.")
        return 0

    if args.close_existing:
        close_existing_issues()

    print("Ensuring labels exist...")
    ensure_labels()
    print()

    print("Creating issues:")
    created = 0
    for target, group in sorted(groups.items()):
        if target == "__delete__":
            title, body, disposition = build_delete_issue(group)
        elif target == "__guides__":
            title, body, disposition = build_guides_issue(group)
        elif target == "__unknown__":
            print(f"  Skipping {len(group)} entries with no valid target.")
            continue
        else:
            title, body, disposition = build_regular_issue(target, group)

        labels = labels_for(group, disposition)
        rc, out, err = gh([
            "issue", "create",
            "--repo", REPO,
            "--title", title,
            "--body", body,
            "--label", labels,
        ], check=False)
        if rc != 0:
            print(f"  ✗ {title}: {err}")
            continue
        issue_url = out.strip()
        print(f"  ✓ {title}")
        created += 1

        # Add to project + set Disposition field
        if project_id and field_id and options:
            item_id = add_item_to_project(issue_url)
            if item_id:
                option_id = options.get(disposition.lower())
                if option_id:
                    set_disposition(project_id, item_id, field_id, option_id)

    print(f"\nCreated {created} issues.")
    if project_id and field_id:
        print("Disposition field set on each item where possible.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
