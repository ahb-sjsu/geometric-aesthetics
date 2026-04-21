# Appendix A: Related Work and Differentiation

This appendix situates *Geometric Aesthetics* within the prior art. Aesthetics is an old subject and an unusually promiscuous one: philosophers, psychologists, computer scientists, neuroscientists, information theorists, and more recently large-scale machine-learning practitioners have all staked claims on what "beauty" and "aesthetic quality" mean and how to measure them. We do not pretend to survey this literature exhaustively. Our aim is narrower. We lay out the lineages our framework inherits from, the lineages it breaks from, and the specific claims that, to the best of our knowledge, originate here.

The reader should treat the enumerated references as a map of the conversation we believe we are joining. Where a citation is representative rather than exhaustive — standing in for a broader literature on, say, BERT-based rating prediction or predictive-processing accounts of aesthetic experience — we note this in context. We would rather be corrected on a specific reference than quiet about the surrounding tradition.

## A.1 Birkhoff and the Measure-of-Aesthetics Tradition

George Birkhoff's *Aesthetic Measure* (1933) is where any serious attempt at computational aesthetics begins. Birkhoff proposed the ratio

$$ M = \frac{O}{C} $$

where $O$ is "order" and $C$ is "complexity", and defended it on ornaments, vases, melodies, and poems. A flower-pattern with high symmetry and low visual clutter has high $M$; a cluttered, asymmetric one has low $M$. The construction has been criticized on many grounds — the order/complexity operationalizations are handcrafted per-modality; the scalar $M$ collapses structure into a single number; the "aesthetic measure" conflates formal regularity with felt beauty. But Birkhoff's framing is the ancestor of everything we do. He took seriously the idea that aesthetic judgment has a computable substructure.

Our relationship to Birkhoff is one of inheritance-with-inversion. We inherit: that aesthetic quality has structural content amenable to measurement. We invert: the scalar. Birkhoff wanted one number. We argue (Chapters 2, 6, 15) that the scalar is precisely what cannot be recovered without loss from the underlying geometric object. In our Phase 4 music experiments, the sign of `pair_sim_mean` reverses between books and music: higher internal coherence predicts *higher* ratings in books and *lower* listens in music. Any framework that reports a single scalar $M$ cannot express this result. Birkhoff's ratio, applied consistently across modalities, would either predict that novels and pop songs are optimal at the same level of internal coherence (false) or require per-modality recalibration (at which point the scalar is modality-specific and no longer a universal measure).

## A.2 Information Aesthetics: Bense, Moles, Nake

The information-theoretic tradition — Max Bense's *Aesthetica* (1954–1960), Abraham Moles's *Information Theory and Esthetic Perception* (1958/1966), Frieder Nake's computational art — carried Birkhoff's program into the Shannon era. The key move was identifying $C$ with Shannon information or Kolmogorov complexity and $O$ with redundancy, symmetry group order, or compressibility. This was generative: Bense's Stuttgart school produced actual computer-generated art and developed a vocabulary (aesthetic state, macro-aesthetic, micro-aesthetic) that survives in contemporary generative-art discourse.

Two limitations constrain this tradition for our purposes. First, information aesthetics typically operates on the surface signal — the pixel array, the symbol sequence, the waveform — rather than on a learned semantic representation. A novel's aesthetic content is not well summarized by the bit-entropy of its character stream. Second, the tradition shares Birkhoff's commitment to a scalar quality measure and therefore faces the same sign-flip problem: if the same redundancy-complexity tradeoff is supposed to govern all art, the empirical modality-specificity of aesthetic direction cannot be expressed.

We take from this tradition the habit of thinking about aesthetic objects as probability distributions and information flows. Our spectral-divergence channel (A in the Phase 1 results) is directly descended from Bense-Moles thinking: we measure how a work's paragraph distribution diverges from a reference distribution, using Kullback–Leibler, Jensen–Shannon, Hellinger, Bhattacharyya, total-variation, and Mahalanobis distances. What we add is (i) that the distributions live in a *learned* semantic space (LaBSE, MERT) rather than in raw signal space, and (ii) that this channel is one of four — the other three (internal coherence, trajectory geometry, Lasso-basis) are not reducible to information content.

