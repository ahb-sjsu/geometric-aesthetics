# Chapter 18 — Geometric Aesthetics for Artificial Agents

> *"The question is not whether machines can make art, but whether the art they make has structure we can recognize, evaluate, and govern."*

**RUNNING EXAMPLE — Daniel's Recommender**

Daniel runs the music-recommendation stack at a mid-sized streaming service. His current system optimizes a single scalar: the probability that a user will finish the track. The model is a gradient-boosted ensemble over Spotify-style hand-engineered acoustic features — tempo, energy, valence, danceability, acousticness, instrumentalness, liveness, speechiness. It does well on engagement metrics. It also produces the canonical failure mode of streaming recommenders: within six weeks of a new user's sign-up, their feed has collapsed onto three adjacent points in the genre space, and every song they are offered is a small perturbation of every other song. Listening time is up. Reported listener satisfaction is flat. The tail of the catalogue is unvisited. Daniel has read the Chapter 17 result — MERT spectrum features beat Spotify's eight hand features 2.2× ($R = 0.225$ vs $R = 0.103$, $p = 0.001$) on the same $n = 5{,}233$ tracks — and he is considering a rebuild. What should the rebuilt system actually optimize? What does the geometric framework, pushed to its engineering consequences, recommend?

## 18.1 Why Artificial Agents Need Aesthetic Geometry {#18-1-why-agents-need-aesthetic-geometry}

The preceding seventeen chapters have developed a mathematical framework for aesthetic judgment. The framework was motivated by a structural claim: that aesthetic response has multi-dimensional content, and that collapsing that content to a scalar — a star rating, a thumbs-up, a finish-rate, a listens count — destroys information that matters. Chapters 2 through 15 made the case philosophically. Chapter 17 made it empirically. Chapter 16 established its limits.

Nowhere is the scalar-collapse problem more consequential, and more urgent, than in artificial agents that generate, curate, or evaluate aesthetic works.

Three classes of system are implicated. **Generative models** — diffusion models for images, transformers for text, autoregressive audio models — sample from learned distributions over aesthetic objects. **Recommendation systems** rank aesthetic objects for users, and in doing so participate in aesthetic judgment at industrial scale. **AI curators** — increasingly being proposed for gallery programming, festival selection, editorial assistance — attempt to perform aesthetic judgment directly. Each sits at a different layer of the geometric framework; each inherits a different subset of its problems.

This chapter considers what the framework implies for the design of each. The chapter parallels *Geometric Ethics* Ch 18 (Geometric Ethics for Artificial Agents), which argued for tensor-valued objectives, invariance-as-alignment, and explicit contraction as design principles for morally-significant AI. The aesthetic analogues, we will argue, are:

- **tensor-valued aesthetic targets** rather than scalar reward signals,
- **learned-representation geometry** rather than hand-engineered features,
- **multi-channel optimization** with explicit contraction rather than opaque scalar aggregation,
- **invariance constraints** that preserve aesthetic coherence under description-equivalent perturbations, and
- **pluralism-preserving curation** that resists the engagement-maximization collapse.

We take each in turn.

## 18.2 The Scalar-Reward Failure Modes {#18-2-scalar-reward-failure-modes}

A streaming service that optimizes expected listens-per-session is optimizing a scalar. A recommender that optimizes click-through is optimizing a scalar. A text-generation model whose RLHF reward head produces a single quality score is optimizing a scalar. Each of these systems collapses a tensor-valued evaluation to a one-dimensional objective, and each inherits the failure modes Chapter 15 predicted.

**Failure 1: Manifold collapse.** A recommender optimizing engagement discovers, empirically, that users who are offered small perturbations of songs they have liked in the past engage more reliably than users offered exploration. The system learns to concentrate recommendations in a small neighborhood of the manifold. Over time the neighborhood shrinks. Users who started with broad tastes end up in "filter bubbles" not because anyone designed them to be there but because the scalar optimization converges on a local basin of the aesthetic manifold. This is the geometric content of the filter-bubble critique: *engagement-maximization is an attractor in the aesthetic manifold, and nearby points flow toward it*. Chapter 26 develops this in detail for AI curation.

