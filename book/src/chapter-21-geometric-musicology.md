# Chapter 21: Geometric Musicology — Structure, Genre, and the Sign That Flipped

**RUNNING EXAMPLE — Daniel's A/B Test**

Daniel is a music producer who has been paid, for the first time, to analyse why a track performed. His client's streaming numbers on one single are five times higher than the same artist's previous single, and the label wants to know whether the difference is promotion, playlist placement, or the song itself. Daniel has access to Spotify's eight acoustic features — danceability, energy, valence, tempo, key, mode, loudness, acousticness — the industry-standard scalars for describing a track. He runs the comparison. The features are nearly identical. Energy 0.73 vs. 0.71. Valence 0.55 vs. 0.58. Tempo within two BPM. The Spotify scalars say the songs are the same song. Daniel's ear, and the listener behaviour, say they are not.

Daniel is the protagonist because his problem is what happens when a scalar description of an aesthetic object is stripped of the very directions the object lives in. Music is not eight dimensions wide in any descriptive sense that captures the experience of listening. The eight acoustic features are a projection, useful for playlisting, impoverished for evaluation. The geometric alternative — which we report on in this chapter — is to represent a track as a trajectory in a learned high-dimensional audio-embedding space, compute the same four structural channels we computed for books in Chapter 20, and ask whether those channels predict listener engagement. The answer is yes, substantially more than Spotify's acoustic features do. The larger finding, which this chapter organizes itself around, is that *the channels have opposite signs in music than in books*. That cross-modality sign flip is the central surprise of this volume.

## 21.1 The Shape of the Problem {#21-1-the-shape-of-the-problem}

A track is not a point. It is a trajectory. Thirty seconds of audio through a music-pretrained encoder yields a sequence of hidden states — a walk through a high-dimensional space, with internal coherence, momentum, curvature, and a spectral signature relative to the corpus of all tracks. Classical MIR (music information retrieval) has known this in principle, but in practice has collapsed the trajectory to a scalar or a short vector: beats per minute, key, mode, mean spectral centroid, a few MFCC summary statistics, and more recently Spotify's proprietary eight-feature vector.

Chapter 15's scalar-irrecoverability theorem applies here with full force. No continuous function $\phi: \mathbb{R}^d \to \mathbb{R}^k$ with $k < d$ is injective. Projecting a 45-timestep × 1024-dimension MERT trajectory down to eight acoustic scalars destroys information that no amount of downstream statistical care can recover. If listener behaviour depends on the dimensions the projection discards, no Spotify-feature-based model can predict that behaviour, no matter how many tracks it trains on.

The empirical question we take up in this chapter is whether listener behaviour does depend on those dimensions. The answer, at $p = 0.001$ in head-to-head comparison, is yes.

## 21.2 The FMA Experiment {#21-2-the-fma-experiment}

The Free Music Archive (FMA) Medium subset contains $n = 24{,}801$ tracks with artist, genre, and `track_listens` annotations. We extracted 30-second clips, passed each through MERT-v1-330M (`m-a-p/MERT-v1-330M`, a music-pretrained transformer trained on ~160,000 hours of audio via self-supervised learning, layer-7 hidden states), and obtained a 45-timestep × 1024-dimension tensor per track. The trajectory analog of a book's paragraph walk is the timestep walk through MERT hidden space. The four structural channels from Chapter 20 port directly:

**A. Spectral divergences** of the track's timestep distribution vs. the corpus pooled distribution. KL, JS, Hellinger, Bhattacharyya, Mahalanobis-mean, TV.

**B. Internal coherence** — $\texttt{pair\_sim\_mean}$ and $\texttt{pair\_sim\_std}$ over timestep pairs within the track.

**C. Trajectory geometry** — $\texttt{step\_mean}$, $\texttt{step\_std}$, $\texttt{recur\_rate}$, $\texttt{curvature}$, $\texttt{path\_eff}$, and the autocorrelation and power-law family.

