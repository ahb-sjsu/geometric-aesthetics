# Corrections to Geometric Aesthetics, 2026-11-26

These corrections were made on 2026-11-26 at the author's direction after a review of the series.

The repository holds no data files or experiment code. The record of the measured results is
`book/src/_BOOK_REFERENCE.md` ("Verified Empirical Findings"), with Chapter 17 and the code sketch
in Appendix B. "The reference" below means that file. All chapter files are under `book/src/`.

## Reconciled

1. **The 91% genre-confound figure for music is a hand-feature figure.** The reference, Chapter 17
   §17.6.2 and Chapter 21 §21.3 say that 91% of the *hand-feature* R² is genre. For the spectrum
   Lasso the printed values (R = 0.302 raw, 0.177 residualized) give 1 − (0.177/0.302)² = 66%.
   Several passages attached the 91% to the music signal in general or to the Lasso result.
   - Chapter 1 ("Three Failures of Flatland"): said "Ninety-one percent of the raw signal is genre confound"
     directly after the Lasso figures. Now says ninety-one percent of the raw hand-feature signal,
     and over sixty percent of the spectrum-Lasso signal (the wording Chapter 8 already uses).
   - Appendix F, row F21.2: said "91% of F21.1's R²". F21.1 is the spectrum Lasso. Now says 91% of
     the hand-feature R² (about 66% of F21.1's spectrum-Lasso R²).
   - "hand-feature" added where the text said only "music": Chapter 3 ("Our Contribution in Context"), Chapter 9
     §9.1 and §9.4, Chapter 14 §14.9, Chapter 18 §18.2, Chapter 23 Prediction 23.2, Chapter 25
     §25.5, Chapter 26 §26.6, Appendix D §D.2.
2. **Lasso axis count.** Chapter 6 §6.5 said the Lasso regressed against the mean projections and
   the spectral variances and that "71 of the 256 axes" were selected. The reference, Chapter 17
   §17.3.4, Appendix F (F14.2) and the Appendix B code (`pca_spectrum`, shape 128) all give a
   128-dimensional input. Chapter 6 now regresses against the 128 mean projections, which is what
   its own Level-4 tensor and the Appendix B code use, and says "71 of the 128 axes". The
   definition of the spectral variance is left in place. See Unresolved 3.
3. **Language counts.** The reference gives a corpus of 19 languages in 10 families, matched
   bundles at the threshold in ten languages, and six families with statistical power.
   - Chapter 29 opening: "across ten language families" is now "across six language families".
   - Chapter 14 §14.2: "survive translation into 19 languages" is now "ten languages from six
     families".
   - Chapter 16 §16.10: "19 languages, 6 families" is now "ten languages, 6 families".
   - Chapter 18 §18.5: after listing the ten languages, "19 languages, 6 language families" is now
     "a corpus of 19 languages, with 6 language families at statistical power".
   - Chapter 23 §23.3: "across 19 languages and 10 families" is now "across ten languages from six
     families".
4. **Number of works tested.** Chapter 16 §16.1 said the account "has been tested against
   hundreds of thousands of works". The printed sample sizes are 4,998 + 4,683 + 24,801 = 34,482.
   Now "tens of thousands of works".
5. **Chapter 17, text carried over from Geometric Ethics.** Chapter 17 began as a chapter of
   *Geometric Ethics* (the reference records its old file name, `chapter-31-geometric-aesthetics.md`)
   and still pointed at that volume's chapters as if they were this one's.
   - §17.1: "The preceding thirty chapters have developed a geometric framework for ethics ... ten
     domains of application — economics (Chapter 20), ..." now names the sibling volume, says nine
     domains (the list has nine, Chapters 20–28 of *Geometric Ethics*), and gives the chapter range
     as that volume's.
   - §17.1, §17.2, §17.5.3, §17.7, §17.9 and §17.10: references to the moral manifold (Chapter 5),
     Chapters 5, 10, 11, the BIP transfer result (Chapter 17), Origin of the Moral Metric
     (Chapter 9), Tensor to Decision (Chapter 15), Chapter 4 §4.9, and the application chapters 20,
     24 and 26 are now attributed to *Geometric Ethics*. References that are right for this volume
     (Chapters 4, 6, 9, 10, 12) are unchanged.
   - §17.6.1: "§31.3" is now "§17.3".
   - §17.11: "The next chapter turns to the remaining horizons of the program" is now "The next
     chapter turns to artificial agents" (Chapter 18).
6. **Claim 17.1.** It gave R = 0.093 for books as a result of "learned high-dimensional regression
   on the PCA spectrum". §17.4.2, the reference and Appendix F (F9.3) give 0.093 for the combined
   Ridge and Lasso model after genre residualization. The claim now says so, and keeps R = 0.177
   for the spectrum regression in music.
7. **Wrong section references to Chapter 17.** Checked against the chapter's headings.
   - Chapter 4 §4.4: "(Chapter 12, §17.7 in the Aesthetics Ch. 17 which is the already-drafted
     empirical chapter)", a drafting note, is now "(Chapter 12; Chapter 17, §17.5)".
   - Chapter 16 §16.6, twice: the music results were cited as §17.4. Now §17.6.
   - Chapter 19 Task E4: the within-stratum evaluation was cited as §17.2. Now §17.4.
   - Chapter 23 §23.1: the trajectory features were cited as §17.4. Now §17.3.
   - Chapter 25 §25.5: books cited as §17.3 and music as §17.5. Now §17.4 and §17.6.
8. **"Our nine working axes."** Chapter 14 §14.4 counted 9 × 9 × 9 = 729 components "using our
   nine working axes". Chapter 5 §5.5 says the aesthetic manifold does not start from nine known
   dimensions. The count is now given as d³ on d axes per reader, with the 128-dimensional case
   kept.

## Marked as illustrative or simulated

1. **Chapter 7, per-work values for *Bleak House*.** The chapter quoted values for one novel
   (distance from prior 1.4σ, `pair_sim_mean = 0.412`, loadings on axes "A-17" and "A-42") as "our
   data". They are not among the reference's verified findings, and Appendix D describes its own
   values for the same novel as representative, not measurements. The chapter introduction now
   says the per-work values are representative in the sense of Appendix D. The running example
   says "an illustrative five-level tensor decomposition", the 1.4σ is called an illustrative
   value, and "in our data" at Level 4 is now "in this illustrative walk-through".
