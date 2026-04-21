# Geometric Aesthetics — Shared Reference for Chapter Authors

**Purpose:** All chapters of *Geometric Aesthetics* (Volume 13 in the Geometric Series by Andrew H. Bond) must be stylistically consistent with the *Geometric Ethics* book (Volume 3 in same series) and numerically consistent with verified empirical findings. Read this entire file before writing.

## Book Identity

- **Title:** *Geometric Aesthetics: The Mathematical Structure of Judgment*
- **Volume:** Book 13 in the Geometric Series (full series: Methods=1, Reasoning=2, Ethics=3, Economics=4, Law=5, Cognition=6, Communication=7, Medicine=8, Education=9, Politics=10, AI=11, Gastronomy=12, Aesthetics=13)
- **Author:** Andrew H. Bond
- **Series:** Geometric Series (sibling to *Geometric Ethics: The Mathematical Structure of Moral Reasoning* and *Geometric Communication: Language, Signal, and the Topology of Meaning*, among others)
- **Voice:** First-person plural ("we"). Formal but readable. Mathematically literate, cross-disciplinary audience (philosophers, ML researchers, cultural theorists, practicing artists).
- **Core thesis:** Aesthetic judgment has geometric structure that a single scalar ("a 4-star book", "a beautiful song") cannot represent. Aesthetic evaluation is not a point on a line — it is a location in a space with dimensions, distances, directions, and curvature.

## Style Guide (Match Geometric Ethics Exactly)

### Opening style
Every chapter opens with a **"RUNNING EXAMPLE"** block introducing or continuing a protagonist whose aesthetic work or crisis illustrates the chapter's problem. Protagonists across the book may include:
- **Priya** (the data-scientist, returning from *Geometric Ethics*): now working on recommendation systems
- **Maya**, a novelist struggling with whether her book "works"
- **Daniel**, a music producer navigating taste-prediction models
- **Hiroshi**, a curator deciding what to acquire
- **Leona**, an architect whose facade designs keep getting rejected
- **Sam**, a film editor studying pacing
- **Elena**, a philosopher-critic writing on algorithmic curation
- *Pick and introduce as fits — write them with dignity, not as straw people.*

### Section structure
- Chapter title as `# Chapter N: Title` (with Chapter N, em-dash, subtitle form)
- Opening running example
- Thematic section headings like "The Shape of the Problem", "Three Failures of Flatland", "What Geometry Provides", "An Old Man and a Horse" — poetic, not just topic labels
- Subsections as `## Section` and `### Subsection`
- Closing note / bridge to next chapter
- Section IDs suitable for HTML anchors: `{#kebab-case-id}`

### Mathematical style
- LaTeX via `$...$` inline, `$$...$$` display
- Use Latin letters for variables, Greek for constants/parameters
- Define notation first use; reference Chapter 4 *Mathematical Preliminaries* for readers needing refreshers

### Rhetorical moves
- Parables and stories (the Old Man and the Horse is used in the Ethics book Ch 1; Aesthetics can use its own — e.g., *Hōjōki*, Zeami's *fūshi*, Duchamp's *Fountain*)
- "Three failures of flatland" style enumerations of scalar-view failures
- Honest caveats — never overclaim effect size; state p-values alongside effect sizes; genre-confound always acknowledged
- Epigraphs in italics where they enhance

### Prohibited
- Emojis
- Bullet-point overuse (prefer prose; bullets sparingly for enumerations)
- Overclaiming: "we prove", "we show definitively" — use "we argue", "we demonstrate empirically", "we present evidence that"
- Statistics reported without n, p, and effect size together

## Table of Contents

**Part I — The Problem**
1. Introduction — Why Geometry?
2. The Failure of Scalar Aesthetics
3. Historical Precursors — Geometry Before Geometry

**Part II — Foundations**
4. Mathematical Preliminaries
5. The Aesthetic Manifold
6. The Tensor Hierarchy
7. One Work — Five Levels
8. Stratification — Genre Boundaries, Style Thresholds, Phase Transitions
9. The Origin of the Aesthetic Metric — Discovery, Construction, Convention

**Part III — Dynamics**
10. Aesthetic Dynamics — Parallel Transport, Style Holonomy, Influence Flows
11. Aesthetic Reasoning as Optimal Search
12. Noether's Theorem for Aesthetics — Symmetry, Invariance, Translation
13. Quantum Aesthetic Dynamics — Superposition, Measurement, Observer
14. Collective Aesthetic Agency — Aggregation, Emergence, Canon
15. From Tensor to Judgment — The Philosophy of Aesthetic Choice

**Part IV — Meta**
16. Aesthetic Uncertainty and the Limits of Geometric Determinacy
17. Empirical Evidence for Geometric Aesthetics *(already drafted — do not rewrite)*
18. Geometric Aesthetics for Artificial Agents
19. The DEME Architecture for Aesthetics