**D. Lasso on PCA spectrum** — project the 1024-dim timesteps onto a 128-dim corpus PCA basis; Lasso-regress against $\log(1 + \texttt{track\_listens})$ with artist-disjoint 5-fold cross-validation.

The artist-disjoint fold discipline matters enormously. If we permitted artist overlap across folds, the model would recover artist identity and inherit the long-tailed distribution of listens across artists as a spurious signal. Artist-disjoint folds ensure that what we are predicting is *not which artist this is*.

Under this discipline, the raw Lasso-on-PCA-spectrum yields $R = 0.302$, $z = 49.8\sigma$. This is the headline number before genre residualization.

## 21.3 The 91% Confession {#21-3-the-ninety-one-percent-confession}

Genre confounds listens at least as badly as it confounds Goodreads ratings. Pop tracks listen more than experimental tracks; rock tracks listen more than avant-garde; a genre classifier applied to the text of a track title would recover a fraction of the listen signal without hearing the music at all. We therefore residualized: each feature replaced by $f_i - \mathbb{E}[f_i \mid g]$ where $g$ is the FMA genre label; target $\log(1 + \texttt{listens})$ residualized identically.

The residualized hand-feature model yields $R = 0.043$, $z = 6.7$. The residualized Lasso-on-PCA-spectrum yields $R = 0.177$, $z = 28.3\sigma$. **91% of the hand-feature $R^2$ is genre confound** — a worse genre confound than books' 85%. The spectrum-Lasso survives genre residualization much better than the hand features do, because the spectrum encodes continuous audio structure that is not reducible to categorical genre.

The honest reframe parallels the books chapter: what the framework captures is *additional engagement signal beyond genre*. It does not capture *what makes a track good*; it captures a substantial fraction of what makes a track listened to, beyond what the track's genre alone would explain.

## 21.4 MERT vs. Spotify — The Head-to-Head {#21-4-mert-vs-spotify}

A legitimate objection is that a 28.3σ residualized signal might be achievable without MERT at all. Spotify's eight acoustic features — danceability, energy, valence, tempo, key, mode, loudness, acousticness — are publicly available for a subset of FMA tracks via the EchoNest/Spotify API. If Spotify's features capture the same thing, the case for a music-pretrained 330M-parameter encoder over a much simpler feature set is weak.

We ran the comparison on the overlap set ($n = 5{,}233$ tracks with both FMA audio and Spotify features), under identical artist-disjoint 5-fold CV, identical target, identical genre residualization. The results:

- MERT Lasso-on-spectrum: $R = 0.225$
- MERT hand features (channels A–C): $R = 0.151$
- Spotify's eight acoustic features: $R = 0.103$

Bootstrap test of the MERT-spectrum vs. Spotify difference: $p = 0.001$. MERT Lasso-on-spectrum beats Spotify's features by more than a factor of two, at a bootstrap-significant margin. The MERT hand features — the four structural channels, no Lasso — also beat Spotify, by a smaller margin. What the music-pretrained encoder sees, and what structural geometry picks up, is strictly more than what eight acoustic scalars see.

This is the empirical core of the chapter's claim against scalar feature vectors. Spotify's features are not nothing; they are a useful low-dimensional summary. They are also a projection that destroys more than half the engagement signal available in the same audio.

## 21.5 The Cross-Modality Sign Flip {#21-5-sign-flip}

Now the chapter's central finding.

We have been reporting Ridge and Lasso models, which use every feature simultaneously. The single-feature Spearman correlations tell a more revealing story. Consider two features that were load-bearing in the books chapter:

**$\texttt{pair\_sim\_mean}$ (internal coherence):**

- Books: $\rho = +0.126$, $8.4\sigma$. Higher coherence $\Rightarrow$ higher rating.
- Music: $\rho = -0.076$, $p = 5 \times 10^{-33}$. Higher coherence $\Rightarrow$ *fewer* listens.

