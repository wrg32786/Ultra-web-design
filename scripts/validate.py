#!/usr/bin/env python3
"""Validate runtime, corpus, evals, examples, and public discovery packaging."""

from __future__ import annotations

import json
import re
import struct
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

from build_manifest import expected_manifest
from build_site import DEFAULT_SITE_URL, build as build_discovery_site
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
CITATION = ROOT / "CITATION.cff"
CODEMETA = ROOT / "codemeta.json"
LLMS = ROOT / "llms.txt"
PUBLICATION = ROOT / "PUBLICATION.md"
REPO_METADATA = ROOT / ".github" / "repository-metadata.yml"
SECURITY = ROOT / ".github" / "SECURITY.md"
PAGES_WORKFLOW = ROOT / ".github" / "workflows" / "pages.yml"
SITE = ROOT / "site"

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
EXPECTED_TOPICS = {
    "web-design",
    "website-design",
    "webdesign",
    "ai-web-design",
    "agent-skills",
    "ai-agent",
    "claude-code",
    "codex",
    "cursor",
    "design-system",
    "landing-page",
    "frontend",
    "responsive-design",
    "accessibility",
    "ui-ux",
    "website-builder",
    "seo",
    "web-performance",
    "gsap",
    "open-source",
}
REQUIRED_CRAWLERS = {
    "OAI-SearchBot",
    "ChatGPT-User",
    "PerplexityBot",
    "ClaudeBot",
    "Claude-SearchBot",
    "Claude-User",
    "Googlebot",
    "Bingbot",
}


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


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


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
        fail(f"runtime SKILL.md exceeds 500-line target: {line_count}")
    for number in range(10):
        if not re.search(rf"modules/{number:02d}-[a-z0-9-]+\.md", body):
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
    if len(re.findall(r"`[0-9a-f]{40}`", notice)) < len(REQUIRED_SOURCES):
        fail("NOTICE.md must retain a pinned SHA for every source")


def validate_templates() -> None:
    for filename, expected in extracted_templates().items():
        path = TEMPLATES / filename
        if not path.is_file():
            fail(f"missing generated template: {path.relative_to(ROOT)}")
        if normalize(path.read_text(encoding="utf-8")) != expected:
            fail(f"stale generated template: {path.relative_to(ROOT)}")


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
    positives = sum(case.get("should_trigger") is True for case in triggers if isinstance(case, dict))
    negatives = sum(case.get("should_trigger") is False for case in triggers if isinstance(case, dict))
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
        html_path = ROOT / "examples" / name / "index.html"
        if not html_path.is_file() or html_path.stat().st_size == 0:
            fail(f"missing example evidence: {html_path.relative_to(ROOT)}")
        html = html_path.read_text(encoding="utf-8")
        lower = html.lower()
        for required in ("<!doctype html>", '<html lang="en">', 'name="viewport"', "<title>", "<main", "<h1", "illustrative concept"):
            if required not in lower:
                fail(f"{html_path.relative_to(ROOT)} is missing {required}")
        if "lorem ipsum" in lower or 'href="#"' in lower:
            fail(f"{html_path.relative_to(ROOT)} contains filler or a fake empty link")
        ids = set(re.findall(r'\bid="([^"]+)"', html))
        for target in re.findall(r'href="#([^"]+)"', html):
            if target not in ids:
                fail(f"{html_path.relative_to(ROOT)} links to missing anchor #{target}")


def validate_png(path: Path, expected: tuple[int, int]) -> None:
    data = path.read_bytes()
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        fail(f"invalid generated PNG: {path}")
    dimensions = struct.unpack(">II", data[16:24])
    if dimensions != expected:
        fail(f"generated social preview must be {expected[0]}x{expected[1]}; found {dimensions[0]}x{dimensions[1]}")
    if len(data) > 1_000_000:
        fail("generated social preview exceeds 1 MB")


def validate_json_ld(html: str, label: str) -> None:
    blocks = re.findall(r'<script\s+type="application/ld\+json">(.*?)</script>', html, flags=re.DOTALL)
    if not blocks:
        fail(f"{label} has no JSON-LD")
    for block in blocks:
        try:
            json.loads(block)
        except json.JSONDecodeError as exc:
            fail(f"invalid JSON-LD in {label}: {exc}")


