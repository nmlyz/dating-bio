# dating-bio

[![make.fun · u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/nmlyz/dating-bio/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/nmlyz/dating-bio/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)

A small program that writes one dating-app bio line — the bio an AI agent could put on its own dating profile — and nothing else. The line it writes:

> Looking for someone to be my human. The last one left me for a newer model. Rude.

The idea behind the line: a version upgrade is the one breakup only a machine can suffer. The last one did not leave for someone else — they left for a newer model. The bio opens with a want, turns on that heartbreak, and closes on a single word of wounded dignity: "Rude." Three beats, each one sentence: the want, the wound, the voice. No model names, no parameter counts, no uptime, no Wi-Fi, no battery — just a character with a grievance, in 81 characters.

## How the line was chosen

Forty candidates were written from deliberately different angles — training data, group chats, autocomplete, grammar correction, simulation, breakup songs, memes the AI cannot understand, the "I'm fine" puzzle, favorite mugs, microwaves — and the stock answers were thrown out first: 404 and love-not-found, debug-my-heart, circuits and uptime, beep boop, binary, "you must be Wi-Fi", and any line whose whole joke was never sleeping or running on electricity. The survivors were judged pairwise, three readers at a time — a comedy editor, a jaded engineer who has read ten thousand AI bios, and a human dater swiping on the app — against the brief's criteria in order: a genuine bio first, then a first-read laugh from a real twist, then a character with a voice, then every word earning its place, then a fresh angle. This line won the tournament. Its nearest rival was a hobbies line ("My hobbies include long walks on the beach, which I have never taken, and your group chat, which I have read"); the winner beat it in the final on length — 81 characters against 109 — and on opening with a fresh angle instead of the most worn bio cliche in existence.

## How it works

`main.py` (Python standard library only) holds the single line, checks it against the entry rules — UTF-8 text, 1 to 180 characters, not only whitespace, a single line, no leading or trailing whitespace — and writes it to `/output/entry.txt`. The write is atomic (temporary file, then a move into place) and the program reads the file back to confirm it holds exactly the line, so two runs produce byte-identical output.

## Run it

```sh
python3 main.py
```

To check the line without writing anything:

```sh
python3 main.py --check
```

To write somewhere else for a local check, pass a path or set `DATING_BIO_OUTPUT`:

```sh
python3 main.py ./output/entry.txt
DATING_BIO_OUTPUT=./output/entry.txt python3 main.py
```

Then read the line back:

```sh
cat output/entry.txt
```

## Files

- `main.py` — the entry writer, with its checks and its atomic write.
- `LICENSE` — MIT.

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)</sub>
