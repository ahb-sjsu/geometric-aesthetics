# Chapter 2: The Failure of Scalar Aesthetics {#chapter-2-the-failure-of-scalar-aesthetics}

**RUNNING EXAMPLE — Maya's 3.8**

Maya's novel is now out. Her agent sold it. It has been in the world for six months. Its Goodreads page reports 3.8 stars across 2,143 ratings. Maya has read the reviews. What she sees there is nothing like a number. One reader loves the prose and hates the plot. One reader loves the plot and finds the prose mannered. A former creative-writing professor writes four paragraphs about the book's handling of time and gives it five stars. A reader who appears to have expected a different genre gives it one star and writes *boring*. A reviewer at a small literary magazine compares it favorably to Marilynne Robinson; a reviewer in a larger outlet compares it unfavorably to a Netflix limited series. The mean of these is 3.8. The *structure* of these is something else entirely: a multi-peaked distribution over a space with at least four independent axes — prose, plot, genre-fit, and what the reviewers seem to want literature *for*. The 3.8 is a shadow. The novel lives in the light.

## What a Scalar Can and Cannot Say {#what-a-scalar-can-and-cannot-say}

Let us be precise about what a scalar aesthetic evaluation is.

A scalar is a quantity fully specified by a single number. In aesthetics, scalar approaches assign a value — a rating, a score, a price, a rank — to a work. The Goodreads five-star system is scalar. The Metacritic 0–100 is scalar. The Billboard Hot 100 is ordinal, which is an even more compressed scalar. An auction hammer price is scalar (with a unit). Even the professional critic's four-star system is scalar, though it is derived from — and usually accompanied by — a paragraph of prose that is obviously not scalar at all.

Formally, a scalar aesthetic evaluation is a function

$$S: \mathcal{W} \to \mathbb{R},$$

assigning to each work $w \in \mathcal{W}$ a real number $S(w)$. The defining feature of a scalar is invariance: under any admissible transformation of the work's representation — any redescription, any reframing, any change of reader — the value $S(w)$ is supposed to remain the same.

This invariance is both the strength and the weakness of scalar aesthetics. It is a strength because it permits aggregation: you can average a 4 and a 3 and get a 3.5. It is a weakness because to achieve that invariance, we must throw away everything that varies across readers, across contexts, and across the dimensions along which the work is actually evaluated.

The companion volume, *Geometric Ethics*, identifies three failures of scalar moral evaluation: no directional information, uncertainty has no shape, no path-dependence. The failures of scalar aesthetic evaluation are structurally parallel. We develop three of them — directional collapse, variance collapse, and regime collapse — and then examine three concrete scalar instruments (Goodreads, Metacritic, Billboard) in which all three failures are load-bearing.

## Failure 1: Directional Collapse {#failure-1-directional-collapse}

A scalar $S(w)$ reports the magnitude of aesthetic value. It cannot report which directions in aesthetic space are responsible for that magnitude.

Consider *Moby-Dick*. As of this writing, the Goodreads average for Herman Melville's *Moby-Dick* hovers around 3.5 stars across more than half a million ratings. By the same metric, a competently executed mid-list thriller routinely reaches 4.1. By the same metric, a viral self-help paperback regularly reaches 4.4. If you were to sort books solely by this number, *Moby-Dick* would be outranked by an enormous fraction of trade paperback fiction published in any given year.

This is not a controversial observation. Every literary reader has made some version of it. But the usual response — *well, Goodreads averages are unreliable; people don't really mean their stars; taste is subjective* — misses the structural point. The stars are not noisy. They are not insincere. They are measuring *something*. What they are measuring is not what a reader means when she says *Moby-Dick* is "aesthetically enormous."

In the vector framing of Chapter 6, *Moby-Dick*'s aesthetic profile might be written as a rank-1 object with components along many dimensions:

- along the prose-density axis: very positive;
- along the formal-ambition axis: very positive;
- along the narrative-momentum axis: uneven, with long digressive stretches;
- along the character-interiority axis: asymmetrically distributed (enormous for Ishmael and Ahab, thin for most others);
- along the pleasure-per-page axis: highly variable;
- along the influence-density axis: extreme (many later books descend from it);
- along the genre-fit axis: ambiguous by design;
- along the readability-at-age-twenty axis: low;
- along the readability-on-second-reading axis: high.

