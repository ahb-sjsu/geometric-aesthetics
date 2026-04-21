# Chapter 5 — The Aesthetic Manifold

**RUNNING EXAMPLE — Daniel's Mixtape**

Daniel is a music producer with a recommendation problem. He has ten thousand 30-second clips and a request from a streaming partner to predict, for each clip, how many plays it will earn in its first month. The partner has sent him Spotify's acoustic feature set — danceability, energy, valence, tempo, eight numbers per track — and asked him to fit a Ridge regression. He does. It explains 1% of the log-listen variance. He repeats the exercise with MERT embeddings: 1,024-dimensional hidden states at 45 time steps per clip, a cloud of 46,000 numbers per song. He does not know what to do with a cloud. His instinct is to average: take the mean of the 45 time steps, feed the single 1,024-vector to Ridge. It works somewhat better. Then his collaborator suggests he also compute the covariance of the 45 time steps, the divergence from the corpus mean, and something called *step skewness* — the third moment of the sequence of frame-to-frame jumps. The cloud, it turns out, has shape. A song whose frames cluster tightly around their mean is doing something categorically different from a song whose frames spread wide, or whose spread is asymmetric, or whose frame-to-frame trajectory has a particular recurrence statistic. Daniel begins to suspect that the eight-number Spotify feature set is not a summary of the song — it is a *projection* of the song onto an eight-dimensional subspace, and the projection has thrown most of the information away.

Daniel's mistake is one we will diagnose formally in this chapter. An aesthetic object is not a point, and an aesthetic feature is not a single number. A work lives on a *manifold* whose points are distributions in embedding space, and whose structure — means, covariances, trajectories, spectra — supports tensors of increasing rank that progressively recover what the scalar summary lost. Chapter 4 gave us the geometric toolkit. This chapter uses it to build the stage.

## 5.1 The Question of Base Space {#5-1-base-space}

Every tensor lives on a manifold. The stress tensor lives on the manifold of spatial points in a body; the metric tensor of general relativity lives on spacetime; the moral manifold of *Geometric Ethics* (Chapter 5 of that volume) lives on the space of structured moral situations. For geometric aesthetics the question is parallel: what is the manifold on which aesthetic tensors are defined?

The question is not a technicality. The choice of base space determines what counts as a point in aesthetic reasoning, what counts as a direction — a tangent vector — in aesthetic change, what it means for two works to be aesthetically close or far apart, what transformations (change of language, change of encoder, change of corpus reference) leave aesthetic judgment invariant, and where the smooth structure breaks down at genre boundaries and style thresholds.

We proceed by candidates, mirroring Ethics Ch 5.

### Candidate 1 — Works as Points

The obvious choice is to make the base space the space of works and let each work be a point. It is wrong, and its wrongness is instructive. A work is not a point because a work has *internal variation*: paragraphs, scenes, frames, phrases, patches. The aesthetic character of *Moby-Dick* is not located at any single paragraph; it is distributed across the paragraphs and carried by their statistical shape — the range of registers, the oscillation between narrative and taxonomy, the recurrent return to the white whale. Treating a work as a point discards exactly this structure.

### Candidate 2 — Tokens as Points

The opposite extreme: let the base space be the space of tokens, frames, patches — the atomic units an encoder operates on. A paragraph of *Moby-Dick* is a point in $\mathbb{R}^{768}$ under LaBSE; a 30-second clip's $20\text{ms}$ frame is a point in $\mathbb{R}^{1024}$ under MERT. This is the right space for individual tokens, but it is the wrong space for the work: tokens are the atoms, not the organisms. A work is the collection.

### Our Choice — Distributions as Points

We take the aesthetic manifold to be the space of *distributions* over the embedding space. A work is a distribution; the corpus is a distribution; a genre is a distribution; a style is a distribution. This is the natural home for the objects of aesthetic reasoning, and it has well-developed Riemannian geometry (Chapter 4, §4.4–4.5).

**Definition 5.1 (Aesthetic manifold, informal).** *The aesthetic manifold $\mathcal{A}$ is a space whose points are probability distributions $p$ on a modality-specific embedding space $\mathbb{R}^d$. A work $W$ is represented by the distribution $p_W$ induced by its embedding cloud $X(W)$. The corpus is represented by a reference distribution $p_0$. Distances on $\mathcal{A}$ are given by the divergences of Chapter 4.*

The manifold $\mathcal{A}$ is infinite-dimensional in full generality. For tractability, and consistent with the empirical pipeline used throughout this book, we restrict attention to the *Gaussian submanifold* $\mathcal{A}_G \subset \mathcal{A}$:

