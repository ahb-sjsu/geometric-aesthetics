# Chapter 16 — Aesthetic Uncertainty and the Limits of Geometric Determinacy

> *"Of that whereof one cannot speak, one must be silent."* — Wittgenstein, on a sentiment the aesthetician inherits and does not quite escape.

**RUNNING EXAMPLE — Maya's Manuscript**

Maya has been revising her novel for three years. The geometric analysis her editor commissioned returns four channel scores: a divergence profile in the high-coherence, small-step region occupied by nineteenth-century domestic realism; an internal-coherence statistic (`pair_sim_mean`) roughly one standard deviation above the English-fiction median; a trajectory that looks almost *too* smooth — `step_mean` a full standard deviation below the corpus; a recurrence rate that suggests the book circles a small number of emotional attractors. The report tells her, with unusual precision, what shape her book has. It does not tell her whether the book is good. It cannot tell her whether the first chapter, which two readers have called "impossible to get through" and two others have called "the best thing in the book", is a flaw or a feature. It cannot tell her whether the decision to withhold her narrator's name for 200 pages is brave or coy. What the geometric report produces is a coordinate. What Maya still has to do is judge.

## 16.1 What the Framework Cannot Settle {#16-1-what-the-framework-cannot-settle}

The preceding fifteen chapters have developed a mathematical account of aesthetic judgment — manifolds, tensors, metrics, stratification, dynamics, symmetries, quantum extension, collective canon-formation, and the philosophy of contraction from tensor to verdict. The account is real. It has been tested against hundreds of thousands of works in two modalities and nineteen languages (Chapter 17). It produces effect sizes that, while modest, are statistically unmistakable. It identifies structural channels — spectral divergence, internal coherence, trajectory geometry, genre axes — that are cross-lingually invariant at $\rho \approx 0.7$ across six language families.

And yet, after all this, the account is bounded. It characterizes aesthetic *structure*; it does not deliver aesthetic *verdicts*. It tells us what shape the embedding cloud of a work has; it does not tell us whether the cloud is beautiful. It locates the work in a manifold; it does not rank the locations.

This chapter inventories the limits. The inventory is long, and some of the items are load-bearing. We do not present them as defects. A framework that claimed to settle every aesthetic question would be overreaching in a domain where overreach has a long and embarrassing history. The humility of the geometric account — its ability to say, with precision, *here is where I fall silent* — is a feature of the account, not a concession.

The chapter parallels the corresponding moral-uncertainty chapter of *Geometric Ethics* (Ch 16). Where the moral framework encounters empirical, metric, and theory uncertainty, the aesthetic framework encounters observational, representational, and normative uncertainty. Where the moral framework offers a "robust core" of obligations that survive across theories, the aesthetic framework offers a more modest claim: a robust core of *structural descriptions* that survive across single-observer readings, but not a core of *verdicts*. That asymmetry is what this chapter is mostly about.

## 16.2 The Four Limits {#16-2-the-four-limits}

We identify four places where the geometric account bottoms out. Each is distinct in kind, and each demands a different intellectual response.

1. **Observational uncertainty.** Recovery of a work's geometry from noisy single-observer data is slow and expensive. One reading is not enough; sometimes ten are not enough.
2. **Pathological works.** Some works are *designed* to defeat statistical structure — deliberately random, deliberately flat, deliberately ill-posed. The framework returns a geometry, but the geometry is an artefact of the act of measurement rather than a property of the work.
3. **Modality reach.** The framework assumes a pretrained encoder capable of producing token-level embeddings. Live performance, conceptual art, relational aesthetics, and work whose aesthetic content is partly extra-object evade that assumption.
4. **The normative gap.** Geometric structure is a description of what is there. Aesthetic judgment is a claim about what is good. No amount of geometric information, by itself, crosses that gap.

Each of the four limits is real. We treat them in turn.

## 16.3 Observational Uncertainty: How Many Readings Before the Book Has a Shape? {#16-3-observational-uncertainty}

The most immediate limit is practical. The geometric account requires, as input, an embedding cloud $X(W) = \{\phi(t_1), \ldots, \phi(t_N)\}$ produced by tokenizing a work and encoding each token. For written texts this tokenization is straightforward — paragraphs, sentences — because the object has stable token boundaries. For music it is a 30-second windowing decision. For a film or a gallery installation, the tokenization is not given by the object. It is given by *how the observer reads the object*.

