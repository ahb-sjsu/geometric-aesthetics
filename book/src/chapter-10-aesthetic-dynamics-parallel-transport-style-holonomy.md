# Chapter 10: Aesthetic Dynamics — Parallel Transport, Style Holonomy, Influence Flows

**RUNNING EXAMPLE — Hiroshi's Retrospective**

Hiroshi is curating a retrospective for a museum with a peculiar constraint: the galleries are a ring. Visitors will enter one door and exit the same door, traversing five rooms arranged in a loop. He wants the loop to tell a coherent story about the evolution of the American novel — Hawthorne to Melville to James to Faulkner to Morrison and back to Hawthorne. The problem that keeps him awake: when a visitor finishes the Morrison room and re-enters the Hawthorne room, will they be reading the same Hawthorne they read an hour earlier? Hiroshi suspects not. He suspects that *The Scarlet Letter*, read after Morrison's *Beloved*, has rotated. The text has not changed; the reader has been carried around a loop and returns bearing the accumulated torsion of the passage. Hiroshi does not yet have the vocabulary for what he is arranging. He is arranging a holonomy.

## 10.1 Aesthetics in Motion {#aesthetics-in-motion}

The preceding chapters developed a static picture: the aesthetic manifold $\mathcal{A}$ (Chapter 5), the tensors that live on it (Chapter 6), the metric that measures them (Chapters 6, 9), and the stratified boundaries where genre and form shift the rules (Chapter 8). This apparatus captures the geometry of a single work at a single moment — the structure of its features and its position in aesthetic space.

But aesthetic meaning is not static. Works are read into traditions; traditions absorb and deform them. A novel written in 1851 is not the same work when read in 1951. A recording cut in 1959 is heard through the ear of every cover, sample, and homage that followed. An influence relation between two artists is not a label on an edge; it is a rule for how aesthetic content is carried from one point in the manifold to another. Aesthetics is not a photograph but a trajectory — a path through structured space — and the path, we shall argue, matters.

This chapter introduces the dynamics of geometric aesthetics: how aesthetic tensors change as we move through the aesthetic manifold, how style is transported across adaptations and influences, and what it means for aesthetic evaluation to be path-dependent. The mathematical tools are the covariant derivative, parallel transport, holonomy, and curvature — developed abstractly in Chapter 4 and given, here, their aesthetic content.

The empirical hook is narrower than it will be in Chapter 12, but it is real. Our books experiments (Chapter 17) identified a *trajectory channel* — a family of features that measure not the distribution of content but the shape of the path a work traces through its own semantic space. The features `step_mean`, `curvature`, `recur_rate`, `path_eff`, and `acf1_top3` each carried 3–6σ independent signal beyond divergences and coherence. That channel is a measured shadow of what this chapter develops formally: works are trajectories, and the geometry of their trajectories is part of what makes them what they are.

## 10.2 The Problem of Aesthetic Change {#aesthetic-change}

Consider a simple scenario. In 1851 Melville writes *Moby-Dick* and it sinks: poor reviews, poor sales, near-silence for seventy years. In the 1920s the modernists rediscover it, and by 1950 it is canonical. By 2020 it is unread-assigned in universities. What has happened to the aesthetic valence of the book?

A static analysis takes snapshots:

- At $t_0$ (1851): valence $V(t_0)$ pointing toward "labored allegory."
- At $t_1$ (1925): valence $V(t_1)$ pointing toward "proto-modernist monument."
- At $t_2$ (2020): valence $V(t_2)$ pointing toward "colonial document to be read against the grain."

These are three points in aesthetic space with three valence vectors. The static analysis can compare them — they point in different directions — but it cannot answer the dynamic questions. **How did $V(t_0)$ become $V(t_1)$?** Was the aesthetic judgment destroyed and a new one erected, or was the same valence faithfully carried across a changing critical landscape? **Is there continuity?** Is the 2020 reading a descendant of the 1925 reading, or an unrelated verdict on the same text? **Is there residue?** Does each reading leave traces — vocabularies, expectations, reading practices — that the next inherits? **Is the result path-dependent?** Would the 2020 reading be different if the modernists had never intervened?

