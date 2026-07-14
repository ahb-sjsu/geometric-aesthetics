# Chapter 17: Empirical Evidence for Geometric Aesthetics {#chapter-17-empirical-evidence-for-geometric-aesthetics}

*Ethics is not a number. Neither, we will argue, is beauty.*

## 17.1 The Question Aesthetics Poses for Geometry

The preceding thirty chapters have developed a geometric framework for ethics and traced its consequences through ten domains of application — economics (Chapter 20), clinical ethics (Chapter 21), jurisprudence (Chapter 22), finance (Chapter 23), theology (Chapter 24), environmental ethics (Chapter 25), algorithmic systems (Chapter 26), bioethics (Chapter 27), and the conduct of war (Chapter 28). In each case, the move has been the same: take a domain whose central judgments are widely felt to resist formalization, locate its active manifold dimensions, and show that the apparent resistance is scalar-projection artefact rather than genuine formlessness. The moral content is not absent from the mathematics; it is obscured by the compression to a single score.

This chapter pursues the same move in a domain that has, if anything, resisted formalization more stubbornly than ethics: aesthetic judgment. Beauty, taste, literary merit, the quality of a piece of music — these have been the traditional exhibits for the view that evaluative content is ineliminably subjective, that *de gustibus non est disputandum*, that whatever structure exists is at best sociological rather than mathematical. The history of aesthetics from Kant through the 20th century is in large part a history of negotiating the apparent gap between the felt objectivity of aesthetic judgment ("this is beautiful, not merely pleasing to me") and the absence of any measurable quantity that could ground that objectivity.

The moral manifold hypothesis (Chapter 5) proposes that ethical content has geometric structure: that meaning is not merely encoded in a representation but *is* structure in the representation. If the hypothesis is correct in ethics, it imposes a test condition on its own scope. Either aesthetic judgment also carries geometric content — in which case the framework extends — or it does not, in which case the framework is more local than we have claimed. We take the test seriously in this chapter. We will not stipulate that aesthetics has geometry; we will look for it, measure it, and report what we find, including the parts that are smaller than we hoped and the parts that did not survive control.

The finding, stated plainly and in advance: aesthetic judgment in two modalities (literary text and music) carries measurable geometric content in pretrained representation spaces, that content is partly language-invariant, and — most interestingly — its *directionality* is modality-specific in ways that appear robust. The effect sizes are modest in absolute terms ($R^2 \approx 0.01$–$0.09$ after controls), but the statistical signatures are strong enough ($6\sigma$ to $28\sigma$ after genre residualization) that the question is no longer whether the signal exists but what it means.

## 17.2 The Embedding-Cloud as Aesthetic Object

We begin with a technical reframing. In the geometric ethics program, a moral situation is mapped to a point (or a path) on the moral manifold $\mathcal{M}$, and moral evaluation is the computation of local structure — geodesic length, boundary crossings, holonomy — at or near that point (Chapters 5, 10, 11). The analogous move in aesthetics requires us to specify the mapping from aesthetic object to mathematical object.

Our proposal is that a text or musical work should be represented not as a single embedding but as a *cloud*. Let $W$ denote a work — a novel, a short story, a musical piece — and let $\{t_1, \ldots, t_N\}$ denote a tokenization into content units (sentences, paragraphs, audio windows). A pretrained encoder $\phi : \text{content} \to \mathbb{R}^d$ maps each unit to a point in representation space:

$$
X(W) = \{\phi(t_1), \phi(t_2), \ldots, \phi(t_N)\} \subset \mathbb{R}^d.
$$

The work, as an aesthetic object, is then the cloud $X(W)$ rather than any single point. The candidate claim is that aesthetic features of $W$ are geometric features of $X(W)$ — spread, internal coherence, trajectory shape, divergence from a corpus prior — and that judgments of aesthetic quality, where they are stable across readers or listeners, track these geometric features.

