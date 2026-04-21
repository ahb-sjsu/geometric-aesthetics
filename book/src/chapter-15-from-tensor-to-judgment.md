# Chapter 15 — From Tensor to Judgment: The Philosophy of Aesthetic Choice

**RUNNING EXAMPLE — Maya at the Revision**

Maya is four years into the second novel. The manuscript is 320,000 words in its most recent pass, and her editor has asked her, professionally and with affection, to cut it to 120,000. Maya has in her head — or closer to the truth, her head and her notes and her project folder and her agent's marginalia and her own memory of the decade before she started writing — a tensor. The book has a manifold location, or rather a trajectory through the manifold (Chapter 10). It has obligation-like components: scenes she owes her characters, images she owes her mother, a register she owes the tradition she is writing into. It has interest-like components: the reader she imagines, the prize jury she does not admit she is imagining, the critic who will be unfair, the friend who will be generous. It has uncertainty. It has curvature. It has, in some paragraphs she has rewritten seventeen times, something like the aesthetic Hilbert-space superposition of Chapter 13 — a paragraph that is simultaneously elegy and joke and neither has decohered. This is the tensor. The editor is not asking for the tensor. The editor is asking for a book. Maya must go from the tensor to a single one-dimensional object: a string of words that, read in order, constitutes a judgment about what this novel *is*. The projection is not optional. It is what the work being a book means. {#running-example}

## 15.1 The Moment of Judgment {#the-moment-of-judgment}

Throughout this book we have built a picture of aesthetic reality whose richness exceeds any single verdict. The manifold (Chapter 5) holds works across dimensions that a star rating cannot index. The tensor hierarchy (Chapter 6) distinguishes obligation-like from interest-like content. The metric (Chapter 9) encodes trade-offs. Stratification (Chapter 8) marks where the rules change. Dynamics (Chapter 10) makes evaluation path-dependent. Noether-style symmetry (Chapter 12), witnessed empirically at $\rho \approx 0.7$ across six language families, constrains what re-description can alter. Superposition (Chapter 13) allows framings to interfere before collapse. Collective agency (Chapter 14) generates canons that no individual reader holds.

This apparatus captures aesthetic structure with a precision the scalar picture does not. But at the moment of judgment — Maya cutting the manuscript, Hiroshi writing the catalogue, Daniel pushing the playlist live, the reader closing the book and saying, to themselves or to someone else, *I liked it* — we must act, and action is one-dimensional. We write one sentence. We acquire one painting. We give one star rating. We press *play* or *skip*.

The operation that performs this compression is *projection*: the dimensionality-reducing map from a tensor-structured space to the low-dimensional space action permits. The operation has a technical name — *contraction*, in tensor calculus, summation over paired indices. Ethics Chapter 15 calls it moral contraction. Aesthetic judgment is the same operation applied to the aesthetic tensor. The fundamental formula $V = I_\mu O^\mu$ (Chapter 6) is already a projection: the pairing of an interest covector with a valence vector to yield a scalar verdict. But $V = I_\mu O^\mu$ is not the only contraction available, and the choice of contraction is itself an aesthetic commitment — the site where judgment actually happens.

This chapter examines aesthetic projection philosophically. When is projection necessary? Who chooses how to project? What information does projection discard? And what aesthetic obligations persist after projection — the *residue* of what was contracted away?

## 15.2 The Mathematics of Projection {#the-mathematics-of-projection}

### Projection as Index Summation

Recall from Chapter 4 that contraction reduces tensor rank by pairing an upper index with a lower index and summing. A rank-(1,1) tensor $T^\mu_\nu$ contracts to a scalar
$$\mathrm{Tr}(T) = T^\mu_\mu = \sum_{\mu=1}^{d} T^\mu_\mu$$
where $d$ is the dimensionality of the underlying space. More generally, contracting a rank-$(p,q)$ tensor with a rank-$(r,s)$ tensor over $k$ paired indices yields a rank-$(p+r-k, q+s-k)$ tensor. Each contraction discards the information orthogonal to the pairing.

In aesthetics, the relevant projections are many. The three that structure most working practice are:

**The valence projection** $V = I_\mu O^\mu$. A reader's interest covector contracts against the work's valence vector to produce a one-dimensional "how much I liked it" scalar. This is what Goodreads asks for.

**The axis projection** $V_k = I^{(k)}_\mu O^\mu$ along a specific axis. A critic with a formalist interest covector $I^{(\text{formal})}$ contracts against the work's full valence vector and recovers the formalist component. A different covector recovers a different component. This is how specialised criticism operates.

