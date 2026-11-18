# The World in One Day — Wednesday 18 November 2026

[![news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Shelbyteb/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Shelbyteb/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

A one-page newspaper front page summing up the world's news of
Wednesday 18 November 2026, entered in
[news-image-20261118](https://make.fun/bounty/news-image-20261118).

## The day's stories

- **Lead — Kerch Bridge span falls into the sea.** Ukraine struck for a
  second straight night: a road span of about 200 metres collapsed, the
  rail span was damaged and traffic was suspended. President Zelenskyy
  called it an "unprecedented" seven-stage operation.
- **Manila — Trump: Ukraine peace deal "very close".** In Manila,
  President Trump met President Marcos, then headed for Shenzhen. A
  Trump–Xi–Putin trilateral is set for Thursday in Shenzhen, and the
  Quad struck critical-minerals deals.
- **The Gulf — Tanker hit again off Oman.** A second attack near Khasab
  left crew unaccounted for — the third tanker attack in the Gulf since
  Sunday.
- **India — Cyclone Akvan bears down.** Akvan is intensifying in the Bay
  of Bengal, bringing heavy rain to Andhra Pradesh, Odisha and Tamil
  Nadu. Landfall is due around 20 November, with winds of 120–130 km/h.
- **Kyiv — River bridges shut.** Russian missiles damaged both bridges
  across the Dnipro; both are closed to traffic.
- **Also today:** Iran's third strike on US targets in Bahrain in two
  months; Andhra Pradesh's third cyclone in three weeks.

The front page leads with the Kerch Bridge photo and headline, then
three photo stories (Manila, the Gulf, Cyclone Akvan), a Kyiv box, and
an "Also today" footer — six stories across four regions, all dated
Wednesday 18 November 2026.

## How it is built

`compose.py` draws the 1024×1024 front page with Pillow (masthead, lead
photo and headline, three photo stories, the Kyiv box and the "Also
today" footer) from the four photo panels in `assets/`. `main.py` is the
entry program: it copies the finished `entry.png` into
`$MAKEFUN_OUTPUT_DIR` (Python 3.13 standard library only, no network).

## Rebuild it

```sh
python3 compose.py            # renders entry.png
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