This reframing sits naturally inside the tensor hierarchy of Chapter 6. The individual embeddings $\phi(t_i)$ are rank-1 content vectors. The cloud $X(W)$ admits a rank-2 summary in the form of its empirical covariance $\Sigma(W) = \frac{1}{N-1}\sum_i (\phi(t_i) - \bar{\phi})(\phi(t_i) - \bar{\phi})^\top$. Higher-rank structure — trajectory curvature, recurrence, autocorrelation of the token sequence — enters as rank-3 and above. The aesthetic manifold, if it exists, is the quotient space on which the rating- or reception-relevant features of these tensors live.

Two features of the construction are worth flagging. First, the encoder $\phi$ is not chosen by us — it is a fixed pretrained model (LaBSE for text, MERT-v1-330M for music). The aesthetic structure we find is therefore always *relative to* a representation space that was trained for other purposes (multilingual alignment; music tagging). This is a version of the origin-of-metric problem discussed in Chapter 9: the metric we use is inherited, not derived from first principles, and its status as "the" aesthetic metric is provisional. Second, the cloud representation discards order at the rank-2 summary level and preserves it only in the trajectory channel. Pure bag-of-embeddings aesthetics is therefore testable as a limit case.

## 17.3 Four Channels of Aesthetic Structure

Exploratory work on Project Gutenberg and FMA-Medium convinced us that aesthetic structure, if it lives in the embedding cloud, expresses itself through at least four distinct mathematical channels. We describe each here; their empirical performance is the subject of the next three sections.

### 17.3.1 Spectral Divergence from a Corpus Prior

Let $P$ denote an empirical distribution estimated from a reference corpus — a "prior" over content embeddings — and let $Q(W)$ denote the empirical distribution of embeddings for the work $W$. Modeling each as a multivariate Gaussian $\mathcal{N}(\mu, \Sigma)$ in a $K$-dimensional PCA subspace, we compute five classical divergences:

$$
D_{\mathrm{KL}}(Q \Vert P), \quad
D_{\mathrm{JS}}(Q, P), \quad
H(Q, P) = \sqrt{1 - \mathrm{BC}(Q, P)}, \quad
D_{\mathrm{Bhatt}}(Q, P), \quad
D_{\mathrm{Mahal}}(\mu_Q, \mu_P, \Sigma_P),
$$

where $\mathrm{BC}$ is the Bhattacharyya coefficient. The intuition is that a work that is statistically far from the corpus prior — distinctive in its content distribution — is a candidate for being aesthetically marked. The divergence family is not a single feature; each member emphasizes different geometric relations (tail behavior for KL, centroid displacement for Mahalanobis, distributional overlap for Bhattacharyya and Hellinger).

### 17.3.2 Internal Coherence

Let $\mathrm{pair\_sim\_mean}(W)$ denote the mean cosine similarity among pairs of embeddings drawn from $X(W)$:

$$
\mathrm{pair\_sim\_mean}(W) = \frac{2}{N(N-1)} \sum_{i < j} \frac{\phi(t_i)^\top \phi(t_j)}{\Vert \phi(t_i) \Vert \, \Vert \phi(t_j) \Vert}.
$$

This is a scalar measure of how tightly the work coheres in content-space — how much its parts are about the same things. High values indicate a work that returns repeatedly to a narrow region of content-space; low values indicate a work that ranges widely. Whether coherence is an aesthetic virtue or a sign of monotony is an empirical question that we will find has a modality-dependent answer.

### 17.3.3 Trajectory Geometry

The content cloud $X(W)$ has a natural ordering inherited from the work itself (the sequence of sentences, of audio windows). The trajectory $\phi(t_1) \to \phi(t_2) \to \cdots \to \phi(t_N)$ is a discrete curve in $\mathbb{R}^d$, and its shape admits geometric summaries:

- **Step size** $\mathrm{step\_mean} = \frac{1}{N-1}\sum_i \Vert \phi(t_{i+1}) - \phi(t_i) \Vert$, capturing how much the content jumps between adjacent units.
- **Recurrence rate** $\mathrm{recur\_rate}$, the fraction of pairs $(i, j)$ with $|i-j| > \tau$ such that $\Vert \phi(t_i) - \phi(t_j) \Vert < \varepsilon$.
- **Discrete curvature** $\kappa_i$ at position $i$, computed from the angle subtended by the triple $(\phi(t_{i-1}), \phi(t_i), \phi(t_{i+1}))$.
- **First-lag autocorrelation** $\mathrm{acf1\_top3}$, the top-3 PCA coordinates' lag-1 autocorrelation along the trajectory.

