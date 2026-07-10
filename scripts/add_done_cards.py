#!/usr/bin/env python3
"""Add cards for the pages that were washed before the board was set up.

Creates one issue per already-washed page, adds it to the project, sets
Status = Done and Disposition = keep/merge/etc. Idempotent-ish — will
create duplicates if run twice, so run once only.

Prerequisites:
    gh CLI authenticated with 'project' scope.

Usage:
    python scripts/add_done_cards.py             # create for real
    python scripts/add_done_cards.py --dry-run   # preview only
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys

REPO = "BredeD/transmodel-site"
OWNER = "BredeD"
PROJECT_NUMBER = 4
DISPOSITION_FIELD_NAME = "Disposition"
STATUS_FIELD_NAME = "Status"


# Hardcoded — the 7 pages that were washed before the board existed.
# docs/index.md is already tracked separately, so it's not here.
DONE_CARDS = [
    {
        "target": "about/index.md",
        "sources": [],
        "disposition": "keep",
        "note": "New ecosystem-level landing page. Rewritten from scratch after the site restructure.",
    },
    {
        "target": "about/purpose.md",
        "sources": ["transmodel-cen/purpose.md"],
        "disposition": "keep",
        "note": "",
    },
    {
        "target": "about/legal-context.md",
        "sources": ["transmodel-cen/legal-context.md"],
        "disposition": "keep",
        "note": "",
    },
    {
        "target": "about/governance.md",
        "sources": ["transmodel-cen/governance.md"],
        "disposition": "keep",
        "note": "",
    },
    {
        "target": "about/team.md",
        "sources": ["transmodel-cen/team.md"],
        "disposition": "keep",
        "note": "Two portrait images missing from the export.",
    },
    {
        "target": "standards/transmodel/index.md",
        "sources": ["transmodel-cen/about.md"],
        "disposition": "keep",
        "note": "POC 1. Originally washed as `about/index.md`, later moved here and expanded with the 'Transmodel is conceptual' callout and the Adopters section.",
    },
    {
        "target": "standards/netex/index.md",
        "sources": ["data4pt-wiki/netex.md", "transmodel-cen/netex.md"],
        "disposition": "merge",
        "note": "POC 2. Merged from wiki (conversion-failed, raw wikitext) and WordPress netex.md. Iterated multiple rounds — expanded intro, added 'What NeTEx can exchange' list, EU-wide profile note with NAPCORE, Nordic profile detail, alternative-modes callout with GBFS/TOMP/MDS.",
    },
]


STANDARDS = {
    "netex": "NeTEx",
    "siri": "SIRI",
    "ojp": "OJP",
    "opra": "OpRa",
    "transmodel": "Transmodel",
}


# --- gh CLI wrapper ---------------------------------------------------------

def gh(args, check=True):
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args[:3])} failed: {r.stderr.strip()}")
    return r.returncode, r.stdout.strip(), r.stderr.strip()


# --- Human title (same rules as rename_cards.py) ---------------------------

def human_title(target: str) -> str:
    t = target.strip()
    if t.startswith("docs/"):
        t = t[len("docs/"):]
    if t == "index.md" or t == "":
        return "Home page"
    parts = t.replace(".md", "").split("/")

    if parts[0] == "about":
        if len(parts) == 1 or parts[-1] == "index":
            return "About the ecosystem"
        if len(parts) == 3 and parts[1] == "conformity":
            if parts[-1] == "index":
                return "Conformity overview"
            return "Conformity: " + parts[-1].replace("-", " ").capitalize()
        return parts[-1].replace("-", " ").capitalize()

    if parts[0] == "standards":
        if len(parts) == 2:
            if parts[1] == "index":
                return "Standards overview"
            if parts[1] in STANDARDS:
                return f"{STANDARDS[parts[1]]} overview"
            return "Standards: " + parts[1].replace("-", " ").capitalize()
        if len(parts) == 3:
            std = STANDARDS.get(parts[1], parts[1].capitalize())
            sub = parts[2]
            if sub == "index":
                return f"{std} overview"
            return f"{std}: {sub.replace('-', ' ').capitalize()}"

    if parts[0] == "implementations":
        if parts[-1] == "index":
            return "Implementations overview"
        if len(parts) == 3 and parts[1] == "countries":
            return f"Country: {parts[2].replace('-', ' ').title()}"
        return "Implementations: " + parts[-1].replace("-", " ").capitalize()

    if parts[0] == "faq":
        if parts[1] == "index":
            return "FAQ (general)"
        topic = parts[1]
        if topic in STANDARDS:
            return f"{STANDARDS[topic]} FAQ"
        return f"FAQ: {topic.replace('-', ' ').capitalize()}"

    if parts[0] == "documentation":
        if parts[1] == "index":
            return "Documentation overview"
        return "Documentation: " + parts[1].replace("-", " ").capitalize()

    if len(parts) == 1:
        return parts[0].replace("-", " ").capitalize()

    return target.replace(".md", "").replace("/", " → ")


# --- Issue body ------------------------------------------------------------

def source_link(source_file):
    return f"https://github.com/{REPO}/blob/main/_staging/{source_file}"


def build_body(card):
    lines = [
        f"**Target:** `docs/{card['target']}` — *this page is already washed and live.*",
        "",
        f"**Disposition:** `{card['disposition']}`",
        "",
    ]
    if card["sources"]:
        if len(card["sources"]) == 1:
            src = card["sources"][0]
            lines += [
                f"**Source:** `_staging/{src}` — [open on GitHub]({source_link(src)})",
                "",
            ]
        else:
            lines += ["**Sources merged:**", ""]
            for src in card["sources"]:
                lines.append(f"- `_staging/{src}` ([open]({source_link(src)}))")
            lines.append("")
    else:
        lines += [
            "**No source page** — this was authored from scratch, not derived from either legacy site.",
            "",
        ]
    if card["note"]:
        lines += [f"**Note:** {card['note']}", ""]
    lines += [
        "---",
        "",
        "Card added retroactively to record work completed before the board was set up.",
    ]
    return "\n".join(lines)


# --- Project GraphQL --------------------------------------------------------

def get_project_metadata():
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
    field_lookup = {}
    for f in data["fields"]["nodes"] or []:
        if not f or "name" not in f:
            continue
        options = {o["name"].lower(): o["id"] for o in f.get("options", [])}
        field_lookup[f["name"]] = {"id": f["id"], "options": options}
    return project_id, field_lookup


def add_to_project(issue_url):
    rc, out, _ = gh([
        "project", "item-add", str(PROJECT_NUMBER),
        "--owner", OWNER,
        "--url", issue_url,
        "--format", "json",
    ], check=False)
    if rc != 0:
        return None
    try:
        return json.loads(out)["id"]
    except Exception:
        return None


def set_field(project_id, item_id, field_id, option_id):
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


# --- Labels -----------------------------------------------------------------

def labels_for(card):
    sources = card["sources"]
    if not sources:
        source_label = "source: multi"  # "no source" fits multi/new bucket
    elif len(sources) == 1:
        if "data4pt-wiki" in sources[0]:
            source_label = "source: wiki"
        elif "transmodel-cen" in sources[0]:
            source_label = "source: wp"
        else:
            source_label = "source: multi"
    else:
        source_label = "source: multi"
    return f"{source_label},disposition: {card['disposition']}"


# --- Main -------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    args = parser.parse_args()

    # Auth check
    rc, _, _ = gh(["auth", "status"], check=False)
    if rc != 0:
        print("ERROR: gh not authenticated.", file=sys.stderr)
        return 1

    # Project metadata
    project_id = None
    fields = {}
    if not args.dry_run:
        try:
            project_id, fields = get_project_metadata()
        except Exception as e:
            print(f"ERROR fetching project: {e}", file=sys.stderr)
            return 1

    status_field = fields.get(STATUS_FIELD_NAME)
    disposition_field = fields.get(DISPOSITION_FIELD_NAME)

    if not args.dry_run:
        if not status_field:
            print(f"WARNING: '{STATUS_FIELD_NAME}' field not found — will skip moving to In review.")
        elif "in review" not in status_field["options"] and "in-review" not in status_field["options"]:
            print(f"WARNING: 'In review' option not found in Status field. Available: {list(status_field['options'])}")
        if not disposition_field:
            print(f"WARNING: '{DISPOSITION_FIELD_NAME}' field not found — will skip disposition.")

    print(f"Creating {len(DONE_CARDS)} cards for already-washed pages:\n")

    for card in DONE_CARDS:
        title = f"{human_title(card['target'])} — {card['target']}"
        body = build_body(card)
        labels = labels_for(card)

        if args.dry_run:
            print(f"  would create: {title}")
            print(f"    labels: {labels}")
            print(f"    disposition: {card['disposition']}, status: In review")
            print()
            continue

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

        # Add to project
        item_id = add_to_project(issue_url)
        if not item_id:
            print("    (could not add to project — check auto-add workflow or add manually)")
            continue

        # Set Disposition
        if disposition_field:
            opt = disposition_field["options"].get(card["disposition"])
            if opt:
                set_field(project_id, item_id, disposition_field["id"], opt)

        # Set Status = In review
        if status_field and "in review" in status_field["options"]:
            set_field(project_id, item_id, status_field["id"], status_field["options"]["in review"])
        elif status_field and "in-review" in status_field["options"]:
            set_field(project_id, item_id, status_field["id"], status_field["options"]["in-review"])

    print()
    print("Done.")
    if not args.dry_run:
        print("Refresh the board — 7 new cards should appear in the 'In review' column.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
