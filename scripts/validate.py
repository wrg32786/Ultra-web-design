#!/usr/bin/env python3
"""Validate the Ultra Web Design skill without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "ultra-web-design"
SKILL = SKILL_DIR / "SKILL.md"
HEADER = SKILL_DIR / "SKILL.header.md"
MODULES = SKILL_DIR / "modules"
TEMPLATES = SKILL_DIR / "templates"

REQUIRED_FRONTMATTER = {
    "name": "ultra-web-design",
    "version": "1.1.0",
    "status": "production",
    "license": "Apache-2.0",
}

REQUIRED_SOURCES = (
    "pbakaus/impeccable",
    "nextlevelbuilder/ui-ux-pro-max-skill",
    "emilkowalski/skills",
    "greensock/gsap-skills",
    "VoltAgent/awesome-design-md",
    "nexu-io/open-design",
    "Leonxlnx/taste-skill",
)

REQUIRED_TEMPLATES = (
    "PRODUCT.md",
    "DIRECTION-CARD.md",
    "SURFACE-BRIEF.md",
    "DESIGN.md",
    "manifest.json",
    "tokens.css",
    "CONTENT-MATRIX.md",
    "MOTION-PLAN.md",
    "DECISIONS.md",
    "QA-REPORT.md",
    "REFERENCE-COMP-BIBLE.md",
    "BLOCK-RECORD.md",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def expected_skill() -> str:
    module_paths = sorted(MODULES.glob("[0-9][0-9]-*.md"))
    if len(module_paths) != 10:
        fail(f"expected 10 ordered modules, found {len(module_paths)}")
    parts = [HEADER.read_text(encoding="utf-8").rstrip()]
    parts.extend(path.read_text(encoding="utf-8").strip() for path in module_paths)
    return "\n\n".join(parts) + "\n"


def parse_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter is not closed")
    return text[4:end]


def main() -> None:
    for required in (HEADER, MODULES, SKILL):
        if not required.exists():
            fail(f"missing required path: {required.relative_to(ROOT)}")

    text = SKILL.read_text(encoding="utf-8")
    expected = expected_skill()
    if text != expected:
        fail("SKILL.md is stale; run: python scripts/build_skill.py")

    frontmatter = parse_frontmatter(text)
    for key, value in REQUIRED_FRONTMATTER.items():
        if not re.search(rf"(?m)^{re.escape(key)}:\s*{re.escape(value)}\s*$", frontmatter):
            fail(f"frontmatter must contain {key}: {value}")

    if "# Ultra Web Design Manifest" not in text:
        fail("canonical title is missing")

    for number in range(44):
        if not re.search(rf"(?m)^## {number}\.\s", text):
            fail(f"missing numbered section {number}")

    for source in REQUIRED_SOURCES:
        if source not in frontmatter:
            fail(f"missing pinned source snapshot: {source}")

    line_count = len(text.splitlines())
    word_count = len(re.findall(r"\b\w+[\w'-]*\b", text))
    if line_count < 4_900:
        fail(f"SKILL.md appears truncated: {line_count} lines")
    if word_count < 25_000:
        fail(f"SKILL.md appears truncated: {word_count} words")

    for name in REQUIRED_TEMPLATES:
        path = TEMPLATES / name
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            fail(f"missing or empty template: {name}")

    print(
        f"OK: ultra-web-design v{REQUIRED_FRONTMATTER['version']} — "
        f"{line_count:,} lines, {word_count:,} words, "
        f"10 modules, {len(REQUIRED_SOURCES)} pinned sources, "
        f"{len(REQUIRED_TEMPLATES)} templates"
    )


if __name__ == "__main__":
    main()