2. **Chapter 14, emergence.** Appendix F lists canon formation by geometric aggregation as
   conjectured (F14.1) and counts about 30 of the 71 Lasso axes as interpretable (F14.2).
   - §14.4: "The empirical witness for E ≠ 0" is now "The empirical motivation".
   - §14.4: the axes "are individually interpretable" now reads that about 30 of them are, on
     post-hoc inspection (F14.2).
   - §14.4: "They are E, made visible" is now "They are, we conjecture, E made visible".
   - §14.6: "Our 71 Lasso axes pass it" is now "are consistent with it but do not establish it",
     with the reference to F14.1.
3. **Chapter 12 and Chapter 13, the Noether reading.** Appendix F marks it as analogy (F12.3).
   - §12.1: "Noether's theorem then identifies the conserved current" now begins "By analogy with
     Noether's theorem (Appendix F, F12.3), we then identify".
   - §12.4: "is the Noether current" is now "is, in this analogy, the Noether current", and "this
     vector is a Noether current" is now "plays the role of a Noether current".
   - §12.10: "The conservation law tells her" is now "The invariance result tells her".
   - Chapter 13 §13.1: "the conservation law is not a fantasy" is now "the invariance is not a
     fantasy".
4. **Chapter 12 §12.5, sign flips under residualization.** The text said the flips "are not
   artifacts of sample size, model choice, or residualization" and that genre residualization
   preserves both. Neither Chapter 17 nor the reference reports the flips on residualized targets,
   and §17.9 and Appendix E.4 leave an encoder-level origin open. The passage now says the flips
   are not artifacts of sample size, persist after the Hellinger fix, are not reported on
   residualized targets, and that an encoder-level origin has not been ruled out.
5. **Appendix E.8.** "A framework ... that has passed four tests" referred to the volume's own
   first measurements. The criteria in the same section call for replications that have not been
   run. The sentence now says the first measurements came out in the stated direction and that the
   replications have not yet been run.

## Withdrawn or updated

1. **Conservation of Harm (Chapter 12 §12.8).** *Geometric Ethics* withdrew "Conservation of Harm"
   as a conservation law on 2026-06-19 (its ledger entry GE-HARM-CONSERVATION) and kept invariance
   of harm accounting. A dated note now heads §12.8. "Chapter 12's Noether theorem identifies harm
   as the conserved quantity" is now "Chapter 12's Noether argument identifies harm accounting as
   the invariant", and "Ethics admits a conserved scalar (harm)" is now "an invariant scalar
   account (harm)". The section heading is unchanged.
2. **The Hohfeldian D4 group.** *Geometric Ethics* v1.25 (2026-11-08) withdrew D4 and put the Klein
   four-group V4 in its place. This volume has no theorem that uses D4. Two passing references are
   updated: Chapter 8 §8.8 and Appendix A (the closing differentiation from *Geometric Ethics*).
   Both now name V4 and the withdrawal.

No statement in this volume depends on a quarter-turn or on a group of order 8, so nothing is
marked "withdrawn pending restatement".

## Unresolved

1. **The failed compressibility formula.** The README status block of 2026-07-14 says the original
   compressibility formula failed and is reported as failed, and that the structural-channels
   finding was pre-registered. No chapter or appendix introduces a compressibility formula or
   mentions a pre-registration, so there is no place in the book where the formula is introduced.
   The formula is in `paper/v3.tex` (beauty as diversity times compressibility), which reports all
   five of its pre-registered predictions as confirmed. No record of the failed test exists in the
   repository. Nothing was changed. Needed from the author: the record of the failed test, and
   where the book should report it. `OUTLINE.md` also still describes Chapter 17 as the paper's
   study (50,000+ Goodreads reviews, nine traditions), which is not what Chapter 17 contains.
2. **The raw hand-feature R for music.** (Partly repaired, see below; still open.) Chapter 17 §17.6.2 gives the raw value as R = 0.124,
   corrected to 0.098 after the Hellinger fix. Chapter 8 (running example) and Chapter 9 §9.7 say
   the hand-feature model drops "from R = 0.151". The reference and §17.6.2 give 0.151 as the
   value on the Echonest subset (n = 5,233), and the reference does not list 0.124 or 0.098. With
   residualized R = 0.043, the 91% follows only from 0.151 (91.9%). From 0.124 it would be 88%,
   and from 0.098 it would be 81%. Nothing was changed. Needed: the raw full-corpus hand-feature R
   that the 91% was computed from.
3. **What the Lasso channel regresses on.** Chapter 17 §17.3.4 says the per-component variances.
   Chapter 6 §6.5 and the Appendix B code say the mean projections. Appendix D Step 5 says "the
   PCA spectrum of the paragraph-cloud covariance". The count (128) is reconciled above. The
   feature is not. Needed: the experiment code.
4. **n = 940.** (Repaired, see below.) The reference and §17.5.2 give 940 as the number of non-English books with matched
   ratings in the rating-transfer test. Appendix F (F12.2) and Appendix D §D.3 use "n = 940
   bundles across 19 languages" for the dispersion ratios and the correlation panel. The bundle
   counts printed in the reference sum to 926 at the threshold (ten languages) and 951 with the
   exploratory languages (seventeen languages). Nothing was changed.
5. **How many of the 71 axes are interpretable.** Appendix F (F14.2) says about 30. Chapters 5, 7,
   8, 17, 18 and 29 and the reference call all 71 interpretable, or a large majority of them.
   Only Chapter 14 was brought in line with the ledger. Needed: which count is right.
6. ***Bleak House* in Chapter 7 and Appendix D.** Chapter 7 gives a Goodreads rating of 4.05 and
   about 8,400 paragraphs. Appendix D gives about 4.04 and about 7,400 paragraphs. Neither can be
   checked in the repository.