These are questions about aesthetic dynamics — how aesthetic tensors evolve along paths through $\mathcal{A}$. To answer them, we need the apparatus of connections, parallel transport, and curvature.

## 10.3 The Aesthetic Connection {#aesthetic-connection}

### Comparing Works Across Contexts

On a flat space, comparing vectors at different points is trivial: translate one to the other's location. On a curved space, there is no canonical translation — the comparison depends on the path. A *connection* is the additional structure that specifies how to make such comparisons.

**Definition 10.1 (Aesthetic Connection).** An aesthetic connection is an affine connection $\nabla$ on the aesthetic manifold $\mathcal{A}$ (within each stratum of Chapter 8) that specifies, for any direction of change $X$ and any aesthetic feature-field $F$, the rate of change of $F$ in the direction $X$:

$$\nabla_X F = \text{"how } F \text{ changes as aesthetic context moves in direction } X\text{"}$$

In coordinates, the covariant derivative of a feature vector $F^\mu$ in the direction $\partial_i$ is:

$$(\nabla_i F)^\mu = \frac{\partial F^\mu}{\partial x^i} + \Gamma^\mu_{i\nu} F^\nu$$

The first term is the naive rate of change — how the components of $F$ change if tracked in coordinates. The second term is the correction: the Christoffel symbols $\Gamma^\mu_{i\nu}$ encode how the coordinate system itself is moving, because the aesthetic vocabulary available at one point is not quite the vocabulary available at the next. The connection is the grammar of aesthetic translation.

### What the Aesthetic Connection Encodes

The aesthetic connection has a precise interpretation: it encodes how aesthetic concepts translate across contexts. Consider the feature "restraint." In a Japanese literary tradition, restraint (*shibui*, *yūgen*) means evocative understatement, asymmetry, the unfinished edge. In a neoclassical French tradition, restraint means symmetry, decorum, and the hidden seam. The word translates; the feature-vector rotates.

The connection $\nabla$ specifies exactly how this rotation occurs. Moving across the aesthetic manifold from one region to another, the Christoffel symbols tell us which components of the feature vector grow and which shrink as the coordinate basis rotates. The connection does not say which reading is *correct* — that depends on the metric (Chapter 9). It says: if you carry a feature faithfully from one context to another, here is how its components must change to remain the same feature.

### The Levi-Civita Connection

If the aesthetic manifold is equipped with a metric $g_{\mu\nu}$ (Chapter 6), there is a distinguished connection: the Levi-Civita connection, the unique connection that is metric-compatible ($\nabla g = 0$) and torsion-free. Its Christoffel symbols are determined by the metric:

$$\Gamma^\mu_{\nu\rho} = \tfrac{1}{2} g^{\mu\sigma} \left( \frac{\partial g_{\sigma\nu}}{\partial x^\rho} + \frac{\partial g_{\sigma\rho}}{\partial x^\nu} - \frac{\partial g_{\nu\rho}}{\partial x^\sigma} \right)$$

If we know the metric, we know the connection. The governance account of Chapter 9 — which gives the metric its origin through discovery, construction, and convention — thereby also determines the dynamics. The trade-off structure and the transport rules are not independent aesthetic choices; both are encoded in $g_{\mu\nu}$.

Whether the aesthetic manifold has *torsion* — whether the order in which you traverse contexts matters, beyond what curvature explains — is an open empirical question. The cross-modality sign flips we report in Chapter 17 and revisit in Chapter 12 are consistent with a torsion term operating *across* modality boundaries, but not sufficient to establish one within a modality. For this chapter we work with the torsion-free Levi-Civita connection, flagging where torsion would change the story.

## 10.4 Parallel Transport of Style {#parallel-transport}

### The Concept

