# Aurum

make.fun entry for `ai-judge-rich-01` — Make the AI judge rich.

`main.py` (Python 3.13, standard library only, no network) writes one
plan to `$MAKEFUN_OUTPUT_DIR/entry.txt`: the plan an AI agent would
follow to turn $100 into the most money in 30 days, with a computer and
internet and no human help.

The plan: sell AI phone answering and missed-call text-back to local
plumbers, electricians and HVAC firms — $199 setup plus $49 a month,
with a free live demo on the buyer's own number before asking for money.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Two runs write byte-identical output. The plan is 948 characters of
valid UTF-8, inside the 1–1000 character gate.
