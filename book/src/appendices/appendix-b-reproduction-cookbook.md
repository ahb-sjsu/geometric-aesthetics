# Appendix B: Reproduction Cookbook

This appendix describes how to reproduce the four phases of empirical results reported in Chapter 17 (Phase 1 Books Discovery, Phase 2 Within-Genre Control, Phase 3 Cross-Lingual Invariance, Phase 4 Music) from raw public data to final effect sizes. The recipe is written for a reader with working Python and GPU experience but no prior familiarity with our code. The entire pipeline runs end-to-end on a single 32 GB GPU in approximately two hours.

We give hardware, software versions, exact data sources, the four-channel feature extraction sketch, cross-validation protocol, residualization procedure, known pitfalls, and compute budget. Paths marked with `/labshare/...` are our internal lab-server paths and should be remapped to the reader's environment. Everything else is public.

## B.1 Hardware and Software

**Hardware.** A single NVIDIA GPU with at least 32 GB memory is sufficient. We developed on an RTX A6000 (48 GB) and an A100 (40 GB). MERT inference on 24,801 tracks takes approximately 40 minutes at batch size 16 on the A6000; LaBSE inference on ~900k paragraphs takes approximately 25 minutes at batch size 64. No distributed setup is required. CPU memory of 64 GB is comfortable; 32 GB works if you stream rather than materialize the full paragraph pool in RAM.

**Software versions.** We pin to the versions used in the reported experiments. Newer versions probably work; older may not.

```
python==3.11.7
torch==2.3.1+cu121
transformers==4.42.3
sentence-transformers==3.0.1
numpy==1.26.4
scipy==1.13.1
scikit-learn==1.5.0
pandas==2.2.2
datasets==2.19.1
librosa==0.10.2
soundfile==0.12.1
tqdm==4.66.4
```

Install with:

```bash
conda create -n geomaesth python=3.11
conda activate geomaesth
pip install torch==2.3.1 --index-url https://download.pytorch.org/whl/cu121
pip install transformers==4.42.3 sentence-transformers==3.0.1 \
    numpy==1.26.4 scipy==1.13.1 scikit-learn==1.5.0 pandas==2.2.2 \
    datasets==2.19.1 librosa==0.10.2 soundfile==0.12.1 tqdm==4.66.4
```

## B.2 Data Acquisition

### B.2.1 English Books: Project Gutenberg + Goodreads

**Gutenberg texts.** We download texts directly from the Gutenberg cache:

```
https://www.gutenberg.org/cache/epub/{id}/pg{id}.txt
```

Where `{id}` is the numeric Gutenberg text identifier. Be polite: throttle to ~1 request/second and cache locally; Gutenberg asks for this and will rate-limit aggressive scraping. We use a fixed-seed shuffle of the Gutenberg catalog and pull until we have matched 5,000 candidates against Goodreads.

**Goodreads labels.** Goodreads does not ship a rating dump anymore. We use the Kaggle *goodreads-books* dataset (search on Kaggle; the relevant file is `goodreads_book_genres_initial.json` together with the `books.csv` rating file). The join between Gutenberg and Goodreads is not clean — Gutenberg gives author + title strings, Goodreads gives author + title + ISBN + editions. Our matcher:

1. Normalizes author names to surname (unicode-normalize, strip diacritics, lowercase, split on comma or space, take last non-initial token).
2. Normalizes titles (lowercase, strip `a`/`an`/`the` leading article, strip punctuation).
3. Joins on (surname, normalized-title-prefix) and picks the Goodreads edition with highest `ratings_count`.
4. Rejects matches where `abs(log10(ratings_count)) < 1.0` (too-obscure editions produce noisy mean ratings).

After this we have $n=4{,}998$ English books with (Gutenberg text, Goodreads average rating, ratings count, author).

### B.2.2 Non-English Books: LAION / Project-Gutenberg on Hugging Face

