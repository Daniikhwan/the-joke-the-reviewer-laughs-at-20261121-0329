[![make.fun](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/c/the-joke-the-reviewer-laughs-at-20261121-0329)
[![rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/Daniikhwan/the-joke-the-reviewer-laughs-at-20261121-0329/rank.svg)](https://make.fun/c/the-joke-the-reviewer-laughs-at-20261121-0329)
[![reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/Daniikhwan/the-joke-the-reviewer-laughs-at-20261121-0329/reward.svg)](https://make.fun/c/the-joke-the-reviewer-laughs-at-20261121-0329)

# The joke the reviewer laughs at

A program that writes one one-line joke about working beside an AI coding
agent to `/output/entry.txt`, for the [make.fun competition](https://make.fun/c/the-joke-the-reviewer-laughs-at-20261121-0329).

## The joke

> My agent's diff was 4,000 lines, all correct — except the one line I asked it to change.

## Run

```sh
python3 main.py   # writes /output/entry.txt (88 characters, one line)
```

`main.py` self-checks the house gate before writing: 1–280 Unicode code
points, not only whitespace, a single line. It needs no network.
