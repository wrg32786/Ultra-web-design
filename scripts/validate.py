#!/usr/bin/env python3
"""Validate runtime packaging, manifest integrity, templates, evals, and examples."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from build_manifest import expected_manifest
from sync_templates import extracted_templates, normalize

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "ultra-web-design"
SKILL = SKILL_DIR / "SKILL.md"
MANIFEST = SKILL_DIR / "MANIFEST.md"
MANIFEST_HEADER = SKILL_DIR / "MANIFEST.header.md"
MODULES = SKILL_DIR / "modules"
TEMPLATES = SKILL_DIR / "templates"
NOTICE = ROOT / "NOTICE.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
EVALS = SKILL_DIR / "evals" / "evals.json"
TRIGGERS = SKILL_DIR / "evals" / "trigger-queries.json"

ALLOWED_FRONTMATTER = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
    "allowed-tools",
}
REQUIRED_METADATA = {
    "version": "2.0.0",
    "status": "beta",
    "repository": "wrg32786/Ultra-web-design",
    "manifest": "MANIFEST.md",
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
EXAMPLE_DIRS = ("precision-saas", "local-service", "editorial")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter is not closed")
    return text[4:end], text[end + 5 :]


def top_level_keys(frontmatter: str) -> list[str]:
    keys: list[str] = []
    for line in frontmatter.splitlines():
        if not line or line[0].isspace() or line.lstrip().startswith("#"):
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):", line)
        if match:
            keys.append(match.group(1))
    return keys


def block_value(frontmatter: str, key: str) -> str:
    lines = frontmatter.splitlines()
    for index, line in enumerate(lines):
        match = re.match(rf"^{re.escape(key)}:\s*(.*)$", line)
        if not match:
            continue
        tail = match.group(1).strip()
        if tail and tail not in {">", ">-", "|", "|-"}:
            return tail.strip('"\'')
        values: list[str] = []
        for following in lines[index + 1 :]:
            if following and not following[0].isspace():
                break
            if following.strip():
                values.append(following.strip())
        return " ".join(values)
    return ""


def metadata_values(frontmatter: str) -> dict[str, str]:
    lines = frontmatter.splitlines()
    start = next((i for i, line in enumerate(lines) if line == "metadata:"), None)
    if start is None:
        return {}

    values: dict[str, str] = {}
    for line in lines[start + 1 :]:
        if line and not line[0].isspace():
            break
        match = re.match(r"^\s{2}([A-Za-z0-9_-]+):\s*(.+?)\s*$", line)
        if not match:
            if line.strip():
                fail("metadata values must be a flat string mapping")
            continue
        values[match.group(1)] = match.group(2).strip('"\'')
    return values


def validate_skill() -> None:
    text = SKILL.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)

    keys = top_level_keys(frontmatter)
    unexpected = sorted(set(keys) - ALLOWED_FRONTMATTER)
    if unexpected:
        fail(f"unsupported Agent Skills frontmatter fields: {', '.join(unexpected)}")

    for required in ("name", "description"):
        if required not in keys:
            fail(f"missing required frontmatter field: {required}")

    if block_value(frontmatter, "name") != "ultra-web-design":
        fail("frontmatter name must be ultra-web-design")

    description = block_value(frontmatter, "description")
    if not description or len(description) > 1024:
        fail(f"description must be 1-1024 characters; found {len(description)}")

    compatibility = block_value(frontmatter, "compatibility")
    if compatibility and len(compatibility) > 500:
        fail(f"compatibility exceeds 500 characters; found {len(compatibility)}")

    metadata = metadata_values(frontmatter)
    for key, expected in REQUIRED_METADATA.items():
        if metadata.get(key) != expected:
            fail(f"metadata must contain {key}: {expected}")

    if not body.strip():
        fail("SKILL.md body is empty")

    line_count = len(text.splitlines())
    if line_count > 500:
        fail(f"runtime SKILL.md exceeds 500-line progressive-disclosure target: {line_count}")

    for number in range(10):
        pattern = rf"modules/{number:02d}-[a-z0-9-]+\.md"
        if not re.search(pattern, body):
            fail(f"runtime router does not reference module {number:02d}")

    if "Numeric jury scores" not in body or "advisory heuristics" not in body:
        fail("runtime must classify uncalibrated numeric jury scores as advisory")


def validate_manifest() -> None:
    expected = expected_manifest()
    actual = MANIFEST.read_text(encoding="utf-8")
    if actual != expected:
        fail("MANIFEST.md is stale; run: python scripts/build_manifest.py")

    if "# Ultra Web Design Manifest" not in actual:
        fail("manifest title is missing")

    for number in range(44):
        if not re.search(rf"(?m)^## {number}\.\s", actual):
            fail(f"manifest is missing numbered section {number}")

    notice = NOTICE.read_text(encoding="utf-8")
    for source in REQUIRED_SOURCES:
        if source not in notice or source not in actual:
            fail(f"missing source provenance: {source}")

    sha_count = len(re.findall(r"`[0-9a-f]{40}`", notice))
    if sha_count < len(REQUIRED_SOURCES):
        fail("NOTICE.md must retain a 40-character pinned SHA for every source")


def validate_templates() -> None:
    for filename, expected in extracted_templates().items():
        path = TEMPLATES / filename
        if not path.is_file():
            fail(f"missing generated template: {path.relative_to(ROOT)}")
        actual = normalize(path.read_text(encoding="utf-8"))
        if actual != expected:
            fail(f"stale generated template: {path.relative_to(ROOT)}")


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def validate_evals() -> None:
    payload = load_json(EVALS)
    if not isinstance(payload, dict) or payload.get("skill_name") != "ultra-web-design":
        fail("evals.json must identify skill_name ultra-web-design")

    evals = payload.get("evals")
    if not isinstance(evals, list) or len(evals) < 6:
        fail("evals.json must contain at least six realistic output evals")

    ids: set[object] = set()
    task_types: set[str] = set()
    for case in evals:
        if not isinstance(case, dict):
            fail("every eval case must be an object")
        case_id = case.get("id")
        if case_id in ids:
            fail(f"duplicate eval id: {case_id}")
        ids.add(case_id)
        for key in ("prompt", "expected_output", "task_type"):
            if not isinstance(case.get(key), str) or not case[key].strip():
                fail(f"eval {case_id} is missing {key}")
        task_types.add(case["task_type"])
        assertions = case.get("assertions")
        if not isinstance(assertions, list) or len(assertions) < 3:
            fail(f"eval {case_id} needs at least three assertions")
        if any(not isinstance(item, str) or not item.strip() for item in assertions):
            fail(f"eval {case_id} contains an invalid assertion")

    required_types = {"tiny-fix", "route-extension", "preserve-redesign", "greenfield", "editorial", "audit-only"}
    if not required_types.issubset(task_types):
        fail(f"eval suite is missing task types: {sorted(required_types - task_types)}")

    triggers = load_json(TRIGGERS)
    if not isinstance(triggers, list) or len(triggers) < 20:
        fail("trigger-queries.json must contain at least 20 realistic queries")

    positives = 0
    negatives = 0
    for index, case in enumerate(triggers, start=1):
        if not isinstance(case, dict) or not isinstance(case.get("query"), str):
            fail(f"trigger query {index} is invalid")
        if case.get("should_trigger") is True:
            positives += 1
        elif case.get("should_trigger") is False:
            negatives += 1
        else:
            fail(f"trigger query {index} needs a boolean should_trigger")
    if positives < 8 or negatives < 8:
        fail("trigger suite needs at least eight positive and eight negative cases")


def validate_webp(path: Path) -> None:
    data = path.read_bytes()
    if len(data) < 12 or data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        fail(f"invalid WebP fixture: {path.relative_to(ROOT)}")
    if len(data) < 3_000:
        fail(f"visual fixture is unexpectedly small: {path.relative_to(ROOT)}")


def validate_examples() -> None:
    evidence = ROOT / "examples" / "evidence.webp"
    if not evidence.is_file() or evidence.stat().st_size == 0:
        fail(f"missing visual evidence: {evidence.relative_to(ROOT)}")
    validate_webp(evidence)

    for name in EXAMPLE_DIRS:
        root = ROOT / "examples" / name
        html_path = root / "index.html"
        if not html_path.is_file() or html_path.stat().st_size == 0:
            fail(f"missing example evidence: {html_path.relative_to(ROOT)}")

        html = html_path.read_text(encoding="utf-8")
        lower = html.lower()
        for required in (
            "<!doctype html>",
            '<html lang="en">',
            'name="viewport"',
            "<title>",
            "<main",
            "<h1",
            "illustrative concept",
        ):
            if required not in lower:
                fail(f"{html_path.relative_to(ROOT)} is missing {required}")
        if "lorem ipsum" in lower or 'href="#"' in lower:
            fail(f"{html_path.relative_to(ROOT)} contains filler or a fake empty link")

        ids = set(re.findall(r'\bid="([^"]+)"', html))
        for target in re.findall(r'href="#([^"]+)"', html):
            if target not in ids:
                fail(f"{html_path.relative_to(ROOT)} links to missing anchor #{target}")


def validate_repository_contract() -> None:
    required = (
        SKILL,
        MANIFEST,
        MANIFEST_HEADER,
        MODULES,
        TEMPLATES,
        EVALS,
        TRIGGERS,
        README,
        CHANGELOG,
    )
    for path in required:
        if not path.exists():
            fail(f"missing required path: {path.relative_to(ROOT)}")

    deprecated = (
        SKILL_DIR / "SKILL.header.md",
        ROOT / "scripts" / "build_skill.py",
    )
    for path in deprecated:
        if path.exists():
            fail(f"deprecated path must be removed: {path.relative_to(ROOT)}")

    readme = README.read_text(encoding="utf-8")
    changelog = CHANGELOG.read_text(encoding="utf-8")
    for text, label in ((readme, "README.md"), (changelog, "CHANGELOG.md")):
        if "2.0.0" not in text:
            fail(f"{label} must document version 2.0.0")


def main() -> None:
    validate_repository_contract()
    validate_skill()
    validate_manifest()
    validate_templates()
    validate_evals()
    validate_examples()
    print(
        "OK: ultra-web-design 2.0.0 — compliant lean runtime, synchronized "
        "manifest/templates, 6+ output evals, 20+ trigger evals, and 3 visual fixtures"
    )


if __name__ == "__main__":
    main()
