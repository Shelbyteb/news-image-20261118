#!/usr/bin/env python3
"""Compose the front page for Wednesday 18 November 2026.

Renders a 1024x1024 newspaper front page, "THE WORLD IN ONE DAY",
from the four photo panels in assets/ plus the day's verified stories.
Run:  python3 compose.py [output.png]
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")

WIDTH, HEIGHT = 1024, 1024
PAPER = (247, 243, 234)
INK = (17, 17, 17)
MUTED = (92, 84, 72)
RED = (163, 18, 18)
RULE = (17, 17, 17)
BOX_BG = (238, 231, 218)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"

PANELS = {
    "bridge": "media-generation-panel-bridge-0-d811bc47-8f7b-440e-9275-45d2e88498d4.webp",
    "manila": "media-generation-panel-manila-0-290b10a8-72cf-4fa6-b74c-0ad9ad2a18cc.webp",
    "hormuz": "media-generation-panel-hormuz-0-c3fe40f0-9107-47c2-a5cd-1c27433a4075.webp",
    "cyclone": "media-generation-panel-cyclone-0-c651845d-c4bd-4e62-a704-a86bf208ba07.webp",
}


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def wrap(draw, text, fnt, max_w):
    """Split text into lines that fit max_w, keeping words whole."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, text, fnt, x, y, max_w, leading, fill=INK):
    """Draw wrapped text; return the y just below the last line."""
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def cover(page, name, box):
    """Paste a panel into box, centre-cropped to fill it."""
    x, y, w, h = box
    img = Image.open(os.path.join(ASSETS, PANELS[name])).convert("RGB")
    iw, ih = img.size
    scale = max(w / iw, h / ih)
    nw, nh = int(iw * scale + 0.5), int(ih * scale + 0.5)
    img = img.resize((nw, nh), Image.LANCZOS)
    left, top = (nw - w) // 2, (nh - h) // 2
    page.paste(img.crop((left, top, left + w, top + h)), (x, y))


def rule(draw, x, y, w, weight=2):
    draw.rectangle([x, y, x + w, y + weight - 1], fill=RULE)


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "entry.png")
    page = Image.new("RGB", (WIDTH, HEIGHT), PAPER)
    d = ImageDraw.Draw(page)

    serif_b = font("DejaVuSerif-Bold.ttf", 56)
    serif_h = font("DejaVuSerif-Bold.ttf", 37)
    serif_s = font("DejaVuSerif-Bold.ttf", 21)
    sans_b = font("DejaVuSans-Bold.ttf", 17)
    sans = font("DejaVuSans.ttf", 18)
    sans_m = font("DejaVuSans.ttf", 17)
    sans_s = font("DejaVuSans.ttf", 16)
    sans_xs = font("DejaVuSans.ttf", 14)

    mx = 30                      # side margin
    cw = WIDTH - 2 * mx          # content width

    # ---- Masthead -------------------------------------------------------
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=serif_b)
    d.text(((WIDTH - tw) / 2, 14), title, font=serif_b, fill=INK)
    rule(d, mx, 92, cw, 3)
    d.text((mx, 102), "WEDNESDAY 18 NOVEMBER 2026", font=sans_b, fill=RED)
    right = "ONE DAY  ·  ONE PAGE"
    d.text((WIDTH - mx - d.textlength(right, font=sans_b), 102),
           right, font=sans_b, fill=MUTED)
    rule(d, mx, 128, cw, 2)

    # ---- Lead story: Kerch Bridge ---------------------------------------
    cover(page, "bridge", (mx, 140, cw, 300))
    d.text((mx, 450), "UKRAINE  —  LEAD STORY", font=sans_b, fill=RED)
    y = para(d, "Kerch Bridge span falls into the sea",
             serif_h, mx, 474, cw, 44)
    y = para(d, "Ukraine struck for a second straight night. A road span of "
                "about 200 metres collapsed, the rail span was damaged and "
                "traffic was suspended. President Zelenskyy called it an "
                "\u201cunprecedented\u201d seven-stage operation.",
             sans_m, mx, y + 4, cw, 21)
    rule(d, mx, y + 12, cw, 2)
    top = y + 24

    # ---- Three stories side by side -------------------------------------
    gap = 18
    col_w = (cw - 2 * gap) // 3
    stories = [
        ("manila", "MANILA  ·  THE QUAD",
         "Trump: Ukraine peace deal \u201cvery close\u201d",
         "In Manila, Trump met Marcos, then headed for Shenzhen. A "
         "Trump\u2013Xi\u2013Putin trilateral is set for Thursday."),
        ("hormuz", "THE GULF  ·  HORMUZ",
         "Tanker hit again off Oman",
         "A second attack near Khasab left crew unaccounted for \u2014 "
         "the third tanker attack in the Gulf since Sunday."),
        ("cyclone", "INDIA  ·  CYCLONE AKVAN",
         "Cyclone bears down on India",
         "Akvan is intensifying in the Bay of Bengal, bringing heavy "
         "rain to Andhra Pradesh, Odisha and Tamil Nadu. Landfall due "
         "about 20 November; winds 120\u2013130 km/h."),
    ]
    photo_h = 120
    col_bottom = top
    for i, (panel, kicker, head, body) in enumerate(stories):
        x = mx + i * (col_w + gap)
        cover(page, panel, (x, top, col_w, photo_h))
        yy = top + photo_h + 10
        d.text((x, yy), kicker, font=sans_b, fill=RED)
        yy = para(d, head, serif_s, x, yy + 24, col_w, 25)
        yy = para(d, body, sans_s, x, yy + 4, col_w, 19)
        col_bottom = max(col_bottom, yy)

    # ---- Kyiv text box ---------------------------------------------------
    by = col_bottom + 14
    d.rectangle([mx, by, WIDTH - mx, by + 48], fill=BOX_BG)
    d.rectangle([mx, by, mx + 5, by + 48], fill=RED)
    para(d, "KYIV \u2014 River bridges shut. Russian missiles damaged both "
            "bridges across the Dnipro; both are closed to traffic.",
         sans_b, mx + 18, by + 6, cw - 36, 19)

    # ---- Also today footer -----------------------------------------------
    fy = by + 48 + 12
    rule(d, mx, fy, cw, 2)
    d.text((mx, fy + 10), "ALSO TODAY", font=sans_b, fill=RED)
    para(d, "Iran\u2019s third strike on US targets in Bahrain in two "
            "months  ·  Andhra Pradesh\u2019s third cyclone in three weeks",
         sans_xs, mx, fy + 32, cw, 19, fill=MUTED)
    assert fy + 51 <= HEIGHT, "layout overflowed the page"

    page.save(out, "PNG", optimize=True)
    print("wrote", out, page.size, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
