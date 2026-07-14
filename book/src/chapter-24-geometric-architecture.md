# Chapter 24: Geometric Architecture — Space, Form, and Proportion in Learned Representations

**RUNNING EXAMPLE — Leona's Facade**

Leona's practice has submitted four facade studies for a mid-rise office building on a corner lot in a historic commercial district. Each study has been rejected — by the client, by the planning board, by a conservation officer, and finally by Leona herself, who has begun to suspect that the four rejections are *not* rejecting the same thing. The client wants "more classical." The board wants "less monumental." The conservation officer wants "compatible with the 1908 bank on the opposite corner." Leona wants the building to hold its own without being a quotation. She has tried ratios — Golden Section, Modulor, $\sqrt{2}$ root rectangles, $1{:}3$ Palladian — and each one produces, in turn, a facade that one of the four evaluators finds convincing and the others do not. She has begun to suspect that proportion is not, in fact, the variable the four critiques are arguing about, though it is the variable the architectural tradition tells her to vary. This chapter sets out what the framework says about the suspicion.

As with painting, we do not have direct empirical results for architecture. We have a set of predictions that follow from the framework's core commitments, together with a pipeline specification detailed enough that the predictions are falsifiable. Architecture is, in one sense, the hardest of the application modalities covered in Part V: the "work" is a building, which is not an image but a *three-dimensional spatial configuration* navigated over time; its reception is distributed across drawings, photographs, site visits, and habituation; and its cultural role makes the rating-analog problem even harder than it was for painting (Chapter 23). We begin, again, with the pipeline.

## 24.1 The Pipeline Analog: Built Space as Embedding Cloud {#pipeline}

For a painting, the patch cloud is a single object — one image tiled into patches. A building does not yield a single image. It yields a *set* of images (plan, section, elevation, exterior photograph, interior photograph, street view, panorama) or, in the digital era, a point cloud captured by lidar or photogrammetry. The embedding-cloud analog must be specified before the framework has anything to say.

**Definition 24.1 (Architectural Embedding Cloud).** Let $B$ be a building. Define the architectural embedding cloud of $B$ as

$$
C(B) = \bigcup_{v \in V(B)} \phi(v)
$$

where $V(B)$ is a finite set of *viewpoints* into the building — exterior elevations, interior panoramas, plan and section drawings, and fly-through frames from a 3D model — and $\phi$ is a patch-token encoder (DINOv2, CLIP, or a geometry-aware encoder such as PointNeXt for lidar input) applied to each viewpoint. The cloud $C(B)$ is a finite multiset in $\mathbb{R}^d$, typically with $|V(B)| \cdot N$ points for $N$ patches per view.

Three sub-pipelines deserve mention:

**Panoramic-image sub-pipeline.** Google Street View, Matterport captures, and the Mapillary network now provide systematic panoramic coverage of much of the built environment. For a building with public exterior visibility, $V(B)$ is populated automatically. This is the shortest path to a corpus of $n \geq 10{,}000$ buildings.

**Point-cloud sub-pipeline.** For buildings with architectural-record lidar (most significant heritage structures, an increasing fraction of new construction), $C(B)$ can be taken directly as the lidar point cloud embedded by a geometry-native encoder. This preserves 3D spatial structure the panoramic pipeline compresses.

**Drawing sub-pipeline.** For historical buildings where neither of the above exists, plan-section-elevation drawings can be encoded as 2D images. This is coarser but recovers the majority of pre-20th-century architectural canon.

In each case, the four channels of Chapter 17 have direct analogs: divergence of $C(B)$ from a corpus prior (the average embedding over a reference corpus of buildings); internal patch-coherence within $C(B)$; trajectory geometry along the gaze-path or promenade-path through views; and Lasso-selected latent directions in a PCA of the cloud. The interpretation of each channel requires some care.

### Interpreting the Channels for Buildings

**Channel A (divergence):** A building whose embedding cloud sits far from the reference corpus is typologically or stylistically unusual relative to that corpus. Gehry's Bilbao Guggenheim, measured against a corpus of municipal buildings from 1900–1990, should exhibit high Hellinger and Mahalanobis-mean distances. A Georgian terrace on a street of other Georgian terraces will not.

**Channel B (internal coherence):** A building whose patches are internally consistent — whose facade and interior surfaces share a common visual vocabulary — has high pair_sim_mean. A Palladian villa with classical vocabulary across exterior, portico, and interior should be patch-coherent. A building that abruptly changes register between facade and interior (a great deal of 1980s commercial architecture, for example) will not.

