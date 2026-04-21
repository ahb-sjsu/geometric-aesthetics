# Chapter 19 — The DEME Architecture for Aesthetics

> *"A system that judges should be able to say what it judged, why it judged so, whom it judged for, and what it refused to judge. Anything less is not judgment; it is a verdict without a jurisprudence."*

**RUNNING EXAMPLE — Hiroshi's Acquisition Committee**

Hiroshi chairs the acquisitions committee of a mid-sized contemporary-art museum. The committee meets quarterly. In attendance: three curators, two trustees, a collections manager, a community-liaison representative. At the last meeting a dealer proposed a mid-career painter whose work had been, in Hiroshi's phrase, "statistically invisible to the standard review" — the painter's output did not correspond to any of the active genre clusters the museum's algorithmic first-pass tool flagged as candidates. The committee split. Two curators argued the work was a genuine outlier in a productive way; one argued it was simply peripheral; the trustees wanted a score. Hiroshi, who had been reading the *Geometric Aesthetics* manuscript, proposed a different frame: *what would it look like for our acquisition process to satisfy the four conditions of a principled aesthetic agent?* Could the museum build — or adopt — an assistant that Discovers the manifold from the museum's existing collection, Evaluates a new work along the geometric channels, Mediates between the curators' different aesthetic covectors by representing them as locations on the manifold, and Explains its recommendation by pointing to which channels carried the decision? This chapter sketches what Hiroshi's question would produce if followed through.

## 19.1 From Theory to Infrastructure {#19-1-from-theory-to-infrastructure}

Chapter 18 argued that artificial aesthetic agents should be built around tensor-valued evaluation, learned-representation geometry, explicit governance-specified contraction, and invariance guarantees. The mathematics was developed. The design principles were stated. The question this chapter addresses is: *what architecture realizes those principles?*

The chapter parallels *Geometric Ethics* Ch 19, which presented the DEME (Democratically Governed Ethics Module Engine) architecture and the ErisML modeling language for geometric ethics. We are not the authors of ErisML; it exists, has a reference implementation, and is described in the sibling volume. Our task is to specify the aesthetic analogue.

We name it, by analogy, **aesthetic DEME**. The acronym stands for:

- **D**iscover — learn the manifold structure from a corpus
- **E**valuate — place a new work on the manifold along the four channels
- **M**ediate — model diverse audiences as distributions over interest covectors
- **E**xplain — attribute decisions to specific channel contributions

The four-letter expansion differs from the ethics DEME but intentionally echoes it: both architectures have four layers, both separate representation from judgment, both require governance input at the contraction step, and both produce auditable outputs. Where the ethics DEME runs on a norm-constrained stochastic game, the aesthetic DEME runs on a channel-decomposed content manifold. The engineering problems are parallel; the solutions are parallel.

We state up front: *this chapter is somewhat speculative.* Unlike the empirical chapter (Chapter 17), we are not reporting a built-and-measured system here. We are describing what a principled aesthetic AI — one that takes the framework's commitments seriously — would look like. The individual components (encoders, Lasso channels, invariance audits, tensor contractions) have been implemented and tested in our experimental code; the full stack has not. We mark conjecture as conjecture.

## 19.2 The Four Layers {#19-2-the-four-layers}

The aesthetic DEME is organized as four layers:

1. **Application layer.** The user-facing system — the recommender, the curator, the generative model, the critic's assistant.
2. **Evaluation layer.** The tensor-valued evaluation of candidate works along the four geometric channels. This layer is domain-general; it is the aesthetic DEME proper.
3. **Translation layer.** The mapping from user-facing preferences (ratings, click data, curatorial commitments, editorial voice) to interest covectors in the manifold's cotangent space.
4. **Governance layer.** The process by which the interest covectors and diversity constraints are set, reviewed, and revised. This is the layer at which institutional, community, or individual values enter the system.

