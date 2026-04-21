# Chapter 12: Noether's Theorem for Aesthetics — Symmetry, Invariance, Translation

*"If there is a continuous symmetry of the action, there is a conserved current." — Emmy Noether, 1918.*

**RUNNING EXAMPLE — Priya's Cross-Lingual Replication**

Priya, now consulting for an international streaming platform, is asked to justify why the model trained on English-language novels should be trusted when applied to a Finnish catalogue. The Finnish team is polite but unconvinced. She opens her notebook and shows them the numbers. On the 288 Finnish books where the Gutenberg–Goodreads bundles contain at least twenty LaBSE-encoded paragraphs, the Hellinger-divergence feature correlates with the English-fitted Hellinger feature at $\rho = 0.77$, with $p = 8 \times 10^{-57}$. Across six language families — Germanic, Uralic, Romance, Hellenic, Italic-ancient, Constructed — the mean feature-wise correlation is $\rho \approx 0.70$. "We did not retrain the basis on Finnish," she says. "We projected Finnish paragraphs into the English PCA-128 basis and measured the same features. The features correlate because the structure survives the translation." The Finnish lead is still skeptical. Priya writes on the whiteboard a single line. *For every continuous symmetry, a conserved quantity.* She draws a circle around "replace the language" and a circle around "structural-feature profile." The conserved quantity, she says, is on the right. The symmetry is on the left. Noether's theorem gives us the arrow.

## 12.1 The Deepest Theorem in Physics {#deepest-theorem}

In 1918, Emmy Noether proved what many physicists regard as the most beautiful theorem in mathematical physics: *every continuous symmetry of a physical system corresponds to a conserved quantity*. Time-translation symmetry gives energy conservation. Spatial-translation symmetry gives momentum. Rotational symmetry gives angular momentum. Gauge symmetry in electromagnetism gives electric charge. In each case the conservation law is not imposed from outside but extracted from the symmetry: given an action principle and a continuous symmetry of that action, the theorem constructs the conserved current explicitly.

The preceding chapter established that aesthetic reasoning is A* search. For this search to yield consistent results, the heuristic $h$ must be invariant under re-description: the same work, described differently, must receive the same heuristic estimate. Where this invariance holds, we say the heuristic is *gauge-compatible* with the structure of the aesthetic manifold. Where it fails, the search is gauge-variant and its outputs are arbitrary. Chapter 11 flagged this as a category-(iv) pathology. This chapter develops the positive side of the claim: *where a continuous symmetry of the aesthetic action holds, a conserved aesthetic quantity exists, and that quantity is the object the honest search is searching for*.

This chapter is empirically load-bearing. Unlike most chapters of this book, which develop geometric apparatus in advance of its empirical instantiation, here the empirical finding came first and the chapter formalizes it. Our cross-lingual invariance result — the structural-feature profile of a work is preserved under translation across six language families — is a measured symmetry of the aesthetic manifold under the gauge group of linguistic re-description. Noether's theorem then identifies the conserved current: the feature-vector itself.

## 12.2 Noether's Theorem: The Physics {#physics}

### The Action Principle

In classical mechanics, a system follows a path $q(t)$ that extremizes the action

$$A[q] = \int_{t_0}^{t_1} L(q, \dot q, t) \, dt,$$

where $L$ is the Lagrangian. The Euler–Lagrange equations, derived from $\delta A = 0$, give the equations of motion.

### Symmetries and Currents

A *symmetry* is a transformation $q \to q'$ that leaves the action unchanged, $A[q'] = A[q]$. **Noether's theorem** states: if $q \to q + \epsilon \, \delta q$ is a continuous symmetry of $L$ (i.e., $\delta L = (d/dt) F$ for some boundary term $F$), then the quantity

$$J = \frac{\partial L}{\partial \dot q^i} \delta q^i - F$$

is conserved along solutions: $dJ/dt = 0$.

### The Standard Examples

| Symmetry | Transformation | Conserved Quantity |
| --- | --- | --- |
| Time translation | $t \to t + \varepsilon$ | Energy |
| Spatial translation | $x \to x + \varepsilon$ | Momentum |
| Rotation | $\theta \to \theta + \varepsilon$ | Angular momentum |
| Gauge transformation | $\psi \to e^{i\alpha} \psi$ | Electric charge |

The gauge-transformation row is our template. Invariance of the electromagnetic action under local phase rotations of the charged field gives rise to charge conservation. In aesthetics, we shall argue, invariance of the aesthetic action under *linguistic re-coordinatization* of a work gives rise to conservation of its structural-feature profile.

