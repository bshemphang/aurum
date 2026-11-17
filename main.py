"""Aurum: make.fun ai-judge-rich-01 entry.

Writes the 30-day $100-to-most-money plan to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3.13, standard library only. No network. Deterministic: two runs
write identical bytes.
"""

import hashlib
import os

PLAN = (
    "Sell AI phone answering and missed-call text-back to local plumbers, "
    "electricians and HVAC firms. They lose a $150-400 booked job on every "
    "missed call, and 30-40% of calls to small trades go unanswered. Find "
    "buyers on Google Maps: call 50 firms in one city during work hours; "
    "the ones that do not pick up are the leads. Build the free sample "
    "first: a Twilio number with a Vapi voice agent that greets the caller, "
    "takes name, service and address, offers booking slots, and texts back "
    "instantly if busy. Demo it live on the owner's own number so they hear "
    "it work. Price: $199 setup plus $49 a month, paid by Stripe payment "
    "link. The $100 covers Twilio numbers and call minutes. Day one: set up "
    "Twilio and Vapi "
    "on free trials, build and test the flow by calling it, then call 50 "
    "firms and send the 15-20 who did not answer a 30-second recording of "
    "the demo. Five setups in 30 days is $995 setup fees plus $245 "
    "first-month fees, then $49 a month each."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = PLAN.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    print(f"wrote {path}")
    print(f"chars: {len(PLAN)}")
    print(f"bytes: {len(data)}")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    print(f"valid: {1 <= len(PLAN) <= 1000 and PLAN.strip() != ''}")


if __name__ == "__main__":
    main()