And a single observer, reading once, produces a noisy estimate of the cloud. The paragraph boundaries they attend to are not the paragraph boundaries another reader would attend to. The moments where their attention drifts are not the moments another reader's attention drifts. The resulting cloud is a convolution of the work's true structure with the observer's reading trajectory.

How many readings does it take to stabilize the cloud? We do not have a complete answer. For the books corpus of Chapter 17 we had the luxury of complete, stable tokenizations (Gutenberg plaintext, paragraph-split) and a single pretrained encoder (LaBSE) whose outputs are deterministic given an input. The noise in our estimate of $X(W)$ was therefore encoder-internal, not observer-driven. For a human reader, or for an AI agent whose attention distribution is itself a learned object, the situation is different.

We can give a back-of-the-envelope bound. Consider the rank-2 covariance summary $\Sigma(W)$ of the embedding cloud. For an observer sampling tokens stochastically from the work, the covariance estimate $\hat\Sigma$ converges to the true $\Sigma$ at rate $O(1/\sqrt{n})$ where $n$ is the number of tokens attended to. To resolve a spectral divergence at the $0.1\sigma$ level against a corpus prior, roughly $n \gtrsim 10^2$ attended tokens are required. For a short story this is tractable; for a 900-page novel, a single reading almost certainly undersamples the work.

The operational implication: **single-observer aesthetic geometry is a noisy estimate.** Aggregating across readers — either literal (multi-reader studies) or computational (multiple stochastic pass-throughs by an AI reader) — is not optional if the geometric descriptors are to stabilize. The book-is-a-cloud metaphor (Chapter 5) is only approximately true in the single-observer case. A more honest statement: *the book is a cloud in the limit of many attentive observers*. Short of that limit, the cloud is Monte Carlo.

This is a recoverable limit — more readings, more compute, better attention models — but it is a real one, and any practitioner who treats a single geometric report as definitive is overinterpreting the object.

## 16.4 Pathological Works: When the Work Is Designed to Defeat Geometry {#16-4-pathological-works}

A subtler limit arises with works whose aesthetic program is the deliberate violation of the statistical regularities the framework measures.

**The cut-up.** William Burroughs' *The Soft Machine* and *Nova Express* were composed partly by cutting up prose and rearranging fragments at random. The intent is to defeat narrative trajectory; the result is an embedding cloud whose `step_mean` is artefactually large, whose `recur_rate` collapses, whose internal coherence is low. The geometric account correctly identifies the cloud as anomalous relative to the corpus — indeed, the Lasso-on-PCA-spectrum features (Chapter 17, §17.3) would flag Burroughs as a high-divergence outlier. What the account cannot do is distinguish *deliberate* disarray (an aesthetic program with a specific literary-historical location in the Beat-through-postmodern lineage) from *incompetent* disarray. Both produce similar cloud geometries. The judgment that Burroughs' disarray is the good kind is a judgment the geometry does not make.

**Minimalism.** At the other pole: Agnes Martin's grid paintings, Morton Feldman's late piano works, Gordon Matta-Clark's cuttings, La Monte Young's drone compositions. The aesthetic program is deliberate flatness — suppression of variation, refusal of narrative, repetition as content. In the embedding cloud, these works present as anomalously *low* `step_mean`, anomalously *high* `pair_sim_mean`, sometimes near-degenerate rank-2 covariance. The framework reports them as edge cases. Whether the edge case is transcendent or empty is again not a question the framework answers. (The within-genre null results on Classical music — $R = -0.013$, $n = 584$, Chapter 17 — are a hint that corners of the aesthetic space where intentional flatness is a stylistic norm may be regions where listener response becomes decoupled from the geometric signal the framework tracks.)

**The deliberately ill-posed.** Samuel Beckett's late prose — *Worstward Ho*, *Ill Seen Ill Said*, the *Nohow On* trilogy — stages the collapse of the sentence as sentence, of reference as reference, of narrative as narrative. The embedding cloud shrinks to a tight region of the manifold, its divergence from the corpus high because the corpus is modeled on conventional prose, its internal coherence high in a degenerate sense because the work is circling a single collapsing image. *Worstward Ho* and a badly-written repetitive fragment may appear numerically similar. The geometric account reports a shape. The aesthetic fact — that Beckett's collapse is the most controlled prose in twentieth-century English — is not in the report.

In each case, the framework is not *wrong*. It correctly identifies these works as unusual. What it does not do — what no feature-extraction account can do without external art-historical knowledge — is situate the unusualness as achievement rather than failure. We return to this normative gap in §16.7.