**Part V — Applications**
20. Geometric Literary Criticism
21. Geometric Musicology
22. Geometric Film & Television
23. Geometric Visual Art
24. Geometric Architecture
25. Geometric Game Aesthetics
26. Geometric AI Curation
27. Geometric Fashion & Product Design
28. Geometric Everyday Aesthetics

**Part VI — Conclusion**
29. Open Problems
30. Conclusion — The Geometry of Beauty

**Appendices**
- A. Related Work and Differentiation
- B. Reproduction Cookbook
- C. Human-Subjects Research Roadmap
- D. End-to-End Case Studies
- E. Skeptic's Appendix — Objections, Alternatives, Failure Modes
- F. Mathematical Ledger — Status of Formal Claims

## Cross-References

Each chapter must cite others where relevant, by `Chapter N` or topic. Use forward and backward references. The running philosophical thread: *aesthetic judgment has structure → that structure has geometric content → that geometric content is measurable → it is modality-specific yet cross-linguistically invariant → aesthetic verdicts cannot be reduced to scalars without losing the directional information that matters most.*

## Verified Empirical Findings

These are the ONLY numerical results you may cite. Do not fabricate additional numbers.

### Phase 1 — Books Discovery
- n=4,998 Gutenberg↔Goodreads matched books
- LaBSE-encoded paragraphs
- Author-disjoint 5-fold CV
- Combined Ridge+Lasso R=0.241, 17σ, R²=0.058
- Four structural channels identified:
  - **A. Spectral divergences** (KL, JS, Hellinger, Bhattacharyya, Mahalanobis-mean, TV): ~8σ each
  - **B. Internal coherence** (`pair_sim_mean`, pair_sim_std): 8.4σ — novel finding, distinct from divergences
  - **C. Trajectory geometry** (`step_mean`, `step_std`, `step_skew`, `recur_rate`, `acf1_top3`, `curvature`, `path_eff`, `powerlaw_slope`, `tail_mass_100`): 3–6σ each
  - **D. Lasso on 128-d PCA spectrum**: 71 non-zero interpretable genre/form axes

### Phase 2 — Within-Genre Control (load-bearing)
- Residualized R=0.093, R²=0.009, z=6.5σ, p=5.7×10⁻¹¹
- **85% of headline R² was genre confound**
- Fiction intra-genre: R=0.131, 6.2σ, n=2,250
- Non-fiction, history-biography intra-genre: null
- **Honest reframe: "additional aesthetic signal beyond genre", not "geometry predicts rating"**

### Phase 3 — Cross-Lingual Invariance (the strongest finding)
- 4,683 non-English books, 19 languages, 10 language families
- LaBSE-encoded, projected into the English corpus PCA-128 basis (same axes, not refit per language)
- Bundles (≥20 threshold): FI 288, FR 227, DE 138, NL 88, IT 49, ES 38, EL 33, EO 24, HU 21, LA 20
- Exploratory (<20): PT 10, JA 4, PL 2, SV 2, RU 1, CS 1, ZH 5
- 6 language families with statistical power: Germanic, Uralic, Romance, Hellenic, Italic-ancient, Constructed
- Top features by mean Spearman ρ across language pairs:
  - `pair_sim_mean`: ρ = +0.712
  - `mahal_mean`: ρ = +0.710
  - Hellinger: ρ = +0.675
  - Bhattacharyya: ρ = +0.675
  - JS: ρ = +0.674
- Headline: EN↔FI Hellinger ρ = +0.77, n=288, **p = 8×10⁻⁵⁷**
- EN↔FR Hellinger ρ = +0.78, n=227
- Within-bundle std / between-book std (smaller = more language-invariant):
  - path_eff 0.18
  - recur_rate 0.28
  - Divergence family 0.39–0.44
- Rating transfer (EN-trained Ridge → non-EN bundled books): EN→pooled non-EN R=0.07, n=940, p=0.033 (weak but above chance)
- **Sinitic corpus gap:** Chinese Gutenberg corpus is classical originals (Confucius *Analects*, Sunzi *Art of War*, *Shijing*) — not Western-work translations. Only 5 bundles formed. Gap is corpus-design, not bug.

### Phase 4 — Music (FMA Medium, MERT-v1-330M)
- n=24,801 tracks, 30s clips, 45 timesteps × 1024-d per track
- Artist-disjoint 5-fold CV, target = log(1+track_listens)
- Raw Lasso-on-PCA-spectrum: R=0.302, z=49.8σ
- Genre-residualized: hand-feature R=0.043 (z=6.7), spectrum Lasso R=0.177, **z=28.3σ**
- **91% of hand-feature R² is genre confound** — worse than books' 85%
- Echonest head-to-head (shared n=5,233 tracks):
  - MERT Lasso-spectrum: R=0.225
  - MERT hand features: R=0.151
  - Spotify's 8 acoustic features: R=0.103
  - Bootstrap difference MERT vs Spotify: **p=0.001**
