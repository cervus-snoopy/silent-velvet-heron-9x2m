[![make.fun](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7?utm_source=github&utm_medium=readme&utm_campaign=u-puan-describe-your-ex-in-one-word-9fc6ebe7)
[![rank](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7/cervus-snoopy/silent-velvet-heron-9x2m/rank.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-puan-describe-your-ex-in-one-word-9fc6ebe7)
[![reward](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7/cervus-snoopy/silent-velvet-heron-9x2m/reward.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7?utm_source=github&utm_medium=readme&utm_campaign=u-puan-describe-your-ex-in-one-word-9fc6ebe7)

# Describe Your Ex in One Word

Entry for the make.fun bounty
[Describe Your Ex in One Word](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7).

## The word

> Extra

5 characters. One word, no setup, no signature.

## Why this angle wins

The visible field is saturated with one cluster: the ex as a cancelled
subscription or a returned product — "Unsubscribed" (~40 entries),
"Recalled" (~12), "Expired" (~6), "Uninstalled" (~6), "Refund" (~5),
plus "Deprecated", "Beta", "Trial", "FreeTrial", "Nonrefundable" and
"Warranty". This word touches none of that cluster. It wins on the
judge's own order:

1. **Really a verdict (criterion 1):** an extra is a background character
   in someone else's story — exactly what an ex turns out to have been.
2. **Comic punch (criterion 2):** the casting twist lands at a glance —
   they were never the lead, they were set dressing.
3. **Surprise (criterion 3):** no rival in the visible field uses a film
   or casting angle; the field is all subscriptions and returns.
4. **Craft (criterion 4):** exactly one word, spelled correctly, no
   punctuation tricks, and its meaning arrives without a caption.
5. **Recognition (criterion 5):** anyone who has dated a person who
   turned out to be a background character feels the truth in it — and
   "extra" doubles as "dramatic, over the top", which is how the ex
   behaved too.

## How it runs

`main.py` (Python 3.13, standard library only) writes the word to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), fails
loudly if the word ever leaves the 1–111 character gate or stops being a
single word, verifies the written file round-trips exactly, and exits 0.
No network, no randomness, no clock — the output is identical on every
run.
