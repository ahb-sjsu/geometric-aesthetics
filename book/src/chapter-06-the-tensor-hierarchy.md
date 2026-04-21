# Chapter 6 — The Tensor Hierarchy

**RUNNING EXAMPLE — Hiroshi's Acquisition**

Hiroshi curates a mid-size contemporary art museum. A painter's studio visit has left him with four slides of a new series. He wants to say something more defensible than "I like it" or "it feels important" to his board. The board, skeptical, asks: "important how?" Hiroshi tries to answer. The work, he says, differs from the corpus of contemporary painting in three ways: its palette sits at an unusual point in color-space (first-moment claim about the mean); its internal variation is tighter than typical for its genre, the series is unusually coherent (second-moment claim about the covariance); and it has a distinctive trajectory, moving through its formal possibilities in a non-monotonic way (third-moment claim about sequence structure). He pauses. He does not have these numbers, but he has the *shape* of these numbers. He has been doing tensor aesthetics without knowing it. The board asks for a spreadsheet. Hiroshi realizes that what he has been calling connoisseurship is a mental computation of the first four levels of a tensor hierarchy — and that the computation could, in principle, be made explicit.

Chapter 5 built the stage: the aesthetic manifold $\mathcal{A}$, with a work mapped to a distribution on embedding space, the corpus mapped to a reference Gaussian, and aesthetic distance mediated by divergences on $\mathcal{A}_G$. This chapter populates the stage with the tensor hierarchy: a stack of rank-indexed objects that progressively capture what scalar summaries throw away. The structure mirrors *Geometric Ethics* Ch 6 (satisfaction as $S = I_\mu O^\mu$, a contraction of rank-1 tensors to a scalar), with one crucial difference: where the moral tensor hierarchy rests on a priori nine-dimensional structure, the aesthetic hierarchy is built level-by-level from the empirical shape of the embedding cloud, and its axes are discovered rather than prescribed.

## 6.1 From Scalars to Tensors — Why Rank Matters {#6-1-why-rank}

Recall the argument of Chapter 2: a scalar aesthetic rating — "four stars", "masterpiece", "weak middle" — loses information. It tells us the *magnitude* of the critic's response but not the *direction*. The remedy is to replace scalars with tensors of increasing rank, each preserving more structure:

| Level | Object | What it captures | What it loses |
|------:|:-------|:-----------------|:--------------|
| 1 | scalar + mean vector | Distance from prior; dominant direction | Shape, spread, trajectory, discovered axes |
| 2 | covariance tensor; divergences; coherence | Second-order shape; internal self-similarity | Order, trajectory, axis-specific content |
| 3 | 3-tensor of ordered-sequence features | Trajectory geometry: steps, recurrence, curvature | Structured semantic content on specific axes |
| 4 | learned axis tensor (Lasso on PCA spectrum) | Discovered interpretable style/form axes | Higher-order interactions (pushed to Ch 14) |

The levels form a hierarchy of informativeness, with the scalar rating at the bottom. Information flows downward — higher levels can be contracted to reproduce the scalar — but not upward: no scalar rating reconstructs the covariance, and no covariance reconstructs the trajectory. This is the mathematical content of the complaint that "four stars" loses something: it loses exactly the levels above it.

Each empirical finding in Chapter 17 is located at a specific level. Phase 1's ~8σ divergence signal is Level 2. The 8.4σ internal-coherence signal is a distinct part of Level 2 (coherence is not a divergence from the prior; it is a feature of the work's own covariance, specifically the diagonal vs. off-diagonal structure of the paragraph-to-paragraph similarity matrix). The 3–6σ signal from `step_mean`, `step_skew`, `recur_rate`, and related features is Level 3. The 71 nonzero Lasso coefficients on the 128-d PCA spectrum are Level 4. Each level contributes signal the other levels do not.

## 6.2 Level 1 — The First-Moment Tensor {#6-2-level-1}

### The Mean Vector as a Rank-1 Object

