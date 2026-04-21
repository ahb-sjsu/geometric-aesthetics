# Chapter 8: Stratification — Genre Boundaries, Style Thresholds, Phase Transitions

**RUNNING EXAMPLE — Daniel's Playlist**

Daniel, a music producer building a recommendation engine for an independent label, has inherited a model that predicts listens from MERT embeddings. On the full FMA Medium corpus (n = 24,801, artist-disjoint CV), his Lasso-on-spectrum achieves R = 0.302, a correlation he initially finds exciting. Then an intern runs a genre-residualized version. After controlling for genre, the hand-feature model drops from R = 0.151 to R = 0.043; the spectrum-Lasso drops from R = 0.302 to R = 0.177. Ninety-one percent of the hand-feature signal — and over sixty percent of the spectrum-Lasso signal — was genre confound. Within Rock, the residual is R = 0.139 (n = 7,088); within Electronic, R = 0.143 (n = 6,284); within Pop, R = 0.185 (n = 1,173). Within Classical, the residual is null (R = −0.013, n = 584). Within Jazz, null (R = 0.031, n = 384). Daniel realises his problem is not one model. It is five: one per genre, and in two genres, the predictor he has does not exist. The aesthetic manifold is not uniformly smooth. It is stratified.

## 8.1 The Patchwork Manifold {#patchwork-manifold}

The preceding chapters have developed the geometry of aesthetic space as though it were smooth: a single manifold $M$ with a tangent space at every point, a metric $g_{\mu\nu}$ that varies smoothly, trajectories along which parallel transport is defined. This apparatus is real and useful, but it is useful only *within a stratum*. Between strata — between genres, between historical periods, between modalities — the geometry changes discontinuously. Crossing a boundary is not a smooth trade-off. It is a change of regime.

This is not a theoretical embellishment. It is what the data showed us. Our headline Phase-1 books result (R = 0.241, 17σ) looked strong until we controlled for genre. After genre control, the residual was R = 0.093 (z = 6.5σ, p = 5.7 × 10⁻¹¹) — still real, still significant, but far smaller. Eighty-five percent of what our model was learning was *what genre looks like on the manifold*. The corresponding figure in music was ninety-one percent. The aesthetic metric, as naively fit on a mixed corpus, is mostly a sociological classifier.

The chapter's central claim, parallel to Chapter 8 of *Geometric Ethics* on moral strata and phase transitions, is that aesthetic space is a patchwork of smooth regions joined along boundaries where the rules change. Understanding the boundaries is as important as understanding the smooth interior — and more important for any honest empirical work, because fitting smooth models across boundaries is precisely how genre confound sneaks into an aesthetic claim.

## 8.2 Stratification, Made Concrete {#stratification-concrete}

### What a Stratum Is

In the language of Chapter 5, a *stratum* is a connected region of the aesthetic manifold on which the metric $g_{\mu\nu}$, the set of active dimensions, and the operative constraints are smooth and approximately constant. Examples of candidate strata in our empirical work include:

- The Victorian English novel (roughly 1837–1901), as a region of the book manifold.
- Twentieth-century rock music, as a region of the music manifold.
- Classical instrumental music, as a different region of the music manifold with a different effective metric.
- Non-fiction history-biography, as a region where our within-stratum aesthetic signal turned out to be null.
- Cross-lingual translations of a single source novel, as a tube on the manifold whose transverse structure is governed by the invariants documented in Chapter 17.

Within a stratum, the tensor apparatus of Chapters 6 and 7 applies: trajectories move smoothly, internal coherence and divergence mean what they mean, the Lasso-discovered axes retain their interpretation. Across strata, these things change. A high `pair_sim_mean` means one thing inside Victorian realism (coherent authorial voice, probably a good thing) and quite another inside a post-bop jazz album (tonal stasis, probably not what the album is trying to do).

### The Formal Setup

We follow the mathematical setup of Chapter 8 in *Geometric Ethics*: a stratification of the aesthetic manifold $M$ is a locally finite partition

$$M = \bigsqcup_{\alpha \in A} S_\alpha$$