These summarize, respectively, pacing, return-to-theme, sharpness of transition, and memory structure. They are the aesthetic correlates of the path-dependence features developed in Chapter 10.

### 17.3.4 Learned-Direction Projection via Lasso on PCA Spectrum

The three channels above are hand-crafted. A fourth channel lets the data speak: we compute the PCA spectrum of the content cloud in a fixed $K=128$ basis learned from a large reference corpus, take the per-component variance vector $\lambda(W) = (\lambda_1, \ldots, \lambda_{128})$, and fit an $L_1$-regularized linear model

$$
\hat{y}(W) = \beta_0 + \sum_{k=1}^{128} \beta_k \lambda_k(W), \quad \Vert \beta \Vert_1 \le \tau,
$$

to predict the aesthetic target $y$. The non-zero coefficients identify specific PCA directions along which corpus-scale variance structure aligns with reception. In the book experiment, 71 of 128 coordinates receive non-zero weight and — importantly — they turn out to be interpretable as genre axes under post-hoc inspection. The Lasso channel is therefore diagnostic as well as predictive: it exposes the confounds hiding inside the spectral features.

## 17.4 Empirical Findings (Books)

### 17.4.1 Discovery

The first experiment tests the channels against book reception. We paired $n = 4{,}998$ English-language books from Project Gutenberg with their average Goodreads rating, using author-disjoint 5-fold cross-validation to prevent leakage through idiosyncratic authorial style. Sentences were encoded with LaBSE; the four channels were extracted and combined in a Ridge regressor.

The headline result: discovery $R = 0.241$, $R^2 = 0.058$, corresponding to $z = 17\sigma$ against the null of zero correlation. The channels' individual signatures:

- Spectral divergences (KL, JS, Hellinger, Bhattacharyya, Mahalanobis) each register at roughly $8\sigma$.
- Internal coherence: $\mathrm{pair\_sim\_mean}$ shows $\rho = +0.126$, $z = 8.4\sigma$. Higher-coherence books rate higher.
- Trajectory geometry: step size, recurrence, top-PCA autocorrelation, and discrete curvature contribute at $3$–$6\sigma$ individually.
- Lasso-on-spectrum: 71 of 128 PCA components receive non-zero weight.

Taken at face value, this would be a clean confirmation of the embedding-cloud-as-aesthetic-object hypothesis. It is not what we report.

### 17.4.2 The Within-Genre Control

The Lasso coefficients, inspected, told a disquieting story: the non-zero PCA components were interpretable as genre axes. A component that separates "philosophy" from "adventure" is not an aesthetic feature; it is a content feature. If the discovery signal is driven by genre, and genre is correlated with rating for reasons that have nothing to do with the geometric content of the work, the headline $R = 0.241$ is a genre detector wearing an aesthetic costume.

We residualized the rating against genre (a dummy-coded categorical variable over the Library of Congress top-level classifications), and repeated the analysis on the residuals. The result: $R = 0.093$, $R^2 = 0.009$, $z = 6.5\sigma$, $p = 5.7 \times 10^{-11}$.

The numbers are honest about the stakes. $85\%$ of the apparent $R^2$ was genre confound. The remaining $0.9\%$ of variance is not nothing — at $n \approx 5{,}000$ it is an extraordinarily robust effect, with a $p$-value that would survive almost any multiple-comparison correction — but it is not what the discovery number suggested. The correct summary is not "geometry predicts rating" but "geometry carries additional aesthetic signal beyond genre."

Restricting to the largest intra-genre sub-corpus (Fiction, $n = 2{,}250$) reproduces the effect: $R = 0.131$, $z = 6.2\sigma$. The Non-fiction and History/Biography sub-corpora show null results within-genre, which we interpret conservatively — either the aesthetic channels are genre-specific, or these sub-corpora have higher internal heterogeneity and need larger samples. We do not claim universality; we claim a residual, intra-Fiction signal of approximately 1–2% of variance.

