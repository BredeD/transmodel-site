#!/usr/bin/env python3
"""Backfill the Disposition field on all project items.

Reads each project item's linked issue labels, finds the
'disposition: <name>' label, and sets the corresponding option
on the Disposition Single-select field in the project.

Use this if:
- The Disposition field was added after the cards were created
- The field is empty and needs to be filled from labels
- The field name is different from the script default

Prerequisites: gh CLI authenticated with 'project' scope.

Usage:
    python scripts/backfill_disposition.py                   # default field name "Disposition"
    python scripts/backfill_disposition.py --field-name Disposisjon
    python scripts/backfill_disposition.py --dry-run
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys

OWNER = "BredeD"
PROJECT_NUMBER = 4


def gh(args, check=True):
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"gh failed: {r.stderr.strip()}")
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def get_project(field_name):
    """Get project id, target field id, and its options."""
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
    options = {}
    for f in data["fields"]["nodes"] or []:
        if f and f.get("name") == field_name:
            field_id = f["id"]
            options = {o["name"].lower(): o["id"] for o in f["options"]}
            break
    if not field_id:
        raise RuntimeError(f"Field '{field_name}' not found in project. Available fields: "
                           + ", ".join(sorted(n['name'] for n in data['fields']['nodes'] if n and 'name' in n)))
    return project_id, field_id, options


def list_project_items(project_id):
    """List all items in the project with linked issue labels."""
    items = []
    cursor = None
    while True:
        after = f', after: "{cursor}"' if cursor else ""
        query = f"""
        query {{
          node(id: "{project_id}") {{
            ... on ProjectV2 {{
              items(first: 100{after}) {{
                pageInfo {{ hasNextPage endCursor }}
                nodes {{
                  id
                  content {{
                    ... on Issue {{
                      number
                      title
                      labels(first: 20) {{ nodes {{ name }} }}
                    }}
                  }}
                }}
              }}
            }}
          }}
        }}
        """
        rc, out, _ = gh(["api", "graphql", "-f", f"query={query}"])
        page = json.loads(out)["data"]["node"]["items"]
        items.extend(page["nodes"])
        if not page["pageInfo"]["hasNextPage"]:
            break
        cursor = page["pageInfo"]["endCursor"]
    return items


def extract_disposition_from_labels(labels):
    """Find the 'disposition: X' label and return X."""
    for lbl in labels:
        name = lbl.get("name", "")
        if name.startswith("disposition: "):
            return name.replace("disposition: ", "").strip().lower()
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


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--field-name", default="Disposition",
                        help="Name of the Single-select field in the project (default: Disposition)")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    args = parser.parse_args()

    try:
        project_id, field_id, options = get_project(args.field_name)
    except RuntimeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    print(f"Project: {project_id}")
    print(f"Field '{args.field_name}': {field_id}")
    print(f"Available options: {', '.join(options.keys())}\n")

    items = list_project_items(project_id)
    print(f"Found {len(items)} project items.\n")

    set_count = 0
    skipped = 0
    for item in items:
        content = item.get("content") or {}
        title = content.get("title", "(no title)")
        labels = content.get("labels", {}).get("nodes", [])
        disposition = extract_disposition_from_labels(labels)

        if not disposition:
            print(f"  skip (no disposition label): {title}")
            skipped += 1
            continue

        option_id = options.get(disposition)
        if not option_id:
            print(f"  skip (no matching option '{disposition}' in project field): {title}")
            skipped += 1
            continue

        if args.dry_run:
            print(f"  would set '{disposition}': {title}")
        else:
            set_field(project_id, item["id"], field_id, option_id)
            print(f"  ✓ {disposition}: {title}")
        set_count += 1

    print(f"\n{'Would set' if args.dry_run else 'Set'} {set_count} items. Skipped {skipped}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