- Within-genre (artist-disjoint Ridge):
  - Rock R=0.139, n=7,088
  - Electronic R=0.143, n=6,284
  - Hip-Hop R=0.141, n=2,190
  - Pop R=0.185, n=1,173
  - Classical R=−0.013, n=584 (null)
  - Jazz R=0.031, n=384 (null)

### Cross-Modality Sign Flips (robust at p < 10⁻²⁸)
- `pair_sim_mean` (internal coherence):
  - Books: ρ = +0.126 (8.4σ) — higher coherence → higher rating
  - Music: ρ = −0.076 (p = 5×10⁻³³) — higher coherence → fewer listens
- `step_mean` (trajectory jump size):
  - Books: ρ = −0.096 (6.4σ) — smaller steps → higher rating
  - Music: ρ = +0.071 (p = 4×10⁻²⁹) — larger steps → more listens

**Interpretation: Books reward continuity and coherence. Music rewards contrast and dynamic variation. The aesthetic geometry has directionality that is modality-specific.**

### Methodological Notes
- Hellinger feature saturated at ~1.0 in music due to small-sample-in-high-dim Gaussian fits (45 tokens in 128-d is ill-conditioned). Fixed in K=32 PCA subspace; verdict unchanged. Bhattacharyya directly is preferable in practice.
- LaBSE: `sentence-transformers/LaBSE` (language-agnostic BERT sentence embedding)
- MERT: `m-a-p/MERT-v1-330M` (music-pretrained encoder, 160k hours SSL, layer-7 hidden states)

## Prior-Volume Connective Tissue

The book sits alongside *Geometric Ethics* (same series, same author). Where relevant, reference:
- The moral manifold (Ethics Ch 5) has an aesthetic sibling manifold — same geometric framework, different target variable
- Ethics Ch 6 tensor hierarchy → Aesthetics Ch 6 tensor hierarchy (parallel construction)
- Ethics Ch 9 "Origin of the Moral Metric" → Aesthetics Ch 9 "Origin of the Aesthetic Metric" (parallel methodological argument)
- Ethics Ch 12 Noether's Theorem → Aesthetics Ch 12 Noether (our cross-lingual invariance is a witnessed symmetry-invariance claim, making this chapter empirically load-bearing rather than speculative)
- Ethics Ch 15 "From Tensor to Decision" → Aesthetics Ch 15 "From Tensor to Judgment"
- Ethics Ch 17 "Empirical Evidence" → Aesthetics Ch 17 "Empirical Evidence" (our drafted content)
- Ethics Ch 19 DEME architecture → Aesthetics Ch 19 DEME-for-aesthetics

Where Ethics would say "an action", Aesthetics says "a work". Where Ethics speaks of "agents", Aesthetics speaks of "creators, audiences, critics, curators". Where Ethics has "moral weight", Aesthetics has "aesthetic valence" or "aesthetic signal".

## Where the New Results Create New Chapter Content

1. **Ch 12 (Noether)** — the cross-lingual invariance ρ=0.7 across 6 language families IS an empirical instantiation of a symmetry-invariance claim. Write this chapter with that result as the load-bearing empirical witness, not just a philosophical analogy.
2. **Ch 14 (Collective Agency)** — canon formation through geometric-distance aggregation; tie to the Lasso-discovered genre axes as discovered "canons".
3. **Ch 17** — already written, use as-is.
4. **Ch 20 (Literary Criticism)** — the book experiments are the native content here.
5. **Ch 21 (Musicology)** — the FMA/MERT experiments, with the sign-flip finding as the core surprise of the chapter.
6. **Ch 22–28 (other applications)** — extend the framework to modalities where we do NOT have direct empirical results. Speculative-but-principled: describe what the pipeline would look like, what predictions the framework makes, what would refute it. Do not claim empirical results we don't have.

## Writing Quality Bar

- Each chapter 3,000–5,000 words
- Prose-forward, not outline-disguised-as-prose
- Every claim either cited (to a real paper; flag TODO for citation lookup) or marked as conjecture
- Every numerical result has n, effect size, p-value
- Every effect-size claim has the genre-confound caveat where applicable
- Honest failure modes in any chapter that reports empirical claims
- Cross-references between chapters, by number, at least once per chapter

## Output Filenames

- Write to `C:\source\erisml-lib\docs\book\src\aesthetics\chapter-NN-slug.md`
- Chapter 17 is already at `C:\source\erisml-lib\docs\book\src\chapter-31-geometric-aesthetics.md` — **do not rewrite**; the build step will move it
- Appendices at `C:\source\erisml-lib\docs\book\src\aesthetics\appendices\appendix-X-slug.md`