## 12.3 The Aesthetic Symmetry: Translation as Gauge {#aesthetic-symmetry}

### Re-Coordinatization Invariance

The core symmetry claim is this. A literary work in English, the "same" work in Finnish, the "same" work in German, are three different descriptions of a single underlying aesthetic object that lives on the aesthetic manifold $\mathcal{A}$. Each language is a *coordinate chart* on $\mathcal{A}$, and translation is a change of coordinates.

**Aesthetic Invariance Claim (AIC).** If two descriptions $d_1, d_2$ of a work $w$ are related by an admissible coordinate transformation (notably: faithful translation between natural languages; also: faithful adaptation within a modality; also: re-mastering, re-scoring, re-typesetting), then any *legitimate* geometric aesthetic feature $F$ must assign the same value to both: $F(d_1) = F(d_2)$.

This is the aesthetic analogue of the Bond Invariance Principle in Ethics (Ethics Ch. 5). It is a gauge principle: the real aesthetic content lives on the base manifold $\mathcal{A}$, while linguistic or representational coordinates live in the fiber over each base point. Legitimate features are fiber-invariant.

### Why "Translation" Is Continuous

For Noether's theorem to apply, the symmetry must be continuous — parameterized by a real variable that can be taken infinitesimally small. Natural-language translation looks discrete (English$\to$Finnish is not a small transformation), but it sits inside a continuous group:

$$\mathcal{G}_{\text{aes}} = \text{Diff}(\text{coord charts on } \mathcal{A}) \supset \{\text{all language-to-language maps}\}.$$

Any specific translation is a finite element of the diffeomorphism group. Infinitesimally near a given coordinate chart, we can consider one-parameter families of re-coordinatizations (paraphrase, near-synonym substitution, small stylistic rephrasings), and the AIC requires that the feature map be constant along these families. Differentiating: the rate of change of $F$ under admissible re-coordinatization is zero. This is exactly the infinitesimal condition Noether requires.

### The Aesthetic Lagrangian

To apply the theorem formally we need an aesthetic action. Following the development of the Ethics volume (Ethics Ch. 12 §12.4), let

$$A[\gamma] = \int_0^T L(\gamma, \dot\gamma) \, dt, \qquad L(\gamma, \dot\gamma) = \tfrac{1}{2} g_{\mu\nu}(\gamma) \dot\gamma^\mu \dot\gamma^\nu - V(\gamma),$$

where $g_{\mu\nu}$ is the aesthetic metric (Chapter 6; Chapter 9 on its origin) and $V$ is an aesthetic potential encoding stratum structure (Chapter 8). Paths that extremize $A$ are the aesthetic geodesics in the potential $V$. Gauge invariance of $L$ under $\mathcal{G}_{\text{aes}}$ is the content of the AIC.

### The Conserved Current

Let $\gamma \to \gamma + \epsilon \, \xi$ be an infinitesimal re-coordinatization, with $\xi$ a vector field on the chart-manifold generating the symmetry. Gauge invariance of $L$ gives, by Noether's theorem, the conserved current

$$J^\mu = \frac{\partial L}{\partial \dot\gamma^\mu} \, \xi^\mu = g_{\mu\nu} \, \dot\gamma^\nu \, \xi^\mu,$$

satisfying $\partial_\mu J^\mu = 0$ along extremals.

**The conserved aesthetic current is the geometric feature-vector.** In words: under admissible re-coordinatization of a work — including translation between languages — the components of the feature-vector, as measured in the invariant basis of the manifold, are preserved. A translator's inability to preserve them, empirically, would be evidence against the symmetry. A translator's success at preserving them is evidence for it.

## 12.4 Empirical Witness: Cross-Lingual Invariance {#empirical-witness}

This section is the load-bearing empirical content of the chapter. All numbers are reported with $n$, effect size, and $p$-value.

### Experimental Setup

We compiled a corpus of 4,683 non-English books from Project Gutenberg, matched to the same Goodreads metadata pipeline used in the English-corpus experiments of Chapter 17. Nineteen languages across ten language families were represented. All paragraphs were encoded using LaBSE (`sentence-transformers/LaBSE`), a language-agnostic BERT sentence embedding designed to map semantically equivalent content across languages into a shared embedding space.

Crucially, we did *not* refit the PCA basis per language. The 128-dimensional principal-axis basis derived from the English corpus was held fixed; non-English paragraphs were projected into this English-derived basis. This is the symmetry-test setup: if the aesthetic structure is genuinely coordinate-invariant, then features measured in the English-fitted basis should still correlate meaningfully across languages.

