"""Dad Joke Showdown — one dad joke, written by a program.

This program writes a single dad joke to /output/entry.txt for the
make.fun "Dad Joke Showdown" bounty. The joke is a fixed constant:
a flamingo pun whose punchline lands at the very end. The output is
fully deterministic — every run writes exactly the same bytes.
"""

import os

JOKE = "My wife told me to stop impersonating a flamingo. I had to put my foot down."


def main() -> None:
    # Gate: the entry must be 1-200 characters of non-whitespace UTF-8 text.
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise ValueError("joke must be 1-200 non-whitespace characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
