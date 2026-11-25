#!/usr/bin/env python3
"""Generate README.md from the blocks.json registry.

Usage:
    scripts/generate-readme.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "blocks.json"
OUTPUT = ROOT / "README.md"

# (category, heading) in README order.
INDIVIDUAL_SECTIONS = (
    ("deployment", "Deployment blocks"),
    ("labeling", "Labeling blocks"),
    ("learning", "Learning blocks"),
    ("processing", "Processing blocks"),
    ("synthetic-data", "Synthetic data blocks"),
    ("transformation", "Transformation blocks"),
)

INTRO = """\
Custom blocks let you extend Edge Impulse Studio with your own \
transformation, synthetic data, labeling, processing, learning, and deployment steps. \
See the [custom blocks documentation](https://docs.edgeimpulse.com/docs/edge-impulse-studio/organizations/custom-blocks) \
to learn how they work.

This page lists the public custom block example repositories in this \
GitHub organization. \
Block collections bundle several related blocks in one repository, \
and individual blocks are grouped by type below."""


def cell(text):
    """Make text safe for a single Markdown table cell."""
    text = " ".join(text.split())
    # Escape characters that could inject links, images, or HTML into the README.
    for ch in ("\\", "|", "<", ">", "[", "]"):
        text = text.replace(ch, "\\" + ch)
    return text


def table(blocks):
    lines = ["| Block | Description |", "| --- | --- |"]
    for b in sorted(blocks, key=lambda b: b["id"]):
        lines.append(f"| [{cell(b['id'])}]({b['url']}) | {cell(b['description'])} |")
    return "\n".join(lines)


def main():
    with open(REGISTRY, encoding="utf-8") as f:
        blocks = json.load(f)["blocks"]

    by_category = {}
    for b in blocks:
        by_category.setdefault(b["category"], []).append(b)

    parts = [
        "# Custom Blocks",
        INTRO,
        "<!-- Generated from blocks.json by scripts/generate-readme.py. Do not edit by hand. -->",
    ]
    parts += ["## Block collections", table(by_category.get("collection", []))]

    parts.append("## Individual blocks")
    for category, heading in INDIVIDUAL_SECTIONS:
        parts += [f"### {heading}", table(by_category.get(category, []))]

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n\n".join(parts) + "\n")

    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
