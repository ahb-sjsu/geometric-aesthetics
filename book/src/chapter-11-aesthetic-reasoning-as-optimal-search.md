# Chapter 11: Aesthetic Reasoning as Optimal Search

**RUNNING EXAMPLE — Elena's Anthology**

Elena has been commissioned to edit *An Anthology of the Twenty-First-Century American Short Story* — sixty stories, in order, between two covers. Her inbox contains two emails. The first is from her publisher's data-science team: here are the top two hundred stories by engagement metrics across their reading platform; the ordering is the algorithm's recommendation. The second is from a literary critic she respects: here are sixty stories I would include; the ordering is mine. The two lists overlap on eleven titles. Elena understands immediately that she is not being offered two answers to the same question. She is being offered two different questions — and two different search procedures masquerading as answers. The algorithm is greedily climbing the gradient of engagement. The critic is tracing something else: a path through a space whose geometry the engagement score does not see. Elena's job is to decide which search she is running, and to be honest, in her introduction, about which one she picked.

## 11.1 The Computational Problem {#computational-problem}

The preceding chapter established the geometry of aesthetic dynamics: the covariant derivative, parallel transport, holonomy, geodesics, and curvature. These are the structural features of the aesthetic landscape. But a landscape, however well mapped, does not by itself explain how a curator, anthologist, critic, or recommendation engine *chooses*. Geodesics are the paths of least resistance — the optimal trajectories. But how does an agent *find* a geodesic? How does a chooser, confronted with an aesthetically complex situation, determine which sequence of works minimizes whatever path-integral governs the task at hand?

This chapter answers the question by establishing a formal equivalence between aesthetic reasoning and optimal search. The claim is precise: *aesthetic reasoning — curation, canon-formation, and critical judgment — is A\* pathfinding on the aesthetic manifold, with accumulated aesthetic cost as the backward term and trained aesthetic intuitions as the heuristic*. The equation $f(n) = g(n) + h(n)$, familiar from the AI literature since Hart, Nilsson, and Raphael (1968), is the fundamental equation of aesthetic reasoning.

The shift from geometry to computation is not merely vocabulary. It explains why aesthetic judgment *feels like search* — why curators deliberate, backtrack, reject, regret; why anthologists assemble and reassemble; why critics revise. The answer, parallel to the moral argument in *Geometric Ethics* (Ch. 11), is that the exact optimization is intractable, and so all real aesthetic reasoning is pre-compiled approximation. The *canon*, the *genre*, the *style* — each is an evolved heuristic.

## 11.2 A* Search on the Aesthetic Manifold {#a-star}

A curator occupies an aesthetic state $s_0 \in \mathcal{A}$: a standing program, a half-filled table of contents, an empty gallery. They must choose a sequence of works that moves the program toward some goal region $\mathcal{G}$ — a region of aesthetic "rightness" for the task. The objective is to find the path $\gamma$ from $s_0$ to $\mathcal{G}$ that minimizes a cost functional $C[\gamma]$.

**Definition 11.1 (Aesthetic Search Problem).** Given the aesthetic manifold $\mathcal{A}$, a current state $s_0 \in \mathcal{A}$, and a goal region $\mathcal{G} \subset \mathcal{A}$, the aesthetic search problem is to find

$$\gamma^* = \arg\min_{\gamma \,:\, s_0 \to \mathcal{G}} \; C[\gamma] \quad \text{subject to stratum constraints (Chapter 8).}$$

The cost functional $C[\gamma]$ is task-dependent:

- *Curation of a concert program*: $C$ penalizes incoherence between adjacent pieces and rewards structural arc across the evening.
- *Anthology*: $C$ penalizes tonal whiplash between adjacent stories and rewards cumulative range.
- *Recommendation of a next track*: $C$ is near-zero within a tight local neighborhood and grows outside it.
- *Critical judgment on a single work*: $C$ is the integrated distance from the aesthetic verdict to the geometry of the work as actually structured.

**Definition 11.2 (A\* Aesthetic Search).** The A* evaluation of a candidate state $n$ is $f(n) = g(n) + h(n)$, where