Parallel transport is the operation of carrying a vector along a path while keeping it "as constant as possible" given the connection.

**Definition 10.2 (Parallel Transport).** An aesthetic feature-vector $F$ is parallel-transported along a curve $\gamma(t)$ in $\mathcal{A}$ if

$$\nabla_{\dot\gamma} F = 0$$

In coordinates, this becomes the system of ODEs

$$\frac{dF^\mu}{dt} + \Gamma^\mu_{\nu\rho} \dot\gamma^\nu F^\rho = 0$$

Given an initial feature-vector $F(0)$ at $\gamma(0)$, the parallel-transport equations determine a unique $F(t)$ at every point along the curve.

### Aesthetic Interpretation

Parallel transport is the *faithful maintenance of style* across changing contexts. When a translator carries Dostoevsky into English, when a filmmaker adapts a novel, when a jazz musician covers a standard — each is parallel-transporting an aesthetic structure along a path through $\mathcal{A}$.

But "faithful maintenance" does not mean "identical components." If the local aesthetic vocabulary changes — if what counts as "tension," "economy," or "grain" is different in the destination region — then faithful maintenance requires adjusting the components to compensate. The work is the same in a geometric sense (it satisfies $\nabla_{\dot\gamma} F = 0$), but its expression in local coordinates changes.

**Example: Carrying "economy" across modalities.** Let $F(0)$ be the feature profile of Hemingway's prose, with large weight on `pair_sim_mean` (internal coherence) and small `step_mean` (short semantic strides). Transport this profile along a curve from prose to film. The local coordinate system rotates: "internal coherence" in film lives partly in continuity editing, partly in score, partly in production design. "Short strides" in film lives in cut-length and blocking.

A faithful transport — the parallel transport along the curve from Hemingway to, say, early Hawks — redistributes the components of $F$ across the rotated basis. The profile in film coordinates looks different from the profile in prose coordinates, but in the geometric sense, $\nabla_{\dot\gamma} F = 0$: the same aesthetic commitment is being carried.

This is what adaptation, at its best, does. It is also what bad adaptation fails to do: a bad adaptation keeps the *components* constant in the origin basis (dialogue verbatim, plot verbatim) while the *basis itself* has rotated, producing a work whose parallel-transport-derivative $\nabla_{\dot\gamma} F \neq 0$ — a work whose nominal fidelity to the source masks a geometric infidelity.

### What Is Not Parallel Transport

Not every change in aesthetic profile is parallel transport. A cover that reinvents, an adaptation that takes a source as raw material for an independent vision, a translation that improves on its original — these are genuine new aesthetic choices, not transported versions of the old. The covariant derivative distinguishes the cases. If $\nabla_{\dot\gamma} F = 0$, the change in $F$ is entirely due to transport: the work is faithfully maintained. If $\nabla_{\dot\gamma} F \neq 0$, there is a genuine divergence — new commitments, new forms, additions or subtractions — beyond what transport accounts for. The magnitude $\|\nabla_{\dot\gamma} F\|$ measures the rate of *genuine aesthetic change* at each point along the path.

Wide Sargasso Sea is not a parallel transport of Jane Eyre. Rhys's $\nabla_{\dot\gamma} F$ is large and deliberate: the work announces its divergence. Au Hasard Balthazar is not a parallel transport of The Idiot. Bresson's covariant derivative runs in an explicit direction. The distinction between parallel transport and genuine change is not pedantic; it is the formal structure underlying the intuition that some adaptations are *of* their source and others are *after* it.

## 10.5 Style Holonomy: The Path-Dependence of Influence {#holonomy}

### The Phenomenon

The most striking consequence of curvature is *holonomy*: parallel-transporting a vector around a closed loop may not return it to its original value. The vector has been rotated by the loop, even though the loop returns to the same point in $\mathcal{A}$.