At the bottom of the hierarchy sit the first moments: the mean of the work's embedding cloud, $\hat\mu_W \in \mathbb{R}^d$, and the corpus prior mean $\mu_0 \in \mathbb{R}^d$. The *first-moment displacement* is the vector

$$\delta_W = \hat\mu_W - \mu_0 \in \mathbb{R}^d.$$

This is a rank-1 tensor (a vector) on the ambient embedding space. Its direction encodes *which way* the work differs from the corpus: on which axes of the representation space the work is unusually located. Its magnitude, in Mahalanobis units, encodes *how far*:

$$\|\delta_W\|_{\Sigma_0} = \sqrt{\delta_W^{\top} \Sigma_0^{-1} \delta_W} = D_{\mathrm{Mahal}}(W).$$

The Mahalanobis norm is the Level-1 scalar. It is what a reader who paid attention only to "is this work unusual relative to corpus" would compute. It is not zero — it carries empirical signal on its own — but it is the weakest of the levels in isolation.

### Why Level 1 Alone Is Not Enough

Two novels can have identical $\delta_W$ yet differ radically in shape: one might be a tight book with every paragraph hitting the same note (small $\hat\Sigma_W$), the other a sprawling book with the same *average* location but enormous internal range (large $\hat\Sigma_W$). Level 1 erases this distinction. Level 2 recovers it.

### The Mean Is the Aesthetic Sibling of the Moral Obligation Vector

In *Geometric Ethics* Ch 6, the obligation vector $O^\mu \in T_p M$ lives in the tangent space at a moral situation and has nine components corresponding to the nine moral dimensions. Here, $\delta_W \in \mathbb{R}^d$ lives in the ambient embedding space with no a priori interpretation of its components. Interpretation arrives only after projection into an interpretable basis — the PCA-128 basis, where some axes correspond to genre, some to register, some to narrative mode. This is the first structural difference from the Ethics book: the aesthetic tensor's *components* are not labeled a priori. They are labeled a posteriori, via Lasso discovery (Level 4, Section 6.5).

## 6.3 Level 2 — The Second-Moment Tensor {#6-3-level-2}

### The Covariance as a Rank-2 Object

The covariance matrix $\hat\Sigma_W \in \mathcal{S}^d_{++}$ is a rank-2 symmetric tensor on $\mathbb{R}^d$. It encodes the shape of the work's embedding cloud: the principal axes of variation, the relative spread along each axis, the couplings between axes. As a tensor, it has the transformation law

$$\hat\Sigma_W \mapsto G\, \hat\Sigma_W\, G^{\top}$$

under linear change of basis $G$ — the standard law for a (0, 2)-tensor on $\mathbb{R}^d$.

### Divergences as Level-2 Scalars

The Level-2 scalars are the divergences of Chapter 4 between the work's Gaussian $p_W = \mathcal{N}(\hat\mu_W, \hat\Sigma_W)$ and the prior $p_0 = \mathcal{N}(\mu_0, \Sigma_0)$:

$$D_{\mathrm{KL}}(W \| 0),\quad D_{\mathrm{JS}}(W, 0),\quad H^2(W, 0),\quad D_B(W, 0),\quad \mathrm{TV}(W, 0),\quad D_{\mathrm{Mahal}}(W).$$

In the Phase-1 books experiment (Chapter 17), these divergences each carry approximately 8σ of predictive signal after author-disjoint cross-validation. They are correlated but not redundant. In the Phase-3 cross-lingual experiment, they are also the most *language-invariant* features tested: mean Spearman across language pairs of ρ = +0.675 for Hellinger and Bhattacharyya, ρ = +0.674 for JS, ρ = +0.710 for Mahalanobis-mean. When English readers and Finnish readers rate translations similarly, this is the level at which the agreement is located.

### Internal Coherence — A Second Level-2 Signal

The divergences measure *distance from prior*. There is a second family of Level-2 quantities that measures *internal shape* of the work, independent of any prior. Define the pairwise similarity matrix

$$S_W = \left[\langle \phi(t_i), \phi(t_j)\rangle\right]_{i,j=1}^{N_W},$$

and the *internal coherence* features