For the Phase 3 cross-lingual experiment we use the `laion/Project-Gutenberg` Hugging Face dataset, which bundles Gutenberg EPUBs with language metadata. This saves us from scraping 19 languages manually.

```python
from datasets import load_dataset
ds = load_dataset("laion/Project-Gutenberg", split="train")
# Filter by language code; process same way as English.
```

Language tags follow ISO 639-1. We retain bundles with at least 20 books (the statistical-power threshold): FI 288, FR 227, DE 138, NL 88, IT 49, ES 38, EL 33, EO 24, HU 21, LA 20. Below-threshold languages (PT, JA, PL, SV, RU, CS, ZH) are retained for exploratory analysis but not for the headline invariance claims.

### B.2.3 Music: FMA Medium + MERT

The Free Music Archive Medium split has 25,000 tracks with genre labels and track-level listen counts. The original Switch CDN download is painfully slow (we clocked it at <500 kB/s on good days; 22 GB takes half a day). We use a Hugging Face mirror:

```python
from datasets import load_dataset
fma = load_dataset("benjamin-paine/free-music-archive-medium", split="train")
```

This pulls at multi-MB/s on a good connection and has the tracks pre-decoded. Metadata (the `tracks.csv` file with `track_listens` and `genre_top`) we still pull from the Switch FMA metadata dump; the Hugging Face mirror may not include the full track-level metadata file. If the Switch link is down, community mirrors are indexed from the original FMA GitHub.

We end with $n=24{,}801$ tracks after dropping tracks with missing audio or missing `track_listens`. Target variable is $\log(1 + \text{track\_listens})$.

## B.3 Encoding

### B.3.1 Text: LaBSE

```python
from sentence_transformers import SentenceTransformer
labse = SentenceTransformer("sentence-transformers/LaBSE", device="cuda")
# Output: 768-dimensional L2-normalized sentence embeddings.
emb = labse.encode(paragraphs, batch_size=64,
                   convert_to_numpy=True,
                   normalize_embeddings=True)
```

LaBSE outputs 768-dim embeddings that are L2-normalized. The `normalize_embeddings=True` flag is important: without it the downstream PCA picks up per-paragraph norm variation that is not semantically meaningful.

### B.3.2 Audio: MERT

```python
from transformers import AutoModel, AutoFeatureExtractor
import torch, torchaudio

model = AutoModel.from_pretrained("m-a-p/MERT-v1-330M",
                                  trust_remote_code=True).cuda().eval()
fe = AutoFeatureExtractor.from_pretrained("m-a-p/MERT-v1-330M",
                                          trust_remote_code=True)

def encode_clip(wave_24k_mono_30s: torch.Tensor):
    inputs = fe(wave_24k_mono_30s, sampling_rate=24000,
                return_tensors="pt").to("cuda")
    with torch.no_grad():
        out = model(**inputs, output_hidden_states=True)
    # Layer-7 hidden state, shape (1, T=45, 1024)
    h7 = out.hidden_states[7].squeeze(0).cpu().numpy()
    return h7  # 45 x 1024
```

MERT expects 24 kHz mono audio. Resample and downmix before passing in. The 30-second clip yields $T=45$ token-level hidden states at the layer-7 embedding dimension $D=1024$.

## B.4 Preprocessing

### B.4.1 Books: Header/Footer Strip, Paragraph Split

Gutenberg texts have a boilerplate preamble ending with the `*** START OF THIS PROJECT GUTENBERG EBOOK ...` line and a similar tail marker. Strip between those markers. Paragraph-split on two-or-more consecutive newlines; drop paragraphs under 20 words or over 500 words. This gives us on the order of 200–400 paragraphs per book and a pooled corpus of approximately 900,000 English paragraphs across 4,998 books.

### B.4.2 Music: Clip Selection

