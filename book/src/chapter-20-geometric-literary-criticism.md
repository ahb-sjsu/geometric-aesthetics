# Chapter 20: Geometric Literary Criticism — Books on the Aesthetic Manifold

**RUNNING EXAMPLE — Maya's Novel**

Maya has written a novel. She has read it aloud to her partner, passed drafts to two friends, and received the familiar mixture of encouragement and hedged silence. Her agent says the pacing is wrong in the middle third. Her writing group says the voice is strong but the structure is unclear. A sensitivity reader flags a section her editor then defends. Maya wants to know whether her book *works* — and finds that every reader has a different scalar in mind when they answer. One reads for voice, another for plot, another for theme. No reader reads for all of these at once, and no reader hands back more than a thumbs-up or a thumbs-down with a few annotations attached.

Maya is the protagonist of this chapter because her problem is the chapter's problem. Literary criticism is the oldest and most fully articulated practice of aesthetic judgment in the Western tradition, and it has always been, at its best, a geometry in prose. Close readers have never reduced a novel to a star rating; they have always described it along directions — realist vs. allegorical, aphoristic vs. narrative, Platonic dialogue vs. Aristotelian treatise, romance vs. satire, Apollonian vs. Dionysian. What we demonstrate empirically in this chapter is that those directions are not ornamental; they are recoverable from the text itself, by a pipeline that does not know what genre is, does not know what a critic is, and has never read a review. The axes critics have drawn by hand are present in the geometry of the text, and they can be measured.

This chapter is the native empirical chapter for books. We report the Gutenberg–Goodreads experiments in full: the four structural channels, the 17σ headline signal, the 6.5σ residualized signal after genre is stripped out, the 6.2σ intra-fiction result, and the ρ≈0.7 cross-lingual invariance across six language families. We then interpret what the data tell us about literary criticism — not as a replacement for close reading but as a computational formalization of what close readers have always done, now performable at scale.

## 20.1 The Shape of the Problem {#20-1-the-shape-of-the-problem}

The problem of scalar literary judgment is older than Goodreads. Horace's *dulce et utile* already compressed every poem onto two axes, and the reception history of any canonical work demonstrates how much information is lost when a reader or review site hands back a single number. Goodreads tells us that *Middlemarch* averages 4.0, *The Road* averages 4.0, and *Pride and Prejudice* averages 4.3. On the scalar these are nearly identical works. In the reading experience they are three distinct locations in a space with dimensions the scalar does not represent — tonal register, narrative density, affective direction, philosophical posture.

The scalar-irrecoverability theorem of Chapter 15 applies here without modification. No continuous function $\phi: \mathbb{R}^d \to \mathbb{R}$ is injective for $d > 1$. Any continuous projection of a $d$-dimensional aesthetic attribute vector onto a scalar destroys information that is mathematically irrecoverable. A 4-star novel and a 4-star novel are not the same novel. The critic's job has always been to tell us, along which directions in the full manifold, two apparently similar works actually diverge.

What we add is the claim — and the empirical evidence — that these directions are discoverable from the text's geometry without a critic in the loop. The critic remains necessary to *interpret* the directions once discovered; but the directions themselves fall out of the data.

## 20.2 The Pipeline {#20-2-the-pipeline}

The Gutenberg–Goodreads experiment matched $n = 4{,}998$ books between the Project Gutenberg corpus and Goodreads. Gutenberg provides the text; Goodreads provides the human-aggregated rating target. Each book was paragraph-tokenized, each paragraph encoded with LaBSE (`sentence-transformers/LaBSE`, a language-agnostic BERT sentence embedding of dimension 768), and each book was thus represented as a trajectory $(x_1, x_2, \ldots, x_{T})$ of paragraph vectors in $\mathbb{R}^{768}$. We then computed four families of structural features from this trajectory:

**A. Spectral divergences.** KL, JS, Hellinger, Bhattacharyya, Mahalanobis-mean, and Total Variation, each measured between the book's paragraph distribution and the pooled corpus paragraph distribution. These quantify how far a given book sits, as a distribution, from the average book. Each reaches ~8σ individually under author-disjoint 5-fold cross-validation.

**B. Internal coherence.** The mean and standard deviation of pairwise cosine similarity between paragraphs within the book: $\texttt{pair\_sim\_mean}$ and $\texttt{pair\_sim\_std}$. Books whose paragraphs are all close to each other in LaBSE space are more *internally coherent*. This channel reaches 8.4σ and is statistically distinct from the divergence channel — a book can be close to the corpus mean and internally incoherent, or far from the corpus mean and internally coherent.

**C. Trajectory geometry.** Features of the paragraph-to-paragraph walk: $\texttt{step\_mean}$, $\texttt{step\_std}$, $\texttt{step\_skew}$, $\texttt{recur\_rate}$ (how often the trajectory returns to a previously visited neighborhood), $\texttt{acf1\_top3}$ (autocorrelation structure of the dominant directions), $\texttt{curvature}$, $\texttt{path\_eff}$ (path efficiency, ratio of net displacement to total path length), $\texttt{powerlaw\_slope}$, and $\texttt{tail\_mass\_100}$. Each reaches 3–6σ.

**D. Lasso on PCA spectrum.** The paragraph distribution projected onto a 128-dimensional PCA basis fit on the full corpus, then Lasso-regressed against the rating target with author-disjoint folds. Seventy-one of 128 directions received non-zero coefficients. These are the *discovered axes* we will interpret in Section 20.5.

Combined Ridge+Lasso on all channels yields $R = 0.241$, $R^2 = 0.058$, at $17\sigma$ under author-disjoint 5-fold cross-validation. This is the headline number. It is also the number that is 85% genre confound, as we turn to next.

## 20.3 The 85% Confession {#20-3-the-eighty-five-percent-confession}

Any text-based predictor of rating has to confront a simple structural fact: genres carry average ratings. Fantasy averages higher than literary fiction; young-adult averages higher than classical essay; romance averages higher than philosophy. A model that merely learned to identify a book's genre from its text would recover a substantial portion of the rating signal without saying anything about aesthetic quality. Close readers have always known this — they mark books up or down *within* genre, not across — and a computational literary criticism that does not respect the same discipline is not criticism at all.

We therefore re-ran the pipeline with genre residualization. Each feature $f_i$ was replaced by $f_i - \mathbb{E}[f_i \mid g]$ where $g$ is the book's genre label; the target rating was residualized identically. The combined model then yielded $R = 0.093$, $R^2 = 0.009$, at $z = 6.5\sigma$, $p = 5.7 \times 10^{-11}$.

The honest reframe is that **85% of the headline $R^2$ was genre confound**. What remains is a real effect — 6.5σ is not noise — but the appropriate description of the remaining signal is *additional aesthetic signal beyond genre*, not *geometry predicts rating*. This distinction matters enormously for what the chapter can claim.

Stratifying by genre, the within-fiction result is $R = 0.131$, $6.2\sigma$, $n = 2{,}250$ — a real within-genre effect for novels. The within-nonfiction and within-history-biography results are null. The framework captures fiction-internal aesthetic variation, not variation inside the genres whose own internal structure is closer to an argument or a record than a narrative trajectory.

## 20.4 The Strongest Finding — Cross-Lingual Invariance {#20-4-cross-lingual-invariance}

The finding that bears the most philosophical weight is not the strongest in effect size. It is the *invariance*.

We repeated the pipeline on 4,683 non-English books drawn from Gutenberg in 19 languages across 10 language families. Each non-English book was LaBSE-encoded (LaBSE is language-agnostic by construction — the same semantic content in French or Finnish or Greek maps to a neighborhood in the same 768-d space) and *projected into the English corpus PCA-128 basis*. The axes were held fixed. No language received a retrained model.