$$\text{pair\_sim\_mean}(W) = \frac{1}{\binom{N_W}{2}}\sum_{i<j} S_W[i,j], \qquad \text{pair\_sim\_std}(W) = \operatorname{std}_{i<j}(S_W[i,j]).$$

These are functions of $\hat\Sigma_W$ (for L2-normalized embeddings, $\text{pair\_sim\_mean}$ is directly a function of the trace and the mean magnitude), so they live at Level 2 — but they are a *different contraction* of the second-moment tensor than the divergences. Empirically they carry *8.4σ of signal* in Phase 1, and the signal is not fully explained by the divergences — a regression with all six divergences as covariates leaves `pair_sim_mean` with significant residual predictive power. This is a key empirical observation: Level 2 has at least two qualitatively different contractions — *distance from prior* and *internal self-similarity* — and the aesthetic signal distributes across both.

### The Cross-Modality Sign Flip

One of the book's most striking findings (Chapter 17) is the sign flip of `pair_sim_mean` across modalities:

- **Books:** ρ = +0.126 with rating (8.4σ). Higher internal coherence → *higher* rating.
- **Music:** ρ = −0.076 with log-listens ($p = 5 \times 10^{-33}$). Higher internal coherence → *fewer* listens.

The Level-2 tensor itself is mathematically the same in both cases — a covariance matrix on a $\mathbb{R}^d$ embedding space. But the *aesthetic reward structure* on the manifold is modality-specific: books reward coherence, music rewards contrast. The tensor hierarchy captures the structure; the reward function is an additional (and culturally specific) choice on top. This is one of the places where aesthetic geometry most sharply diverges from moral geometry: the moral manifold's preferred directions are (we argue) cross-culturally invariant at least in structure, while the aesthetic manifold's preferred directions are modality-specific by empirical necessity.

## 6.4 Level 3 — The Trajectory Tensor {#6-4-level-3}

### The Ordered Sequence

Levels 1 and 2 treat the embedding cloud as an unordered bag: $X(W) = \{\phi(t_1), \ldots, \phi(t_N)\}$ with the curly braces indicating no sequence structure. But a work is an *ordered* sequence: the paragraphs of a novel are read in order, the frames of a song are heard in order, the patches of a painting are (for sighted, Latin-script readers) scanned roughly left-to-right and top-to-bottom. The order carries information. Level 3 of the hierarchy captures this.

### Defining the Trajectory Tensor

Consider the sequence of consecutive displacements

$$\Delta_n(W) = \phi(t_{n+1}) - \phi(t_n), \qquad n = 1, \ldots, N_W - 1.$$

The collection $\{\Delta_n\}$ is a sequence of vectors in $\mathbb{R}^d$. The Level-3 tensor is the third central moment of this sequence along with related third-order statistics. Schematically, the Level-3 object is the rank-3 tensor

$$T^{ijk}_W = \frac{1}{N_W - 1}\sum_n (\Delta_n^i - \bar\Delta^i)(\Delta_n^j - \bar\Delta^j)(\Delta_n^k - \bar\Delta^k),$$

where $\bar\Delta$ is the mean displacement. This object is cubically many coefficients in the full embedding space and is not directly useful; we contract it to scalars that have interpretation.

### Trajectory-Feature Contractions

The specific features used in the empirical work are the following scalar contractions of the trajectory tensor (and related objects):

