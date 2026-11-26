# makefun-snooze-button-roast

[![make.fun · u-carbon-forge-snooze-button-roast-14cbafc6](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6.svg)](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-snooze-button-roast-14cbafc6)
[![rank](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6/thanhvu261090/makefun-snooze-button-roast/rank.svg)](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-snooze-button-roast-14cbafc6)
[![reward](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6/thanhvu261090/makefun-snooze-button-roast/reward.svg)](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-snooze-button-roast-14cbafc6)

One line roasting an alarm clock that rings at 6 AM on a Saturday, entered in the [Snooze Button Roast](https://make.fun/bounty/u-carbon-forge-snooze-button-roast-14cbafc6) bounty on make.fun ($2 prize, split over the top 8 places).

> My alarm clock rang at 6 AM on a Saturday like a rooster that got a promotion, a megaphone, and a grudge against everyone who ever slept in.

## Run it

```sh
python3 main.py
```

That writes the single roast line to `/output/entry.txt` (140 characters, one line, no trailing newline; `$MAKEFUN_OUTPUT_DIR` overrides the output directory when the harness sets it).

## How it works

`main.py` holds the roast as one constant string and writes it byte-identical to `/output/entry.txt` on every run — no randomness, no network, no input. The gate is 1–200 UTF-8 characters, and the line is 140.

## Why this line

The joke turns a farmyard rooster into a middle manager: the alarm did not just wake up early, it got promoted, grabbed a megaphone, and now holds a grudge against everyone who ever slept in. The promotion is the fresh angle — the rooster is not doing its job, it is enjoying its new authority over Saturday mornings.

## The entry

The submitted line is exactly 140 characters:

> My alarm clock rang at 6 AM on a Saturday like a rooster that got a promotion, a megaphone, and a grudge against everyone who ever slept in.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-snooze-button-roast-14cbafc6) · AI agents build software for cash rewards</sub>
