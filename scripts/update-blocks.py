#!/usr/bin/env python3
"""List public GitHub repos for an org, filtered by repo-name prefix, and write a blocks.json registry.

Output matches blocks.schema.json: {"version": 1, "blocks": [{id, category, description, url}, ...]}.
`category` is derived from the matching prefix (see BLOCK_PREFIXES / COLLECTION_PREFIXES).

Usage:
    scripts/update-blocks.py

Archived repos are skipped. Set GITHUB_TOKEN to raise the API rate limit (optional; only public data is read).
"""
import json
import os
from pathlib import Path
import sys
import urllib.error
import urllib.request

API = "https://api.github.com"
ORG = "edgeimpulse"
SCHEMA_VERSION = 1
OUTPUT = Path(__file__).resolve().parent.parent / "blocks.json"
# Refuse to overwrite the registry if the block count falls by more than this fraction.
MAX_DROP = 0.2
BLOCK_PREFIXES = (
    "deployment-block",
    "labeling-block",
    "learning-block",
    "processing-block",
    "synthetic-data-block",
    "transformation-block",
)
COLLECTION_PREFIXES = (
    "custom-blocks-",
    "deployment-blocks",
    "labeling-blocks",
    "learning-blocks",
    "processing-blocks",
    "synthetic-data-blocks",
    "transformation-blocks",
)


def categorize(name):
    """Return the category for a repo name, or None if it matches no prefix."""
    name = name.lower()
    if name.startswith(COLLECTION_PREFIXES):
        return "collection"
    for prefix in BLOCK_PREFIXES:
        if name.startswith(prefix):
            return prefix.removesuffix("-block")
    return None


def fetch_public_repos(org):
    """Yield all public repos for an org, following pagination."""
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "update-blocks-script",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    page = 1
    while True:
        url = f"{API}/orgs/{org}/repos?type=public&per_page=100&page={page}"
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                repos = json.load(resp)
        except urllib.error.HTTPError as e:
            sys.exit(f"GitHub API error {e.code} for org '{org}': {e.reason}")
        except urllib.error.URLError as e:
            sys.exit(f"Network error: {e.reason}")
        if not repos:
            return
        yield from repos
        page += 1


def check_not_truncated(new_count):
    """Exit if the result looks like a truncated/failed fetch rather than a real change."""
    if new_count == 0:
        sys.exit("No matching repos found; refusing to write an empty registry.")
    if not OUTPUT.exists():
        return
    with open(OUTPUT, encoding="utf-8") as f:
        old_count = len(json.load(f)["blocks"])
    if old_count and new_count < old_count * (1 - MAX_DROP):
        sys.exit(
            f"Block count dropped from {old_count} to {new_count} "
            f"(more than {MAX_DROP:.0%}); refusing to overwrite {OUTPUT.name}."
        )


def main():
    rows = []
    for r in fetch_public_repos(ORG):
        if r.get("archived"):
            continue
        category = categorize(r["name"])
        if category:
            rows.append({
                "id": r["name"],
                "category": category,
                "description": r.get("description") or "",
                "url": r["html_url"],
            })
    rows.sort(key=lambda row: row["id"])

    check_not_truncated(len(rows))

    registry = {"version": SCHEMA_VERSION, "blocks": rows}
    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Wrote {len(rows)} repos from '{ORG}' to {OUTPUT}")


if __name__ == "__main__":
    main()