$$\mathcal{A}_G = \{\,\mathcal{N}(\mu, \Sigma) : \mu \in \mathbb{R}^d,\; \Sigma \in \mathcal{S}^d_{++}\,\},$$

a finite-dimensional manifold of dimension $d + d(d+1)/2$ under the Fisher information metric. The residual non-Gaussianity — skewness, multi-modality, heavy tails — is not discarded; it is pushed into the higher-rank tensors of Chapter 6 (Level 3: trajectory geometry, which uses third and fourth moments of frame-to-frame jumps). The Gaussian submanifold captures the first two moments exactly; the tensor hierarchy captures the rest.

## 5.2 The Embedding Cloud {#5-2-embedding-cloud}

### From Work to Cloud

A work $W$ is a sequence of atomic units: paragraphs for a novel, seconds for a song, patches for an image. An encoder $\phi : \mathcal{T} \to \mathbb{R}^d$ maps each unit to a vector. The work is the cloud

$$X(W) = \{\phi(t_1), \phi(t_2), \ldots, \phi(t_{N_W})\} \subset \mathbb{R}^d.$$

Concretely, for a 300-paragraph novel encoded by LaBSE, $X(W)$ is 300 points in $\mathbb{R}^{768}$. For a 30-second clip encoded by MERT at 1.5Hz frame rate, $X(W)$ is 45 points in $\mathbb{R}^{1024}$. For a 224×224 image encoded by DINO with 14×14 patches, $X(W)$ is 196 points in $\mathbb{R}^{768}$.

**Modality choices in this book.**

- Text: LaBSE (`sentence-transformers/LaBSE`), 768-d, language-agnostic by construction.
- Music: MERT (`m-a-p/MERT-v1-330M`), 1024-d, layer-7 hidden states, 160k hours SSL pretraining.
- Images: CLIP ViT-L/14 or DINO-v2 (framework-compatible; empirical chapters report on text and music).

The choice of encoder is a modeling choice, not a discovery. The framework is encoder-agnostic: any encoder that produces a sensible distributional representation of tokens can play the role of $\phi$. The empirical claims of Chapter 17 depend on the specific encoders; the geometric framework does not.

### What the Cloud Inherits from the Encoder

The cloud's shape depends on the encoder. LaBSE embeddings are L2-normalized and live on the unit sphere $S^{767}$ rather than in the full $\mathbb{R}^{768}$. MERT hidden states are not normalized; they have a natural magnitude scale. CLIP image embeddings are normalized by convention in most applications. These conventions matter: a Gaussian on the sphere is not the same as a Gaussian in the ambient; a divergence between Gaussians on the sphere must be computed with care (we project into the tangent space at a reference point, fit Gaussians there, and compute divergences in the tangent).

In practice, for LaBSE we work in the PCA-128 basis of the prior corpus; the PCA projection both reduces dimensionality and effectively flattens the sphere locally, making the Gaussian approximation defensible. For MERT we work in the raw 1024-d space and accept that Gaussian fits are ill-conditioned for short clips (45 frames in 1024 dimensions is badly under-sampled), which is why we re-fit in a $K = 32$ PCA subspace for the music experiments of Chapter 21. The framework is robust to these choices; the divergences are not always, and the Hellinger saturation observed in music (Chapter 17) is a direct consequence.

## 5.3 Mean, Covariance, and What They Mean Aesthetically {#5-3-mean-cov}

### The First Moment

The mean $\hat\mu_W = \frac{1}{N_W}\sum_n \phi(t_n)$ is the *centroid* of the work in embedding space. Aesthetically, the mean captures the *dominant thematic location* of the work: where, on average, the work sits relative to the corpus. Two novels with very different plots may have nearby means if they share voice, register, and subject matter. Two songs in the same genre but with radically different dynamics may have nearby means.

The Mahalanobis distance of the mean from the prior,

$$D_{\mathrm{Mahal}}(W) = \sqrt{(\hat\mu_W - \mu_0)^{\top}\Sigma_0^{-1}(\hat\mu_W - \mu_0)},$$

is the *distance-from-prior* at the level of first moments. It measures, in prior-normalized units, how unusual the work's centroid is. In Phase 3 of the empirical work (cross-lingual, Chapter 17), the Mahalanobis-mean feature is the single most language-invariant of all hand-features tested, with a mean Spearman correlation across language pairs of ρ = +0.710. When Finnish readers and English readers rate translations of the same book similarly, this is one of the features on which they agree.

### The Second Moment

