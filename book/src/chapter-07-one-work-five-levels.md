# Chapter 7: One Work — Five Levels

**RUNNING EXAMPLE — Elena's Review**

Elena, a philosopher-critic who has spent the better part of a decade writing about algorithmic curation, is asked by an editor at the *Times Literary Supplement* to produce a short assessment of Dickens' *Bleak House*. She has three thousand words and a deadline. She has also — because of the project we are writing about in this book — a five-level tensor decomposition of the novel sitting in a parquet file on her laptop. The review she files will not cite the tensor. But the tensor, as she discovers over the course of a week, organises her prose. At Level 0, *Bleak House* is a 4.05 on Goodreads. At Level 1, its mean LaBSE embedding sits 1.4 standard deviations from the corpus prior: further than typical, but not estranged. At Level 2, its internal coherence (`pair_sim_mean = 0.412`) is unusually high for its length; its spectral divergences from the corpus prior are correspondingly moderate. At Level 3, the paragraph-trajectory recurs — its `recur_rate` is large, its `path_eff` low — the novel doubles back. At Level 4, it loads heavily on two of our seventy-one Lasso-discovered axes: one that behaves like "Victorian social-realist" and one that behaves like "epistolary interleave." Each level answered a question Elena had been circling for years. None of them, individually, gave her the review. Together, they gave her the structure of one.

## Introduction: The Pedagogy of Accumulation {#introduction}

The preceding chapters have developed geometric aesthetics in abstract terms: the manifold of Chapter 5, the tensor hierarchy of Chapter 6, and the mathematical preliminaries of Chapter 4. This chapter takes a different approach, parallel to Chapter 7 of the sibling *Geometric Ethics* volume ("One Case — Five Levels"). We pick one work and revisit it five times, adding structure at each pass. The work is Charles Dickens' *Bleak House* (1852–53), an English novel of roughly three hundred and sixty thousand words, narrated in two voices — an omniscient present-tense narrator and the retrospective first-person Esther Summerson — telling a fog-bound story of an interminable Chancery suit, a hidden mother, and a spontaneously-combusting rag-and-bottle merchant. We chose *Bleak House* because it is canonical enough that most readers have some intuition for its shape, structurally unusual enough that every level of our tensor reveals something different, and long enough that trajectory statistics are well-sampled.

The pedagogic claim of this chapter is the same as its sibling in Ethics: no single number can collapse the levels. Each level answers a different aesthetic question. If we care about aesthetic evaluation at all, we need the whole stack.

## Level 0: The Scalar — A 4.05 {#level-0-scalar}

### What the Number Says

Goodreads users have rated *Bleak House* 4.05 out of 5 across many tens of thousands of ratings. This is Level 0 of our tensor hierarchy: a (0,0)-tensor, a pure scalar, the endpoint of the evaluative computation. It is what most readers, most editors, most recommender systems, and most book-club interfaces will tell you about the novel.

The 4.05 is not meaningless. It is a summary statistic over a large, self-selected population of readers who have engaged with the book and returned to the platform to register a verdict. It carries information. It tells us that, on average, readers who finished or partly finished *Bleak House* liked it more than they liked the median rated book on the platform. It tells us that *Bleak House* is more admired than *The Old Curiosity Shop* (3.82) and less so than *Great Expectations* (3.79 — which complicates the "more admired" reading already) and nearly tied with *David Copperfield* (4.04). In its direct neighbourhood, the scalar distinguishes.

### What the Number Cannot Say

What the scalar cannot say is what the admiration consists of. It cannot say whether readers love the Chancery satire and tolerate the Esther passages, whether they love the Esther passages and tolerate the Chancery satire, or whether the coupling of the two is itself the object of admiration. It cannot distinguish readers who admire *Bleak House* for its form from readers who admire it for its moral weather. It cannot locate the book in any space — cannot tell us whether 4.05 is the same kind of number for *Bleak House* as 4.05 is for *Middlemarch* (4.03) or for *Jane Eyre* (4.13). It cannot be differentiated. You cannot take the gradient of a one-dimensional landmark.

The scalar is the (0,0)-tensor — the endpoint. The failure of scalar aesthetics, laid out in Chapter 2, is that it makes the endpoint the beginning. A reviewer who begins with "4.05" has already collapsed the structure of the novel before examining it. The tensor hierarchy we build in the following sections is designed to delay that collapse until it can be examined, and only collapse once the structure is visible.