Ten languages reached the $\geq 20$-book bundling threshold: Finnish (288), French (227), German (138), Dutch (88), Italian (49), Spanish (38), Greek (33), Esperanto (24), Hungarian (21), Latin (20). Six language families had statistical power: Germanic, Uralic, Romance, Hellenic, Italic-ancient, Constructed. For each feature, we measured the mean Spearman ρ across language-pair comparisons: a feature that preserves its within-book signature across languages gets ρ close to 1; a feature that is a language-specific artifact gets ρ close to 0.

The top features were:

- $\texttt{pair\_sim\_mean}$: ρ = $+0.712$
- $\texttt{mahal\_mean}$: ρ = $+0.710$
- Hellinger: ρ = $+0.675$
- Bhattacharyya: ρ = $+0.675$
- JS: ρ = $+0.674$

The headline pair is EN↔FI Hellinger, $\rho = +0.77$ on $n = 288$ books, $p = 8 \times 10^{-57}$. EN↔FR Hellinger, $\rho = +0.78$ on $n = 227$. When we compute the ratio of within-bundle standard deviation to between-book standard deviation — the proportion of a feature's variance that is language-specific rather than book-specific — we get $\texttt{path\_eff}$ at 0.18, $\texttt{recur\_rate}$ at 0.28, and the divergence family at 0.39–0.44. The geometry of a book in LaBSE-token space is substantially preserved when the book is translated.

A rating-transfer test — train a Ridge model on English books, apply it to bundled non-English books — yields $R = 0.07$ on $n = 940$, $p = 0.033$. This is weak but above chance, and it is the exact kind of weakness we would expect: rating is a culturally and linguistically specific evaluation, even when the geometric structure that drives it is largely preserved.

The Chinese Gutenberg corpus deserves its own caveat. Only five Chinese bundles formed, because Chinese Gutenberg contains classical originals — the *Analects*, Sunzi's *Art of War*, the *Shijing* — not translations of Western works. The Sinitic gap is corpus-design, not a model failure. We flag it honestly and do not count it as a disconfirmation.

We will return to the philosophical significance of this invariance in Chapter 12, where it serves as the empirical witness to a Noether-style symmetry-invariance claim: under the symmetry group of meaning-preserving linguistic transformations, the structural features of an aesthetic trajectory are conserved. That is a stronger statement than "translation preserves content"; it is a statement about the geometry of the content.

## 20.5 The Discovered Axes — What the Lasso Found {#20-5-the-discovered-axes}

The Lasso on the 128-d PCA spectrum produced 71 non-zero directions. These are not directions we imposed; they are directions the data selected. We have spent considerable time examining the top-loading paragraphs on each direction, and what we find is that the axes are *recognizably literary-critical*. The data have rediscovered, without supervision, distinctions close readers have drawn for centuries.

We catalogue four representative axes below. Each is characterized by the paragraphs that load highest positively and highest negatively on the corresponding PCA direction — the paragraphs the data says the direction is *about*. The glosses are ours; the directions are the corpus's.

**Axis 1 — Narrative–folklore vs. aphoristic.** At one extreme, long paragraphs of connected action: characters, scenes, rising clauses, temporal adverbs ("then", "after", "once"). At the other extreme, short paragraphs of compressed generalization: proverbial constructions, balanced antitheses, atemporal present-tense. Novels and folktales at one pole; Pascal, La Rochefoucauld, and the Chinese classics at the other. The Lasso does not know what a novel is. It has discovered the structural signature of narrative vs. sententious prose from sentence distribution alone.

**Axis 2 — Poetry vs. philosophy / biography.** Highly compressed, metrically salient, image-dense paragraphs (lyric poetry, verse drama) at one pole; discursive, propositional, transition-dense paragraphs (academic philosophy, historical biography) at the other. The biography–poetry contrast is one of the sharpest macro-distinctions a librarian makes. The data make it at the level of paragraph geometry.