**$\texttt{step\_mean}$ (trajectory jump size):**

- Books: $\rho = -0.096$, $6.4\sigma$. Smaller steps $\Rightarrow$ higher rating.
- Music: $\rho = +0.071$, $p = 4 \times 10^{-29}$. *Larger* steps $\Rightarrow$ more listens.

Both sign flips are individually significant beyond $p < 10^{-28}$. They are the same *features*, computed the same way, on the same mathematical objects (trajectories in a learned embedding space). They go the opposite direction when the modality changes from text to audio.

The simplest statement of the finding is that **books reward continuity and coherence; music rewards contrast and dynamic variation**. The aesthetic geometry is not merely a feature set; it has a *directionality* that is modality-specific.

This result could not have been found by a scalar-per-modality research program. A rating-regression on books and a listens-regression on music, each run in isolation, would have surfaced the coefficients but not the sign comparison. The sign flip is visible only because we used the same geometric feature set on both modalities and stood back to look.

## 21.6 What Music Theory Already Knew {#21-6-what-music-theory-already-knew}

The finding is novel in its empirical precision; it is not novel as an intuition. Music theorists have written about contrast, variation, tension, and release for centuries, and at least three lines of prior work anticipate the sign flip.

**Schenkerian analysis.** Schenker argued that a composition's *foreground* (surface-level variation) prolongs a stable *background* (the underlying harmonic structure). The sign of $\texttt{pair\_sim\_mean}$ in music is Schenker's foreground-prolongation principle in empirical form: a track that sits still on its background does not hold listener attention. The background provides coherence; the foreground provides the motion. Our feature measures only the foreground's step-by-step displacement, not the background it prolongs, and the measure says: tracks that move more get listened to more.

**Meyer's theory of musical expectation.** Leonard Meyer (*Emotion and Meaning in Music*, 1956) argued that musical meaning arises from the interaction of expectation and surprise. A track that never surprises is uninteresting; a track that surprises constantly is incoherent. Our features do not measure expectation-violation directly — MERT is not a predictive encoder of the kind Meyer would have wanted — but the $\texttt{step\_mean}$ sign flip suggests that listener engagement tracks the *motion* side of Meyer's coin more than the *coherence* side.

**Huron's ITPRA theory.** David Huron (*Sweet Anticipation*, 2006) extended Meyer into a five-phase account (Imagination, Tension, Prediction, Reaction, Appraisal) of how listeners form and resolve musical expectations. Huron's empirical work predicts that preferred music balances predictability and surprise. Our residualized effect sizes are small enough — $R = 0.177$ spectrum-Lasso, $\rho = -0.076$ on $\texttt{pair\_sim\_mean}$ alone — that they are entirely consistent with a Huron-style balance: the sign tells us which side of the balance the FMA corpus's listener population sits on, on average, in 2024 streaming-mediated listening conditions.

The modality-specific sign is, in other words, not an exotic finding. It is what a music theorist would have predicted. What is new is that a text-audio-comparable framework can measure the sign and state the direction at 28σ residualized.

## 21.7 Within-Genre Breakdown — and the Jazz / Classical Nulls {#21-7-within-genre}

We ran artist-disjoint Ridge regressions within each major FMA genre, to test whether the framework captures intra-genre engagement variation or only cross-genre structure. The results are heterogeneous in an interpretable way:

- Rock: $R = 0.139$, $n = 7{,}088$
- Electronic: $R = 0.143$, $n = 6{,}284$
- Hip-Hop: $R = 0.141$, $n = 2{,}190$
- Pop: $R = 0.185$, $n = 1{,}173$
- Classical: $R = -0.013$, $n = 584$ (null)
- Jazz: $R = 0.031$, $n = 384$ (null)

Pop, rock, electronic, and hip-hop all support intra-genre effect sizes in the $R = 0.14$–$0.19$ range. The framework captures real within-genre variation in these popular genres. Classical and jazz are null. This deserves interpretation rather than silence.