- $g(n) = C[\gamma_{s_0 \to n}]$ is the exact accumulated aesthetic cost of the chosen partial path — already-made choices, their commitments, their residues;
- $h(n)$ is the heuristic estimate of the cheapest remaining path from $n$ to $\mathcal{G}$ — the curator's trained intuition for "how far we still have to go";
- $f(n)$ is the total estimated cost of the cheapest path through $n$.

A* expands the node with the lowest $f(n)$ at each step. It is optimal when $h(n)$ is admissible (never overestimates) and consistent (satisfies the triangle inequality).

Why A* rather than alternatives? The choice reflects the structure of aesthetic reasoning.

- **Dijkstra's algorithm** is A* with $h = 0$ — no heuristic. In aesthetic terms, this is pure empirical cost-minimization without trained taste: evaluate every candidate by its on-record cost alone. It is optimal but computationally explosive.
- **Greedy best-first search** uses only $h(n)$, ignoring accumulated cost $g(n)$. This is pure trained-reflex curation: pick whichever candidate your gut says is closest to the goal, without regard to what you have already committed to. It is fast but suboptimal — it gets misled by locally attractive paths that require backtracking.
- **Gradient ascent on engagement** is greedy search with $h$ set equal to a local reward signal. It is myopic and local. Chapter 10 identified local-gradient pathologies; this chapter identifies their curatorial signature: filter-bubbles, micro-genres that collapse, and the phenomenon in which a recommendation system converges on an aesthetic monoculture for each user.
- **A\*** combines exact accumulated cost with heuristic forward estimation. It is both optimal (when $h$ is admissible) and efficient (the heuristic prunes the search).

In aesthetic terms, A* balances the consequentialist accounting of already-chosen works (no rescinding, no do-overs, the program-so-far is what it is) with the deontological guidance of trained taste (this next work *feels* right, toward-the-goal, given what the curator knows of the form). This is the computational content of the observation that good aesthetic reasoning requires both *what you have already committed to* and *where you are trying to go*.

## 11.3 Trained Taste as a Heuristic Function {#trained-taste}

The central claim of this chapter is that *aesthetic intuitions* — the trained reflexes of a curator, the "feel" a critic has for how a book is going, the taste of a seasoned anthologist — are the gradients of heuristic functions in the A* framework.

**Proposition 11.1 (Taste–Heuristic Correspondence).** The aesthetic tangent vector $T^\mu$ at a point $p \in \mathcal{A}$ — the directional signal that "this is where the program wants to go next" — is the negative metric-raised gradient of the heuristic $h$:

$$T^\mu = -g^{\mu\nu} \partial_\nu h.$$

The taste-vector points in the direction of steepest descent of $h$: toward the estimated cheapest path to the goal. This is not a stipulation but a consistency condition between the geometric and computational interpretations of the same underlying structure.

Trained aesthetic intuitions — "don't put these two stories back-to-back," "this album needs a palate cleanser in position five," "the program peaks in the second-to-last movement" — are highly optimized heuristic functions. They let a curator with finite deliberation time instantly approximate the optimal path through a space whose exact optimization is intractable. When a curator experiences the phenomenological force of aesthetic judgment — the sense that a work *belongs here* or *doesn't* — they are reading the output of a heuristic compiled from training, reading history, and critical conversation.

### The Genre Heuristic

Consider the heuristic "don't mix these two genres in a single programming block." This is a high-efficiency heuristic that prunes vast regions of the search space. It is also, unavoidably, an over-approximation: some cross-genre mixes are beautiful. The heuristic is $\varepsilon$-admissible rather than strictly admissible. In Chapter 17 we report that 85% of the headline $R^2$ of the books model was genre confound — in our notation, $h_{\text{genre}}(n)$ was doing most of the work of predicting rating. Within-genre, the independent aesthetic signal drops to $R = 0.093$, $z = 6.5\sigma$. This is not evidence that the genre heuristic is wrong; it is evidence that the genre heuristic is *efficient* — it captures most of the structure, allowing the remaining signal to fit within a much smaller search space.

### The Canon Heuristic