into smooth submanifolds, together with a partial order $\preceq$ on $A$ encoding which strata lie in the closures of which others. The frontier condition — $S_\alpha \cap \overline{S_\beta} \neq \emptyset$ implies $S_\alpha \subset \overline{S_\beta}$ and $\alpha \preceq \beta$ — ensures a clean nesting.

The strata we observe empirically are not required to be Whitney-regular in the full technical sense. But the motivation for Whitney's conditions (A) and (B) carries over directly. We want tangent planes to behave continuously as we approach a stratum boundary, and we want the direction of approach to be well-defined. Empirically, this is what the cross-lingual invariance results of Chapter 17 demonstrate for translation-strata: the tangent structure of the within-bundle variation is tightly controlled (within-bundle std / between-book std runs from 0.18 on `path_eff` up to 0.44 on the divergence family), which is what "translations approach each other smoothly in the shared geometry" looks like statistically.

## 8.3 A Taxonomy of Aesthetic Boundaries {#boundary-taxonomy}

Aesthetic boundaries come in several kinds, and it will help to name them.

### Type I: Genre Boundaries

The clearest kind of aesthetic stratification is the genre boundary: the codimension-1 (or higher) surface separating one recognised form from another. Across such a boundary, the relative weights of aesthetic dimensions change. Within literary fiction, narrative coherence and character depth are heavily weighted; within scientific exposition, clarity of argument and accuracy dominate; within poetry, prosodic and imagistic features become central and sentence-level semantics less so.

Empirically, genre boundaries showed up in our data in two ways. First, as variance: Lasso on the PCA spectrum recovered seventy-one interpretable axes, of which a large majority correspond, on inspection, to genre or form directions. Second, as the genre-confound residualisation gap: the drop from R = 0.241 to R = 0.093 after genre control in books, and the drop from R = 0.302 to R = 0.177 in music.

The genre boundary is aesthetic reality's version of Chapter 8's Type I threshold in Ethics. It has a normal direction (across the boundary, rules change) and tangent directions (along the boundary, smooth variation preserves the regime). A book can become "more Victorian" without crossing out of Victorian realism; it crosses only when the governing metric itself changes — say, into modernist stream-of-consciousness, where internal coherence statistics reverse meaning.

### Type II: Style Thresholds

Within a genre, there are thresholds. A sonata becomes a symphony at a certain orchestral scale. A novella becomes a novel at length thresholds convention has fixed more or less arbitrarily. A poem becomes a prose-poem when line-breaks cease to be metrically load-bearing.

Style thresholds are typically first-order phase transitions in the sense of Chapter 8's physics analogy: the aesthetic evaluation function $S$ may jump discontinuously across the threshold (the symphonic evaluation is not simply the sonata evaluation with a multiplier), but the operative metric often retains its signature. Thresholds are smaller changes than genre boundaries; the generative rules are mostly preserved.

### Type III: Phase Transitions (Metric Change)

The most dramatic aesthetic boundary is the phase transition proper: a boundary across which the metric $g_{\mu\nu}$ changes in rank or signature — where different dimensions become relevant, different couplings become active, and the aesthetic regime shifts entirely.

The clearest empirical example we have is the books-vs-music cross-modality sign flip. Consider `pair_sim_mean`, the internal coherence statistic. In books, higher internal coherence correlates positively with rating (ρ = +0.126, 8.4σ). In music, higher internal coherence correlates *negatively* with listens (ρ = −0.076, p = 5×10⁻³³). The statistic is the same; the sign is opposite. Analogously, `step_mean` (the size of paragraph-to-paragraph or timestep-to-timestep jumps) is negatively correlated with rating in books (ρ = −0.096) but positively correlated with listens in music (ρ = +0.071).

These cross-modality sign flips are robust (each at p < 10⁻²⁸). They are also interpretable: books reward continuity (smaller steps, tighter coherence); music rewards contrast (larger steps, more dynamic variation). But this interpretation is a *restatement* of what we mean by phase transition. The very sign of the aesthetic gradient with respect to these features reverses between modalities. This is what it means for the metric to change at the boundary.

### Type IV: Absorbing Strata (Aesthetic Nullifiers)

