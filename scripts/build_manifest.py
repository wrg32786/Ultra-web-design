#!/usr/bin/env python3
"""Build the complete reference manifest from ordered source modules."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "ultra-web-design"
HEADER = SKILL_DIR / "MANIFEST.header.md"
MODULES = SKILL_DIR / "modules"
OUTPUT = SKILL_DIR / "MANIFEST.md"


def expected_manifest() -> str:
    module_paths = sorted(MODULES.glob("[0-9][0-9]-*.md"))
    if len(module_paths) != 10:
        raise SystemExit(f"Expected 10 ordered modules, found {len(module_paths)}")

    parts = [HEADER.read_text(encoding="utf-8").rstrip()]
    parts.extend(path.read_text(encoding="utf-8").strip() for path in module_paths)
    return "\n\n".join(parts) + "\n"


def main() -> None:
    OUTPUT.write_text(expected_manifest(), encoding="utf-8")
    print(f"Built {OUTPUT.relative_to(ROOT)} from 10 modules")


if __name__ == "__main__":
    main()