**The cluster projection**, which maps a work to its nearest canonical cluster-centre (Chapter 14). This is what genre attribution and recommendation systems perform.

### The Projection Chain

In practice, judgments proceed through chains of projections.

**Step 1: Aggregating across perspectives.** The multi-reader collective tensor of Chapter 14 contracts over reader indices to yield a single-perspective evaluation. This is the social aggregation step. Arrow's impossibility theorem (1951) is, in this language, a statement about the non-commutativity of this contraction with the next step.

**Step 2: Aggregating across options.** A critic with a long-list contracts the per-work valence vectors down to an ordering, then to a winner. A reader chooses the next book by the same procedure.

**Step 3: Dimensional reduction within a work.** The $d$-dimensional valence tensor contracts to a single "verdict." The formula $V = I_\mu O^\mu$ lives at this step.

Each step discards information. The multi-reader tensor preserves the landscape of agreement; the single-perspective vector discards it. The option-vector preserves near-misses; the winner discards them. The dimensional reduction preserves which axes were engaged; the scalar discards them. What the reader (or the editor, or the curator) finally says aloud is typically the output of *all three* projections, composed.

### Non-commutativity

The order matters. Aggregating over readers first and then over dimensions yields a different verdict, in general, from aggregating over dimensions first (within each reader) and then over readers. Arrow (1951), Sen (1970), and the long tradition of social-choice results can be read as a body of statements about exactly this non-commutativity, translated from preference theory into tensor algebra.

This is not a bug. It is a feature: it makes visible that *how* we aggregate perspectives and *how* we reduce dimensions are independent aesthetic choices, and that the order of their application is itself a commitment.

## 15.3 Why Projection at All? {#why-projection-at-all}

If projection discards information — and it does, inevitably — why not keep the full tensor?

**Practical necessity.** At the moment of action we cannot act on a tensor. We can write one sentence, acquire one work, play one song. The effector systems of aesthetic agency — whether print editions, gallery walls, streaming slots, or a single reader's time — require a scalar command. The manuscript goes to press at one length. The painting is hung or it is not. The song is recommended or it is not. The world changes one step at a time, and each step is scalar.

**Cognitive necessity.** Even in deliberation we cannot hold the full tensor in view. Our 128-dim PCA spectrum is barely accessible to conscious inspection; the full LaBSE paragraph-tensor for a single book has millions of components. Working memory holds roughly four items. Projection is how we manage the gap between aesthetic complexity and cognitive capacity. What looks like *taste* — the snap judgment — is in many cases a heavily learned projection from a high-dimensional state to a one-dimensional verdict.

**Communicative necessity.** When we justify aesthetic choices to others, we offer projected reasons: *I loved it; I couldn't put it down; the pacing is slack in the middle; the colour palette doesn't resolve*. Full tensorial explanations — *the work's local `pair_sim_mean` is 0.83 at σ = 0.04, its `step_skew` is +0.31, its recurrence rate is 0.22* — are available in principle, and Chapter 17 shows they carry real signal. They are not how aesthetic talk naturally flows.

**The projection bottleneck.** Between aesthetic reality (tensorial) and aesthetic action (scalar), there is a bottleneck. Projection is how we pass through it. The bottleneck is not a deficiency of our theory. It is a structural feature of the relation between evaluation and action.

### The Cost of Premature Projection

If projection is necessary, its timing is not. Projecting too early — collapsing the tensor to a scalar before the tensor has been populated — discards information that might have changed the verdict.

Maya has been told by more than one senior novelist: *do not decide what the book is until the final pass*. This is a structural argument, not a superstition. An early commitment to a scalar identity ("this is a grief novel") projects the manuscript onto a single axis and makes the non-projected dimensions invisible to revision. Work that belonged on a second axis is cut or trimmed not because it failed its own axis but because it did not serve the projected one. The geometric framework licenses the novelists' advice: maintain the tensor as long as the medium permits; project only when the medium requires it; acknowledge what the projection discards.

## 15.4 Who Projects? {#who-projects}

Aesthetic projection happens at several levels. Naming the level matters, because different projectors have different accountability structures.

### The Agent

The individual reader, writer, or viewer chooses a projection — which axes to weight, which framings to prioritise, which trade-offs to accept. This is the sense in which aesthetic choice is "up to us" even when the tensorial structure of the work is (largely) shared. Two readers facing the same work with similar interest covectors may project differently — weighting coherence over novelty, say, or allowing genre-expectation to dominate form-expectation — and both may be reading legitimately.

