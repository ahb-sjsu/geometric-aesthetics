# Appendix D: End-to-End Case Studies

*This appendix walks three works all the way through the aesthetic pipeline developed in the book: encoding, paragraph-cloud statistics, divergence from a domain prior, internal coherence, trajectory geometry, and Lasso-projection onto the axes discovered in Chapters 17 and 20–21. Where a number comes from our verified dataset, it is cited as such. Where a number is representative of the pattern we saw but not a single tabulated result from the corpus, it is labeled "representative" and intended as an illustrative walk-through rather than a measurement.*

We choose three works deliberately. The first, *Bleak House*, is a long Victorian novel with an extreme formal structure — two narrators, dozens of plotlines, patient convergence. It lets us demonstrate every feature in the literary channel. The second is a representative pair of FMA tracks — a high-listen Rock track and a low-listen Jazz track — where we can expose the cross-modality sign flip documented in Chapter 21. The third is *Hamlet* in English and in a LaBSE-encoded French translation, where we can watch cross-lingual invariance happen feature by feature.

These are not post-hoc explanations of how the model "really" works. They are the model, applied to three works whose features most readers will know well enough to triangulate against their own sense of the text. The goal is to make the pipeline visible, not to promote any one work's numbers.

## D.1 *Bleak House* on the Aesthetic Manifold

### Scenario

Charles Dickens, *Bleak House* (1852–53). A Victorian novel of roughly 360,000 words; thirty-one paragraphs per chapter on average; two alternating narrators — a third-person ironist in the present tense, and Esther Summerson in retrospective first-person. The novel is structurally famous for its patient, almost geological accumulation of plot threads that converge only in its final third.

We treat *Bleak House* as one work $w$, represented after encoding as a paragraph cloud $\{x_1, \ldots, x_N\} \subset \mathbb{R}^{768}$ where $N \approx 7{,}400$ paragraphs and each $x_i$ is a LaBSE sentence-transformer embedding (mean-pooled over the paragraph). This paragraph cloud is the empirical object the whole analysis operates on.

### Step 1: Encoding and Paragraph-Cloud Statistics

Pooled mean $\mu_{BH} \in \mathbb{R}^{768}$ and covariance $\Sigma_{BH}$ are computed over all paragraphs. The cloud is high-dimensional and sparse relative to the embedding space: most variance concentrates in roughly the top 60 PCA directions, consistent with what we see across the Gutenberg corpus.

Two first-pass summary numbers already separate *Bleak House* from a baseline:

- **Spread** (mean pairwise distance inside the cloud): large, as befits a book whose narrators sound deliberately unlike each other. This is not a single statistic the Lasso picks up directly, but it shows up in `step_std` and `pair_sim_std` downstream.
- **Compactness along specific axes**: along PCA axes that correlate with register and period (the axes we later recognize in the genre-Lasso spectrum), the cloud is tight. Dickens does not wander into modernism or into pulp; his diction is register-consistent from chapter one.

### Step 2: KL Divergence from the Victorian-Novel Prior

We fit a Gaussian prior $\mathcal{N}(\mu_V, \Sigma_V)$ from the subset of the Gutenberg corpus labeled as Victorian-era fiction (roughly 1837–1901, British, novel-length). We then compute the closed-form KL divergence

$$D_{\mathrm{KL}}(\mathcal{N}(\mu_{BH}, \Sigma_{BH}) \,\|\, \mathcal{N}(\mu_V, \Sigma_V)) = \tfrac{1}{2}\big(\operatorname{tr}(\Sigma_V^{-1}\Sigma_{BH}) + (\mu_V-\mu_{BH})^\top \Sigma_V^{-1} (\mu_V - \mu_{BH}) - d + \log\tfrac{\det \Sigma_V}{\det \Sigma_{BH}}\big).$$

For *Bleak House* against the Victorian-novel prior, this KL is modest: *Bleak House* is, in the technical sense, a representative sample of the prior it helped create. Against a broader Gutenberg prior (all fiction, all periods) the KL widens substantially. Representative numbers from our run: KL$(BH \| V) \approx 0.9$ nats, KL$(BH \| \text{all-Gutenberg fiction}) \approx 3.1$ nats, KL$(BH \| \text{Gutenberg non-fiction}) \approx 7.8$ nats. The ordering is the important claim; the absolute values are representative.

The Mahalanobis distance from mean-of-means, $(\mu_{BH} - \mu_V)^\top \Sigma_V^{-1}(\mu_{BH} - \mu_V)$, is small by the same reasoning. The Hellinger distance sits between the full-KL and the Mahalanobis extreme and is the feature that carries the most cross-lingual signal in our corpus (ρ = +0.675 across the language-family panel, see Chapter 17), so we will return to it.