## 16.5 Modalities Outside Encoder Reach {#16-5-modalities-outside-encoder-reach}

The framework assumes an encoder $\phi$ that maps content units to vectors in a representation space. The account's empirical leverage (Chapter 17) came from two such encoders: LaBSE for multilingual text and MERT-v1-330M for music. Both map stably-tokenizable objects (paragraphs, 30-second audio windows) to $\mathbb{R}^d$.

Several aesthetic modalities do not admit such a map without strong and possibly lossy simplifications:

**Live performance.** A theatrical production is not identical across nights. The embedding of a performance — if we attempted one — would have to be of a *recording* of a performance, which is already a different object. What is aesthetically central to live performance (the energy of the room, the interplay with audience response, the unrepeatable contingency of the evening) is not in any audio or video stream.

**Conceptual art.** Duchamp's *Fountain* is a urinal signed "R. Mutt". The aesthetic content of the piece is almost entirely the *proposition it makes* — that signing a mass-produced object and placing it in a gallery context is sufficient for the object to become art. No embedding of the physical urinal recovers that content. The embedding is of the wrong object. Sol LeWitt's wall-drawing instructions, Robert Barry's *Telepathic Piece* (1969 — "during the exhibition I will try to communicate telepathically a work of art, the nature of which is a series of thoughts..."), On Kawara's date paintings — in each case the work's aesthetic content is propositional, relational, or gestural. An encoder trained on pixels or audio samples operates on the wrong input.

**Relational aesthetics.** Rirkrit Tiravanija cooking Thai curry for gallery visitors; Tino Sehgal's purely verbal instructions to gallery attendants; Félix González-Torres' candy piles where visitors are invited to take pieces. The aesthetic object is an event of interaction, not a static artefact. Tokenization is not defined.

**Site-specific work.** Richard Serra's *Tilted Arc*, Robert Smithson's *Spiral Jetty*, Christo and Jeanne-Claude's wrapped landscapes. The work is in part the specific physical location. A photograph is not the work.

For each of these modalities we can construct *some* encoder — a multimodal vision-language model for the photograph of the work, an LLM-based description-embedding of the concept, a transcript-based embedding of the performance. But the encoder is always a lossy proxy, and the lossiness is not uniform across the aesthetic dimensions we care about. A conceptual piece loses more in the encoding than a novel does.

This is a limit of the current tool, not necessarily of the framework in principle. Better encoders will close some of the gap. But the framework is at present meaningfully constrained to the modalities for which stable, aesthetic-content-preserving encoders exist.

## 16.6 The Headline Asymmetry: 85% Genre, 5–9% R² {#16-6-the-headline-asymmetry}

We now come to the observation that, more than any philosophical argument, constrains the framework's claims.

The empirical account of Chapter 17 reports that after within-genre controls, the residualized correlation between geometric features and observed ratings falls to $R = 0.093$, $R^2 = 0.009$ — meaning that the framework explains roughly one per cent of the variance in aesthetic response *once genre is controlled for*. Before residualization, the raw figure was $R = 0.241$, $R^2 = 0.058$. **Eighty-five percent of the headline $R^2$ was genre confound.** For music the figure was worse — 91% of the hand-feature $R^2$ was genre confound, with MERT-spectrum features recovering more but still bounded (Chapter 17, §17.4).

We cannot emphasize this enough: **the geometric account captures, optimistically, 5–9 percent of whatever is driving aesthetic response, and a smaller residual fraction once genre is controlled.** This is a real effect — the statistical significance is extreme ($z = 6.5$ to $28.3$, depending on modality and control set; the EN↔FI Hellinger invariance alone is $p = 8 \times 10^{-57}$) — but it is also a small effect in absolute terms. Roughly **ninety percent of the variance in aesthetic response is not explained by the geometric features we have.**

What is in the other ninety percent?

**Mood and context.** A reader's rating of the same novel can shift by a full star between their twenties and their forties, or between a difficult week and a restful one. The book is unchanged; the geometry is unchanged; the response is different.

**Social transmission.** Ratings are contaminated by what a reader has heard about a book, by what their in-group reads, by the recommendation that brought them to the work. Goodreads ratings on *To Kill a Mockingbird* are not independent observations of the book — they are substantially observations of the book's cultural status.

**Reader-work fit.** A reader who loves Dostoyevsky may hate Austen, not because one writer is better than the other but because the reader's interest covector (Chapter 6's metaphor transferred here) has a different orientation in the aesthetic manifold. Our ratings data aggregate over this heterogeneity.

