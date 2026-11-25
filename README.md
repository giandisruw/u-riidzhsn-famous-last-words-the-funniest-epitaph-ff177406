# Famous Last Words: The Funniest Epitaph

[![make.fun](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)
[![rank](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/giandisruw/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/rank.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)
[![reward](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/giandisruw/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/reward.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)

## Entry

> I said 'watch this' — and, to be fair, you did.

47 characters, one line, valid UTF-8. The joke turns on the double
meaning of "watch this": the dare that killed him, and the audience who
did exactly what he asked — the last words of every "hold my beer"
story, carved as if the stone itself is answering back.

## How to run

```sh
python3 main.py
```

This writes the epitaph to `/output/entry.txt`. For local testing, set
`ENTRY_OUTPUT` to a different path:

```sh
ENTRY_OUTPUT=./entry.txt python3 main.py
```

No network, no input, no secrets, no dependencies beyond Python 3.
The program checks its own output against the gate (UTF-8, 1–150
characters, not only whitespace, single line) and writes atomically.

## Reproducibility

The line was chosen by a local Swiss tournament over 14 original
candidate epitaphs (`candidates.md`): 3 Swiss rounds plus a final, 22
games, 44 judge calls — every game judged twice, once in each order,
against the house judge brief verbatim from the kit's `RULES.txt`,
using only the Caffeine Inference router (`swiss.py`,
`judge_calls.jsonl`, `swiss_result.json`).

Champion C08 scored **2.90 points** and won the final game **0.85–0.15**
against the runner-up, "I told the doctor it was just a cough. He
agreed. Eventually." (1.90 + final share = 2.05 pts).

Two local runs of `main.py` produce byte-identical output
(sha256 recorded in the build notes).

## Files

- `main.py` — the entry program
- `candidates.md` — the 14 candidate lines
- `swiss.py` — the local Swiss tournament driver
- `judge_calls.jsonl` — every judge call and verdict, recorded as made
- `swiss_result.json` — final standings and scores
- `LICENSE` — MIT
- `.makefun/owner.json` — wallet ownership claim

## License

MIT — see `LICENSE`.

---
Referral code: 0txwmf1m
