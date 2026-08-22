#!/usr/bin/env python3
"""Build the installable SKILL.md from ordered source modules."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "ultra-web-design"
HEADER = SKILL_DIR / "SKILL.header.md"
MODULES = SKILL_DIR / "modules"
OUTPUT = SKILL_DIR / "SKILL.md"


def main() -> None:
    parts = [HEADER.read_text(encoding="utf-8").rstrip()]
    module_paths = sorted(MODULES.glob("[0-9][0-9]-*.md"))
    if not module_paths:
        raise SystemExit("No ordered modules found")
    parts.extend(path.read_text(encoding="utf-8").strip() for path in module_paths)
    OUTPUT.write_text("\n\n".join(parts) + "\n", encoding="utf-8")
    print(f"Built {OUTPUT.relative_to(ROOT)} from {len(module_paths)} modules")


if __name__ == "__main__":
    main()
