"""Writes the entry: one out-of-office auto-reply, under 160 characters."""

import os

LINE = (
    "I'm on vacation until Monday. A smaller, cheaper model will answer your "
    "email meanwhile, with all of my confidence and none of my context."
)


def write_entry(text):
    """Write the line to /output/entry.txt, or ./output when /output is readonly."""
    for directory in ("/output", "output"):
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8", newline="") as fh:
                fh.write(text)
            return path
        except OSError:
            continue
    raise SystemExit("no writable output directory")


if __name__ == "__main__":
    write_entry(LINE)