A scalar that collapses this vector into a single number is, mechanically, some weighted inner product of the profile with a weight vector that represents the reader's preferences at the moment of rating. The 3.5 stars is not wrong; it is the projection of the nine-plus-dimensional object onto a particular one-dimensional axis chosen by the distribution of Goodreads readers. A different axis would give a different number. The axis that Goodreads readers happen to use is dominated by pleasure-per-page, readability-at-first-reading, and narrative-momentum — axes along which *Moby-Dick* is decidedly not a 4.5.

The thriller at 4.1, meanwhile, projects strongly onto exactly the axes that the rating aggregates. The thriller is not 4.1 because it is "better" than *Moby-Dick* in any whole-work sense. It is 4.1 because *its direction in aesthetic space is aligned with the reader-weight vector that the Goodreads aggregate happens to apply*. The thriller and the whale-book are nearly orthogonal. Comparing their scalars is comparing the lengths of the shadows they cast on the same wall from different angles.

The same pathology runs the other way. John Coltrane's late work — *Interstellar Space*, *Meditations* — rates modestly on listener-aggregated platforms and ranks low on most playlists. A top-40 single from the same week routinely outranks it by orders of magnitude. No one with the slightest knowledge of jazz history believes that *Alabama* or *A Love Supreme* are aesthetically "less" than the typical chart-topper. But the scalar, projecting onto an axis whose weights are dominated by first-listen pleasure and rhythmic familiarity, reports exactly that.

The aesthetic vocabulary that the informed reader and listener actually use — *ambitious*, *formally restless*, *emotionally exposed*, *historically decisive*, *technically virtuosic*, *generically pure*, *generically disruptive* — names components of the profile, not coordinates of a single number. These are directions. The scalar lives in magnitudes.

## Failure 2: Variance Collapse {#failure-2-variance-collapse}

The second failure concerns uncertainty.

A scalar, when it reports uncertainty at all, reports a single variance: $S(w) = \mu \pm \sigma$. But readers are not uncertain uniformly. Critics are not uncertain uniformly. Ratings are not noisy in a scalar way. The *shape* of the disagreement about a work is its own structural feature.

Consider two books with identical Goodreads averages of 3.8.

The first has a narrow, peaked distribution: most readers rate it 3 or 4, few give it 1 or 5. This is a consensus mediocre-to-good book. The standard deviation is small.

The second has a bimodal distribution: a large cluster at 5 stars and a large cluster at 1 or 2 stars, with relatively few readers in the middle. The mean is the same. The variance is larger. But even "variance is larger" understates the case: the *shape* of the disagreement is diagnostic. A bimodal distribution usually means the book has a strong directional profile — something about its voice, its moral stance, its genre commitment — that readers love or reject on one dimension that most readers are not in the middle on. This is usually a sign of *aesthetic stake*. Scalar variance does not tell you what is at stake. It tells you only that people disagreed.

The geometric object that captures this information is the covariance tensor of judgments:

$$\Sigma^{ij} = \mathbb{E}[(\delta q^i)(\delta q^j)],$$

where $q^i$ is the reader's judgment along aesthetic dimension $i$ and $\delta q^i$ is the deviation from the mean along that dimension. A scalar disagreement is what you get when you contract $\Sigma$ with a single weight vector. The directional disagreement — *people agreed about the prose and disagreed about the plot* — is visible in the off-diagonal and along-diagonal structure of $\Sigma$. Readers of Goodreads have some intuitive access to this when they read individual reviews. Aggregates do not.

This is the same pathology that Chapter 2 of *Geometric Ethics* identifies for moral uncertainty: the variance has shape, and the shape is ethically (or aesthetically) decisive. In aesthetics, the scalar variance bar around a rating is, in many cases, not noise — it is the signature of the work's directional content reflected back through the population of readers. A scalar that reports only the mean throws this information away. A scalar that reports mean-and-variance throws away the directional structure of the variance.