Two interpretations are compatible with the data.

**Interpretation A — internal structural saturation.** Classical and jazz pieces are, on average, much longer and more internally structured than a 30-second clip can represent. A 30-second window of a 9-minute symphonic movement or a 12-minute jazz improvisation captures a single phrase, not the piece's architecture. The trajectory features that read out of 30 seconds of a rock song's chorus read out of classical and jazz as a contextless slice whose structural signature depends heavily on which 30 seconds were sampled. The framework is not wrong about classical and jazz; it is measuring something that does not correspond to the thing listeners evaluate in those genres.

**Interpretation B — listens is the wrong target.** Classical and jazz audiences are smaller, more specialized, more driven by reputation and context than by track-level engagement. FMA's $\log(1 + \texttt{track\_listens})$ target is close to the right quantity for pop or rock, where an anonymous listener's willingness to play a track is a reasonable proxy for the track's appeal. It is close to the wrong quantity for classical and jazz, where cultural access, performer reputation, and discographic context dominate the listen signal and track-internal structure is confounded by all three.

We cannot distinguish Interpretation A from Interpretation B on the current data. Both would predict null coefficients; neither predicts a negative coefficient of substantial magnitude, and we do not observe one. A corpus that included full-piece audio and a non-listens target (critical rating, concert attendance, scholarly citation) would decide between them. We flag this as an open empirical question. What we do not do is claim that classical and jazz are aesthetically flat on the framework's axes; the framework may simply be measuring the wrong thing for these audiences.

## 21.8 Back to the Manifold {#21-8-back-to-the-manifold}

What does the sign flip tell us about the aesthetic manifold? Three things.

*First*, the manifold has modality-specific directions. The axes are shared — internal coherence, trajectory step-size, spectral divergence — but the signs attached to them are modality-dependent. A modality-free manifold would not have this property; a per-modality, scalar-per-modality account could not discover it. The geometric framework accommodates both the sharing and the signs.

*Second*, the manifold's directions are *psychologically grounded*. Books are consumed linearly, slowly, one paragraph at a time; a paragraph that breaks with the previous paragraph is experienced as a disruption. Music is consumed linearly, quickly, under 30 seconds to 5 minutes per piece; a timestep that does not break with the previous timestep is experienced as stagnation. The sign flip is not a mystery; it is a consequence of how the modalities are temporally consumed. Chapter 13's quantum-aesthetic account, where the observer's relationship to the work co-determines its evaluation, has a direct empirical witness in the sign flip: the *observer* is the same human, but the *observation mode* differs, and the manifold's directionality responds.

*Third*, the framework licenses cross-modality comparisons that scalar-per-modality approaches cannot express. We can now ask, of a given work, *in which channels is it book-like, and in which is it music-like?* A lyric poem sits between the modalities — delivered as text but consumed in close to musical time — and one could hypothesize that its optimal $\texttt{pair\_sim\_mean}$ sign is intermediate. A long-form ambient album consumed as a unit might sit on the book side of $\texttt{pair\_sim\_mean}$. The framework turns these hypotheses into experiments. We have not run them. Chapter 22 will take a speculative-but-principled step toward film, where the modality is more complex than either.

## 21.9 Against the Recommendation-Engine Worry {#21-9-recommendation-engine-worry}

A reasonable objection to any quantitative musicology is that streaming platforms will use it to optimize their recommendation engines in ways that narrow rather than broaden listener exposure. The worry is not small. Spotify's existing eight-feature recommendation stack has been widely criticized for pushing a within-genre sameness that rewards already-popular artists and suppresses structural innovation.

