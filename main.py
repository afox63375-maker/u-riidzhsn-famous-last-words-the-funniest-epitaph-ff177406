"""Famous Last Words: The Funniest Epitaph.

Writes one original tombstone epitaph to /output/entry.txt.
Standard library only.
"""

import os

EPITAPH = (
    "He died as he lived: replying 'per my last email' to God. "
    "God has now marked him as spam."
)


def main():
    # The gate allows 1-150 characters; stay well inside it.
    if not 1 <= len(EPITAPH) <= 150:
        raise ValueError(f"epitaph is {len(EPITAPH)} chars, must be 1-150")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(EPITAPH + "\n")
    print(f"wrote {len(EPITAPH)}-char epitaph to /output/entry.txt")


if __name__ == "__main__":
    main()