Canon-inclusion is an even denser heuristic. To say "X is canonical" is to say, in effect, "the geodesic of the tradition passes near X." This is a pre-compiled result of past searches by past critics, and it radically prunes the search space a new curator faces. A curator who uses the canon as a heuristic is not lazy; they are using a pattern-database the tradition has accumulated.

But canon-heuristics become inadmissible when the tradition's metric drifts (Chapter 9) without the canon updating. Historical revaluations — Melville in the 1920s, Hurston in the 1970s, women modernists in the 1990s — are moments in which the community detects the inadmissibility of the prior canon-heuristic and recalibrates. The heuristic was overestimating the cost of paths through regions of $\mathcal{A}$ that, under a corrected metric, contained cheap and strong geodesics. Recalibration is not anti-canonical; it is *canon-search continuing*.

### Algorithmic Taste as Compiled Heuristic

A recommendation system trained on engagement data has compiled a very particular heuristic: $h_{\text{engagement}}(n)$ estimates the forward cost to a *local* goal — the user's next-ten-minute engagement peak — rather than any global aesthetic path. We will return to this in §11.7. For now, note only that it is a legitimate heuristic for the task it is trained on; the aesthetic objection to it is not that it is a heuristic (all reasoning uses heuristics) but that the task it solves is not the task curators have historically solved.

## 11.4 Admissibility, Consistency, and Aesthetic Calibration {#admissibility}

**Definition 11.3 (Admissibility).** A heuristic $h$ is admissible if, for every state $n \in \mathcal{A}$, $h(n) \leq g^*(n, \mathcal{G})$, where $g^*(n, \mathcal{G})$ is the true minimum cost from $n$ to the goal.

**Definition 11.4 ($\varepsilon$-Admissibility).** $h$ is $\varepsilon$-admissible if $h(n) \leq (1 + \varepsilon) \cdot g^*(n, \mathcal{G})$ for all $n$. An $\varepsilon$-admissible A* search returns a path of cost at most $(1 + \varepsilon)$ times the optimum (Pohl 1970; Pearl 1984).

Real aesthetic heuristics are $\varepsilon$-admissible, not strictly admissible. A curator's intuition is wrong often enough that they backtrack, revise, reshuffle. But it is wrong in a bounded way. Good training — ear-training for musicians, reading-history for editors, immersion for curators — calibrates $\varepsilon$ downward. The skill is not perfect admissibility (a fragile state) but small, stable $\varepsilon$.

The categories of Chapter 11 in the Ethics volume carry over almost verbatim.

- *Strictly admissible* heuristics for aesthetics are the core negative prohibitions that no serious tradition violates: don't open a concert with the finale, don't end an anthology with the weakest story, don't put the climactic reveal in the first paragraph. These are near-universal because their true costs genuinely are as large as the heuristic estimates.
- *$\varepsilon$-admissible* heuristics are the normal operating range of trained taste. Slight overcaution, slight bias toward canonical orderings, slight preference for the known over the new — the signature of a calibrated chooser.
- *Inadmissible* heuristics are aesthetic injury: a critic whose formative bad experience with a genre makes them systematically overestimate cost in that region and refuse beneficial paths through it. Aesthetic injury is structurally the same as moral injury; its repair requires directed re-exposure, not generic openness.
- *Gauge-variant* heuristics are the truly pathological category: heuristics whose output depends on irrelevant features of the description. Status-quo bias toward the familiar, anchoring on first-heard versions, order effects in judging blind samples — these are heuristics that violate the aesthetic analogue of the Bond Invariance Principle (Chapter 12). They estimate the wrong quantity.

The distinction matters. Categories (i)–(iii) are calibration issues: the heuristic estimates the right quantity, more or less accurately. Category (iv) is a *symmetry failure* — the heuristic estimates something other than the aesthetic content of the work — and Chapter 12's Noether argument will develop its consequences.

## 11.5 Intractability and the Necessity of Heuristics {#intractability}

**Theorem 11.1 (Intractability of Exact Aesthetic Planning).** Finding the exact optimal path on $\mathcal{A}$ is computationally intractable in the dimensionality of the manifold.