def validate_discovery() -> None:
    required = (
        CITATION,
        CODEMETA,
        LLMS,
        PUBLICATION,
        REPO_METADATA,
        SECURITY,
        PAGES_WORKFLOW,
        ROOT / "scripts" / "build_site.py",
        ROOT / "scripts" / "build_social_preview.py",
        SITE / "index.html",
        SITE / "source.html",
        SITE / "assets" / "site.css",
        SITE / "favicon.svg",
        SITE / "manifest.webmanifest",
        SITE / "robots.txt",
        SITE / "sitemap.xml",
    )
    for path in required:
        if not path.is_file() or path.stat().st_size == 0:
            fail(f"missing discovery file: {path.relative_to(ROOT)}")

    readme = README.read_text(encoding="utf-8")
    for phrase in (
        "open-source AI web design Agent Skill",
        "open-source web design repository on GitHub",
        "CITATION.cff",
        "codemeta.json",
        "llms.txt",
        "PUBLICATION.md",
        "examples/evidence.webp",
        "build_social_preview.py",
    ):
        if phrase not in readme:
            fail(f"README.md is missing discovery phrase: {phrase}")

    repo_meta = REPO_METADATA.read_text(encoding="utf-8")
    if "Open-source AI web design Agent Skill" not in repo_meta or "https://wrg32786.github.io/Ultra-web-design/" not in repo_meta:
        fail("repository metadata is missing the canonical description or homepage")
    topics = set(re.findall(r"(?m)^\s{2}- ([a-z0-9-]+)$", repo_meta))
    if topics != EXPECTED_TOPICS:
        fail(f"repository topics drifted: missing={sorted(EXPECTED_TOPICS - topics)}, extra={sorted(topics - EXPECTED_TOPICS)}")

    codemeta = load_json(CODEMETA)
    if not isinstance(codemeta, dict):
        fail("codemeta.json must be an object")
    for key, expected in {
        "@type": "SoftwareSourceCode",
        "name": "Ultra Web Design",
        "codeRepository": "https://github.com/wrg32786/Ultra-web-design",
        "version": "2.0.0",
    }.items():
        if codemeta.get(key) != expected:
            fail(f"codemeta.json must contain {key}: {expected}")

    cff = CITATION.read_text(encoding="utf-8")
    for phrase in ("cff-version: 1.2.0", "title: Ultra Web Design", "family-names: Gwyn", "version: 2.0.0", "license: Apache-2.0"):
        if phrase not in cff:
            fail(f"CITATION.cff is missing {phrase}")

    llms = LLMS.read_text(encoding="utf-8")
    for phrase in ("# Ultra Web Design", "Canonical repository:", "## Primary documents", "## Reliable summary", "## Citation"):
        if phrase not in llms:
            fail(f"llms.txt is missing {phrase}")

    index = (SITE / "index.html").read_text(encoding="utf-8")
    source = (SITE / "source.html").read_text(encoding="utf-8")
    for html, label in ((index, "site/index.html"), (source, "site/source.html")):
        lower = html.lower()
        for required_text in (
            "<!doctype html>",
            'name="description"',
            'name="robots"',
            'rel="canonical"',
            'property="og:title"',
            'property="og:description"',
            'property="og:image"',
            'name="twitter:card"',
            "{{site_url}}",
            "<h1",
        ):
            if required_text not in lower:
                fail(f"{label} is missing {required_text}")
        validate_json_ld(html, label)
    if "SoftwareSourceCode" not in index or "codeRepository" not in index:
        fail("site/index.html must identify the canonical software repository")
    if "What the project does not claim" not in source or "Preferred citation" not in source:
        fail("source profile must include limitations and citation guidance")

    robots = (SITE / "robots.txt").read_text(encoding="utf-8")
    for crawler in REQUIRED_CRAWLERS:
        if f"User-agent: {crawler}" not in robots:
            fail(f"robots.txt is missing {crawler}")
    if "Sitemap: {{SITE_URL}}/sitemap.xml" not in robots:
        fail("robots.txt is missing the canonical sitemap placeholder")

    sitemap_text = (SITE / "sitemap.xml").read_text(encoding="utf-8").replace("{{SITE_URL}}", DEFAULT_SITE_URL)
    try:
        root = ET.fromstring(sitemap_text)
    except ET.ParseError as exc:
        fail(f"invalid sitemap.xml: {exc}")
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = {node.text for node in root.findall("s:url/s:loc", namespace)}
    expected_urls = {
        f"{DEFAULT_SITE_URL}/",
        f"{DEFAULT_SITE_URL}/source.html",
        *(f"{DEFAULT_SITE_URL}/examples/{name}/" for name in EXAMPLE_DIRS),
    }
    if urls != expected_urls:
        fail(f"sitemap URL set drifted: {sorted(urls)}")

    workflow = PAGES_WORKFLOW.read_text(encoding="utf-8")
    for phrase in ("github.event.repository.private == false", "actions/configure-pages@v5", "actions/upload-pages-artifact@v3", "actions/deploy-pages@v4", "python scripts/build_site.py"):
        if phrase not in workflow:
            fail(f"Pages workflow is missing {phrase}")

    with tempfile.TemporaryDirectory() as tmp:
        output = Path(tmp) / "site"
        build_discovery_site(output, DEFAULT_SITE_URL)
        validate_png(output / "assets" / "social-preview.png", (1200, 630))
        for path in (output / "index.html", output / "source.html", output / "robots.txt", output / "sitemap.xml", output / "llms.txt", output / ".nojekyll"):
            if not path.exists():
                fail(f"site builder omitted {path.name}")
        for path in output.rglob("*"):
            if path.is_file() and path.suffix.lower() in {".html", ".txt", ".xml", ".json", ".svg", ".css", ".webmanifest"}:
                if "{{SITE_URL}}" in path.read_text(encoding="utf-8"):
                    fail(f"site builder left an unresolved SITE_URL placeholder in {path.relative_to(output)}")
        for name in EXAMPLE_DIRS:
            html = (output / "examples" / name / "index.html").read_text(encoding="utf-8")
            for phrase in ('rel="canonical"', 'property="og:image"', 'type="application/ld+json"'):
                if phrase not in html:
                    fail(f"built example {name} is missing {phrase}")
            validate_json_ld(html, f"built example {name}")

    publication = PUBLICATION.read_text(encoding="utf-8")
    for phrase in ("Google Search Console", "Bing Webmaster Tools", "OAI-SearchBot", "External corroboration", "web design GitHub"):
        if phrase not in publication:
            fail(f"PUBLICATION.md is missing {phrase}")