7. **Claims about Geometric Ethics in Chapter 8 §8.8 and Chapter 17 §17.7.** The "100%
   cross-linguistic transfer of the deontic axis" and the section numbers cited for the
   nine-dimensional structure (§17.3, §17.2, §20.10 of that volume) were left as written, now
   attributed to *Geometric Ethics*. That volume's ledger classes the cross-lingual
   nine-dimension claim as exploratory, and its v1.25 reports four axes doing no better than a
   general-valence channel. Whether this volume's summary should be weakened is the author's call.
8. **Chapter 2, "the nine-plus-dimensional object".** (Closed on re-verification, see below.) The Moby-Dick passage uses a dimension count
   that Chapter 5 §5.5 does not support. Left as written, since it reads as a figure of speech.
9. **The README's admission-filter statement.** The README says the AesBSE embedding instrument was
   ruled inadmissible (surface is the thing, genre confound, cross-modal sign flips). The book
   does not mention AesBSE, and it calls the cross-lingual result its strongest finding. No
   chapter sentence was found that contradicts the README outright, so nothing was changed.

## Corrected with the figures (2026-11-26)

- Chapter 4, Section 4.4 worked example: for mu = 0 and sigma = 2 the text gave H^2 = 0.056; the chapter's own closed form gives 1 - sqrt(4/5) = 0.106 (and 0.118 for the mean shift, as printed). The sentence's conclusion, that Hellinger ranks the mean shift as the larger change while KL ranks the spread larger, still holds. Figure 4.1 draws the computed values.
- Appendix F, row F5.3: the status cell read "TODO; open problem in Chapter 29."; it now reads "Open problem; see Chapter 29."

The five older figures in figures/ (wundt_curve, expertise_shift, preference_manifold, symmetry_budget, compression_progress) illustrate the compressibility theory of paper/v3.tex, which no chapter introduces; none is embedded and none belongs to a chapter. They are left as files, unreferenced. Faults found in them, for the record: the Wundt curve's "optimum" sits at a local minimum between two humps; the preference manifold places the cheap direction on the wrong axis and posits an optimum the book does not; all five use dark text on a transparent background, nearly invisible on the dark site.

## Found while drawing the figures (2026-11-26), not changed

These were noticed while the figures were drawn. No figure draws them.

1. Chapter 2, Case 2: nineteen critics at 70 and one at 100 average 71.5, not 72. (Repaired, see below.)
2. The 91% (the hand-feature figure) is still applied to music in general in Chapter 2 ("85-91% ... across books and music", whose "six-to-eight-sigma" also ignores the 28.3 sigma music result), Chapter 8 (Sections 8.1 and 8.8), Chapter 26 (Section 26.2, "9-15% non-confounded"), Chapter 29 (Section 29.12, where the 28 sigma result is the spectrum Lasso, 66%) and Chapter 21 (Section 21.6). (Repaired, see below.)
3. Chapter 4: "128 axes capture about 85% of variance" (Section 4.3) and "inflated by an order of magnitude" (Section 4.6) are unsourced; Appendix B, Section B.8.2, says a factor of 2 to 3. (Repaired, see below.)
4. The cross-lingual rho is described as readers rating translations alike (Sections 5.3, 6.3, 28.1); Chapter 5 calls mahal_mean the most language-invariant feature, while pair_sim_mean is higher; Chapters 1 and 6 (Section 6.9) attribute rho of about 0.7 to the trajectory features. (Repaired, see below.)
5. Saturation dimension: Sections 5.2 and 6.8 say 45 frames in 1024 dimensions; Chapter 17, the reference and B.8.1 say 128. In Chapter 5, 224/14 gives 256 patches, not 196. (Repaired, see below.)
6. Section 5.5: with a single Gaussian prior the inverse covariance is constant everywhere, so the metric does not depend on location. (Repaired, see below.)
7. Wrong references to Chapter 7: Sections 5.10 and 6.9 say it uses Moby-Dick (it uses Bleak House); Section 30.2 describes its five levels wrongly; Section 30.9 says Chapter 29 is longer than Chapter 17 (the reverse). (Repaired, see below.)
8. Chapter 6: the level-by-level R values of Section 6.7 (0.08, 0.18, 0.21, 0.24) and their F-tests are not in the reference; Section 6.8 calls the music pair_sim_mean result "8 sigma-equivalent", while rho = -0.076 with p = 5e-33 is about 12 sigma. (Repaired, see below.)
9. Chapter 7, Level 0: "less so than Great Expectations (3.79)" compares a lower rating as if higher; the comparison ratings are unsourced. (Repaired, see below.)
10. Chapter 7, shuffle counterfactual: shuffling lowers path_eff toward 0 (not "toward unity"); with Appendix B's code recur_rate does not change under shuffling, and with Chapter 17's definition it would rise, not collapse. (Repaired, see below.)
11. Feature definitions in Appendix B's code differ from the chapters (recur_rate, acf1_top3, tail_mass_100; `js` is a symmetrized KL, not Jensen-Shannon); Section 25.3 defines curvature differently again. (Partly repaired, see below; still open.)
12. Section 10.5 calls "My Favorite Things" a Gershwin song (it is by Rodgers and Hammerstein); Sections 10.6 and 10.9 attribute residualized results to the trajectory channel that the reference does not report. (Repaired, see below.)
13. Section 11.5's effective dimension "d ~ 30-60 (Chapter 17)" is not in Chapter 17. (Repaired, see below.)
14. The bundle threshold is 20 bundles per language; Sections 12.4 and 12.6 call it 20 paragraphs per side; Section 29.2 says five Chinese bundles "reached the n>=20 threshold" (they fell below it). (Repaired, see below.)
15. Section 14.4: "~8 sigma on top of the hand-designed features" is unsourced, and Lasso sparsity comes from the l1 penalty, so it is not evidence of emergence. (Repaired, see below.)
16. Theorem 15.1(i): non-injectivity holds for continuous Q, not "any function" (Chapter 20 states it correctly). (Repaired, see below.)
17. Chapter 18: Section 18.3 gives d of about 25-30 yet includes the 71 axes; Section 18.7 makes causal claims about conditioning on channel values, which Section 17.8 rules out. (Repaired, see below.)
18. Section 21.4 says the head-to-head uses genre residualization, which the reference does not say; Section 21.8 calls the sign flip a "direct empirical witness" for Chapter 13, which Appendix F lists as an analogy. (Repaired, see below.)
19. Section 22.5: the 2010 Psychological Science paper is by Cutting, DeLong and Nothelfer, not "Cutler and colleagues". (Repaired, see below.)
20. Chapter 26: "we observed basin structure directly" (Section 26.3) is unsupported; Section 26.4 cites Chapter 12 for a cross-modality-invariant signal, which Chapter 12 shows is not. (Repaired, see below.)
21. Chapter 27: "70-85% genre accuracy" (Section 27.3) is unsourced; Section 27.2 calls tr(Sigma) a measure of coherence, though it measures spread. (Repaired, see below.)
22. Chapter 28: "twentieth-first-century" (typo). (Repaired, see below.)
23. Section 29.3: pair_sim_mean is said to compare consecutive windows (it averages over all pairs), and the "30-second windows" are one 30-second clip. (Repaired, see below.)
24. Claims with no data behind them: Chapter 3 (a hand-versus-learned feature comparison for books, an Arnheim-encoder correlation), Chapter 8 (within-rock and penumbral-zone findings), Section 9.9 ("survive translation across media"). (Repaired, see below.)