The covariance $\hat\Sigma_W = \frac{1}{N_W - 1}\sum_n (\phi(t_n) - \hat\mu_W)(\phi(t_n) - \hat\mu_W)^{\top}$ captures the *aesthetic range* of the work: how far the work wanders from its centroid, in which directions, and with what orientation. A work with a large top eigenvalue of $\hat\Sigma_W$ has a dominant axis of variation — the narrative oscillates along one primary dimension (the high seas and the whale; the verse and the chorus). A work with a flat spectrum has no dominant axis; the variation is uniform across directions.

The trace $\operatorname{tr}(\hat\Sigma_W)$ is the total variance. The log-determinant $\ln|\hat\Sigma_W|$ is the *differential entropy* of the fitted Gaussian up to a constant, and is sensitive to shape: two works with the same total variance can have very different log-determinants if their eigenvalue distributions differ.

The divergences of Chapter 4 combine first and second moments into single scalars measuring distance between the work and the prior on $\mathcal{A}_G$. Each divergence emphasizes a different aspect (KL is asymmetric and sensitive to support mismatch; Hellinger is bounded and symmetric; Bhattacharyya is stable in ill-conditioned regimes), and the four used together carry ~8σ signal in the Phase-1 books experiment (Chapter 17).

## 5.4 The Corpus Prior {#5-4-prior}

### A Reference Point

An aesthetic judgment is always a judgment *relative to something*. Critics who claim to evaluate a work "in itself" are, when pressed, found to be evaluating it against an implicit body of expectation — prior work in the tradition, the reader's past reading, the listener's formed taste. The geometry makes this explicit: we need a reference distribution $p_0$ against which $p_W$ is measured.

For Phase 1, $p_0$ is fitted on the pooled paragraphs of 4,998 Gutenberg novels matched against Goodreads ratings. For Phase 3, the cross-lingual study, $p_0$ is the *same English* prior — the non-English books are projected into the English-corpus PCA basis and compared against the English prior, not re-centered per language. This is the methodologically load-bearing choice of the book: we treat the English corpus as a frozen reference frame, and we see how far into other languages the invariance of aesthetic features extends.

### Why a Gaussian Prior?

$p_0$ could in principle be any distribution. We use a multivariate Gaussian for the prior for the same reasons we use one for the work: closed-form divergences, tractable statistics, principled approximation to the first two moments. The Gaussian choice is a modeling decision; its adequacy is empirical. If a non-Gaussian prior (a Gaussian mixture, say) yielded more robust invariance, we would use it. So far, the Gaussian prior is sufficient for the effects we document.

### Choice of Corpus Matters

The prior is not neutral. A prior fitted on English novels puts classical Chinese texts at a Mahalanobis distance that reflects both their translation status and the historical fact that English literary forms differ from classical Chinese ones. This is not a bug; it is the content of the framework. The "Sinitic corpus gap" noted in Chapter 17 — only 5 bundles forming for Chinese Gutenberg texts, because the Chinese corpus is classical originals (Confucius, Sunzi, the *Shijing*) rather than translations of Western works — is not a failure of the framework but a direct consequence of the prior choice. Change the prior to a Chinese literary prior and the distances rearrange. The *relational* structure — which works are near which others, on which axes — is what the framework delivers; the absolute distances depend on the reference point.

## 5.5 The Aesthetic Metric {#5-5-aesthetic-metric}

### The Fisher Information Metric

On the Gaussian submanifold $\mathcal{A}_G$, there is a canonical Riemannian metric: the Fisher information metric. For a parametric family $p_\theta$, its components are

$$g_{ab}(\theta) = \mathbb{E}_{p_\theta}\!\left[\frac{\partial \log p_\theta}{\partial \theta^a}\,\frac{\partial \log p_\theta}{\partial \theta^b}\right].$$

For Gaussians parameterized by $(\mu, \Sigma)$ the Fisher metric decomposes: the mean part is the Mahalanobis metric $g^\mu_{ij} = (\Sigma^{-1})_{ij}$, and the covariance part is the affine-invariant metric on $\mathcal{S}^d_{++}$ discussed in Chapter 4. The KL divergence of Chapter 4 is, locally, a second-order approximation to Fisher distance.

### What the Metric Encodes

For the aesthetic manifold, the metric encodes *how much a unit displacement matters*. In regions of $\mathcal{A}$ where the prior is concentrated — near the corpus centroid — a small Euclidean displacement corresponds to a large aesthetic displacement, because the prior is tightly sampled. In thin regions of the prior, the same Euclidean step is aesthetically smaller. This is the content of measuring in Mahalanobis units: we normalize by the local prior variance.