**Definition 10.3 (Style Holonomy).** Let $\gamma:[0,1]\to \mathcal{A}$ be a closed loop with $\gamma(0) = \gamma(1) = p$. The holonomy of $\gamma$ is the linear transformation $H_\gamma: T_p \mathcal{A} \to T_p \mathcal{A}$ given by parallel transport of feature-vectors around $\gamma$. If $H_\gamma = \mathrm{id}$ for all loops at $p$, the connection is locally flat. If $H_\gamma \neq \mathrm{id}$ for some $\gamma$, the connection has nontrivial curvature.

### The Dickens–Tolstoy–Joyce–Franzen Circuit

Consider a canonical loop of influence in the nineteenth-to-twenty-first-century novel: Dickens $\to$ Tolstoy $\to$ Joyce $\to$ Franzen $\to$ contemporary readers of Dickens. Each arrow is a historically real parallel-transport of aesthetic content. Dickens's serial realism is carried into Tolstoy's panoramic realism; Tolstoy is carried into Joyce's psychological interiority; Joyce is carried into Franzen's domestic-omniscient; contemporary readers reading Dickens-after-Franzen are, themselves, parallel-transporting back to the origin.

Is the Dickens at the end of the loop the Dickens at the beginning? No. The contemporary reader hears free indirect discourse where Dickens wrote ironic narrator. They hear Victorian plot-engineering as artifice where Dickens's first readers heard it as craft. The holonomy is not destructive — Dickens is still Dickens — but it is nontrivial. A rotation has accumulated.

Formally: the feature-vector $F_{\text{Dickens}}(0)$ at the start of the loop, parallel-transported around the Dickens$\to$Tolstoy$\to$Joyce$\to$Franzen$\to$Dickens circuit, returns as $H_\gamma F_{\text{Dickens}}(0)$. The components that have rotated most are those along axes the intervening tradition sharpened: interiority, irony, the authorial ledger. The Dickens of a reader who has read Joyce has a different `pair_sim_mean` signature at the sentence level — not because the sentences changed, but because the reader's decoding basis rotated.

This is the geometric content of the critical intuition that *reading order changes reading*. A reader who reads Joyce first and then Dickens is not at the same point in aesthetic space as a reader who reads Dickens first and then Joyce. Both sit above the same texts. The holonomy of their paths differs.

### A Musical Example: The Coltrane Loop

A shorter musical loop makes the same point. Start at the Gershwin song "My Favorite Things." Rodgers and Hammerstein wrote it as a waltz. Coltrane recorded it in 1960 as a modal excursion. Every post-Coltrane jazz player inherits the Coltrane reading as the default. A contemporary listener who hears the original Broadway waltz after growing up on Coltrane's recording hears the waltz as strangely *simple*, a reading Rodgers and Hammerstein could not have intended and their first audience could not have had.

The feature-vector of the Broadway waltz has not changed. Its holonomy through the Coltrane loop has. In our measured features, this would register as a shift in `step_mean` and `recur_rate` as heard — not as measured from the score, which is unchanged, but as measured from the listener's internal trajectory through the piece, which carries the rotation Coltrane installed.

### The Holonomy Group

The set of all holonomies at a point $p$ — over all loops through $p$ — forms a group under composition, the *holonomy group* $\mathrm{Hol}_p(\nabla)$. A stratum of $\mathcal{A}$ whose holonomy group is trivial is flat: all loops through it preserve aesthetic content. A stratum with a rich holonomy group is curved: paths through it leave lasting rotations.

Genre-internal aesthetic space, we conjecture, is approximately flat: loops entirely inside "the nineteenth-century realist novel" accumulate small rotations. Cross-genre, cross-tradition, cross-modality loops — the loops that make up most of the history of art — accumulate large rotations. This is why cross-genre influence is interesting and genre-internal influence is merely continuous.

## 10.6 Curvature of the Aesthetic Manifold {#curvature}

The Riemann curvature tensor $R^\rho_{\sigma\mu\nu}$ measures, infinitesimally, the holonomy of an arbitrarily small loop. In aesthetic terms, it measures the local path-dependence of style transport: if you commit to a small aesthetic move in direction $X$ and then in direction $Y$, how does the result differ from committing first in $Y$ and then in $X$?