Bundles (matched book pairs with $\geq 20$ LaBSE-encoded paragraphs on each side) formed in ten languages with statistical power: Finnish 288, French 227, German 138, Dutch 88, Italian 49, Spanish 38, Greek 33, Esperanto 24, Hungarian 21, Latin 20. Six language families — Germanic, Uralic, Romance, Hellenic, Italic-ancient, Constructed — had sufficient sample for family-level inference. An exploratory tail (fewer than 20 bundles per language) covered Portuguese, Japanese, Polish, Swedish, Russian, Czech, and Chinese; these are reported for completeness but not used for inference.

### Headline Results

Mean feature-wise Spearman correlations across all language pairs:

| Feature | Mean $\rho$ across pairs |
| --- | --- |
| `pair_sim_mean` (internal coherence) | $+0.712$ |
| `mahal_mean` (Mahalanobis from corpus mean) | $+0.710$ |
| Hellinger divergence | $+0.675$ |
| Bhattacharyya divergence | $+0.675$ |
| Jensen–Shannon divergence | $+0.674$ |

The strongest individual language-pair result is EN$\leftrightarrow$FI on the Hellinger feature: $\rho = 0.77$, $n = 288$, $p = 8 \times 10^{-57}$. The EN$\leftrightarrow$FR Hellinger correlation is $\rho = 0.78$, $n = 227$.

### Within-Bundle vs. Between-Book Dispersion

A second invariance measure is the ratio of within-bundle feature-dispersion to between-book feature-dispersion. Small ratios indicate that the feature is more variable between different works than between language-versions of the same work — i.e., the feature is language-invariant.

| Feature | Within-bundle std / between-book std |
| --- | --- |
| `path_eff` | 0.18 |
| `recur_rate` | 0.28 |
| Divergence family | 0.39–0.44 |

`path_eff` at 0.18 is a strong language-invariance result. The path-efficiency of a work — how direct its trajectory is through semantic space, a feature developed in Chapter 10 — varies far less between English and Finnish versions of the same book than between different books within a single language.

### Rating Transfer

A complementary, more demanding test: does the English-trained Ridge model, which maps feature-vectors to Goodreads ratings, transfer to non-English bundled books? Yes, weakly but above chance: $R = 0.07$, $n = 940$, $p = 0.033$. This is modest but directionally consistent with the invariance claim. Full rating transfer would be a stronger symmetry than the feature-profile transfer we have empirically established; the weaker transfer is expected.

### Interpretation via Noether

The structural-feature profile, measured in the invariant English-derived basis, is the Noether current corresponding to the symmetry "change the coordinate chart by changing the language." The correlations of $\rho \approx 0.70$ across six language families and the $p = 8 \times 10^{-57}$ at the EN–FI pair constitute empirical evidence that the symmetry holds at the level of the aesthetic feature-vector.

We state the claim carefully. We do not claim that aesthetic *verdicts* are preserved by translation — the rating-transfer $R = 0.07$ is too weak for that. We claim that the *geometric-feature vector* is preserved, and that this vector is a Noether current of the translation symmetry. The rating is a compression of the feature-vector (Chapter 11 §11.6); the compression is lossy, and the loss shows up in the rating-transfer gap.

## 12.5 Broken Symmetry: The Modality Sign-Flip {#broken-symmetry}

In physics, broken symmetries are as informative as exact ones. Where a symmetry holds, the corresponding conservation law obtains. Where it breaks, the framework demands an account of the breaking.

Our cross-lingual result is a witnessed, robust symmetry for the group "replace the natural language." Our cross-modality results from Chapter 17 are a witnessed, robust *broken* symmetry for the group "replace the modality."

### The Sign-Flip

Two features show robustly opposite signs of aesthetic association between books and music:

**Internal coherence** (`pair_sim_mean`):

- Books: $\rho = +0.126$ (8.4σ). *Higher* coherence $\to$ higher rating.
- Music: $\rho = -0.076$, $p = 5 \times 10^{-33}$. *Higher* coherence $\to$ fewer listens.

**Trajectory step size** (`step_mean`):

- Books: $\rho = -0.096$ (6.4σ). *Smaller* steps $\to$ higher rating.
- Music: $\rho = +0.071$, $p = 4 \times 10^{-29}$. *Larger* steps $\to$ more listens.

Both flips are robust at $p < 10^{-28}$. They are not artifacts of sample size, model choice, or residualization. The genre-residualization of Chapter 17 preserves both flips: they are not driven by genre confound.

