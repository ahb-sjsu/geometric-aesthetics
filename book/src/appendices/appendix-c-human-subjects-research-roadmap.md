# Appendix C: Human-Subjects Research Roadmap

The empirical results reported in this volume (Chapter 17) are derived from existing archival data: Gutenberg texts paired with Goodreads ratings, and FMA Medium tracks paired with Free Music Archive listen counts. No human subjects were recruited. No consent was solicited. The ratings and listens used as target variables were produced by uncountable anonymous individuals over years of platform use, aggregated into per-work summary statistics before we ever looked at them. This is research on *traces* of aesthetic judgment, not on aesthetic judgment in the act.

The framework, however, reaches further than trace data can test. Several of its most interesting claims — that aesthetic judgment has personal structure that aggregates into collective canon, that taste drifts along geodesics over time, that non-Western aesthetic traditions occupy different regions of the manifold than the LaBSE-trained encoder would naturally find, that the cross-modality sign flip is a property of individual evaluative systems and not merely an artifact of population-level aggregation — these require *new* data, and that data will come from human subjects. This appendix lays out what studies we believe the framework calls for, what they would need in order to be ethically defensible, and what we see as the specific risks that come with applying a Western-text-and-Western-music-trained geometric apparatus to participants whose aesthetic traditions were not represented in the training corpora.

This is a research program, not a set of completed studies. We sketch protocols at the level of research-design and ethics-of-data; specific IRB protocol text, sample-size refinement, and preregistration are work for the labs that take this up, not for this volume.

## C.1 Four Research Programs the Framework Invites

### C.1.1 Personalized-Aesthetic Learning

The framework as presented in Chapters 5–7 treats the aesthetic manifold as a shared space on which an individual evaluator has a personal metric $g^{(i)}$ (Chapter 9). The empirical results in Chapter 17 are aggregated: we predict *mean Goodreads rating*, which is a population-averaged collapse of many individual metrics. The natural next question is whether we can *separate* the individual from the population: given per-participant aesthetic judgments on a diverse stimulus set, can we fit a personal metric $g^{(i)}$ that predicts held-out judgments by the same participant better than a population-averaged predictor?

Such a study would recruit participants (rough target: $n=300$–$600$), present a curated stimulus set (perhaps 50–100 texts and 50–100 music clips spanning known genre axes and known structural variations), collect ratings on multiple ordinal dimensions — overall aesthetic, emotional intensity, perceived novelty, perceived coherence, willingness-to-recommend — and test whether per-participant Ridge or Gaussian-process models on our four-channel features outperform a participant-agnostic baseline. A positive result would confirm that individual metrics carry information beyond population mean; a null result would suggest (as some aesthetic philosophers would predict) that aesthetic variation is dominated by shared response rather than personal structure.

### C.1.2 Canon-Formation Studies

Chapter 14 argues that canons form through aggregation of geometric-distance structure rather than through voting on scalar quality. The empirical test requires observing canon formation in the small: give participants an initially unfamiliar corpus (contemporary short fiction, or a playlist of lesser-known tracks), ask them to re-encounter the works over weeks, track evolving rankings and discussion-text, and test whether the works that end up "canonized" within the participant group are those whose positions in the aesthetic manifold are centroidal relative to the group's collective metric.

This is longitudinal and therefore expensive ($n\approx 100$ across four to eight weeks, per cohort), and it carries richer ethical weight than a single-session study because the researcher is embedded in the participants' aesthetic-social life for an extended period. Debriefing must include clear communication that the study's aim is descriptive, not prescriptive: we are trying to observe how a small-group canon forms, not to shape what the participants like.

### C.1.3 Cross-Cultural Aesthetic-Judgment Collection

