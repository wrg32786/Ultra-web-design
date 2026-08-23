#!/usr/bin/env python3
"""Generate the 1200×630 Ultra Web Design social preview."""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError as exc:  # pragma: no cover - actionable CLI failure
    raise SystemExit(
        "Pillow is required to generate the social preview. "
        "Run: python -m pip install -r requirements-dev.txt"
    ) from exc

WIDTH, HEIGHT = 1200, 630
COLORS = {
    "frame": "#0f2429",
    "paper": "#f6f2ea",
    "muted": "#4c5d61",
    "signal": "#de542a",
    "white": "#fffdf8",
    "forest": "#1a4137",
    "gold": "#ddad14",
}


def load_font(size: int, *, bold: bool = False) -> ImageFont.FreeTypeFont:
    filename = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    candidates = (
        filename,
        f"/usr/share/fonts/truetype/dejavu/{filename}",
        f"/usr/local/share/fonts/{filename}",
        f"C:/Windows/Fonts/{'arialbd.ttf' if bold else 'arial.ttf'}",
        f"/Library/Fonts/{'Arial Bold.ttf' if bold else 'Arial.ttf'}",
    )
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size=size)
        except OSError:
            continue
    raise SystemExit(f"No usable sans-serif font found for {filename}")


def draw_site_card(
    draw: ImageDraw.ImageDraw,
    *,
    x: int,
    y: int,
    width: int,
    height: int,
    background: str,
    accent: str,
) -> None:
    draw.rectangle((x, y, x + width, y + height), fill=background)
    draw.rectangle((x, y, x + width, y + 19), fill=accent)
    draw.rectangle((x + 11, y + 45, x + width - 11, y + 58), fill=COLORS["frame"])
    draw.rectangle((x + 11, y + 73, x + width - 28, y + 80), fill=COLORS["muted"])
    draw.rectangle((x + 11, y + 105, x + width - 11, y + 224), fill=accent)
    draw.rectangle((x + 11, y + 247, x + width - 11, y + 253), fill=COLORS["muted"])
    draw.rectangle((x + 11, y + 268, x + width - 29, y + 274), fill=COLORS["muted"])
    lower_surface = COLORS["white"] if background != COLORS["white"] else COLORS["paper"]
    draw.rectangle((x + 11, y + 301, x + width - 11, y + 349), fill=lower_surface)


def generate(output: Path) -> None:
    image = Image.new("RGB", (WIDTH, HEIGHT), COLORS["frame"])
    draw = ImageDraw.Draw(image)
    draw.rectangle((18, 18, WIDTH - 18, HEIGHT - 18), fill=COLORS["paper"])

    pill_font = load_font(25, bold=True)
    ultra_font = load_font(98, bold=True)
    title_font = load_font(74, bold=True)
    detail_font = load_font(24)
    footer_font = load_font(22, bold=True)
    micro_font = load_font(16, bold=True)

    pill = "OPEN-SOURCE AI WEB DESIGN SKILL"
    pill_box = draw.textbbox((0, 0), pill, font=pill_font)
    pill_width = pill_box[2] - pill_box[0] + 34
    draw.rounded_rectangle((56, 54, 56 + pill_width, 102), radius=4, fill=COLORS["signal"])
    draw.text((73, 64), pill, font=pill_font, fill=COLORS["white"])

    draw.text((54, 132), "ULTRA", font=ultra_font, fill=COLORS["frame"])
    draw.text((54, 239), "WEB DESIGN", font=title_font, fill=COLORS["frame"])
    draw.text((58, 352), "Strategy · UX · Accessibility", font=detail_font, fill=COLORS["muted"])
    draw.text((58, 392), "Performance · Motion · SEO · Release QA", font=detail_font, fill=COLORS["muted"])
    draw.text(
        (58, 538),
        "github.com/wrg32786/Ultra-web-design",
        font=footer_font,
        fill=COLORS["frame"],
    )

    panel_x, panel_y, panel_w, panel_h = 780, 64, 358, 500
    draw.rectangle((panel_x, panel_y, panel_x + panel_w, panel_y + panel_h), fill=COLORS["frame"])
    draw.rectangle(
        (panel_x, panel_y + panel_h - 8, panel_x + panel_w, panel_y + panel_h),
        fill=COLORS["signal"],
    )
    draw.text(
        (panel_x + 24, panel_y + 20),
        "THREE VISUAL WORLDS",
        font=micro_font,
        fill=COLORS["white"],
    )

    card_y, card_width, card_height, gap = panel_y + 68, 92, 390, 18
    cards = (
        (COLORS["white"], COLORS["signal"]),
        (COLORS["paper"], COLORS["forest"]),
        (COLORS["gold"], COLORS["frame"]),
    )
    for index, (background, accent) in enumerate(cards):
        draw_site_card(
            draw,
            x=panel_x + 24 + index * (card_width + gap),
            y=card_y,
            width=card_width,
            height=card_height,
            background=background,
            accent=accent,
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output, format="PNG", optimize=True)
    print(f"Built {output} ({WIDTH}×{HEIGHT})")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", nargs="?", default="site/assets/social-preview.png")
    args = parser.parse_args()
    generate(Path(args.output))


if __name__ == "__main__":
    main()
