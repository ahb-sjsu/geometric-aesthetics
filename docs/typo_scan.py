"""Scan the paper for common typo / duplicate-word patterns."""
import re
from pathlib import Path


def main():
    tex = (Path(__file__).resolve().parents[1] / "paper" / "v3.tex").read_text(
        encoding="utf-8"
    )
    # Strip LaTeX commands to get approximate plain text
    text = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^}]*\})?", " ", tex)
    text = re.sub(r"\$[^$]+\$", "", text)
    text = re.sub(r"\s+", " ", text)

    # Double word: match case-insensitively, same word twice
    dups = re.findall(r"\b(\w+)\s+\1\b", text, re.IGNORECASE)
    # Filter common valid double words
    valid = {"that", "had", "is", "on"}  # e.g. "so that that"
    dups = [d for d in dups if d.lower() not in valid]
    if dups:
        print("Possible duplicate words:")
        for d in dups[:20]:
            idx = text.lower().find(f"{d.lower()} {d.lower()}")
            if idx >= 0:
                ctx = text[max(0, idx - 40) : idx + 40]
                print(f"  {d!r}: ...{ctx}...")
    else:
        print("No obvious duplicate words found.")


if __name__ == "__main__":
    main()