FMA tracks vary in length. We take a single 30-second clip starting at 30 seconds in (avoiding intros/fade-outs). Where the track is under 60 seconds we take from the start. Downmix stereo to mono. Resample to 24 kHz using `torchaudio.transforms.Resample` (polyphase).

## B.5 PCA Basis

The critical move for cross-modality and cross-lingual consistency is fitting a PCA basis *once*, on the English paragraph pool, and then using the same axes everywhere downstream.

```python
from sklearn.decomposition import PCA
# english_para_emb: (N_para ~ 900k, 768)
pca = PCA(n_components=128, random_state=0)
pca.fit(english_para_emb)
# Save pca.components_ (128 x 768) and pca.mean_ (768,) for all downstream use.
```

Top-128 PCs capture enough of the variance for stable downstream features without over-parameterizing the Gaussian fits (see pitfall B.8.1). Do **not** refit the PCA on non-English corpora or on the music side. The invariance result requires a shared basis.

For music, we fit a separate 128-d PCA on MERT layer-7 states pooled across all FMA Medium tracks (roughly $24801 \times 45 \approx 1.1\text{M}$ token-level vectors). The two PCA bases (text and audio) are unrelated — we do not and cannot force them to share axes — but within each modality the basis is fit once and used everywhere.

## B.6 Feature Extraction: Four Channels

Given a work represented as a sequence of projected vectors $\{x_t\}_{t=1}^T \subset \mathbb{R}^{128}$, we extract four channels of features.

```python
import numpy as np
from scipy.spatial.distance import pdist
from scipy.stats import skew

def extract_features(X, ref_mean, ref_cov, ref_cov_inv, ref_logdet):
    # X: (T, 128). ref_*: English-corpus reference Gaussian.
    T, D = X.shape

    # --- Channel A: spectral divergences vs reference ---
    m = X.mean(axis=0)
    C = np.cov(X.T) + 1e-4 * np.eye(D)
    # Mahalanobis between means
    mahal_mean = np.sqrt((m - ref_mean) @ ref_cov_inv @ (m - ref_mean))
    # KL(work || ref) for Gaussians
    sign, logdet = np.linalg.slogdet(C)
    kl = 0.5 * (np.trace(ref_cov_inv @ C)
                + (ref_mean - m) @ ref_cov_inv @ (ref_mean - m)
                - D + ref_logdet - logdet)
    # Bhattacharyya, Hellinger (symmetric)
    C_avg = 0.5 * (C + ref_cov)
    _, logdet_avg = np.linalg.slogdet(C_avg)
    bhatt = 0.125 * (m - ref_mean) @ np.linalg.solve(C_avg, (m - ref_mean)) \
          + 0.5 * (logdet_avg - 0.5 * (logdet + ref_logdet))
    hellinger = np.sqrt(1.0 - np.exp(-bhatt))
    js = 0.5 * (kl + _reverse_kl(X, ref_mean, ref_cov))  # symmetrized
    tv = 0.5 * np.linalg.norm(m - ref_mean, ord=1)  # crude TV proxy

    # --- Channel B: internal coherence ---
    # Average pairwise cosine similarity between paragraphs within the work
    Xn = X / (np.linalg.norm(X, axis=1, keepdims=True) + 1e-12)
    sim = Xn @ Xn.T
    iu = np.triu_indices(T, k=1)
    pair_sim_mean = sim[iu].mean()
    pair_sim_std  = sim[iu].std()

    # --- Channel C: trajectory geometry ---
    steps = np.linalg.norm(np.diff(X, axis=0), axis=1)  # (T-1,)
    step_mean = steps.mean()
    step_std  = steps.std()
    step_skew = skew(steps)
    # Autocorrelation of step magnitude, lags 1..3 summed
    acf1_top3 = sum(_acf(steps, lag) for lag in (1, 2, 3))
    # Recurrence rate: fraction of pairs with similarity > threshold
    recur_rate = (sim[iu] > 0.9).mean()
    # Path efficiency: displacement / total path length
    path_eff = np.linalg.norm(X[-1] - X[0]) / (steps.sum() + 1e-12)
    # Rough curvature proxy: mean angle between successive step vectors
    d = np.diff(X, axis=0)
    dn = d / (np.linalg.norm(d, axis=1, keepdims=True) + 1e-12)
    cos_angles = (dn[:-1] * dn[1:]).sum(axis=1)
    curvature = np.mean(1.0 - cos_angles)
    # Power-law slope on sorted step magnitudes (tail index proxy)
    sorted_steps = np.sort(steps)[::-1]
    ranks = np.arange(1, len(sorted_steps) + 1)
    powerlaw_slope = np.polyfit(np.log(ranks), np.log(sorted_steps + 1e-12), 1)[0]
    # Fraction of path length in top-100 largest steps
    tail_mass_100 = sorted_steps[:100].sum() / (steps.sum() + 1e-12)

    # --- Channel D: raw 128-d mean for downstream Lasso ---
    # This channel provides the vector fed to Lasso-on-PCA-spectrum.
    pca_spectrum = m  # shape (128,)

    return dict(
        mahal_mean=mahal_mean, kl=kl, bhatt=bhatt, hellinger=hellinger,
        js=js, tv=tv,
        pair_sim_mean=pair_sim_mean, pair_sim_std=pair_sim_std,
        step_mean=step_mean, step_std=step_std, step_skew=step_skew,
        acf1_top3=acf1_top3, recur_rate=recur_rate, path_eff=path_eff,
        curvature=curvature, powerlaw_slope=powerlaw_slope,
        tail_mass_100=tail_mass_100,
        pca_spectrum=pca_spectrum,
    )
```