There is one important honest caveat before we proceed. In the empirical programme reported in Chapter 17, we found that roughly eighty-five percent of our rating-predictive signal was genre confound — that is, our models mostly learned what genre looked like on the manifold, and the within-genre aesthetic residual was modest (R = 0.093, n = 4,998, p = 5.7×10⁻¹¹). The Goodreads rating is therefore not a clean signal about aesthetic quality. It is a partly-sociological artefact. We will return to this in Chapter 9. For now it is enough to note: the 4.05 is the scalar we have, not necessarily the scalar we want.

## Level 1: The Vector — A Mean Embedding and a Distance {#level-1-vector}

### Adding Structure

Instead of collapsing *Bleak House* to a single number, we can represent it as a vector. The representation we use throughout this book is a paragraph-level LaBSE embedding: each paragraph of the novel is encoded as a 768-dimensional vector in a multilingual sentence-embedding space. For the Level 1 view, we take the mean of these paragraph vectors:

$$\bar{v}_{\text{BH}} = \frac{1}{N} \sum_{i=1}^{N} v_i$$

where $v_i \in \mathbb{R}^{768}$ is the embedding of paragraph $i$ and $N \approx 8{,}400$ for *Bleak House*. We compare $\bar{v}_{\text{BH}}$ to the corpus prior $\bar{v}_{\text{corpus}}$, the mean of all paragraph embeddings across our 4,998-book Gutenberg↔Goodreads corpus. The distance

$$d_{\text{prior}}(w) = \|\bar{v}_w - \bar{v}_{\text{corpus}}\|_2$$

measures how far the book's mean representation sits from the typical book on the manifold. For *Bleak House*, this distance, standardised against the distribution of `d_prior` across the corpus, is roughly 1.4σ. Not an outlier. Further from the centre than most books, but within the main body.

### What the Vector Can Say

The vector already says things the scalar could not. It says that *Bleak House*, considered as a cloud of paragraphs, has a centroid that is not average. It sits noticeably to one side of the manifold's centre. If we project $\bar{v}_{\text{BH}}$ onto the top PCA axes of the corpus (the 128-dimensional spectrum basis used throughout our work), we can read off which corpus-wide axes it loads on: a strong component on an axis that tracks nineteenth-century English prose, a negative loading on an axis that separates non-fiction from fiction, a moderate loading on an axis that tracks high-lexical-variety narrative.

Crucially, the vector supports dominance and trade-off reasoning. Two books with the same rating but very different mean-vector positions are doing different things. The scalar cannot see this; the vector must.

### What the Vector Cannot Say

What the vector cannot say — and where our empirical work in Chapter 17 becomes load-bearing — is *how* the paragraphs are distributed around their mean. The mean is a single point. It ignores dispersion, shape, correlation, and sequence. A Dickens novel and a hypothetical "Dickens paragraphs in uniformly random order" would have, up to sampling, the same mean vector. They would also have the same Level-1 distance from the corpus prior. They would not be the same book. The Level-1 view is a one-point summary in a space that is, in reality, a cloud of many thousands of points. We need Level 2.

## Level 2: The Rank-2 View — Divergence and Internal Coherence {#level-2}

### Two Channels

At Level 2, we stop treating the book as a point and start treating it as a distribution. Two families of statistics emerge naturally, and both were empirical finds of Phase 1 of our programme (see Chapter 17 for the full methodology).

**Channel A: Spectral divergences from the corpus prior.** We fit a Gaussian to the paragraph cloud of *Bleak House* in a PCA-128 subspace, and another to the corpus prior. We then compute a suite of divergences: Kullback–Leibler, Jensen–Shannon, Hellinger, Bhattacharyya, total-variation, and the Mahalanobis distance of means. Each of these captures how far the book's *distribution* sits from the corpus's. For *Bleak House*, the Hellinger is moderate-to-high, the JS is moderate, and the Mahalanobis-of-means is large. Each divergence channel gave us a ~8σ signal against rating in our Phase-1 analysis.

**Channel B: Internal coherence.** We also compute the mean pairwise cosine similarity between paragraphs inside the book, `pair_sim_mean`, and its standard deviation, `pair_sim_std`. This is the channel that most surprised us when it appeared: internally, some books look like a single region of embedding space, revisited paragraph after paragraph; others look like a walk through many regions. `pair_sim_mean` is a measure of how much the book sounds like itself. For *Bleak House*, `pair_sim_mean` is elevated relative to median — the book is internally coherent at the paragraph level, which is something one might not have guessed from reading the novel straight through, with its wildly different narrators.

