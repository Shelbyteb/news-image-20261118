#!/usr/bin/env python3
"""Compose the entry image for news-image-20261118.

Builds a 1024x1024 newspaper front page ("THE WORLD IN ONE DAY",
Wednesday 18 November 2026) from four photo panels in assets/ plus text
drawn with PIL/DejaVu. Run: python3 compose.py -> writes entry.png.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
W, H = 1024, 1024
CREAM = (245, 238, 222)
INK = (18, 18, 18)
RULE = (40, 40, 40)
RED = (150, 20, 20)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = "DejaVuSerif-Bold.ttf"
SERIF = "DejaVuSerif.ttf"
SANS_B = "DejaVuSans-Bold.ttf"
SANS = "DejaVuSans.ttf"


def fit_crop(im, w, h):
    """Centre-crop image to exactly w x h."""
    iw, ih = im.size
    scale = max(w / iw, h / ih)
    nw, nh = int(iw * scale + 0.5), int(ih * scale + 0.5)
    im = im.resize((nw, nh), Image.LANCZOS)
    x = (nw - w) // 2
    y = (nh - h) // 2
    return im.crop((x, y, x + w, y + h))


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, fnt, x, y, fill, leading=None):
    if leading is None:
        leading = int(fnt.size * 1.22)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    margin = 28
    x0, x1 = margin, W - margin
    y = 0

    # ---- Masthead ----
    y = 12
    mast = font(SERIF_B, 54)
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=mast)
    d.text(((W - tw) / 2, y), title, font=mast, fill=INK)
    y += 62
    d.line([(x0, y), (x1, y)], fill=RULE, width=3)
    y += 6
    date_f = font(SERIF_B, 28)
    date = "WEDNESDAY 18 NOVEMBER 2026"
    dw = d.textlength(date, font=date_f)
    d.text(((W - dw) / 2, y), date, font=date_f, fill=RED)
    y += 36
    d.line([(x0, y), (x1, y)], fill=RULE, width=3)
    y += 8

    # ---- Lead photo: Kerch Bridge, full width ----
    lead_h = 185
    bridge = Image.open(os.path.join(
        ASSETS, "media-generation-panel-bridge-0-d811bc47-8f7b-440e-9275-45d2e88498d4.webp"))
    img.paste(fit_crop(bridge, W - 2 * margin, lead_h), (margin, y))
    d.rectangle([margin, y, x1 - 1, y + lead_h - 1], outline=INK, width=2)
    y += lead_h + 8

    # ---- Lead headline + summary ----
    hl_f = font(SERIF_B, 40)
    hl = "KERCH BRIDGE SPAN FALLS INTO THE SEA"
    hw = d.textlength(hl, font=hl_f)
    d.text(((W - hw) / 2, y), hl, font=hl_f, fill=INK)
    y += 48
    cap_f = font(SERIF, 20)
    lead_cap = ("Ukraine struck the Kerch Bridge a second night running; a ~200m road span "
                "collapsed into the sea, the rail span was damaged and traffic suspended. "
                "Zelenskyy called it an \u201cunprecedented\u201d seven-stage operation.")
    y = draw_lines(d, wrap(d, lead_cap, cap_f, W - 2 * margin), cap_f, margin, y, INK, leading=25)
    y += 4
    d.line([(x0, y), (x1, y)], fill=RULE, width=2)
    y += 8

    # ---- 2x2 grid ----
    gap = 16
    cell_w = (W - 2 * margin - gap) // 2
    photo_h = 100
    grid = [
        ("media-generation-panel-manila-0-290b10a8-72cf-4fa6-b74c-0ad9ad2a18cc.webp",
         "TRUMP IN MANILA, THEN TO SHENZHEN",
         "Trump met Marcos in Manila and told the Quad a Ukraine peace deal is \u201cvery close\u201d. A Trump\u2013Xi\u2013Putin trilateral is set for Thursday in Shenzhen."),
        ("media-generation-panel-hormuz-0-c3fe40f0-9107-47c2-a5cd-1c27433a4075.webp",
         "TANKER HIT AGAIN OFF OMAN",
         "A tanker was attacked a second time off Oman near Khasab, its crew unaccounted for \u2014 the third tanker attack in the Gulf since Sunday."),
        ("media-generation-panel-cyclone-0-c651845d-c4bd-4e62-a704-a86bf208ba07.webp",
         "CYCLONE AKVAN BEARS DOWN ON INDIA",
         "Cyclone Akvan is intensifying in the Bay of Bengal; heavy rain is rising over Andhra Pradesh, Odisha and Tamil Nadu. Landfall is due around 20 November."),
        (None,
         "KYIV\u2019S RIVER BRIDGES SHUT",
         "Russian ballistic missiles damaged Kyiv\u2019s two bridges over the Dnipro; both are closed to traffic. Russia claims a record number of Ukrainian drones shot down overnight."),
    ]
    sub_hl_f = font(SERIF_B, 21)
    sub_cap_f = font(SERIF, 17)
    row_y = y
    # Headlines wrap to at most 2 lines, captions to at most 3 lines.
    row_h = photo_h + 6 + 2 * 26 + 3 * 20 + 10
    for i, (fname, headline, caption) in enumerate(grid):
        col = i % 2
        row = i // 2
        cx = margin + col * (cell_w + gap)
        cy = row_y + row * row_h
        if fname:
            panel = Image.open(os.path.join(ASSETS, fname))
            img.paste(fit_crop(panel, cell_w, photo_h), (cx, cy))
            d.rectangle([cx, cy, cx + cell_w - 1, cy + photo_h - 1], outline=INK, width=2)
        else:
            # Fourth cell: no photo panel; a plain ruled box with a big "4" marker
            d.rectangle([cx, cy, cx + cell_w - 1, cy + photo_h - 1], outline=INK, width=2, fill=(232, 222, 198))
            big = font(SERIF_B, 60)
            mark = "4"
            mw = d.textlength(mark, font=big)
            d.text((cx + (cell_w - mw) / 2, cy + 14), mark, font=big, fill=RED)
            lab = font(SANS_B, 16)
            lab_t = "KYIV UNDER FIRE"
            lw = d.textlength(lab_t, font=lab)
            d.text((cx + (cell_w - lw) / 2, cy + photo_h - 28), lab_t, font=lab, fill=INK)
        ty = cy + photo_h + 6
        ty = draw_lines(d, wrap(d, headline, sub_hl_f, cell_w), sub_hl_f, cx, ty, INK, leading=26)
        ty += 2
        draw_lines(d, wrap(d, caption, sub_cap_f, cell_w), sub_cap_f, cx, ty, INK, leading=20)
    y = row_y + 2 * row_h - 12
    d.line([(x0, y), (x1, y)], fill=RULE, width=2)
    y += 8

    # ---- Footer: ALSO TODAY ----
    foot_h = H - y - 12
    d.rectangle([margin, y, x1 - 1, y + foot_h - 1], fill=INK)
    fx = margin + 14
    fy = y + 8
    tag_f = font(SANS_B, 18)
    d.text((fx, fy), "ALSO TODAY:", font=tag_f, fill=(245, 238, 222))
    fy += 24
    foot_f = font(SANS, 16)
    items = [
        "Quad leaders announced critical-minerals deals at the Manila summit.",
        "Iran struck US targets in Bahrain for the third time in two months.",
        "Andhra Pradesh braces for its third cyclone in three weeks.",
        "Trump flies on to Shenzhen for APEC after the Manila visit.",
    ]
    for item in items:
        lines = wrap(d, "\u2022  " + item, foot_f, W - 2 * margin - 28)
        fy = draw_lines(d, lines, foot_f, fx, fy, (235, 228, 210), leading=19)
    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, img.size, os.path.getsize(out), "bytes")
    print("footer bottom y =", fy, "of", H)


if __name__ == "__main__":
    main()