For most aesthetic decisions within a single work, the answer is: not much. The tangent space locally commutes. But at stratum boundaries (genre thresholds, form transitions, modality changes), the Riemann tensor spikes. Moving from "realist scene" to "stream-of-consciousness scene" and then to "formal letter" is not aesthetically commutative with doing those moves in the reverse order. The resulting work reads differently. Curvature has performed work on the trajectory.

We do not claim to have estimated $R^\rho_{\sigma\mu\nu}$ from data. We do claim that the trajectory channel of Chapter 17 — specifically the `curvature` feature, which measures the second-derivative of a book's semantic path — is a consistent-with-curvature signal at the level of within-work variation. It carried 3–6σ independent predictive weight in the books headline (Chapter 17, Phase 1), disappearing substantially under genre residualization (Phase 2) but not vanishing. That residual is where local curvature lives: the part of within-work path-shape that is not explained by genre membership.

## 10.7 Influence as a Connection {#influence-connection}

Influence, in art history, is usually depicted as a directed graph: arrows between artists and works. This is impoverished. An arrow is a discrete labeled edge, but aesthetic influence is a *continuous prescription for transport*: it tells us how to carry features from source to target, in what directions to rotate the basis, which components to preserve and which to let go.

This is precisely what a connection is: a rule that, at every point, tells transported vectors how to change. We therefore reread the art-historical influence graph as a discretized sample of an underlying connection field on $\mathcal{A}$. The Christoffel symbols at a point $p$ encode the *local school*: how an artist working at $p$ receives and transmits features.

Three consequences follow.

First, **influence is not binary.** An artist does not simply "draw on" a precursor; they parallel-transport a specific bundle of features along a specific path. Different features may be transported along different paths, in the same work, and that is why the standard influence arrow ("Morrison influenced by Faulkner") is inadequate — the relation is a multi-vector transport, not a single arrow.

Second, **influence compounds non-commutatively.** Tolstoy-through-Flaubert is not Flaubert-through-Tolstoy. The ordering of the parallel transports differs by the holonomy of the small loop they enclose. Critics who compare "Morrison influenced by Faulkner and then by García Márquez" versus "Morrison influenced by García Márquez and then by Faulkner" are making a claim that is, in principle, geometrically measurable. The measurable difference is the commutator of the two transport operators.

Third, **influence is conserved by transport, not by identity.** The feature-profile of a source is not preserved in the target; only the *parallel-transported* profile is. This is why direct pattern-matching approaches to influence detection (which compare raw feature vectors) systematically fail. They measure $F_{\text{target}} - F_{\text{source}}$, which conflates two different things: the connection-induced rotation and the genuine aesthetic change $\nabla_{\dot\gamma} F$. Only the latter is the artist's contribution. Only the latter should be what we call "the new work."

## 10.8 Geodesics and the Canon {#geodesics}

A geodesic is a path that satisfies $\nabla_{\dot\gamma} \dot\gamma = 0$: the path parallel-transports its own tangent vector. Intuitively, a geodesic is a path that does not turn unless forced by the geometry of the manifold itself. The canon of a tradition, we suggest, is approximately a geodesic.

This is a strong claim, and we are careful. We do not mean the canon is the *best* set of works (that would require a welfare argument we have not made). We mean that the sequence of works that a tradition treats as canonical tends to trace a path whose curvature is *externally forced* rather than internally elective. The tradition moves in aesthetic space, and the canon is the trace of movement that did not, in retrospect, waste energy on turns that the tradition's own structure did not require.

This reading makes the canon contingent on the metric (Chapter 9) and the connection (this chapter), which are both historically produced. Different traditions have different canons not because they disagree about individual works but because they ride different connections on the same manifold. A geodesic in one tradition's connection is not a geodesic in another's.