**Failure 2: Cross-modality sign inversion.** Chapter 17's most striking finding was that the same geometric channel predicts opposite responses in different modalities. In books, higher `pair_sim_mean` (internal coherence) predicts higher rating, $\rho = +0.126$ at $8.4\sigma$. In music, higher `pair_sim_mean` predicts *fewer* listens, $\rho = -0.076$ at $p = 5 \times 10^{-33}$. A scalar optimizer trained on a mixed corpus will learn a compromise weight that is wrong for both. A tensor-valued system can track coherence separately for text and audio and apply the modality-appropriate sign. Scalar reward cannot.

**Failure 3: Genre confound masquerading as quality.** Chapter 17's within-genre controls demonstrated that 85% of the raw books $R^2$ and 91% of the raw music $R^2$ are genre effects rather than aesthetic-quality effects. A scalar optimizer that does not control for genre will interpret "song is in the popular-genre cluster" as "song is good" — effectively, the optimizer learns to recommend within the modal genre and nothing else. A geometric system that separates genre coordinates from within-stratum aesthetic coordinates can recommend a good country song to a user who likes country even when most of the catalogue's engagement is concentrated in pop.

**Failure 4: Reward hacking via style proxies.** Generative models conditioned on scalar preference rewards have been documented to produce outputs that exploit the reward model's biases — excessive fluency at the expense of content, excessive agreeableness at the expense of accuracy, excessive stylistic consistency at the expense of variety. These are aesthetic analogues of the specification-gaming phenomena catalogued in the AI-safety literature. In the framework's vocabulary: the scalar reward is a lossy contraction of a richer aesthetic tensor, and the generator learns to exploit the many-to-one character of the contraction.

Each failure mode is a specific instance of the general principle that a scalar reward is a specific contraction of a tensor-valued evaluation, and the specific contraction discards specific information. The remedy is not "a better scalar" — there is no scalar that avoids the trade-offs, because the trade-offs are what scalar collapse *is*. The remedy is to push the contraction downstream, so that the system maintains the tensor as long as possible and only collapses at the last step, under explicit control.

## 18.3 Tensor-Valued Aesthetic Targets {#18-3-tensor-valued-targets}

The first design principle: **an artificial aesthetic agent should maintain a vector-valued or tensor-valued evaluation throughout its decision pipeline, collapsing to scalar only when action is required.**

Concretely, a tensor-valued aesthetic target $T^\mu$ for a work $W$ has components along the four channels identified in Chapter 17:

- $T^1$: **divergence channel** — the work's distributional distance from a reference corpus (KL, JS, Hellinger, Bhattacharyya, Mahalanobis-mean, TV). The ~8σ-each significance of these features across languages says this channel carries real aesthetic signal.
- $T^2$: **coherence channel** — `pair_sim_mean` and `pair_sim_std`. 8.4σ in books, and the sign is modality-specific.
- $T^3$: **trajectory channel** — `step_mean`, `step_std`, `step_skew`, `recur_rate`, `acf1_top3`, `curvature`, `path_eff`, `powerlaw_slope`, `tail_mass_100`. Individually 3–6σ; jointly informative about the temporal shape of the work.
- $T^4$: **genre-axis channel** — the 71 non-zero interpretable axes recovered by Lasso on the PCA-128 spectrum (Chapter 17 §17.3). These are the discovered genre coordinates; they are *not* confounds to be removed from a recommender, they are the coordinates a recommender should know it is operating in.

The tensor value is:
$$
T^\mu(W) = (T^1(W),\; T^2(W),\; T^3(W),\; T^4(W)) \in \mathbb{R}^d
$$
where $d$ is the total dimensionality across channels (roughly 25–30 for our implementation). The agent's policy is then a function of the tensor, not of its scalar contraction. A rank-2 extension — a tensor $T^{\mu}_\nu$ with stakeholder-dimension $\nu$ representing different user-profiles on the manifold — is the natural generalization for recommendation.

The contraction from tensor to action is a separate, auditable step:
$$
S(W; I) = I_\mu T^\mu(W)
$$
where $I_\mu$ is the interest covector — the weights that specify which channels matter and with what sign for the particular user, context, or curatorial objective. **The covector is not learned from engagement data; it is specified by governance.** This is the aesthetic analogue of the ethics-framework separation of tensor representation from contraction decision (Ethics Ch 18, §18.3).

## 18.4 Learned-Representation Geometry Beats Hand Features {#18-4-learned-representations}

The second design principle is an empirical lesson from Chapter 17.

On the shared $n = 5{,}233$ FMA tracks with Echonest metadata, the head-to-head comparison was:

- MERT-v1-330M Lasso on PCA spectrum: $R = 0.225$
- MERT hand features: $R = 0.151$
- Spotify's 8 acoustic features: $R = 0.103$

Bootstrap difference MERT-spectrum vs Spotify hand features: $p = 0.001$. **MERT-geometry beat Spotify hand features by a factor of 2.2 in correlation.** The gap is not marginal; it is the difference between a recommender that sees twice as much aesthetic signal.

The design implication is direct: *aesthetic prediction pipelines should optimize on learned-representation geometry, not on hand-crafted acoustic or textual features.* The hand features are interpretable but lossy. The learned representations are less interpretable but capture dimensions of aesthetic content the hand features demonstrably miss.

This is not a claim that MERT is the "right" encoder — Chapter 17's methodological notes (§17.8) list the known failure modes, including the Hellinger-saturation problem at high ambient dimension. It is a claim that *some* learned-representation geometry is, in current practice, meaningfully better than any hand-feature set we know how to construct. A generative or curatorial system that does not operate in such a space is leaving a factor-of-two improvement on the table.

There is a governance consequence. Hand features are auditable in the straightforward sense that an engineer can read off "tempo = 128 bpm, energy = 0.7, valence = 0.3". Learned-representation features are not auditable in that sense. The framework's response is that auditability should be moved from the feature level to the *channel level*: the agent must report which of the four geometric channels (divergence, coherence, trajectory, genre-axis) drove its decision, even if the individual PCA component values are opaque. This is the aesthetic analogue of the ethics-framework audit requirement (Ethics Ch 18, §18.3, Req. 3): the output is accompanied by the tensor and the contraction, not by the raw feature values.

## 18.5 Invariance as Aesthetic Alignment {#18-5-invariance-as-alignment}

Chapter 17's strongest finding was cross-lingual invariance. The geometry recovered from English Gutenberg text was the same geometry, at $\rho \approx 0.7$, recovered from Finnish, French, German, Dutch, Italian, Spanish, Greek, Esperanto, Hungarian, and Latin text — 19 languages, 6 language families, $n = 4{,}683$ non-English books, with the EN↔FI Hellinger correlation at $\rho = 0.77$, $p = 8 \times 10^{-57}$. This is the aesthetic equivalent of the Bond Invariance Principle: *aesthetic structure is invariant under admissible re-descriptions of the work.*

For artificial agents, this translates into a concrete alignment criterion: **an aesthetic AI is aligned to the extent that its evaluations are invariant under transformations that ought to leave aesthetic content unchanged.**

Examples of required invariances:

- **Translation invariance.** A recommender that recommends *Anna Karenina* to a user should recommend it at the same rank whether the user's library is in Russian, English, or French. The invariance result of Chapter 17 says this is possible; an aligned system is one that achieves it.
- **Format invariance.** An aesthetic agent evaluating a novel should return the same evaluation for a plain-text version, an EPUB, and a cleanly-extracted PDF. The invariance result extends: small encoding-format differences should not propagate to large evaluation differences.
- **Tokenization invariance.** The cloud-based evaluation (Chapter 5) should be robust to reasonable variations in how the work is tokenized — paragraph split, sentence split, fixed-window split — for tokenizations that preserve content structure.
- **Order-invariance at the rank-2 level.** The covariance summary $\Sigma(W)$ is order-invariant by construction. The trajectory channel is order-sensitive. An agent should track which parts of its evaluation are gauge-invariant at which rank.

An aesthetic agent that fails these invariances is not merely performing poorly — it is performing a specific kind of misalignment. It is treating descriptively-irrelevant features of the input (its language, its format, its tokenization) as aesthetically relevant. The BIP methodology from the ethics framework transfers directly: generate transformation suites of equivalent inputs, evaluate the system on each, and measure the variance of outputs. A low-variance system is aesthetically well-aligned; a high-variance system is not.

The quantitative target for aesthetic invariance should be calibrated against the cross-lingual result. The within-bundle standard deviations reported in Chapter 17 (§17.5) — `path_eff` 0.18, `recur_rate` 0.28, divergence family 0.39–0.44 (ratios of within-bundle to between-book SD) — give concrete benchmarks. A system whose evaluations shift by more than, say, 0.3–0.4 between English and French versions of the same work is less aesthetically-invariant than the underlying manifold geometry is.

## 18.6 The Engagement-Maximization Trap {#18-6-engagement-maximization-trap}

Chapter 26 will develop the filter-bubble critique at length. This section states the framework's warning at the architectural level.