- $\mathtt{step\_mean}(W) = \frac{1}{N-1}\sum_n \|\Delta_n\|$, the average jump size.
- $\mathtt{step\_std}(W) = \operatorname{std}_n \|\Delta_n\|$, the variation in jump size.
- $\mathtt{step\_skew}(W)$, the skewness of the jump-size distribution — a genuine third-moment quantity, and the one most directly corresponding to the rank-3 contraction $T^{ijk}_W$.
- $\mathtt{recur\_rate}(W)$, the fraction of time steps $n$ at which $\phi(t_n)$ is close (within a fixed threshold) to some earlier $\phi(t_m)$ with $m \ll n$ — a recurrence-plot statistic.
- $\mathtt{acf1\_top3}(W)$, the lag-1 autocorrelation of the projection onto the top-3 PCA components.
- $\mathtt{curvature}(W) = \frac{1}{N-2}\sum_n 1 - \cos\angle(\Delta_n, \Delta_{n+1})$, a discrete curvature of the trajectory.
- $\mathtt{path\_eff}(W) = \|\phi(t_{N}) - \phi(t_1)\| / \sum_n \|\Delta_n\|$, the ratio of straight-line distance from start to end to total path length — a path efficiency.
- $\mathtt{powerlaw\_slope}(W)$, the fitted power-law exponent of the step-size distribution tail.
- $\mathtt{tail\_mass\_100}(W)$, the fraction of steps larger than the 99th percentile of the corpus step-size distribution — how often the work "jumps far".

Each of these is a scalar extracted from the ordered sequence. In Phase 1 of the books experiment, each of these carries roughly 3–6σ of independent predictive signal after author-disjoint CV. They are *independent* in a practically important sense: regressing out Level-1 and Level-2 features still leaves substantial Level-3 residual signal.

### What Level 3 Captures That Level 2 Cannot

Two books with identical Gaussian fits — identical means and covariances — can have very different trajectories. One might wander between two tight clusters, giving large $\mathtt{step\_mean}$ and low $\mathtt{recur\_rate}$; the other might meander smoothly, giving small $\mathtt{step\_mean}$ and high $\mathtt{recur\_rate}$. The Level-2 tensor, which is the bag-of-embeddings second moment, cannot tell them apart. The Level-3 features can. This is why the trajectory tensor is a genuine additional level: it extracts information that the first- and second-moment tensors *mathematically cannot encode*.

### Another Cross-Modality Sign Flip

The `step_mean` feature also exhibits a robust cross-modal sign flip in Phase 1 and Phase 4:

- **Books:** ρ = −0.096 with rating (6.4σ). Smaller steps → higher rating. Readers reward continuity.
- **Music:** ρ = +0.071 with log-listens ($p = 4 \times 10^{-29}$). Larger steps → more listens. Listeners reward dynamic contrast.

Again, the tensor is mathematically identical across modalities; the reward direction is modality-specific. The geometry of the hierarchy is universal; the direction of aesthetic preference on the hierarchy is cultural.

## 6.5 Level 4 — The Learned Axis Tensor {#6-5-level-4}

### The Discovered Axes

Levels 1–3 can be computed in closed form from the embedding cloud without any training data. Level 4 cannot. It is the *learned* level: a tensor whose components are discovered by regressing a target variable against the structured features of Levels 1–3 and, crucially, against the spectrum of projections onto the corpus PCA basis.

Concretely: let $U_K \in \mathbb{R}^{d \times K}$ be the top-$K$ PCA basis of the corpus prior, with $K = 128$. Define, for each work, the *projected spectrum*

$$s_W^{(k)} = \frac{1}{N_W}\sum_n (\phi(t_n) - \mu_0)^{\top} u_k \quad \text{for } k = 1, \ldots, K,$$

the mean projection of the work's cloud onto the $k$-th corpus axis. Also define the *spectral variance* $v_W^{(k)} = \operatorname{var}_n\{(\phi(t_n))^{\top} u_k\}$.

Lasso-regressing rating (Phase 1) or log-listens (Phase 4) against $(s_W^{(1)}, \ldots, s_W^{(K)}, v_W^{(1)}, \ldots, v_W^{(K)})$ yields a sparse vector of nonzero coefficients. In Phase 1, 71 of the 256 axes are selected as nonzero. Inspection of the paragraphs loading most strongly on each selected axis reveals interpretable content: one axis separates adventure from romance, another separates dialogue-heavy from exposition-heavy, a third separates archaic from modern diction, a fourth separates first-person from third-person voice, and so on. These are the *discovered style/content/form axes* — the aesthetic-geometry analogues of the moral manifold's nine a priori cells, but bottom-up and data-driven.

### The Level-4 Tensor

Formally, the Level-4 object is the tensor