## Repaired in the survey of 2026-11-26

Each open item above was re-checked against the current text first. The right text was
established from the volume itself (the reference, Chapter 17, Appendix F, the chapter's own
definitions and printed numbers) or, for the two attribution errors, from the cited works. Where
no source exists in the repository, the claim was weakened to an estimate, an expectation or an
attribution, and nothing was deleted. No figure line, caption, heading before a figure, or file
under `tools/`, `figures/` or `.build/` was edited. None of the 34 figures draws a number that
changed. "F" numbers refer to the list "Found while drawing the figures", "U" numbers to
"Unresolved".

**F1. Chapter 2, Case 2 (Metacritic).** Said "Nineteen critics gave it a 70 and one gave it a
100" as a configuration with mean 72; that averages 71.5. Now "Fourteen critics gave it a 70 and
one gave it a 100": (14 × 70 + 100) / 15 = 72 exactly, with the scores and the single enthusiast
kept. Established by arithmetic.

**F2. The 91% applied to music in general.** The 91% is the hand-feature share; the spectrum
Lasso loses 1 − (0.177/0.302)² = 66% (reference, Phase 4; F21.2).
- Chapter 2, "The Empirical 85% as Structural Evidence": "roughly 85–91% of the predictive
  variance ... is absorbed by ... genre" and "R in the 0.09–0.19 range, with six-to-eight-sigma
  significance" now read "most of the predictive variance ... 85% in books, 91% for the music hand
  features, and about two-thirds even for the music spectrum Lasso (1 − (0.177/0.302)² = 66%)" and
  "R from about 0.04 to 0.19, with significance from about six sigma to 28 sigma" (the printed
  residual values are 0.043, 0.093, 0.131, 0.139–0.185 and 0.177, at 6.2σ to 28.3σ).
- Chapter 8 §8.1: "The corresponding figure in music was ninety-one percent" now adds that it is
  the hand-feature figure, "and about two-thirds for the music spectrum Lasso". §8.8: "(85% in
  books, 91% in music)" is now "(85% in books, 91% for the music hand features)".
- Chapter 26 §26.1: "the within-genre residualized effect was R = 0.043 (8.4σ) compared to the
  raw R = 0.302" paired the hand-feature residual with the spectrum-Lasso raw value and with the
  books coherence z. Now: the hand-feature residual is R = 0.043 (z = 6.7), and the spectrum Lasso
  fell from R = 0.302 to 0.177 (28.3σ), losing about two-thirds of its R². §26.2: "(85–91% genre
  confound)" and "the 9–15% non-confounded signal" now give the shares per model (85%, 91%, about
  two-thirds) and the residuals (15%, 9%, about a third).
- Chapter 29 §29.12: "a 28σ music result with a 91% genre confound correctly diagnosed" now says
  the 28σ is the spectrum Lasso after residualization and gives both shares.
- Chapter 21 §21.6: "Our residualized effect sizes ... ρ = −0.076" (that ρ is not a residualized
  value) is now "Our effect sizes ... R = 0.177 for the residualized spectrum-Lasso, ρ = −0.076 ...",
  and "state the direction at 28σ residualized" is now "state its direction (p = 5 × 10⁻³³ for
  pair_sim_mean; the 28σ figure belongs to the residualized spectrum Lasso, not to the sign)".
- The same slip, found on the way: §21.9 "the 91% genre-confound finding" now gives both shares;
  Appendix E §E.1 "That 85–91% of the headline is genre" now reads "That most of the headline is
  genre (85% of the books R²; in music, 91% of the hand features' and about two-thirds of the
  spectrum Lasso's)"; Chapter 17 Claim 17.1 ("dominated by genre in hand-crafted features (85–91% of
  raw variance ...)") and §17.8 ("hand-engineered features are dominated by genre confound ... (85%
  in books, 91% in music)") credited the books' 85% to hand features, but it is the share of the
  combined Ridge+Lasso model (reference, Phase 2). They now say "85% of the combined books model's
  R², and 91% of the music hand features'" and "85% of the combined model's R² in books, 91% of the
  hand features' in music".

**F3. Chapter 4, unsourced figures.** §4.3 "it captures roughly 85% of embedding variance" is now
"by an estimate that is not among the results recorded in Chapter 17, it captures roughly 85% ...",
and "well-conditioned" is now "well-conditioned for books" (§17.6.1 reports the 128-d fits
ill-conditioned for music). §4.6 "inflated by an order of magnitude" is now "inflated, by an
estimated factor of 2 to 3 (Appendix B, §B.8.2)", the weaker of the two in-volume figures; Appendix
B §B.8.2 "will inflate the headline R by a factor of 2–3" now says "by an estimated factor of 2–3".
Neither figure has a source in the repository.

