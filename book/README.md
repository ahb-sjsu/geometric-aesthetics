# Geometric Aesthetics — Book Source

Canonical markdown source for *Geometric Aesthetics: The Mathematical Structure of Judgment* (Book 13 of the Geometric Series).

## Structure

```
book/
├── README.md                        ← this file
└── src/
    ├── _BOOK_REFERENCE.md            ← shared style / identity / notation guide
    ├── chapter-01-introduction-why-geometry.md
    ├── chapter-02-the-failure-of-scalar-aesthetics.md
    ├── chapter-03-historical-precursors-geometry-before-geometry.md
    ├── chapter-04-mathematical-preliminaries.md
    ├── chapter-05-the-aesthetic-manifold.md
    ├── chapter-06-the-tensor-hierarchy.md
    ├── chapter-07-one-work-five-levels.md
    ├── chapter-08-stratification-boundaries-thresholds-phase-transitions.md
    ├── chapter-09-origin-of-the-aesthetic-metric.md
    ├── chapter-10-aesthetic-dynamics-parallel-transport-style-holonomy.md
    ├── chapter-11-aesthetic-reasoning-as-optimal-search.md
    ├── chapter-12-noethers-theorem-for-aesthetics.md
    ├── chapter-13-quantum-aesthetic-dynamics-superposition-measurement.md
    ├── chapter-14-collective-aesthetic-agency-canon-and-emergence.md
    ├── chapter-15-from-tensor-to-judgment.md
    ├── chapter-16-aesthetic-uncertainty-and-the-limits-of-geometric-determinacy.md
    ├── chapter-17-empirical-evidence-for-geometric-aesthetics.md
    ├── chapter-18-geometric-aesthetics-for-artificial-agents.md
    ├── chapter-19-deme-architecture-for-aesthetics.md
    ├── chapter-20-geometric-literary-criticism.md
    ├── chapter-21-geometric-musicology.md
    ├── chapter-22-geometric-film-and-television.md
    ├── chapter-23-geometric-visual-art.md
    ├── chapter-24-geometric-architecture.md
    ├── chapter-25-geometric-game-aesthetics.md
    ├── chapter-26-geometric-ai-curation.md
    ├── chapter-27-geometric-fashion-and-product-design.md
    ├── chapter-28-geometric-everyday-aesthetics.md
    ├── chapter-29-open-problems.md
    ├── chapter-30-conclusion-the-geometry-of-beauty.md
    └── appendices/
        ├── appendix-a-related-work-and-differentiation.md
        ├── appendix-b-reproduction-cookbook.md
        ├── appendix-c-human-subjects-research-roadmap.md
        ├── appendix-d-end-to-end-case-studies.md
        ├── appendix-e-skeptics-appendix-objections-alternatives-failure-modes.md
        └── appendix-f-mathematical-ledger-status-of-formal-claims.md
```

## Reading order

See [`../OUTLINE.md`](../OUTLINE.md) for the 6-part plan. Short version:

| Part | Chapters | Theme |
|---|---|---|
| **I — The Problem** | 1–3 | Why scalar aesthetics fails; historical precursors |
| **II — Foundations** | 4–9 | Mathematical machinery: manifolds, tensors, metric, stratification |
| **III — Dynamics** | 10–15 | Parallel transport; search; Noether; quantum dynamics; collectives |
| **IV — Meta** | 16–19 | Uncertainty limits; empirical evidence; artificial agents; DEME architecture |
| **V — Applications** | 20–28 | Literature, music, film, visual art, architecture, games, AI curation, design, everyday |
| **VI — Conclusion** | 29–30 | Open problems; the geometry of beauty |
| **Appendices** | A–F | Related work; reproduction; human-subjects protocol; case studies; skeptic's appendix; formal-claims ledger |

## Building

HTML rendering uses [`../build_book.py`](../build_book.py). From the repo root:

```bash
# Builds 30 chapters + 6 appendices + index.html using pandoc.
# Default output: ../erisml-lib/docs/geometric-aesthetics/  (the website)
# Override: AESTHETICS_OUT_DIR=/some/path python build_book.py
python build_book.py
```

Prerequisites:

- `pandoc` 3.x on PATH
- A sibling checkout of `ahb-sjsu/erisml-lib` at `../erisml-lib/` (or set `AESTHETICS_OUT_DIR`)

## Authoring conventions

Everything in [`src/_BOOK_REFERENCE.md`](src/_BOOK_REFERENCE.md) is load-bearing:

- Every chapter opens with a **RUNNING EXAMPLE** block (fixed protagonist set — Maya, Priya, Daniel, Hiroshi, Leona, Sam, Elena)
- First-person plural ("we")
- `# Chapter N: Title` heading, em-dash-subtitle form
- Section headings are poetic, not topic labels
- Empirical numbers must match the ledger in Appendix F