This is the first empirical lesson of the chapter, and it will recur. Aesthetic geometry, measured crudely, is dominated by confounds. Measuring it cleanly requires aggressive control of the confound and explicit acknowledgement of what survives.

## 17.5 Cross-Lingual Invariance

The within-genre result, while honest, leaves open a deeper question. Is the residual signal *aesthetic* in any interesting sense — anything that generalizes beyond the idiosyncrasies of English-language Goodreads readers — or is it a sociology of taste local to the training distribution of LaBSE?

Cross-lingual invariance is the strongest available test. If the geometric features we have identified in English books reproduce in books written in entirely unrelated languages, then what we are measuring is not a text-feature but a content-feature — something that rides above the linguistic surface.

### 17.5.1 Setup

We assembled $n = 4{,}683$ non-English books from Gutenberg across 19 languages and 10 language families. Books were encoded with LaBSE and projected into the *English* PCA-128 basis fit in §17.4. The channels were then recomputed in this shared basis, and each channel's values were correlated across languages on book-title-matched bundles (same book, different languages).

Bundle counts are unevenly distributed: Finnish ($n=288$), French ($n=227$), German ($n=138$), Dutch ($n=88$), Italian ($n=49$), Spanish ($n=38$), Greek ($n=33$), Esperanto ($n=24$), Hungarian ($n=21$), Latin ($n=20$). Six language families are represented: Germanic, Uralic, Romance, Hellenic, Italic-ancient, Constructed. Sinitic is absent — not through methodological choice but because Gutenberg's Chinese corpus consists of classical Chinese originals (Confucius, Sunzi) rather than translations of Western works. This is a corpus-design limit that we report rather than repair.

### 17.5.2 Results

For each aesthetic channel, we computed the Spearman correlation $\rho$ of the channel's value on English versus its value on each non-English language, matched book-by-book. The mean across language pairs:

$$
\bar{\rho}_{\mathrm{pair\_sim}} = 0.712, \quad
\bar{\rho}_{\mathrm{mahal}} = 0.710, \quad
\bar{\rho}_{H} = 0.675, \quad
\bar{\rho}_{\mathrm{Bhatt}} = 0.675, \quad
\bar{\rho}_{\mathrm{JS}} = 0.674.
$$

Individual pairs reach higher values. English–Finnish Hellinger: $\rho = +0.77$ at $n = 288$, $p = 8 \times 10^{-57}$. English–French Hellinger: $\rho = +0.78$ at $n = 227$. These are correlations between two entirely distinct writing systems and language families (Uralic and Romance, against Germanic English), computed on geometric summaries of content clouds.

A complementary variance-ratio analysis confirms the invariance from a different angle. Within-bundle (same book, different language) standard deviation divided by between-book standard deviation ranges from $0.18$ for the path-efficiency feature to $0.39$–$0.44$ for the divergence family. That is: a book's geometric aesthetic fingerprint varies more between books than it does between translations of itself — by a factor of two to five.

We also tested *rating* transfer in the weakest form available: a Ridge model trained on English rating and applied cross-lingually. On the pooled non-English corpus ($n = 940$ books with matched rating data), $R = 0.07$, $p = 0.033$. This is small, but it suggests the rating-relevant direction, not just the feature values, survives projection across languages.

### 17.5.3 What the Result Means

The cross-lingual result is, to our mind, the single strongest piece of evidence for the chapter's thesis. It translates the book-level claim from "text-geometry" to "content-geometry." The geometric features we have identified are not riding on English surface regularities; they survive the substitution of an entirely different writing system and linguistic family. This is the aesthetic analogue of the BIP transfer result reported in Chapter 17: structure transfers; surface does not.

The invariance is not complete. The mean $\bar{\rho} \approx 0.70$ implies that about half the variance in the channel values is cross-lingually preserved, and half is not. Some of the unpreserved variance is translation-specific (different translators make different choices), some is encoder-specific (LaBSE is not perfectly isometric across languages), and some is presumably genuine linguistic surface structure that interacts with the channels. The framework does not claim gauge invariance in the strong sense of Chapter 12; it claims robust cross-lingual correlation of geometric content features.

