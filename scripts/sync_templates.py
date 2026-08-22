#!/usr/bin/env python3
"""Generate or verify standalone templates extracted from module 08."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "ultra-web-design"
SOURCE = SKILL_DIR / "modules" / "08-templates.md"
TEMPLATES = SKILL_DIR / "templates"

SECTION_TO_FILE = {
    1: "PRODUCT.md",
    2: "DIRECTION-CARD.md",
    3: "SURFACE-BRIEF.md",
    4: "DESIGN.md",
    5: "manifest.json",
    6: "tokens.css",
    7: "CONTENT-MATRIX.md",
    8: "MOTION-PLAN.md",
    9: "DECISIONS.md",
    10: "QA-REPORT.md",
    11: "REFERENCE-COMP-BIBLE.md",
    12: "BLOCK-RECORD.md",
}

SECTION_RE = re.compile(
    r"(?ms)^### 38\.(\d+)\b[^\n]*\n(.*?)(?=^### 38\.\d+\b|\Z)"
)
FENCE_RE = re.compile(r"(?ms)^```(?:markdown|json|css)?\s*\n(.*?)\n```\s*$", re.MULTILINE)
TOKEN_WARNING = (
    "/* TEMPLATE ONLY: replace project-specific values from the approved "
    "DESIGN.md; do not ship unchanged. */\n\n"
)


def normalize(text: str) -> str:
    return text.replace("\r\n", "\n").rstrip() + "\n"


def extracted_templates() -> dict[str, str]:
    text = SOURCE.read_text(encoding="utf-8")
    sections = {int(number): body for number, body in SECTION_RE.findall(text)}

    missing = sorted(set(SECTION_TO_FILE) - set(sections))
    if missing:
        raise ValueError(f"Missing template sections in {SOURCE}: {missing}")

    output: dict[str, str] = {}
    for number, filename in SECTION_TO_FILE.items():
        match = FENCE_RE.search(sections[number])
        if not match:
            raise ValueError(f"Section 38.{number} has no extractable fenced template")
        content = normalize(match.group(1))
        if filename == "tokens.css":
            content = TOKEN_WARNING + content
        output[filename] = content
    return output


def check() -> int:
    failed = False
    for filename, expected in extracted_templates().items():
        path = TEMPLATES / filename
        if not path.is_file():
            print(f"ERROR: missing generated template: {path.relative_to(ROOT)}", file=sys.stderr)
            failed = True
            continue
        actual = normalize(path.read_text(encoding="utf-8"))
        if actual != expected:
            print(
                f"ERROR: stale generated template: {path.relative_to(ROOT)}; "
                "run python scripts/sync_templates.py",
                file=sys.stderr,
            )
            failed = True
    return 1 if failed else 0


def write() -> None:
    TEMPLATES.mkdir(parents=True, exist_ok=True)
    for filename, content in extracted_templates().items():
        (TEMPLATES / filename).write_text(content, encoding="utf-8")
    print(f"Synchronized {len(SECTION_TO_FILE)} templates from {SOURCE.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail when generated templates are stale")
    args = parser.parse_args()

    if args.check:
        raise SystemExit(check())
    write()


if __name__ == "__main__":
    main()
