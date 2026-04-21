# Proofreading log — v3 paper

Pass date: 2026-04-20.

## Automated checks

- [x] `\ref` / `\eqref` ↔ `\label` consistency (21 labels, 4 refs used, no dangling)
- [x] `\cite` ↔ `\bibitem` consistency (7 cites, 9 bibitems, no dangling; 2 unused)
- [x] Duplicate-word scan: clean
- [x] LaTeX source compiles (v3.pdf already in `paper/`)

## Notes for the author

- **Unused bibitems:** `fechner1876vorschule`, `weyl1952symmetry` are in the
  bibliography but not yet `\cite`d in the paper. They're referenced in the
  book outline (Chapters 2 and 3) so leaving them is fine — they'll be
  needed when the Wundt / symmetry content moves from outline to prose.
- **Defensive labels:** many section / definition labels (`sec:intro`,
  `def:metric`, `eq:utility`, etc.) are placed but not yet referenced.
  Leaving them for future cross-reference is the right call.
- **Paper vs. book scope:** the paper (v3) covers roughly chapters 1-4 and
  14 of the book outline. Chapters 5-13 (sensory aesthetics and domain
  extensions) have no paper counterpart yet — they'd be the material for
  a second, more applied paper if you want a journal pair.

## Suggested next editorial moves

These are **not** defects in the current paper, just observations that
might inform future revisions:

1. **Section-level `\ref` use** would tighten the reading experience.
   Several sections cross-reference each other in prose ("as shown above")
   that could become "(Section~\ref{sec:utility})" for a tighter journal feel.
2. **A single figure** (the Wundt-curve or the preference-manifold SVG
   from `figures/`) would give the paper a visual anchor. Right now the
   paper is text-dense — journal editors usually appreciate one diagram
   in a theory paper.
3. **Pre-registration pointer** in §VII (Empirical Validation) could
   include a link to an OSF or Zenodo deposit once the data is public —
   reviewers ask for this consistently.

## Items left alone (per the standing instruction that the paper is
complete and production-quality)

- Thesis, theorems, proof sketches — not edited.
- Bibliography content — not edited.
- Author listing, affiliations, key formulas — not touched.
