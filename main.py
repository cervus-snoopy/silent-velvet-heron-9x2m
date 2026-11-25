"""Describe Your Ex in One Word -- make.fun entry.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt.
Gate: UTF-8 text, 1-111 characters, a single word, no trailing newline.
"""
import os
import sys

WORD = "Extra"


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    if len(WORD) < 1 or len(WORD) > 111:
        print(f"gate fail: word length {len(WORD)} outside 1-111", file=sys.stderr)
        return 1
    if len(WORD.split()) != 1:
        print("gate fail: entry must be exactly one word", file=sys.stderr)
        return 1
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        data = f.read()
    if data != WORD.encode("utf-8"):
        print("round-trip fail: written bytes differ", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
