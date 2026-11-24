"""One Word From Your Ex: the word my ex would use to describe me.

The entry is exactly one word, "Ghoster" (7 characters, inside the
1-24 character gate). The program writes it to $MAKEFUN_OUTPUT_DIR/entry.txt
with no trailing newline and asserts the gate before writing.
"""

import os


WORD = "Ghoster"


def main() -> None:
    word = WORD
    assert 1 <= len(word) <= 24, "word must be 1-24 characters"
    assert word.strip() == word and len(word.split()) == 1, "exactly one word"
    assert word.strip(), "word must not be only whitespace"
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