**F4. What the cross-lingual ρ measures.** It correlates a feature's value on a book with its
value on the translation (§17.5.2); no ratings of translations by Finnish readers were collected,
and rating transfer is R = 0.07.
- §5.3: "When Finnish readers and English readers rate translations of the same book similarly,
  this is one of the features on which they agree" is now "When a book and its Finnish translation
  are encoded, this is one of the features on which the two clouds agree most closely". "The single
  most language-invariant of all hand-features tested" (mahal_mean, 0.710) is now "after internal
  coherence (pair_sim_mean, ρ = +0.712), the most language-invariant of the hand-features ranked by
  mean Spearman correlation".
- §6.3: "the most language-invariant features tested" is now "among the most ...; only the
  internal-coherence feature below ranks higher (ρ = +0.712)", and "When English readers and Finnish
  readers rate translations similarly" is now "When a book and its Finnish translation yield similar
  feature values". §6.8, Level 1: "the single most language-invariant in Phase 3" is now "after
  pair_sim_mean (ρ = +0.712), the most language-invariant by mean Spearman correlation".
- §28.1: "the same feature carried the same aesthetic signal in Finnish, French, and Greek" is now
  "the same feature took similar values on a book and on its translations into Finnish, French, and
  Greek".
- Chapter 1, "What Geometry Provides": "(internal-coherence, trajectory-geometry, and
  spectral-divergence measures) exhibit Spearman correlations of ρ ≈ 0.71" is now "(internal-
  coherence, mean-displacement, and spectral-divergence measures) exhibit mean Spearman correlations
  of ρ ≈ 0.67–0.71 ..., while trajectory-geometry features such as path efficiency vary little between
  a book's translations"; "the strongest pair (English–Finnish ...)" is now "the headline pair"
  (English–French is higher, 0.78).
- §6.9: "the Level-2 divergences and the Level-3 trajectory features ... transfer across languages
  with Spearman ρ ≈ 0.7" now gives ρ ≈ 0.7 for the divergences and the coherence feature, and says
  that the trajectory features path_eff and recur_rate vary least between translations (ratios 0.18
  and 0.28, F12.2).

**F5. Dimension of the Gaussian fits; patch count.** The reference ("45 tokens in 128-d"), §17.6.1,
§B.5 and §B.8.1 put the music Gaussian fits in the 128-d PCA basis. §5.2 "For MERT we work in the raw
1024-d space ... (45 frames in 1024 dimensions is badly under-sampled)" now says the states are
projected into a 128-d PCA basis fitted on the music corpus (Appendix B, §B.5) and "45 frames in 128
dimensions"; §6.8 "45 frames in 1024-d" is now "45 frames in 128-d". The same slip, found in
Appendix D §D.2 Step 1 ("the 45-in-1024 regime") and Appendix E §E.4 ("Gaussian fits in 1024-d"),
is repaired the same way. §5.2 "encoded by DINO with 14×14 patches, X(W) is 196 points" is now
"encoded by DINOv2 with 14×14-pixel patches, X(W) is 16 × 16 = 256 points" (224/14 = 16; the chapter
names DINO-v2 as its image encoder, and Figure 23.1 uses the same patching, 518/14 = 37). Found on
the way, §5.1: "a 30-second clip's 20ms frame" contradicted the 45 frames per clip of §5.2 and is now
"each of a 30-second clip's 45 frames".

**F6. §5.5, location-dependent metric.** Said that near the corpus centroid a small displacement
is aesthetically larger and in thin regions smaller, "we normalize by the local prior variance".
D_Mahal uses Σ0⁻¹, which for a single Gaussian prior is the same at every point. The passage now
weights by direction (a step along a direction of small prior variance is aesthetically larger), says
"we normalize by the prior variance in each direction", and adds that with a single Gaussian prior
the weighting does not change from region to region; a metric that did would need a non-Gaussian
prior such as a mixture.

**F7. References to Chapter 7.** §5.10 and §6.9 "Moby-Dick" are now "Bleak House". §30.2 "five tensor
levels ...: the brush-stroke, the phrase, the movement, the corpus, the tradition" now names
Chapter 7's work and levels as its headings give them: the scalar rating, the mean embedding and its
distance from the corpus, the divergences and internal coherence, the trajectory, and the loadings on
the Lasso-discovered axes. §30.9 "Chapter 29 is longer than Chapter 17" (Chapter 17 has 5,281 words,
Chapter 29 3,918) is now "Chapter 29's list of what the framework has not produced is longer than its
list of what it has (§29.12)" (eight items against seven).

**F8. Chapter 6.** §6.7: the level-by-level ladder (R ≈ 0.08, 0.18, 0.21, 0.24, partial F-tests at
p < 10⁻⁶) is not in the reference or Chapter 17. It is now stated as an expectation, not a
measurement; only the 0.24 of the combined model is called measured. §6.8: "pair_sim_mean contributes
8σ-equivalent signal" (music) is now "about 12σ-equivalent": ρ = 0.076 at n = 24,801 gives
z ≈ 0.076 × √24,800 ≈ 12.0, and p = 5 × 10⁻³³ corresponds to about 11.9σ.

**F9. Chapter 7, Level 0.** "more admired than The Old Curiosity Shop (3.82) and less so than Great
Expectations (3.79 — which complicates ...)" is now "It tells us, on approximate ratings quoted here
as illustrations, that Bleak House is more admired than The Old Curiosity Shop (3.82) and Great
Expectations (3.79), and nearly tied with David Copperfield (4.04)". The comparison now follows the
numbers printed; the ratings, which have no source, are labelled approximate illustrations.

**F10. Chapter 7, the shuffled Bleak House.** "recur_rate collapses (the narrative no longer
revisits), path_eff rises toward unity" now says that recur_rate does not collapse (Appendix B's code
counts all pairs, so shuffling leaves it unchanged; §17.3.3 counts only pairs far apart in the
sequence, so it rises as formerly adjacent close pairs are scattered) and that path_eff falls toward
zero (the first-to-last distance stays that of a typical pair while the path length grows with every
random step; with path_eff = ‖φ(t_N) − φ(t_1)‖ / Σ‖Δ_n‖ the shuffled value is about 1/(N − 1)). The
same slip in "What the Trajectory Can Say" ("a much lower recur_rate") is repaired. Figure 7.1 draws
only step_mean and is unaffected.

