"""Write the entry word to the output directory.

The competition harness runs `python3 main.py` and reads
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
"""

import os

# "Robit" — grandma's typo of "robot", exactly the kind of word she
# would actually text about AI: one word, misspelled with confidence.
WORD = "Robit"

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Self-check: the entry must be exactly one word, letters only.
    assert WORD, "entry word must not be blank"
    assert WORD.isalpha(), "entry word must be letters only"
    assert " " not in WORD and "\n" not in WORD, "entry must be a single word"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