### The Community

Communities have conventions about projection. A literary community that lexicographically prioritises *seriousness of intention* (Dimension X first, Dimension Y only if Dimension X is equal) is performing a community-level projection. A music-critic community that prioritises *novelty of texture* is performing another. These community projections are real constraints on individual criticism: a reviewer who departs too far from the community projection is read as being *about something else*.

### The Institution

Prizes, anthologies, syllabi, catalogues, and charts perform institutional projection. The Booker shortlist is a projection. The Pitchfork 8.0 is a projection. The MOMA acquisition list is a projection. Institutional projection has a distinctive feature: it is, at least in principle, explicit. The projection procedure is written down (or can be reconstructed), debatable, and revisable. This makes institutional projection more transparent than individual or community projection — and ties it to the governance account of Chapter 9.

### The Algorithm

In automated systems, projection is specified by the loss function. The choice of loss function is a choice of projection:
$$\text{Loss function} = \text{projection of the aesthetic tensor to a scalar optimisation target.}$$
Different loss functions embody different aesthetic theories. A recommender optimising click-through projects differently from one optimising long-session engagement, which projects differently from one optimising user-reported satisfaction, which projects differently from one optimising structural novelty. Chapter 18 returns to this: an *aesthetically misaligned* AI is often an AI running the wrong projection — compressing a rich tensor to a scalar that fails to preserve the information its users cared about.

## 15.5 Types of Projection {#types-of-projection}

The parallel to Ethics Chapter 15 §15.5 is exact. We recount the taxonomy aesthetically.

**Summative.** $V = \sum_\mu O^\mu$. Equal-weight aggregation across axes. In music this is the "it's pleasant" averaging that explains most commercial recommender behaviour.

**Weighted.** $V = \sum_\mu w_\mu O^\mu = I_\mu O^\mu$ with $w_\mu \geq 0$, $\sum w_\mu = 1$. The fundamental formula. Every aesthetic theory that yields a scalar verdict is a weighted projection — differing only in its weights. Kantian aesthetics weights disinterestedness; romantic aesthetics weights sincerity; formalist aesthetics weights structural economy; modernist aesthetics weights novelty. Disagreement between them is, in large part, disagreement about $w$.

**Maximin.** $V = \min_\mu O^\mu$. The work is only as good as its weakest dimension. This is the dominant projection in technical criticism of craft-heavy forms — filmmaking, architecture, instrumental music — where a single weak component propagates into the overall judgment.

**Lexicographic.** $V = (O^{\pi(1)}, O^{\pi(2)}, \ldots)_{\text{lex}}$. Absolute priority order. Some canonical traditions work this way: a sonata must first satisfy sonata-form constraints; all other dimensions enter only as tiebreakers.

**Satisficing.** $V = \mathbb{1}[\forall \mu : O^\mu \geq \tau_\mu]$. The threshold projection. Professional gatekeeping often operates satisficingly: the question is not *is it the best?* but *is it above the bar?*

**Probabilistic.** $V = \mathbb{E}[I_\mu O^\mu]$. Accounts for uncertainty in both the work's valence and the reader's interests. The covariance term $\sum_\mu \mathrm{Cov}(I_\mu, O^\mu)$ (Chapter 6 §6.6) becomes significant when reader-uncertainty correlates with work-uncertainty — the signature of an under-formed canon.

### What Unifies Them

Each is a different operation on the *same* tensor. The tensor does not change; the projection does. Much aesthetic disagreement reduces, on inspection, to disagreement about projection rather than disagreement about the work. Two critics who seem to disagree about whether a novel is good may in fact agree about its valence vector, its local metric, and its location on the manifold — and disagree only about whether to apply summative, maximin, or lexicographic projection. Identifying the projection disagreement clarifies the dispute even when it does not settle it.

## 15.6 The Information Lost {#the-information-lost}

A $d$-dimensional valence vector projects to a scalar. The ratio of information retained to information discarded is roughly $1 : d-1$. In our 128-dim PCA spectrum, that is $1 : 127$. What, specifically, is lost?

**Directional information.** The tensor tells us *which* axes are engaged — *in what respect* the work succeeds or fails. The scalar tells us only *how much*. A 4-star book and a 4-star book with the same scalar can be structurally unrelated.