### Axes Discovered From Data

Where the moral manifold of *Geometric Ethics* has a priori valence axes (Individual/Relational/Collective × What Matters/Who Decides/What We Know), the aesthetic manifold does not. We do not start with nine known dimensions; we *discover* the relevant axes from data. In Phase 1, Lasso on the 128-d PCA spectrum yields 71 nonzero axes. Inspection of the paragraphs loading most positively and most negatively on each axis reveals interpretable content: romance vs. adventure, first-person vs. third-person, dialogue-heavy vs. exposition-heavy, archaic vs. modern diction, and so on. These are the *discovered style/content/form axes* — the aesthetic analogues of the moral manifold's nine cells, but derived bottom-up from corpus statistics rather than top-down from philosophical taxonomy.

This is a methodological commitment with consequences. The moral manifold rests on the claim that the nine cells exhaust moral space; that claim is falsifiable but a priori. The aesthetic manifold rests on the claim that the axes Lasso discovers are the relevant ones; that claim is also falsifiable — by showing that some aesthetically relevant distinction is not captured by any Lasso-selected axis — and is empirical from the ground up. Chapter 9 (*The Origin of the Aesthetic Metric*) returns to this contrast.

## 5.6 Aesthetic Distance {#5-6-aesthetic-distance}

### Distance Between Two Works

Given two works $W_1$ and $W_2$ with fitted Gaussians $p_{W_1}, p_{W_2}$, the aesthetic distance between them is the divergence $D(p_{W_1}, p_{W_2})$ for some choice of $D$. The six divergences of Chapter 4 each give a slightly different answer; the book uses all six and treats them as independent probes.

**A worked example (schematic).** Consider two novels $A$ and $B$ with mean embeddings $\mu_A, \mu_B$ at cosine similarity 0.95 (very close centroids), but covariances with $D_B(\Sigma_A, \Sigma_B)$ large. Standard "nearest-neighbor in embedding space" retrievers would declare them similar. The Bhattacharyya distance between the fitted Gaussians declares them dissimilar. Readers who have read both novels report that they share subject matter but differ radically in form. The covariance divergence captures what the mean-only similarity misses.

### Distance From the Prior

The distance $D(p_W, p_0)$ — how unusual a work is, relative to the corpus — is the single most empirically important quantity in the book. It is the Level 1/Level 2 tensor contraction of Chapter 6, and it carries 8σ signal in Phase 1. Interpretively, a work at large $D(p_W, p_0)$ is either innovative or anomalous; distinguishing these is a direction-rather-than-magnitude question, which is why the vector-valued mean displacement $\hat\mu_W - \mu_0$ matters in addition to its scalar Mahalanobis norm.

### The Asymmetry of Novelty

KL is asymmetric: $D_{\mathrm{KL}}(p_W \| p_0) \neq D_{\mathrm{KL}}(p_0 \| p_W)$. The first quantity — how surprising the work is under the prior — measures the work's *information content* relative to expectation. The second — how surprising the prior is under the work — measures how much the prior would have to be *updated* to accommodate the work. Aesthetic novelty is closer to the first; aesthetic influence is closer to the second. Chapter 10 (*Aesthetic Dynamics*) develops this asymmetry.

## 5.7 The Per-Work Gaussian Is an Approximation {#5-7-approximation}

### Non-Gaussianity in Practice

Embedding clouds are not Gaussian. They are:

- **Heavy-tailed.** Rare passages, surprising moments, unusual phrases live in the tails.
- **Multi-modal.** A novel alternating between two narrators has a bimodal cloud.
- **Anisotropic in ways a Gaussian captures only coarsely.** The top few PCA axes carry most of the variance; the residual is non-Gaussian structure.

We embrace this. The Gaussian fit captures the first two moments exactly — and that is already enough for 8σ + 8.4σ of signal (Chapter 17). The residual non-Gaussianity is captured by higher-rank tensors:

- **Third moments** (skewness of frame-to-frame jumps) → `step_skew` feature (3–6σ, Level 3).
- **Return-map structure** (does the cloud revisit regions of embedding space?) → `recur_rate` feature.
- **Path geometry** (is the trajectory efficient, meandering, curvature-laden?) → `curvature`, `path_eff`.

This is the rationale for the tensor *hierarchy* of Chapter 6: each level adds information that the previous levels cannot represent. The Gaussian is not the endpoint; it is Level 2 of a four-level stack.

### What Gaussian Fits Miss

