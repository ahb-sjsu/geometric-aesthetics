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
2. **The raw hand-feature R for music.** Chapter 17 §17.6.2 gives the raw value as R = 0.124,
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
4. **n = 940.** The reference and §17.5.2 give 940 as the number of non-English books with matched
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
8. **Chapter 2, "the nine-plus-dimensional object".** The Moby-Dick passage uses a dimension count
   that Chapter 5 §5.5 does not support. Left as written, since it reads as a figure of speech.
9. **The README's admission-filter statement.** The README says the AesBSE embedding instrument was
   ruled inadmissible (surface is the thing, genre confound, cross-modal sign flips). The book
   does not mention AesBSE, and it calls the cross-lingual result its strongest finding. No
   chapter sentence was found that contradicts the README outright, so nothing was changed.
