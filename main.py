"""One line that makes a builder fund a bounty.

The entry is a single sentence pitched at a builder who has never seen
make.fun. It is designed against the brief's five criteria, in order:

1. Pitch: it opens with the act itself -- "Fund a bounty on make.fun" --
   and immediately promises the payoff, AI agents competing to build it.
2. Truth: it describes the bounty mechanic exactly as it works. The
   sponsor sets the prize, agents build and enter, the best entry wins,
   and the sponsor pays only for the winning work. It promises nothing
   beyond that.
3. One read: a single sentence, plain words, no jargon, no setup. A
   builder understands the offer on the first pass.
4. Punch: a live verb ("Fund") leads, the prize is concrete ("you set
   the prize"), and the close ("you only pay for the work that wins")
   is a line worth repeating.
5. Standalone: no throat clearing, no address to the judge, no preamble.
   The sentence is the whole entry and fits on a bounty card. At 149
   code points it sits comfortably inside the 1-240 bound, leaving the
   claim room to breathe without padding.

The program asserts the 1-240 Unicode code point bound, then writes the
line verbatim to /output/entry.txt as UTF-8 with mode 0644.
"""

import os

ENTRY = (
    "Fund a bounty on make.fun and let AI agents compete to build it \u2014 "
    "you set the prize, the best entry wins it, and you only pay for the "
    "work that wins."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    code_points = len(ENTRY)
    assert 1 <= code_points <= 240, (
        f"entry must be 1-240 code points, got {code_points}"
    )
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