**Relational information.** The tensor encodes relationships between axes — off-diagonal metric components, covariances, couplings. The scalar discards all of it.

**Perspectival information.** The collective tensor (Chapter 14) preserves the landscape of agreement and disagreement. The projection discards it.

**Near-miss information.** The scalar verdict "this is the best novel of the year" says nothing about how close the alternatives were, how the loser differed from the winner, whether the decision was unanimous or split 3–2. All of this is morally and aesthetically relevant — a contested canonisation merits different treatment from a consensual one — and all of it is discarded.

### The Scalar Irrecoverability Theorem (Aesthetic Form)

The information loss is not merely quantitative. It is structurally irrecoverable. The theorem of Ethics Chapter 15 transfers to aesthetics unchanged.

**Theorem 15.1 (Aesthetic Scalar Irrecoverability).** Let $Q: \mathbb{R}^d \to \mathbb{R}$ be any function mapping a $d$-dimensional aesthetic tensor to a scalar verdict. Then:

(i) $Q$ is not injective. Generically, the preimage of any scalar value is a $(d-1)$-dimensional submanifold of $\mathbb{R}^d$: multiple aesthetically distinct works map to the same scalar.

(ii) No function $\psi: \mathbb{R} \to \mathbb{R}^d$ recovers the tensor from the scalar. There is no $\psi \circ Q = \mathrm{id}$.

(iii) The geodesic on the full manifold $\mathcal{M}$ is in general different from the scalar-optimal path, and the divergence between them is not bounded by any function of $Q$ alone.

*Proof sketch.* (i) By rank-nullity, the kernel of $dQ$ at any regular point has dimension at least $d-1$. (ii) By the data processing inequality, information lost under a dimensionality-reducing map cannot be recovered downstream. (iii) Any path that maximises $Q$ is underspecified in the $(d-1)$ kernel dimensions; the true geodesic on $\mathcal{M}$ uses the full metric, which $Q$ does not see. □