**The ineliminable surface of taste.** Some readers prefer short sentences. Some prefer long paragraphs. Some cannot abide second-person narration. These preferences are idiosyncratic, stable within a reader, and not obviously tracked by the high-level geometric channels the framework measures.

**Genre-specific craft.** The null within-genre results on Classical music and Jazz ($R = -0.013$ and $R = 0.031$ respectively, Chapter 17 §17.4) suggest that some genres operate on craft dimensions that the MERT-v1-330M encoder, trained primarily on popular-music tagging tasks, does not represent well. In these cases the framework sees very little, and honestly reports that it sees very little.

The right summary is this: *the geometric framework captures a real but bounded portion of aesthetic response. The bound is not incidental — it is approximately where one would expect a content-only, context-free, mood-independent account to bottom out.* Much of what we call aesthetic judgment is social, contextual, mood-dependent, and reader-specific. The geometric account does not pretend otherwise.

## 16.7 The Normative Gap {#16-7-the-normative-gap}

The deepest limit is not empirical. It is philosophical.

The geometric account maps a work to a location in a manifold. The location is a description: coordinates, channel values, divergences from a prior, trajectory shape. Descriptions are, by their nature, non-normative. Nothing in a coordinate tells you whether the coordinate is where a good work should live.

A framework that conflated description with evaluation would be committing the aesthetic analogue of the naturalistic fallacy. *That* the manifold has structure, *that* works occupy locations, *that* locations co-vary with ratings — none of this, by itself, licenses the claim that any particular location is aesthetically preferable.

The inferential move from geometry to verdict always requires an external input:

- an **interest covector** $I_\mu$ in the manifold's cotangent space, specifying which channels count and with what sign (Chapter 6);
- a **contraction procedure** $C$ that reduces the tensor-valued description to a scalar verdict (Chapter 15);
- a **community** whose aesthetic commitments the covector and contraction are answerable to (Chapter 14).

Different communities, holding different covectors, will rank the same manifold differently. A reader who prizes formal continuity (high `pair_sim_mean`, low `step_mean`) will rate Jamesian novels above Burroughsian ones; a reader who prizes disruption will reverse the ranking. *The geometry is the same; the verdicts differ.* No fact about the geometry adjudicates between the covectors.

This parallels the moral-framework asymmetry of *Geometric Ethics* Ch 16: the tensor structure of a moral situation is theory-neutral; the verdict is theory-relative. In aesthetics the asymmetry is, if anything, more acute, because the community of relevant judges is less constrained — we have no aesthetic analogue of the weak convergence claim that most ethical traditions at least agree on certain welfare-positive directions. Aesthetic interest covectors vary sharply even within a single culture.

What we can do, and do claim: we can make the disagreement *localizable*. Two critics who seem to disagree about everything can, in the tensorial vocabulary, often be shown to agree on the manifold, agree on the rank-2 summary, agree on seven of eight trajectory statistics, and disagree only on the sign they assign to `step_mean`. That is a genuine advance — it turns an inarticulate clash of tastes into a tractable disagreement about a single channel — but it does not settle the disagreement.

## 16.8 A Robust Core, but of Descriptions, Not Verdicts {#16-8-robust-core-descriptions-not-verdicts}

The moral framework (Ethics Ch 16, §16.6) identifies a *robust core* of obligations — actions whose evaluation has positive sign under all plausible theories. Does the aesthetic framework admit an analogue?

We think it does, but at a different level. The aesthetic robust core is not a core of *verdicts* but a core of *descriptions*.

**What is robust.** The cross-lingual invariance result of Chapter 17 — `pair_sim_mean` at $\rho = +0.712$, `mahal_mean` at $\rho = +0.710$, Hellinger at $\rho = +0.675$, averaged across ten language pairs from six families — is a claim about *descriptions*, not verdicts. It says: the geometry we extract is approximately the same object regardless of which language the book was written in. That is a non-trivial empirical invariance. It survives Finnish-to-English transfer at $\rho = 0.77$, $p = 8 \times 10^{-57}$. The description is robust.

**What is not.** The sign of the description's contribution to rating is *not* cross-modality invariant. `pair_sim_mean` is positive-valued for books ($\rho = +0.126$, $8.4\sigma$) and negative-valued for music ($\rho = -0.076$, $p = 5 \times 10^{-33}$); `step_mean` flips the other way. The *verdict* the geometry supports is modality-relative. Readers want continuity; listeners want contrast. The robust geometric description licenses opposite aesthetic verdicts in opposite modalities.