The Sinitic gap deserves repeating. We cannot report on Mandarin, Japanese, Korean, or Classical Chinese translations because the available public-domain corpus does not contain them at the required scale. This is the most serious limitation of the cross-lingual result, and until it is remedied any claim to full linguistic universality is premature.

## 17.6 Cross-Modality: Music

### 17.6.1 Setup

The second major test extends the framework from text to music. We used FMA-Medium ($n = 24{,}801$ tracks, 30-second clips, artist-disjoint 5-fold CV) and extracted MERT-v1-330M layer-7 embeddings as content vectors. The aesthetic target was $\log(1 + \mathrm{listens})$, which is noisier than Goodreads rating (listens conflate quality with promotion, genre popularity, and platform effects) but provides the only available large-scale reception signal for this corpus.

All four channels from §31.3 were applied without structural modification. One technical note: the Hellinger feature saturated to $\approx 1.0$ in music due to small-sample-in-high-dimensions Gaussian fits (typically 45 audio tokens per clip in a $d = 128$ PCA subspace). We resolved this by computing divergences in a reduced $K = 32$ subspace, and by substituting the Bhattacharyya divergence directly as a robustness check. The substantive findings are unchanged.

### 17.6.2 Results

At the raw level, the music channels outperform the book channels:

- Hand features (Ridge): $R = 0.124$. The corrected version of this measurement after the Hellinger fix is $R = 0.098$, which we report as the honest number.
- Lasso on 128-dimensional PCA spectrum: $R = 0.302$, $z = 49.8\sigma$.
- Combined: $R = 0.301$.

After genre residualization the picture is closer to the book result:

- Hand features: $R = 0.043$.
- Lasso on spectrum: $R = 0.177$, $z = 28.3\sigma$.

Music genre is an even stronger confound than book genre — $91\%$ of the hand-feature $R^2$ is genre, compared to $85\%$ in books. The Lasso-on-spectrum channel survives residualization with the strongest post-control signature we have obtained in any domain of the chapter.

A head-to-head against Spotify's 8 hand-engineered acoustic features, on the shared Echonest-annotated subset ($n = 5{,}233$), is diagnostic: MERT hand features $R = 0.151$, Spotify 8 features $R = 0.103$, MERT Lasso-on-spectrum $R = 0.225$. A bootstrap test of the MERT-vs-Spotify difference gives $p = 0.001$. Learned content embeddings outperform curated acoustic features at predicting listens, by a statistically significant and practically noticeable margin.

Within-genre regressions within the music corpus further sharpen the result. Rock ($n = 7{,}088$) $R = 0.139$; Electronic ($n = 6{,}284$) $R = 0.143$; Hip-Hop ($n = 2{,}190$) $R = 0.141$; Pop ($n = 1{,}173$) $R = 0.185$. Classical ($n = 584$) $R = -0.013$ and Jazz ($n = 384$) $R = 0.031$ are null. We do not know whether the null is a sample-size effect, a genre-convention effect (these genres reward different geometric features), or a signal-to-noise issue with listens as a reception proxy in audiophile genres. This is an open question.

### 17.6.3 The Cross-Modality Sign Flip

The most interesting finding of the chapter, from a philosophical standpoint, is not the size of the effect in either domain but the *inversion of sign* between them on two shared channels.

$$
\begin{array}{lcc}
\text{Channel} & \text{Books} & \text{Music} \\
\hline
\mathrm{pair\_sim\_mean} & \rho = +0.126 \; (8.4\sigma) & \rho = -0.076 \; (p = 5 \times 10^{-33}) \\
\mathrm{step\_mean} & \rho = -0.096 \; (6.4\sigma) & \rho = +0.071 \; (p = 4 \times 10^{-29}) \\
\end{array}
$$

Both flips are robust at $p < 10^{-28}$.

The substantive reading: higher-rated books are the ones whose content cloud is *tighter* in representation space — whose sentences cohere, return to themes, do not jump sharply. Higher-listened music tracks are the ones whose content cloud is *looser* — whose audio windows differ from each other, step farther between adjacent windows, do not return obsessively to a single texture. Books reward continuity and internal coherence; music rewards contrast and dynamic variation.

