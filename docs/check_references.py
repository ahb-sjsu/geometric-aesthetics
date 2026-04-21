"""Quick proofreader for the LaTeX paper: checks for dangling refs / cites."""
import re
import sys
from pathlib import Path


def main():
    tex_path = Path(__file__).resolve().parents[1] / "paper" / "v3.tex"
    tex = tex_path.read_text(encoding="utf-8")

    labels = set(re.findall(r"\\label\{([^}]+)\}", tex))
    refs = set(re.findall(r"\\ref\{([^}]+)\}", tex))
    eqrefs = set(re.findall(r"\\eqref\{([^}]+)\}", tex))
    cites_raw = re.findall(r"\\cite\{([^}]+)\}", tex)
    cites = set()
    for c in cites_raw:
        for k in c.split(","):
            cites.add(k.strip())
    bib = set(re.findall(r"\\bibitem\{([^}]+)\}", tex))

    all_refs = refs | eqrefs
    dangling_ref = all_refs - labels
    dangling_cite = cites - bib
    unused_labels = labels - all_refs
    unused_bib = bib - cites

    print(f"labels:      {len(labels)}")
    print(f"refs+eqrefs: {len(all_refs)}")
    print(f"cites:       {len(cites)}")
    print(f"bibitems:    {len(bib)}")
    print()
    bad = False
    if dangling_ref:
        print(f"DANGLING refs (no matching label): {sorted(dangling_ref)}")
        bad = True
    if dangling_cite:
        print(f"DANGLING cites (no bibitem): {sorted(dangling_cite)}")
        bad = True
    if unused_labels:
        print(f"NOTE unused labels: {sorted(unused_labels)}")
    if unused_bib:
        print(f"NOTE unused bibitems: {sorted(unused_bib)}")
    if not bad:
        print("all refs and cites resolve cleanly.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
