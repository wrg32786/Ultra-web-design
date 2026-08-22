#!/usr/bin/env python3
"""Generate the 1200x630 social preview using only the Python standard library."""

from __future__ import annotations

import argparse
import struct
import zlib
from pathlib import Path

WIDTH, HEIGHT = 1200, 630
COLORS = {
    "canvas": (243, 239, 230),
    "ink": (16, 37, 42),
    "muted": (86, 102, 106),
    "signal": (223, 90, 47),
    "paper": (255, 253, 248),
    "forest": (23, 63, 54),
    "gold": (217, 169, 41),
}
FONT = {
    "A": ("01110","10001","10001","11111","10001","10001","10001"),
    "B": ("11110","10001","10001","11110","10001","10001","11110"),
    "C": ("01111","10000","10000","10000","10000","10000","01111"),
    "D": ("11110","10001","10001","10001","10001","10001","11110"),
    "E": ("11111","10000","10000","11110","10000","10000","11111"),
    "F": ("11111","10000","10000","11110","10000","10000","10000"),
    "G": ("01111","10000","10000","10111","10001","10001","01111"),
    "H": ("10001","10001","10001","11111","10001","10001","10001"),
    "I": ("11111","00100","00100","00100","00100","00100","11111"),
    "J": ("00111","00010","00010","00010","10010","10010","01100"),
    "K": ("10001","10010","10100","11000","10100","10010","10001"),
    "L": ("10000","10000","10000","10000","10000","10000","11111"),
    "M": ("10001","11011","10101","10101","10001","10001","10001"),
    "N": ("10001","11001","10101","10011","10001","10001","10001"),
    "O": ("01110","10001","10001","10001","10001","10001","01110"),
    "P": ("11110","10001","10001","11110","10000","10000","10000"),
    "Q": ("01110","10001","10001","10001","10101","10010","01101"),
    "R": ("11110","10001","10001","11110","10100","10010","10001"),
    "S": ("01111","10000","10000","01110","00001","00001","11110"),
    "T": ("11111","00100","00100","00100","00100","00100","00100"),
    "U": ("10001","10001","10001","10001","10001","10001","01110"),
    "V": ("10001","10001","10001","10001","10001","01010","00100"),
    "W": ("10001","10001","10001","10101","10101","10101","01010"),
    "X": ("10001","10001","01010","00100","01010","10001","10001"),
    "Y": ("10001","10001","01010","00100","00100","00100","00100"),
    "Z": ("11111","00001","00010","00100","01000","10000","11111"),
    "0": ("01110","10001","10011","10101","11001","10001","01110"),
    "1": ("00100","01100","00100","00100","00100","00100","01110"),
    "2": ("01110","10001","00001","00010","00100","01000","11111"),
    "-": ("00000","00000","00000","11111","00000","00000","00000"),
    ".": ("00000","00000","00000","00000","00000","00110","00110"),
    "/": ("00001","00010","00010","00100","01000","01000","10000"),
    " ": ("00000",) * 7,
}


def rect(pixels: bytearray, x: int, y: int, w: int, h: int, color: tuple[int, int, int]) -> None:
    x0, y0 = max(0, x), max(0, y)
    x1, y1 = min(WIDTH, x + w), min(HEIGHT, y + h)
    row = bytes(color) * max(0, x1 - x0)
    for yy in range(y0, y1):
        i = (yy * WIDTH + x0) * 3
        pixels[i : i + len(row)] = row


def text(pixels: bytearray, value: str, x: int, y: int, scale: int, color: tuple[int, int, int]) -> None:
    cursor = x
    for char in value.upper():
        glyph = FONT.get(char, FONT[" "])
        for gy, row in enumerate(glyph):
            for gx, bit in enumerate(row):
                if bit == "1":
                    rect(pixels, cursor + gx * scale, y + gy * scale, scale, scale, color)
        cursor += 6 * scale


def png_bytes(pixels: bytearray) -> bytes:
    raw = bytearray()
    stride = WIDTH * 3
    for y in range(HEIGHT):
        raw.append(0)
        raw.extend(pixels[y * stride : (y + 1) * stride])

    def chunk(name: bytes, payload: bytes) -> bytes:
        return struct.pack(">I", len(payload)) + name + payload + struct.pack(">I", zlib.crc32(name + payload) & 0xFFFFFFFF)

    return (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", WIDTH, HEIGHT, 8, 2, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(bytes(raw), 9))
        + chunk(b"IEND", b"")
    )


def generate(output: Path) -> None:
    pixels = bytearray(COLORS["canvas"] * (WIDTH * HEIGHT))
    rect(pixels, 64, 54, 386, 44, COLORS["signal"])
    text(pixels, "OPEN SOURCE AGENT SKILL", 82, 65, 4, COLORS["paper"])
    text(pixels, "ULTRA", 64, 132, 14, COLORS["ink"])
    text(pixels, "WEB DESIGN", 64, 250, 10, COLORS["ink"])
    text(pixels, "STRATEGY  ACCESSIBILITY  PERFORMANCE", 64, 382, 4, COLORS["muted"])
    text(pixels, "MOTION  SEO  RELEASE QA", 64, 424, 4, COLORS["muted"])
    text(pixels, "GITHUB.COM/WRG32786/ULTRA-WEB-DESIGN", 64, 558, 3, COLORS["ink"])

    rect(pixels, 650, 44, 486, 542, COLORS["ink"])
    panels = (
        (674, 78, 134, 454, COLORS["paper"], COLORS["signal"]),
        (826, 78, 134, 454, COLORS["canvas"], COLORS["forest"]),
        (978, 78, 134, 454, COLORS["gold"], COLORS["ink"]),
    )
    for x, y, w, h, background, accent in panels:
        rect(pixels, x, y, w, h, background)
        rect(pixels, x, y, w, 22, accent)
        rect(pixels, x + 12, y + 44, w - 24, 18, COLORS["ink"])
        rect(pixels, x + 12, y + 74, int((w - 24) * .72), 9, COLORS["muted"])
        rect(pixels, x + 12, y + 102, w - 24, 138, accent)
        rect(pixels, x + 12, y + 258, w - 24, 8, COLORS["muted"])
        rect(pixels, x + 12, y + 282, int((w - 24) * .84), 8, COLORS["muted"])
        rect(pixels, x + 12, y + 318, w - 24, 58, COLORS["paper"] if background != COLORS["paper"] else COLORS["canvas"])
        rect(pixels, x + 12, y + 396, int((w - 24) * .56), 28, accent)
    rect(pixels, 650, 590, 486, 8, COLORS["signal"])

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(png_bytes(pixels))
    print(f"Built {output} ({WIDTH}x{HEIGHT})")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", nargs="?", default="site/assets/social-preview.png")
    args = parser.parse_args()
    generate(Path(args.output))


if __name__ == "__main__":
    main()