Finally, there are absorbing strata: small, lower-dimensional regions that, once entered, dominate the evaluation regardless of other structure. In *Geometric Ethics*, Chapter 8 identified abuse, danger, and impossibility as universal nullifiers. The aesthetic sibling concept is less dramatic but real: works can enter aesthetic-absorbing regions where one feature collapses the evaluation. A novel with unreadable grammar, a piece of music with phase-cancellation errors, a film with severe projection faults — any of these enters a stratum where the transverse coordinates stop mattering. The rating collapses, and the richer aesthetic structure is bracketed out.

We do not have the clean empirical taxonomy for aesthetic nullifiers that *Geometric Ethics* has for moral ones. This is an open area, flagged also in Chapter 16.

## 8.4 Aesthetic Regimes and Metric Variation {#aesthetic-regimes}

### The Regime Concept

The empirical finding that most of our rating signal was genre confound is not a nuisance to be subtracted away. It is a structural observation about aesthetic space. It says: the manifold's metric is not constant. It is piecewise constant (roughly) on strata, and the strata correspond, to a substantial degree, to things humans already recognise as genres.

We will call each stratum's local metric its *aesthetic regime*. A regime is:

1. A set of active dimensions (which features of the work matter).
2. A local metric $g_{\mu\nu}^{(\alpha)}$ on those dimensions (how they trade off against each other).
3. A set of structural invariants (features that cannot be traded off at all within the regime, or that have been absorbed into constraint surfaces).

Within the fiction regime, internal coherence is positively valued, small steps are positively valued, moderate distance-from-prior is acceptable, and the seventy-one Lasso axes carry interpretable genre content. Within the rock-music regime, larger steps are positively valued, coherence is a weaker predictor, and specific timbral features dominate. Within the classical-music regime — where our Phase-4 within-genre residual was null (R = −0.013, n = 584) — our currently-extracted features *do not form a working aesthetic regime at all*. The features we have extracted are not the features by which classical listens are determined. This is a negative result, and a load-bearing one: it tells us that the aesthetic regime of classical music requires features we have not yet learned. Jazz showed the same null (R = 0.031, n = 384).

### Within-Genre Signal is Small but Real

Within fiction (excluding non-fiction), our Phase-2 residualised correlation was R = 0.131 at 6.2σ on n = 2,250. Within non-fiction history-biography, it was null. The "aesthetic residual beyond genre" — the claim that there is geometric aesthetic signal even after you have removed the sociological classifier — is therefore empirically supported *in fiction* and not supported (at our current feature set) in non-fiction history-biography or in classical/jazz music. This is the correct honest reframe: we argue that there is additional aesthetic signal beyond genre, in the strata where our features are well-tuned. We do not claim a universal "geometry predicts rating" across all strata.

### Metric Variation as a Field

Formally, we model the metric as a tensor field $g_{\mu\nu}(p)$ that varies across the manifold. On the smooth interior of each stratum, this field is approximately constant. At stratum boundaries, it jumps (Type I, II thresholds) or changes signature (Type III phase transitions). Outside each stratum, the field does something our current models do not cleanly represent, and Chapter 10 takes up the question of parallel transport across boundaries: can we move an aesthetic judgment from one regime to another coherently?

The practical consequence for any empirical aesthetic programme is: *fit within strata*. Fitting a single model across strata learns, primarily, the stratum boundaries. It learns the genre classifier. Honest aesthetic inference requires first identifying the stratum, then fitting within it, and reporting residuals against both the within-stratum and the cross-stratum baselines.

## 8.5 Cross-Lingual Invariance as Evidence Against Stratum Uniqueness {#cross-lingual-invariance}

A potential worry about the stratum picture is that it makes aesthetics too local — reducible to genre, to period, to reception community, to sociological category. If everything is stratum-bound, nothing survives beyond the particular regime in which it is measured.

Our Phase-3 cross-lingual results (Chapter 17; full methodology there) push against this worry. We encoded 4,683 non-English books in 19 languages across 10 language families using LaBSE, projected them into the English corpus's PCA-128 basis (the *same axes*, not refit per language), and measured whether the structural features of Chapters 6–7 transferred across language-family strata.

The headline numbers:

- `pair_sim_mean` transfers at mean Spearman ρ = +0.712 across language pairs.
- Mahalanobis-of-means: ρ = +0.710.
- Hellinger: ρ = +0.675.
- Bhattacharyya: ρ = +0.675.
- Jensen-Shannon: ρ = +0.674.
- Within-bundle standard deviation divided by between-book standard deviation — a measure of how language-invariant a feature is — runs 0.18 for `path_eff`, 0.28 for `recur_rate`, and 0.39–0.44 for the divergence family. Smaller is better, and these are small.

The English↔Finnish Hellinger correlation was ρ = +0.77 on n = 288 translations, p = 8×10⁻⁵⁷. English↔French Hellinger was ρ = +0.78 on n = 227. Six language families had statistical power: Germanic, Uralic, Romance, Hellenic, Italic-ancient, and Constructed.

Interpreted stratum-theoretically: translation is a tube on the aesthetic manifold, running from the source-language stratum to the target-language stratum. The cross-lingual invariance result shows that the transverse structure of this tube is tight. The aesthetic regime of a novel is preserved, to first approximation, across language-family boundaries. The stratum boundaries between, say, English-fiction and Finnish-fiction are *not* hard aesthetic boundaries: the same book in translation stays close to itself in the shared geometry.

This is the strongest piece of evidence we have that not every aesthetic boundary is a hard regime-change. Some boundaries — language-family boundaries in prose, in our data — are traversable without metric discontinuity. Others — the books/music modality boundary, the classical/rock genre boundary — are not.

### The Sinitic Gap

We flag honestly: our Chinese Gutenberg corpus (only five bundles formed, below the threshold of 20) did not participate in the invariance result. This is a corpus-design issue (Chinese Gutenberg is classical Chinese originals, not Western-work translations), not a failure of the method. The invariance claim is established for Germanic, Uralic, Romance, Hellenic, Italic-ancient, and Constructed language families. Extension to Sinitic, Japonic, and Slavic awaits a matched-translation corpus.

## 8.6 Boundary Effects in Practice {#boundary-effects}

Three practical recommendations follow from the stratification picture.

### Fit within strata.

A model that trains on a mixed corpus and reports a correlation with rating is, predominantly, learning genre. Report within-stratum residuals explicitly. If the within-stratum residual vanishes (as in history-biography, classical music, jazz), say so. Do not round the genre-confound finding into an aesthetic claim.

### Report both effect sizes and stratum coverage.

An aesthetic claim of the form "feature X predicts rating with ρ = 0.1" should always come with "in stratum $S$, n = n, p = p," and "the corresponding residualised ρ on mixed data is ρ'." The difference ρ − ρ' is the portion of the claim that was stratum membership rather than aesthetic content.

### Treat cross-modal transfer sceptically.

The books↔music sign flips on `pair_sim_mean` and `step_mean` are the cleanest empirical case of metric change across a phase transition we have. Any claim that aesthetic features transfer across modality should be checked directly, not assumed. Within modality, cross-lingual transfer is empirically well-supported (ρ = 0.7 across six language families). Across modality, even sign is not preserved.

## 8.7 The Geometry Near a Boundary {#geometry-near-boundary}

Parallel to Chapter 8's discussion in *Geometric Ethics* of the geometry near a moral stratum boundary, we can say something concrete about the geometry near an aesthetic one.

At a codimension-1 stratum boundary $B \subset M$, the tangent space at a point $p \in B$ decomposes into a tangential part $T_p B$ (directions along the boundary) and a normal part $N_p B$ (directions across it). Tangential motion keeps a work inside the stratum, varying it along feature-dimensions that preserve genre or regime. Normal motion crosses the boundary into a different regime.

For aesthetic work, this decomposition is operationally useful. Consider a novelist revising a draft. Some revisions move the book tangentially — sharpening character, improving prose rhythm, tightening plotting — keeping it inside the fiction regime where the metric that scored it is still meaningful. Other revisions move it normally — introducing essayistic digressions, breaking the fourth wall, adopting a documentary voice — crossing into a regime where different features become active and the original metric may no longer apply. A feedback mechanism that cannot tell tangential from normal revisions will give misleading advice near boundaries.

### Jump Discontinuities

