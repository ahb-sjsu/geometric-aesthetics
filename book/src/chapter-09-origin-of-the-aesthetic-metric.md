# Chapter 9: The Origin of the Aesthetic Metric — Discovery, Construction, Convention

**RUNNING EXAMPLE — Hiroshi's Acquisition Committee**

Hiroshi, a curator at a mid-sized art museum, chairs the acquisitions committee. A board member has asked a question he cannot answer: *what metric are you using when you decide a piece is worth acquiring?* He lists some candidates. Art-historical significance, as judged by consensus of the curatorial staff. Market trajectory, as reported by two auction-house analysts. Fit with the collection. Condition. Provenance. Each of these, he realises, is itself a scalar summary of something richer. Behind each stands a richer object: a distance in some space of works, a trade-off between dimensions. Where do those trade-off rates come from? He can list three candidate answers. The museum *discovered* them — reading them off some fact about what good art is. The museum *constructed* them — baked them into policy documents, acquisition guidelines, training for junior curators. The museum *inherited* them — they came from the field, from a reception history the museum did not author. Hiroshi suspects the honest answer is all three at once, in a specific way. The board member wants one. This chapter is about why the honest answer is better than the simple one.

## 9.1 The Metric Is Not Given {#not-given}

Chapter 6 set out what the aesthetic metric $g_{\mu\nu}$ does. It defines distances between works, inner products between feature vectors, and the trade-off structure that determines which aesthetic properties can be exchanged against which, and at what rates. Chapter 7 walked through a single novel at five tensor levels. Chapter 8 showed that the metric is not uniform across the manifold — that it varies, often discontinuously, across genre and modality strata.

What none of those chapters answered is the question Hiroshi's board member asked: *where does the metric come from?*