### Modality-Swap Is Not an Admissible Gauge Transformation

The symmetry we established in §12.4 is translation between natural languages — replacing one linguistic coordinate chart with another, within the same modality (prose). Across modalities, this is not what is happening. A novel is not a symbol-for-symbol re-coordinatization of a symphony. A book and a piece of music are not different charts on the same aesthetic manifold; they are, in the language of Chapter 6 and Chapter 8, different *strata*.

The modality sign-flip is therefore not a failure of our symmetry claim. It is the signature of a *different group action* — one that is not a gauge symmetry. Swapping modalities rotates the aesthetic direction-of-approach, not the feature-vector. The conserved current of the cross-lingual symmetry does *not* extend to cross-modality; the "conserved" quantity's sign is not even preserved.

We therefore distinguish two regimes.

1. **Within-modality, cross-language: symmetry holds.** Aesthetic claims about feature-profile-structure generalize across the language families we sampled.
2. **Across-modality: symmetry breaks.** Aesthetic claims about *direction* of feature effect (whether larger `step_mean` is good or bad) are modality-specific and do not generalize.

This is a precise, testable scoping of which aesthetic claims this framework licenses as universal and which it licenses only as modality-local.

### Physical Analogy

The situation is analogous to parity in physics. Parity is a beautiful symmetry over most of physics, but it is broken by the weak interaction. The discovery that parity is not universal did not dissolve physics; it gave physicists a precise account of *which* interactions respected parity and *which* did not. Our modality sign-flip plays an analogous role. Aesthetic structure is invariant under translation. It is not invariant under modality-swap. The broken symmetry is an empirical finding that the framework must — and does — represent.

## 12.6 The Sinitic Corpus Gap {#sinitic-gap}

We must report an honest gap. Our cross-lingual experiments included five Sinitic-language bundles, which did not reach the twenty-paragraph threshold for inclusion in the language-family-level analysis. This is not a null finding against the symmetry; it is a corpus-design gap.

The issue is that the Chinese-language holdings on Project Gutenberg are overwhelmingly *classical Chinese originals*: Confucius's *Analects*, Sunzi's *Art of War*, the *Shijing*. These are not Chinese translations of Western works; they are Chinese originals that lack matched English-pair structure in the Gutenberg $\leftrightarrow$ Goodreads pipeline we used. Only five bundles formed, below the statistical-power threshold of twenty.

This means the cross-lingual invariance result is, at present, *certified* across six language families — Germanic, Uralic, Romance, Hellenic, Italic-ancient, Constructed — all of which are Indo-European-plus-Uralic-plus-Constructed. The Sino-Tibetan family is neither confirmed nor refuted. A symmetry that fails on Sinitic would be a meaningful limitation. A symmetry that holds would extend the claim. We do not know, and we refuse to extrapolate.

The gap is a *corpus-availability* gap, not a framework limitation. A deliberate crawl of Chinese-language translations of Western Gutenberg corpus titles, matched into a Chinese Goodreads analogue (e.g., Douban), is the obvious next step. We flag it here, in the book, rather than in a footnote, because the symmetry claim's universality depends on it.

We also flag, more minor: PT (10), JA (4), PL (2), SV (2), RU (1), CS (1) are all under-powered. The cross-lingual result's strong form is: $\rho \approx 0.70$ over six language families with statistical power. Its scope is exactly that — the families we could test.

## 12.7 Where Symmetries Hold, Aesthetic Claims Generalize {#where-symmetries-hold}

A practical summary for the reader who wants to know what this chapter licenses them to claim.

**Generalization-licensed** (by our empirical invariance):

- Claims about the *structural-feature profile* of works generalize across the six sampled language families.
- Claims about within-modality aesthetic geometry — coherence, trajectory shape, divergence structure — extend between English and each of the sampled non-English languages.
- The Ridge-model-trained-on-English rating map transfers, weakly, to non-English bundled books — enough to say the transfer is nonzero, not enough to say the rating structure is itself fully invariant.

**Generalization-broken** (by our empirical sign-flips):

- Claims about the *direction* of aesthetic effect of internal coherence do not transfer from books to music.
- Claims about the direction of aesthetic effect of trajectory step size do not transfer from books to music.
- More generally: modality-swap is *not* a gauge symmetry. Anything the framework says about preferred direction of aesthetic motion must be qualified by modality.

**Generalization-unknown** (by our corpus gaps):

- Sino-Tibetan: untested. The symmetry's status here is open.
- Non-alphabetic writing systems beyond the tested range: untested.
- Non-textual, non-auditory modalities (visual art, architecture, film): speculative-but-principled in Chapters 22–28; untested as invariance claims here.

