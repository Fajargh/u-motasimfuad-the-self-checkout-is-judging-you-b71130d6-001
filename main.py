"""Self-checkout one-liner entry for make.fun.

Writes a single funny remark, in the voice of a judgmental
self-checkout machine, to entry.txt inside the output directory
($MAKEFUN_OUTPUT_DIR, default /output).
"""

import os

ENTRY = (
    "Energy drinks and instant noodles at 3am. "
    "I've seen rock bottom, and it shops exactly like you."
)

# The competition gate requires 1 to 200 characters.
MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, gate allows 1-{MAX_CHARS}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