Any recommender that optimizes a scalar engagement proxy — time-on-platform, completion rate, thumbs-up probability — is subject to a theorem that is in large part geometric rather than social.

**Claim (informal).** *Under a scalar engagement objective, the policy's long-run stationary distribution over recommended works concentrates on a subset of the aesthetic manifold whose diameter is bounded above by the correlation scale of the user's engagement signal.*

The intuition: the system recommends a work, observes engagement, updates. If a work at manifold location $p$ produces high engagement, nearby works — locations within some neighborhood of $p$ determined by the encoder's Lipschitz constant and the noise in the engagement signal — will also produce high engagement. The policy's gradient points into the neighborhood. Over iterations, recommendations concentrate. This is not a failure of implementation; it is what gradient ascent on a noisy reward landscape does.

A tensor-valued objective with explicit multi-channel contraction resists this dynamic, if the contraction includes terms that penalize concentration. Specifically, if the interest covector $I_\mu$ includes a *divergence-reward* component — a positive weight on the divergence channel $T^1$ — then works at the periphery of the manifold, which have high divergence from the typical-user prior, are incentivized even when their engagement is below median. The policy does not collapse onto the engagement attractor because the objective is not purely engagement-indexed.

This is not a hypothetical architecture. It is the concrete consequence of building a recommender around Chapter 17's tensor rather than around a scalar. The governance-specified weights $I_\mu$ can be set to prioritize catalogue exploration, aesthetic diversity, within-stratum quality, or any combination — and the *choice is transparent and auditable* rather than buried in an opaque reward model.

The warning, stated sharply: *a system whose only optimization target is engagement cannot, as a mathematical matter, avoid the filter-bubble attractor. Escaping it requires building the objective around the geometry, not around the scalar.*

## 18.7 Generative Models: Conditioning on Aesthetic Targets {#18-7-generative-models}

The argument transfers to generative systems with minor modifications. A diffusion model trained with classifier-free guidance samples from a conditional distribution $p(W \mid c)$ where $c$ is a conditioning signal — a text prompt, a style tag, a preference signal. Most current systems condition on scalar or nearly-scalar signals (text embeddings flattened to a single vector, preference scores).

The framework proposes **multi-channel aesthetic conditioning**: conditioning the generator on a target location in the aesthetic manifold, specified not as a single point but as target values along each of the four channels.

A concrete specification:

$$
c = (c_1, c_2, c_3, c_4) = (\text{target divergence}, \text{target coherence}, \text{target trajectory}, \text{target genre-axis})
$$

For music generation, $c_2 < 0$ (low internal coherence) and $c_3 > 0$ (large steps) are conditioning signals that, by Chapter 17's sign-flip result, predict higher listener engagement. For text generation, the signs reverse. The generator is conditioned not on a single quality score but on a geometric location. Two works conditioned on different channel profiles can both be "high-quality" — they just live in different regions of the manifold.

This has the pleasant property that the generator's biases are legible. If a system consistently produces work at a specific manifold location, that location is read off the channel values. A generator that secretly reduces to a single aesthetic attractor — the generative analogue of the filter bubble — is detectable by geometry. The channel-conditioning target $c$ makes the aesthetic intent of the generation *auditable* in a way scalar RLHF preference-tuning does not.

## 18.8 Curation: The AI Curator Problem {#18-8-curation-the-ai-curator}

A curator is an agent who selects works for an audience. A museum curator selects which paintings to acquire; a festival director selects which films to program; an editor selects which stories to publish; a streaming service's home-page algorithm selects which tracks to foreground. All of these are curation. Increasingly, all of them are partly algorithmic.

The framework suggests that an AI curator should satisfy four design conditions, paralleling Ethics Ch 18's four requirements for structurally contained ethical agents:

**Condition 1: Explicit manifold coordinates.** The curator must, for every candidate work, maintain and report its location on the aesthetic manifold — its channel values, its stratum membership, its position relative to the audience's prior.

**Condition 2: Governance-specified interest covector.** The weights that translate channel values into a scalar ranking are specified by the institution the curator serves, not learned from behavioral data. A museum curator's $I_\mu$ differs from a streaming service's $I_\mu$; both are legitimate; both are declared.

**Condition 3: Audit trail.** Every curatorial decision is accompanied by the tensor, the covector, the contraction, and the residue. When a work is rejected, the audit records which channels it scored low on and what it would have taken to change the decision. This is the aesthetic analogue of the moral-residue logging principle.