This is the study the framework most obviously invites and where we are most uncomfortable about the ethical terrain. The Phase 3 cross-lingual results use a LaBSE encoder trained on a corpus that, despite its 109 languages, is overwhelmingly dominated by English and by texts whose translations into non-English languages exist because some institution valued them enough to translate. The "cross-lingual invariance" we measure is invariance-as-recovered-by-an-English-biased-encoder, not invariance-in-the-aesthetic-traditions-themselves.

To do better, we would need to collect aesthetic judgments from participants embedded in non-Western traditions — Chinese classical poetry readers, West African oral-epic audiences, Japanese *monogatari* scholars, South Asian *rasa* theorists, Indigenous North American storytelling communities — on works from their own traditions, in their own languages, with their own evaluative vocabularies. The study would need to test whether our four-channel geometric decomposition recovers aesthetic structure that maps onto *their* reported judgments, and where it does not, which dimensions it misses.

We do not imagine this study as one our own lab will run. We imagine it as a collaboration with scholars and communities whose traditions are being asked about. The section below on cultural sensitivity elaborates. We flag this as a research program because the framework calls for it; we do not pretend we are ready to run it responsibly on our own.

### C.1.4 Taste-Drift Longitudinal

If aesthetic judgment has manifold structure and individual metrics, an individual's aesthetic trajectory should be trackable. A person whose taste in literature drifts from YA-romance toward literary fiction over five years should, in our framework, be moving along a particular direction on the aesthetic manifold. A longitudinal study — $n$ on the order of 200, tracked over two to five years, with periodic rating sessions and life-context interviews — could test whether individual taste trajectories are coherent (directional, low-curvature) or random (brownian on the manifold).

This is the most ethically demanding of the four because it is the most invasive. Two-to-five-year engagement is life-scale. Participants need robust withdrawal rights, meaningful understanding of what is being collected and retained, and genuine benefit-sharing from the research output.

## C.2 Institutional Review and Consent

All four programs above require IRB/Research Ethics Committee approval before any data is collected. The specific IRB standards vary by institution and country, but across jurisdictions the baseline requirements are:

- **Informed consent** delivered at enrollment, in language the participant understands, specifying the study's purpose in plain terms, the data to be collected, the duration of retention, the uses to which the data will be put, the identity of who will see it, and the withdrawal procedure.
- **Withdrawal rights** that include the right to withdraw at any point, the right to request deletion of collected data (subject to narrow research-integrity carve-outs), and the right to withdraw without impact on compensation already received for completed sessions.
- **Risk minimization** — for aesthetic-judgment research specifically, most sessions are minimal-risk (rating texts and songs is not harmful), but distress can arise from exposure to emotionally charged content (violence, grief, intimate trauma in the texts) or from self-disclosure during taste-history interviews. A distress protocol and access to a skip-without-penalty option are minimum standards.
- **Fair compensation** that is not coercive. Payments must be enough to respect participants' time but not so high as to induce enrollment against the participants' interests. The line is judgment-dependent and institution-dependent; IRBs will push back either way.
- **Independent ethics review** for anything longitudinal or cross-cultural; single-session laboratory studies can often proceed under an expedited-review track, but taste-drift longitudinals and cross-cultural fieldwork typically require full-board review.

We recommend pre-registration of every study (OSF, AsPredicted, or equivalent) with the specific analysis plan locked before data collection. This is a discipline the framework advocates for itself (Chapter 17 on honest reporting) and it belongs here.

## C.3 Data Minimization

The framework needs participants' aesthetic judgments. It does not need their names, email addresses, home locations, browser fingerprints, social-media handles, or any other identifier beyond what is required for repeated-measures linkage. Data minimization is not a courtesy; it is a structural defense against secondary-use drift.

Specifically:

- Collect the *minimum* demographic information needed to test the hypothesis. If the hypothesis is about cross-cultural variation, age bracket and self-identified cultural-tradition affiliation are the relevant fields; precise birthdate, street address, and employer are not.
- Store the linkage key (the string that maps "participant 47" to a specific individual) separately from the research data, in a compartment with stricter access control than the research compartment itself.
- Age the linkage key. After the study's publication and a predefined post-publication retention period (we suggest 2–5 years for longitudinal, 1 year for single-session), the linkage key is destroyed and the research data becomes permanently anonymized. This is not ethical theater: it is the structural guarantee against future re-identification pressure.
- If any open-data release is planned (we strongly recommend release of anonymized response matrices and of the analysis code), run the release through a re-identification audit. Small-$n$ cross-cultural data is particularly vulnerable because the intersection of "French-speaking resident of city X who prefers Author Y" is often uniquely identifying.

## C.4 Cultural Sensitivity and the Encoder-Bias Problem

This is the section we most want the reader to take seriously.

### C.4.1 The Structural Risk

LaBSE is trained on a corpus that, despite its nominal multilingual coverage, is overwhelmingly English-grounded and Western-canon-weighted. MERT is trained on approximately 160,000 hours of music that, whatever its breadth, was assembled under a particular industry's notion of what music is worth collecting and licensing. PCA bases fit on these encoders' outputs inherit those biases. When we then turn around and use these PCA bases to measure the "aesthetic structure" of a Chinese classical poem, a West African griot performance, an Indigenous Australian songline, or a medieval Arabic *qasida*, we are imposing a Western-trained geometric frame on artifacts whose own evaluative traditions were not represented in the training data.

The Phase 3 result — $\rho \approx 0.7$ invariance across 6 language families — is *consistent with* the claim that aesthetic structure is genuinely universal. It is also consistent with the claim that LaBSE has projected every language into the English-dominant subspace well enough that residual Western-aesthetic-signal is recoverable in any language. We cannot distinguish these two hypotheses from invariance measurements alone. The Sinitic-corpus gap we document in Chapter 17 — only 5 Chinese bundles formed, because Chinese Gutenberg is classical Chinese originals rather than Chinese translations of Western works — is a hint of this: the classical Chinese tradition does not map cleanly into the English PCA basis, and that may be the basis's limitation, not Chinese literature's.

### C.4.2 What Responsible Cross-Cultural Work Requires

We believe responsible extension of this framework to non-Western aesthetic traditions requires at least the following:

- **Collaborative framing.** The study is designed *with* scholars and practitioners of the tradition, not designed by us and then applied to them. Co-authorship, shared framing authority over what the research question is, shared decision rights over how results are interpreted.
- **Tradition-native evaluative vocabulary.** Rating scales, dimension labels, and instructions in the participants' language, using the tradition's own aesthetic vocabulary where applicable. Where Western aesthetic dimensions (novelty, coherence, emotional intensity) do not map cleanly onto the tradition's own (e.g., *rasa*, *yugen*, *duende*), the study should let the tradition's dimensions coexist with, or replace, the imported ones.
- **Refitting the encoder basis when justified.** For traditions where the default encoder demonstrably under-represents the material (classical Chinese is our clearest case), refit the PCA basis on a tradition-native corpus before computing structural features. The Phase 3 headline claim of cross-lingual invariance was made with a shared English-fit basis because that is the specific symmetry we were testing; for cross-cultural judgment collection the methodological question is different and the basis choice should match the question.
- **Benefit-sharing.** Any publishable result must be returned to the participating communities in a usable form — published also in the tradition's language; co-authored with community scholars; data held in ways the community can access. Extractive research — go in, collect, publish, leave — is not acceptable and the framework's universalist ambition makes it particularly tempting, so the guardrails must be explicit.
- **Willingness to not do the study.** If a community declines, or if a study cannot be done with the collaborative structure above, we do not do the study and we do not claim the empirical result. The four-channel framework makes a universal-sounding prediction; we are prepared to leave that prediction empirically unconfirmed in a given tradition rather than produce a non-consensual confirmation.

### C.4.3 The Specific Hazard of Reducing Culturally-Specific Aesthetics to English-Encoder Biases

