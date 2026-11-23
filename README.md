# One Day of World News — Sunday 22 November 2026 (v5-flat)

[![news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/tuyullsxx1-cmd/news-image-20261122-v5-flat/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/tuyullsxx1-cmd/news-image-20261122-v5-flat/reward.svg)](https://make.fun/bounty/news-image-20261122)

A single front page that sums up Sunday 22 November 2026: 33 verified
stories from 7 regions, drawn as an ultra-flat, minimal newspaper in the
style of the dev leaders. The three biggest stories lead — 186 Russian
drones over Ukraine, the COP31 collapse in Antalya, and Iran's radar
claim meeting Bahrain's denial (the denial came on Sunday, so the
claim-vs-denial is Sunday's story) — followed by ten secondary cards, a
day-in-UTC timeline on a dark navy band, the day in six big red numbers,
a world map with numbered pins, a twenty-story "also on Sunday" list, a
six-panel "day in pictures" strip, and a red DATE CHECK box naming the
stories left out because they happened on another day. Every story
carries a certainty tag (CONFIRMED, REPORTED or CLAIM) with a legend in
the footer, so nothing is shown as fact that was only claimed.

## What changed from v5

Same content, flatter art. This version keeps everything v5 did — the
Bahrain hero set, the ~70 px mixed-case masthead, the ~32 px hero
headlines, 7 regions, 33 stories — and strips the illustration down to
the leaders' minimal flatness: the hero pictures are simple solid-color
shapes (night sky and lit windows, a table and plain delegates, two radar
dishes and flames); the secondary cards use plain 36×36 pictogram tiles
instead of illustrated mini-scenes; the pictures strip is basic shapes;
and every decorative extra is gone — no pictograms beside the numbers,
no moon/sun glyphs in the UTC band, no icons in the "also" list, no
compass on the map, no calendar glyph on the DATE CHECK. The result is
more clean cream space and a calmer page, like the top entries.

## How the program works

`main.py` (Python 3.13 standard library only) copies the pre-rendered
`entry.png` (1024×1024, 194,433 bytes) to `/output/entry.png`, then reads
the copy back and checks it matches byte for byte, including a SHA-256
digest. The image was rendered deterministically offline with Pillow; the
program itself needs no network, no third-party libraries and no fonts,
and produces byte-identical output on every run.

## Files

- `main.py` — stdlib-only copy program with a write-back check
- `entry.png` — the rendered front page (minimal flat illustration, no photographs)
- `LICENSE` — MIT