**Axis 3 — Platonic dialogue vs. Aristotelian treatise.** Both are philosophy; both appear on Axis 2's philosophy pole; but within the philosophical sub-corpus, a third axis separates them. Platonic dialogues have short, alternating paragraphs (because speakers alternate); they exhibit high $\texttt{recur\_rate}$ (the conversation circles a question). Aristotelian treatises have long, non-alternating paragraphs with low $\texttt{recur\_rate}$ (the argument advances monotonically). The data rediscover the oldest generic distinction in the philosophical tradition.

**Axis 4 — Romance vs. satire.** Both are narrative; both appear on Axis 1's narrative pole. Within narrative, Axis 4 separates paragraphs whose emotional register trends upward (encounters, reconciliations, celebratory descriptions) from paragraphs whose register trends downward (irony, deflation, grotesque). Frye's quadrant diagram in *Anatomy of Criticism* drew this axis by hand. The PCA has drawn it from text.

We do not claim that all 71 directions are this interpretable. Some are clearly genre labels in disguise (the "fantasy" direction, the "Victorian novel" direction); some are closer to register or diction signatures that do not correspond to any critical tradition we recognize; some are almost certainly PCA rotations of other axes rather than independent discoveries. The general point, however, holds: the axes a critic would hand-write are recoverable from paragraph-level LaBSE geometry, and they are far more numerous than any critical school has catalogued.

This is the offering to literary studies. Close readers have always produced axes of judgment — Auerbach's *Mimesis* is a catalogue of them, as is Bakhtin's *Dialogic Imagination*, as is the entire genre criticism of the twentieth century. What we offer is that the axes can be derived from the text rather than imposed on it, and that they can be computed at corpus scale. The critic's job is not replaced; it is amplified. The critic is no longer the sole source of axes; she is the interpreter of a much larger axis catalogue that the data have already drawn.

## 20.6 What the Geometry Says About Reading {#20-6-what-the-geometry-says-about-reading}

The $\texttt{pair\_sim\_mean}$ sign is positive in books: $\rho = +0.126$, $8.4\sigma$. Higher internal coherence predicts higher rating. Books that stay close to themselves, tonally and thematically, are rewarded. The $\texttt{step\_mean}$ sign is negative: $\rho = -0.096$, $6.4\sigma$. Smaller paragraph-to-paragraph jumps predict higher rating. Books that move in smaller increments through their semantic space are rewarded.

Together these two signs say something about what makes a novel work. Novels reward continuity. Paragraphs that belong to each other, that do not jolt the reader from one neighborhood to another, that maintain a coherent voice from chapter to chapter, are the paragraphs readers rate highly. This is not a controversial claim about novels. It is very nearly the first thing any creative-writing workshop teaches. What is new is that the claim falls out of the text's geometry without a workshop in the loop.

This finding becomes philosophically interesting only in Chapter 21, where we will see that *music goes the other way*. Music rewards contrast. The sign of $\texttt{pair\_sim\_mean}$ flips in the FMA experiment. The sign of $\texttt{step\_mean}$ flips as well. Readers reward books for staying close to themselves; listeners reward tracks for moving. We will have more to say about this cross-modality sign flip in the musicology chapter, where it is the chapter's central surprise. For the present chapter it is enough to note that *books reward continuity* is not a trivial statement; it is one pole of a sign that the framework could have come out the other way on.

## 20.7 Against the Algorithmic-Curation Worry {#20-7-against-curation-worry}

A reasonable objection to any quantitative literary criticism is that it licenses algorithmic curation: once a model predicts what readers will rate highly, platforms will use it to promote books that game the model. The worry has teeth in the music-streaming context (Chapter 21) and in fashion and product design (Chapter 27); it has teeth here as well.