At a Type I genre boundary, the evaluation function $S$ can exhibit a well-defined jump:

$$\Delta S(p) = \lim_{\varepsilon \to 0^+} S(p + \varepsilon n) - \lim_{\varepsilon \to 0^+} S(p - \varepsilon n)$$

where $n$ is the unit normal to the boundary at $p$. Empirically, this jump appears as the genre-confound residual itself: the 85% of books R² that disappears when we residualise against genre *is* the jump, projected onto the rating target. The within-stratum residual of R = 0.093 is the smooth-interior signal. Together, they decompose the total variance: a large boundary-aligned component plus a smaller within-stratum aesthetic component.

### Penumbral Zones

In practice, aesthetic boundaries are not always sharp. A novel-in-verse inhabits a penumbra between prose fiction and poetry. A documentary with scripted reenactments inhabits a penumbra between documentary and narrative film. In our corpus, works in penumbral zones can show unusual trajectory statistics — moderate values of several statistics that would be high on one side and low on the other — and their Lasso loadings often split across axes that are typically exclusive. The penumbra is not a failure of the stratification. It is the resolution of the stratification telling us that some works genuinely inhabit the boundary.

## 8.8 Connecting to the Ethics Sibling {#ethics-sibling}

The argument of this chapter parallels Chapter 8 of *Geometric Ethics* closely, but with a different source of empirical evidence. In Ethics, the stratification story is anchored by the Hohfeldian $D_4$ group, the universality of abuse/danger/impossibility as nullifiers across the Dear Abby corpus, and the 100% cross-linguistic transfer of the deontic axis in the BIP experiments. In Aesthetics, the stratification story is anchored by genre-confound residualisation (85% in books, 91% in music), by the within-genre fiction/non-fiction split (6.2σ in fiction, null in history-biography), and by the cross-lingual-invariance results across six language families.

The structural moral is the same in both books: aesthetic space, like moral space, is a patchwork. Smooth geometric methods work within a patch. Across patches, the rules change — sometimes by a threshold, sometimes by a phase transition with genuinely different metric signature, sometimes by entry into an absorbing regime. Honest work respects the patchwork.

And as in Ethics, the patchwork is not a nuisance. It is *the structure*. The strata are where genres live, where canonical periods live, where modalities differ. Studying the boundaries is studying the structure of aesthetic culture itself. Chapter 14 returns to this under the heading of collective aesthetic agency, where canon formation appears as the slow consolidation of strata through reception history.

## 8.9 Closing Note {#closing-note}

Before returning to Daniel, one more methodological remark. The stratification picture suggests a specific experimental protocol. For any new modality or corpus, before reporting aesthetic claims, run three analyses in sequence: a headline model fit across the whole corpus; a residualised model after controlling for the most obvious stratum variable (genre, period, language); and a within-stratum model fit on the largest coherent patch. The gap between the first and the second quantifies the stratum confound. The within-stratum result, where it is non-null, quantifies the genuine aesthetic residual. Where it is null (as in our Classical and Jazz results), the honest report is: the features we have do not form an aesthetic regime in this stratum, and additional feature work is required. This protocol was expensive to learn; its value is in forestalling overclaim.

Daniel, our music producer, finishes his week with a refactored model: five within-genre Ridge regressions, each reporting its own R and its own n, with explicit null flags on Classical and Jazz. He puts the global R = 0.302 in a footnote with the words "partially genre-classifier." His label's editorial team is unhappy at first — the footnote is a smaller number — but then they realise what the within-genre Rock R = 0.139 on 7,088 tracks actually means: an honest, small, real aesthetic residual, not inflated by genre confound, usable for in-genre recommendation without the failure mode of exporting rock assumptions to classical strata where they do not hold.

The manifold is stratified. The metric varies. The boundaries are real, sometimes traversable (translations) and sometimes not (modalities). The patchwork is the map.

Chapter 9 takes up the harder question lurking beneath the regime concept: if the metric varies across strata, where does any given stratum's metric *come from*? Is it a fact we discovered, a consequence of our modelling choices, or a convention we inherited? We argue for a middle position, and show that the cross-lingual invariance result is the strongest empirical evidence we have that the metric is more than convention.
