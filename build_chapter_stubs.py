"""Generate chapter stub files for the Geometric Aesthetics book.

Each stub contains the outline sub-bullets as the section plan, plus slots
for figures and paper cross-references. Promote sub-bullets to prose as
the chapters mature.

Run once after cloning; idempotent (overwrites existing stubs).
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent / "book"
OUT.mkdir(parents=True, exist_ok=True)


CHAPTERS = [
    (1, "geometry-hiding-in-plain-sight", "The Geometry Hiding in Plain Sight", "I",
     [
         "The universality problem: why do humans across cultures agree (roughly) on what is beautiful?",
         "The two failures of aesthetics (pure subjectivism vs pure objectivism); geometry as the third path",
         "Precedents: Pythagoras, Birkhoff (1933), Fechner (1876), Ramachandran's eight laws (1999)",
         "What's new: high-dim perceptual spaces, manifold learning, info-theoretic formalization, neural coding",
         "The plan: symmetry (Ch. 2), complexity (Ch. 3), compressibility (Ch. 4), then across domains (Parts II-IV), unified theory (Part V)",
     ], [], ["Paper v3 Section I (Introduction)"]),

    (2, "symmetry-and-its-violations", "Symmetry and Its Violations", "I",
     [
         "Symmetry as the baseline: bilateral in faces, rotational in flowers, translational in architecture",
         "The symmetry paradox: perfect symmetry is boring; slight asymmetry is more attractive",
         "Broken symmetry as the source of interest (Noether in physics to meaning in aesthetics)",
         "Group-theoretic formalization: beauty as a representation of a symmetry group with controlled deformations",
         "Weyl's Symmetry (1952) revisited: crystals, ornament, music",
         "The asymmetry budget: how much violation is optimal",
     ],
     ["symmetry_budget.svg"],
     ["Paper v3 Section V (Symmetry as Group-Invariant Utility), Proposition 3"]),

    (3, "complexity-and-the-wundt-curve", "Complexity and the Wundt Curve", "I",
     [
         "Wundt's inverted-U (1874): the most replicated finding in experimental aesthetics",
         "Berlyne's neo-Berlynian framework (1971): arousal potential from novelty, complexity, surprise",
         "Complexity relative to the perceiver's model: same stimulus, different effective dimensionality",
         "Expertise as manifold expansion: the Wundt peak shifts rightward",
         "The peak as a phase transition (beauty at the edge of chaos)",
         "Formalization: optimal K(x | M) neither too low nor too high",
     ],
     ["wundt_curve.svg", "expertise_shift.svg"],
     ["Paper v3 Section IV (Berlyne's Law as Tangency Condition)",
      "Proposition 2 (Expertise expands D_eff)"]),

    (4, "beauty-as-compressibility", "Beauty as Compressibility", "I",
     [
         "The compression thesis: low description length in the natural basis, high in a random basis",
         "Why it works: natural basis = eigenvectors of the learned covariance",
         "PCA-Matryoshka connection: eigenvalues as importance weights; beauty = meaning preserved under compression",
         "Schmidhuber's compression progress theory (2009): beauty is the change in compressibility",
         "Elegance in mathematics: short argument covering vast territory (Euler's identity, Cantor diagonal)",
         "Three levels: symmetry (group invariance), harmony (basis alignment), elegance (compression progress)",
     ],
     ["compression_progress.svg", "preference_manifold.svg"],
     ["Paper v3 Section III (Aesthetic Utility Function)",
      "Paper v3 Section VI (Temporal Aesthetics as Geodesic Ascent)"]),

    (5, "visual-beauty", "Visual Beauty", "II",
     [
         "The visual field as a manifold: retinal images on the natural-image manifold",
         "Gestalt laws as geometric priors: proximity, similarity, continuity, closure",
         "Composition: rule of thirds, golden ratio, Fibonacci spiral",
         "Color harmony in CIE Lab space: complementary = antipodal, analogous = geodesic neighborhoods",
         "Face aesthetics: averageness, symmetry, dimorphism as signed distance from a gender boundary",
         "Abstract art as manifold exploration: Mondrian (restriction), Pollock (random walks), Rothko (low-dim projections)",
     ], [], []),

    (6, "musical-beauty", "Musical Beauty", "II",
     [
         "Pitch as a 1-D manifold with periodic structure (octave equivalence Z/12Z)",
         "Consonance and dissonance: integer ratios, roughness (Plomp and Levelt), cultural exposure",
         "Tymoczko's geometry of music: voice leading as paths on an orbifold",
         "Rhythm as geometry: meter as a lattice, syncopation as lattice violation",
         "Melodic contour as a curve in pitch-time space (tension = curvature)",
         "Musical form as large-scale symmetry: sonata (ABA'), theme and variations, rondo",
         "Why music moves us: emotion as derivative of tension along the harmonic trajectory",
     ], [],
     ["Paper v3 Section VI (Temporal Aesthetics)"]),

    (7, "gustatory-beauty", "Gustatory Beauty", "II",
     [
         "Recap: flavor space from Vol 12 (taste + aroma + trigeminal)",
         "Palatability (innate hedonic peaks) vs culinary beauty (learned appreciation of structure)",
         "The composed dish as a musical chord: superposition in flavor space",
         "Meal progression as a flavor-space trajectory",
         "Wine vocabulary as geometric descriptors (round = smooth curvature; long finish = slow decay)",
         "Universality: same three principles across visual, musical, gustatory",
     ], [], []),

    (8, "tactile-olfactory-kinesthetic", "Tactile, Olfactory, and Kinesthetic Beauty", "II",
     [
         "Texture aesthetics: smoothness as low curvature; uncanny valley of artificial textures",
         "Perfume pyramid (top / middle / base notes) as a trajectory in olfactory space",
         "Dance and movement: curves in body-configuration space",
         "Architectural space: high ceilings liberate the perceived spatial manifold",
         "Haptic aesthetics: beauty in the geometry of function",
     ], [], []),

    (9, "mathematical-beauty", "Mathematical Beauty", "III",
     [
         "Unreasonable effectiveness of mathematical beauty (Hardy, Dirac, Atiyah)",
         "Elegance as compression: Erdos's 'Book'",
         "Surprise as compression progress: Euler's identity, uncountability, continuum hypothesis",
         "Visual proof and geometric intuition",
         "Symmetry in mathematics: group theory as both subject and framework (meta-circular)",
         "Ugliness: four-color theorem's computer proof, classification of finite simple groups",
     ],
     ["compression_progress.svg"],
     ["Paper v3 Section V (Symmetry implies compression)",
      "Paper v3 Section VI Conjecture 1 (Insight as curvature)"]),

    (10, "literary-and-narrative-beauty", "Literary and Narrative Beauty", "III",
     [
         "Narrative as a curve: Vonnegut's shape of stories",
         "Poetic form as symmetry; free verse as broken symmetry",
         "Metaphor as geometric mapping (Lakoff and Johnson conceptual metaphor theory)",
         "Plot topology: hero's journey (loop), tragedy (non-closing), comedy (unexpected closure)",
         "Style as basis transformation: Hemingway vs Faulkner",
         "Shklovsky's defamiliarization as effective-dimensionality increase",
     ], [], []),

    (11, "beauty-of-justice", "The Beauty of Justice and Moral Aesthetics", "III",
     [
         "Fairness as symmetry: the veil of ignorance (Rawls) as a symmetry operation",
         "Elegance of legal arguments: precedent as compression; landmark rulings as compression progress",
         "Moral beauty: selfless courage and graceful forgiveness as symmetry where asymmetry was expected",
         "Institutional design: simple rules producing rich coherent behavior",
         "Connection to Vol 4: equilibria that feel elegant vs kludgy",
     ], [], []),

    (12, "the-aesthetic-brain", "The Aesthetic Brain", "IV",
     [
         "Common neural currency: OFC responds to beauty across visual, musical, mathematical domains",
         "Chatterjee's aesthetic triad (2014): sensation, meaning, emotion",
         "Reward prediction error as compression progress signal (dopamine as the 'aha' of beauty)",
         "DMN activation during aesthetic contemplation",
         "Neuroaesthetics of expertise: expanded manifold, shifted peak, new discriminable dimensions",
         "Limits of neuroaesthetics: beauty in the relationship, not in the substrate alone",
     ], [], []),

    (13, "the-cultural-manifold", "The Cultural Manifold", "IV",
     [
         "Innate substrate: cross-cultural preferences in infants (symmetry, moderate complexity)",
         "Cultural learning as manifold deformation",
         "Mere-exposure effect as gradient descent on the aesthetic manifold",
         "Fashion cycles as oscillations on the manifold (novelty vs familiarity)",
         "Artistic revolutions as phase transitions (impressionism, atonality, cubism)",
         "Global aesthetic: universal manifold or higher-dim space with cultural submanifolds?",
     ],
     ["expertise_shift.svg"],
     []),

    (14, "the-three-principles", "The Three Principles", "V",
     [
         "Principle 1: symmetry with controlled violation (the asymmetry budget)",
         "Principle 2: compressibility in the natural basis (the PCA-Matryoshka insight)",
         "Principle 3: compression progress - the 'aha' of beauty as discovery of a new eigenvalue",
         "Unification: three timescales (instantaneous, learned, dynamic) of the same geometric phenomenon",
     ],
     ["symmetry_budget.svg", "preference_manifold.svg", "compression_progress.svg"],
     ["Paper v3 Sections VI-VII (unified theory)"]),

    (15, "beauty-across-the-series", "Beauty Across the Series", "V",
     [
         "Geometric Reasoning (Vol 3): valid inference as symmetry preservation",
         "Geometric Economics (Vol 4): beautiful mechanisms = simple rules producing complex desired behavior",
         "Geometric Law (Vol 5): justice as aesthetic symmetry",
         "Geometric Cognition (Vol 6): the feeling of understanding as compression progress",
         "Geometric Gastronomy (Vol 12): flavor harmony as basis compression",
         "Meta-principle: every domain in the series has an aesthetic dimension, and it is always geometric",
     ], [], []),

    (16, "open-questions", "Open Questions and Future Directions", "V",
     [
         "Can aesthetic quality be computed? The compression thesis suggests a metric; the perceiver's basis is private",
         "Artificial aesthetics: can AI develop genuine preferences, or only simulate?",
         "Evolution of beauty: fitness signaling, efficient perception, social bonding, or all three?",
         "Ethics of aesthetic manipulation: advertising as aesthetic-manifold deformation",
         "Limits of geometry: the sublime (Kant), the numinous (Otto), the tragic",
     ], [], []),
]


def render(n, slug, title, part, bullets, figures, refs):
    fig_lines = "\n".join(f"- [{f}](../figures/{f})" for f in figures) \
        if figures else "*(none yet - figure slots open)*"
    ref_lines = "\n".join(f"- {r}" for r in refs) \
        if refs else "*(none yet - chapter sits above the paper's formalization)*"
    section_plan = "\n".join(f"{n}.{i + 1}. {b}" for i, b in enumerate(bullets))
    return f"""# Chapter {n}: {title}

> Part {part} of *Geometric Aesthetics* - Volume 7 of the Geometric Series

**Draft status:** outline

## Section plan

{section_plan}

## Key figures

{fig_lines}

## Paper cross-references

{ref_lines}

## Draft

*To be written - promote sub-bullets above into full prose, weaving in the
paper's theorems and the key references from [OUTLINE.md](../OUTLINE.md).*
"""


def main():
    for n, slug, title, part, bullets, figures, refs in CHAPTERS:
        path = OUT / f"chapter-{n:02d}-{slug}.md"
        path.write_text(
            render(n, slug, title, part, bullets, figures, refs),
            encoding="utf-8",
        )
        print(f"  wrote {path.name}")
    print(f"{len(CHAPTERS)} chapter stubs generated.")


if __name__ == "__main__":
    main()