*Proof sketch.* Following the argument of Ethics Ch. 11 §11.5: on a $d$-dimensional stratified Riemannian manifold, achieving accuracy $\varepsilon$ requires $N \propto (1/\varepsilon)^d$ discretization vertices per stratum. Shortest-path algorithms are polynomial in $N$ but the dependence on $d$ is exponential. For the aesthetic manifold, our empirical estimate of the effective dimension from the 128-d PCA basis (Chapter 17) is on the order of $d \sim 30$–$60$ significant axes. With practical $\varepsilon = 0.01$, $N \sim 10^{60}$ vertices per stratum is an unachievable budget. $\square$

The intractability is the reason heuristics exist. A curator without trained taste — without a compiled heuristic — is not a principled empiricist; they are an agent facing an intractable optimization with no pruning. They will fail in real time. Canon, genre, style, and taste are the compiled pattern-databases that make real-time aesthetic judgment possible.

## 11.6 The Verdict Scalar as Search Output {#verdict}

Aesthetic discourse reduces rich judgments to scalars: four-star reviews, green-lights, playlist inclusion. We have argued throughout the book that these scalars discard directional information. But they are not *useless*: they are the *output* of an A* search that has already happened.

**Proposition 11.2 (Verdict as A\* Output).** The scalar aesthetic verdict $V(w)$ assigned to a work $w$ by an agent is the value $f(n^*)$ at the terminal node of the agent's A* search evaluating $w$ against their goal region $\mathcal{G}$:

$$V(w) = g(n^*) + h(n^*).$$

The scalar is a compression: it retains the value at the end of the search but discards the path. Every complaint critics make about star ratings — that two four-star works can be incomparable, that the scalar hides disagreement about what the goal is — reduces to the observation that the scalar outputs of two searches with different $\mathcal{G}$ or different $h$ are not commensurable even when their numerical values match.

The geometric aesthetic framework is, on this reading, a proposal to *not compress* the search output: report the $f$-value, yes, but also report the $\mathcal{G}$ and the $h$ that produced it. This is the formal content of the book's repeated insistence that aesthetic judgment is a location in a space, not a point on a line.

## 11.7 Greedy Local Optimization and the Filter Bubble {#filter-bubble}

We distinguish two searches that are frequently conflated: A* (the non-local path search developed above) and *greedy local optimization on engagement*. They are not the same procedure, and the distinction is load-bearing.

**Engagement maximization** is a greedy search whose heuristic is "the user's probability of engaging with the next item, given the current state." Formally: $h_{\text{eng}}(n) = -P(\text{engagement} \mid n)$. This is a legitimate heuristic for a legitimate task — predicting the next-click — but it has three structural properties that make it a poor proxy for the aesthetic geodesic.

First, **it is local.** The heuristic evaluates only the immediate next state, not the whole path to any aesthetic goal. It has no $\mathcal{G}$. The only goal is the next engagement event. In geometric terms, it is gradient ascent, not geodesic search.

Second, **it has no $g$.** Greedy search ignores accumulated path cost. A recommendation sequence that climbs the local engagement gradient for a thousand steps may have traveled a path of enormous aesthetic cost — bizarrely repetitive, narrow, and self-reinforcing — but the greedy search does not see the accumulated cost because it does not evaluate it.

Third, **it inherits the local metric from the user's current neighborhood.** The manifold's global structure is invisible; only the immediate tangent space is sampled. This is the formal statement of what is colloquially called the *filter bubble*: the sequence of recommendations traces a path that stays, by construction, in a shrinking neighborhood whose metric the user's own past clicks have distorted into approximate flatness.

The consequence is precise. Greedy local optimization on engagement produces a trajectory whose asymptotic behavior is trapping in a local minimum of $h_{\text{eng}}$. Aesthetic content along the trajectory becomes increasingly homogeneous. The user experiences this as narrowing. The recommender system experiences this as high engagement. Both are correct about their local measurements, and neither is detecting the global fact that the trajectory has lost aesthetic range.

A* search — the non-local path-integral optimum — would not exhibit this pathology, because the heuristic $h$ in the aesthetic case estimates distance to a *global* goal region defined on the manifold's global structure (range, variety, or whatever the task's $\mathcal{G}$ demands), not distance to the next click. The filter bubble is not a failure of recommendation in general; it is a specific failure of *greedy local* optimization on a task whose true cost functional is non-local.