The geometric framework is, we argue, better-behaved than a scalar predictor in this regard. A scalar predictor tells a publisher *whether* a book will be rated highly; a geometric predictor tells them *along which axes* a book will be received. The former licenses Goodhart's-law optimization; the latter at least *surfaces* what is being optimized for. If a book climbs the "romance" axis, the critic sees that; if it climbs the "aphoristic" axis, the critic sees that; if it climbs a direction that does not correspond to any recognized critical axis — a pure artifact direction the Lasso found and labelled only by its PCA index — the critic sees that too and is invited to look at it.

This does not solve the curation problem. It reframes it. The question shifts from *how do we stop algorithms from optimizing quality?* to *which axes do we want algorithms to surface, and which do we want them to suppress?* That is a critical and curatorial question, not a purely technical one, and it is one the critic is well-positioned to answer.

## 20.8 Honest Failure Modes {#20-8-honest-failure-modes}

The chapter would be dishonest without a catalogue of what the framework fails to capture.

**Author effects are enormous.** Our author-disjoint 5-fold CV is a discipline against author leakage. If we had permitted cross-fold author overlap, the headline $R$ would be substantially higher. This is not a bug; it is a warning. A large portion of what readers rate is *which author wrote it*, and no text-based feature can distinguish an author from the distributional signature of her prose.

**Non-fiction is largely invisible to the framework.** Within-history-biography and within-nonfiction-general intra-genre residualized signals are null. The framework captures something about fiction-internal variation that it does not capture in argument or record. We conjecture that non-fiction's quality signature lives more in factual accuracy and argumentative validity than in trajectory geometry, and that both of those are outside the reach of a paragraph-level LaBSE encoder. This is a genuine limit.

**Rating is not the same as literary merit.** The Goodreads rating is the aggregated preference of a self-selected population of readers. It correlates with literary merit, weakly, but the correlation is not identity. A more principled target would be critical reception (reviews, citations, canon status); that target is harder to measure at corpus scale and we do not yet have a high-quality version of it. We are reporting what we can, not what we wish.

**Translation effects are real even when small.** The cross-lingual invariance ρ ≈ 0.7 is remarkable but is not ρ = 1. Some fraction of a book's LaBSE geometry is language-specific. The framework cannot distinguish, from LaBSE features alone, a book whose original language was French from a skilled French translation of an English book. Prose registers, sentence-length conventions, and paragraph-break conventions differ systematically across literary traditions, and they shift the geometry by small but detectable amounts.

**The genre confound is not eliminated, only reduced.** Residualization by observable genre labels does not remove genre structure that lives inside labels — "literary fiction" covers wildly different aesthetic traditions. The 6.5σ residualized signal is a lower bound on genre confound reduction, not an upper bound.

## 20.9 Bridge to Musicology {#20-9-bridge-to-musicology}

We have argued that books sit on an aesthetic manifold whose directions are measurable, interpretable, and cross-lingually invariant. The axes close readers have drawn by hand are recoverable from paragraph-level LaBSE geometry at statistical significance. The framework captures 6.5σ of additional aesthetic signal beyond genre and 6.2σ of within-fiction signal on a sample of 2,250 novels. This is the first computational literary criticism, to our knowledge, that respects genre-confound discipline and reports residualized rather than headline effect sizes.

The next chapter asks whether the same framework carries over to music. The short answer is that it does — the FMA experiment on 24,801 tracks produces a residualized $R = 0.177$ at $28.3\sigma$, with the MERT encoder out-competing Spotify's eight acoustic features at $p = 0.001$. But the framework's *direction* flips. The channels that drive rating-up in books drive listens-down in music, and vice versa. Books reward continuity. Music rewards contrast. That sign flip, discovered only because we had both modalities on the same framework, is Chapter 21's central finding. It is also the reason a multi-modal, manifold-based account of aesthetics is not a luxury but a necessity: a scalar-per-modality account could not have seen the sign flip at all.