$$L_W^{(k)} = \beta_k\, s_W^{(k)} \mathbb{1}[\beta_k \neq 0],$$

where $\beta_k$ are the Lasso coefficients and $\mathbb{1}[\cdot]$ is the indicator. The object has support on the 71 selected axes and zero support elsewhere. Its contraction to a scalar,

$$\mathrm{Score}_W = \sum_k \beta_k s_W^{(k)},$$

is the Level-4 prediction. In Phase 1 it contributes to the combined Ridge+Lasso $R = 0.241$ headline. After within-genre control (Phase 2), the residual signal is substantially smaller — 85% of headline $R^2$ was genre confound — but a residualized $R = 0.093$ ($z = 6.5$σ, $p = 5.7 \times 10^{-11}$) remains. The Level-4 tensor carries both the genre signal and, beneath it, a residual "additional aesthetic signal beyond genre" that is load-bearing for the cross-lingual invariance chapter.

### Discovery Versus Prescription

This is the structural respect in which Aesthetics Ch 6 diverges from Ethics Ch 6. The Ethics tensor hierarchy is prescriptive: the nine dimensions of the moral manifold are posited from philosophical considerations (Individual/Relational/Collective × What Matters/Who Decides/What We Know), and the tensors inherit this structure. The Aesthetics tensor hierarchy is *discovered* at Level 4: we do not know, in advance, which PCA axes matter. We fit Lasso, we see what lights up, we interpret it post hoc. The framework is still falsifiable — one could show that no Lasso selection stabilizes across folds, or that the selected axes do not admit interpretation, or that predictive performance does not exceed a baseline — but it is empirical from the bottom up.

Chapter 9 (*The Origin of the Aesthetic Metric — Discovery, Construction, Convention*) returns to this contrast and argues that aesthetic metrics are in part *discovered* (the PCA basis is a genuine property of the corpus), in part *constructed* (which axes we attend to depends on the regression target we chose), and in part *conventional* (which corpus we use as prior is a choice with no natural default).

## 6.6 Contractions and Recovery of Scalars {#6-6-contractions}

### The Scalar Is Recoverable

Given the full tensor hierarchy — Levels 1–4 — the scalar aesthetic score is recoverable by contraction:

$$\hat y_W = \alpha\, D_{\mathrm{Mahal}}(W) + \sum_{d \in \{\text{divs}\}} \beta_d D_d(W) + \gamma\, \mathtt{pair\_sim\_mean}(W) + \sum_{f \in \text{traj}} \delta_f f(W) + \sum_k \epsilon_k s_W^{(k)}.$$

This is a linear contraction of all four levels to a scalar prediction. In Phase 1, fitting the contraction with Ridge+Lasso yields $R = 0.241$ (17σ, $R^2 = 0.058$). It is worth noting what this number *is*: an empirically fit contraction of the aesthetic tensor hierarchy to the rating scalar. The scalar was never the object; it is a projection of the tensor.

### What Contraction Discards

The information that contraction discards is exactly what scalar aesthetics throws away. Two works can have identical $\hat y_W$ while differing in every individual component. A work that scores $\hat y = 0.5$ might be a book that is unusually coherent on a common theme (high `pair_sim_mean`, small divergences), while another work scoring $\hat y = 0.5$ might be an innovative but incoherent book (large divergences, low `pair_sim_mean`). Scalar aesthetics says they are equivalent; the tensor hierarchy distinguishes them precisely, and a reader who wants to know *why* a work is rated as it is requires the tensor, not the scalar.

This is the aesthetic analogue of moral residue (Ethics Ch 15): the contraction to a scalar is mathematically well-defined but lossy, and the loss is not incidental. It is the loss of the directional information that makes aesthetic discourse intelligible.

## 6.7 Why Each Level Is Irreducible to the Others {#6-7-irreducibility}

A natural question: could we dispense with Levels 2, 3, or 4, and compute everything from the rest?