In books, higher internal coherence predicts higher rating (ρ = +0.126, 8.4σ in Phase 1). In music, the same statistic predicts *fewer* listens (ρ = −0.076, p = 5×10⁻³³). This cross-modality sign flip is one of the central empirical findings of the project, and we return to it in Chapter 21. For the present chapter, the point is geometric: coherence is a distinct axis from divergence. Books can be internally tight and far from the prior (*Bleak House* is), internally loose and close to the prior (much pulp fiction is), or any other combination.

### What the Rank-2 View Can Say

Level 2 tells us something Level 1 structurally cannot. It says that *Bleak House*, whose mean sits 1.4σ from the corpus prior, is also a book whose paragraphs look very much like each other — surprisingly much, given the dual narrators. It says the cloud is tight. The divergence-from-prior and the internal-coherence numbers together locate the book in a two-dimensional sub-space of the aesthetic manifold where we can now ask: which *other* books are in this quadrant? The answer is informative — a cluster of Victorian three-deckers with multiple narrators but a strong unifying authorial voice, including *Middlemarch* and *Vanity Fair*.

### What the Rank-2 View Cannot Say

What it cannot say is anything about sequence. The coherence statistic `pair_sim_mean` is invariant under permutation of the paragraphs. It does not care what order Dickens put them in. Neither do the divergences, which are distributional. If we shuffled *Bleak House*'s paragraphs uniformly at random, every Level-2 number in this section would be, up to sampling, unchanged. A reader of the shuffled book would not have the same experience. To see the difference, we need Level 3.

## Level 3: The Trajectory — Step, Curvature, Recurrence {#level-3}

### The Paragraph Trajectory

At Level 3, the book is no longer a cloud. It is a path — a sequence of points $v_1, v_2, \ldots, v_N$ in embedding space, in the order the author wrote them. From this trajectory we extract a family of statistics, developed in Chapter 6 and in our Phase-1 results.

The step statistics — `step_mean`, `step_std`, `step_skew` — measure the sizes of consecutive jumps $\|v_{i+1} - v_i\|$. For *Bleak House*, `step_mean` is noticeably smaller than the corpus median: paragraph-to-paragraph, the book moves slowly in embedding space. `step_skew` is positive: most steps are small, but occasional large jumps occur — these align, on inspection, with the narrator-switches between the omniscient present-tense voice and Esther's retrospective first-person. The dual-narrator structure, which the coherence statistic smoothed over, reappears at Level 3 as long-tail step skewness.

The recurrence statistic, `recur_rate`, measures how often the trajectory revisits a neighbourhood it has already been in. *Bleak House* has a high recurrence rate. The novel circles. Chancery returns, the fog returns, Tulkinghorn returns, Krook's shop returns. The trajectory loops. Corresponding to this, `path_eff` — path efficiency, the ratio of straight-line distance to traversed arc-length — is low. The book does not move toward a goal; it orbits one.

The curvature statistic and the autocorrelation statistics (`curvature`, `acf1_top3`) reveal additional structure: how sharply the narrative direction changes, and how correlated nearby paragraphs are along principal directions. For *Bleak House* these align with what the step-skewness already flagged: locally smooth motion punctuated by voice-switches that introduce curvature spikes.

In our Phase-1 analysis, `step_mean` correlated negatively with rating in books (ρ = −0.096, 6.4σ): smaller steps predicted higher ratings. In music, the sign flipped: larger steps predicted more listens (ρ = +0.071, p = 4×10⁻²⁹). Books reward continuity; music rewards contrast. We return to this in Chapter 21.

### What the Trajectory Can Say

Level 3 says something no earlier level could: *Bleak House* is a returning novel. Its trajectory recurs. Its narrator-switches are not gradual dissolves but step-discontinuities. Its overall curvature is low except at those switches. A reader feels this as the "circling fog" of the book — a stylistic intuition that the trajectory statistics operationalise directly.

More precisely, the trajectory distinguishes *Bleak House* from a hypothetical shuffled version of *Bleak House*. The shuffle would have the same mean, the same distributional shape, the same `pair_sim_mean`. It would have a much larger `step_mean` (random pairs are further apart than adjacent pairs) and a much lower `recur_rate`. The entire order-sensitive signal lives at Level 3.