The layers correspond, not exactly but closely, to the four layers of the ethics DEME: Application, Ethics Module, Canonicalizer + Translation, and Governance. The key architectural identity: **representation lives below governance; governance lives above contraction.** An aesthetic evaluation is a fact about the work; an aesthetic verdict is a fact about the work *and* the covector a community has specified. The architecture enforces the distinction at the layer boundary.

We now describe each of the four stages of the aesthetic DEME (Discover, Evaluate, Mediate, Explain) and place them within the four-layer stack.

## 19.3 Discover: Learning the Manifold {#19-3-discover}

The Discover stage operates on a corpus. It has two tasks.

**Task D1: Fit the encoder output as a manifold.** Given a corpus $\mathcal{C} = \{W_1, W_2, \ldots, W_M\}$ and a pretrained encoder $\phi$, compute the cloud $X(W_i)$ for each work. Fit a shared PCA basis on the pooled corpus to produce a low-dimensional (e.g., 128-d) representation space. Chapter 17 used this exact step: a PCA-128 basis fit on the English Gutenberg corpus was then used to project non-English works, producing the cross-lingual invariance results at $\rho \approx 0.7$.

**Task D2: Extract channel features.** For each work, compute the four-channel feature vector:

- divergence features against a corpus prior (KL, JS, Hellinger, Bhattacharyya, Mahalanobis-mean, TV),
- coherence features (`pair_sim_mean`, `pair_sim_std`),
- trajectory features (`step_mean`, `step_std`, `step_skew`, `recur_rate`, `acf1_top3`, `curvature`, `path_eff`, `powerlaw_slope`, `tail_mass_100`),
- genre-axis features (Lasso-on-PCA-spectrum; Chapter 17 recovered 71 interpretable axes for books).

**Task D3: Identify strata.** Cluster the manifold into genre strata using the Lasso-recovered genre axes. Chapter 8's stratification theory applies: genre boundaries are first-order discontinuities in the manifold, and a principled curator should know which stratum a candidate work lives in before asking how the work ranks within that stratum.

**Task D4: Calibrate invariances.** For a subset of works for which equivalent re-descriptions exist (translations, format variants, tokenization variants), measure the within-description variance of channel features. This yields the system's invariance envelope, the aesthetic analogue of the BIP audit (Ethics Ch 18). A deployed system whose evaluations drift outside this envelope under gauge transformations is misaligned.

The output of Discover is a fit encoder + PCA basis + channel feature-extractors + stratum assignments + invariance envelope. This package is the "manifold" the rest of the architecture operates on.

**Governance note.** The corpus choice is a governance decision. A museum whose acquisitions committee calibrates the Discover stage on its existing collection has chosen to measure candidate works against *its own prior*. A streaming service that calibrates on its entire catalogue has chosen the global prior. A scholarly edition that calibrates on a single author's oeuvre has chosen the author-internal prior. All three are legitimate; the choice changes what divergence means. The choice must be declared.

## 19.4 Evaluate: Placing a Work {#19-4-evaluate}

The Evaluate stage operates on a candidate work $W^*$ not in the Discover corpus (or, for internal benchmark use, on a held-out portion of it).

**Task E1: Encode.** Produce the cloud $X(W^*)$ using the frozen encoder from Discover.

**Task E2: Project.** Map the cloud into the PCA-128 basis. The invariance result of Chapter 17 §17.5 licenses this projection: the same basis works across languages at $\rho \approx 0.7$, and should transfer within modality to unseen works from the same distribution.

**Task E3: Channel.** Compute the tensor value $T^\mu(W^*)$ across the four channels. Return the full tensor, not a scalar.

**Task E4: Stratum assignment.** Identify which genre stratum $W^*$ sits in, using the Discover-stage stratum boundaries. The within-stratum evaluation of Chapter 17 §17.2 — the honest aesthetic signal after genre controls — should drive the evaluation's intended interpretation. A work near a stratum boundary should be flagged; the framework's behavior at boundaries is less well characterized.

**Task E5: Invariance check.** Where possible (format variants, paraphrases), re-run E1–E3 under gauge transformations and verify the result is within the invariance envelope. Flag when it is not.