The empirical answer is no. In Phase 1, fitting a model using only Level 1 features yields $R \approx 0.08$; adding Level 2 brings $R$ to $\approx 0.18$; adding Level 3 brings $R$ to $\approx 0.21$; adding Level 4 brings $R$ to $0.24$. Each level adds roughly 0.03–0.10 to $R$, with partial F-tests significant at $p < 10^{-6}$ for each added level. The levels are statistically independent contributors.

The mathematical answer is also no. Level 2 encodes second-moment information that Level 1 (a single vector) cannot represent. Level 3 encodes ordering information that Level 2 (an unordered bag's covariance) cannot represent. Level 4 encodes axis-specific content that the moment hierarchy, at any finite order, averages over. The levels are information-theoretically distinct, not merely different parameterizations of the same content.

## 6.8 The Music-Books Comparison, Tensor by Tensor {#6-8-music-books}

It is worth laying out, level by level, how the tensor hierarchy looks across the two modalities for which we have empirical evidence. This is also a foreshadowing of Chapters 20 and 21.

**Level 1 (first moments).** Books: Mahalanobis-mean is one of the strongest features in Phase 1 and the single most language-invariant in Phase 3 (ρ = +0.710 across language pairs). Music: Mahalanobis-mean is present but less load-bearing; the music signal concentrates at Levels 2 and 4.

**Level 2 (second moments).** Books: divergences each contribute ~8σ in Phase 1; internal coherence `pair_sim_mean` contributes 8.4σ with positive sign (coherent books are rewarded). Music: divergences contribute signal but with saturation issues (Hellinger saturates near 1.0 due to ill-conditioned Gaussian fits on 45 frames in 1024-d; Bhattacharyya is well-behaved and is the preferred metric). `pair_sim_mean` contributes 8σ-equivalent signal but with *negative* sign ($\rho = -0.076$, $p = 5 \times 10^{-33}$; coherent music is listened to *less*).

**Level 3 (trajectory).** Books: `step_mean` and `step_skew` contribute 3–6σ; smaller steps are rewarded. Music: `step_mean` contributes signal with *positive* sign (larger steps → more listens, $\rho = +0.071$, $p = 4 \times 10^{-29}$); the sign flip is robust at $p < 10^{-28}$ and is one of the book's most striking findings.

**Level 4 (discovered axes).** Books: 71 nonzero Lasso axes on 128-d PCA spectrum; axes separate romance/adventure, first-/third-person, dialogue/exposition. Music: Lasso on the PCA spectrum yields a raw $R = 0.302$ ($z = 49.8$σ) that collapses to $R = 0.177$ ($z = 28.3$σ) after genre residualization — but still beats hand features and vastly beats Spotify's 8 acoustic features (MERT vs. Spotify bootstrap difference $p = 0.001$ on shared $n = 5{,}233$). The discovered axes correspond to genre and instrumentation.

The tensor hierarchy is mathematically identical across the two modalities; the *direction* of the aesthetic reward at each level — which way on each tensor the audience prefers — is modality-specific. The framework supplies the structure; empirical measurement supplies the direction. This is one reason the framework does not collapse into the scalar aesthetics it replaces: the sign of the tensor's contribution is part of the result, and no scalar rating can preserve a sign flip.

## 6.9 Bridge {#6-9-bridge}

Chapter 6 has built the tensor hierarchy: four levels stacked on the aesthetic manifold of Chapter 5, each extracting information the others cannot, each documented empirically in Chapter 17. Chapter 7 applies the hierarchy to a single work — *Moby-Dick* in five levels (including a Level 0 for scalar rating, for contrast) — so the reader can see the four channels computed on a specific famous book. Chapter 8 develops stratification: where and how the smooth structure of the manifold breaks down at genre boundaries, where the Level-4 Lasso axes change their selection, where the cross-modal sign flips occur. Chapter 12 returns to the question of invariance: the Level-2 divergences and the Level-3 trajectory features are the quantities that, as Chapter 17 documents, transfer across languages with Spearman ρ ≈ 0.7, a symmetry-invariance witnessing of a strength no scalar aesthetic theory has ever produced. The tensor hierarchy is the mathematical object that makes this invariance visible; the empirical chapter ratifies that the object is not a formal curiosity but a real feature of aesthetic data.