Chapter 26 will develop this into a full account of algorithmic curation, including the question of what an aesthetically responsible recommender would compute instead. For now we register only the structural point: the filter bubble is the predicted asymptote of the wrong search algorithm, and the aesthetic geodesic is the object that algorithm fails to find.

## 11.8 The Curator, the Anthologist, the Critic {#three-searches}

Three common aesthetic reasoning tasks instantiate the A* framework differently.

**The curator** (Hiroshi, in Chapter 10; any concert programmer, museum hanger, festival director) solves a path-planning problem with strong stratum constraints. The space of admissible paths is heavily pruned by practical constraints (room size, running time, balance of media). The heuristic is trained from watching audiences traverse prior programs. The cost functional rewards arc: buildup, peak, release.

**The anthologist** solves a path-planning problem with *ordering* as a primary variable and *composition* as a secondary one. Elena's problem in the opening of this chapter is of this type. The search is over permutations of a candidate set, with a pruned candidate set as a further search layer. The heuristic is trained from critical reading, not from audience behavior.

**The critic** writing on a single work solves a *single-point* evaluation problem that is, in the search frame, degenerate: $s_0 = w$, $\mathcal{G}$ is the aesthetic "correct reading" region, and $h$ is the critic's trained taste. The path $\gamma$ the critic traces in the essay is the *written trajectory* from the first line of the review to its concluding verdict. An honest critic's path should be a geodesic: the shortest argumentative distance from initial orientation to verdict, passing through the work's structure. Critics who meander are running a badly-calibrated search; critics who leap are using an inadmissible heuristic.

## 11.9 Implications for Aesthetic Philosophy {#implications}

The A* framing resolves a long-standing opposition between *aesthetic formalism* (which emphasizes the work's internal structure) and *aesthetic pragmatism* (which emphasizes use, context, and reception).

The formalist's object is the *state* of aesthetic space at a point — the tensor structure of the work. The pragmatist's object is the *search* — the path by which the work is approached, situated, deployed. The A* framework shows these are dual: the state is the node, the search is the traversal, and no verdict is deliverable without both. A formalism that ignores the search cannot explain taste disagreement without geometric curvature to blame. A pragmatism that ignores the state cannot explain why some works reward search regardless of context.

The framework also clarifies the status of *aesthetic expertise*. An expert is an agent whose heuristic $h$ has been calibrated over many searches, in many goal regions, across many traditions. They are fast because their heuristic prunes well. They are reliable because their $\varepsilon$ is small. They are disagreeable with each other not because aesthetics is arbitrary, but because their $\mathcal{G}$'s and $h$'s have been trained in different traditions, and the A* search is well-defined only relative to a goal.

## 11.10 Bridge: From Search to Symmetry {#bridge}

This chapter has developed the computational content of aesthetic reasoning. We have argued that curation, anthologization, and criticism are instances of A* search on the aesthetic manifold, that trained taste is a compiled heuristic, and that the filter bubble is the structural signature of greedy local search deployed on a task whose true objective is non-local.

The next chapter turns to *symmetry*. Every A* search requires a heuristic that respects the symmetries of the manifold it searches on: if the heuristic's output depends on coordinate-artifacts rather than on geometric content, the search is gauge-variant and its answers are arbitrary. Chapter 12 develops the aesthetic analogue of Noether's theorem — every continuous symmetry of the aesthetic manifold corresponds to a conserved quantity — and offers as empirical witness the cross-lingual invariance result of Chapter 17: across six language families, the structural-feature profile of a work is conserved under the symmetry "replace the language" with $\rho \approx 0.70$. That is a measured symmetry, and it is the strongest empirical finding the book has.

Elena, with whom this chapter opened, will choose her sixty stories. She will run, in effect, an A* search whose heuristic she cannot fully articulate and whose goal region she has defined more clearly to herself than she will ever make it in the introduction. If she is honest, the anthology's introduction will describe the $\mathcal{G}$ — the goal, the implicit theory of the decade's short story she is defending — and will not hide behind the algorithm's engagement-sorted list. Between her and the algorithm is not a disagreement about taste. It is a disagreement about which search problem the book is even solving.