**Task E6: Uncertainty.** Quantify the observation-count noise: for the given work's size $N$ (tokens), the channel-level standard errors. Chapter 16 §16.3 warned that single-observer evaluations are noisy; the system should report its own noise.

The output of Evaluate is a structured object:
$$
\text{eval}(W^*) = \bigl\langle T^\mu(W^*),\ \text{stratum}(W^*),\ \text{se}(T^\mu),\ \text{gauge-status} \bigr\rangle.
$$
No scalar verdict is produced at this stage. No recommendation is made. Evaluate is strictly descriptive.

## 19.5 Mediate: Modeling Audiences {#19-5-mediate}

The Mediate stage is where the framework's approach to aesthetic pluralism gets architectural form. The key move: **each audience member, or each institutional commitment, is represented as an interest covector $I_\mu$ in the manifold's cotangent space.** Aesthetic disagreement is modeled not as a disagreement about the work but as a difference in the covector applied to the (shared, invariant) tensor.

**Task M1: Elicit covectors.** For each user or each institutional commitment, infer $I_\mu$ from whatever signal is available. For a user with rating history, this is a regression problem — fit the covector that best predicts their ratings from works' channel values. For an institution declaring a curatorial philosophy, it is a direct specification — "we weight divergence positively, coherence weakly, trajectory variance positively within the within-stratum evaluation". For a community, it is an aggregation: see M3.

**Task M2: Place covectors on the manifold.** Each covector, once elicited, is a location on a secondary structure — a *covector manifold* dual to the content manifold. Audiences cluster in this dual space. Two readers who love nineteenth-century realism have nearby covectors even if their favorite individual authors differ. A recommender that thinks of audiences as covector clusters rather than as behavior traces has a more parsimonious, more generalizable audience model.

**Task M3: Aggregate for collective decisions.** When a curatorial decision must be made on behalf of a plural audience, the covectors must be aggregated. Chapter 15 (on contraction) and Chapter 14 (on collective aesthetic agency) offer options: a summative aggregation averages covectors weighted by credence; a Rawlsian aggregation takes the minimum-weighted covector to ensure the least-advantaged aesthetic taste is not ignored; a lexicographic aggregation commits to one covector's priorities before others. Each aggregation is a contraction in the theory-space sense of the ethics framework (Ethics Ch 16). The system must name which aggregation it is performing.

**Task M4: Flag irreducible disagreement.** When the covectors of relevant stakeholders point in opposite directions on a particular channel, the Mediate stage flags an irreducible disagreement. The system does not resolve it. It reports: "The committee is split on channel $T^2$ (coherence): two members weight it positively, three negatively. The candidate work scores high on $T^2$. The decision depends on which committee subset's covector is privileged." This is the aesthetic analogue of the ethics-framework's moral-uncertainty reporting (Ethics Ch 16).

**Connection to canon formation.** Chapter 14's account of collective aesthetic agency described canon formation as a geometric-distance aggregation in the content manifold. The Mediate stage is where that aggregation becomes operational. The covector cluster of the "mainstream critical establishment" is one aggregation; the covector cluster of "a specific artistic community" is another. Canons are the contractions of these clusters with the content manifold. An aesthetic DEME that models canons as covector clusters can represent multiple simultaneous canons without requiring them to reduce to one.

## 19.6 Explain: Channel Attribution {#19-6-explain}

The Explain stage is what makes the aesthetic DEME accountable.

**Task X1: Decompose the contraction.** When a scalar verdict $S = I_\mu T^\mu$ is produced, decompose it:
$$
S = I_1 T^1 + I_2 T^2 + I_3 T^3 + I_4 T^4 \quad \text{(channel-level attribution)}
$$
and, within each channel, further decompose into the specific features (the seven trajectory features, the two coherence features, the six divergence features, the 71 genre-axes). Report the contribution of each feature to the scalar.