This is not a trivially derivable consequence of the modalities. Nothing in the mathematics of the channels prescribes a sign; they are symmetric features of the cloud geometry, and either direction could in principle correlate with aesthetic value. The empirical observation that two distinct modalities produce *opposite* signs on the same geometric quantities is the clean finding: the aesthetic manifold has *directionality*, and the directionality is modality-specific.

## 17.7 Philosophical Interpretation

We may now state the philosophical upshot of the chapter in a form compatible with the book's larger project.

**Claim 17.1 (Aesthetic Geometric Content).** *Aesthetic judgment, in the modalities we have tested, carries measurable geometric content in pretrained representation spaces. The content is partly language-invariant (mean cross-lingual $\bar{\rho} \approx 0.70$ on divergence and coherence channels across ten languages from six language families), dominated by genre in hand-crafted features (85–91% of raw variance is genre confound), and recoverable in a residual form by learned high-dimensional regression on the PCA spectrum ($R = 0.093$ in books post-residualization, $R = 0.177$ in music).*

**Claim 17.2 (Modality-Specific Directionality).** *The aesthetic metric is not a single signed quantity that generalizes across modalities. On two channels — internal coherence $\mathrm{pair\_sim\_mean}$ and trajectory step size $\mathrm{step\_mean}$ — the sign of the correlation with reception flips between literary text and music, at $p < 10^{-28}$ in both directions. The "rules" of aesthetic geometry differ between modalities in a principled and inverted way: books reward coherence and continuity, music rewards contrast and variation.*

The second claim is the more novel of the two. It says something that the first claim alone would not force us to accept: aesthetic geometry is not a *single* manifold but at minimum a *bundle* of manifolds indexed by modality, with the same candidate coordinates (spread, coherence, trajectory, spectrum) but modality-specific directions of preferred value. This is weaker than claiming that beauty is universal; it is stronger than claiming it is arbitrary.

The analogy to the moral manifold (Chapter 5) runs as follows. The moral manifold carries a nine-dimensional structure that is cross-culturally invariant at the level of dimensions (Chapter 17 §17.3) but culturally variable at the level of metric weights (Chapter 17 §17.2; Chapter 20 §20.10). The aesthetic manifold, as our evidence has it, shows an analogous structure: cross-modal invariance at the level of the four channels (the same geometric questions are meaningful in both text and music), but modality-specific values and even signs on those channels. One could formalize the aesthetic manifold as a rank-4 tensor with modality as an external index; that formalization is premature pending a third modality, but the structural parallel with Chapter 6's tensor hierarchy is explicit.

The methodological parallel with Chapter 9 (Origin of the Moral Metric) is also explicit. The moral metric, Chapter 9 argued, is neither stipulated nor discovered in the simple senses of those words: it is *discovered-constructed* through an iterative process in which features are proposed, tested, and revised. The aesthetic metric has the same status in our work. We did not derive the four channels from first principles; we proposed them, measured them, discarded some (the raw Hellinger feature failed in music), and report what survives. The aesthetic metric, in the form we have it, is an empirical artifact of a particular pretrained encoder and a particular reception signal. Its status as "the" aesthetic metric is, like the moral metric's, provisional.

The connection to Chapter 15 (Tensor to Decision) completes the picture. Chapter 15 argued that the compression of multidimensional moral content to a scalar decision is a genuine act of loss, not a neutral summary. Aesthetic judgment, in the form of a numeric rating or a play-count, is that same compression applied to a different manifold. Our $R^2 \approx 0.01$–$0.09$ numbers are not disappointingly small; they are what one should expect when one projects a multi-channel geometric object onto a one-dimensional proxy under severe genre confound. The geometric content is not missing; it is partially visible through a narrow channel.

## 17.8 Limits and Honest Caveats

No chapter of this book is complete without a frank accounting of its limits. Geometric aesthetics has several that readers should weight.