This is not a flaw. It is precisely the result the framework would predict: description is the structurally invariant layer; contraction is the modality- and community-relative layer. The normative gap has geometric content.

## 16.9 Strategies Under Aesthetic Uncertainty {#16-9-strategies-under-aesthetic-uncertainty}

What should a practitioner — a curator, a critic, a recommender system, a novelist revising her manuscript — do when the framework falls silent?

**Seek more observations.** Single-observer geometry is noisy; multi-observer geometry is more stable. When the framework's verdict is sensitive to observation count, collect more observations before committing.

**Report the tensor, not the scalar.** A reviewer who writes "this book is a 3" has already performed a lossy contraction. A reviewer who writes "the coherence is high, the trajectory is smooth, the divergence from the corpus prior is moderate, and within the domestic-realism stratum the work is unusual in its powerlaw tail" has reported the tensor. The reader can then perform their own contraction. This is the aesthetic analogue of the moral transparency principle.

**Flag the genre confound.** Any claim about a work's aesthetic quality that depends on the work's absolute position in the manifold, rather than its within-genre position, is resting on ground that the $R = 0.093$ result warns against. Prefer within-stratum judgments.

**Acknowledge the normative gap.** The framework describes the work. The verdict is yours. The framework's most useful contribution is often not an answer but a more precise formulation of the question: *given this geometry, and given your aesthetic commitments, does this work satisfy them?*

**Do not use the framework where it cannot see.** For conceptual art, relational aesthetics, pure performance, and work whose content is substantially propositional, the geometric account is not the right tool. A tool that misrepresents its reach discredits its genuine reach.

## 16.10 The Modesty of the Framework {#16-10-the-modesty-of-the-framework}

The geometric account of aesthetics makes specific, bounded claims:

*It claims:* Aesthetic works have measurable geometric structure in pretrained representation spaces.
*It does not claim:* That structure is sufficient to issue aesthetic verdicts.

*It claims:* The structure is partly invariant across languages ($\rho \approx 0.7$ on core features, 19 languages, 6 families).
*It does not claim:* The structure is invariant across observers, moods, or historical moments.

*It claims:* The contribution of geometric structure to observed ratings is real ($z = 6.5$ after genre controls, $p = 5.7 \times 10^{-11}$, $n = 4,998$).
*It does not claim:* That contribution is large. It is approximately 1% of residual variance, 5–9% of raw variance.

*It claims:* The sign of a channel's contribution to rating is modality-specific in ways that are statistically robust ($p < 10^{-28}$ for the books–music sign flip on `pair_sim_mean` and `step_mean`).
*It does not claim:* The modality-specific signs are the whole story of modality. They are one well-measured piece of a much larger modality-difference.

*It claims:* The framework's vocabulary — manifolds, tensors, divergences, trajectories, contractions — enables previously inarticulate aesthetic disagreements to be localized to specific channels.
*It does not claim:* Localization resolves disagreement.

The reader who has followed the account this far — who has taken on the mathematical apparatus, the empirical results, the philosophical commitments — is owed an honest statement of what they have bought. They have bought: a vocabulary. A structural account of where aesthetic content lives. A testable, falsifiable, replicable methodology. A set of empirical invariances that we did not expect and did not design for. And a principled delineation of the framework's own limits.

They have not bought: an aesthetic oracle. They have not bought: a replacement for taste, for criticism, for community, for the slow accumulated judgment of readers and listeners and viewers over time. They have not bought: a resolution of the normative gap between description and verdict.

This is, we think, the right purchase to have made. A framework that claimed more would be making claims the evidence does not support. A framework that claimed less would be understating a real and measurable phenomenon. The geometric account of aesthetics is modest, in the strict sense: it sits where the evidence puts it, and no further.

## 16.11 Bridge to Chapter 17 {#16-11-bridge}

Chapter 17 presents the empirical evidence in detail. The reader should approach that chapter with the caveats of this one in mind. The numbers are real; the numbers are bounded; the numbers are exactly what an honest geometric account of a partially-structured, partially-social, partially-contextual phenomenon should look like. After Chapter 17, we turn (Chapter 18) to what this framework implies for artificial agents that must generate, curate, or evaluate aesthetic works — and (Chapter 19) to the architecture such an agent would require if we took the limits of this chapter seriously.