A Gaussian fit cannot distinguish a novel whose paragraphs form two tight clusters from one whose paragraphs form a single wider cluster with the same covariance. A moment-matching Gaussian fits both identically. The trajectory features of Level 3 distinguish them: the bimodal novel has a low `recur_rate` (paragraphs do not return to the other cluster from within the first) and a bimodal `step_mean` distribution (jumps within a cluster are small, jumps between clusters are large). The Gaussian has erased a distinction that mattered; the third-order tensor recovers it.

## 5.8 Foreshadow — The Four Channels {#5-8-four-channels}

The aesthetic manifold supports four structural channels of the tensor hierarchy developed in Chapter 6, each extracting signal the others cannot:

- **Level 1 (scalar, first moments).** Mean direction $\hat\mu_W - \mu_0$ and its Mahalanobis norm. Captures: how far, and in what direction, the work's centroid sits from the corpus.
- **Level 2 (rank-2 tensors, second moments).** Covariance $\hat\Sigma_W$ and its divergences from $\Sigma_0$; internal coherence features (`pair_sim_mean`, `pair_sim_std`) which measure how tightly the cloud clusters around its own mean. Captures: the work's shape and its shape-distance from the prior.
- **Level 3 (rank-3 tensor, trajectory geometry).** Features computed on the ordered sequence $(\phi(t_1), \phi(t_2), \ldots, \phi(t_N))$: step statistics, recurrence, curvature, power-law tails. Captures: what a time-ordered or sequence-ordered reading reveals that the unordered bag-of-embeddings misses.
- **Level 4 (learned, discovered axes).** Lasso on the 128-d PCA spectrum discovers interpretable genre/form axes. Captures: structured content that does not reduce to first/second/third moments.

Each channel's empirical contribution is documented in Chapter 17: Level 2 divergences at ~8σ per divergence family; internal coherence at 8.4σ (a distinct signal from the divergences); Level 3 trajectory features at 3–6σ; Level 4 Lasso with 71 nonzero axes in the books experiment. The channels are *independent contributions to the aesthetic signal*, which is the empirical justification for the tensor hierarchy.

## 5.9 Stratification, Foreshadowed {#5-9-stratification}

A last point of structure before the bridge. The aesthetic manifold $\mathcal{A}$ is not homogeneous. Different regions of the manifold support different local structure: the region occupied by 19th-century English novels is densely sampled and has tight local metric; the region occupied by classical Chinese texts is sparsely sampled and, relative to an English prior, pathologically far. These regions are *strata* — pieces of the manifold where the local geometry is effectively constant, separated by *boundaries* where the local geometry changes abruptly.

Genre is a stratification. Style is a finer stratification. Period is another. The empirical work of Phase 2 (Chapter 17) — the within-genre control that revealed 85% of the Phase-1 headline $R^2$ was genre confound — is a direct consequence of the manifold's stratified structure: a model that does not respect the stratum boundaries picks up cross-stratum variance (genre effects) that is larger than within-stratum aesthetic signal, and reports an inflated $R^2$. The same phenomenon is even more pronounced in music (Phase 4: 91% of hand-feature $R^2$ is genre confound). Respecting the stratification — fitting within-stratum models, or residualizing genre before reporting signal — is a methodological requirement the framework itself imposes.

Chapter 8 develops the formal theory of aesthetic stratification, using the Whitney-stratified-space machinery that *Geometric Ethics* Chapter 4 used for moral manifolds. The point here is to foreshadow: when Chapter 17 reports that within-genre residualized $R$ is 0.093 ($z = 6.5$σ, $p = 5.7 \times 10^{-11}$) against a headline Phase-1 $R$ of 0.241, this is not a deflation of the theory; it is the framework *correctly locating* where the signal lives. It lives on the stratum, not on the unstratified manifold. The honest reframe — "additional aesthetic signal beyond genre", not "geometry predicts rating" — follows from the stratified geometry.

## 5.10 Bridge {#5-10-bridge}

Chapter 5 has established the stage: the aesthetic manifold $\mathcal{A}$, with its points (distributions), its metric (Fisher, with the Mahalanobis and affine-invariant components), its reference point (the corpus prior), and its dimensional structure (axes discovered, not prescribed). Chapter 6 populates the stage with the tensor hierarchy: four levels, each stacking on top of the previous, each encoding a kind of aesthetic structure the previous cannot capture. Chapter 7 shows the hierarchy applied to a single work — *Moby-Dick* as a case study in five levels. Chapter 17 delivers the empirical evidence that the hierarchy is not a formal curiosity but carries independent signal at each level. The geometric stage is set; the tensors are ready to be raised upon it.