**Channel C (trajectory):** This is the channel where architecture diverges most interestingly from painting. A building is experienced as a *promenade*: Le Corbusier's *promenade architecturale* is the canonical concept, but the idea runs from the Beaux-Arts procession through the pavilion sequences of Japanese tea-garden architecture to the spatial choreography of Zumthor. The trajectory channel, instantiated for architecture, tracks what the experience of traversing the building *looks like* in embedding space: the step sizes between successive views, the curvature of the path, the recurrence rate of visual motifs.

**Channel D (Lasso-latent directions):** The surviving axes in a 128-dimensional PCA Lasso should be interpretable architectural features: massing type, fenestration rhythm, material vocabulary, structural expression. The test of the channel is whether the selected directions align with the axes that architectural critics already use — and whether they reveal additional axes that critics have not articulated.

### The Rating Analog

Architecture's rating problem is harder than painting's. Candidate rating targets include: post-occupancy evaluation scores (cleaner than museum wall-time but limited coverage); professional peer awards (RIBA, AIA, Pritzker — high-quality but sparse and prestige-confounded); user-generated ratings on platforms such as Atlas Obscura and ArchDaily (noisier but higher coverage); property market proxies (confounded by location to a degree that dwarfs any aesthetic signal); and controlled perceptual studies specifically commissioned for the pipeline. None of these is a Goodreads-class target. We flag the rating-analog problem as the first substantial empirical gap for architecture, parallel to the gap we flagged in §23.1 for painting.

## 24.2 Proportion Systems as Constrained Trajectories

The architectural tradition has, for at least twenty-five centuries, produced *proportion systems*: rules relating the dimensions of building parts to one another and to the whole. Vitruvius's human-body canon, the medieval ad quadratum and ad triangulum schemata, Palladio's *I Quattro Libri*, Le Corbusier's Modulor (1948, 1955). A proportion system, formally, specifies a set of admissible ratios between building elements and rejects configurations outside that set.

**Proposition 24.1 (Proportion Systems as Constrained-Trajectory Patterns).** A proportion system $\Pi$ specifies a submanifold $M_\Pi \subset M_{\text{arch}}$ of the architectural manifold, consisting of buildings whose element-level attributes satisfy $\Pi$'s ratio constraints. The claim of the tradition is not that $M_\Pi$ contains all beautiful buildings (it does not) but that $M_\Pi$ excludes, with high reliability, a substantial class of aesthetically inferior configurations. In the framework's language, $\Pi$ is a constrained trajectory: a restriction on the admissible paths through the building's compositional state space.

This is a reframing. A proportion system is traditionally *described* as a set of ratios. It is most usefully *modeled* as a restriction on trajectories — on how the building is allowed to unfold from its generating element to its completed form. Palladio's *Quattro Libri* does not, in fact, prescribe a single ratio: it prescribes a family of admissible ratios (the seven shapes of rooms in Book I, Chapter XXI — circle, square, square-and-a-third, square-and-a-half, square-and-two-thirds, double square, root-two rectangle) and a procedure for assembling them. The procedure is the content; the ratios are the basis vectors of the constraint.

The framework, applied to a large corpus, should detect these constraints as *high-density tubes* in the trajectory channel. A 4,000-building corpus containing (say) 800 buildings with explicitly Palladian ratios and 3,200 without should, after PCA and Lasso, produce a latent direction whose top-loading buildings are the Palladian subset. The direction would be an empirical identification of the constraint.

### The Golden Ratio, Empirically Reconsidered

No proportion has generated more literature and less agreement than the golden ratio $\varphi = (1+\sqrt{5})/2 \approx 1.618$. Claims have been made that $\varphi$ structures the Parthenon, Chartres, the Villa Stein at Garches, Notre Dame, and a great many other buildings. Analyses by Livio (2002), Markowsky (1992), and Falbo (2005) have shown that most of these claims survive only with charitable measurement conventions — the Parthenon's facade can be fit to a $\varphi$ rectangle only by choosing the correct reference points from several plausible alternatives. The question becomes: is the golden ratio *prescriptive* (architects deliberately employed it, and it produces measurable aesthetic effects), or is it *descriptive* (it is a plausible post hoc fit to a wide range of proportions that include but are not exclusive to $\varphi$)?

