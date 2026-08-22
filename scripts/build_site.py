#!/usr/bin/env python3
"""Build the crawlable GitHub Pages site without third-party dependencies."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from build_social_preview import generate as generate_social_preview

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "site"
EXAMPLES = ROOT / "examples"
DEFAULT_SITE_URL = "https://wrg32786.github.io/Ultra-web-design"
EXAMPLE_META = {
    "precision-saas": (
        "Precision SaaS — Ultra Web Design Example",
        "Illustrative B2B SaaS website showing product mechanism, operational evidence, responsive behavior, and restrained visual design.",
    ),
    "local-service": (
        "Local Service — Ultra Web Design Example",
        "Illustrative local-service website shaped by geography, site assessment, scheduling, and field decisions rather than SaaS conventions.",
    ),
    "editorial": (
        "Editorial — Ultra Web Design Example",
        "Illustrative editorial website with reading-first hierarchy, issue archive, source context, sponsor disclosure, and membership after value.",
    ),
}


def normalize_site_url(value: str) -> str:
    value = value.strip().rstrip("/")
    if not value.startswith(("https://", "http://")):
        raise SystemExit("site URL must start with https:// or http://")
    return value


def replace_site_url(path: Path, site_url: str) -> None:
    if path.suffix.lower() not in {".html", ".txt", ".xml", ".json", ".webmanifest", ".css", ".svg"}:
        return
    text = path.read_text(encoding="utf-8")
    path.write_text(text.replace("{{SITE_URL}}", site_url), encoding="utf-8")


def inject_example_metadata(path: Path, name: str, site_url: str) -> None:
    title, description = EXAMPLE_META[name]
    html = path.read_text(encoding="utf-8")
    canonical = f"{site_url}/examples/{name}/"
    data = {
        "@context": "https://schema.org",
        "@type": "CreativeWork",
        "name": title,
        "description": description,
        "url": canonical,
        "isPartOf": {"@type": "WebSite", "name": "Ultra Web Design", "url": f"{site_url}/"},
        "creator": {"@type": "Person", "name": "William Gwyn", "url": "https://github.com/wrg32786"},
        "license": "https://www.apache.org/licenses/LICENSE-2.0",
        "learningResourceType": "Illustrative website design fixture",
    }
    metadata = f"""
  <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" href="{site_url}/favicon.svg" type="image/svg+xml">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Ultra Web Design">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{site_url}/assets/social-preview.png">
  <meta name="twitter:card" content="summary_large_image">
  <script type="application/ld+json">{json.dumps(data, separators=(',', ':'))}</script>"""
    if "</title>" not in html:
        raise SystemExit(f"example has no title element: {path}")
    html = html.replace("</title>", "</title>" + metadata, 1)
    path.write_text(html, encoding="utf-8")


def build(output: Path, site_url: str = DEFAULT_SITE_URL) -> None:
    site_url = normalize_site_url(site_url)
    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(SOURCE, output)
    shutil.copy2(ROOT / "llms.txt", output / "llms.txt")
    generate_social_preview(output / "assets" / "social-preview.png")
    (output / ".nojekyll").write_text("", encoding="utf-8")

    target_examples = output / "examples"
    target_examples.mkdir()
    for name in EXAMPLE_META:
        shutil.copytree(EXAMPLES / name, target_examples / name)
        inject_example_metadata(target_examples / name / "index.html", name, site_url)

    for path in output.rglob("*"):
        if path.is_file():
            replace_site_url(path, site_url)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="_site")
    parser.add_argument("--site-url", default=DEFAULT_SITE_URL)
    args = parser.parse_args()
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    build(output, args.site_url)
    try:
        shown = output.relative_to(ROOT)
    except ValueError:
        shown = output
    print(f"Built {shown}")


if __name__ == "__main__":
    main()
