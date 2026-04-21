# Appendix F: Mathematical Ledger — Status of Formal Claims

*This appendix enumerates every formal mathematical claim that appears in* Geometric Aesthetics *and marks each with an epistemic status. The purpose is transparency: a reader should be able to see at a glance what is proved from standard mathematics, what is verified empirically by our data, what is conjectured as a framework prediction awaiting test, and what is analogy — mathematical language used for its expressive power without a literal claim on the domain.*

## F.1 The Four Epistemic Statuses

We use four labels throughout the ledger.

**Proved.** The claim is a standard mathematical result or follows by routine calculation from standard results. No aesthetic modeling commitment is required to establish it; it is mathematics. Example: the closed-form expression for the Kullback-Leibler divergence between two multivariate Gaussians.

**Verified empirically.** The claim is a predictive or structural assertion that we have tested against our data. Each such entry carries an effect size, a sample size, and a p-value. A "verified empirically" claim is not a logical theorem; it is a replicable finding in our corpora. If a future replication fails, the verification is withdrawn.

**Conjectured.** The claim is stated formally by the framework as a prediction but has not been tested, either because the required data does not yet exist or because the test requires infrastructure we have not built. Conjectures are falsifiable in principle; they await data.

**Analogy.** The claim uses the mathematical language of some formal system (Noether's theorem, quantum mechanics, gauge theory) for its expressive and structural power, but without committing to the literal applicability of that system to aesthetic phenomena. An analogy is not false; it is a deliberate interpretive move whose value is conceptual scaffolding, not theorem-proving. Appendix E §E.9 defends this move philosophically.

## F.2 The Ledger

The table below groups claims by chapter. The columns are: **Claim** (a brief formal statement), **Status** (one of the four above), **Evidence** (proof sketch, dataset and test, or commentary), and **Dependencies** (what the claim rests on).

### Chapter 4 — Mathematical Preliminaries

| # | Claim | Status | Evidence | Dependencies |
|---|---|---|---|---|
| F4.1 | A Riemannian metric $g$ on a smooth manifold $M$ induces a geodesic distance satisfying the triangle inequality. | Proved | Standard result; see do Carmo, *Riemannian Geometry*. | Axioms of a Riemannian metric. |
| F4.2 | For Gaussian $\mathcal{N}(\mu_1, \Sigma_1)$ and $\mathcal{N}(\mu_2, \Sigma_2)$, $D_{\mathrm{KL}} = \tfrac{1}{2}\big(\operatorname{tr}(\Sigma_2^{-1}\Sigma_1) + (\mu_2-\mu_1)^\top \Sigma_2^{-1}(\mu_2-\mu_1) - d + \log\tfrac{\det \Sigma_2}{\det \Sigma_1}\big)$. | Proved | Direct calculation from the definition of KL divergence. | Multivariate Gaussian density. |
| F4.3 | The Bhattacharyya coefficient between Gaussians: $BC = \det(\Sigma)^{-1/2}\det(\Sigma_1)^{1/4}\det(\Sigma_2)^{1/4}\exp(-\tfrac{1}{8}(\mu_1-\mu_2)^\top \Sigma^{-1}(\mu_1-\mu_2))$ with $\Sigma = (\Sigma_1 + \Sigma_2)/2$. | Proved | Standard. | Multivariate Gaussian density. |
| F4.4 | Hellinger distance: $H^2 = 1 - BC$ where $BC$ is the Bhattacharyya coefficient. | Proved | Standard. | F4.3. |
| F4.5 | Jensen-Shannon divergence: $JS = \tfrac{1}{2}D_{\mathrm{KL}}(p\|m) + \tfrac{1}{2}D_{\mathrm{KL}}(q\|m)$ with $m = (p+q)/2$ is symmetric and bounded. | Proved | Standard. | F4.2. |

### Chapter 5 — The Aesthetic Manifold

| # | Claim | Status | Evidence | Dependencies |
|---|---|---|---|---|
| F5.1 | The space of LaBSE-encoded paragraph clouds for a work can be embedded in a finite-dimensional feature space preserving enough structure to define pairwise distances. | Verified empirically | Paragraph clouds reduced to ~20 hand-features plus 128-d PCA spectrum; pairwise distances computed on 4,998 books; triangle inequality holds on all sampled triples (finite sample check). | Empirical dataset. |
| F5.2 | The empirical aesthetic manifold, equipped with the distance derived from feature-vector differences, has no degenerate pairs (zero distance between non-identical works) in our corpus. | Verified empirically | n = 4,998 books; all pairwise distances strictly positive in floating-point. | F5.1. |
| F5.3 | The aesthetic manifold carries the structure of a Riemannian manifold with a positive-definite metric everywhere. | Conjectured | Pairwise distances in the corpus satisfy triangle inequality on sampled triples, but the formal manifold-structure theorems (differentiable structure, metric smoothness, geodesic completeness) are not established. | TODO; open problem in Chapter 29. |
| F5.4 | Genre regions of the aesthetic manifold are connected subsets. | Conjectured | Empirically, within-genre k-NN graphs are connected at reasonable k, but a formal proof of connectedness requires topological assumptions on the encoder we have not established. | F5.1. |

### Chapter 6 — The Tensor Hierarchy

| # | Claim | Status | Evidence | Dependencies |
|---|---|---|---|---|
| F6.1 | The rank-0 aesthetic scalar (e.g., rating) is the lowest-information projection of the full feature tensor. | Proved (trivially) | Direct from dimension reduction; a scalar has strictly less information than a vector unless the feature vector is degenerate. | — |
| F6.2 | The rank-1 aesthetic vector field $O^\mu$ on a work is well-defined given a chosen basis of feature dimensions. | Verified empirically | All works in the corpus produce non-degenerate feature vectors of the posited dimensionality. | F5.1. |
| F6.3 | Rank-2 and higher tensors on the aesthetic manifold (metric, curvature) are mathematically well-defined given a smooth-manifold structure. | Conjectured (pending F5.3) | The tensors are defined in our code on finite-sample numerical approximations; formal smooth-manifold status is not established. | F5.3. |

### Chapter 9 — The Origin of the Aesthetic Metric

| # | Claim | Status | Evidence | Dependencies |
|---|---|---|---|---|
| F9.1 | An aesthetic metric can be *constructed* on the manifold by declaring a bilinear form and is not forced by the geometry. | Proved (by construction) | The framework exhibits multiple consistent metrics (Euclidean on features, Mahalanobis from the corpus covariance, learned from rating regression). | — |
| F9.2 | Any two candidate metrics induce different geodesics in general. | Proved | Standard Riemannian result. | F4.1. |
| F9.3 | The metric most predictive of human ratings in our corpus is the Mahalanobis-in-PCA-128 metric. | Verified empirically | Within-genre Ridge+Lasso R = 0.093, z = 6.5σ, p = 5.7×10⁻¹¹, n = 4,998 (after 85% genre residualization). | Dataset. |

### Chapter 10 — Aesthetic Dynamics

| # | Claim | Status | Evidence | Dependencies |
|---|---|---|---|---|
| F10.1 | Parallel transport on the aesthetic manifold along a path is well-defined given a connection $\nabla$ compatible with the metric. | Proved | Standard Levi-Civita result. | F4.1, F5.3. |
| F10.2 | "Style holonomy" — the failure of parallel transport to return to the starting tangent after a closed loop — is non-zero in the presence of curvature. | Proved (abstract) / Conjectured (empirical) | Abstract result from Riemannian geometry. Empirical measurement of holonomy on our corpus is not yet implemented. | F10.1. |
| F10.3 | Influence flows between works can be modeled as geodesic paths on the manifold. | Conjectured | No direct empirical test. | F5.3. |

### Chapter 12 — Noether's Theorem for Aesthetics

| # | Claim | Status | Evidence | Dependencies |
|---|---|---|---|---|
| F12.1 | **Language transformation leaves the geometric feature vector approximately invariant at the language-family level.** | Verified empirically | Spearman ρ averaged across language pairs: `pair_sim_mean` ρ = +0.712, `mahal_mean` ρ = +0.710, Hellinger ρ = +0.675, Bhattacharyya ρ = +0.675, JS ρ = +0.674. Headline EN↔FI Hellinger ρ = +0.77, n = 288, p = 8×10⁻⁵⁷. EN↔FR Hellinger ρ = +0.78, n = 227. 6 language families with statistical power (Germanic, Romance, Uralic, Hellenic, Italic-ancient, Constructed). | Chapter 17 experiments. |
| F12.2 | Within-bundle feature-std / between-book feature-std < 0.5 for a subset of structural features. | Verified empirically | `path_eff` 0.18, `recur_rate` 0.28, divergence family 0.39–0.44. n = 940 bundles across 19 languages. | F12.1. |
| F12.3 | Cross-lingual invariance is an instance of a Noether-style symmetry: a continuous transformation of the representation (language) that leaves a structural quantity (feature vector) invariant, implying a conserved quantity. | **Analogy** | The correspondence between language-invariance and Noether's theorem is suggestive and structurally apt: we have a transformation (language swap, acting on the underlying work), an invariant (the feature vector), and a conserved-quantity intuition (the aesthetic identity of the work). We do not *prove* a conservation law in the differential-geometric sense of Noether's theorem; the framework uses Noetherian vocabulary because the conceptual pattern matches, not because we establish a Lagrangian with a continuous symmetry group. | F12.1. |
| F12.4 | Rating transfer across languages: English-trained Ridge predicts non-English bundled ratings above chance. | Verified empirically | R = 0.07, n = 940, p = 0.033. Weak but above null. | F12.1, Goodreads dataset. |

### Chapter 13 — Quantum Aesthetic Dynamics

| # | Claim | Status | Evidence | Dependencies |
|---|---|---|---|---|
| F13.1 | Aesthetic judgment exhibits context-dependence analogous to quantum measurement: the act of articulating a judgment alters the judged. | **Analogy** | We adopt the mathematical vocabulary of quantum states and measurement operators to describe how aesthetic judgment is context-sensitive and observer-dependent. We do not claim aesthetic phenomena are quantum-mechanical in any literal physical sense. The analogy's value is that operator non-commutativity, superposition, and measurement collapse are well-understood conceptual templates for features of aesthetic experience that resist scalar modeling. | — |
| F13.2 | Order effects in pairwise aesthetic comparison: $\|A|B\rangle\neq \|B|A\rangle$ in general. | **Analogy** (structurally) / Conjectured (empirically) | The non-commutativity is built into the formalism. Empirical order-effect tests in aesthetic comparison are not yet part of our data; we propose them in Chapter 29 as a human-subjects study. | F13.1. |
| F13.3 | Aesthetic superposition: an unarticulated judgment is a linear combination of basis verdicts. | **Analogy** | The framework uses superposition as an expressive device for pre-articulation aesthetic states. No claim is made that inner experience literally has complex amplitudes. | F13.1. |

### Chapter 14 — Collective Aesthetic Agency

| # | Claim | Status | Evidence | Dependencies |
|---|---|---|---|---|
| F14.1 | Canon formation can be modeled as aggregation of individual judgments weighted by geometric distance on the manifold. | Conjectured | Plausible from aggregation theory, no direct empirical fit in our data yet. | F5.3. |
| F14.2 | The Lasso-discovered genre axes correspond to discovered canonical partitions. | Verified empirically | 71 non-zero Lasso axes on the 128-d PCA spectrum; post-hoc inspection reveals ~30 axes with interpretable genre/form correlates. | Chapter 17, books corpus. |

### Chapter 16 — Aesthetic Uncertainty

| # | Claim | Status | Evidence | Dependencies |
|---|---|---|---|---|
| F16.1 | The framework is well-defined only for encodable artifacts; live performance requires proxies. | Definitional / Proved by scope | The encoders used (LaBSE, MERT) operate on text and audio; live-event aesthetics fall outside this input class by construction. | — |
| F16.2 | Uncertainty in aesthetic judgment is upper-bounded by the uncertainty of the encoder-induced geometric measurement. | Conjectured | No formal bound established. | F5.1. |

### Chapter 17 — Empirical Evidence (load-bearing)

All numerical findings in Chapter 17 are *Verified empirically*; the ledger entries below consolidate them.

| # | Claim | Status | Evidence |
|---|---|---|---|
| F17.1 | Combined Ridge+Lasso on LaBSE-encoded Gutenberg↔Goodreads books predicts rating at R = 0.241, 17σ, R² = 0.058. | Verified empirically | n = 4,998, author-disjoint 5-fold CV. |
| F17.2 | 85% of F17.1's R² is attributable to genre confound. | Verified empirically | Residualization comparison; within-genre R² drops to 0.009. |
| F17.3 | Within-genre residualized signal: R = 0.093, z = 6.5σ, p = 5.7×10⁻¹¹. | Verified empirically | n = 4,998. |
| F17.4 | Fiction intra-genre signal: R = 0.131, 6.2σ. | Verified empirically | n = 2,250. |
| F17.5 | Non-fiction (history-biography) intra-genre signal: null. | Verified empirically (null) | R not statistically distinguishable from zero. |
| F17.6 | Cross-lingual invariance headline findings. | Verified empirically | See F12.1–F12.4. |

### Chapter 21 — Geometric Musicology

| # | Claim | Status | Evidence |
|---|---|---|---|
| F21.1 | Raw Lasso-on-PCA-spectrum predicts log(1+track_listens) at R = 0.302, z = 49.8σ. | Verified empirically | FMA Medium, n = 24,801, artist-disjoint 5-fold CV, MERT-v1-330M. |
| F21.2 | 91% of F21.1's R² is genre confound. | Verified empirically | Genre-residualized hand-feature R = 0.043 (z = 6.7); spectrum Lasso R = 0.177 (z = 28.3σ). |
| F21.3 | MERT-derived features outperform Spotify's 8 acoustic features on the Echonest head-to-head. | Verified empirically | Shared n = 5,233; MERT Lasso-spectrum R = 0.225, Spotify 8 features R = 0.103, bootstrap difference p = 0.001. |
| F21.4 | Within-genre predictive signal, artist-disjoint: Rock R = 0.139 (n = 7,088), Electronic R = 0.143 (n = 6,284), Hip-Hop R = 0.141 (n = 2,190), Pop R = 0.185 (n = 1,173). | Verified empirically | — |
| F21.5 | Within-genre, Classical and Jazz are null. | Verified empirically (null) | Classical R = −0.013, n = 584; Jazz R = 0.031, n = 384. |
| F21.6 | **Cross-modality sign flip on `pair_sim_mean`**: books ρ = +0.126 (8.4σ), music ρ = −0.076 (p = 5×10⁻³³). | Verified empirically | "Higher internal coherence → higher rating in books, lower listens in music." |
| F21.7 | **Cross-modality sign flip on `step_mean`**: books ρ = −0.096 (6.4σ), music ρ = +0.071 (p = 4×10⁻²⁹). | Verified empirically | "Smaller trajectory steps → higher rating in books, lower listens in music." |

### Chapters 22–28 — Modality Extensions (Applications)

| # | Claim | Status | Evidence |
|---|---|---|---|
| F22.1 | The sign-flip pattern on coherence and step-size generalizes to film and television (where continuity and pacing play analogous roles to books and music). | Conjectured | No empirical test with a film-specific encoder has been conducted. |
| F23.1 | A visual-art analog of the paragraph-cloud feature vector — computed from multi-crop or patch embeddings of an image — carries a measurable within-genre signal for viewer ratings. | Conjectured | Not tested. |
| F24.1 | Architectural aesthetics admit a geometric representation via multi-view image embeddings plus floor-plan embeddings, with cross-cultural invariance analogous to cross-lingual invariance. | Conjectured | Not tested; proposed as a future experiment in Chapter 29. |
| F25–F28 | The framework extends, mutatis mutandis, to game aesthetics, fashion, AI curation, and everyday aesthetics. | Conjectured | Framework prediction; no direct empirical program yet. |

### Chapter 29 — Open Problems (formal statements thereof)

| # | Claim | Status |
|---|---|---|
| F29.1 | Cross-cultural invariance holds beyond European language families. | Conjectured (open). |
| F29.2 | The aesthetic manifold admits a positive-definite Riemannian metric globally. | Conjectured (open; see F5.3). |
| F29.3 | Order effects in aesthetic judgment fit the quantum-analog prediction of F13.2. | Conjectured (open, human-subjects study proposed). |
| F29.4 | Sign-flip generalization across modalities (film, visual art, architecture). | Conjectured (open; see F22.1, F23.1, F24.1). |

## F.3 Commentary: Why the Status Distinctions Matter

The reader could in principle collapse all four statuses into "things the book says" and not lose narrative thread. We insist on the distinction for three reasons.

First, the status labels tell the reader where the work has been done and where it remains to be done. *Proved* results are complete — no future data will overturn F4.2, because it is algebra. *Verified empirically* results rest on replicable datasets and can be broken by future replications; their status is contingent. *Conjectured* results are open invitations to work. *Analogy* results are load-bearing conceptually but make no empirical commitment, and they protect against the reification trap Appendix E §E.9 warns about.

Second, the analogies are where the framework is most vulnerable to skeptical dismissal and most valuable as conceptual scaffolding. Noether's theorem (F12.3) and quantum dynamics (F13.1–F13.3) are the two places where the book uses heavy physics-theoretic vocabulary. We want readers to know, precisely, that these are *analogies*: the cross-lingual invariance result F12.1 is *verified*, but its interpretation as a Noether-style conservation law is interpretive. The fact that the analogy is apt — continuous symmetry in, conserved quantity out — is part of the book's argument. The fact that the analogy is not a proof is part of the book's honesty.

Third, the conjectures are the ledger of what we owe the field. F5.3 (the manifold structure), F14.1 (canon formation), F22.1–F24.1 (modality extensions), and F29.1–F29.4 (open problems) are commitments to future work, and they frame the research program *Geometric Aesthetics* opens. The book does not close an inquiry; it catalogues where the inquiry stands and what remains to prove, test, or refute.

We close the ledger with a principle that governs the whole book's relationship to its own formalism: **the framework is a tool, not a verdict.** The proofs hold. The empirical findings replicate (we claim; future replications will tell). The conjectures are open. The analogies are analogies. Readers who want a single scalar summary of "how much of aesthetics we have formalized" will not find one here, and that absence is the point: aesthetic judgment has geometric structure, and a scalar summary of it would be, once again, the Flatland mistake the book was written against.