**F11 (partly). Feature definitions.** Appendix B §B.6 now says, after the code, that the sketch's
`js` is a symmetrized KL divergence, not the Jensen–Shannon divergence of Chapter 4 (which has no
closed form for Gaussians), that its recur_rate, acf1_top3 and tail_mass_100 differ from the
definitions in Chapter 6 and §17.3.3, and that the appendix does not record which form produced the
reported numbers. §25.3 Prediction 25.2 now says its curvature is the second difference
‖s_{t+1} − 2s_t + s_{t−1}‖, which, unlike the angle-based curvature of Chapter 6, grows with step
size. Which definitions the experiments used is still open (below).

**F12. Chapter 10.** §10.5 "Start at the Gershwin song "My Favorite Things."" is now "the Broadway
song"; the next sentence already names Rodgers and Hammerstein, its authors. §10.6 "disappearing
substantially under genre residualization (Phase 2) but not vanishing. That residual is where local
curvature lives" now says that Chapter 17 does not report how much of it survives residualization,
that the residualized model as a whole keeps R = 0.093, and "Whatever part survives is where local
curvature would live". §10.9, second observation: "The trajectory channel is not trivially reducible
to genre. It is, at reduced effect size, independently predictive within genre" now says that
R = 0.093 is for all channels together, that Chapter 17 does not report the channel's residualized
effect, and that the claim is "an expectation rather than a finding". Found on the way, §10.9 first
observation: "They are a found rather than constructed channel" contradicted §17.3.4 ("The three
channels above are hand-crafted"); it now says the features were proposed and measured in
exploratory work before the framework was imposed, are hand-crafted, and that their signal was found
in the data rather than derived from the framework.

**F13. §11.5.** "our empirical estimate of the effective dimension from the 128-d PCA basis
(Chapter 17) is on the order of d ~ 30–60" is now "a rough estimate of the effective dimension of
the 128-d PCA basis, which Chapter 17 does not report, is ...".

**F14. The bundle threshold.** The threshold is 20 bundles per language (reference; §B.2.2; §8.5).
Chapter 12's running example ("bundles contain at least twenty LaBSE-encoded paragraphs") is now
"the 288 Finnish books matched in bundles with their English originals"; §12.4 "(matched book pairs
with ≥ 20 LaBSE-encoded paragraphs on each side) formed in ten languages with statistical power" is
now "(matched book pairs: a book and its translation) formed in ten languages at or above the
statistical-power threshold of 20 bundles per language"; §12.6 "the twenty-paragraph threshold" is
now "the threshold of twenty bundles per language"; §29.2 "Only five Chinese-language bundles reached
the n≥20 threshold" is now "Only five Chinese-language bundles formed, below the threshold of 20
bundles per language".

**F15. §14.4.** The bullet "collectively contribute ~8σ of predictive signal on top of the
hand-designed features" is now "collectively add predictive signal ... (roughly 8σ, by an estimate
that Chapter 17 does not report)". The caveat "the Lasso's discovery of any interpretable axes at
all — let alone 71 — is evidence that the collective aesthetic tensor has non-zero emergent
components. A pure sum of individual judgments would have produced a diffuse, un-sparse solution. It
did not." now says that the interpretable axes (about 30 of the 71, F14.2) are consistent with
emergent components but not evidence for them, because the sparsity comes from the ℓ1 penalty
(§4.6), which would give a sparse solution for a pure sum of individual judgments too.

**F16. Theorem 15.1.** "Let Q: ℝ^d → ℝ be any function" is now "Let Q: ℝ^d → ℝ, d > 1, be any
continuous function" (an arbitrary function from ℝ^d to ℝ can be injective). The proof sketch of (i)
now opens with the reason: no continuous map from ℝ^d to ℝ with d > 1 is injective, since removing
one point disconnects an interval but not ℝ^d; the rank-nullity remark is kept for smooth Q. This is
the form Chapters 20 and 21 already state. The same qualifier is added in §26.5 ("A continuous
aesthetic reward function").

**F17. Chapter 18.** §18.3: "d ... (roughly 25–30 for our implementation)" contradicted the channel
list just above, which includes the 71 Lasso axes. Now "88 for our implementation, counting the
features listed above: 6 divergences, 2 coherence features, 9 trajectory features and the 71
Lasso-selected axes" (a count of that list). §18.7: "conditioning signals that, by Chapter 17's
sign-flip result, predict higher listener engagement" is now "conditioning signals in the direction
that ... goes with higher listener engagement among existing tracks", followed by "Whether
conditioning a generator in that direction would raise engagement is untested: Chapter 17 reports
correlations and makes no causal claim (§17.8)." Found on the way: §18.3 "The ~8σ-each significance
of these features across languages" (the 8σ is the books result) now says "in the books corpus";
§18.4's unfinished comparison "the difference between a recommender that sees twice as much
aesthetic signal." now ends "and one that does not."

**F18. Chapter 21.** §21.4 "identical genre residualization" for the Echonest head-to-head (the
reference does not say so) is now "(Chapter 17 does not say whether this comparison was
genre-residualized)". §21.8 "has a direct empirical witness in the sign flip" is now "finds an
illustration, by analogy only (Appendix F, F13.1), in the sign flip".

**F19. §22.5.** "Cutler and colleagues (Psychological Science, 2010, "Attention and the Evolution of
Hollywood Film")" is now "Cutting, DeLong and Nothelfer". The finding was also misdescribed: that
paper analyses the sequence of shot lengths in 150 films of 1935–2005, whose power spectra approach
1/f over time; it is not a property of the distribution of durations. "the distribution of shot
durations ... has followed approximately 1/f statistics, and that the slope has steepened (shorter
average shots)" is now "the sequence of shot durations ... has come to follow approximately 1/f
statistics, the spectral slope steepening toward 1/f over the twentieth century while average shots
grew shorter".