**The Sinitic corpus gap.** Our cross-lingual claim is based on ten languages from six families, and Sinitic is absent. The Gutenberg-Chinese corpus consists of classical Chinese originals, not translations, which precludes the matched-book bundle analysis. Until this gap is closed — by extending to translated corpora, or by switching encoders to Chinese-native models — claims to full linguistic universality are premature.

**Genre confound dominance.** In both modalities, hand-engineered features are dominated by genre confound to an extent ($85\%$ in books, $91\%$ in music) that makes "raw" aesthetic results nearly worthless as evidence. Any future work must residualize or be ignored. We suspect that most published empirical aesthetic-ML literature understates this problem.

**Small absolute effect sizes.** Even after residualization, the variance explained is $R^2 \approx 0.01$–$0.09$. This is enough to generate large $z$-scores at our sample sizes, but it is not enough to predict the reception of an individual work with any useful accuracy. Geometric aesthetics, as developed here, is a claim about statistical structure in large samples, not a method for ranking works. This distinction matters: the framework supports the existence of aesthetic geometry as an object of study, not its deployment as a taste algorithm.

**Learned-representation dependence.** The channels are computed on LaBSE (text) and MERT (music) embeddings. Replacing these encoders with alternatives (BERT, mBERT, CLAP, audio-MAE) would produce different values and, in principle, different signs. We have no reason yet to believe the signs we report are encoder-artefactual, but we have no proof that they are not. Replication across encoders is the natural next test.

**Rating and listens as reception proxies.** Goodreads rating is a public, conscious, self-reported quality judgment. Play-count is a behavioral, implicit, platform-mediated signal. They are not the same thing, and neither is "aesthetic quality" in any philosophical sense. They are the reception signals that are publicly available at scale. We report them as what we have, not as what we would wish to have.

**No causal claim.** The chapter reports correlations between geometric features and reception, with controls for the largest available confound (genre). It does not claim that the geometric features *cause* reception, nor that optimizing a work for the favorable direction on a channel would improve its reception. The geometry may be a correlate, not a driver. Distinguishing these cases requires intervention, which is not available in retrospective corpora.

## 17.9 Open Questions

We close with the questions that this chapter has raised and not answered.

**Does the metric extend to a third modality?** Our sign-flip claim is based on two modalities. A third — film, visual art, dance — would sharpen the picture. If the channel signs in a third modality partition cleanly into "continuity-rewarding" and "contrast-rewarding" clusters, the bundle-of-manifolds picture is strengthened. If the signs are idiosyncratic, the picture is weakened.

**Is the sign flip encoder-artefactual?** The most parsimonious alternative to the modality-specific-directionality thesis is that LaBSE and MERT organize their spaces differently in a way that happens to flip signs on our channels. Replicating the book analysis with a music-pretrained encoder, or the music analysis with a text-pretrained encoder (applied to audio transcripts, say), would help adjudicate.

**Can the aesthetic manifold be integrated with the moral manifold?** Chapter 5's moral manifold and the aesthetic manifold sketched here share representational substrate (pretrained content embeddings) and mathematical form (spread, coherence, trajectory, spectrum). Whether they are two faces of a single manifold, two parallel manifolds on the same base space, or genuinely distinct structures is an open theoretical question. The claim in Chapter 4 §4.9 that meaning has geometric structure in a unified sense would predict eventual unification; the modality-specific-directionality finding suggests that unification is non-trivial.

**What does the trajectory channel correspond to?** The trajectory channel (step size, recurrence, curvature, autocorrelation) is small but non-zero in both modalities. We have not given it a semantic interpretation beyond "pacing" and "return-to-theme." A satisfying account would connect the trajectory channel to narrative arc in literature and to formal structure (verse-chorus, development-recapitulation) in music, and would do so at a level of mathematical specificity that permits falsification. This is, in our view, the single most promising direction for future work.

**Does the Fiction-null for Non-fiction reflect genre convention or sample issue?** The within-genre fiction result ($R = 0.131$, $6.2\sigma$) contrasts with null results in Non-fiction and History/Biography. Whether this is a genre-convention effect (these readerships reward different features) or a sample-size effect (these sub-corpora are smaller and noisier) is testable with expanded data.