The sibling volume *Geometric Ethics*, in its Chapter 9, takes up the parallel question about the moral metric and distinguishes four positions: realism (the metric is a fact to be discovered), constructivism (it is built through idealized deliberation), expressivism (it is projected from agents' attitudes), and governance (it is determined by legitimate institutional processes). In aesthetics, the landscape is similar but not identical. The three classical positions have names with long pedigrees:

- **Discovery** (realism): the metric is a feature of the world, uncovered by careful inquiry — a descendant of Kant's purposiveness made empirical.
- **Construction** (constructivism): the metric is determined by our methods of representation — the choice of encoder, training corpus, and statistical machinery.
- **Convention** (sociological): the metric emerges from collective reception — canon formation, critical consensus, the accumulated judgments of a community.

Our position, which occupies the middle ground between these three, is that the aesthetic metric is *discovered-constructed* — neither free-floating in the world nor freely invented, but extracted under specific representational constraints that themselves reflect prior human choices.

The empirical warrants for this middle position are two. The cross-lingual invariance result (ρ = 0.7 across six language families, Chapter 17) is the strongest evidence we have that the metric tracks something *more-than-conventional*: it survives translation into geometrically distant languages. The genre-confound finding (85% of our books R², 91% of our music R²) is the strongest evidence we have that, without care, the metric tracks sociological categories much more than aesthetic ones. Between these two findings the middle position is forced. The chapter is about why.

## 9.2 The Discovery Account {#discovery}

### The Claim

The realist account holds that aesthetic structure exists in the world prior to our methods for measuring it. On this view, when our Lasso recovered seventy-one interpretable axes on the PCA spectrum, we were not inventing those axes — we were uncovering a structure that was there all along, imprinted on the space of works by whatever combination of cognitive, cultural, and material facts constitute the aesthetic domain. The metric $g_{\mu\nu}^{*}$ is approximated by our measurements; we never reach it exactly, but we improve. Different methods, applied to the same population of works, converge on the same structure as they refine.

**Formal statement.** There exists a tensor field $g_{\mu\nu}^{*}$ on the aesthetic manifold $M$ such that correct aesthetic evaluations are consistent with $g^{*}$. Empirical methods (feature extraction, regression, metric learning) produce progressively better approximations to $g^{*}$.

This is the closest thing in aesthetics to a Kantian position: Kant's *Critique of Judgment* held that aesthetic judgment, while subjective in the sense that it flows from feeling rather than concept, was *universally communicable* — it made claims on other minds. Our realism is the computable descendant of that claim: *purposiveness without purpose* becomes *geometric structure without predictive target*.

### Strengths

**Phenomenology of aesthetic inquiry.** Working critics often feel, as Elena did in Chapter 7, that they are discovering something about a work rather than imposing something on it. When the tensor stack revealed *Bleak House*'s high recurrence rate and low path-efficiency, Elena did not feel she had *decided* the book circles. She felt she had *detected* it circling. Realism explains this phenomenology.

**Progress.** Realism allows aesthetic inquiry to have progress. Our discovery of the internal-coherence channel (`pair_sim_mean`, 8.4σ) was an addition to what prior feature sets could see. On the realist reading, this was the field learning something new about the structure of aesthetic space — not merely switching to a new convention.

**Cross-lingual invariance.** The ρ = 0.7 correlations across language families (Chapter 17) are hard to explain on a purely conventional account. If the metric were entirely a convention of English-language reception, there would be no reason for its features to appear, at the same numerical values, in translations into Finnish, French, German, Dutch, Italian, Spanish, Greek, Esperanto, Hungarian, and Latin bundled corpora. The pattern in the data is what a realist would predict: a structural fact of the work, tracked by LaBSE, recovered consistently across language families.

### Challenges

**Epistemology.** How do we access $g^{*}$? In physics, the metric of spacetime manifests through measurable phenomena — light bending, clocks slowing. What are the aesthetic analogues? Goodreads ratings? Listen counts? These are available, but Chapter 8's genre-confound result shows they are heavily contaminated by sociological signal. We lack a clean aesthetic measurement device. The realist must find a way to factor the noise.

**Metaphysics.** What kind of entity is an aesthetic metric? It is a tensor field over a space of works. Where does it live? Realism owes some answer — whether in Platonic style (abstract structure existing independently), in naturalist style (grounded in cognitive invariants common to human minds), or in some other form.

**Underdetermination.** Different representational pipelines might recover different metrics, even given the same works. A metric extracted under Word2Vec features, a metric extracted under BERT, and a metric extracted under LaBSE will differ. If all three are approximations of a single $g^{*}$, they should converge as they improve — an empirical claim that has not been systematically tested in aesthetics.

## 9.3 The Construction Account {#construction}

### The Claim

The constructivist account holds that the metric is built through our methods. There is no prior fact to discover; the features we extract, the axes we find, the distances we compute are products of the choices we made in setting up the computation. Change the encoder and you change the metric. Change the corpus and you change the metric. Change the CV protocol and the Lasso's regularisation path and you change which axes are "discovered."

**Formal statement.** The aesthetic metric $g_{\mu\nu}$ is a function of the modelling pipeline $\Pi$:

$$g_{\mu\nu} = \Pi(\text{encoder}, \text{corpus}, \text{features}, \text{estimator}, \text{target})$$

Different $\Pi$'s yield different $g$'s. There is no pipeline-independent metric.

### Strengths

**Pipeline dependence is real.** Our books metric was extracted under LaBSE pretraining. Our music metric was extracted under MERT-v1-330M pretraining. Neither encoder was chosen to optimise aesthetic reconstruction; each was pretrained on its own very specific task (multilingual sentence similarity, self-supervised audio modelling). The representational priors of those encoders are baked into our metric. A different encoder would produce a different metric. This is straightforwardly true.

**The features we extract are geometrically inevitable given the prior.** Once the encoder is chosen, much of what follows is forced. Spectral divergences follow from the distributional view, internal coherence follows from pairwise similarity, trajectory statistics follow from the sequential ordering of paragraphs. These are not independent inventions. Given a vector representation of sequential content, they are the natural rank-2 and trajectory-level statistics. Our work is, in this respect, a *discovery given a construction*: given the LaBSE/MERT prior, these are the features.

**Residualisation exposes construction.** The 85% / 91% genre-confound results are, in effect, a constructivist finding. They show that much of what our metric appears to measure is determined by choices of corpus composition and target variable. A corpus balanced differently, or a target variable other than rating, would yield a different headline effect.

### Challenges

**Convergence across pipelines.** If the metric were pure construction, we would expect metrics extracted under radically different pipelines to be uncorrelated. In practice, they are not. Ordinal aesthetic comparisons between books — which book is more coherent, which has longer internal trajectories, which loads on more interpretable axes — tend to agree across reasonable pipeline choices. This is not predicted by strong constructivism.

**Cross-lingual invariance.** The same problem as above, now from the other side. The cross-lingual result says that the metric, as extracted, is *relatively independent of the language stratum of the corpus*. This is difficult to reconcile with an account on which the metric is mostly a product of our modelling.

**Interpretability.** Some of our Lasso-discovered axes are directly interpretable ("Victorian social-realist," "epistolary interleave," "Gothic mood"). These correspond to named critical categories that pre-exist our pipeline. A strong constructivist account has to explain the prior naming.

## 9.4 The Convention Account {#convention}

### The Claim

The conventionalist account holds that the metric emerges from collective judgment: canon formation, critical reception, accumulated academic consensus, editorial decisions about what gets reprinted and assigned. On this view, Goodreads ratings and listen counts are not biased measurements of an underlying aesthetic fact; they are the aesthetic fact, at least insofar as aesthetic facts exist. The metric is a convention of a reception community.

**Formal statement.** The aesthetic metric for a community $C$ is the fixed point of the community's reception history — the function $g_{\mu\nu}^{(C)}$ that rationalises the community's aggregate ordinal judgments over works.

### Strengths

**The genre-confound result.** Eighty-five percent of our books R² was genre confound, and ninety-one percent of our music R² was. These are big numbers. They say that a very large share of what our pipeline learns, when trained against human rating and listen data, is *what category the community has placed the work in*. The conventionalist says: that is not a bug. That is the metric. The metric just is the pattern of collective categorisation.

**Canon explains reception.** The highest-rated books on Goodreads are not a random sample of literature. They are, largely, canonical works that have had decades to accumulate reputation. Any metric trained against Goodreads rating will thus recover, primarily, the structure of the reception-filtered canon. Conventionalism accepts this at face value.

**Metaphysical economy.** No Platonic $g^{*}$. No hidden structural fact. Just a community's aggregated verdicts, extracted as geometry.

### Challenges

**Cross-lingual invariance, again.** The ρ = 0.7 across six language families is the hardest challenge for pure conventionalism. Each language family has its own reception community, its own canon-formation history, its own editorial practices. If the metric were purely conventional, we should see its features at best weakly correlated between English and Finnish, English and Greek, English and Esperanto. We see them strongly correlated: ρ = +0.77 for the English-Finnish Hellinger feature on n = 288 translations, p = 8×10⁻⁵⁷. Something is transferring that is not reception community.

**Rating transfer is weak but above chance.** An EN-trained Ridge applied to pooled non-English bundled books gave R = 0.07 on n = 940 at p = 0.033. Weak. But above chance. Strong conventionalism, which expects per-community metrics to be approximately independent across communities, does not predict above-chance transfer.

**Within-genre fiction signal is real.** After removing genre (the main conventional signal), there is still a residual aesthetic correlation in fiction: R = 0.131 on n = 2,250 at 6.2σ. This residual is what remains *after* removing sociological category. Conventionalism needs a way to explain its persistence.

## 9.5 The Discovered-Constructed Position {#discovered-constructed}

### Our Claim

We argue that the aesthetic metric is *discovered-constructed*. More precisely:

1. The learned encoder (LaBSE for text, MERT for music) imposes a representational prior. This prior is a *construction*: it reflects choices about pretraining corpus, architecture, objective, and scale.
2. Given that prior, the structural features we extract — spectral divergences, internal coherence, trajectory statistics, Lasso axes on PCA spectrum — are *geometrically inevitable*. They are what rank-2 and trajectory-level statistics naturally are in a vector representation of sequential content. This is *discovery given the construction*.
3. The metric $g_{\mu\nu}$ induced by these features, evaluated on a corpus, therefore has two sources of contingency (the encoder and the corpus) and one source of inevitability (the feature set, given the encoder). It is discovered in the inevitable layer, constructed in the contingent ones.

### Why Not Pure Discovery

Because the encoder is not given by nature. LaBSE was trained by a team at Google on a specific set of bilingual pairs; MERT was trained by the Multimodal Art Projection group on 160,000 hours of music under self-supervised objectives. Neither choice was forced. Had pretraining been done differently, the metric would differ.

### Why Not Pure Construction

Because the cross-lingual invariance result exists. Features extracted under the LaBSE prior, applied to translations into six language families, recover the same structural signal (ρ = 0.7) *using the same PCA basis*, refit on English. This is not a free parameter. If the metric were pure construction, nothing would force Finnish translations of English novels to sit in the same positions on the English PCA axes as their English sources. They do. That is a fact about translation, and about LaBSE, and about the metric — and it is more than construction.

### Why Not Pure Convention

Because the cross-lingual invariance result cuts across reception communities. If the metric were the pattern of a community's judgment, it would change as the community changed. Going from the English reception community to the Finnish reception community changes almost everything — readership, editorial practice, critical tradition — and yet the structural features transfer. Something is surviving that is not the convention.

### The Honest Middle

The metric is a tensor field extracted by a pipeline whose contingencies are the encoder and the corpus; given those contingencies, it tracks genuine structure of how sequential content distributes in representational space; and that structure is, as a matter of empirical fact, partly conserved across reception communities that share nothing else of the relevant kind. This is discovered-constructed.

## 9.6 Evidence: The Cross-Lingual Invariance Result {#cross-lingual-evidence}

We have referred repeatedly to the cross-lingual result as our strongest evidence against pure convention. The specifics (full methodology in Chapter 17):

- n = 4,683 non-English books in 19 languages, 10 language families.
- LaBSE encoding, projected into the English corpus's PCA-128 basis. The basis is *not refit per language*: the same axes are used.
- Bundles requiring at least 20 matched translations: Finnish (288), French (227), German (138), Dutch (88), Italian (49), Spanish (38), Greek (33), Esperanto (24), Hungarian (21), Latin (20).
- Exploratory bundles below threshold: Portuguese (10), Japanese (4), Polish (2), Swedish (2), Russian (1), Czech (1), Chinese (5, classical originals rather than translations).
- Six language families with statistical power: Germanic, Uralic, Romance, Hellenic, Italic-ancient, Constructed.
- Feature-by-feature Spearman correlations across matched translation pairs:
  - `pair_sim_mean`: ρ = +0.712
  - `mahal_mean`: ρ = +0.710
  - Hellinger: ρ = +0.675
  - Bhattacharyya: ρ = +0.675
  - Jensen-Shannon: ρ = +0.674
- Ratios of within-bundle to between-book standard deviations (smaller = more invariant):
  - `path_eff`: 0.18
  - `recur_rate`: 0.28
  - divergence family: 0.39–0.44
- Rating transfer: EN-trained Ridge applied to pooled non-English bundled books: R = 0.07 on n = 940, p = 0.033.

The interpretation is: translation acts like a tube on the manifold, and the within-tube variation is much smaller than between-book variation. Works stay close to themselves, in the shared geometry, across language families. The metric — to the extent our features instantiate it — is *not* a pure convention of English reception.

### The Sinitic Gap, Honestly

The Chinese Gutenberg corpus is classical originals (Confucius's *Analects*, Sunzi's *Art of War*, the *Shijing*) — not translations of Western works. Only five bundles formed, below the significance threshold. This is a corpus-design limitation, not a failure of the method. The invariance claim we make is established across Germanic, Uralic, Romance, Hellenic, Italic-ancient, and Constructed families. Claims about Sinitic, Japonic, Slavic, and beyond require a matched-translation corpus that, at time of writing, we do not have.

## 9.7 Evidence: The Genre-Confound Result {#genre-evidence}

Complementary evidence, from the other direction: without care, the metric tracks sociological category much more than aesthetic structure.

- Books: headline Phase-1 combined Ridge+Lasso R = 0.241. Phase-2 genre-residualised R = 0.093. Eighty-five percent of the headline R² was genre confound.
- Music (FMA Medium, MERT): Lasso-on-spectrum R = 0.302. Genre-residualised R = 0.177 for spectrum Lasso; R = 0.043 for hand features (down from R = 0.151). Ninety-one percent of hand-feature R² was genre confound.
- Within-genre residuals:
  - Fiction (R = 0.131, n = 2,250, 6.2σ).
  - Non-fiction history-biography: null.
  - Rock (R = 0.139, n = 7,088), Electronic (0.143, 6,284), Hip-Hop (0.141, 2,190), Pop (0.185, 1,173).
  - Classical (R = −0.013, n = 584): null. Jazz (R = 0.031, n = 384): null.

The conventionalist reading of this result is that the metric is mostly a genre classifier. This reading is partly correct. The honest conclusion is that genre *is* a governance-like stratum structure — communities have organised works into reception categories, and our metric, trained against community judgments, learns those categories first.

But the within-stratum residual is real in fiction and in the mainstream music genres. After removing the sociological classifier, there is additional aesthetic signal — small, but well-measured. This residual is where the "discovered" portion of the discovered-constructed metric lives.

## 9.8 The Position, Summarised {#position-summary}

The aesthetic metric has three sources and no single source.

**From construction**: the encoder, the corpus, the feature set, the target. Our LaBSE and MERT pipelines, our 4,998-book and 24,801-track corpora, our choice to regress against Goodreads rating and FMA listen-count. Change these, and the metric changes.

**From discovery**: given the construction, the structural features are geometrically inevitable. Spectral divergences, internal coherence, trajectory statistics, sparse axes on the PCA spectrum — these are forced by the representational setup. They are also, as a matter of fact, conserved across six language families, which means they track more than a single reception community's convention.

**From convention**: a substantial share of what our metric weighs, without residualisation, is stratum membership — genre, period, language-family reception category. Genre is not a nuisance variable to be removed. It is a *part* of the aesthetic metric, reflecting real patterns of collective reception, and removing it too aggressively removes structure that culturally matters.

The honest empirical practice is to report the metric at all three levels: the full model (with genre in it), the within-stratum residual (genre removed), and the cross-stratum invariants (the features that transfer across language families). All three carry information. None is "the" metric by itself.

## 9.9 What This Means for Practice {#practice}

Hiroshi's committee, given the honest answer, can now articulate a position for the board. Their acquisition metric is *discovered-constructed*. It was constructed by the museum's history — the choices of what to collect and how to train curators. It was inherited from the art-world reception community — from the critics, galleries, dealers, and scholars whose judgments preceded any individual acquisition. And yet, within these contingencies, it tracks structural facts about works that are not purely conventional: facts that survive translation across media, that show up consistently to well-trained curatorial eyes independent of the local reception tradition, that can be sharpened but not fabricated.

The methodological recommendation of this chapter, to any empirical aesthetic programme, is the same as its sibling's methodological recommendation for moral inquiry. Do not claim discovery alone. Do not concede all ground to construction. Do not dissolve the metric into convention. The honest middle position is:

1. Acknowledge the pipeline explicitly. Say which encoder, which corpus, which target.
2. Report the genre-confound residual explicitly. Do not let the headline number stand unexamined.
3. Demonstrate cross-stratum transfer where possible. Cross-lingual invariance is our strongest evidence for structure beyond convention; look for the analogue in any new modality.
4. When you cannot demonstrate cross-stratum transfer (as with our Classical and Jazz nulls), say so. Do not export the aesthetic regime of one stratum into another where it has not been shown to hold.

## 9.10 Closing Note {#closing-note}

The three classical accounts of the aesthetic metric — discovery, construction, convention — each capture something. Each is, alone, inadequate to the empirical situation. The cross-lingual invariance result forbids convention; the pipeline dependence forbids discovery; the interpretability of discovered axes and their cross-community robustness forbid pure construction.

The argument parallels, closely, the argument of Chapter 9 in *Geometric Ethics*. There, the conclusion is that the moral metric is governed — the output of legitimate institutional processes operating within structural constraints. In aesthetics, governance is a weaker notion (no aesthetic legislature, no binding aesthetic constitutional court), but the structural analogue is real. What governance is to ethics, *canon formation and critical reception* are to aesthetics: imperfect, contested, partly legitimate, partly captured by power. The metric we extract under our pipeline is neither the bare reflection of these processes nor fully independent of them.

Chapter 10 takes up what happens to this metric as works influence each other through history — parallel transport, style holonomy, and the flows of aesthetic influence across periods and schools. If Chapter 9 is about where the metric *comes from*, Chapter 10 is about how it *moves*.