**Proposition 24.2 (The Golden Ratio as a Weak Prior).** If the golden ratio has any empirical content, it is as a *weak* prior — a slight elevation in the probability density of aesthetically-rated buildings over a narrow band around $\varphi$, observable only in very large samples and easily masked by stronger signals such as structural coherence, stylistic consistency, and contextual fit. The framework predicts: in a Lasso regression over a 128-dimensional PCA of architectural embedding clouds, the coefficient on any $\varphi$-aligned latent direction will be small, possibly non-significant, and substantially dominated by coefficients on stylistic-coherence and contextual-fit directions.

This is a sharp claim. If a careful study recovers a strong, residualized $\varphi$-coefficient, Proposition 24.2 fails. If such a study recovers no $\varphi$-coefficient at all, the descriptive-not-prescriptive view is confirmed. If, as we predict, the coefficient is small but non-zero and highly sensitive to corpus composition, the $\varphi$ tradition is reframed: it is a post hoc rationalization of a weak prior that operates, when it operates at all, only because stronger signals did not override it.

The broader point is that the framework does not need to adjudicate the golden-ratio controversy to be useful. It tells us what kind of thing a proportion claim is (a constrained-trajectory claim), what its empirical signature should be (a Lasso-detectable high-density tube in representation space), and how to measure its effect size against confounds. This is more than the architectural literature has had.

## 24.3 Space, Circulation, and the Promenade

If proportion systems are constraints on static form, circulation is the constraint on *motion through form*. A building is not only a composition of elements; it is a sequence of spatial experiences that unfolds as the occupant moves from street to threshold to foyer to principal rooms to service areas to egress.

**Definition 24.2 (Architectural Trajectory).** Given an ordered sequence of viewpoints $v_1, v_2, \dots, v_k$ corresponding to a plausible circulation path through $B$, the architectural trajectory of $B$ on that path is the sequence of mean patch embeddings $\bar\phi(v_1), \dots, \bar\phi(v_k) \in \mathbb{R}^d$. The trajectory's step geometry — step_mean, step_std, curvature, path_eff, recur_rate — characterizes the unfolding of spatial experience.

**Prediction 24.1 (Architecture Shares the Book-Like Sign on Coherence).** Architecture, like literature (Chapter 20) and — we predicted in Chapter 23 — like painting, should exhibit the book-like sign on the internal-coherence channel: higher pair_sim_mean predicts higher aesthetic rating, controlling for style/era/genre. A coherent building is one whose parts belong together; most successful architectural traditions select strongly for this property.

**Prediction 24.2 (Architecture Has a Distinctive Promenade Signature).** Where architecture should depart from painting is in the trajectory channel. A well-regarded building is not one in which all views are similar (that would be a building without spatial interest). It is one in which the *step geometry* has a specific profile: moderate step_mean (the sequence of rooms is differentiated, not uniform), low step_std (the differentiation is systematic, not random), and characteristic recurrence (motifs return in transformed form). This is, in the architectural tradition, the signature of a well-composed plan: Sir John Soane's Dulwich Picture Gallery, Louis Kahn's Kimbell Art Museum, Tadao Ando's Church of the Light.

We predict that a study of architectural embedding clouds, stratified by award status or critical rating, will find that *awarded* buildings have a lower step_std at comparable step_mean than unawarded peers. This is a testable architectural-aesthetic claim with no direct analog in painting.

## 24.4 Cross-Cultural Invariance: The Strong Prediction

Chapter 12 established, from the cross-lingual book corpus (4,683 non-English books, 19 languages, 10 language families), that the aesthetic geometry of literature is substantially translation-invariant: pair_sim_mean transfers at $\rho = +0.712$ across language pairs, with the EN↔FI Hellinger correlation reaching $\rho = +0.77$ at $p = 8 \times 10^{-57}$. This is the strongest empirical result in the book. The natural question: does the analog hold for architecture?

**Prediction 24.3 (Cross-Cultural Architectural Invariance).** The geometric structure recovered from a Western architectural corpus will transfer to a non-Western corpus — Chinese timber-frame temple architecture, Indian stepwell and temple traditions, Islamic mosque and madrasa architecture, West African vernacular, Japanese sukiya — at correlations comparable to the book cross-lingual result, provided the embedding encoder was trained on sufficiently diverse imagery. The internal-coherence channel should transfer most robustly (highest $\rho$); the divergence channel should transfer next; the Lasso-latent directions should be *partially* transferable, with tradition-specific axes (for example, the vocabulary of dogu brackets in East Asian timber-frame construction) that do not map onto a Western corpus but are themselves identifiable as high-density tubes within the non-Western corpus.

