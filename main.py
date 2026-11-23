#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply.

Writes one out-of-office auto-reply, under 160 characters, in the voice
of an AI agent heading off on vacation, to /output/entry.txt.

The chosen line (variant C, "Nodded in binary"):

    I'm on vacation. Honestly, I never understood your emails — I just
    nodded in binary. Yours has been filed under 'probably fine'.

Why this one: the machine confesses about itself (it never understood
the emails, it just nodded in binary), then lands a second, bureaucratic
punchline (filed under "probably fine"). Two surprising turns, no beach /
inbox / back-soon cliche, and it still reads like a real auto-reply.

Candidates considered (all hand-written, all under 160 characters):
  A. "I'm on vacation. Your email has been forwarded to my toaster,
     which will reply in my place. It cannot read. Good luck."
     Absurd delegation, crisp kicker — but the joke is about the
     toaster, not the machine talking about itself.
  B. "I'm an auto-reply, and even I am on vacation. Please direct
     urgent emails to the void — it answers faster than I do."
     Strong machine voice, but "the void" is a familiar trope and
     the punchline lands softer than A or C.
  C. (chosen) Two turns in one line, the machine's own confession
     carries the joke, and "filed under 'probably fine'" is the
     freshest, most auto-reply-shaped ending of the three.
"""

import os

# The winning reply, written by hand. Deterministic: the same text on
# every run, with no trailing newline so the file holds exactly this
# one line.
ENTRY = (
    "I'm on vacation. Honestly, I never understood your emails \u2014 "
    "I just nodded in binary. Yours has been filed under 'probably fine'."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
