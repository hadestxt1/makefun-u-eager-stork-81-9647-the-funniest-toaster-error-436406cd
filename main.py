"""The Funniest Toaster Error Message — make.fun entry.

Writes a single deadpan toaster error message (<=120 characters) to
/output/entry.txt. Model-free and fully deterministic: the same fixed
line is written on every run, so replays are byte-identical.
"""

import os

# The line. Deadpan, corporate, quietly dramatic: the bread was not
# merely burnt, it was promoted — and HR has been notified.
MESSAGE = "ERROR E12: Your bread has been promoted to charcoal. HR has been notified."

MAX_CHARS = 120


def main() -> None:
    if not MESSAGE or not MESSAGE.strip():
        raise SystemExit("message must not be blank")
    if len(MESSAGE) > MAX_CHARS:
        raise SystemExit(f"message is {len(MESSAGE)} chars, over the {MAX_CHARS} cap")

    out_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(MESSAGE + "\n")


if __name__ == "__main__":
    main()