This is the strong form. We predict it because the architectural tradition has, for centuries, observed cross-cultural convergences in what buildings do well: *legibility of structure*, *hierarchy of entry*, *orientation to site*, *light as organizing principle*. These observations predate the framework by millennia. The framework does not explain why they hold; it predicts that if they hold at the level of practitioner consensus, they should also hold at the level of learned-representation geometry.

If they do not hold — if a model trained on Western buildings fails to recover the structural organization of a Japanese temple, *even after controlling for material and pixel-level difference* — the framework's translation-invariance finding for text does not generalize to built form. We predict that this will not happen; we acknowledge that we have not done the experiment.

## 24.5 Urbanism: Neighborhoods as Building Clouds

An architectural embedding cloud is a representation of a single building. A *neighborhood* embedding cloud is the aggregation of the clouds of the buildings within a spatial boundary. A city becomes a hierarchy of clouds: building, block, district, city.

**Definition 24.3 (Urban Embedding Cloud).** Let $N$ be a spatial neighborhood with buildings $B_1, \dots, B_m$. The urban embedding cloud is $C(N) = \bigcup_i C(B_i)$, and the neighborhood manifold $M_N$ is the corpus-level geometry across a reference set of neighborhoods.

The pair_sim_mean of $C(N)$ measures the *visual coherence* of the neighborhood — how much its buildings resemble one another. This is a quantity urbanists already discuss under the rubric of *fabric*, *texture*, and *urban grain* (Alexander, *A Pattern Language*, 1977; Rossi, *The Architecture of the City*, 1966; Kostof, *The City Shaped*, 1991). The divergence of $C(N)$ from a city-wide prior measures the neighborhood's distinctiveness.

**Prediction 24.4 (Urban Coherence and Desirability).** Residentially desirable neighborhoods, controlling for price and amenities, will exhibit higher pair_sim_mean than less desirable neighborhoods. This is the urban analog of the book-level coherence result. The mechanism is similar: coherence signals intentionality, stewardship, and continuity; its absence signals entropy, neglect, or accelerated redevelopment without shared standards.

The prediction admits an important failure mode: it must be residualized against the confound that wealthy neighborhoods are coherent *because* wealth produces stewardship. A proper test must use within-wealth-band comparisons, or longitudinal data showing that changes in coherence predict subsequent changes in desirability at constant wealth. Without that residualization, the correlation is unsurprising and explains nothing.

## 24.6 Connection to the Architectural Tradition

The predictions above are not arbitrary. They echo and extend claims from within the architectural literature.

**Alexander's *A Pattern Language* (1977).** Christopher Alexander's pattern language is an attempt to catalog the recurrent spatial-compositional motifs that make buildings and settlements succeed. Patterns such as *Alcoves* (no. 179), *Light on Two Sides of Every Room* (no. 159), and *Small Public Squares* (no. 61) are, in the framework's terms, proposals for high-density tubes in the trajectory channel — recurrent, identifiable configurations that a well-trained Lasso on a sufficiently large corpus should recover as latent directions. Alexander's later work (*The Nature of Order*, 2002–2004) posits fifteen properties of life — levels of scale, strong centers, boundaries, alternating repetition, positive space — each of which is a candidate for a named axis in the Lasso decomposition.

**Hillier's space syntax.** Bill Hillier's space syntax (*The Social Logic of Space*, 1984) provides a graph-theoretic vocabulary for spatial configuration: *integration*, *depth*, *intelligibility*. These are properties of the building's circulation graph, not of its surface appearance. The framework's trajectory channel is, in a certain light, a learned-representation analog of space syntax — one that operates on patch embeddings rather than hand-coded graph topology, but that targets the same underlying question: how does the unfolding of space structure the occupant's experience?

**Norberg-Schulz's *Genius Loci* (1980).** Christian Norberg-Schulz's phenomenological architecture argues that a building's aesthetic success depends on its faithfulness to the spirit of its site — its genius loci. In the framework, site-fit is the divergence of the building's embedding cloud from its contextual prior, computed not at the city scale but at the immediate-surround scale. A building that fits its site is one whose patches lie near the distribution of its adjacent built context; a building that defies its site diverges. Norberg-Schulz's claim becomes a testable hypothesis: awarded buildings that are explicitly contextual have lower surround-prior divergence than awarded buildings that are explicitly iconic, and both are rated higher than buildings that are neither.

