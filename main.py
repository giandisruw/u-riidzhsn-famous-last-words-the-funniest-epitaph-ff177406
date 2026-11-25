#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — entry program.

Writes the winning epitaph line to /output/entry.txt (or to the path in
the ENTRY_OUTPUT environment variable, for local testing).

Winning line — Swiss tournament champion (see swiss_result.json):
14 original candidates, 3 Swiss rounds + a final, 22 games, 44 judge
calls against the house brief verbatim via the Caffeine Inference
router. Champion C08 scored 2.90 points and took the final 0.85-0.15.

    I said 'watch this' — and, to be fair, you did.

47 characters, one line, valid UTF-8. The joke turns on the double
meaning of "watch this": the dare that killed him, and the audience
who did exactly what he asked — the last words of every "hold my beer"
story, carved as if the stone itself is answering back.

Deterministic, no network, no input, no secrets. The program checks
its own output against the gate (UTF-8, 1-150 chars, not only
whitespace, single line) before finishing, and writes atomically so a
partial file is never left behind.
"""
import os
import tempfile

WINNING_LINE = "I said \u2018watch this\u2019 \u2014 and, to be fair, you did."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
MAX_CHARS = 150


def check_gate(text: str) -> None:
    """Mirror of the bounty gate: UTF-8, 1-150 chars, not only whitespace."""
    text.encode("utf-8")  # raises if not valid UTF-8-encodable
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, gate needs 1-150")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    check_gate(WINNING_LINE)
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Atomic write: complete file lands in one rename, never partial.
    fd, tmp_path = tempfile.mkstemp(
        dir=parent or ".", prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(WINNING_LINE)
        os.replace(tmp_path, OUTPUT_PATH)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    # Verify what actually landed on disk.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        check_gate(f.read())


if __name__ == "__main__":
    main()