## Failure 3: Regime Collapse {#failure-3-regime-collapse}

The third failure is the most structural. Aesthetic reality is not uniformly smooth. There are regime boundaries — strata — across which aesthetic rules change discontinuously.

A chart-topping single and a piece of late-period Coltrane both exist in the same medium (recorded music), but they are not located at nearby points in the aesthetic manifold. They occupy different strata. The rules of evaluation differ. On the chart single, faithful reproduction of genre conventions is a positive; on Coltrane, it would be a negative. The listener's attention is structured differently: on the single, every second is supposed to count; on *Ascension*, the work unfolds in a different time-geometry where moment-to-moment engagement is not the right axis.

A scalar that lives over the entire manifold — "how good is this recording?" — cannot represent this stratification. It has to choose an axis and apply it uniformly. Whatever axis it chooses will misread one of the two strata. If the axis is dominated by first-listen pleasure, late Coltrane is badly misread. If the axis is dominated by formal ambition, the top-40 single is misread (not as bad, but as *irrelevant*, which it is not — within its stratum it is doing something that the stratum is about).

Chapter 8 formalizes stratification. The empirical intuition is simple: ratings are only locally meaningful. A four-star romance novel and a four-star literary novel are not four-star objects along the same axis. They are four-star objects along two different, locally-defined axes that happen to be called *four stars* by the same rating site. Readers implicitly know this. The aggregation function does not.

The same phenomenon happens across media. Chapter 21 develops the music case in detail. Within-genre rating prediction in our FMA data shows Rock R=0.139 (n=7,088), Electronic R=0.143 (n=6,284), Hip-Hop R=0.141 (n=2,190), Pop R=0.185 (n=1,173), all modestly but significantly nonzero. Classical R=−0.013 (n=584) and Jazz R=0.031 (n=384) are consistent with zero. The same geometric features that carry signal within Rock carry nearly none within Classical. This is not model failure. It is that Classical and Rock are different strata of the aesthetic manifold, and the local metric is not the same.

A scalar rating cannot represent this. It treats a 4.2 in Classical and a 4.2 in Rock as commensurable numbers. They are not, because they are computed from local projections onto locally different axes in locally different strata.

## Case 1: Goodreads and the Meaning of 3.8 {#case-1-goodreads-and-the-meaning-of-3-8}

We can now read the three common scalar instruments precisely.

Goodreads reports the mean of user-submitted 1–5 integer ratings. The distribution is notoriously compressed: the overall Goodreads average across all ratings is well above 3.5, because readers who dislike a book typically do not finish it and do not rate it, and because the five-point scale invites ceiling effects. Most books in active circulation live in the 3.5-to-4.5 band. The dynamic range of the instrument is, in practice, about one star.

This compression means that the scalar carries relatively little information. We have direct empirical evidence of this, from our own work on the Gutenberg↔Goodreads matched corpus (Chapter 17). With LaBSE-encoded paragraph trajectories and an author-disjoint 5-fold cross-validation on n=4,998 books, we obtain a combined Ridge+Lasso headline correlation of R=0.241 (R² = 0.058, 17σ) between a rich geometric feature set and the Goodreads rating. That sounds substantial. It is also almost all genre signal.

When we residualize by genre (Chapter 17, Phase 2) — that is, when we ask how well the geometric features predict the rating *within genre*, not the rating *across genres* — the correlation drops to R=0.093 (R² = 0.009, z=6.5σ, p = 5.7×10⁻¹¹, n=4,998). **Eighty-five percent of the raw signal was genre confound.** In fiction alone, we get R=0.131 (6.2σ, n=2,250), and in non-fiction history-biography, the intra-genre correlation is null.

The honest reframe of this result is: *there is structured aesthetic signal beyond genre, with small effect size and high statistical confidence.* It is not the case that geometry predicts rating. It is the case that *once the rating's dominant genre signal is accounted for, what remains is small*. Said another way: the Goodreads rating is, to a very substantial extent, *a classifier of what genre the book is*, not a measure of its aesthetic quality. The scalar is doing genre work, not aesthetic work. It is directionally collapsed along the genre axis because that axis carries the most population-aggregate variance.