The geometric framework does not solve this problem. We argue it reframes it in two useful ways. First, the 91% genre-confound finding is a warning: any recommendation system that optimizes raw engagement will, to a first approximation, be optimizing genre membership, and the "personalization" it produces will be a within-genre clustering. The geometric framework *surfaces* this, in a way that Spotify's eight-feature model does not. Second, the sign-flip finding suggests that "engagement" in music is already optimizing for *contrast* rather than for coherence — which has very different aesthetic implications than the books case. A recommender that over-weights the $\texttt{step\_mean}$ direction would, predictably, push listeners toward high-variation tracks. Whether that is desirable is a curatorial question, not a technical one, and it is one a practicing musicologist is better-positioned to answer than a recommendation engineer.

This is, again, not a solution. It is a repositioning of the question. The framework allows the curatorial community to see the direction along which a recommendation engine is optimizing and to argue, in specific terms, for or against that direction.

## 21.10 Honest Failure Modes {#21-10-honest-failure-modes}

**The Hellinger saturation.** In the music experiment, the Hellinger feature computed on full 128-dim PCA saturates at ~1.0 for most tracks because 45 timesteps in 128 dimensions is ill-conditioned for Gaussian-fit distributional estimation (too many parameters per sample). In a K = 32 PCA subspace, the Hellinger signal is recovered and the verdict is unchanged; Bhattacharyya directly is preferable in practice and we recommend it over Hellinger for music-scale trajectories. We flag the saturation honestly; it does not affect the headline results but it is a lesson for practitioners.

**30 seconds is not a song.** The FMA pipeline processes 30-second clips, not full tracks. For pop songs, 30 seconds is roughly one chorus plus a verse, which captures the track's structural signature reasonably well. For classical and jazz, 30 seconds is not the piece; see Section 21.7. We have not yet run a full-track version of the pipeline; the compute cost is substantial and we do not expect the headline effect sizes to change by more than a factor of 1.5 in either direction, but we have not confirmed this.

**MERT is Western-music-biased.** MERT-v1-330M was trained on a large corpus of Western popular and classical music. Non-Western musical traditions — Carnatic, Hindustani, gamelan, Arabic maqam, West African polyrhythmic music — are underrepresented in training. The framework's portability to these traditions is an open question that we have not yet tested, and we would expect effect sizes to degrade when the encoder is pushed off-distribution.

**The cross-lingual invariance of Chapter 20 has no direct audio analog.** LaBSE is language-agnostic by training; MERT is not modality-agnostic across music traditions in the same way. A rigorous cross-tradition invariance study in music — the equivalent of our 19-language books study — is not yet possible without either a genuinely cross-tradition music encoder or a post-hoc alignment across tradition-specific encoders. We flag this as a future-work gap.

**Listens is a noisy target.** We have used $\log(1 + \texttt{track\_listens})$ throughout. This target is confounded by algorithmic recommendation, by release date, by artist promotion, and by platform policy. Residualization by genre addresses part of this; it does not address all of it. A more principled target (say, a weighted combination of critical reception and independent listener rating) is not available at FMA scale.

## 21.11 Bridge to Film and Television {#21-11-bridge}

Chapter 20 established that books live on a manifold whose directions are measurable, interpretable, and cross-lingually invariant. This chapter has established that music lives on the same manifold — same feature definitions, same pipeline architecture — but with *opposite signs* on the two most interpretable channels. Books reward continuity; music rewards contrast. The aesthetic manifold has modality-specific directionality.

The next chapter asks what happens in film. The modality is more complex: a shot sequence is something like a paragraph sequence, but the encoder of a shot is much less well-studied than LaBSE or MERT, and film has an editing layer (the cut) that has no direct analog in either books or music. We have not yet run the film experiment. Chapter 22 is therefore speculative-but-principled: we describe what the pipeline would look like, what predictions the framework makes, and what an empirical result would need to show to confirm or falsify the predictions. Among those predictions is the following: if the continuity-vs-contrast dimension extends to film, it will have a *specific direction*, and we state the direction before running the experiment so that the result can be adjudicated honestly.