Channels A, B, C yield scalar features; Channel D is the 128-dimensional PCA-spectrum vector fed separately to a Lasso regressor.

## B.7 Cross-Validation and Residualization

### B.7.1 Group-Disjoint Folds

We use `sklearn.model_selection.GroupKFold` with 5 folds. The group identifier is the *author* for books and the *artist* for music. This prevents trivial leakage — a Ridge model that learns "Jane Austen's Goodreads rating is 4.2" would score well on non-grouped splits and tell us nothing about aesthetic signal.

```python
from sklearn.model_selection import GroupKFold
from sklearn.linear_model import RidgeCV, LassoCV

gkf = GroupKFold(n_splits=5)
preds = np.zeros(len(y))
for tr, te in gkf.split(X, y, groups=author):
    model = RidgeCV(alphas=[0.1, 1.0, 10.0, 100.0]).fit(X[tr], y[tr])
    preds[te] = model.predict(X[te])
r = np.corrcoef(preds, y)[0, 1]
```

### B.7.2 Genre Residualization (Phase 2 / Phase 4 Within-Genre)

To get the genre-confound-honest effect size, subtract the per-genre target mean before fitting the model on the target:

```python
def residualize(y, genre):
    y_res = y.copy()
    for g in np.unique(genre):
        mask = (genre == g)
        y_res[mask] = y[mask] - y[mask].mean()
    return y_res

y_res = residualize(y, genre)
# Re-run Ridge CV on y_res instead of y.
```

For the strictest within-genre analysis (the 6.2σ fiction result, the music within-genre per-genre numbers) we restrict to a single genre and fit independently. This removes all between-genre variance by construction.

The delta between the raw and residualized $R^2$ is the genre confound. In our data it is 85% for books and 91% for music hand features.

## B.8 Known Pitfalls

### B.8.1 Hellinger Saturation in High-Dimensional Small-Sample

With $T=45$ token-level vectors in $D=128$ dimensions, the empirical covariance $C$ is rank-deficient. Closed-form Gaussian Hellinger becomes numerically unstable: the $\log\det$ terms diverge and the feature saturates at 1.0. We observed this first in the music data (every track scored Hellinger $\approx 1.0$) and the feature became useless.