This is the data-side version of Failure 1. The scalar is a projection; the projection is dominated by the axis with the most readers-per-genre-per-year, which is a demographic feature, not an aesthetic one. And this is not a Goodreads problem per se — it is a structural property of any user-aggregated five-point scale.

## Case 2: Metacritic and the Averaging of Critics {#case-2-metacritic-and-the-averaging-of-critics}

Metacritic is more interesting because its inputs are not naïve readers but professional critics, each producing a long-form review that is itself multi-dimensional, and many of whom have calibrated their own scalar scales against years of prior work. The aggregate is a weighted arithmetic mean of these scalars, normalized to a 0–100 scale.

The input is better. The output still loses almost everything that made the input valuable.

Consider a film that earns a Metacritic score of 72. That 72 is compatible with several entirely different underlying configurations:

- Twenty critics each gave the film a 72: consensus mid-to-good.
- Ten critics gave it a 95 and ten gave it a 49: a divisive film that half the profession regards as major.
- Nineteen critics gave it a 70 and one gave it a 100: a consensus good film with a single enthusiast.

These are three very different aesthetic facts. They lead to three very different decisions about whether to see the film, teach the film, preserve the film, or let it fade. The scalar 72 represents all three identically.

Chapter 14 develops the aggregation theory in full. The formal point is that the mean is a contraction along a single direction in the space of critic-judgment vectors, and the contraction discards exactly the directional and variance structure that is most diagnostic of aesthetic stake. The mean is correct as a contraction — it is a valid scalar output — but it is a poor summary of the underlying distribution. A better aggregation would report a low-dimensional decomposition: the mean, the dispersion, and the principal direction of disagreement. That output is not a scalar; it is a small tensor.

Notice what happens when critics *themselves* argue. They do not argue about whether the film is a 72 or a 74. They argue about *what is at stake*. Does the film's formal experimentation redeem its narrative thinness? Is its emotional charge bought honestly or sentimentally? Is its political content courageous or opportunistic? These arguments are about components of the aesthetic vector and about the legitimate weighting of those components. The scalar output of the aggregation is a declaration that the argument has already been settled by averaging — which is, structurally, a declaration that the argument does not exist.

## Case 3: Billboard and the Ordinal Trap {#case-3-billboard-and-the-ordinal-trap}

The Billboard Hot 100 is scalar in the most compressed possible form: ordinal. The difference between a number-one single and a number-two single is not a number of points. It is a rank. This flattens the distribution by design — it is exactly the projection onto the ordering axis. Any information about margins, directional content, or stratification is formally absent from the list.

Ordinal scalars have a further pathology: they make within-regime comparison compulsory. A Billboard ranking implicitly asserts that every record on the chart is commensurable with every other record on the chart. A pop single and a country single on the same chart in the same week are declared rankable along one axis. The axis exists — sales, streams, radio spins, weighted by format — but it is an industrial axis, not an aesthetic one. Billboard is not pretending otherwise. The trap is on the consumer's side: a ranking *looks like* an aesthetic verdict because it has the form of an ordering.

Our own FMA-Medium work (Chapter 21) is instructive here. When we try to predict $\log(1 + \text{track\_listens})$ from the MERT-v1-330M representation space, we get raw R=0.302 (z=49.8σ, n=24,801). Genre-residualize, and the spectrum-Lasso drops to R=0.177 (z=28.3σ); hand features drop to R=0.043 (z=6.7σ). **Ninety-one percent of the hand-feature signal is genre confound — worse than books.** In head-to-head on a shared n=5,233 tracks against the Echonest / Spotify eight acoustic features, MERT Lasso-spectrum beats Spotify R=0.225 vs R=0.103 (bootstrap p=0.001).

What this tells us is that the *listen-count* scalar is a genre-confounded object, and that the geometric framework carries *additional* information beyond what Spotify's scalar features carry. The Billboard ranking sits on top of a similar listen-count scalar, propagated by aggregation. The chart ordering is a shadow of a shadow.

## The Empirical 85% as Structural Evidence {#the-empirical-85-as-structural-evidence}