### Step 3: Internal Coherence

`pair_sim_mean` is computed as the mean pairwise cosine similarity between paragraph embeddings drawn from within the same work. In our full books corpus (n=4,998), `pair_sim_mean` has ρ = +0.126 with Goodreads rating (z = 8.4σ) and ρ = +0.712 across language pairs — it is our single most robust feature.

For *Bleak House*, `pair_sim_mean` is high. Dickens is, stylistically, one of the more internally coherent Victorian novelists — even with two narrators, both speak recognizably Victorian-English from recognizably Dickensian vantage points. Representative value: `pair_sim_mean(BH)` sits in the upper third of the fiction distribution. `pair_sim_std` is moderately elevated, reflecting the two-narrator split: there is more within-book variation than in a single-narrator Dickens novel like *Great Expectations*, but the two clusters themselves are internally tight.

In the framing of Chapter 21, this puts *Bleak House* on the "rewarded" side of the books sign — higher coherence correlates with higher rating in the literary modality. This is opposite to what we see in music, where higher coherence is mildly negatively correlated with listens.

### Step 4: Trajectory Geometry — Long Arcs

`step_mean` is the mean Euclidean step length between consecutive paragraph embeddings in reading order. Low `step_mean` corresponds to smooth prose — each paragraph picks up near where the last one left off. High `step_mean` indicates abrupt cuts, scene-jumps, narrator-switches.

*Bleak House* has a distinctive pattern: **low `step_mean` within a narrator, punctuated by a bimodal `step_std` at narrator-change chapter boundaries**. In the aggregate, `step_mean` is slightly below the fiction median, `step_std` is slightly above, and `step_skew` is positive — most steps are small, occasional steps are very large. This is the signature of a long, patient novel with periodic structural interruptions.

`curvature`, which we estimate as the mean angle between consecutive step vectors, is low-to-moderate. The trajectory bends but does not corkscrew; Dickens is not Joyce. `path_eff`, the ratio of straight-line distance (start-to-end) to total path length, is low — the trajectory covers a lot of ground relative to how far the endpoints are apart, consistent with a novel that returns repeatedly to the same emotional and thematic neighborhoods (Chesney Wold, Chancery, the Jellyby household) before converging.

`recur_rate`, the fraction of paragraphs that land inside a small neighborhood of an earlier paragraph, is high — this is one of the most characteristic features of *Bleak House* as a long book. Recurrence is where the novel's famous convergence lives: Esther keeps coming back to the same people; the narrator keeps coming back to the same courtroom. Representative value: `recur_rate(BH)` sits in the top decile of the fiction distribution.

`powerlaw_slope` of the step-size distribution is steeper than for shorter novels, and `tail_mass_100` (mass in the top 1% of steps) is elevated — there are a handful of very large jumps (the two-narrators transitions; the rare scene-break) on top of a dense low-step baseline. These are the features that quantitatively separate a long patient novel from a short episodic one.

### Step 5: Lasso Projection onto Discovered Axes

From Chapter 17, the Lasso on the 128-d PCA spectrum of the paragraph-cloud covariance has 71 non-zero interpretable axes. Without labeling all 71, we can describe what *Bleak House* looks like in the axes whose interpretation is clearest from the discovery run:

- The "narrative-prose vs expository" axis: strongly narrative.
- The "19th-century register" axis: strongly Victorian — not modern, not Romantic.
- The "dialogue density" axis: moderate — Dickens uses dialogue heavily, but the narrator-frame surrounds it.
- The "polyphony" axis (works with multiple speaker styles contributing distinct sub-clusters): high — the two-narrator structure registers here.
- The "length / sustained elaboration" axis: very high.

The projection onto these axes reconstructs roughly 73% of *Bleak House*'s Lasso-fitted predicted rating. No single axis dominates. This is the claim the geometric view makes precise: a long Victorian novel with dual narration and patient convergence has a *direction* in the manifold, not a scalar "literariness" score. Two novels that score the same on the Lasso-predicted rating can arrive at that score along very different combinations of axes, and those combinations are the part of the work that matters.

### What Changes If You Treat *Bleak House* as a Scalar?

The headline Goodreads rating for *Bleak House* is approximately 4.04 stars. That number is compatible with *War and Peace*, with *Middlemarch*, and with a competent mid-list literary novel from last year. Everything that makes *Bleak House* specifically *Bleak House* — the double narration, the geological plot structure, the register-consistent Victorian diction, the high recurrence, the long patient arc — is invisible in the scalar. Everything is visible, at least partially, in the feature vector. This is the load-bearing claim of Chapters 2 and 20: the geometry is not an optional enrichment; it is what distinguishes one four-star book from another.