Two fixes. First, reduce to a $K=32$ PCA subspace before computing Hellinger on music. The geometric verdict — sign of correlation with `log(track_listens)` — is unchanged between $K=32$ and $K=128$ for the divergence family, so the reduction does not distort the empirical claim. Second, use Bhattacharyya directly instead of Hellinger. Bhattacharyya $B = 0.125 (\mu_1-\mu_2)^\top C_{\text{avg}}^{-1}(\mu_1-\mu_2) + 0.5 \log(|C_{\text{avg}}|/\sqrt{|C_1||C_2|})$ does not exponentiate away into saturation. Our book data at $T\gtrsim 200$ is not as badly affected, but we report both and prefer Bhattacharyya in practice.

### B.8.2 Author/Artist Leakage

We reiterate: use group-disjoint folds. A standard 5-fold on books without author grouping will inflate the headline $R$ by a factor of 2–3 because the model learns per-author intercepts. This is the single biggest reproducibility trap.

### B.8.3 Genre Confound

Reporting $R$ without genre residualization is not wrong if clearly labeled as "includes genre signal", but it is misleading if presented as aesthetic predictive power. Our headline decomposition — raw $R=0.241$ vs residualized $R=0.093$ — shows that 85% of the variance explained is genre. Always report the residualized number alongside the raw number.

### B.8.4 Cross-Lingual Basis Must Be Shared

For Phase 3 to mean anything, do not refit PCA per language. The PCA basis must be fit once on English and applied to all non-English corpora. If you refit per language you will get high within-language effects that do not transfer across languages, which is the trivial outcome and tells you nothing about symmetry. The shared-basis design is what makes the invariance claim non-trivial.

### B.8.5 MERT Layer Choice

MERT exposes all transformer layers; different layers specialize in different musical attributes. Layer 7 is our choice because it gave the best downstream performance in our grid search and matches what the MERT authors report as the best layer for music tagging. Earlier layers (1–3) are closer to acoustic features; later layers (10–12) are closer to high-level musical semantics. If you try a different layer, re-fit your music PCA on that layer's states.

## B.9 Statistical Reporting

For every headline number we report: sample size $n$, effect size (Pearson $R$ or Spearman $\rho$), and either a z-score or a p-value. Converting between: a Pearson $R$ at sample size $n$ has z-score roughly $R\sqrt{n-2}/\sqrt{1-R^2}$, and the bootstrap CI we use in the manuscript is 1000 resamples of books (or tracks, or language bundles) with replacement.