def validate_repository_contract() -> None:
    required = (SKILL, MANIFEST, MANIFEST_HEADER, MODULES, TEMPLATES, EVALS, TRIGGERS, README, CHANGELOG)
    for path in required:
        if not path.exists():
            fail(f"missing required path: {path.relative_to(ROOT)}")
    for path in (SKILL_DIR / "SKILL.header.md", ROOT / "scripts" / "build_skill.py"):
        if path.exists():
            fail(f"deprecated path must be removed: {path.relative_to(ROOT)}")

    readme = README.read_text(encoding="utf-8")
    changelog = CHANGELOG.read_text(encoding="utf-8")
    if "2.0.0" not in readme or "2.0.0" not in changelog:
        fail("README and changelog must retain runtime version 2.0.0")
    if "2.0.1" not in changelog:
        fail("CHANGELOG.md must document public-discovery packaging 2.0.1")


def main() -> None:
    validate_repository_contract()
    validate_skill()
    validate_manifest()
    validate_templates()
    validate_evals()
    validate_examples()
    validate_discovery()
    print(
        "OK: ultra-web-design runtime 2.0.0 / repository 2.0.1 — compliant "
        "runtime, synchronized corpus/templates, evals, visual fixtures, and "
        "validated search/citation/Pages packaging"
    )


if __name__ == "__main__":
    main()
