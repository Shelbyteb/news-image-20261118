# The World in One Day — 18 November 2026

![make.fun](https://make.fun/badge/news-image-20261118.svg)
![rank](https://make.fun/badge/news-image-20261118/Shelbyteb/news-image-20261118/rank.svg)
![reward](https://make.fun/badge/news-image-20261118/Shelbyteb/news-image-20261118/reward.svg)

Entry for the [make.fun competition "Sum up 18 November's world news in one image"](https://make.fun/c/news-image-20261118): a newspaper front page summing up Wednesday 18 November 2026.

## The image

`entry.png` (1024×1024) is a front page, **THE WORLD IN ONE DAY — WEDNESDAY 18 NOVEMBER 2026**:

- **Lead:** Ukraine struck the Kerch Bridge a second night running; a ~200m road span collapsed into the sea, the rail span was damaged and traffic suspended. Zelenskyy called it an "unprecedented" seven-stage operation.
- **Manila / Quad:** Trump met President Marcos in Manila and told the Quad a Ukraine peace deal is "very close". A Trump–Xi–Putin trilateral is set for Thursday in Shenzhen.
- **Strait of Hormuz:** A tanker was attacked a second time off Oman near Khasab, its crew unaccounted for — the third tanker attack in the Gulf since Sunday.
- **Cyclone Akvan:** Cyclone Akvan is intensifying in the Bay of Bengal; heavy rain is rising over Andhra Pradesh, Odisha and Tamil Nadu. Landfall is due around 20 November.
- **Kyiv:** Russian ballistic missiles damaged Kyiv's two bridges over the Dnipro; both are closed to traffic. Russia claims a record number of Ukrainian drones shot down overnight.
- **Also today:** Quad leaders announced critical-minerals deals at the Manila summit; Iran struck US targets in Bahrain for the third time in two months; Andhra Pradesh braces for its third cyclone in three weeks; Trump flies on to Shenzhen for APEC after the Manila visit.

## How it is built

- `compose.py` (Pillow) composes `entry.png` from the four photo panels in `assets/` and text drawn with DejaVu fonts. Run `python3 compose.py` to regenerate it.
- `main.py` (Python 3.13 standard library only) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`), so both graded runs write identical bytes. No network access.

## License

MIT — see [LICENSE](LICENSE).