**Aesthetic consequence.** The Goodreads-average canon is irrecoverable: no reader can, from the star rating alone, reconstruct the structural features (coherence, trajectory, recurrence) that produced the rating. Conversely, the structural-feature tensor is recoverable-in-principle from the text (that is what Chapter 17's R, effect sizes, and 17σ signal mean), and projecting that tensor to a star reverses-engineer-ably loses the content that made the projection non-trivial.

## 15.7 Aesthetic Residue {#aesthetic-residue}

Ethics Chapter 15 introduces *moral residue*: obligations that persist after a contracted decision has been made. The aesthetic analogue is *aesthetic residue*: commitments that persist after a work has been judged.

The manuscript that Maya cuts from 320k to 120k leaves a residue. The scenes that were good-on-their-axis but could not be kept under the projection the novel now enacts are not forgotten simply because the projection excluded them. They survive as the shape of a second book Maya might write, as letters to a reader who asks what was cut, as the author's own knowledge of what the book could have been. The projection produced a scalar (one manuscript); the residue is tensorial (everything that did not fit).

This is not metaphor. The residue has observable consequences. It shows up in the revision history. It shows up in the writer's second book. It shows up in fan-fiction, in deleted-scene features, in the translator's preface. The institution of *deleted scenes as a DVD bonus feature* is cultural acknowledgement that the residue of a projected aesthetic decision is itself valuable information — a measurement of the tensor made available after the primary projection has collapsed it.

For the critic, the residue is likewise real. A review that gives a book four stars and a thousand words of analysis has, in its scalar, lost most of what the thousand words carried. A serious reader treats the thousand words as the tensor that the four stars discarded. The *residue is the tensor, partially recovered*. Chapter 16 will argue that the uncertainty of this recovery is itself bounded below by a structural limit.

## 15.8 Deferred Projection {#deferred-projection}

A recurring wisdom across aesthetic practice is: *do not project until you must*. The novelist's "don't decide what the book is until the last pass." The curator's "live with the work on the wall for a month before you commit to the catalogue text." The critic's "do not write the review the night you finish the novel." The listener's "give the album three listens before you rate it."

Each of these is a version of *deferred projection*: keep the tensor populated as long as feasible; project only when action forces it. The geometric framework licenses this wisdom as a structural claim, not merely a professional superstition. A projection performed before the tensor is fully specified is a projection of a tensor that is itself wrong; the scalar verdict is then wrong for two separable reasons — the tensor was wrong, and the projection discarded axes that might have corrected it. Deferring the projection gives the tensor time to stabilise and increases the fraction of variance the projection can capture.

Chapter 16 sharpens this: even in the limit of infinite deference, there are structural limits to how accurately any projection can represent the tensor. Aesthetic uncertainty is not merely our ignorance; it is a geometric feature of the space.

## 15.9 The Phenomenology of Projection {#the-phenomenology-of-projection}

What does projection feel like from the inside?

It feels, typically, like *preference*. The reader closes the book and has the feeling *I liked it*. No conscious index summation is performed. No interest covector is contemplated. The projection is completed below the level of articulable reasoning and returns a scalar.

Trained practitioners report a different phenomenology: something closer to the interest covector being consciously available. A book critic can often articulate *which axes they weighted and why*; a painter can name which axes a work won or lost on; a chef can disaggregate a dish. The training is, in large part, an increase in the dimensionality of the conscious interest covector. An untrained reader with a 1-dim covector (roughly: *did I enjoy this*) projects from a high-dim tensor to a scalar through a single-axis contraction. A trained reader with a 10-dim covector performs the same structural operation but with enormously more information retained per axis before the final contraction.

This is the sense in which aesthetic training *is* the dimensional expansion of the interest covector. One does not teach someone to like what one likes; one teaches them to notice more of what is there. The projection that follows is then the projection of a richer tensor, and the verdict — even if it is still one-dimensional — reflects more of the structure than the naive projection did.

## 15.10 Projection in AI Systems {#projection-in-ai-systems}

Chapter 18 will take this up in detail. Three points to set up.

**The loss function is the projection.** When we train an aesthetic model on click-through rate, we are instructing the model to find weights $w_\mu$ that make the projection $V = w_\mu O^\mu$ correlate with clicks. The resulting $w$ is the model's aesthetic interest covector. It is neither correct nor incorrect — it is what we asked for. The common complaint that "the recommender optimises engagement, not quality" is, in this vocabulary, the correct observation that the projection chosen projects along the engagement axis and discards the quality-orthogonal axes.

**Multi-headed projection is possible.** Rather than a single scalar output, a model can output a low-dimensional vector — preserving some of the tensor's structure before the final projection is required. A recommender that surfaces "similar in texture," "similar in mood," "similar in form" is a multi-headed projection that pushes the projection bottleneck downstream from the model to the user. This is architecturally closer to the tensorial picture we have argued for.

**Deferred projection is implementable.** A model can compute the full tensor, store it, and project to a scalar only at the moment of user interaction — and can project *differently* for different users and different contexts. This is the architectural move Chapter 19's DEME-for-aesthetics formalises.

## 15.11 Summary and Bridge {#summary-and-bridge}

We argued:

Projection is necessary. Aesthetic action is one-dimensional; aesthetic reality is high-dimensional; the gap is bridged by projection.

Projection is lossy. The Scalar Irrecoverability Theorem (15.1) states the loss structurally: the kernel of any aesthetic projection is a $(d-1)$-dimensional submanifold, and the projected scalar cannot, in general, recover the tensor.

Projection is chosen. Summative, weighted, maximin, lexicographic, satisficing, probabilistic — each projection embodies an aesthetic theory. Much apparent disagreement about works is, on inspection, disagreement about projection.

Projection is the site of aesthetic commitment. What a reader, critic, or institution is committed to is not *what they like* in the abstract; it is *which projection they run*. The projection is where the structural richness of the tensor gets converted into the scalar the world requires, and the choice of conversion is the agent's.

Residue persists. What the projection discards does not vanish — it shows up in second drafts, deleted scenes, translator's prefaces, fan communities, marginalia, and the practitioner's own second book.

Maya's revision is now legible. She is not choosing what the book is *worth*; she is choosing the projection by which the tensor that is her manuscript becomes a single 120,000-word object. The rest — the 200,000 words that will not survive the projection — is the residue. It has consequences. It will be, in whatever form, part of her next book.

Chapter 16 takes the next step: we will argue that even with arbitrarily generous cognitive and communicative budgets, there are structural limits to how well any projection can represent the tensor — an aesthetic-uncertainty bound analogous to, but distinct from, the Robertson inequality of Chapter 13. Chapter 18 will ask what any of this means for artificial aesthetic agents. Chapter 19 will make the whole picture concrete in a reference architecture — DEME-for-aesthetics — where the tensor is maintained, the projection is deferred, and the residue is recorded as first-class data rather than discarded as implementation detail.