## A.3 Computational Creativity: Colton, Wiggins

Simon Colton's work on computational creativity (Colton 2008; Colton et al. 2012) and Geraint Wiggins's formal framework for creative systems (Wiggins 2006) approach aesthetics from the generative side: not "how do we measure beauty in existing works" but "how do we build systems that produce works that are received as beautiful." Wiggins's framework is explicit about the triple of concept-space, traversal-strategy, and evaluation-function, and is careful to distinguish transformational from exploratory creativity (borrowing from Margaret Boden).

We are downstream of this tradition in Chapter 18 (Geometric Aesthetics for Artificial Agents) and Chapter 19 (DEME for Aesthetics). The present volume is primarily about measurement rather than generation, but the measurement framework implies a generation framework: an aesthetic manifold with geometric structure is something an agent can navigate, and the four-channel decomposition gives a generative agent four distinct knobs to turn rather than a single scalar to maximize. Our differentiation: Colton and Wiggins write mostly at the level of architecture and philosophy; we provide empirically-fit geometric objects that a creative system could, in principle, use as its evaluation function.

## A.4 Large-Scale Book-Rating Prediction

There is an ML literature on predicting book ratings from text — typically Goodreads ratings from review text, sometimes from the book content itself when available. Representative threads include:

- BERT-based regression on Goodreads review text predicting star ratings (several papers in the 2019–2022 window; representative: Maharjan, Arevalo, Montes, González, and Solorio 2017, *A Multi-task Approach to Predict Likability of Books*, EACL);
- Meta-review-level aggregation studies using Amazon and Goodreads data (e.g., McAuley, Targett, Shi, and van den Hengel 2015, *Image-based Recommendations on Styles and Substitutes*, SIGIR; and McAuley and Leskovec 2013, *Hidden Factors and Hidden Topics: Understanding Rating Dimensions with Review Text*, RecSys);
- Literary-quality classification using stylometric and embedding features (Underwood's work in the digital humanities is adjacent; Underwood 2019, *Distant Horizons*, is directly relevant).

Our Phase 1 experiment differs from most of this literature in three load-bearing ways. First, we predict from the book's content, not from the reviews. This is methodologically harder (the text does not contain any direct evidence of reception) and theoretically more interesting (we are asking what in the work itself correlates with received evaluation). Second, we use author-disjoint cross-validation. An author-leaking split inflates reported $R^2$ by learning author identity rather than aesthetic signal. Third, and most importantly, we report and explicitly decompose the genre confound: 85% of our headline $R^2$ was lost to within-genre residualization, and we report the residualized number ($R=0.093$, $z=6.5\sigma$) as the honest result. Most published book-prediction work does not residualize by genre and does not disclose what fraction of the reported performance survives within-genre.

## A.5 Music Popularity Prediction: Spotify Features and MERT

Music-popularity prediction has a longer and more industrialized literature, anchored by the eight acoustic features Spotify inherited from Echonest (acousticness, danceability, energy, instrumentalness, liveness, speechiness, tempo, valence). The original Echonest technical notes, and the MIR literature that built on them (Bertin-Mahieux, Ellis, Whitman, and Lamere 2011, *The Million Song Dataset*, ISMIR), established a handcrafted feature vocabulary that was adopted industry-wide. Downstream work predicting streaming counts, chart performance, or skip-rates from these features is extensive (representative: Interiano, Kazemi, Wang, Yang, Yu, and Komarova 2018, *Musical trends and predictability of success in contemporary songs in and out of the top charts*, Royal Society Open Science 5(5): 171274).

Self-supervised audio representation learning changed the scene. MERT (Li et al. 2023, *MERT: Acoustic Music Understanding Model with Large-Scale Self-Supervised Training*) is the model we use: a music-pretrained encoder trained on ~160k hours of music with masked-acoustic-modelling and student-teacher objectives, producing 1024-dimensional hidden states at layer 7 that generalize across downstream music-understanding tasks. MuLan (Huang et al. 2022), Jukebox (Dhariwal et al. 2020), and MULE (McCallum et al. 2022) are in the same family.

Our Phase 4 experiment compares three featurizations head-to-head on a shared $n=5{,}233$ subset: Spotify's 8 acoustic features ($R=0.103$), MERT hand-engineered aggregates ($R=0.151$), and MERT Lasso-on-PCA-spectrum ($R=0.225$). The bootstrap difference MERT-spectrum vs Spotify-8 is $p=0.001$. This is the first direct three-way comparison we are aware of that holds the track-set fixed and isolates representation quality from dataset differences. The MERT-vs-Spotify delta is not huge ($\Delta R \approx 0.12$), but it is robust and constitutes our empirical case that self-supervised music representations carry aesthetic signal that handcrafted Echonest features do not.

Our second music-specific contribution is the cross-modality sign flip. `pair_sim_mean` has $\rho=+0.126$ ($8.4\sigma$) for books and $\rho=-0.076$ ($p=5\times 10^{-33}$) for music; `step_mean` has $\rho=-0.096$ ($6.4\sigma$) for books and $\rho=+0.071$ ($p=4\times 10^{-29}$) for music. Both flips are robust. We are not aware of any prior work that identifies this pattern, because the prior work typically operates in a modality-specific feature space (Spotify features are audio-specific; literary-quality features are text-specific) and therefore cannot ask the cross-modality question.

## A.6 Cross-Lingual Sentence Embeddings

The cross-lingual embedding literature is where our strongest empirical result (Phase 3) lives. Four lineages matter:

**Artetxe and Schwenk (2019), *Massively Multilingual Sentence Embeddings*.** LASER: a single BiLSTM encoder trained on 93 languages with a translation-equivalence objective. LASER established the "one shared semantic space for all languages" target that subsequent work refined.

**Reimers and Gurevych (2019, 2020), *Sentence-BERT* and *Making Monolingual Sentence Embeddings Multilingual Using Knowledge Distillation*.** SBERT's siamese-network framing, then the distillation approach that bootstraps multilingual encoders from strong monolingual ones.

**Conneau et al. (2020), *Unsupervised Cross-lingual Representation Learning at Scale* (XLM-R).** Demonstrates that multilingual encoders can be trained with purely language-modelling objectives and still produce a usable shared space.

**Feng et al. (2022), *Language-agnostic BERT Sentence Embedding* (LaBSE).** Our encoder. LaBSE combines a masked-language-modelling objective with a translation-ranking objective on bilingual pairs across 109 languages, producing a 768-dimensional sentence embedding space in which semantically equivalent sentences across languages live close together. LaBSE's target is semantic equivalence of isolated sentences; the standard evaluation is cross-lingual retrieval and bitext mining.

Our Phase 3 experiment uses LaBSE in a way that is, to our knowledge, new. We encode paragraph-level text (not sentence-level) in 19 non-English languages, project into a PCA-128 basis *fit on the English corpus* (same axes across all languages, never refit per language), and then measure whether structural features (spectral divergences, coherence, trajectory geometry) behave consistently across languages. They do: $\rho \approx 0.71$ for `pair_sim_mean` and `mahal_mean`, $\rho \approx 0.67$ for Hellinger/Bhattacharyya/JS. The headline is EN↔FI Hellinger $\rho=+0.77$, $n=288$, $p=8\times 10^{-57}$.

This is our Noether-style empirical finding (Chapter 12). LaBSE is designed for semantic equivalence at the sentence level; we are using it to test whether *structural aesthetic signal* is invariant under language change at the book level. The invariance is empirically witnessed — we did not build it in, LaBSE does not optimize for it, and the fact that it emerges under a PCA basis fit on English alone is strong evidence that the aesthetic structure lives above the level of any particular language's surface.

## A.7 Neural Aesthetics and EEG Correlates

A loosely confederated body of work — Chatterjee and Vartanian's *Neuroaesthetics* (2014), the EEG beauty-judgment literature (e.g., Jacobsen and Höfel 2003, *Descriptive and evaluative judgment processes: Behavioral and electrophysiological indices of processing symmetry and aesthetics*, Cognitive, Affective, & Behavioral Neuroscience 3(4): 289–299), and fMRI studies of reward correlates of aesthetic experience — attempts to ground aesthetic evaluation in neural substrate. This is important but tangential to our project. We measure structure in the stimulus and its correlation with received evaluation; neuroaesthetics measures the brain response to stimuli. The two approaches are complementary. A complete account of aesthetic judgment needs both: what in the work has structure, and what in the observer is responsive to that structure. We limit ourselves to the first question in this volume.

The closest bridge is work on predictive-processing accounts of aesthetic experience (Van de Cruys and Wagemans 2011, *Putting reward in art: A tentative prediction error account of visual art*, i-Perception 2(9): 1035–1062; Koelsch, Vuust, and Friston 2019, *Predictive Processes and the Peculiar Case of Music*, Trends in Cognitive Sciences 23(1): 63–77), which frame aesthetic pleasure as the dynamics of prediction error over time. Our trajectory-geometry channel — `step_mean`, `step_std`, `acf1_top3`, `curvature`, `path_eff`, `powerlaw_slope` — is compatible with this framing: we are measuring how a work moves through semantic space over time, which is a stimulus-side quantification of exactly what predictive-processing accounts claim the brain is tracking.

## A.8 Adjacent Formal Frameworks

Several mathematical traditions sit near ours without being aesthetics-specific. **Information geometry** (Amari 1985; Amari and Nagaoka 2000) gives us the language of statistical manifolds with Fisher-Rao metric; our paragraph distributions are points on such a manifold, and our Mahalanobis and KL features are geodesic-related quantities on it. **Topological data analysis** (Carlsson 2009; Ghrist 2014) provides persistent-homology tools for trajectory shape that are complementary to our `curvature` and `path_eff` features and that we plan to incorporate in Phase 5. **Optimal transport** (Villani 2008; Peyré and Cuturi 2019) provides Wasserstein distances between paragraph clouds that we did not use here but that would be a natural extension of our divergence channel.

These frameworks are substrate, not competitors. We borrow their tools without claiming their frames. Our frame — that aesthetic judgment specifically has modality-specific geometric structure that is cross-linguistically invariant — is, as far as we can tell, original to this volume.

## A.9 Companion Volume: *Geometric Ethics*

Finally, we differentiate from our own prior volume. *Geometric Ethics* (Bond 2026) establishes the mathematical apparatus — manifolds, stratification, gauge structure, tensor hierarchy, Bond Index — for a sibling domain: moral evaluation. *Geometric Aesthetics* inherits the apparatus and applies it to a new domain with different data. Where Ethics used synthetic scenario data and algebraic verification (the D₄ gauge structure on Hohfeldian states, the DEME pipeline), Aesthetics uses large-scale natural data: 4,998 English books, 4,683 non-English books, 24,801 music tracks. Where Ethics's symmetry claims are proved algebraically, Aesthetics's symmetry claims (Chapter 12) are witnessed empirically: cross-lingual invariance is the Noether-style symmetry, measured not assumed.

The relationship to the companion volume is one of methodological parallel with empirical independence. A reader who rejects *Geometric Ethics* on normative grounds can still accept *Geometric Aesthetics* on empirical grounds; the two stand or fall separately, even though they share a framework.

## A.10 What We Claim Is New

Consolidating the differentiation above, the contributions we believe are original to this work are:

1. **Multi-channel geometric decomposition.** The four-channel structure (spectral divergences, internal coherence, trajectory geometry, Lasso-basis spectrum) is, to our knowledge, not present in the prior aesthetic-measurement literature. Birkhoff–Bense–Moles collapse structure into a scalar; we decompose it into independent geometric channels and report effect sizes per channel.

2. **Cross-lingual invariance as a witnessed symmetry.** The $\rho \approx 0.7$ invariance of aesthetic structural features across 6 language families, using a shared PCA basis fit on English alone, is an empirically-witnessed Noether-like invariance. We do not claim this was unknowable in principle; we claim no one we have found has measured it.

3. **Cross-modality sign-flip finding.** The same structural feature (`pair_sim_mean`, `step_mean`) has opposite sign of correlation with received evaluation in books vs. music, robust at $p<10^{-28}$. This is inexpressible in scalar-aesthetic-measure frameworks and, we argue, undermines any account of aesthetic quality that assumes a single universal preference direction across modalities.

4. **Honest genre-confound decomposition.** Roughly 85% of headline book $R^2$ and 91% of headline music hand-feature $R^2$ are genre confound. We report the residualized numbers as the honest effect sizes. This is methodological hygiene that, in our reading of the rating-prediction literature, is often omitted.

5. **Empirical reframe from "predicts rating" to "additional aesthetic signal beyond genre."** The residualized result is real ($R=0.093$, $p=5.7\times 10^{-11}$ in books; $R=0.177$, $z=28.3\sigma$ in music spectrum) but modest. We frame it correctly rather than puffing the headline number.

We believe (1)–(5) are individually defensible and jointly constitute the differentiated contribution of this volume. Where we are mistaken — where a paper we missed has already made one of these claims — we will correct the citation record in subsequent editions. We would rather be corrected than be quiet.

## A.11 Comparison Summary

The following table summarizes the differentiation. We deliberately do not fill every cell; some prior traditions are methodologically adjacent rather than direct comparators, and forcing a one-to-one mapping would misrepresent the relationship.

| Prior Tradition | Core Contribution | Limitation for Our Question | What *Geometric Aesthetics* Adds |
|---|---|---|---|
| Birkhoff 1933 | Aesthetic measure as $O/C$ | Scalar output; handcrafted per modality | Four-channel geometric decomposition; sign-flip evidence against scalar framing |
| Bense / Moles / Nake | Information-theoretic aesthetics | Surface-signal; scalar | Learned-representation features; multi-channel |
| Colton / Wiggins | Computational creativity architecture | Generation-focused, not measurement | Empirically-fit geometric evaluation functions |
| Book-rating ML (Maharjan et al. 2017; McAuley and Leskovec 2013) | Large-scale rating prediction | Review-text-based; no genre residualization | Content-based; author-disjoint CV; genre-residualized reporting |
| Spotify / Echonest features | Industry-standard acoustic features | Handcrafted; modality-specific | MERT self-supervised features with $\Delta R=0.12$ over Spotify-8; cross-modality structural features |
| MERT (Li et al. 2023) | Music-pretrained SSL encoder | Designed for MIR tasks | Downstream geometric-aesthetics application; cross-modality structural comparison with books |
| LaBSE (Feng et al. 2022) | Language-agnostic sentence embedding | Sentence-level semantic equivalence | Paragraph-level aesthetic-structure invariance across languages; shared-PCA-basis design |
| Artetxe–Schwenk, Reimers–Gurevych, Conneau (XLM-R) | Cross-lingual representation learning | Task-agnostic; no aesthetic evaluation | Phase 3 cross-lingual aesthetic invariance as witnessed Noether-like symmetry |
| Neuroaesthetics / EEG (Jacobsen and Höfel 2003; Chatterjee and Vartanian 2014) | Neural correlates of aesthetic experience | Response-side only | Stimulus-side geometric structure complementary to neural measurements |
| Information geometry, TDA, optimal transport | Mathematical substrate | Not aesthetics-specific | Domain-specific application with empirical calibration |
| *Geometric Ethics* (Bond 2026) | Companion framework in moral domain | Different target variable | Parallel apparatus; independent empirical base |

The pattern across the table is consistent: prior work captures important pieces of the aesthetic-measurement problem, but no prior work we have found captures the combination of content-based, multi-channel, cross-linguistically invariant, cross-modality-comparable, genre-confound-honest decomposition that *Geometric Aesthetics* attempts. If a reader knows of prior work that pre-empts one of these claims, we consider the correction a favor.