**F20. Chapter 26.** §26.3 "we observed basin structure directly" is now "Our music empirical work is
consistent with basin structure but does not observe it directly", and "the cross-genre distances on
an engagement-trained embedding are much larger. A user ... faces" is now "we expect the cross-genre
distances on an engagement-trained embedding, which we have not built, to be much larger. A user ...
would then face". §26.4 "cross-modality-invariant aesthetic signal (Chapter 12)" is now
"cross-lingually invariant aesthetic signal (Chapter 12; across modalities their signs flip)". Found
on the way, §26.4 Prescription 3: "classical music, which has R = −0.013 in our data and is therefore
in a distinct engagement basin" (a null within-genre R says nothing about basins) is now "where our
within-genre signal is null, R = −0.013, and which we expect to form a distinct engagement basin".

**F21. Chapter 27.** §27.3 "where genre classification from MERT embeddings is routinely 70–85%
accurate on FMA" is now "is, by a rough estimate not measured in this book, 70–85% accurate". §27.2
"A brand's within-catalog coherence is tr(Σ_B)" is now "within-catalog spread is tr(Σ_B), so a small
trace measures its coherence".

**F22. §28.1.** "twentieth-first-century" is now "twenty-first-century".

**F23. §29.3.** pair_sim_mean "measured as the mean cosine similarity between consecutive embedded
windows" is now "over all pairs of embedded windows" (§17.3.2). "adjacent 30-second windows in a
track" is now "adjacent timesteps of a track's single 30-second clip" (§17.6.1, §B.4.2).

**F24. Claims with no data behind them.** Chapter 3, "What Birkhoff Missed": "In our empirical work
on books (Chapter 17), ... hand features recover a small fraction of the signal ..." now cites the
comparison that exists, in music (Spotify's eight features R = 0.103 against the MERT spectrum Lasso
R = 0.225 on the Echonest subset, §17.6.2), and adds "We have not run the corresponding comparison on
books." "What Arnheim Missed": "A sufficiently trained vision encoder produces a representation space
... substantially correlated with Arnheim's described forces" now begins "We expect that" and ends
"this has not been measured." Chapter 8 §8.4: the fiction and rock channel signs are now
expectations, with a sentence that the within-genre analyses report only each stratum's overall
result (fiction R = 0.131, rock R = 0.139); §8.7, penumbral zones: "can show ... often split" is now
"we would expect ... to show ... to split ...; we have not tested this." §9.9 "facts that survive
translation across media" is now "across languages" (the measured invariance is across languages;
across media Chapter 17 finds the signs reverse).

**U2 (partly).** Chapter 8's running example ("the hand-feature model drops from R = 0.151 to
R = 0.043") and §9.7 ("down from R = 0.151") presented the Echonest-subset value (n = 5,233; §17.6.2,
reference) as the full-corpus raw value. Both now give R = 0.043 and attribute 0.151 to the Echonest
subset of 5,233 tracks. The full-corpus raw value is still open (below).

**U4. n = 940.** 940 is the number of non-English books with matched ratings in the rating-transfer
test (reference; §17.5.2; F12.4). The headline invariance analyses use only the ten languages at the
threshold (§B.2.2: the below-threshold languages are "not for the headline invariance claims"; §12.4),
whose bundle counts sum to 926. Appendix F, F12.2 "n = 940 bundles across 19 languages" is now
"Matched bundles of the ten languages at the threshold of 20 (926 by the per-language counts of
Chapter 17; the n = 940 of F12.4 counts non-English books with matched ratings)"; Appendix D §D.3
"(n=940 bundles, 19 languages)" is now "(the matched bundles of the ten languages at the threshold,
926 by the per-language counts of Chapter 17, from a corpus of 19 languages)".

**U8 (closed on re-verification, no change).** "The nine-plus-dimensional object" in Chapter 2 counts
the nine illustrative axes the same passage lists for Moby-Dick ("might be written as a rank-1 object
with components along many dimensions"). It makes no claim about the dimension of the aesthetic
manifold and does not conflict with §5.5.

**Other slips found while reading, repaired.**
- §12.4 "The strongest individual language-pair result is EN↔FI" (0.77) is now "The most
  significant"; EN↔FR is 0.78.
- §29.1: "(§29.8–§29.9)" is now "(§29.8–§29.10)" (the nine problems run from §29.2 to §29.10;
  integration is §29.10). "witnessing Chapter 12's Noether-style symmetry claim in data rather than
  analogy" is now "the measured invariance on which Chapter 12's Noether-style reading rests; the
  reading itself is an analogy (Appendix F, F12.3)". §29.2: "headline values above ρ=+0.77 in the
  largest bundles" is now "of ρ=+0.77 and +0.78 in the two largest bundles", and "the other nineteen
  languages" is now "the other eighteen" (Chinese is one of the 19).
- §30.6: "Chapter 26's AI curation results, modest as they are" (Chapter 26 reports none) is now
  "Chapter 26's AI-curation arguments, untested as they are". §30.9: "a negative slope at
  p < 10⁻³³" (5 × 10⁻³³ is not below 10⁻³³) is now "at p = 5×10⁻³³".
- Appendix B §B.10: "4,998 × 19 langs ≈ 9,681 books" (4,998 × 19 = 94,962) is now "4,998 English +
  4,683 in 19 other languages = 9,681 books".
- Appendix D §D.1 Step 2: Hellinger "carries the most cross-lingual signal in our corpus (ρ = +0.675
  ...)" (pair_sim_mean and mahal_mean are higher) is now "is the feature of the headline cross-lingual
  pairs in our corpus (EN↔FI ρ = +0.77, EN↔FR ρ = +0.78; mean ρ = +0.675 across language pairs ...)";
  §D.3 "`Hellinger`: the most predictive individual channel" is now "the channel of the headline
  pairs".
- Spelling: Prediction 24.3 "dogu brackets" is now "dougong brackets" (the East Asian timber bracket
  set); §22.8 "neuro-cinematics program of Hasson" is now "neurocinematics", the name of that
  program.