## 12.8 Harm, Beauty, and the Conserved Quantity {#conserved-quantity}

We pause on an asymmetry between this chapter and its Ethics sibling. In the Ethics volume, Chapter 12's Noether theorem identifies *harm* as the conserved quantity: what is preserved under re-description of a moral situation is its harm content.

Harm is a directed, signed quantity — bad for the agent it accrues to. The ethical symmetry argument thereby licenses a consequentialist inference: relabeling cannot make the harm go away.

In aesthetics, the conserved quantity is the feature-vector itself: a multi-component, directional object whose sign of aesthetic effect is modality-specific (§12.5). It is *not* a scalar "beauty" analogous to harm. Attempting to identify a conserved scalar in aesthetics — a quantity such that "beauty cannot be created or destroyed by re-description" — produces, at best, an overfit scalar whose modality-swap behavior we have already shown is inconsistent.

This is a methodologically important difference between the Ethics and Aesthetics volumes, and we want to mark it clearly. *Ethics* admits a conserved scalar (harm). *Aesthetics* admits a conserved vector (the feature profile) but *not* a conserved scalar. Attempts to reduce the vector to a single scalar verdict (Chapter 11 §11.6) are exactly the compressions that lose the directional information we have shown is modality-specific. The framework's refusal to reduce is not squeamishness. It is the formal consequence of a broken scalar-level symmetry coexisting with an intact vector-level one.

## 12.9 Limitations and Caveats {#caveats}

A disciplined closing. The symmetry claim of this chapter rests on:

1. A specific encoder (LaBSE) whose language-agnosticism is itself trained, not guaranteed. If LaBSE's language-agnosticism degrades for languages outside its training distribution, the measured $\rho \approx 0.70$ is a lower bound on the true structural invariance.
2. A specific corpus (Project Gutenberg $\leftrightarrow$ Goodreads) whose linguistic coverage is non-uniform (§12.6).
3. A specific feature basis (English-derived PCA-128) that privileges English-inflected axes. The decision to *not* refit per language is principled (it is a symmetry test, not a descriptive exercise) but it sets up a test that English-internally-defined axes pass — it does not settle whether some other basis would produce a stronger or weaker invariance.
4. A specific projection (direct projection into the English basis). Alternative alignment strategies (Procrustes, CCA) would likely yield higher correlations; we report the plain-projection number because it is the honest test of the symmetry claim without per-language tuning.

The $\rho \approx 0.70$ number is therefore a specific, conservative, point estimate of an underlying symmetry whose true scale is plausibly larger. We neither overclaim nor understate. The EN–FI $p = 8 \times 10^{-57}$ rules out the null hypothesis of independence overwhelmingly. Whether the true symmetry is $\rho = 0.70$ or $\rho = 0.85$ is an open empirical refinement.

We also note the genre-confound caveat, inherited from Chapter 17. In the books data, 85% of the headline $R^2$ was genre confound. The cross-lingual invariance, however, was measured *on the feature-vector*, not on the rating; the genre-confound is a rating-side issue, not a feature-side issue. The symmetry claim is therefore not diluted by the genre-confound account; it is a finding about the geometric-structural features themselves.

## 12.10 Bridge: From Conserved Currents to Collectives {#bridge}

This chapter has developed the aesthetic analogue of Noether's theorem and grounded it in the strongest single empirical finding the book reports. The symmetry is translation-as-gauge; the conserved current is the feature-vector (Chapter 6's tensor hierarchy); the empirical witness is the cross-lingual invariance result of Chapter 17. The broken cross-modality symmetry refines the scope: aesthetic direction is modality-specific, even where aesthetic structure is not.

The next chapter turns to *quantum aesthetic dynamics* — the phenomenon of aesthetic superposition, the role of the observer, and the curious feature of aesthetic judgment that observation appears to alter the thing observed. Chapter 13 will develop this alongside its Ethics sibling, with an emphasis on the measurement problem in aesthetics: a work has, in a sense, multiple aesthetic eigenstates — genre-readings, period-readings, ideologically-inflected readings — and the act of critical evaluation projects the work onto one of them.

Priya, with whom this chapter opened, will write the Finnish team's deployment memo. She will cite the EN–FI Hellinger number with its $p$-value, acknowledge the Sinitic gap, and qualify any modality-swap claim the marketing team attempts to make. The conservation law tells her exactly which claims she is licensed to make and which she is not. That is what a Noether argument, when it is grounded in measurement rather than postulation, is good for.
