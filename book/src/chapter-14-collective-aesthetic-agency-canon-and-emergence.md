# Chapter 14 — Collective Aesthetic Agency: Aggregation, Emergence, and Canon

**RUNNING EXAMPLE — Daniel and the Long Tail**

Daniel works at a music-recommendation startup. His day job is training the ranking model. His evenings are spent on a side project: a hand-curated list of the 500 songs he thinks deserve to outlive their streaming counts. He has 4.2-star songs he would die for and 4.7-star songs he would not play at a party. The gap between his private canon and the Goodreads-style average his company serves to users is what keeps him awake. Last week his product manager asked him, in good faith, "why not just sort by average rating?" He gave a professional answer about diversity and long-tail discovery. He did not give the answer he believed, which is that the average rating is not a measurement of the work at all. It is a measurement of the measurement apparatus. A 4.2-star average on a song with 50,000 listens and a 4.7-star average on a song with 400 listens are not the same kind of thing. The canon his company is implicitly constructing — *the work people agree about* — is missing something the canon he believes in — *the work the data clusters around, regardless of whether anyone has noticed* — has. He does not yet have the language to say why. This chapter is the language. {#running-example}

## 14.1 Beyond the Individual Reader {#beyond-the-individual-reader}

Part III, so far, has been about single agents and single works. A reader receives a poem (Chapter 10). A critic searches the manifold for a best interpretation (Chapter 11). A translator preserves invariants across a change of basis (Chapter 12). A measurement operator collapses a Hilbert-space superposition (Chapter 13). Each of these has been, in its own way, a private transaction between one mind and one object.

But aesthetic life is rarely private. Works are read in book clubs, rated on Goodreads, discussed at parties, reviewed in journals, taught in syllabi, anthologised in collections, and — slowly, over decades — absorbed into or excluded from a canon. The work that matters is rarely the work you privately love; it is the work your community, your era, and your institutions have agreed matters, and that agreement is itself a collective-agent phenomenon with its own geometry.

This chapter asks how the geometric framework handles the transition from individual aesthetic judgment to collective structure. The answer, as in Ethics Chapter 14, is: the collective is not the sum of its parts, and the emergent remainder is where the interesting content lives. The parallel sections are exact. Where Ethics treats corporate obligation, we treat canon. Where Ethics measures structural injustice via an emergent tensor component, we measure canonical distortion via the same.

## 14.2 The Scalar-Average Fallacy {#the-scalar-average-fallacy}

The working canon of our time is, increasingly, a scalar average. Goodreads sorts by mean rating. Rotten Tomatoes aggregates percent-positive. Spotify's "most played" is a count. A mid-2020s reader who wants to know *what to read next* is handed a list produced by arithmetic mean.

The failure of this procedure is well known in the social-choice literature and has been rediscovered several times in recommender-system practice. We rehearse it only briefly.

**Failure 1: The Goodreads average is not a measurement of the work.** It is a measurement of the joint distribution of *(readers who chose to read it, readers who chose to rate it, what the platform's rating interface encouraged them to enter)*. Our own book study (Chapter 17) showed that genre confounds accounted for 85% of the headline R² between tensorial structure and ratings. The average rating is not even a clean rating; it is a rating heavily confounded by who-rates-what.

**Failure 2: Arithmetic means dissolve disagreement.** A novel that half its readers loved and half hated receives the same mean rating as a novel that every reader found mediocre. These are morally and aesthetically different facts about the works, and the scalar discards both.

**Failure 3: Means are non-invariant under basis change.** We showed in Chapter 12 that the aesthetic tensor has specific invariant components — `pair_sim_mean`, Hellinger — that survive translation into 19 languages at $\rho \approx 0.7$. The *average rating* has no such invariance: Goodreads averages in Finnish, French, and Japanese do not measure the same quantity even for the same book. The geometry transfers; the scalar does not.

The scalar-average canon is a collapsed observable with no basis-invariance, no disagreement signal, and no confound correction. It is the aesthetic analogue of what Ethics Chapter 14 calls "the majoritarian fallacy": the assumption that aggregation is addition.

## 14.3 Canon as Cluster-Centre, Not Vote {#canon-as-cluster-centre-not-vote}

Here is our alternative. A canon is not a list of works that most readers voted for. A canon is a *cluster-centre on the aesthetic manifold* — a location in the space of tensorial features around which a mass of well-received works accumulates, and toward which individual readings drift when they are working well.

The picture is geometric. Imagine a cloud of books, each a point in the 128-dimensional PCA spectrum of their paragraph-trajectory features. Some regions of that cloud are dense; others are empty. The dense regions are genre-clusters, form-clusters, mood-clusters. A *canon*, on this picture, is a maximally dense region relative to some defining label (e.g., "literary fiction judged worthwhile by English-language critics, 1900–2000"). The canon is *discovered*, not voted on. A work enters it by being at or near the centre of a dense cluster; it exits by drifting away from that centre as the cluster itself drifts.

We argue that this is the correct picture for three reasons.

**Reason 1: Empirically, the data picks out canonical axes without anyone voting.** Our Phase 1 book study ran Lasso on a 128-dimensional PCA spectrum of paragraph-trajectory features. The Lasso retained 71 non-zero coefficients (Chapter 17, and §14.4 below). Each retained coefficient is a direction in feature space that the data itself selects as predictive. None of these axes were hand-specified, voted for, or named in advance. The statistical procedure discovered them. Calling them "emergent canons of form" is not poetic; it is a literal description of what Lasso-on-PCA does: it finds the axes along which the data clusters.

**Reason 2: Cross-linguistically, the same clusters appear.** Our Phase 3 results (Chapter 12) showed that the same structural features are preserved at $\rho \approx 0.7$ across Germanic, Uralic, Romance, Hellenic, Italic-ancient, and Constructed language families. If canons were mere votes, they would not survive basis change. They do. The clusters are geometric features of the aesthetic manifold, not sociological artefacts of any one linguistic community.

**Reason 3: Cluster-centres, unlike averages, support disagreement without dissolution.** A cluster in feature space has a centre and a variance. The variance is not noise; it is information about how tightly the cluster coheres. A canonical cluster with high variance is a canon-under-construction; one with low variance is a canon-at-consensus; one with bimodal structure is a canon-splitting. The scalar average discards all of this.

## 14.4 The Collective Aesthetic Tensor {#the-collective-aesthetic-tensor}

We now make the picture precise, paralleling Ethics Chapter 14's collective agency tensor.

### Definition

Let $\mathcal{A} = \{1, \ldots, n\}$ be a population of readers, each with an interest covector $I^{(a)}_\mu$ (what axes of the aesthetic manifold that reader weights) over a shared manifold $\mathcal{M}$. The **collective aesthetic tensor** $\mathcal{C}$ is a multilinear map
$$\mathcal{C} : T_1^* \otimes \cdots \otimes T_n^* \to T_p \mathcal{M}$$
that takes one interest covector from each reader and returns a collective aesthetic valence direction on $\mathcal{M}$. In components,
$$V^\mu_{\text{coll}} = \mathcal{C}^\mu_{\nu_1 \cdots \nu_n}\, I^{(1)}_{\nu_1} \cdots I^{(n)}_{\nu_n}.$$

For a two-reader collective, $\mathcal{C}$ has rank 3 and $9 \times 9 \times 9 = 729$ components (using our nine working axes; the full 128-dimensional PCA basis gives $128^3 \approx 2.1 \times 10^6$).

### Decomposition

**Definition 14.1 (Decomposition of Collective Valence).** For a two-reader collective,
$$\mathcal{C}^\mu_{\nu_1 \nu_2} = \mathcal{C}^\mu_{(\nu_1)} \delta_{\nu_2} + \delta_{\nu_1} \mathcal{C}^\mu_{(\nu_2)} + \mathcal{E}^\mu_{\nu_1 \nu_2},$$
where the first two terms are the individual contributions (each reader's valence independent of the other's interests) and $\mathcal{E}^\mu_{\nu_1 \nu_2}$ is the **emergent component** — the part of collective valence not attributable to any individual.

The emergent component vanishes if and only if the collective valence is the sum of individual valences. When $\mathcal{E} \neq 0$, the collective has aesthetic agency that exceeds its members.

### Measuring Emergence: The 71 PCA Axes as Discovered Canons

The empirical witness for $\mathcal{E} \neq 0$ in the aesthetic setting comes from our Lasso study.

We ran Lasso regression of Goodreads ratings on the 128-dimensional PCA spectrum of LaBSE paragraph-trajectory features, author-disjoint 5-fold CV, $n = 4{,}998$ Gutenberg↔Goodreads matched books. The Lasso retained 71 non-zero coefficients. These axes:

- were not specified in advance;
- are individually interpretable as genre-and-form directions (narrative continuity, register-variation, lexical-field coherence, and so on);
- survive cross-validation;
- collectively contribute ~8σ of predictive signal on top of the hand-designed features.

Each of these axes is, in the vocabulary of this chapter, a *discovered canonical direction*. No reader picked them. No critic wrote an essay naming them. No voting produced them. They are the directions along which the collective reception data — 4,998 books, millions of reader-hours — clusters. They are $\mathcal{E}$, made visible.

**Caveat on effect size.** The genre-confound correction brings the total predictive R down from 0.241 to 0.093 intra-genre. Most of the 71 axes are doing genre-discrimination work; a smaller subset is doing within-genre aesthetic work. But the point for Chapter 14 is structural rather than effect-size-dependent: the Lasso's discovery of any interpretable axes at all — let alone 71 — is evidence that the collective aesthetic tensor has non-zero emergent components. A pure sum of individual judgments would have produced a diffuse, un-sparse solution. It did not.

## 14.5 The Reception Structure Tensor {#the-reception-structure-tensor}

A collective of readers is not a set. It has structure: who cites whom, which critics read which magazines, which syllabi feed which graduate programs, which algorithm recommends which playlists, which language family the work is translated into first. The structure tensor $\Sigma_{ab}$ encodes these relationships, exactly paralleling Ethics Chapter 14 §14.4.

$\Sigma_{ab} > 0$ where reader $a$ and reader $b$ share influences and co-cluster; $\Sigma_{ab} < 0$ where they define themselves by opposition (think *New York Review* vs *n+1* in the 2010s, or cultural vs popular music criticism); $\Sigma_{ab} = 0$ where they are structurally independent.

The antisymmetric part $\Sigma_{[ab]} = \tfrac{1}{2}(\Sigma_{ab} - \Sigma_{ba})$ is the aesthetic-power differential: who cites whom without being cited back. In reception history this is the critic who *names a movement* but is not named by it; the editor who *anthologises* but is not anthologised; the algorithm that *recommends* but does not rate.

The collective aesthetic tensor factorises through the reception structure:
$$\mathcal{C}^\mu_{\nu_1 \nu_2} = \sum_{a,b} \Sigma_{ab}\, E^{(a)\mu}_{\nu_1} \otimes E^{(b)\mu}_{\nu_2} + \mathcal{E}^\mu_{\nu_1 \nu_2}.$$
The first term is structure-mediated individual judgment; the second is the irreducibly collective remainder.

## 14.6 Emergent Canonical Properties {#emergent-canonical-properties}

### Canons No Reader Holds

The emergent component $\mathcal{E}$ represents canonical properties that exist at the collective level but at no individual level. Three paradigm cases.

**The modernist novel as a form.** No reader reading *Ulysses* in 1922 knew they were reading "a modernist novel." The category did not yet stabilise. The form was an emergent property of the reception-structure that coalesced over decades. It is now a stable canonical axis — one of the directions that our Lasso would almost certainly recover on a 1900–1940 corpus — but it was not present in any single reader's interest covector in 1922. $\mathcal{E}$ caught up with the work.

**The album as an aesthetic unit.** Before the LP, there was no canonical *album*. Listeners had records, sides, singles. The LP's physical form made the 40-minute sequenced listening experience possible; the reception-structure of album reviews, album charts, and album-of-the-year lists made it *canonical*. No individual listener had "album" as a weighted interest dimension before the form emerged. The structure tensor generated the dimension.

**Genre drift and genre collision.** Our cross-modality finding — that `pair_sim_mean` correlates *positively* with book rating ($\rho = +0.126$, 8.4σ) and *negatively* with music listens ($\rho = -0.076$, p = 5×10⁻³³) — is an emergent property of the structure tensors of the two reception communities. No individual reader and no individual listener has these signs as explicit preferences. They fall out of the collective structure.

### A Formal Criterion

**Proposition 14.1 (Emergent Canon).** A canonical property is emergent if and only if there exists no set of individual interest weightings $\{I^{(a)}_\mu\}$ and no set of functions $\{f_a\}$ such that
$$V^\mu_{\text{coll}} = \sum_a f_a(I^{(a)}_\mu, O^{(a) \mu})$$
for all works in the canonised cluster. Equivalently, the contraction
$$\mathcal{E}^\mu_{\nu_1 \cdots \nu_n} I^{(1)}_{\nu_1} \cdots I^{(n)}_{\nu_n} \neq 0$$
on a set of non-trivial measure in the manifold.

The criterion is testable. Our 71 Lasso axes pass it: no linear combination of the hand-designed individual-reader-scale features reproduces them, which is exactly why the Lasso selected them as independent predictors.

## 14.7 Cultural Memory as Slow Averaging {#cultural-memory-as-slow-averaging}

Canon formation, viewed dynamically, is a slow averaging process on the manifold. Every critical act, every citation, every syllabus inclusion is a local update of the collective density — a small push toward the cluster-centre or a small reinforcement of it. Over decades, the process has the character of gradient flow on a slowly evolving loss surface.

Three features of this flow matter.

**Drift.** The cluster-centre moves. Genres that were stable in 1950 — *the Western*, *the dry-martini thriller* — have migrated to different regions of the manifold by 2020, not because the old works changed but because the reception structure revised its preferred axes. The motion is holonomic: a work transported through the reception apparatus and returned to itself is not the same work (Chapter 10).

**Splitting.** A canonical cluster can bifurcate. The Gothic novel split into horror and romance. The "album" split into hip-hop album and indie-rock album and EDM set. A cluster splits when the reception structure develops two sufficiently distinct sub-communities to pull the centre in different directions; the emergent tensor $\mathcal{E}$ develops a double-peaked density.

**Collision.** Two previously separated clusters can collide. The literary/genre distinction in fiction is, in the 2020s, mid-collision: what were once two manifold-regions with distinct local metrics are fusing into a single region with a complex metric. Our cross-lingual invariance results (Chapter 12) are relevant here: the *structural* features ($\rho \approx 0.7$) transfer across language families, but the *sociological* canonical boundaries do not. When two communities' canons collide, the structural tensor survives; the institutional labelling does not.

## 14.8 The Institutional Measurement Apparatus {#the-institutional-measurement-apparatus}

We borrow the Hilbert-space vocabulary of Chapter 13. A canon is, in the collective setting, an *aggregated measurement apparatus*. The MacArthur committee, the Booker judges, the Pitchfork editorial board, the Spotify algorithm — each is an institutional observable with its own eigenbasis and its own density operator. A work submitted to the apparatus is collapsed into one of its eigenstates.

Daniel's intuition, at the start of this chapter, was right. A 4.2-star average on 50,000 Goodreads ratings and a 4.7-star average on 400 Goodreads ratings are not the same kind of quantity. They are eigenvalues of different measurement operators — the Goodreads-mass-reader observable vs the Goodreads-enthusiast observable — applied to different states. Summing them arithmetically, as if they were repeated measurements of the same quantity, is a category error.

The Goodreads average has a specific failure mode we can now name: it is a measurement made by a large apparatus whose coupling to any particular work is weak, and whose collapse basis is the five-star scale — an observable whose dimensionality is so coarse that it discards nearly all the tensorial information about the work. A cluster-centre in the 128-dim PCA spectrum is a measurement made by a different apparatus — one with fine-grained structural basis — and it retains information the star-average throws away. Neither is the *true* reading. They are different measurements. The canon is the record of which measurements the institutional apparatus preserves.

## 14.9 Artificial Canons: Recommender Systems as Collective Agents {#artificial-canons-recommender-systems-as-collective-agents}

Increasingly, the reception structure includes non-human agents. A recommender system is a collective-agent-builder: it reads the $n$-reader interaction history and emits a canonical ordering. The algorithm is a contraction of the collective aesthetic tensor — typically to a single scalar ranking per user per slot. We flag three things this chapter has prepared us to see.

First, a recommender system's canon is not *found* in the data; it is *imposed on* the data by the choice of loss function. Different loss functions perform different contractions (Chapter 15), producing different canons. The "neutrality" claim common in platform rhetoric is false at the level of the collective tensor.

Second, the genre-confound asymmetry we found in Phase 2 (85% of books' headline R² is genre; 91% of music's is) is directly relevant. A recommender trained on raw engagement data learns an aesthetic tensor that is 85–91% genre-sorting machinery. This is not necessarily a failure — sometimes we want genre sorting — but it is not aesthetic recommendation, and calling it that is a mis-measurement.

Third, cross-lingual recommender systems will succeed or fail based on which observables they learn. The invariant features ($\rho \approx 0.7$ across 6 language families) will transfer; the non-invariant ones will not. A recommender relying on raw star averages will not cross linguistic borders. One relying on `pair_sim_mean` or the Hellinger structural signal will. This is an empirical, falsifiable claim about recommender-system architecture, not a philosophical one.

Chapter 18 will return to this in detail, asking what it means for an artificial agent to have aesthetic taste at all. Chapter 19 will make it concrete in the DEME-for-aesthetics architecture.

## 14.10 Summary and Bridge {#summary-and-bridge}

We argued three things.

One: the scalar average is the wrong aggregation. It discards directional information, dissolves disagreement, and fails basis invariance. The Goodreads-style canon is a structurally impoverished measurement.

Two: canons are discovered cluster-centres on the aesthetic manifold, not voted-on rankings. Our Lasso-retained 71 PCA axes are an empirical instance: directions the data itself selects as canonical, without anyone voting. The cross-lingual $\rho \approx 0.7$ invariance is the same fact seen from the symmetry side.

Three: collective aesthetic tensors have emergent components — parts of the collective valence that cannot be reconstructed from any individual reader's judgment. The modernist novel as a form, the album as an aesthetic unit, the sign-flip between book-coherence and music-coherence: all are $\mathcal{E}$, not $\sum_a f_a$.

Daniel's private canon of 500 songs is, in this vocabulary, an attempt to occupy and curate a local region of the manifold where the cluster-density he cares about is high and the official Goodreads-style apparatus under-measures. His tension with his product manager is not a matter of preference. It is a dispute about which contraction of the collective aesthetic tensor the company should deploy.

Chapter 15 closes Part III by asking what happens when the individual agent — a reader, listener, critic, curator — is finally forced to act. The tensor is rich. The judgment is one-dimensional. The projection is lossy and unavoidable. We will argue, as Ethics Chapter 15 does for moral contraction, that the choice of projection is itself the site where aesthetic commitment actually lives.