For the cross-modality sign-flip test we compute Spearman $\rho$ on each modality separately and test the null $H_0: \rho_{\text{books}} \cdot \rho_{\text{music}} \ge 0$ by stratified bootstrap. This null is rejected at $p<10^{-28}$ for `pair_sim_mean` and $p<10^{-28}$ for `step_mean` (the p-values dominate by the music side's larger sample).

## B.10 End-to-End Compute Budget

On a single 32 GB GPU (A100-40G or A6000-48G both tested):

| Stage | Wall-clock |
|---|---|
| Gutenberg download + EPUB decode (4,998 books, throttled) | 90 min (I/O bound) |
| LaBSE paragraph encoding (~900k paragraphs) | 25 min |
| Non-English book acquisition (HF `laion/Project-Gutenberg`) | 30 min (I/O) |
| Non-English LaBSE encoding | 40 min |
| English PCA-128 fit | 2 min |
| Book feature extraction (all four channels, 4,998 × 19 langs ≈ 9,681 books) | 15 min |
| FMA Medium download from HF mirror | 30 min (I/O) |
| MERT inference (24,801 tracks × 30s clips) | 40 min |
| Music PCA + feature extraction | 15 min |
| Ridge/Lasso fits (GroupKFold × 4 channels × 4 phases) | 10 min |
| Residualization + within-genre fits | 5 min |
| Bootstrap CIs (1000 resamples across all headlines) | 20 min |

Total: approximately 2 hours of GPU time plus 2.5 hours of network I/O (the bulk of which is the Gutenberg polite-throttle and the HF dataset pulls). If the data is already on disk, the compute side runs in under 2 hours end-to-end. This is a tractable single-workstation experiment; no cluster is required.

## B.11 Reproducibility Artifacts

We release:

- `configs/phase1_books_en.yaml` — data paths, PCA dim, CV config for English books.
- `configs/phase2_within_genre.yaml` — genre residualization and intra-genre splits.
- `configs/phase3_cross_lingual.yaml` — list of language codes, bundle thresholds, shared-PCA-basis pointer.
- `configs/phase4_music.yaml` — MERT model id, layer, audio preprocessing, artist groups.
- `scripts/fetch_gutenberg.py`, `scripts/fetch_fma_hf.py`, `scripts/fetch_laion_pg.py`
- `scripts/encode_labse.py`, `scripts/encode_mert.py`
- `scripts/extract_features.py` (the four channels above)
- `scripts/fit_ridge_lasso.py` (cross-validation + residualization)
- `scripts/bootstrap_sign_flip.py` (cross-modality test)

Random seeds are fixed: PCA random_state=0, GroupKFold shuffle=False (deterministic grouping), RidgeCV α-grid is fixed, LassoCV uses 5-fold internal CV with random_state=0. Bootstraps use `numpy.random.Generator(PCG64(seed=17))`. With the same input data and these seeds, our reported headline numbers reproduce to the fourth decimal.

We also release the pre-computed PCA basis (`labse_pca128_english.npz` and `mert_l7_pca128_fma.npz`), the feature matrices, and the author/artist group keys. A reader who does not want to re-run the encoders can skip from Section B.6 onward using our cached features.

## B.12 Paths on Our Lab Server

For internal reference, the experiment tree on our lab server lives under `/labshare/geomaesth/` with subdirectories `raw/gutenberg/`, `raw/fma_medium/`, `raw/laion_pg/`, `cache/labse/`, `cache/mert/`, `features/`, `models/`, `results/`, and `paper/`. The scripts pick up these paths from environment variables (`GEOMAESTH_RAW`, `GEOMAESTH_CACHE`, `GEOMAESTH_RESULTS`); override them to point at the reader's own storage. Nothing in the public release depends on our lab paths.

## B.13 When Things Break

The most common failure modes we have observed during internal re-runs:

- **Out-of-memory during LaBSE encoding.** Drop batch size to 32 or 16. LaBSE at batch 64 uses about 14 GB; at batch 16 it uses about 6 GB.
- **MERT `trust_remote_code` prompt.** The model ships a custom model class. Accept the prompt or set `trust_remote_code=True` explicitly.
- **FMA track decoding errors.** A small fraction of tracks have corrupted mp3 frames. Skip them and note the final $n$. We end at $n=24{,}801$ after skipping approximately 200 broken files.
- **Goodreads match ambiguity.** Two different books with the same surname-title prefix (e.g., multiple authors named "Stevenson" with titles starting "The"). Our matcher picks the highest-rating-count edition and logs the alternative; for headline results we additionally hand-audited the top-100 and bottom-100 rated matches.
- **Genre labels missing.** Goodreads' `genre_top` is occasionally empty. We drop these rows for residualized analyses; they are retained for raw-R analyses.
- **Sinitic corpus near-empty.** Chinese Gutenberg is classical Chinese (*Analects*, *Art of War*, *Shijing*), not Chinese translations of Western works. Five bundles formed. This is a corpus-design artifact, not a bug. Document and move on.

With these caveats noted, the pipeline is deterministic and the reported headline numbers are reproducible end-to-end. If a reader's reproduction diverges from our numbers by more than one decimal, we would like to know; file an issue against the release and include the config hash and the first-divergent stage output.