The hazard we most want to name is the one closest to our own work: the temptation to declare that our framework has "measured the aesthetic structure" of a non-Western tradition, when what we have actually measured is that tradition's shadow in the English-encoder's semantic space. A $\rho$ that looks good in a cross-lingual invariance table can paper over a tradition whose aesthetic axes are genuinely different from the English-weighted ones. If our framework is used as a tool in curation, recommendation, or cultural-heritage evaluation, this hazard becomes practical: downstream systems will propagate the encoder's biases into decisions about which works are deemed "structurally excellent" within a tradition the encoder did not learn from.

We think the mitigation is methodological humility. Report the invariance measurement with the encoder-provenance caveat. Run the basis-refitting check for traditions where the default encoder is suspect. Collaborate with tradition-native scholars before claiming to have measured anything about the tradition. Decline to deploy the framework as a filter in settings where the encoder-bias propagation would materially affect what cultural material reaches what audience.

## C.5 Subject-Level Data Retention

For single-session studies, we recommend retention of identified data for no longer than the duration of data analysis plus a peer-review cycle (typically 2 years from collection), followed by anonymization (destruction of the linkage key) and indefinite retention of the anonymized response matrix for reproducibility. For longitudinal studies, retention must match the study's duration plus a post-completion period agreed with participants at consent.

Encrypted storage at rest; access-controlled compartments; audit logs on access; no copies to personal devices; no cloud storage outside the IRB-approved providers. These are infrastructure requirements that every institutional compliance office will specify; we are not adding to them, we are stating that the framework's human-subjects extensions must satisfy them.

One specific recommendation: separate the *aesthetic-judgment data* from the *demographic/identifier data* in storage, and apply tighter access controls to the latter. Most analyses do not need to see demographics at the per-row level; aggregate summaries are enough. The linkage key should be accessible only to the small subset of personnel who administer repeated-measures sessions, not to the analysts who fit the models.

## C.6 Reporting and Open Science

All human-subjects extensions should be preregistered, report effect sizes with confidence intervals (not just p-values), release anonymized data and analysis code, and include the genre-confound and encoder-bias caveats we have insisted on throughout this volume. Honest negative results are publishable and valuable — a study that shows our framework fails to predict cross-cultural aesthetic judgments in a given tradition is a more important scientific contribution than a study that confirms the framework in a tradition where the confirmation is over-determined by encoder bias.

We specifically recommend that studies in this program adopt the *registered report* format where the journal accepts the protocol before data collection and commits to publishing the result regardless of outcome. This is the strongest defense against publication bias and it aligns with the framework's self-declared empirical standards.

## C.7 What We Will Not Do

To close on the negative: the framework, even extended with the research programs sketched above, is not a basis for the following, and we want this on the record.

- It is not a basis for ranking individuals' aesthetic sophistication. The personal metric $g^{(i)}$ is a description of an individual's evaluative pattern; it does not license "this person has better taste than that person" claims.
- It is not a basis for algorithmic cultural gatekeeping. Using a Western-encoder-derived geometric framework to decide which works are "canonical" in any living tradition is exactly the encoder-bias failure mode C.4.3 names.
- It is not a basis for clinical or diagnostic claims about aesthetic-responsiveness or aesthetic dysfunction. There are no clinical findings in this volume, and the framework is not a clinical instrument.
- It is not a basis for commercial recommendation systems that manipulate users without their awareness. If the framework is deployed in consumer products, its operation and its limitations must be disclosed in terms the user can understand.

The research programs in this appendix are offered in the spirit of open scientific inquiry. They are also offered with a recognition that aesthetic judgment is intimately entangled with personal identity, cultural belonging, and communal meaning, and that any research program that touches it takes on obligations beyond the methodological. We want the framework to be tested — including tested to destruction, in traditions where it fails. We do not want it to be deployed faster than it is understood. These two stances are compatible, and the appendix is meant to keep them in view at the same time.