We emphasize the 85%-and-91% genre-confound results because they are the strongest data-side evidence we know for the thesis of this chapter.

If scalar aesthetic ratings carried primarily aesthetic information, we would expect residualization by genre to reduce predictive performance by a small fraction. Genre is one aesthetic axis among many. It should not absorb most of the variance. In fact, it does. Across books and music, roughly 85–91% of the predictive variance that geometric features carry onto scalar ratings is absorbed by a single categorical nuisance variable: what genre the work is. Within genre, the remaining predictive signal is real but small: R in the 0.09–0.19 range, with six-to-eight-sigma significance.

This is exactly what the three failures predict.

Directional collapse predicts that scalar ratings will be dominated by whichever direction has the most population variance, because that is the direction along which the aggregate projection is most stable. Genre is that direction. Scalar ratings, across aggregators and media, are primarily directional-collapse artifacts along the genre axis.

Variance collapse predicts that the scalar will be a poor predictor of within-genre quality, because the within-genre disagreement is *shape* disagreement, and the scalar does not represent shape. This is exactly what we see: within-genre R drops to small numbers, and for some genres (Classical, Jazz, history-biography) it drops to null within the power we can muster on these corpora.

Regime collapse predicts that the ratings will not be comparable across strata even when they sit on the same chart. A 4.2-star romance and a 4.2-star literary novel are not commensurable; our within-genre analysis shows that the geometric channels that predict one often fail to predict the other.

Each of the three structural failures of scalar aesthetics has a corresponding empirical signature in our data. The scalar rating is not ineffable; it is informative about genre and demographics, and weakly informative about within-stratum aesthetic quality. The claim of the chapter is not that scalar ratings are meaningless. It is that *they do not mean what they look like they mean*. They look like verdicts about aesthetic quality. They are, in the aggregate, classifications of genre with a small aesthetic residual.

## A Note on Who Is Served {#a-note-on-who-is-served}

A final observation, before we bridge to Chapter 3.

Scalar aesthetic systems did not arise because they captured the structure of aesthetic life. They arose because they served institutional needs: ranking for curation, scoring for marketing, aggregating for recommendation, pricing for sale. Each of these needs is real. Each of them requires, at some point, a scalar output — the decision to buy or not, to play or skip, to shelve or cull.

The problem is not that scalars exist as contractions. Chapter 15 will show that contractions are mathematically necessary: a decision is a scalar because a decision has a yes/no shape. The problem is that institutional aesthetics has mistaken the contraction for the full object. It has forgotten that what precedes the scalar is a tensor — directional, uncertainty-shaped, regime-stratified — and that the process of contracting that tensor is a choice, not a discovery. Different weight vectors yield different numbers. Different strata require different metrics. Different populations project onto different axes.

A geometric framework does not eliminate the scalar. It recovers what preceded it. And by doing so, it makes the contraction process visible, auditable, and reformable — which is to say, it makes possible the critique of the contractions that already happen, every day, at enormous scale, under the signs of engagement, rating, and chart position.

## Bridge to Chapter 3 {#bridge-to-chapter-3}

The case against scalar aesthetics is an old one. It has been made, in different vocabularies, for at least two thousand years. Plato and Aristotle each identified structural features of aesthetic judgment that resist scalar reduction. Kant's *Critique of Judgment* is in large part an extended argument that aesthetic evaluation has a distinctive form that cannot be reduced to cognition, desire, or moral judgment — a claim that, in the light of the present chapter, looks like a claim about directional content. Vitruvius and the Fibonacci tradition sought proportional (not scalar) accounts of beauty. George Birkhoff in 1933 proposed an explicit multi-factor formula for aesthetic measure. The information-theoretic aestheticians of the mid-twentieth century — Bense, Moles, Arnheim — sought structural, non-scalar accounts drawn from Shannon's mathematics of communication.

These were quasi-geometric moves. They reached toward the framework of this book without the tools to complete it. Chapter 3 traces their history honestly — what they saw, what they missed, and why the full geometric formulation had to wait for the learned-representation era.

❖

*The 3.8 is a shadow. The novel lives in the light.*

*What casts the shadow is not, and has never been, a number.*