**Condition 4: Pluralism preservation.** The curator's long-run output distribution must not concentrate below a governance-specified diameter on the manifold. The diameter is a parameter; different institutions choose different values; the constraint is enforceable.

Condition 4 is the one that most directly addresses the engagement-maximization trap. A curator that would produce an output distribution tighter than the diameter must either abstain or expand its recommendations into the under-represented region. The diameter constraint is a geometric analogue of a diversity requirement, but it is principled rather than ad hoc: it is specified in the same manifold coordinates in which the aesthetic evaluation itself is specified, so it is invariant under the same gauge transformations.

## 18.9 What a Principled Aesthetic Agent Looks Like {#18-9-principled-aesthetic-agent}

Collecting the design principles:

- The agent operates on **cloud-valued representations** of works — sets of token-level embeddings in a learned representation space — not on single scalar or vector summaries (Chapter 5).
- The agent's internal evaluation is **tensor-valued** across at least the four channels of Chapter 17 (divergence, coherence, trajectory, genre-axis), with rank-2 extensions for stakeholder-conditional evaluation (Chapter 6).
- The agent's **contraction from tensor to action** is explicit, auditable, and specified by governance — not learned from engagement data and not buried in the model's parameters (Chapter 15).
- The agent satisfies **geometric invariances** — translation, format, tokenization, rank-appropriate order-invariance — calibrated against the cross-lingual benchmarks of Chapter 17 §17.5.
- The agent **resists manifold collapse** by incorporating divergence and diameter terms in its interest covector, preventing the engagement-maximization attractor.
- The agent **logs residue** — the channels it sacrificed, the near-miss alternatives, the genre-confound magnitude in its current decision — for post-hoc review (Chapter 16, §16.9).
- The agent **acknowledges the normative gap**: it produces geometric evaluations, not verdicts, and reports the dependency of its verdicts on the specified interest covector (Chapter 16, §16.7).

This is not a description of any system that currently exists. It is a description of a system that takes the geometric framework seriously as an engineering specification.

## 18.10 Why This Matters Beyond Music and Books {#18-10-why-this-matters}

The framework's direct empirical leverage is in two modalities. Its design prescriptions, we argue, transfer more broadly. Any aesthetic domain in which:

1. works can be tokenized into content units,
2. a pretrained encoder produces stable token-level embeddings, and
3. cloud-level statistics (divergence, coherence, trajectory, genre-axis) are computable,

is a candidate for the framework's engineering architecture. This currently includes: generated images (via CLIP or similar), generated video (via temporal vision encoders), generated code (via code-language-model embeddings), and generated conversation (via sentence encoders). Each carries modality-specific sign structure that has not yet been measured but that the framework predicts will exist and will be testable in the same way.

For modalities where one or more of the three conditions fails — live performance, conceptual art, relational aesthetics (Chapter 16 §16.5) — the framework's engineering prescriptions do not directly apply. Honesty about this matters: a recommender for live-performance events, a curator for conceptual-art programs, cannot be designed by these methods alone. The framework is a tool for a subset of the problem.

## 18.11 The Ethical Continuity {#18-11-ethical-continuity}

We close by noting the continuity with *Geometric Ethics*. An aesthetic agent operating at scale is also a moral agent. A music recommender shapes the listening habits of millions; a text generator influences public discourse; an image generator reshapes the visual culture. The two frameworks operate on parallel manifolds, with parallel tensor hierarchies, parallel contraction problems, and parallel invariance constraints — and they operate on the same agent.

A streaming service that builds a tensor-valued recommender but deploys it within a scalar-reward engagement-optimized business metric has built the aesthetic geometry on top of a moral architecture that will pull it back into the filter-bubble attractor. The two layers must be consistent. The ethics framework's governance stack (Ethics Ch 19's DEME) and the aesthetics framework's channel architecture are not alternatives; they compose. The next chapter develops that composition.

## 18.12 Bridge to Chapter 19 {#18-12-bridge}

Chapter 19 specifies the architecture — Discover, Evaluate, Mediate, Explain — that an aesthetic AI would need to implement the design principles of this chapter. The architecture is somewhat speculative; it describes what a principled aesthetic agent *would* look like rather than what currently exists. We build it in parallel with, and in reference to, the DEME architecture of *Geometric Ethics* Ch 19 and the ErisML framework from the same volume.