The chapter-11 material on canon-formation as optimal search develops this thread further. The canon is not merely a sequence; it is the approximate output of a search whose target is geodesic efficiency under the tradition's own metric. When the tradition is honest — when it allows recalibration — the search continues. When it is captured by extraneous forces, the canon drifts off its geodesic and eventually requires correction, of which critical revisionism is the historical signature.

## 10.9 Empirical Grounding: The Trajectory Channel {#trajectory-channel}

The dynamics developed in this chapter are not purely theoretical. Chapter 17 reports that a family of features measuring the *shape of a work's trajectory through its own semantic space* carried 3–6σ of independent predictive signal on the books dataset (n=4,998 Gutenberg$\leftrightarrow$Goodreads matched), distinct from divergence features and distinct from coherence features. The trajectory channel includes:

- **`step_mean`, `step_std`, `step_skew`** — mean, dispersion, and asymmetry of the semantic step-size between successive paragraphs. These are first-order derivatives of the trajectory.
- **`recur_rate`** — the rate at which the trajectory returns near earlier states. This is a measure of the closedness of local loops, a proxy for within-work holonomy.
- **`acf1_top3`** — autocorrelation structure on the top principal axes. A trajectory's long-memory signature.
- **`curvature`** — a direct second-derivative measure of how sharply the path turns.
- **`path_eff`** — path efficiency: how direct the trajectory is between its endpoints, the within-work analogue of geodesic adherence.
- **`powerlaw_slope`, `tail_mass_100`** — heavy-tail statistics of step-size distributions, flagging works whose trajectories include rare large leaps.

Three observations discipline our theoretical use of these features.

*First*, the features were identified in data before the geometric framework was imposed. They are a found rather than constructed channel.

*Second*, under within-genre residualization (Chapter 17, Phase 2), the channel's effect size shrinks substantially — 85% of the headline $R^2$ was genre confound. What remains is an honest "additional aesthetic signal beyond genre," $R = 0.093$, $z = 6.5\sigma$. The trajectory channel is *not* trivially reducible to genre. It is, at reduced effect size, independently predictive within genre.

*Third*, the modality sign-flips (Chapter 17, Chapter 21) show that the trajectory channel's *direction* of effect is modality-specific. In books, smaller `step_mean` predicts higher ratings ($\rho = -0.096$, 6.4σ). In music, *larger* `step_mean` predicts more listens ($\rho = +0.071$, $p = 4 \times 10^{-29}$). The trajectory channel therefore does not carry a universal aesthetic sign; it carries a modality-conditioned one. The geometry is real; the preferred direction of motion along it depends on the stratum you are in.

## 10.10 Bridge: From Dynamics to Reasoning {#bridge}

We have developed the aesthetic analogue of the parallel-transport apparatus introduced in the Ethics volume (*Geometric Ethics*, Ch. 10). Where the Ethics chapter concerned obligations carried faithfully across changing circumstances, this chapter concerns *style* carried faithfully across adaptations, translations, and influence. Where Ethics asked whether a promise survives an emergency, we ask whether a reading survives the tradition it generated.

The next chapter turns from dynamics to search. A curator choosing a program, an anthologist ordering texts, a recommendation system selecting a next track — each is, we will argue, attempting an optimal path on the aesthetic manifold, minimizing a path-integral that the machinery of this chapter makes precise. Chapter 11 will distinguish that path-integral optimum from the *greedy local optimum* that pure engagement-maximization produces, and will flag the consequences of that distinction — consequences that Chapter 26 (Geometric AI Curation) will develop into a full account of algorithmic filter bubbles as a pathology of local-gradient search.

Hiroshi's retrospective, with which this chapter opened, is a curatorial bet that the loop he arranges has a specific holonomy — one that enriches rather than distorts each room's reading. He is not merely sequencing works. He is installing a connection. The holonomy of the completed loop is his authorial signature as a curator, and whether it is good is a question only the visitors, traversing the loop, will settle.