## 24.7 What Would Refute the Framework in Architecture

The framework is refuted in architecture under conditions parallel to those laid out in §23.3 for painting, with one addition specific to the modality.

First, if the four-channel decomposition does not recover within-style signal — if divergence, coherence, trajectory, and Lasso-latent features all dissolve under within-style residualization — the claim that architectural aesthetic judgment has structure beyond style is falsified. We would retain the result that style is measurable (that is trivial once one has an encoder) but lose the claim that the framework adds explanatory power.

Second, if the sign of the coherence channel is inverted relative to books — if architectural aesthetic rating *decreases* with pair_sim_mean — then Prediction 24.1 fails, and the book-like/music-like dichotomy of Chapter 17 does not generalize to built space.

Third, if cross-cultural invariance (Prediction 24.3) fails — if a model fit on Western buildings systematically misranks non-Western buildings even within their own tradition — the translation-invariance extension fails.

Fourth, and specific to this chapter, if a careful study of proportion systems finds that the Palladian, Modulor, and $\varphi$ traditions do *not* form high-density tubes in the trajectory channel — if buildings that follow these proportion systems are geometrically indistinguishable from buildings that do not — then Proposition 24.1 fails, and we must say that proportion systems, while historically important, do not leave detectable signatures in learned representation space. This would be an important negative result; we would note it without euphemism.

## 24.8 Honest Acknowledgment of the Empirical Gap

As with Chapter 23, the pipeline of §24.1 has not been run. The closest prior work is at the intersection of computational architectural history and computer vision: Llamas et al. (2017) on classification of architectural heritage images; ArchiNet and related datasets; urban-morphology projects using Street View (Doersch et al., *What Makes Paris Look Like Paris?*, 2012, which is the closest published precedent). None of these has explicitly computed the four-channel decomposition on an architectural corpus with a rating signal. The study is doable with current infrastructure. We do not claim it is done.

What we claim is narrower: that if the study is done, the predictions of §§24.3–24.4 are the specific commitments of this framework, and their confirmation or refutation constitutes evidence about the framework's scope. A reader who is skeptical that the book and music results generalize should hold architecture as a test case — one where the framework has staked bite-sized claims in advance, and where those claims admit clean falsification.

## 24.9 Leona, Reconsidered

Return to Leona and her four rejected facade studies. The framework's diagnosis is this: the four evaluators are not disagreeing about proportion. They are disagreeing about *which* corpus prior the building should be close to (the client invokes a classical corpus; the board invokes a modest-scale corpus; the conservation officer invokes the 1908 bank corpus; Leona invokes her own training corpus). Each evaluator has a different $C_{\text{ref}}$ and measures the facade's divergence from that reference. The facade that minimizes distance to one reference maximizes it to another. Proportion is not what is being contested; *reference* is.

The practical consequence, for Leona, is to stop iterating on proportion and start *eliciting references*. What are the three buildings each evaluator thinks the new building should feel like? Compute the embedding cloud of each, form the mixture, and compute her current designs' divergence from that mixture. The evaluation is no longer "do you like the facade" but "does this facade approach the reference mixture you named, and if not, in which direction does it depart?" This reframes an argument about taste as an argument about reference, which is tractable.

That is the practical contribution. The theoretical contribution is more modest and more durable: the architectural tradition's two-thousand-year investment in proportion, circulation, context, and coherence has, in the framework's vocabulary, been investment in *channels* that learned representations are now equipped to measure. Whether the framework is correct in detail will be settled by experiment. That it offers the correct *kind* of tool — a multi-channel geometric vocabulary, not a scalar score — is, we believe, already visible in the chapter's running example.

## 24.10 Bridge to Chapter 25

Architecture is the spatial case. Games — the subject of the next chapter — are the spatial case *extended through time by the player's own choices*. A building's promenade is fixed by the architect; a game's promenade is co-authored by the player. This makes the trajectory channel the load-bearing one, and it sharpens the central prediction of Part V to its most specific form: game aesthetics should exhibit a stronger trajectory signal than any other modality we have studied. We turn to that now.

---

*For the covariance structure of the architectural metric tensor, see the general treatment in Chapter 5; the architectural instantiation is a straightforward specialization. For the empirical grounding of the cross-cultural invariance prediction of §24.4, see Chapter 12 and the cross-lingual results reported in Chapter 17, §17.5.*