### What the Trajectory Cannot Say

What trajectory statistics cannot say is *which directions* the trajectory prefers. `step_mean` measures the size of steps, not their direction. `recur_rate` measures return, not return *to what*. To get at direction — to see which axes of the embedding space the book actually occupies and prefers — we need to go to Level 4.

## Level 4: The Learned Projections — Loading on the 71 Axes {#level-4}

### The Discovered Axes

In Phase 1 of our work, we trained a Lasso on the 128-dimensional PCA spectrum of the paragraph cloud and recovered seventy-one non-zero interpretable axes. These axes are, roughly, discovered genre/form directions: they each correspond to a direction in embedding space along which a coherent cluster of corpus books concentrates. Some are easily labelled on inspection — one tracks nineteenth-century domestic realism, one tracks adventure-romance, one tracks epistolary form, one tracks Gothic mood, one tracks scientific exposition. Others resist easy naming but are stable across cross-validation folds.

Level 4 asks: which of these axes does *Bleak House* load on? The answer, in our data, is primarily two. *Bleak House* has strong positive loadings on an axis we will call A-17 (which our nearest-neighbour inspection suggests behaves like "Victorian social-realist") and on an axis A-42 (which behaves like "epistolary interleave" — a direction picked up by books with nested or alternating narrative forms). It has a moderate negative loading on an axis that tracks pure-adventure fiction, and near-zero loadings on axes that track verse, drama, and scientific prose.

The rank-ordering matters: the Lasso is sparse by construction. A typical novel in our corpus has loadings on three to seven axes. *Bleak House*, by this measure, is relatively interpretable — two axes carry most of its explained variance in the 71-dimensional coefficient space.

### What the Level-4 View Can Say

This is the level at which genre and form become computationally visible. It says *Bleak House* is a mixture: mostly Victorian social-realism, with a strong secondary component of narrative-interleave, and a conspicuous absence of adventure and of verse. An algorithmic recommender that used only Level 4 features would group *Bleak House* with *Middlemarch*, *Vanity Fair*, and perhaps *Wives and Daughters*. This matches human critical intuition well enough that it is not coincidence.

Level 4 is also where our learned metric most visibly *can be wrong*. The axes are learned from the corpus. A different corpus — more translated works, more genre fiction, more twentieth-century novels — would produce different axes. Our A-17 is not a fact of nature. It is a direction in a representational space that LaBSE pretraining and our corpus curation together determined. Chapter 9 examines this point at length.

### What Level 4 Cannot Say

Level 4, like every level before it, is a projection. Seventy-one axes out of a 128-dimensional spectrum out of a 768-dimensional embedding space is still a lossy summary. The axes were chosen for cross-validated predictive utility against Goodreads ratings — a target we already acknowledged, in Level 0, to be genre-confounded. Eighty-five percent of the headline signal in the Phase-1 regression was genre. So Level 4 cannot cleanly separate "aesthetic loading on a form" from "sociological loading on a reception category." This is a substantive limitation, not a technical one. We return to it in Chapter 9.

## Five Levels, Five Questions {#five-questions}

We have now walked through *Bleak House* five times. Each pass added structure; each pass answered a question the previous pass could not.

| Level | Object | Question Answered |
|-------|--------|-------------------|
| 0 | Scalar (4.05) | How good, on average, do readers find it? |
| 1 | Mean vector + prior distance | How far from typical is the book's centroid? |
| 2 | Divergences + coherence | How does the book's distribution differ from, and cohere internally against, the corpus? |
| 3 | Trajectory statistics | How does the book unfold — its steps, returns, curvatures? |
| 4 | Lasso loadings on 71 axes | Along which discovered form/genre directions does it live? |

No level subsumes another. Level 4, the "most mathematical" level, cannot tell us the book's rating (Level 0) or its average distance from typical (Level 1). Level 0 cannot tell us anything about Levels 1 through 4. The claim of this chapter — parallel to the claim of its sibling in *Geometric Ethics* — is that these are not redundant views. They are independent questions, each with its own aesthetic content.

### The Shape of the Book

Putting the levels together gives Elena, our critic, a description she could not have assembled from any one of them:

*Bleak House* is rated 4.05 — well-admired. Its mean representation sits 1.4σ from the corpus centre, marking it as somewhat unusual but not foreign. Its distributional divergence from the prior is moderate, but its internal coherence is high: the book sounds like itself, despite its two narrators. Its paragraph-trajectory moves slowly, with positively-skewed steps (the large steps concentrate at narrator-switches) and high recurrence (Chancery, fog, Tulkinghorn keep returning). Its principal loadings are on a Victorian social-realist axis and on a narrative-interleave axis. It is a tight, slow, returning, socially-realist novel with a secondary interleave structure and a high admiration score.

This is not a review. But it is a scaffold for one — a structural description of the book that no scalar could provide, no vector alone could capture, and no distributional summary could render in time.

## A Second Pass: Why Order Matters {#order-matters}

It is worth dwelling, briefly, on the progression of the levels. They are not arbitrary. Each level adds a specific mathematical object that the previous level lacked, and the ordering is structurally forced.

Level 0 gives us a scalar; Level 1 gives us a vector, which is the minimum structure needed to support difference and direction. Level 2 gives us a rank-2 object (a covariance in the distributional view, a pairwise similarity matrix in the coherence view) — the minimum structure needed to support the concept of internal shape. Level 3 introduces sequence, which no previous level could see: trajectory statistics are invariant under all the previous statistics but detect all the order-sensitive content that rank-2 objects miss. Level 4 is a projection — a sparse loading pattern onto axes chosen for predictive utility — and it is at Level 4 that the metric becomes interpretable against named critical categories.

An interesting consequence of this ordering is that *each level has a specific shuffling invariance*. Level 1 is invariant under all orderings of paragraphs. Level 2 is invariant under permutation but not under subsampling. Level 3 is invariant under global rotations in embedding space (distance and curvature are) but not under paragraph shuffling. Level 4 is invariant under relabelling of the Lasso axes but not under change of corpus. The invariance structure *is* the hierarchy. A reader who wants to know "what does this level see that the previous level does not?" can ask, equivalently, "what invariance does the previous level have that this level breaks?"

### A Counterfactual: *Bleak House* Shuffled

Consider, briefly, a hypothetical edition of *Bleak House* in which paragraphs have been permuted uniformly at random. The thought experiment is useful because it cleanly separates the order-sensitive levels from the order-invariant ones.

The shuffled book has the same Level 0 (if we charitably suppose readers rated the shuffled text the same, which they would not; but definitionally, the scalar as a static summary is the same). It has the same Level 1 mean vector and the same distance from prior. It has the same Level 2 divergences and the same `pair_sim_mean`. It has a radically different Level 3: `step_mean` jumps upward (random pairs are further apart than adjacent ones), `recur_rate` collapses (the narrative no longer revisits), `path_eff` rises toward unity (random walks average straight-line efficiency closer to 1 under a single-step metric than a returning narrative does). It retains, mostly, its Level 4 loadings, since sparse axis loading depends on the cloud of paragraphs more than on their order — with the exception of any axis tuned to sequence-sensitive features.

The shuffled book is, in the technical sense, indistinguishable from the original under the first two levels of our tensor. It is sharply distinguishable under the third. This is what "trajectory geometry" buys us: a family of statistics that cares about authorial ordering.

## Closing Note: Against Collapse {#closing-note}

The argument of this chapter is precisely the argument of its sibling in *Geometric Ethics*, with the target variable changed. In ethics, collapsing the case to a scalar before examining it hides structure — the rank-2 tensor of multi-agent evaluation, the metric that determines trade-off rates, the stratum boundaries at which rules change. In aesthetics, collapsing the work to a scalar before examining it hides the same sorts of structure: internal coherence versus distance-from-prior (rank-2, in a sense), trajectory shape, and the discovered axes along which genre and form live.

The recommendation is not "never use the scalar." The scalar exists because some decisions require a single number — shall we buy the book, shall we recommend it, shall we teach it. It is fine to collapse to a scalar at the *moment of decision*. It is a mistake to collapse before then. The tensor hierarchy is the structure of aesthetic understanding; the scalar is the last step of aesthetic choice.

Chapter 8 takes up the structure that we saw flickering at the edge of our data here — the way the manifold is not uniformly smooth, but stratified by genre boundaries, by style thresholds, and by phase transitions where the metric itself changes. Chapter 9 takes up the deeper question of where the metric comes from in the first place: discovered, constructed, or conventionally imposed. *Bleak House* will return in both.