## 17.10 Connection to the Framework

We situate geometric aesthetics in the architecture of the book:

- **Chapter 4 (Mathematical Preliminaries).** The PCA spectrum, the Gaussian divergence family, the Mahalanobis metric, and the Riemannian trajectory summaries are all imported directly from Chapter 4. The aesthetic chapter adds no new mathematical machinery; it is an application of the standing toolkit.
- **Chapter 5 (The Moral Manifold).** The aesthetic manifold is proposed in structural parallel to the moral manifold: a quotient space on which the rating-relevant features of content tensors live. The two manifolds share a representational substrate (pretrained content embeddings) and share a mathematical form (spread, coherence, trajectory, spectrum), but differ in their external coordinate (modality for aesthetics; context for ethics).
- **Chapter 6 (The Tensor Hierarchy).** Aesthetic features live at ranks 1 (content embeddings) through 3+ (trajectory summaries), parallel to the moral tensor hierarchy. The Lasso-on-spectrum channel is a rank-2 feature (covariance eigenvalues); the trajectory channel is rank-3.
- **Chapter 9 (Origin of the Moral Metric).** The aesthetic metric is discovered-constructed, not stipulated, by the same iterative process described in Chapter 9. Its provisional status is explicit; its candidate-ness is the point.
- **Chapter 15 (From Tensor to Decision).** Rating and listens are scalar contractions of a multi-channel geometric tensor. The small $R^2$ values are the expected consequence of contraction loss, not evidence against geometric content.
- **Chapter 17 (Empirical Evidence).** Our cross-lingual invariance result is structurally parallel to Chapter 17's BIP transfer result: structure transfers across languages; surface does not. Geometric aesthetics supplements the empirical pillar on which the book rests.
- **Chapter 20 (Geometric Economics), Chapter 24 (Geometric Theology), Chapter 26 (Geometric AI Ethics).** Sibling application chapters. Like economics, aesthetics reveals that a scalar reception signal (rating, listens; analogously, price) is a low-rank projection of multi-dimensional geometric content. Like theology, aesthetics engages a domain historically taken to resist formalization, and finds that the resistance weakens under careful measurement. Like AI ethics, aesthetics depends on pretrained representations whose provenance and biases are load-bearing and must be acknowledged.

## 17.11 Summary

This chapter has proposed that aesthetic judgment, in the modalities of literary text and music, carries measurable geometric content in pretrained content-embedding spaces; characterized that content through four channels (spectral divergence, internal coherence, trajectory geometry, learned-direction projection); and reported empirical findings that substantiate the proposal while constraining its scope.

The results: on $n = 4{,}998$ Gutenberg-Goodreads books under author-disjoint cross-validation, discovery $R = 0.241$ ($17\sigma$); after genre residualization, $R = 0.093$ ($6.5\sigma$), with $85\%$ of raw variance attributable to genre confound. On $n = 4{,}683$ non-English books across 19 languages and 10 families projected into a shared English PCA basis, mean cross-lingual Spearman $\bar{\rho} \approx 0.70$ on divergence and coherence channels. On $n = 24{,}801$ FMA tracks with MERT embeddings, Lasso-on-spectrum $R = 0.302$ raw, $R = 0.177$ genre-residualized ($28.3\sigma$); MERT outperforms Spotify's 8 acoustic features head-to-head at $p = 0.001$. On two channels shared between modalities, the sign of the reception correlation inverts at $p < 10^{-28}$: books reward coherence and continuity, music rewards contrast and dynamic variation.

The philosophical take: aesthetic judgment is neither subjective residue nor cleanly universal. It carries geometric content that is partly language-invariant and modality-aware, that is genre-confounded in hand-crafted features and so requires learned high-dimensional representation to isolate, and that has modality-specific directionality such that the "rules" of aesthetic geometry differ between text and music in principled, inverted ways. The aesthetic manifold, like the moral manifold, is discovered-constructed, small-in-absolute-terms, statistically robust, and — most importantly — an object of study rather than an algorithm for taste.

The next chapter turns to the remaining horizons of the program.

---

*Ethics is not a number. Neither, now, is beauty.*