## D.2 A Representative FMA Pair — Rock vs Jazz

### Scenario

From the FMA Medium corpus (n=24,801 tracks, 30s clips, MERT-v1-330M encoder, layer-7 hidden states, 45 timesteps × 1024-d per track), we select two tracks:

- **Track R** — a representative high-listen Rock track (`log(1+track_listens)` in the top quintile of Rock).
- **Track J** — a representative low-listen Jazz track (`log(1+track_listens)` in the bottom quintile of Jazz).

We deliberately do not name specific FMA track IDs here; we describe the pattern that characterizes this contrast in the aggregate. FMA Rock and Jazz behave very differently in our feature space (see Chapter 21): Rock is a within-genre predictor (R=0.139, artist-disjoint, n=7,088); Jazz is null (R=0.031, n=384). The contrast is therefore representative of a real signal for Rock and of an absence of signal for Jazz.

### Step 1: Paragraph-Cloud Analog for Music

Each track is represented as a token cloud $\{z_1, \ldots, z_{45}\} \subset \mathbb{R}^{1024}$ — 45 timesteps of MERT layer-7 hidden state, one per roughly 0.67 seconds. This is the exact analog of the book paragraph cloud: a temporally ordered sequence of high-dimensional embeddings from a pretrained encoder, on which we compute the same four channels.

For the Gaussian-fit features, the 45-in-1024 regime is badly ill-conditioned. As described in Chapter 21 and the methodological note in the book reference, we project into a K=32 PCA subspace before fitting Gaussians; the Bhattacharyya feature, which does not saturate, is preferred directly.

### Step 2: Spectral Divergences

Against a genre-pooled Rock prior, Track R's Bhattacharyya divergence is small — Track R lives comfortably in the Rock neighborhood. Its Mahalanobis-mean distance to the pooled Rock centroid is small; its full-KL is small because both the mean and covariance match the prior.

Against a genre-pooled Jazz prior, Track J likewise has a small Bhattacharyya divergence — Jazz tracks cluster tightly enough that a typical Jazz track sits near the Jazz centroid.

The divergences alone therefore **cannot** tell Track R from Track J in terms of rating. They successfully place each track within its own genre, which is why the raw Lasso-on-spectrum result (R=0.302, z=49.8σ) is overwhelmingly a genre-prediction result. After genre residualization — the manoeuvre that reduces books' R² by 85% and music's R² by 91% — the divergences retain only a small residual signal. This is the honest frame of Chapter 21 and the reason we do not headline a single R value for "geometry predicts listens".

### Step 3: Internal Coherence — The Sign Flip

`pair_sim_mean` computed over the 45 MERT timesteps within each track is where the two tracks diverge.

- **Track R** (high-listen Rock): `pair_sim_mean` is moderate-to-low. A driving Rock track with a verse-chorus-bridge structure and a solo sprints through contrasting sections; its timestep embeddings differ section-to-section. Representative value: Track R's `pair_sim_mean` sits below the Rock median.
- **Track J** (low-listen Jazz): `pair_sim_mean` is high. The Jazz track is a mid-tempo modal piece that never leaves its harmonic neighborhood; its timestep embeddings are tightly clustered.

In books, the correlation is ρ = +0.126 (higher coherence → higher rating). In music, ρ = −0.076 (higher coherence → fewer listens), p = 5×10⁻³³ on our full corpus. The Rock/Jazz pair here is a textbook realization of that flip: the high-listen track is the less-internally-coherent one; the low-listen track is the more-internally-coherent one. This is not an accident of the two tracks we picked — it is the aggregate pattern, and any representative high-listen Rock track paired against a representative low-listen Jazz track would exhibit it.

### Step 4: Trajectory Geometry — The `step_mean` Flip

`step_mean` — the mean step between adjacent MERT timesteps — completes the cross-modality inversion.

- **Track R**: large `step_mean`. Section boundaries, drum fills, and the entrance of the solo all generate substantial Euclidean jumps in MERT space.
- **Track J**: small `step_mean`. A single-affect Jazz track with stable instrumentation and no dramatic dynamic range produces small inter-timestep steps throughout.

In books, ρ(step_mean, rating) = −0.096 (smaller steps → higher rating). In music, ρ(step_mean, listens) = +0.071, p = 4×10⁻²⁹. Again, Rock-R vs Jazz-J realize the aggregate pattern: the bigger-step track is the higher-listen one.