**Task X2: Report the residue.** Chapter 15 defined the moral residue as the information lost in contraction. The aesthetic residue is the channels and features *not* contributing to the verdict — either because their covector weight was small or because their value was near-median. The residue records the alternatives that were close in manifold distance but differed along ignored channels. When the verdict is questioned, the residue reveals what the contraction sacrificed.

**Task X3: Report the uncertainty.** Chapter 16's four limits produce explicit uncertainty flags: observation-count noise (E6), pathological-work warning (stratum boundary, extreme channel values), modality-reach warning (if the work type is near the encoder's domain boundary), normative-gap reminder (the verdict is covector-relative).

**Task X4: Report the counterfactual.** For a negative decision, report the minimum covector perturbation that would flip the decision. "This work would be accepted if the coherence weight were reduced by 0.3" is actionable feedback both to the submitter and to the governance layer.

The Explain stage is not post-hoc rationalization. It is a formal part of the output structure. A system that produces verdicts without Explain is not a DEME-compliant system.

## 19.7 The Layered Flow {#19-7-layered-flow}

A full pipeline, end-to-end, for a single query (e.g., "should we acquire this painting?"):

1. **Application** receives the candidate work $W^*$.
2. **Evaluation** runs Discover's pre-fit pipeline on $W^*$: encode, project, channel, stratum-assign, invariance-check, uncertainty-quantify. Returns the tensor and metadata. No verdict.
3. **Translation** retrieves the relevant interest covector $I_\mu$ — either the current user's covector, the committee's aggregated covector, or the institution's declared covector.
4. **Application** requests a scalar verdict. The system performs the contraction $S = I_\mu T^\mu$, passes the result to Explain.
5. **Explain** produces the channel-attribution, residue, uncertainty flags, and counterfactual.
6. **Governance** periodically audits: are the covectors still the ones we declared? Has the output distribution collapsed below the diversity diameter? Are invariance violations growing? Trigger covector revision as needed.

The flow is specified at a level of abstraction that admits many implementations. It does not dictate the encoder, the PCA dimension, the exact covector-elicitation protocol, or the aggregation rule. These are parameters of the deployment, set by the governance layer. What is fixed by the architecture is the separation of layers, the tensor-valued intermediate representation, the explicit contraction, and the Explain accountability.

## 19.8 Connection to ErisML {#19-8-connection-to-erisml}

The ErisML modeling language developed for *Geometric Ethics* Ch 19 is directly applicable to aesthetic DEME. Where the ethics-framework ErisML specifies *environment* (state space), *agency* (capabilities, beliefs), *intent* (multi-objective utilities), *norms* (permissions, obligations, prohibitions), and *dynamics* (multi-agent interactions), the aesthetic-framework ErisML would specify:

- **Content corpus** — the manifold-fitting corpus and its governance;
- **Encoder** — the pretrained embedding model, fixed, with declared provenance;
- **Channel extractors** — the four-channel feature pipeline, version-pinned;
- **Audience model** — covector elicitation, aggregation rules, cluster definitions;
- **Curatorial norms** — the governance-specified weights, diversity constraints, invariance envelope;
- **Audit spec** — the Explain stage's output format.

A well-specified aesthetic DEME is an ErisML specification in this sense. Like the ethics-framework compilations (to PDDL, PRISM, safe RL, multi-agent RL), the aesthetic-framework specification compiles to runnable evaluators — batch-mode (offline curation), streaming-mode (real-time recommendation), interactive (decision-support tool for human curators).

The point of the shared language is not notational elegance. It is that **the ethics and aesthetics of an AI system compose**. A streaming recommender is an ethical agent (affecting millions of listening habits) and an aesthetic agent (making content-level judgments). Its full specification is an ErisML object with both ethics-layer constraints (privacy, non-discrimination, fairness) and aesthetics-layer constraints (channel balance, diversity diameter, invariance envelope). The governance layer operates on both simultaneously.

## 19.9 What Is and Is Not Built {#19-9-what-is-and-is-not-built}

Honesty about the current state:

**What exists.** The Discover stage is fully implemented for books and music in our experimental code. The channel extractors are tested and validated at the significance levels reported in Chapter 17. The PCA-128 basis, the Lasso-recovered genre axes, the cross-lingual invariance measurements are all real. The Evaluate stage, for a new work drawn from the same distribution as the training corpus, works end-to-end in the book and music experiments.

**What is partial.** The Mediate stage — covector elicitation from user behavior — is implementable with standard preference-learning methods but has not been integrated into the framework's experimental code. The aggregation rules are implementable; specific production protocols have not been designed.

**What is speculative.** The full four-layer architecture, operating as a deployed governance system for a real curatorial institution, does not exist. The ErisML aesthetic specification language does not yet exist as a distinct artefact; it would be a natural extension of the ethics ErisML but has not been formalized. The diversity-diameter enforcement mechanism is described at the specification level but no production implementation has been tested.

The reader should treat this chapter, then, as a design document. It describes what a principled aesthetic AI would look like, given the empirical and philosophical results of the preceding eighteen chapters. It does not describe a running system. Where Chapter 17 earned the right to make empirical claims, this chapter earns the right only to make design claims — claims that the architecture *could* be built, that its components *have* been tested in isolation, and that it *would* satisfy the principles of Chapter 18 if built and deployed as described.

## 19.10 Why This Architecture and Not Another {#19-10-why-this-architecture}

One might ask: why four stages, why the Discover–Evaluate–Mediate–Explain structure, and not some other decomposition?

The answer traces back to the four failure modes of Chapter 18 §18.2. **Manifold collapse** is prevented by Discover's stratification and Mediate's diversity-diameter enforcement — both require the separation of manifold learning from in-context evaluation. **Cross-modality sign inversion** is handled by Evaluate's channel-decomposed output — the tensor carries sign information that a scalar would lose. **Genre confound** is handled by Evaluate's stratum-assignment and Explain's residue reporting — the within-stratum evaluation is exposed separately from the across-stratum evaluation. **Reward hacking via style proxies** is prevented by Explain's counterfactual reporting and by the separation of contraction from representation — a system whose aesthetic target is the tensor, not the scalar, is less exploitable than a system whose target is a single score.

Each architectural feature is load-bearing against a specific failure mode. The architecture is not arbitrary. It is the minimum structure required to preserve the framework's principles under deployment pressure.

The parallel with the ethics DEME is not decorative. It reflects that aesthetic agents and moral agents share the same fundamental problem: *a tensor-valued evaluation must, at some point, be compressed to an action, and the compression is lossy, and the losses can be minimized but not eliminated, and the only honest response is an architecture that makes the compression explicit.* Ethics DEME solved this for moral action. Aesthetics DEME solves it for aesthetic judgment. The same philosophical move; the same engineering response.

## 19.11 Closing the Part IV Arc {#19-11-closing-part-iv}

Part IV of this book (Chapters 16–19) has addressed the meta-level: what the framework cannot do (Chapter 16), what it does empirically (Chapter 17), what it implies for artificial agents (Chapter 18), and what architecture realizes those implications (this chapter). Part V turns to applications — literary criticism, musicology, film, visual art, architecture, games, AI curation, fashion, and everyday aesthetics — each a domain in which the framework's descriptive apparatus and engineering architecture can be specialized.

The reader arrives at Part V with, we hope, a clear sense of the framework's reach and its boundaries. The geometric account of aesthetics is real, measurable, bounded, and — if taken seriously as an engineering specification — useful. The aesthetic DEME is what taking it seriously looks like. Whether any institution chooses to build one, and under what governance, is the question the book cannot answer. It can only supply the architecture.

## 19.12 Bridge to Part V {#19-12-bridge}

Chapter 20 opens with literary criticism — the domain where the book's empirical work has been most thoroughly developed and where the aesthetic DEME's Discover and Evaluate stages are closest to production-ready. The reader should carry forward the four-layer architecture; each of the Part V chapters will identify where in the stack its domain-specific concerns enter.