**Series checker.** `series_check.py` (erisml-lib) was run before and after. Its four prose-dup
findings were false positives (a heading followed by a paragraph that starts with the same word, and a
display formula followed by a paragraph that starts with a formula); the current version of the
checker no longer reports them. It reported no placeholder (the "TODO" of F5.3 was removed with the
figures). The codespell findings ("pre-empts", the loop variable `te` in Appendix B's code, the
author Hart of Hart, Nilsson and Raphael) are not errors. Of the spelling candidates only "dogu" and
"neuro-cinematics" were errors; the rest are proper names, terms ("hana", "griot", "maqam",
"dougong"), the bolded initials of §19.1 ("**D**iscover"), or British spellings, which several
chapters use throughout and which were left. Final counts: 0 hard defects; 65 candidates (5
codespell, 60 spelling candidates, no prose-dup, no placeholder); KaTeX 1,656 snippets, 0 failures;
788 cross-references, 0 dangling.

## Still open after the survey of 2026-11-26

These need something the repository does not hold or a decision that is the author's.

1. **The failed compressibility formula (U1).** Needed: the record of the failed test (or word that
   the README status block is wrong) and the place in the book where the formula and its failure
   should be reported. Also the author's decision on `OUTLINE.md`, whose Chapter 17 line
   ("Pre-registered, double-blind validation ... 50,000+ Goodreads reviews, 9 cultural traditions")
   and paper paragraph ("condenses ... the empirical results of Chapter 17") describe the study of
   `paper/v3.tex`, not the current chapter.
2. **The raw full-corpus hand-feature R for music (U2).** §17.6.2 prints 0.124 (0.098 after the
   Hellinger fix). With the residual R = 0.043, a 91% share needs a raw R between about 0.140 and
   0.147; 0.151 gives 92%, 0.124 gives 88%, 0.098 gives 81%. Needed: the raw value the 91% was
   computed from, or the corrected share. If the share changes, every 91% in the book changes (37
   mentions across 16 chapters and five appendices); Figure 16.1's caption names the 91% but no
   figure draws it.
3. **The experiment's feature definitions (U3, F11).** Needed: the experiment code, or the author's
   statement, for: what the Lasso regresses on (per-component variances, §17.3.4; mean projections,
   §6.5 and the Appendix B code; "the PCA spectrum of the paragraph-cloud covariance", Appendix D
   Step 5); recur_rate (Chapter 6: return to an earlier state with m ≪ n; §17.3.3: pairs with
   |i − j| > τ; Appendix B: all pairs with cosine > 0.9); acf1_top3 (Chapter 6 and §17.3.3: lag-1
   autocorrelation of the top three PCA coordinates; Appendix B: step-magnitude autocorrelation at
   lags 1–3, summed); tail_mass_100 (Chapter 6: share of steps above the corpus 99th percentile;
   Appendix B: share of path length in the 100 largest steps; Appendix D: mass in the top 1% of
   steps); and whether the reported "JS" is the Jensen–Shannon divergence or the sketch's symmetrized
   KL. With Appendix B's recur_rate (all pairs) the feature ignores order, so Chapter 7's Level 3
   account, in which recurrence separates Bleak House from its shuffle, holds only under an
   order-sensitive definition. Also the author's choice for Prediction 25.2: the second difference
   it now names explicitly, or the angle-based curvature of Chapter 6.
4. **How many of the 71 Lasso axes are interpretable (U5).** Appendix F, F14.2 (and now §14.4) say
   about 30. The reference, §4.3, §4.6, §5.5, §5.8, §6.5, Chapter 7 Level 4, §8.3, §8.4, §9.2,
   §17.3.4, §17.4.2, §18.3, §19.3, §29.6, §30.3 and Appendix D Step 5 call all 71 interpretable or
   a large majority of them; Appendix D §D.2 Step 5's "30+ surviving axes" for music has no source.
   Needed: which count is right.
5. **Bleak House in Chapter 7 and Appendix D (U6).** Rating 4.05 (Chapter 7) against about 4.04
   (Appendix D); about 8,400 paragraphs (Chapter 7) against about 7,400 (Appendix D), and Appendix
   D's "thirty-one paragraphs per chapter on average" gives about 2,100 for the novel's 67 chapters.
   All are representative values. Needed: one consistent set (or the measured values).
6. **Summaries of Geometric Ethics (U7).** Chapter 8 §8.8's "100% cross-linguistic transfer of the
   deontic axis in the BIP experiments" still matches Geometric Ethics v1.29, whose Chapter 17
   opening says "BIP experiments show 100% transfer of O/L structure across eleven languages" (that
   volume now keeps a LaBSE-is-not-human caveat beside such claims). Chapter 17 §17.7's "a
   nine-dimensional structure that Geometric Ethics reports as cross-culturally invariant at the level
   of dimensions (its Chapter 17 §17.3)" no longer matches it: v1.29 reports eight of nine axes
   passing its gate, four collapsing onto one general-valence channel, an effective rank of 5.19 of
   8 (its §5.3), and calls the nine a chart. Needed: the author's wording for §17.7, and that
   volume's current section numbers for the §17.3, §17.2 and §20.10 cited there.
7. **The README's admission-filter statement (U9).** The README rules the AesBSE embedding
   instrument inadmissible; the book does not mention AesBSE and calls the cross-lingual result its
   strongest finding. Needed: the author's decision whether, and where, the book should report that
   verdict.
8. **Other statements with no source, found while reading.** §6.4 ("regressing out Level-1 and
   Level-2 features still leaves substantial Level-3 residual signal"); §6.8, Level 4 music ("The
   discovered axes correspond to genre and instrumentation"); Chapter 7 Level 4 (the axes "are stable
   across cross-validation folds"; "A typical novel in our corpus has loadings on three to seven
   axes"); Appendix E §E.1 (the features "recover fiction-vs-non-fiction, Victorian-vs-Modern, and
   Romance-vs-Mystery with high accuracy"); Appendix E §E.4 (the sign flip "persists and intensifies"
   after the Hellinger fix; no pre-fix values are reported); §27.3 ("Design critics can, in blind
   comparison, identify Apple products from silhouette alone with high accuracy"). Needed: a source
   for each, or agreement to weaken them as the items above were.