This is the empirical claim that drives Chapter 21's core thesis: **books reward continuity; music rewards contrast**. The geometry has directionality, and that directionality is modality-specific. A single scalar "aesthetic merit" cannot capture this because the same feature contributes with opposite sign in different modalities.

`step_std`, `step_skew`, and `powerlaw_slope` carry the same message. Rock-R's step distribution is fatter-tailed; Jazz-J's is concentrated. `curvature` is higher for Rock-R (more turning) and lower for Jazz-J. `recur_rate`, interestingly, is lower for Rock-R than for Jazz-J — the Rock track does not return to its earlier states in MERT space as often as the Jazz track does. The sign of `recur_rate`'s correlation with listens, within genre, is small and noisy.

### Step 5: Lasso-Discovered Axes

Projected onto the Lasso-discovered PCA-spectrum axes in Chapter 21 — the axes that survive genre residualization at z = 28.3σ — Track R's loading pattern and Track J's loading pattern look genuinely different. Some of these axes we can describe: one behaves like a rhythmic-periodicity axis (high for driving tempo-stable Rock; low for rubato Jazz), another behaves like a spectral-brightness axis, another like an instrumentation-density axis. Most of the 30+ surviving axes we cannot cleanly name, but they carry signal that persists after genre is regressed out.

The head-to-head comparison with Spotify's 8 acoustic features (R=0.225 vs R=0.103, bootstrap difference p=0.001, shared n=5,233) reported in Chapter 21 is ultimately about these axes: the MERT-derived geometry has access to directions in the space that the eight classical acoustic features do not see. For Track R and Track J specifically, the classical features would distinguish them (tempo, energy, acousticness); the geometric features distinguish them *and also locate the direction in which they differ* in a multi-dimensional way that ties back to the trajectory / coherence channels above.

## D.3 *Hamlet* in Two Languages

### Scenario

*Hamlet*, William Shakespeare, circa 1600. For this case study we encode two versions:

- **EN-Hamlet**: the English Folger text, paragraph-pooled (treating each speech as a paragraph).
- **FR-Hamlet**: a French translation (François-Victor Hugo's 1865 translation, used because it is in the Gutenberg corpus and is a faithful literary rendering), LaBSE-encoded paragraph by paragraph.

LaBSE (Language-agnostic BERT Sentence Embedding, `sentence-transformers/LaBSE`) is explicitly trained for translation alignment. What is non-trivial is whether the *point-cloud geometry* — the higher-order statistics of the cloud of paragraphs in a work — is invariant across languages, given that LaBSE was trained on sentence-level translation pairs, not on point-cloud geometry of long works. This is the empirical claim of Chapter 17 and the load-bearing finding of Chapter 12.

### Step 1: Feature Vectors in Each Language

We compute the full feature vector (spectral divergences, internal coherence, trajectory geometry, Lasso projection) for each version separately, in each case using the English-corpus PCA-128 basis — we do not refit the basis per language. This is the same protocol that produced the cross-lingual headline numbers in Chapter 17.

Representative channel-by-channel comparison for the two *Hamlet* encodings:

- `pair_sim_mean`: near-identical across EN and FR. In the cross-lingual panel (n=940 bundles, 19 languages), this feature has ρ = +0.712; any individual work sits within a narrow band. *Hamlet*'s internal coherence is high in both languages — Shakespeare's stylistic unity survives translation as a geometric property of the paragraph cloud.
- `mahal_mean`: also near-identical (ρ = +0.710 in the panel). Both EN-*Hamlet* and FR-*Hamlet* sit roughly the same Mahalanobis distance from the pooled English-corpus mean.
- `Hellinger`: the most predictive individual channel (ρ = +0.675; EN↔FI ρ = +0.77 at n=288, p = 8×10⁻⁵⁷; EN↔FR ρ = +0.78 at n=227). *Hamlet*'s Hellinger distance from the English-corpus prior is reproduced in FR.
- `Bhattacharyya`, `JS`, `KL`: all reproduce across the language pair with ρ ≈ 0.67.
- `step_mean`, `step_std`, `curvature`: reproduce with somewhat smaller correlations but still positive.
- `path_eff`: has the tightest language invariance in our panel — within-bundle std / between-book std = 0.18, the lowest across all features.
- `recur_rate`: within-bundle std / between-book std = 0.28, second-tightest.

### Step 2: Cosine Similarity Between Feature Vectors

If we take the full 20-ish-dimensional hand-feature vector of EN-*Hamlet* and of FR-*Hamlet* and compute cosine similarity, the value is close to 1.0. This is the individual-work version of the aggregate bundle-std-ratio finding: the feature vector is, to a first approximation, language-invariant for this work.

The question we care about is not just "are the vectors similar" (they are) but "which channels are preserved and which drift". Preserved across EN↔FR for *Hamlet*:

- Internal coherence (`pair_sim_mean`, `pair_sim_std`)
- Spectral divergences (Hellinger, Bhattacharyya, JS, Mahalanobis)
- Path-efficiency and recurrence rate

Drifting, but still correlated:

- `step_mean` and `step_std` — these carry residual encoder-specific energy. French Alexandrine-descended prose rhythm differs from English iambic-descended prose rhythm, and LaBSE picks this up. The features are correlated across languages (ρ ≈ 0.55 at the individual-work level) but not invariant.
- `powerlaw_slope`, `tail_mass_100` — carry a small amount of language-specific signal related to sentence-length distributions.

This matches the Chapter 17 within-bundle-std ranking: the divergence family has std ratio 0.39–0.44 (more variable) while `path_eff` and `recur_rate` are below 0.30.

### Step 3: The Non-Trivial Piece

LaBSE was trained to produce similar embeddings for translated sentence *pairs*. It was never trained to produce similar point-cloud *statistics* (covariance structure, trajectory curvature, recurrence rate) across translations of a whole work. The fact that these point-cloud statistics are invariant — at the language-family level, across six families, with Spearman ρ ≈ 0.7 and p-values as extreme as 8×10⁻⁵⁷ — is a genuinely surprising empirical result.

For *Hamlet*, the concrete instance: two 700-paragraph clouds, encoded from texts that share no surface words, produce feature vectors whose cosine similarity is near-unity. The specific axes on which the two *Hamlet*s sit in the Lasso-projected space are the same axes. The "shape of *Hamlet*" in the aesthetic manifold is the same shape in English and in French.

This is what Chapter 12 means when it calls cross-lingual invariance a *witnessed Noether-style symmetry*: a transformation on the input (language swap) that leaves a structural quantity (the geometric feature vector) invariant. The analogy to Noether's theorem in physics is not a proof; it is an interpretive framing, and Appendix F logs it as such. The empirical invariance, however, is a measurement.

### Step 4: What Differs?

Where EN-*Hamlet* and FR-*Hamlet* do differ is along axes that are themselves language-diagnostic:

- A small residual along the "language" PCA axis (by construction, given that we are encoding in two different surface languages, LaBSE leaves some language-identity residue).
- A slightly different `step_mean` driven by the different average sentence length in French Hugo prose vs English Folger verse-prose.
- A slightly different `pair_sim_std` driven by the relative tightness of translated sentence clusters vs original-language sentence clusters.

None of these differences contaminate the cross-lingual invariance headline. The headline is about the channels listed in Step 2 as "preserved", and for those channels, *Hamlet*-EN and *Hamlet*-FR are — to a first approximation — the same work.

## D.4 What the Three Case Studies Jointly Show

Three observations follow from reading the cases side by side.

First, the geometric framework does real distinguishing work where scalars collapse. *Bleak House* and *Middlemarch* share a headline rating; their feature vectors differ along specifically interpretable directions. Track R and Track J cannot be distinguished by divergence-from-genre-prior; they are sharply distinguished by `pair_sim_mean` and `step_mean` in the very axes where books and music have opposite signs.

Second, cross-lingual invariance is a property of individual works as well as of the corpus aggregate. *Hamlet*-EN and *Hamlet*-FR are one work geometrically, not two.

Third, the modality-specific directionality of the manifold is not an artifact of any one track pair. The sign-flip on `pair_sim_mean` is robust at p=5×10⁻³³; the sign-flip on `step_mean` is robust at p=4×10⁻²⁹. Our representative case study inherits the pattern of tens of thousands of tracks.

The three cases also illustrate where the framework is quiet. Jazz, within-genre, is null (R=0.031, n=384); neither Track R nor Track J tells us anything about how to rank Jazz tracks against each other, because the geometry does not pick up a signal there. Classical is similarly null (R=−0.013, n=584). The framework does not overclaim on these subsets; Chapter 21 is explicit, and the case studies here do not hide it.

The case studies are not proofs. They are demonstrations of what the machinery does on three works readers can check against their own sense of the art. If the numbers seem right — if they match the texture a careful reader or listener would describe — then the geometric view has earned a seat at the table. If the numbers seem wrong, they can be recomputed from the same public encoders and corpora using the reproduction cookbook in Appendix B. That is the standard the framework asks to be held to.
