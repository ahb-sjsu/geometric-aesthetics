"""Figures for Geometric Aesthetics (Volume 13), Chapters 1 to 30 and Appendix B.

Measured numbers come only from book/src/_BOOK_REFERENCE.md ("Verified Empirical Findings"),
Chapter 17 and Appendix F, and each is asserted against the value printed in the chapter.
Nothing on the "Unresolved" list of CORRECTIONS-2026-11-26.md is drawn. Schematic figures use
illustrative values that their captions state.
"""

import heapq
import math
import random

from figkit import (
    BORDER, BOX, CRITICAL, GRID, INK, INK2, INK3, SERIES, SURFACE, Axes, Canvas, legend, reg,
)

SRC = "book/src/"
APP = "book/src/appendices/"


# ------------------------------------------------------------------ helpers
def _ch(n):
    names = {
        1: "chapter-01-introduction-why-geometry.md",
        2: "chapter-02-the-failure-of-scalar-aesthetics.md",
        3: "chapter-03-historical-precursors-geometry-before-geometry.md",
        4: "chapter-04-mathematical-preliminaries.md",
        5: "chapter-05-the-aesthetic-manifold.md",
        6: "chapter-06-the-tensor-hierarchy.md",
        7: "chapter-07-one-work-five-levels.md",
        8: "chapter-08-stratification-boundaries-thresholds-phase-transitions.md",
        9: "chapter-09-origin-of-the-aesthetic-metric.md",
        10: "chapter-10-aesthetic-dynamics-parallel-transport-style-holonomy.md",
        11: "chapter-11-aesthetic-reasoning-as-optimal-search.md",
        12: "chapter-12-noethers-theorem-for-aesthetics.md",
        13: "chapter-13-quantum-aesthetic-dynamics-superposition-measurement.md",
        14: "chapter-14-collective-aesthetic-agency-canon-and-emergence.md",
        15: "chapter-15-from-tensor-to-judgment.md",
        16: "chapter-16-aesthetic-uncertainty-and-the-limits-of-geometric-determinacy.md",
        17: "chapter-17-empirical-evidence-for-geometric-aesthetics.md",
        18: "chapter-18-geometric-aesthetics-for-artificial-agents.md",
        19: "chapter-19-deme-architecture-for-aesthetics.md",
        20: "chapter-20-geometric-literary-criticism.md",
        21: "chapter-21-geometric-musicology.md",
        22: "chapter-22-geometric-film-and-television.md",
        23: "chapter-23-geometric-visual-art.md",
        24: "chapter-24-geometric-architecture.md",
        25: "chapter-25-geometric-game-aesthetics.md",
        26: "chapter-26-geometric-ai-curation.md",
        27: "chapter-27-geometric-fashion-and-product-design.md",
        28: "chapter-28-geometric-everyday-aesthetics.md",
        29: "chapter-29-open-problems.md",
        30: "chapter-30-conclusion-the-geometry-of-beauty.md",
    }
    return SRC + names[n]


def _close(a, b, tol=1e-9):
    return abs(a - b) <= tol


def _poly(c, pts, fill="none", stroke=INK2, width=1.5, opacity=1.0, dash=None, title=None):
    d = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
    da = f' stroke-dasharray="{dash}"' if dash else ""
    t = f"<title>{title}</title>" if title else ""
    c.add(f'<polygon points="{d}" fill="{fill}" fill-opacity="{opacity}" stroke="{stroke}" '
          f'stroke-width="{width}" stroke-linejoin="round"{da}>{t}</polygon>')


def _dashpoly(c, pts, stroke, width=1.5, dash="5 4"):
    d = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
    c.add(f'<polyline points="{d}" fill="none" stroke="{stroke}" stroke-width="{width}" '
          f'stroke-dasharray="{dash}" stroke-linejoin="round" stroke-linecap="round"/>')


def _circle(c, x, y, r, stroke, fill="none", width=1.5, opacity=1.0, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    c.add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{fill}" fill-opacity="{opacity}" '
          f'stroke="{stroke}" stroke-width="{width}"{da}/>')


def _rect(c, x, y, w, h, fill="none", stroke="none", width=1.0, opacity=1.0, rx=0, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    c.add(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx}" fill="{fill}" '
          f'fill-opacity="{opacity}" stroke="{stroke}" stroke-width="{width}"{da}/>')


def _hbar(c, x0, y, w, h, fill, title=None):
    """Horizontal bar from x0, signed width w, rounded at the data end."""
    if w >= 0:
        c.hrect(x0, y, max(w, 0.5), h, fill, title=title)
        return
    w = -w
    r = min(4, h / 2, w)
    x = x0 - w
    d = (f"M{x0:.2f},{y:.2f} L{x + r:.2f},{y:.2f} Q{x:.2f},{y:.2f} {x:.2f},{y + r:.2f} "
         f"L{x:.2f},{y + h - r:.2f} Q{x:.2f},{y + h:.2f} {x + r:.2f},{y + h:.2f} L{x0:.2f},{y + h:.2f} Z")
    t = f"<title>{title}</title>" if title else ""
    c.add(f'<path d="{d}" fill="{fill}">{t}</path>')


def _vbar(c, x, y_base, y_top, w, fill, title=None):
    """Vertical bar between a baseline and a data end, rounded at the data end (up or down)."""
    if y_top <= y_base:
        c.rect(x, y_top, w, y_base - y_top, fill, title=title)
        return
    h = y_top - y_base
    r = min(4, w / 2, h)
    d = (f"M{x:.2f},{y_base:.2f} L{x:.2f},{y_top - r:.2f} Q{x:.2f},{y_top:.2f} {x + r:.2f},{y_top:.2f} "
         f"L{x + w - r:.2f},{y_top:.2f} Q{x + w:.2f},{y_top:.2f} {x + w:.2f},{y_top - r:.2f} L{x + w:.2f},{y_base:.2f} Z")
    t = f"<title>{title}</title>" if title else ""
    c.add(f'<path d="{d}" fill="{fill}">{t}</path>')


def _gauss_cloud(n, seed, cx, cy, sx, sy, rho=0.0):
    rnd = random.Random(seed)
    pts = []
    for _ in range(n):
        a, b = rnd.gauss(0, 1), rnd.gauss(0, 1)
        x = cx + sx * a
        y = cy + sy * (rho * a + math.sqrt(1 - rho * rho) * b)
        pts.append((x, y))
    return pts


def _mean_cov(pts):
    n = len(pts)
    mx = sum(p[0] for p in pts) / n
    my = sum(p[1] for p in pts) / n
    sxx = sum((p[0] - mx) ** 2 for p in pts) / (n - 1)
    syy = sum((p[1] - my) ** 2 for p in pts) / (n - 1)
    sxy = sum((p[0] - mx) * (p[1] - my) for p in pts) / (n - 1)
    return (mx, my), (sxx, sxy, syy)


def _eig2(sxx, sxy, syy):
    """Eigen-decomposition of a symmetric 2x2: returns (l1, l2, angle of the l1 axis in radians)."""
    tr, det = sxx + syy, sxx * syy - sxy * sxy
    disc = math.sqrt(max(tr * tr / 4 - det, 0.0))
    l1, l2 = tr / 2 + disc, tr / 2 - disc
    ang = 0.5 * math.atan2(2 * sxy, sxx - syy)
    return l1, l2, ang


def _chol(sxx, sxy, syy):
    a = math.sqrt(sxx)
    b = sxy / a
    d = math.sqrt(syy - b * b)
    return a, b, d  # L = [[a, 0], [b, d]]


def _cov_ellipse(c, X, Y, mean, cov, k, stroke, fill="none", opacity=0.0, width=1.5):
    """k-standard-deviation ellipse of a 2x2 covariance, drawn with axis maps X, Y (equal scale)."""
    l1, l2, ang = _eig2(*cov)
    sx = X(1) - X(0)
    c.ellipse(X(mean[0]), Y(mean[1]), k * math.sqrt(l1) * sx, k * math.sqrt(l2) * sx,
              -math.degrees(ang), stroke, fill, width, opacity)


# ------------------------------------------------------------------ chapter 1
def fig_1_1():
    a = (5.8, 0.0)
    b = (0.0, 5.8)
    w = (1 / math.sqrt(2), 1 / math.sqrt(2))
    sa = a[0] * w[0] + a[1] * w[1]
    sb = b[0] * w[0] + b[1] * w[1]
    assert _close(a[0] * b[0] + a[1] * b[1], 0.0)
    assert _close(sa, sb) and round(sa, 1) == 4.1
    p = reg(_ch(1), "1.1",
            "Two illustrative work profiles on two qualities the chapter names, structure and emotional warmth, "
            "in arbitrary units. Work A is structurally brilliant and emotionally cold; work B is warm and "
            "structurally loose. The two are orthogonal, yet their shadows on a reader-weight axis at 45 degrees "
            "are equal, 4.1, the rating of the chapter's example. Every profile on the dashed line casts the same "
            "shadow, so the rating cannot tell the works apart.",
            "### Failure 3: Canon Formation {#failure-3-canon-formation}")
    c = Canvas(720, 400, "Two orthogonal works, one shadow on the reader's axis")
    ox, oy, k = 100, 345, 40
    X = lambda u: ox + k * u
    Y = lambda v: oy - k * v
    c.line(ox, oy, X(7.0), oy, GRID, 1)
    c.line(ox, oy, ox, Y(7.0), GRID, 1)
    c.text(X(7.0), oy + 18, "structure", 11.5, "end", INK2)
    c.text(ox - 14, Y(3.5), "emotional warmth", 11.5, "middle", INK2, rotate=-90)
    # reader-weight axis
    c.line(ox, oy, X(7.2 * w[0]), Y(7.2 * w[1]), INK3, 1.5)
    c.text(X(7.2 * w[0]) + 6, Y(7.2 * w[1]) - 2, "reader-weight axis w", 11, "start", INK2, italic=True)
    # the iso-shadow line through A and B
    c.line(X(a[0]), Y(a[1]), X(b[0]), Y(b[1]), INK3, 1.5, dash="5 4")
    mx, my = (X(sa * w[0]) + X(a[0])) / 2 + 9, (Y(sa * w[1]) + Y(a[1])) / 2 - 9
    c.text(mx, my, "same shadow along this line", 10.5, "middle", INK2, italic=True, rotate=45)
    # the work vectors
    c.arrow(ox, oy, X(a[0]), Y(a[1]), SERIES[0], 2.5)
    c.arrow(ox, oy, X(b[0]), Y(b[1]), SERIES[1], 2.5)
    c.text(X(a[0]) + 6, Y(a[1]) - 10, "work A", 12, "start", INK, "600")
    c.text(X(b[0]) + 10, Y(b[1]) + 4, "work B", 12, "start", INK, "600")
    # right angle mark
    c.line(ox + 12, oy, ox + 12, oy - 12, INK3, 1)
    c.line(ox, oy - 12, ox + 12, oy - 12, INK3, 1)
    # the shared shadow
    px, py = X(sa * w[0]), Y(sa * w[1])
    c.dot(px, py, CRITICAL, 5, title="shadow 4.1")
    c.text(px - 12, py + 4, "shadow 4.1", 11, "end", INK)
    x0 = 430
    c.text(x0, 110, "A: strong structure, emotionally cold", 11.5, "start", INK2)
    c.text(x0, 132, "B: emotionally warm, loose structure", 11.5, "start", INK2)
    c.text(x0, 166, "A and B are orthogonal (90 degrees)", 11.5, "start", INK2)
    c.text(x0, 200, "shadow = w · profile", 11.5, "start", INK2, italic=True)
    c.text(x0, 222, f"A: {sa:.1f}    B: {sb:.1f}", 11.5, "start", INK)
    c.text(x0, 256, "the rating sees only the shadow", 11.5, "start", INK2)
    c.text(16, 390, "illustrative profiles, arbitrary units", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 2
def fig_2_1():
    narrow = [0.0, 0.05, 0.20, 0.65, 0.10]
    divided = [0.15, 0.15, 0.05, 0.05, 0.60]
    def stats(pr):
        m = sum((i + 1) * q for i, q in enumerate(pr))
        v = sum((i + 1) ** 2 * q for i, q in enumerate(pr)) - m * m
        return m, math.sqrt(v)
    m1, s1 = stats(narrow)
    m2, s2 = stats(divided)
    assert _close(sum(narrow), 1.0) and _close(sum(divided), 1.0)
    assert _close(m1, 3.8) and _close(m2, 3.8)
    p = reg(_ch(2), "2.1",
            f"Two illustrative distributions of 1-to-5-star ratings built to the chapter's description, each with "
            f"mean exactly 3.8. On the left most readers give 3 or 4 stars (standard deviation {s1:.2f}). On the "
            f"right 60% give 5 stars and 30% give 1 or 2 (standard deviation {s2:.2f}). The mean is the same, and "
            f"even mean and variance together do not say which quality divides the readers. Bars are the share of "
            f"readers at each rating.",
            "## Failure 3: Regime Collapse {#failure-3-regime-collapse}")
    c = Canvas(720, 400, "Same mean, 3.8 stars: two different shapes of disagreement")
    for j, (pr, name, sd, x0) in enumerate(((narrow, "consensus", s1, 90), (divided, "divided", s2, 420))):
        ax = Axes(c, x0, 76, 250, 250, (0.5, 5.5), (0, 0.72), [], [0, 0.2, 0.4, 0.6] if j == 0 else [], "stars",
                  "share of readers" if j == 0 else "")
        if j == 1:
            for v in (0.2, 0.4, 0.6):
                c.line(ax.x0, ax.Y(v), ax.x0 + ax.w, ax.Y(v), GRID, 1)
        for i, q in enumerate(pr):
            xc = ax.X(i + 1)
            c.text(xc, ax.y0 + ax.h + 16, str(i + 1), 11, "middle", INK2)
            if q > 0:
                c.rect(xc - 12, ax.Y(q), 24, ax.Y(0) - ax.Y(q), SERIES[j], title=f"{i + 1} stars: {q:.0%}")
            c.text(xc, ax.Y(q) - 6, f"{q:.0%}", 10.5, "middle", INK)
        xm, yb = ax.X(3.8), ax.y0 + ax.h
        _poly(c, [(xm, yb + 1), (xm - 4, yb + 7), (xm + 4, yb + 7)], CRITICAL, CRITICAL, 1, 1.0,
              title="mean 3.8")
        c.text(x0 + 125, 52, f"{name}: mean 3.8", 12, "middle", INK, "600")
        c.text(x0 + 125, 68, f"standard deviation {sd:.2f}", 11.5, "middle", INK2)
    c.text(16, 390, "illustrative distributions, each with mean exactly 3.8 (marked by the triangle)", 10.5, "start",
           INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 3
def fig_3_1():
    p = reg(_ch(3), "3.1",
            "Birkhoff's evaluation plane as the chapter reads it: complexity C across, order O up. Each ray from the "
            "origin is a set of objects with the same aesthetic measure M = O / C, drawn for M = 0.5, 1 and 2. The two "
            "illustrative objects a and b differ in both coordinates yet lie on the same ray and receive the same "
            "M = 1. The ratio is one choice of contraction of the plane back to a single number.",
            "## Information-Theoretic Aesthetics: Bense, Moles, and the Shannon Turn "
            "{#information-theoretic-aesthetics-bense-moles-and-the-shannon-turn}")
    c = Canvas(720, 400, "Birkhoff's M = O/C: a plane contracted back to one number")
    ax = Axes(c, 80, 52, 380, 290, (0, 10), (0, 10), [0, 2, 4, 6, 8, 10], [0, 2, 4, 6, 8, 10],
              "complexity C", "order O")
    for j, m in enumerate((0.5, 1.0, 2.0)):
        ce = min(10.0, 10.0 / m)
        c.line(ax.X(0), ax.Y(0), ax.X(ce), ax.Y(m * ce), SERIES[j], 2)
        cl = 4.5 if m == 2.0 else 9.0
        c.text(ax.X(cl) - 12, ax.Y(m * cl) + 4 - (8 if m == 0.5 else 0), f"M = {m:g}", 11, "end", INK)
    pa, pb = (2.0, 2.0), (8.0, 8.0)
    assert _close(pa[1] / pa[0], pb[1] / pb[0])
    for (cc, oo), lab in ((pa, "a"), (pb, "b")):
        c.dot(ax.X(cc), ax.Y(oo), INK, 5, title=f"{lab}: C {cc:g}, O {oo:g}, M {oo / cc:g}")
        c.text(ax.X(cc) - 9, ax.Y(oo) - 9, lab, 12, "end", INK, "600")
    x0 = 500
    c.text(x0, 96, "a: a simple object", 11.5, "start", INK2)
    c.text(x0, 114, "C = 2, O = 2", 11.5, "start", INK2)
    c.text(x0, 146, "b: an ornate object", 11.5, "start", INK2)
    c.text(x0, 164, "C = 8, O = 8", 11.5, "start", INK2)
    c.text(x0, 200, "both: M = O / C = 1", 11.5, "start", INK)
    c.text(x0, 236, "the point (C, O) is two numbers;", 11.5, "start", INK2, italic=True)
    c.text(x0, 254, "M keeps one of them", 11.5, "start", INK2, italic=True)
    c.text(16, 390, "objects a and b are illustrative", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 4
def fig_4_1():
    def kl(mu, s):
        return 0.5 * (s * s + mu * mu - 1 - math.log(s * s))

    def h2(mu, s):
        return 1 - math.sqrt(2 * s / (1 + s * s)) * math.exp(-mu * mu / (4 * (1 + s * s)))

    ka, ha = kl(1, 1), h2(1, 1)
    kb, hb = kl(0, 2), h2(0, 2)
    assert _close(ka, 0.5) and round(ha, 3) == 0.118
    assert round(kb, 3) == 0.807
    # the chapter prints H^2 ~ 0.056 for (mu = 0, sigma = 2); its own formula gives 0.106
    assert round(hb, 3) == 0.106
    p = reg(_ch(4), "4.1",
            "The chapter's worked example, prior N(0, 1). Each curve plots a family of perturbations by its KL "
            "divergence from the prior (across) and its squared Hellinger distance (up), both from the chapter's "
            "closed forms. The upper curve shifts the mean with σ = 1; the lower curve widens the spread with "
            f"μ = 0. The shift μ = 1 has KL 0.5 and H² {ha:.3f}; doubling the standard deviation has KL {kb:.3f} "
            f"and H² {hb:.3f}. KL ranks the spread change as the larger, Hellinger the mean shift.",
            "### Why All Six")
    c = Canvas(720, 400, "KL and Hellinger rank the same two perturbations differently")
    ax = Axes(c, 80, 52, 500, 280, (0, 1.2), (0, 0.25), [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2],
              [0, 0.05, 0.1, 0.15, 0.2, 0.25], "KL divergence from the prior", "squared Hellinger distance")
    mus = [1.517 * i / 120 for i in range(121)]
    c.polyline([(ax.X(kl(m, 1)), ax.Y(h2(m, 1))) for m in mus], SERIES[0], 2, title="mean shift, sigma = 1")
    sig = [1 + 1.24 * i / 120 for i in range(121)]
    sig = [s for s in sig if kl(0, s) <= 1.2]
    c.polyline([(ax.X(kl(0, s)), ax.Y(h2(0, s))) for s in sig], SERIES[1], 2, title="spread change, mu = 0")
    c.text(ax.X(kl(1.517, 1)) + 8, ax.Y(h2(1.517, 1)) + 4, "mean shift", 11, "start", INK2)
    c.text(ax.X(kl(0, sig[-1])) + 8, ax.Y(h2(0, sig[-1])) + 4, "spread change", 11, "start", INK2)
    for kx, hy in ((ka, ha), (kb, hb)):
        c.line(ax.X(0), ax.Y(hy), ax.X(kx), ax.Y(hy), INK3, 1, dash="3 3")
        c.line(ax.X(kx), ax.Y(0), ax.X(kx), ax.Y(hy), INK3, 1, dash="3 3")
    c.dot(ax.X(ka), ax.Y(ha), SERIES[0], 5, title="mu = 1, sigma = 1")
    c.dot(ax.X(kb), ax.Y(hb), SERIES[1], 5, title="mu = 0, sigma = 2")
    c.text(ax.X(ka) - 10, ax.Y(ha) - 12, f"μ = 1: KL 0.5, H² {ha:.3f}", 11, "end", INK)
    c.text(ax.X(kb) + 10, ax.Y(hb) + 20, f"σ = 2: KL {kb:.3f}, H² {hb:.3f}", 11, "start", INK)
    legend(c, 80, 40, [("mean shift, σ = 1", SERIES[0]), ("spread change, μ = 0", SERIES[1])])
    c.save(p)


def fig_4_2():
    A = ((1.0, 0.3), (0.3, 0.8))
    b = (1.6, 0.75)
    t = 1.0

    def loss(x, y):
        dx, dy = x - b[0], y - b[1]
        return A[0][0] * dx * dx + 2 * A[0][1] * dx * dy + A[1][1] * dy * dy

    n = 40000
    l1 = []
    for i in range(n):
        s = 4 * i / n
        if s < 1:
            pt = (1 - s, s)
        elif s < 2:
            pt = (-(s - 1), 1 - (s - 1))
        elif s < 3:
            pt = (-(1 - (s - 2)), -(s - 2))
        else:
            pt = (s - 3, -(1 - (s - 3)))
        l1.append(pt)
    b1 = min(l1, key=lambda q: loss(*q))
    l2 = [(t * math.cos(2 * math.pi * i / n), t * math.sin(2 * math.pi * i / n)) for i in range(n)]
    b2 = min(l2, key=lambda q: loss(*q))
    assert abs(b1[0] - 1.0) < 1e-3 and abs(b1[1]) < 1e-3          # a corner: beta2 = 0 exactly
    assert b2[0] > 0.2 and b2[1] > 0.2                              # both non-zero on the disc
    p = reg(_ch(4), "4.2",
            "Two coefficients, an illustrative quadratic loss whose level curves are the ellipses (centred on the "
            "unpenalized fit), and the same budget, 1, for each penalty. Inside the ℓ1 diamond the smallest loss is "
            "reached at a corner, where β2 = 0 exactly. Inside the ℓ2 disc it is reached at a point where both "
            f"coefficients are non-zero, here ({b2[0]:.2f}, {b2[1]:.2f}). This is the sparsity the chapter relies on "
            "to select axes.",
            "### Why Lasso Is Load-Bearing Here")
    c = Canvas(720, 400, "Why the ℓ1 penalty sets coefficients exactly to zero")
    l1v, l2v, ang = _eig2(A[0][0], A[0][1], A[1][1])
    subs = ("optimum at a corner: β2 = 0", f"optimum ({b2[0]:.2f}, {b2[1]:.2f}): both non-zero")
    for k, (x0, name, best, shape) in enumerate(((60, "ℓ1 budget (Lasso)", b1, "diamond"),
                                                  (400, "ℓ2 budget (ridge)", b2, "disc"))):
        y0, size, lo, hi = 80, 270, -1.4, 2.9
        X = lambda u, x0=x0: x0 + size * (u - lo) / (hi - lo)
        Y = lambda v: y0 + size * (1 - (v - lo) / (hi - lo))
        cid = f"clip42_{k}"
        c.add(f'<defs><clipPath id="{cid}"><rect x="{x0}" y="{y0}" width="{size}" height="{size}"/></clipPath></defs>')
        c.line(X(lo), Y(0), X(hi), Y(0), GRID, 1)
        c.line(X(0), Y(lo), X(0), Y(hi), GRID, 1)
        c.text(X(hi), Y(0) + 16, "β1", 11.5, "end", INK2)
        c.text(X(0) + 8, Y(hi) + 12, "β2", 11.5, "start", INK2)
        col = SERIES[0] if k == 0 else SERIES[2]
        if shape == "diamond":
            _poly(c, [(X(1), Y(0)), (X(0), Y(1)), (X(-1), Y(0)), (X(0), Y(-1))], col, col, 2, 0.18)
        else:
            _circle(c, X(0), Y(0), X(1) - X(0), col, col, 2, 0.18)
        lstar = loss(*best)
        sc = X(1) - X(0)
        c.add(f'<g clip-path="url(#{cid})">')
        for f in (0.35, 1.0):
            c.ellipse(X(b[0]), Y(b[1]), math.sqrt(f * lstar / l1v) * sc, math.sqrt(f * lstar / l2v) * sc,
                      -math.degrees(ang), INK3, "none", 1.5)
        c.add("</g>")
        c.dot(X(b[0]), Y(b[1]), INK2, 3.5, title="unpenalized fit")
        c.dot(X(best[0]), Y(best[1]), CRITICAL, 5, title=f"constrained optimum ({best[0]:.2f}, {best[1]:.2f})")
        c.text(x0 + size / 2, 52, name, 12, "middle", INK, "600")
        c.text(x0 + size / 2, 69, subs[k], 11, "middle", INK2)
    c.text(16, 390, "illustrative loss; ellipses: two of its level curves, centred on the unpenalized fit (small dot)",
           10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 5
def fig_5_1():
    mu = 1.0

    def fwd(s):
        return 0.5 * (s * s + mu * mu - 1 - math.log(s * s))

    def rev(s):
        return 0.5 * (1 / (s * s) + mu * mu / (s * s) - 1 + math.log(s * s))

    assert _close(fwd(1), 0.5) and _close(rev(1), 0.5)
    p = reg(_ch(5), "5.1",
            "The two directions of the KL divergence of Chapter 4 for a prior N(0, 1) and a work N(1, σ²), against "
            "the work's standard deviation σ. The chapter reads KL(work ‖ prior) as how surprising the work is under "
            "the prior (novelty) and KL(prior ‖ work) as how far the prior would have to be updated to accommodate "
            "the work (influence). They are equal, 0.5, only at σ = 1; for a narrow work the update is the larger, "
            "for a broad work the surprise.",
            "## 5.7 The Per-Work Gaussian Is an Approximation {#5-7-approximation}")
    c = Canvas(720, 400, "The two directions of KL: novelty and required update")
    ax = Axes(c, 70, 52, 560, 280, (0.4, 2.5), (0, 5), [0.5, 1, 1.5, 2, 2.5], [0, 1, 2, 3, 4, 5],
              "standard deviation σ of the work (prior: σ = 1, mean 0; work mean 1)", "KL divergence, nats")
    ss = [0.4 + 2.1 * i / 200 for i in range(201)]
    c.polyline([(ax.X(s), ax.Y(fwd(s))) for s in ss], SERIES[0], 2, title="KL(work || prior)")
    c.polyline([(ax.X(s), ax.Y(min(rev(s), 5))) for s in ss if rev(s) <= 5], SERIES[1], 2, title="KL(prior || work)")
    c.dot(ax.X(1), ax.Y(0.5), INK, 4.5, title="equal at sigma = 1")
    c.text(ax.X(1) - 10, ax.Y(0.5) + 20, "equal at σ = 1: 0.5", 11, "end", INK)
    c.text(ax.X(0.62), ax.Y(3.9), "narrow work: the update is larger", 11, "start", INK2, italic=True)
    c.text(ax.X(1.62), ax.Y(2.75), "broad work: the surprise is larger", 11, "start", INK2, italic=True)
    legend(c, 70, 40, [("KL(work ‖ prior): novelty", SERIES[0]), ("KL(prior ‖ work): update", SERIES[1])])
    c.save(p)


def fig_5_2():
    uni = _gauss_cloud(80, 21, 0.0, 0.0, 1.0, 0.75, 0.45)
    rnd = random.Random(5)
    raw = []
    for i in range(80):
        cx, cy = ((1.6, 0.6) if i % 2 == 0 else (-1.6, -0.6))
        raw.append((cx + rnd.gauss(0, 0.22), cy + rnd.gauss(0, 0.22)))
    mu_u, cov_u = _mean_cov(uni)
    mu_b, cov_b = _mean_cov(raw)
    au, bu, du = _chol(*cov_u)
    ab, bb, db = _chol(*cov_b)
    bim = []
    for x, y in raw:
        zx = (x - mu_b[0]) / ab                      # L_b^{-1}(x - mu_b)
        zy = (y - mu_b[1] - bb * zx) / db
        bim.append((mu_u[0] + au * zx, mu_u[1] + bu * zx + du * zy))
    mu2, cov2 = _mean_cov(bim)
    assert all(abs(a - b) < 1e-9 for a, b in zip(mu_u + cov_u, mu2 + cov2))
    lim = 3.0
    assert all(abs(x) < lim and abs(y) < lim for x, y in uni + bim)
    p = reg(_ch(5), "5.2",
            "Two illustrative clouds of 80 points in a two-dimensional embedding. The left is one wide cluster. The "
            "right is two tight clusters, transformed so that its mean and covariance equal the left cloud's "
            "exactly. Both are fitted by the same Gaussian, whose 2-standard-deviation ellipse is drawn on each, so "
            "every first- and second-moment quantity agrees. The chapter assigns the difference to the higher levels "
            "of Chapter 6.",
            "## 5.8 Foreshadow — The Four Channels {#5-8-four-channels}")
    c = Canvas(720, 400, "Two different clouds, one fitted Gaussian")
    for k, (pts, name, x0) in enumerate(((uni, "one wide cluster", 80), (bim, "two tight clusters", 410))):
        size, y0 = 270, 62
        X = lambda u, x0=x0: x0 + size * (u + lim) / (2 * lim)
        Y = lambda v: y0 + size * (1 - (v + lim) / (2 * lim))
        _rect(c, x0, y0, size, size, stroke=GRID, width=1)
        c.line(X(-lim), Y(0), X(lim), Y(0), GRID, 1)
        c.line(X(0), Y(-lim), X(0), Y(lim), GRID, 1)
        _cov_ellipse(c, X, Y, mu_u, cov_u, 2, SERIES[2], SERIES[2], 0.08, 2)
        for x, y in pts:
            c.dot(X(x), Y(y), SERIES[k], 3)
        c.dot(X(mu_u[0]), Y(mu_u[1]), INK, 4, title="common mean")
        c.text(x0 + size / 2, y0 + size + 22, name, 12, "middle", INK, "600")
    c.text(16, 390, "illustrative points; same mean and covariance (checked to 1e-9)", 10.5, "start", INK3, italic=True)
    legend(c, 470, 390, [("fitted Gaussian, 2 SD", SERIES[2])], 10.5)
    c.save(p)


# ------------------------------------------------------------------ chapter 6
def fig_6_1():
    p = reg(_ch(6), "6.1",
            "The tensor hierarchy as the chapter defines it, computed from one work's embedding cloud. Levels 1, 2 "
            "and 4 treat the cloud as an unordered set; Level 3 alone uses the order of the units; Level 4 alone is "
            "fitted to a reception target. The linear contraction of §6.6 maps all four levels to the scalar of "
            "Level 0, and no map runs back. In the books experiment 71 of the 128 axes receive non-zero Lasso weight.",
            "## 6.7 Why Each Level Is Irreducible to the Others {#6-7-irreducibility}")
    c = Canvas(720, 460, "Four levels from one cloud, contracted to one scalar")
    c.box(20, 196, 110, 60, "work W", "units t1 … tN")
    c.box(160, 196, 120, 60, "cloud X(W)", "encoder φ")
    c.arrow(130, 226, 158, 226, INK2, 1.5)
    levels = [("Level 1: mean displacement", "as a set: δ = μ̂ − μ0"),
              ("Level 2: covariance Σ̂", "as a set: divergences, pair_sim"),
              ("Level 3: ordered steps Δn", "in order: step_mean, recur_rate"),
              ("Level 4: learned axes", "fitted: Lasso on PCA-128 spectrum")]
    ys = [62, 152, 242, 332]
    for (lab, sub), y in zip(levels, ys):
        c.box(330, y, 220, 58, lab, sub)
        c.arrow(280, 226, 328, y + 29, INK2, 1.5)
        c.arrow(550, y + 29, 598, 226, INK2, 1.5)
    c.box(600, 196, 110, 60, "contraction", "ŷ, a weighted sum")
    c.box(600, 332, 110, 58, "Level 0", "scalar rating")
    c.arrow(655, 256, 655, 330, INK2, 1.5)
    c.text(330, 418, "71 of 128 Lasso axes non-zero in the books experiment (Level 4)", 11, "start", INK2)
    c.text(16, 446, "contraction runs one way: no scalar reconstructs a level above it", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 7
def fig_7_1():
    n = 40
    pts = []
    for i in range(n):
        tt = 4 * math.pi * i / (n - 1)
        r = 1.0 + 0.25 * math.sin(3 * tt) + 0.12 * tt / (4 * math.pi)
        pts.append((r * math.cos(tt), 0.85 * r * math.sin(tt)))
    order = list(range(n))
    random.Random(7).shuffle(order)
    shuf = [pts[i] for i in order]

    def step_mean(seq):
        return sum(math.dist(a, b) for a, b in zip(seq[:-1], seq[1:])) / (len(seq) - 1)

    s0, s1 = step_mean(pts), step_mean(shuf)
    m0, c0 = _mean_cov(pts)
    m1, c1 = _mean_cov(shuf)
    assert all(abs(a - b) < 1e-12 for a, b in zip(m0 + c0, m1 + c1))
    assert s1 > 2.5 * s0
    p = reg(_ch(7), "7.1",
            f"An illustrative trajectory of {n} points that circles back on itself (left) and the same {n} points in "
            f"a random order (right). The two clouds are identical, so the mean, the covariance and every pairwise "
            f"similarity agree, and with them every Level 0 to Level 2 quantity. The mean step between consecutive "
            f"points, step_mean, is {s0:.2f} in the author's order and {s1:.2f} after shuffling. Illustrative points, "
            f"not data from Bleak House.",
            "## Closing Note: Against Collapse {#closing-note}")
    c = Canvas(720, 400, "Same paragraphs, new order: only the trajectory changes")
    lim = 1.6
    for k, (seq, name, x0) in enumerate(((pts, "the author's order", 80), (shuf, "shuffled order", 410))):
        size, y0 = 270, 56
        X = lambda u, x0=x0: x0 + size * (u + lim) / (2 * lim)
        Y = lambda v: y0 + size * (1 - (v + lim) / (2 * lim))
        _rect(c, x0, y0, size, size, stroke=GRID, width=1)
        if k == 0:
            c.polyline([(X(x), Y(y)) for x, y in seq], SERIES[0], 2, title="ordered path")
        else:
            c.add('<g stroke-opacity="0.55">')
            c.polyline([(X(x), Y(y)) for x, y in seq], SERIES[1], 1.2, title="shuffled path")
            c.add("</g>")
        for x, y in seq:
            c.dot(X(x), Y(y), INK2, 2.6)
        c.dot(X(seq[0][0]), Y(seq[0][1]), CRITICAL, 4.5, title="first point")
        c.text(x0 + size / 2, y0 + size + 20, name, 12, "middle", INK, "600")
        c.text(x0 + size / 2, y0 + size + 38, f"step_mean {(s0 if k == 0 else s1):.2f}", 11.5, "middle", INK2)
    c.text(16, 390, "illustrative points; first point marked; mean and covariance identical", 10.5, "start", INK3,
           italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 8
def fig_8_1():
    b = 0.25
    fa = lambda x: 3.4 + b * (x - 0.5)
    fb = lambda x: 4.15 + b * (x - 1.8)
    xa = [0.05 + 0.95 * i / 199 for i in range(200)]
    xb = [1.3 + 1.0 * i / 199 for i in range(200)]
    xs = xa + xb
    ys = [fa(x) for x in xa] + [fb(x) for x in xb]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    icpt = my - slope * mx
    xbnd = 1.15
    jump = fb(xbnd) - fa(xbnd)
    assert slope > 2 * b
    p = reg(_ch(8), "8.1",
            f"Schematic with illustrative values: two genre strata along one feature of the work, each with the same "
            f"within-stratum slope, {b}, and a jump of {jump:.2f} in the evaluation at the boundary between them. A "
            f"single least-squares line fitted across both strata has slope {slope:.2f}, most of it the jump. The "
            f"chapter identifies this jump with the genre-confound share of R², 85% in books, and the within-stratum "
            f"slope with the residual signal.",
            "### Penumbral Zones")
    c = Canvas(720, 400, "A fit across strata learns the boundary, not the work")
    ax = Axes(c, 70, 52, 560, 280, (0, 2.5), (2.8, 4.8), [], [3.0, 3.5, 4.0, 4.5], "a feature of the work",
              "evaluation")
    _rect(c, ax.X(0), ax.y0, ax.X(1.05) - ax.X(0), ax.h, BOX, opacity=0.55)
    _rect(c, ax.X(1.25), ax.y0, ax.X(2.4) - ax.X(1.25), ax.h, BOX, opacity=0.55)
    c.text(ax.X(0.52), ax.y0 + 18, "stratum A (genre 1)", 11, "middle", INK2)
    c.text(ax.X(1.82), ax.y0 + 18, "stratum B (genre 2)", 11, "middle", INK2)
    c.line(ax.X(xbnd), ax.y0 + 28, ax.X(xbnd), ax.y0 + ax.h, INK3, 1.5, dash="4 4")
    c.text(ax.X(xbnd), ax.y0 + ax.h - 8, "boundary", 10.5, "middle", INK2, italic=True)
    c.line(ax.X(-0.0), ax.Y(icpt), ax.X(2.4), ax.Y(icpt + slope * 2.4), INK3, 1.5, dash="6 4")
    c.line(ax.X(0.05), ax.Y(fa(0.05)), ax.X(1.0), ax.Y(fa(1.0)), SERIES[0], 3)
    c.line(ax.X(1.3), ax.Y(fb(1.3)), ax.X(2.3), ax.Y(fb(2.3)), SERIES[1], 3)
    # the jump, drawn as a bracket at the boundary
    xj = ax.X(xbnd) + 14
    c.line(ax.X(1.0), ax.Y(fa(1.0)), xj - 4, ax.Y(fa(xbnd)), SERIES[0], 1, dash="2 3")
    c.line(ax.X(1.3), ax.Y(fb(1.3)), xj + 4, ax.Y(fb(xbnd)), SERIES[1], 1, dash="2 3")
    c.line(xj, ax.Y(fa(xbnd)), xj, ax.Y(fb(xbnd)), INK, 1.5)
    c.line(xj - 4, ax.Y(fa(xbnd)), xj + 4, ax.Y(fa(xbnd)), INK, 1.5)
    c.line(xj - 4, ax.Y(fb(xbnd)), xj + 4, ax.Y(fb(xbnd)), INK, 1.5)
    c.text(xj + 8, (ax.Y(fa(xbnd)) + ax.Y(fb(xbnd))) / 2 + 4, f"jump {jump:.2f}", 11, "start", INK)
    c.text(ax.X(0.08), ax.Y(fa(0.08)) + 22, f"within-stratum slope {b}", 11, "start", INK)
    c.text(ax.X(2.4) + 6, ax.Y(icpt + slope * 2.4) + 4, f"pooled {slope:.2f}", 11, "start", INK)
    legend(c, 70, 40, [("within stratum A", SERIES[0]), ("within stratum B", SERIES[1]),
                       ("one fit across both", INK3)])
    c.text(16, 390, "schematic, illustrative values", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 9
def fig_9_1():
    rows = [("path_eff", 0.18, None), ("recur_rate", 0.28, None), ("divergence family", 0.39, 0.44)]
    p = reg(_ch(9), "9.1",
            "Within-bundle standard deviation divided by between-book standard deviation for features of the "
            "cross-lingual study, as the chapter reports them: path_eff 0.18, recur_rate 0.28, and 0.39 to 0.44 "
            "across the divergence family (drawn as a range). A ratio of 1 would mean that a book's translations "
            "differ from one another as much as different books do. Verified empirically (Appendix F, F12.2).",
            "### The Sinitic Gap, Honestly")
    c = Canvas(720, 330, "Translations of one book differ less than different books do")
    x0, w = 200, 460
    X = lambda v: x0 + w * v / 1.1
    for v in (0, 0.25, 0.5, 0.75, 1.0):
        c.line(X(v), 66, X(v), 266, GRID, 1)
        c.text(X(v), 284, f"{v:g}", 11, "middle", INK2)
    c.text(x0 + w / 2, 304, "within-bundle SD / between-book SD (smaller is more language-invariant)", 11.5,
           "middle", INK2)
    for i, (name, lo, hi) in enumerate(rows):
        y = 92 + 66 * i
        c.text(x0 - 12, y + 15, name, 12, "end", INK)
        c.hrect(X(0), y, X(lo) - X(0), 22, SERIES[0], title=f"{name} {lo}")
        if hi is None:
            c.text(X(lo) + 8, y + 15, f"{lo:.2f}", 11, "start", INK)
        else:
            c.hrect(X(lo), y + 6, X(hi) - X(lo), 10, SERIES[0], title=f"{name} {lo}-{hi}", opacity=0.45)
            c.line(X(hi), y + 2, X(hi), y + 20, INK2, 1.5)
            c.text(X(hi) + 8, y + 15, f"{lo:.2f} to {hi:.2f}", 11, "start", INK)
    c.line(X(1.0), 66, X(1.0), 266, INK3, 1.5, dash="4 4")
    c.text(X(1.0) - 6, 60, "1: as different as two books", 10.5, "end", INK2, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 10
def fig_10_1():
    e, a = math.radians(24), math.radians(40)
    v = (math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e))
    r = (-math.sin(a), math.cos(a), 0.0)
    u = (-math.sin(e) * math.cos(a), -math.sin(e) * math.sin(a), math.cos(e))
    cx, cy, R = 220, 226, 150
    dot3 = lambda p, q: p[0] * q[0] + p[1] * q[1] + p[2] * q[2]
    S = lambda p: (cx + R * dot3(p, r), cy - R * dot3(p, u))
    vis = lambda p: dot3(p, v) > 0

    def curve(fn, n=90):
        segs, cur = [], []
        for i in range(n + 1):
            pt = fn(i / n)
            if vis(pt):
                cur.append(S(pt))
            elif cur:
                segs.append(cur)
                cur = []
        if cur:
            segs.append(cur)
        return segs

    leg1 = lambda s: (math.cos(math.pi / 2 * (1 - s)), 0.0, math.sin(math.pi / 2 * (1 - s)))
    leg2 = lambda s: (math.cos(math.pi / 2 * s), math.sin(math.pi / 2 * s), 0.0)
    leg3 = lambda s: (0.0, math.cos(math.pi / 2 * s), math.sin(math.pi / 2 * s))
    # numerical parallel transport: step along the loop, project the vector onto each new tangent plane
    def transport(v0, legs, n=3000):
        vv, out = list(v0), []
        for leg in legs:
            for i in range(1, n + 1):
                pt = leg(i / n)
                d = dot3(vv, pt)
                vv = [vv[k] - d * pt[k] for k in range(3)]
                nrm = math.sqrt(dot3(vv, vv))
                vv = [x / nrm for x in vv]
                if i == n // 2 or i == n:
                    out.append((pt, tuple(vv)))
        return out

    th = math.radians(225)
    start = (math.cos(th), math.sin(th), 0.0)
    marks = transport(start, (leg1, leg2, leg3))
    final = marks[-1][1]
    rot = math.degrees(math.atan2(start[0] * final[1] - start[1] * final[0], dot3(start, final)))
    area = 4 * math.pi / 8
    assert abs(rot - 90.0) < 0.2 and _close(area, math.pi / 2)
    p = reg(_ch(10), "10.1",
            "Holonomy on a unit sphere, the standard picture behind Definition 10.3. A vector is carried without "
            "turning around a closed loop: from the pole N down a meridian to A, along a quarter of the equator to "
            "B, and back up to N. It returns rotated by 90 degrees, equal to the area the loop encloses, π/2. The "
            "chapter posits style holonomy on the aesthetic manifold by analogy; Appendix F lists it as proved in "
            "the abstract and not yet measured on the corpus (F10.2).",
            "### The Dickens–Tolstoy–Joyce–Franzen Circuit")
    c = Canvas(720, 420, "A vector carried around a closed loop comes back rotated")
    _circle(c, cx, cy, R, BORDER, BOX, 1.5, 0.35)
    for lat in (-60, -30, 0, 30, 60):
        la = math.radians(lat)
        fn = lambda s, la=la: (math.cos(la) * math.cos(2 * math.pi * s), math.cos(la) * math.sin(2 * math.pi * s),
                               math.sin(la))
        for seg in curve(fn, 180):
            c.polyline(seg, GRID, 1)
    for lon in range(0, 360, 30):
        lo = math.radians(lon)
        fn = lambda s, lo=lo: (math.cos(math.pi * (s - 0.5)) * math.cos(lo), math.cos(math.pi * (s - 0.5)) * math.sin(lo),
                               math.sin(math.pi * (s - 0.5)))
        for seg in curve(fn, 120):
            c.polyline(seg, GRID, 1)
    for fn in (leg1, leg2, leg3):
        for seg in curve(fn, 90):
            c.polyline(seg, SERIES[0], 3)

    def vec(pt, d, col, width=2.0, L=0.34):
        tip = tuple(pt[i] + L * d[i] for i in range(3))
        (x1, y1), (x2, y2) = S(pt), S(tip)
        c.arrow(x1, y1, x2, y2, col, width)

    vec((0, 0, 1), start, SERIES[1], 2.5, 0.42)
    for pt, d in marks[:-1]:
        vec(pt, d, INK2)
    vec((0, 0, 1), final, CRITICAL, 2.5, 0.42)
    arc = [S(tuple((0, 0, 1)[i] + 0.16 * (math.cos(s) * start[i] + math.sin(s) * final[i]) for i in range(3)))
           for s in [math.pi / 2 * k / 20 for k in range(21)]]
    c.polyline(arc, INK, 1.5)
    nx, ny = S((0, 0, 1))
    c.text(nx + 12, ny + 4, "N", 12, "start", INK, "600")
    axx, ayy = S((1, 0, 0))
    c.text(axx - 10, ayy + 4, "A", 12, "end", INK, "600")
    bx, by = S((0, 1, 0))
    c.text(bx + 10, by + 4, "B", 12, "start", INK, "600")
    x0 = 430
    legend(c, x0, 110, [("vector at the start", SERIES[1])])
    legend(c, x0, 134, [("the same vector after one loop", CRITICAL)])
    legend(c, x0, 158, [("loop N → A → B → N", SERIES[0])])
    c.text(x0, 196, "at each step the vector is kept", 11.5, "start", INK2)
    c.text(x0, 214, "parallel (no turning on the surface)", 11.5, "start", INK2)
    c.text(x0, 248, "it returns rotated by 90 degrees,", 11.5, "start", INK)
    c.text(x0, 266, "the enclosed area, π/2", 11.5, "start", INK)
    c.text(x0, 300, "on a flat surface the rotation is 0", 11.5, "start", INK2, italic=True)
    c.text(16, 410, "the curvature of a sphere, as an analogy for the chapter's style holonomy", 10.5, "start", INK3,
           italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 11
def fig_11_1():
    W, H = 14, 9
    swamp = {(x, y) for x in range(4, 10) for y in range(2, 7)}
    S0, G = (1, 4), (12, 4)
    h = lambda q: abs(q[0] - G[0]) + abs(q[1] - G[1])        # admissible: every step costs at least 1
    cost = lambda q: 5 if q in swamp else 1

    def nbrs(q):
        for dx, dy in ((1, 0), (0, -1), (0, 1), (-1, 0)):
            n = (q[0] + dx, q[1] + dy)
            if 0 <= n[0] < W and 0 <= n[1] < H:
                yield n

    def search(greedy):
        cnt = 0
        g = {S0: 0}
        parent = {S0: None}
        heap = [(h(S0), h(S0), cnt, S0)]
        closed = set()
        while heap:
            _, _, _, q = heapq.heappop(heap)
            if q in closed:
                continue
            closed.add(q)
            if q == G:
                break
            for n in nbrs(q):
                ng = g[q] + cost(n)
                if greedy:
                    if n in parent:
                        continue
                    parent[n], g[n] = q, ng
                    cnt += 1
                    heapq.heappush(heap, (h(n), h(n), cnt, n))
                elif ng < g.get(n, 1e9):
                    g[n], parent[n] = ng, q
                    cnt += 1
                    heapq.heappush(heap, (ng + h(n), h(n), cnt, n))
        path, q = [], G
        while q is not None:
            path.append(q)
            q = parent[q]
        path = path[::-1]
        return path, sum(cost(q) for q in path[1:])

    pa, ca = search(False)
    pg, cg = search(True)
    assert cg > ca
    p = reg(_ch(11), "11.1",
            f"An illustrative grid on which each step costs 1, or 5 inside the shaded block, searched from S to G "
            f"with the Manhattan-distance heuristic, which never overestimates here. A\\* expands by f = g + h and "
            f"returns the cheapest path, of cost {ca}, around the block. Greedy best-first search expands by h alone, "
            f"heads straight at the goal through the block, and returns a path of cost {cg}. Ignoring the "
            f"accumulated cost g misleads the search, as the chapter argues.",
            "## 11.3 Trained Taste as a Heuristic Function {#trained-taste}")
    c = Canvas(720, 400, "A* weighs the cost so far; greedy search follows the heuristic alone")
    cs, x0, y0 = 32, 28, 58
    for x in range(W):
        for y in range(H):
            if (x, y) in swamp:
                _rect(c, x0 + x * cs + 1, y0 + y * cs + 1, cs - 2, cs - 2, SERIES[6], opacity=0.32, rx=3)
            else:
                _rect(c, x0 + x * cs + 1, y0 + y * cs + 1, cs - 2, cs - 2, BOX, opacity=0.45, rx=3)
    ctr = lambda q, off=0.0: (x0 + (q[0] + 0.5) * cs, y0 + (q[1] + 0.5) * cs + off)
    c.polyline([ctr(q) for q in pg], SERIES[1], 3, title=f"greedy path, cost {cg}")
    c.polyline([ctr(q) for q in pa], SERIES[0], 3, title=f"A* path, cost {ca}")
    for q, lab in ((S0, "S"), (G, "G")):
        xq, yq = ctr(q)
        c.dot(xq, yq, INK, 8)
        c.text(xq, yq + 4, lab, 11, "middle", SURFACE, "700")
    xr = 500
    legend(c, xr, 106, [(f"A*: cost {ca}", SERIES[0])])
    legend(c, xr, 132, [(f"greedy: cost {cg}", SERIES[1])])
    legend(c, xr, 158, [("step costs 5 here", SERIES[6])])
    c.text(xr, 196, "A* ranks by f = g + h", 11.5, "start", INK2)
    c.text(xr, 214, "(cost so far + estimate)", 11.5, "start", INK2)
    c.text(xr, 242, "greedy ranks by h only", 11.5, "start", INK2)
    c.text(xr, 276, "h: Manhattan distance to G", 11.5, "start", INK2, italic=True)
    c.text(16, 390, "illustrative grid; step cost 1, or 5 in the shaded block", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 12
def fig_12_1():
    feats = [("pair_sim_mean", 0.712), ("mahal_mean", 0.710), ("Hellinger", 0.675), ("Bhattacharyya", 0.675),
             ("Jensen–Shannon", 0.674)]
    pairs = [("English–Finnish", 0.77, "n = 288, p = 8×10⁻⁵⁷"), ("English–French", 0.78, "n = 227")]
    p = reg(_ch(12), "12.1",
            "Spearman correlation between a feature's value on a book in English and on its translation, as the "
            "chapter reports it. The upper five bars are means over language pairs for the five most invariant "
            "features; the lower two are the headline pairs on the Hellinger feature (English–Finnish, n = 288, "
            "p = 8×10⁻⁵⁷; English–French, n = 227). Verified empirically (Appendix F, F12.1); reading the "
            "feature profile as a Noether current is an analogy (F12.3).",
            "### Within-Bundle vs. Between-Book Dispersion")
    c = Canvas(720, 400, "The same books score alike across languages")
    x0, w = 200, 420
    X = lambda v: x0 + w * v
    top, bot = 62, 352
    for v in (0, 0.25, 0.5, 0.75, 1.0):
        c.line(X(v), top, X(v), bot, GRID, 1)
        c.text(X(v), bot + 16, f"{v:g}", 11, "middle", INK2)
    c.text(x0 + w / 2, bot + 34, "Spearman ρ across translations", 11.5, "middle", INK2)
    c.text(x0, 76, "mean over language pairs", 11, "start", INK2, italic=True)
    for i, (name, rv) in enumerate(feats):
        y = 86 + 30 * i
        c.text(x0 - 12, y + 14, name, 12, "end", INK)
        c.hrect(X(0), y, X(rv) - X(0), 20, SERIES[0], title=f"{name} {rv}")
        c.text(X(rv) + 8, y + 14, f"+{rv:.3f}", 11, "start", INK)
    c.text(x0, 256, "single pairs, Hellinger feature", 11, "start", INK2, italic=True)
    for i, (name, rv, note) in enumerate(pairs):
        y = 266 + 30 * i
        c.text(x0 - 12, y + 14, name, 12, "end", INK)
        c.hrect(X(0), y, X(rv) - X(0), 20, SERIES[1], title=f"{name} {rv}")
        c.text(X(rv) + 8, y + 14, f"+{rv:.2f}  ({note})", 11, "start", INK)
    c.save(p)


# ------------------------------------------------------------------ chapter 13
def fig_13_1():
    amp = 0.5
    th = [2 * math.pi * i / 240 for i in range(241)]
    pr = lambda t, cf: 0.5 * (amp ** 2 + amp ** 2) + cf * amp * amp * math.cos(t)
    assert _close(pr(0, 1), 0.5) and _close(pr(math.pi, 1), 0.0) and _close(pr(1.0, 0), 0.25)
    p = reg(_ch(13), "13.1",
            "The verdict probability of §13.6 for a reader holding two framings with equal amplitudes 0.5 on a "
            "verdict x, against their relative phase θ, with the off-diagonal (interference) term scaled by a "
            "coherence factor c. At c = 1 the probability swings between 0 and 0.5; at c = 0.5 the swing halves; at "
            "c = 0, a classical mixture, it is flat at 0.25. Decoherence (§13.7) is the passage from the first curve "
            "to the last. The quantum vocabulary is an analogy (Appendix F, F13.1); the curves are the formula, not "
            "measurements.",
            "## 13.8 The Classical Limit {#the-classical-limit}")
    c = Canvas(720, 400, "Interference between two framings, and its loss to decoherence")
    ax = Axes(c, 70, 52, 520, 280, (0, 2 * math.pi), (0, 0.6), [], [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
              "relative phase θ between the two framings", "probability of verdict x")
    for v, lab in ((0, "0"), (math.pi / 2, "π/2"), (math.pi, "π"), (1.5 * math.pi, "3π/2"), (2 * math.pi, "2π")):
        c.text(ax.X(v), ax.y0 + ax.h + 16, lab, 11, "middle", INK2)
    for j, (cf, name) in enumerate(((1.0, "c = 1, full coherence"), (0.5, "c = 0.5"), (0.0, "c = 0, mixture"))):
        c.polyline([(ax.X(t), ax.Y(pr(t, cf))) for t in th], SERIES[j], 2, title=name)
        c.text(ax.X(2 * math.pi) + 8, ax.Y(pr(2 * math.pi, cf)) + 4, f"c = {cf:g}", 11, "start", INK2)
    c.text(ax.X(0.18), ax.Y(0.5) - 8, "constructive", 11, "start", INK, italic=True)
    c.text(ax.X(math.pi), ax.Y(0) - 20, "destructive", 11, "middle", INK, italic=True)
    legend(c, 70, 40, [("c = 1, full coherence", SERIES[0]), ("c = 0.5", SERIES[1]), ("c = 0, classical mixture",
                                                                                      SERIES[2])])
    c.save(p)


# ------------------------------------------------------------------ chapter 14
def fig_14_1():
    c1 = _gauss_cloud(45, 21, -1.9, 0.6, 0.42, 0.38, 0.3)
    c2 = _gauss_cloud(55, 22, 1.6, -0.4, 0.52, 0.45, -0.25)
    allp = c1 + c2
    gm = (sum(q[0] for q in allp) / len(allp), sum(q[1] for q in allp) / len(allp))
    nearest = min(math.dist(gm, q) for q in allp)
    assert nearest > 0.6
    m1, v1 = _mean_cov(c1)
    m2, v2 = _mean_cov(c2)
    p = reg(_ch(14), "14.1",
            "Schematic with illustrative points: works in two dense regions of a two-dimensional feature space. The "
            "average of all works falls in the empty gap between them; no work lies near it. That is what a "
            "scalar-average canon reports. The chapter's alternative takes a canon as a cluster centre together with "
            "its spread, drawn here as each cluster's mean and one-standard-deviation ellipse. Canon formation by "
            "geometric aggregation is conjectured (Appendix F, F14.1).",
            "## 14.4 The Collective Aesthetic Tensor {#the-collective-aesthetic-tensor}")
    c = Canvas(720, 400, "The average lands where no work is; a canon is a cluster centre")
    x0, y0, w, h = 60, 56, 400, 300
    xl, yl = (-3.6, 3.6), (-2.7, 2.7)
    X = lambda u: x0 + w * (u - xl[0]) / (xl[1] - xl[0])
    Y = lambda v: y0 + h * (1 - (v - yl[0]) / (yl[1] - yl[0]))
    assert all(xl[0] < q[0] < xl[1] and yl[0] < q[1] < yl[1] for q in allp)
    _rect(c, x0, y0, w, h, stroke=GRID, width=1)
    for k, (pts, m, v) in enumerate(((c1, m1, v1), (c2, m2, v2))):
        _cov_ellipse(c, X, Y, m, v, 1, SERIES[k], SERIES[k], 0.1, 1.5)
        for q in pts:
            c.dot(X(q[0]), Y(q[1]), SERIES[k], 2.8)
    for k, m in enumerate((m1, m2)):
        c.dot(X(m[0]), Y(m[1]), INK, 5, title="cluster centre")
    c.text(X(m1[0]), Y(m1[1]) - 52, "cluster 1", 11, "middle", INK2)
    c.text(X(m2[0]), Y(m2[1]) + 60, "cluster 2", 11, "middle", INK2)
    _circle(c, X(gm[0]), Y(gm[1]), 9, CRITICAL, "none", 2)
    c.dot(X(gm[0]), Y(gm[1]), CRITICAL, 3.5, title="average of all works")
    lab = "average of all works"
    tw, gx, gy = 6.0 * len(lab), X(gm[0]), Y(gm[1])
    screen = [(X(q[0]), Y(q[1])) for q in allp]
    placed = None
    for dy in (-20, 30, -34, 44, -48, 58):
        x1, x2, y1, y2 = gx - tw / 2 - 4, gx + tw / 2 + 4, gy + dy - 13, gy + dy + 4
        if not any(x1 <= sx <= x2 and y1 <= sy <= y2 for sx, sy in screen):
            placed = dy
            break
    assert placed is not None
    if abs(placed) > 24:
        c.line(gx, gy + (10 if placed > 0 else -10), gx, gy + placed + (-12 if placed > 0 else 4), INK3, 1)
    c.text(gx, gy + placed, lab, 11, "middle", INK)
    xr = 490
    c.dot(xr + 6, 116, INK, 5)
    c.text(xr + 20, 120, "cluster centre: a canon,", 11.5, "start", INK2)
    c.text(xr + 20, 138, "with its spread (ellipse)", 11.5, "start", INK2)
    _circle(c, xr + 6, 176, 8, CRITICAL, "none", 2)
    c.text(xr + 20, 180, "grand average: the", 11.5, "start", INK2)
    c.text(xr + 20, 198, "scalar-average canon", 11.5, "start", INK2)
    c.text(xr, 240, "nearest work to the average:", 11.5, "start", INK2)
    c.text(xr, 258, f"{nearest:.2f} units away", 11.5, "start", INK)
    c.text(16, 390, "schematic, illustrative points", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 15
def fig_15_1():
    A, B = (0.9, 0.3), (0.55, 0.55)
    sumA, sumB = A[0] + A[1], B[0] + B[1]
    minA, minB = min(A), min(B)
    assert _close(sumA, 1.2) and _close(sumB, 1.1) and _close(minA, 0.3) and _close(minB, 0.55)
    p = reg(_ch(15), "15.1",
            "Two illustrative works, A and B, on two quality axes. Under the summative projection of §15.5, "
            "V = O¹ + O², the lines of equal verdict are diagonals and A ranks first, 1.2 to 1.1. Under the maximin "
            "projection, V = min(O¹, O²), they are corners and B ranks first, 0.55 to 0.3. The works do not change; "
            "only the projection does.",
            "## 15.6 The Information Lost {#the-information-lost}")
    c = Canvas(720, 400, "One pair of works, two projections, opposite verdicts")
    size, y0 = 250, 72
    for k, (x0, name) in enumerate(((80, "summative: V = O¹ + O²"), (420, "maximin: V = min(O¹, O²)"))):
        X = lambda u, x0=x0: x0 + size * u
        Y = lambda v: y0 + size * (1 - v)
        _rect(c, x0, y0, size, size, stroke=GRID, width=1)
        for g in (0.25, 0.5, 0.75):
            c.line(X(g), Y(0), X(g), Y(1), GRID, 1)
            c.line(X(0), Y(g), X(1), Y(g), GRID, 1)
        c.text(x0 + size / 2, y0 + size + 18, "quality 1 (O¹)", 11.5, "middle", INK2)
        c.text(x0 - 14, y0 + size / 2, "quality 2 (O²)", 11.5, "middle", INK2, rotate=-90)
        c.text(x0 + size / 2, 60, name, 12, "middle", INK, "600")
        if k == 0:
            for val, col in ((sumA, SERIES[0]), (sumB, SERIES[1])):
                c.line(X(val - 1), Y(1), X(1), Y(val - 1), col, 1.5, dash="5 4")
            c.dot(X(A[0]), Y(A[1]), SERIES[0], 5)
            c.dot(X(B[0]), Y(B[1]), SERIES[1], 5)
            c.text(X(A[0]) + 10, Y(A[1]) + 4, "A 1.2: first", 11, "start", INK)
            c.text(X(B[0]) - 10, Y(B[1]) + 16, "B 1.1", 11, "end", INK)
        else:
            for val, col in ((minA, SERIES[0]), (minB, SERIES[1])):
                _dashpoly(c, [(X(val), Y(1)), (X(val), Y(val)), (X(1), Y(val))], col, 1.5)
            c.dot(X(A[0]), Y(A[1]), SERIES[0], 5)
            c.dot(X(B[0]), Y(B[1]), SERIES[1], 5)
            c.text(X(A[0]), Y(A[1]) + 20, "A 0.3", 11, "middle", INK)
            c.text(X(B[0]) + 10, Y(B[1]) - 10, "B 0.55: first", 11, "start", INK)
    c.text(16, 390, "illustrative works; dashed lines are lines of equal verdict through each work", 10.5, "start",
           INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 16
def fig_16_1():
    rb, rbr, rm, rmr = 0.241, 0.093, 0.302, 0.177
    zb, zbr, zm, zmr = 17, 6.5, 49.8, 28.3
    gb = 1 - (rbr / rb) ** 2
    gm = 1 - (rmr / rm) ** 2
    assert round(rb ** 2, 3) == 0.058 and round(rbr ** 2, 3) == 0.009
    assert round(100 * gb) == 85 and round(100 * gm) == 66
    p = reg(_ch(16), "16.1",
            f"Variance explained, R² as a percentage, before and after genre residualization, from the correlations "
            f"the chapter and Chapter 17 report: books R = 0.241 and 0.093, the music spectrum Lasso R = 0.302 and "
            f"0.177, with each bar's z. The genre share of R² is 1 − (0.093/0.241)² = {100 * gb:.0f}% for books and "
            f"1 − (0.177/0.302)² = {100 * gm:.0f}% for the music spectrum Lasso. The chapter's 91% for music is the "
            f"share for the hand features.",
            "## 16.7 The Normative Gap {#16-7-the-normative-gap}")
    c = Canvas(720, 400, "Strong z, small R²: what the geometry explains")
    ax = Axes(c, 80, 60, 600, 260, (0, 2), (0, 10), [], [0, 2, 4, 6, 8, 10], "", "R², percent of variance")
    groups = [("books, combined model", (rb, zb), (rbr, zbr), gb), ("music, spectrum Lasso", (rm, zm), (rmr, zmr), gm)]
    for i, (name, raw, res, g) in enumerate(groups):
        cx = ax.X(i + 0.5)
        for j, (rr, zz) in enumerate((raw, res)):
            x = cx - 47 + j * 70
            v = 100 * rr ** 2
            c.rect(x, ax.Y(v), 24, ax.Y(0) - ax.Y(v), SERIES[j], title=f"{name}: R {rr}, R2 {v:.2f}%")
            c.text(x + 12, ax.Y(v) - 20, f"{v:.1f}%", 11, "middle", INK)
            c.text(x + 12, ax.Y(v) - 6, f"{zz:g}σ", 10.5, "middle", INK2)
        c.text(cx, ax.y0 + ax.h + 18, name, 11.5, "middle", INK)
        c.text(cx, ax.y0 + ax.h + 36, f"genre share of R²: {100 * g:.0f}%", 11, "middle", INK2)
    legend(c, 80, 44, [("raw", SERIES[0]), ("genre-residualized", SERIES[1])])
    c.text(16, 390, "R² is the square of the R reported in Chapter 17 (§17.4, §17.6)", 10.5, "start", INK3,
           italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 17
def fig_17_1():
    rows = [("pair_sim_mean", "books", 0.126, "+0.126 (8.4σ)", 0),
            ("pair_sim_mean", "music", -0.076, "−0.076 (p = 5×10⁻³³)", 1),
            ("step_mean", "books", -0.096, "−0.096 (6.4σ)", 0),
            ("step_mean", "music", 0.071, "+0.071 (p = 4×10⁻²⁹)", 1)]
    for _, _, v, _, _ in rows:
        assert abs(v) < 0.2
    assert rows[0][2] * rows[1][2] < 0 and rows[2][2] * rows[3][2] < 0
    p = reg(_ch(17), "17.1",
            "Spearman correlation of two cloud features with reception, as §17.6.3 reports it: Goodreads rating for "
            "books (n = 4,998) and log(1 + listens) for music (n = 24,801). Internal coherence, pair_sim_mean, is "
            "positive for books and negative for music; step size, step_mean, is the reverse. Each flip is robust "
            "at p < 10⁻²⁸. Verified empirically (Appendix F, F21.6 and F21.7).",
            "## 17.7 Philosophical Interpretation")
    c = Canvas(720, 400, "The same two features, opposite signs in books and music")
    x0, w = 250, 420
    lim = 0.2
    X = lambda v: x0 + w * (v + lim) / (2 * lim)
    top, bot = 70, 330
    for v in (-0.2, -0.1, 0, 0.1, 0.2):
        c.line(X(v), top, X(v), bot, GRID, 1)
        c.text(X(v), bot + 16, f"{v:+.1f}" if v else "0", 11, "middle", INK2)
    c.line(X(0), top, X(0), bot, INK3, 1.5)
    c.text(X(0), bot + 34, "Spearman ρ with reception", 11.5, "middle", INK2)
    ys = [96, 136, 216, 256]
    for (feat, mod, v, lab, j), y in zip(rows, ys):
        c.text(x0 - 12, y + 14, mod, 12, "end", INK)
        _hbar(c, X(0), y, X(v) - X(0), 22, SERIES[j], title=f"{feat}, {mod}: {v}")
        if v > 0:
            c.text(X(v) + 8, y + 15, lab, 11, "start", INK)
        else:
            c.text(X(v) - 8, y + 15, lab, 11, "end", INK)
    c.text(20, 90, "pair_sim_mean", 12, "start", INK, "600")
    c.text(20, 108, "internal coherence", 11, "start", INK2)
    c.text(20, 210, "step_mean", 12, "start", INK, "600")
    c.text(20, 228, "trajectory step size", 11, "start", INK2)
    legend(c, 250, 50, [("books: Goodreads rating", SERIES[0]), ("music: log(1 + listens)", SERIES[1])])
    c.save(p)


# ------------------------------------------------------------------ chapter 18
def fig_18_1():
    rows = [("MERT, Lasso on PCA spectrum", 0.225), ("MERT hand features", 0.151), ("Spotify's 8 acoustic features", 0.103)]
    ratio = rows[0][1] / rows[2][1]
    assert round(ratio, 1) == 2.2
    p = reg(_ch(18), "18.1",
            f"Correlation R with log(1 + listens) on the shared Echonest subset of n = 5,233 tracks, as the chapter "
            f"reports it: the MERT spectrum Lasso 0.225, MERT hand features 0.151, Spotify's eight acoustic features "
            f"0.103. The bootstrap difference between the first and the last gives p = 0.001; their ratio, "
            f"{ratio:.1f}, is the chapter's factor of 2.2. Verified empirically (Appendix F, F21.3).",
            "## 18.5 Invariance as Aesthetic Alignment {#18-5-invariance-as-alignment}")
    c = Canvas(720, 340, "On the same 5,233 tracks, learned geometry beats curated features")
    x0, w = 250, 380
    X = lambda v: x0 + w * v / 0.25
    top, bot = 70, 250
    for v in (0, 0.05, 0.1, 0.15, 0.2, 0.25):
        c.line(X(v), top, X(v), bot, GRID, 1)
        c.text(X(v), bot + 16, f"{v:g}", 11, "middle", INK2)
    c.text(x0 + w / 2, bot + 34, "correlation R with log(1 + listens)", 11.5, "middle", INK2)
    ys = [86, 146, 206]
    for i, ((name, v), y) in enumerate(zip(rows, ys)):
        c.text(x0 - 12, y + 15, name, 12, "end", INK)
        c.hrect(X(0), y, X(v) - X(0), 22, SERIES[0] if i < 2 else SERIES[1], title=f"{name} {v}")
        c.text(X(v) + 8, y + 15, f"{v:.3f}", 11, "start", INK)
    xb = X(0.225) + 48
    c.line(xb, ys[0] + 11, xb, ys[2] + 11, INK2, 1.5)
    c.line(xb - 6, ys[0] + 11, xb, ys[0] + 11, INK2, 1.5)
    c.line(xb - 6, ys[2] + 11, xb, ys[2] + 11, INK2, 1.5)
    c.text(xb + 8, (ys[0] + ys[2]) / 2 + 15, "p = 0.001", 11, "start", INK)
    c.text(16, 330, "shared Echonest subset, n = 5,233, artist-disjoint 5-fold CV", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 19
def fig_19_1():
    p = reg(_ch(19), "19.1",
            "The six steps of §19.7 for one query. The evaluation layer returns a tensor and no verdict; the scalar "
            "appears only at step 4, when an interest covector supplied by the translation layer is contracted "
            "against it; governance audits the covectors and revises them. A design, not a running system: §19.9 "
            "reports Discover and Evaluate built for books and music, Mediate partial, and the full four-layer "
            "architecture not built.",
            "## 19.8 Connection to ErisML {#19-8-connection-to-erisml}")
    c = Canvas(720, 400, "One query through the aesthetic DEME: tensor first, verdict last")
    bw, bh = 190, 64
    xs = [30, 265, 500]
    y1, y2 = 76, 252
    c.box(xs[0], y1, bw, bh, "1  Application", "receives the work W*")
    c.box(xs[1], y1, bw, bh, "2  Evaluation", "tensor T, no verdict")
    c.box(xs[2], y1, bw, bh, "3  Translation", "interest covector I")
    c.box(xs[2], y2, bw, bh, "4  Application", "verdict S = I · T")
    c.box(xs[1], y2, bw, bh, "5  Explain", "attribution, residue, flags")
    c.box(xs[0], y2, bw, bh, "6  Governance", "audits the covectors")
    c.arrow(xs[0] + bw, y1 + bh / 2, xs[1] - 2, y1 + bh / 2, INK2, 1.5)
    c.arrow(xs[1] + bw, y1 + bh / 2, xs[2] - 2, y1 + bh / 2, INK2, 1.5)
    c.arrow(xs[2] + bw * 0.7, y1 + bh, xs[2] + bw * 0.7, y2 - 2, INK2, 1.5)
    c.arrow(xs[2], y2 + bh / 2, xs[1] + bw + 2, y2 + bh / 2, INK2, 1.5)
    c.arrow(xs[1], y2 + bh / 2, xs[0] + bw + 2, y2 + bh / 2, INK2, 1.5)
    fx = xs[2] + bw * 0.3
    _dashpoly(c, [(xs[0] + bw / 2, y2), (xs[0] + bw / 2, 196), (fx, 196), (fx, y1 + bh + 10)], INK3, 1.5)
    c.arrow(fx, y1 + bh + 12, fx, y1 + bh + 2, INK3, 1.5)
    c.text((xs[0] + bw / 2 + fx) / 2, 188, "governance revises the covectors", 11, "middle", INK2, italic=True)
    c.text(xs[2] + bw / 2, y2 + bh + 20, "the only contraction to a scalar", 11, "middle", INK2, italic=True)
    c.text(16, 390, "design document (§19.9): Discover and Evaluate built for books and music; full stack not built",
           10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 20
def fig_20_1():
    rb, rr = 0.241, 0.093
    assert round(100 * (1 - (rr / rb) ** 2)) == 85
    p = reg(_ch(20), "20.1",
            "The Gutenberg–Goodreads experiment as the chapter describes it, with the significance each channel "
            "reaches and the result at each control. The headline R = 0.241 falls to R = 0.093 when genre is "
            "residualized, so 85% of the R² was genre; within fiction alone R = 0.131. Non-fiction and "
            "history-biography are null within genre. Verified empirically (Appendix F, F17.1 to F17.5).",
            "## 20.4 The Strongest Finding — Cross-Lingual Invariance {#20-4-cross-lingual-invariance}")
    c = Canvas(720, 500, "The books pipeline, from text to the residual signal")
    row1 = [(20, 160, "Gutenberg books", "n = 4,998, Goodreads"), (205, 120, "paragraphs", "per book"),
            (350, 140, "LaBSE", "768-d per paragraph"), (515, 185, "trajectory", "x1 … xT per book")]
    y1 = 58
    for i, (x, w, lab, sub) in enumerate(row1):
        c.box(x, y1, w, 54, lab, sub)
        if i:
            px, pw = row1[i - 1][0], row1[i - 1][1]
            c.arrow(px + pw, y1 + 27, x - 2, y1 + 27, INK2, 1.5)
    chans = [("A  divergences", "~8σ each"), ("B  coherence", "pair_sim, 8.4σ"), ("C  trajectory", "3–6σ each"),
             ("D  Lasso, PCA-128", "71 of 128 non-zero")]
    y2, cw = 172, 160
    cxs = [20 + i * 175 for i in range(4)]
    c.line(607, y1 + 54, 607, 146, INK2, 1.5)
    c.line(100, 146, 607, 146, INK2, 1.5)
    for x, (lab, sub) in zip(cxs, chans):
        c.arrow(x + cw / 2, 146, x + cw / 2, y2 - 2, INK2, 1.5)
        c.box(x, y2, cw, 56, lab, sub)
        c.line(x + cw / 2, y2 + 56, x + cw / 2, 252, INK2, 1.5)
    c.line(100, 252, 625, 252, INK2, 1.5)
    c.arrow(360, 252, 360, 274, INK2, 1.5)
    c.box(190, 276, 340, 60, "combined Ridge + Lasso", "author-disjoint 5-fold CV: R = 0.241, 17σ")
    c.arrow(300, 336, 230, 390, INK2, 1.5)
    c.arrow(420, 336, 490, 390, INK2, 1.5)
    c.box(110, 392, 240, 60, "genre residualized", "R = 0.093, 6.5σ")
    c.box(380, 392, 240, 60, "fiction only", "R = 0.131, 6.2σ, n = 2,250")
    c.text(238, 368, "85% of R² was genre", 11, "end", INK2, italic=True)
    c.text(16, 490, "channel significances and results as reported in Chapters 17 and 20", 10.5, "start", INK3,
           italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 21
def fig_21_1():
    rows = [("Rock", 0.139, "7,088"), ("Electronic", 0.143, "6,284"), ("Hip-Hop", 0.141, "2,190"),
            ("Pop", 0.185, "1,173"), ("Classical", -0.013, "584"), ("Jazz", 0.031, "384")]
    p = reg(_ch(21), "21.1",
            "Artist-disjoint within-genre Ridge correlation R with log(1 + listens), with each genre's track count, as "
            "the chapter reports it. Rock, electronic, hip-hop and pop lie between 0.139 and 0.185; classical "
            "(−0.013) and jazz (0.031) are null. The chapter leaves open whether the nulls come from 30-second clips, "
            "from listens as the target, or both. Verified empirically (Appendix F, F21.4 and F21.5).",
            "## 21.8 Back to the Manifold {#21-8-back-to-the-manifold}")
    c = Canvas(720, 400, "Within-genre signal: four popular genres, none in classical or jazz")
    ax = Axes(c, 80, 56, 600, 260, (0, 6), (-0.05, 0.22), [], [0, 0.05, 0.1, 0.15, 0.2], "",
              "within-genre R")
    c.line(ax.x0, ax.Y(0), ax.x0 + ax.w, ax.Y(0), INK3, 1.5)
    for i, (g, v, n) in enumerate(rows):
        cx = ax.X(i + 0.5)
        null = i >= 4
        col = INK3 if null else SERIES[0]
        _vbar(c, cx - 12, ax.Y(0), ax.Y(v), 24, col, title=f"{g}: R {v}, n {n}")
        lab = f"{v:+.3f}".replace("+", "") if v >= 0 else f"−{abs(v):.3f}"
        if v >= 0:
            c.text(cx, ax.Y(v) - 6, lab, 11, "middle", INK)
        else:
            c.text(cx, ax.Y(v) + 16, lab, 11, "middle", INK)
        c.text(cx, ax.y0 + ax.h + 18, g, 11.5, "middle", INK)
        c.text(cx, ax.y0 + ax.h + 34, f"n = {n}", 10.5, "middle", INK2)
        if null:
            c.text(cx, ax.Y(0.075), "null", 11, "middle", INK2, italic=True)
    c.text(16, 390, "artist-disjoint 5-fold CV within each genre", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 22
def fig_22_1():
    books, music = (0.126, -0.096), (-0.076, 0.071)
    assert books[0] > 0 > books[1] and music[0] < 0 < music[1]
    p = reg(_ch(22), "22.1",
            "Each modality placed by its two measured rank correlations with reception: internal coherence "
            "(pair_sim_mean) across, step size (step_mean) up. Books and music, from Chapter 17, fall in opposite "
            "quadrants. The chapter's predictions for film are regions, not points: A puts film with books, B with "
            "music, and C, the chapter's prior, splits art-house and drama from action and thriller. The film "
            "predictions are conjectured and untested (Appendix F, F22.1).",
            "## 22.4 Eisenstein, Bazin, and the Theory Prior {#22-4-eisenstein-bazin}")
    c = Canvas(720, 420, "Where would film fall? Two measured points, three predictions")
    x0, y0, s, lim = 90, 56, 300, 0.16
    X = lambda u: x0 + s * (u + lim) / (2 * lim)
    Y = lambda v: y0 + s * (1 - (v + lim) / (2 * lim))
    _rect(c, X(0), Y(0), X(lim) - X(0), Y(-lim) - Y(0), SERIES[0], opacity=0.08)
    _rect(c, X(-lim), Y(lim), X(0) - X(-lim), Y(0) - Y(lim), SERIES[1], opacity=0.08)
    _rect(c, x0, y0, s, s, stroke=GRID, width=1)
    for v in (-0.1, 0.1):
        c.line(X(v), y0, X(v), y0 + s, GRID, 1)
        c.line(x0, Y(v), x0 + s, Y(v), GRID, 1)
        c.text(X(v), y0 + s + 16, f"{v:+.1f}", 11, "middle", INK2)
        c.text(x0 - 8, Y(v) + 4, f"{v:+.1f}", 11, "end", INK2)
    c.line(X(0), y0, X(0), y0 + s, INK3, 1.5)
    c.line(x0, Y(0), x0 + s, Y(0), INK3, 1.5)
    c.text(X(0), y0 + s + 16, "0", 11, "middle", INK2)
    c.text(x0 + s / 2, y0 + s + 34, "ρ for coherence (pair_sim_mean)", 11.5, "middle", INK2)
    c.text(x0 - 40, y0 + s / 2, "ρ for step size (step_mean)", 11.5, "middle", INK2, rotate=-90)
    c.text(X(lim) - 8, Y(-lim) - 10, "continuity-rewarding", 11, "end", INK2, italic=True)
    c.text(X(-lim) + 8, Y(lim) + 18, "contrast-rewarding", 11, "start", INK2, italic=True)
    c.text(X(0.08), Y(-0.03), "A?", 13, "middle", INK3, "600", italic=True)
    c.text(X(-0.08), Y(0.03) + 8, "B?", 13, "middle", INK3, "600", italic=True)
    c.dot(X(books[0]), Y(books[1]), SERIES[0], 6, title="books (+0.126, -0.096)")
    c.dot(X(music[0]), Y(music[1]), SERIES[1], 6, title="music (-0.076, +0.071)")
    c.text(X(books[0]) - 10, Y(books[1]) + 4, "books", 12, "end", INK, "600")
    c.text(X(music[0]) + 10, Y(music[1]) + 4, "music", 12, "start", INK, "600")
    xr = 430
    c.text(xr, 76, "measured (Chapter 17)", 12, "start", INK, "600")
    c.text(xr, 98, "books: +0.126, −0.096", 11.5, "start", INK2)
    c.text(xr, 116, "music: −0.076, +0.071", 11.5, "start", INK2)
    c.text(xr, 152, "predicted for film, untested", 12, "start", INK, "600")
    lines = ["A: with books (continuity editing,", "    the long take)",
             "B: with music (montage,", "    fast cutting)",
             "C: split by genre: art-house with", "    books, action with music",
             "    (the chapter's prior)"]
    for i, ln in enumerate(lines):
        c.text(xr, 174 + 18 * i, ln, 11.5, "start", INK2)
    c.save(p)


# ------------------------------------------------------------------ chapter 23
def fig_23_1():
    side, patch = 518, 14
    grid = side // patch
    assert grid == 37 and grid * grid == 1369
    seq = [(2, 1), (5, 2), (4, 4), (6, 5), (2, 5), (3, 6), (5, 6)]
    emb = [(0.15, 0.75), (0.38, 0.88), (0.48, 0.55), (0.72, 0.62), (0.3, 0.3), (0.45, 0.2), (0.8, 0.3)]
    p = reg(_ch(23), "23.1",
            "Schematic. A vision transformer tiles the image into patches, 37 × 37 = 1,369 for a 518-pixel input to "
            "DINOv2-ViT-L/14 (drawn here as 8 × 8), and gives each patch an embedding; together they form the "
            "painting's patch cloud. A predicted order of fixations (illustrative, numbered) turns the cloud into a "
            "trajectory, on which the step and recurrence features of Chapter 17 are defined. The painting pipeline "
            "is proposed and untested (Appendix F, F23.1).",
            "### What the Rating-Analog Is")
    c = Canvas(720, 400, "A painting becomes a trajectory when a viewing order is imposed")
    x0, y0, cs, n = 60, 64, 30, 8
    _rect(c, x0, y0, cs * n, cs * n, BOX, BORDER, 1, 0.6)
    for i in range(1, n):
        c.line(x0 + i * cs, y0, x0 + i * cs, y0 + n * cs, GRID, 1)
        c.line(x0, y0 + i * cs, x0 + n * cs, y0 + i * cs, GRID, 1)
    ctr = lambda q: (x0 + (q[0] + 0.5) * cs, y0 + (q[1] + 0.5) * cs)
    pts = [ctr(q) for q in seq]
    for (xa, ya), (xb, yb) in zip(pts[:-1], pts[1:]):
        c.arrow(xa, ya, xb, yb, SERIES[1], 1.5)
    off_grid = [(-9, 4, "end"), (9, 4, "start"), (-9, 4, "end"), (9, 4, "start"), (-9, 4, "end"), (0, 17, "middle"),
                (9, 4, "start")]
    for k, (xq, yq) in enumerate(pts):
        c.dot(xq, yq, SERIES[1], 4)
        dx, dy, anc = off_grid[k]
        c.text(xq + dx, yq + dy, str(k + 1), 10.5, anc, INK)
    c.text(x0 + n * cs / 2, y0 + n * cs + 20, "image patches (8 × 8 drawn; 37 × 37 in DINOv2-L/14)", 11, "middle",
           INK2)
    c.text(x0 + n * cs / 2, y0 + n * cs + 38, "numbers: an illustrative fixation order", 11, "middle", INK2)
    c.arrow(318, y0 + n * cs / 2, 398, y0 + n * cs / 2, INK2, 1.5)
    c.text(358, y0 + n * cs / 2 - 10, "encode", 11, "middle", INK2, italic=True)
    ex, ey, ew, eh = 410, 64, 270, 240
    _rect(c, ex, ey, ew, eh, stroke=GRID, width=1)
    E = lambda q: (ex + 16 + (ew - 32) * q[0], ey + 12 + (eh - 24) * (1 - q[1]))
    epts = [E(q) for q in emb]
    c.polyline(epts, SERIES[0], 2, title="patch trajectory")
    off_emb = [(-9, 4, "end"), (0, -10, "middle"), (0, 18, "middle"), (9, 4, "start"), (-9, 4, "end"),
               (0, 18, "middle"), (9, 4, "start")]
    for k, (xq, yq) in enumerate(epts):
        c.dot(xq, yq, SERIES[0], 4)
        dx, dy, anc = off_emb[k]
        c.text(xq + dx, yq + dy, str(k + 1), 10.5, anc, INK)
    c.text(ex + ew / 2, ey + eh + 20, "embedding space: the patch trajectory", 11, "middle", INK2)
    c.text(ex + ew / 2, ey + eh + 38, "steps, recurrence, path efficiency", 11, "middle", INK2)
    c.text(16, 390, "schematic; positions illustrative", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 24
def fig_24_1():
    shapes = [("circle", None), ("square", 1.0), ("4 : 3", 4 / 3), ("√2 : 1", math.sqrt(2)), ("3 : 2", 1.5),
              ("5 : 3", 5 / 3), ("2 : 1", 2.0)]
    phi = (1 + math.sqrt(5)) / 2
    ratios = [r for _, r in shapes if r]
    assert all(abs(r - phi) > 0.04 for r in ratios)
    p = reg(_ch(24), "24.1",
            "The seven room shapes of Palladio's Quattro Libri as the chapter lists them, drawn to their ratio of long "
            "side to short: circle, square, square and a third, root-two rectangle, square and a half, square and two "
            "thirds, double square. The system admits a family of ratios, not a single one. The golden ratio "
            "φ ≈ 1.618, the subject of the next section, is marked on the ratio line for comparison.",
            "### The Golden Ratio, Empirically Reconsidered")
    c = Canvas(720, 400, "Palladio's seven room shapes: a family of ratios, not one")
    base, sw, gap, x = 232, 56, 34, 62
    for name, r in shapes:
        if r is None:
            _circle(c, x + sw / 2, base - sw / 2, sw / 2, SERIES[0], SERIES[0], 2, 0.15)
        else:
            hgt = sw * r
            _rect(c, x, base - hgt, sw, hgt, SERIES[0], SERIES[0], 2, 0.15)
        c.text(x + sw / 2, base + 20, name, 11.5, "middle", INK)
        x += sw + gap
    lx0, lx1, ly = 100, 620, 320
    L = lambda r: lx0 + (lx1 - lx0) * (r - 1.0)
    c.line(lx0, ly, lx1, ly, INK3, 1.5)
    for r in ratios:
        c.dot(L(r), ly, SERIES[0], 4.5, title=f"{r:.3f}")
        c.text(L(r), ly - 12, f"{r:.3f}".rstrip("0").rstrip("."), 10.5, "middle", INK)
    c.line(L(phi), ly - 6, L(phi), ly + 6, CRITICAL, 2.5)
    c.text(L(phi), ly + 22, "φ ≈ 1.618", 11, "middle", INK)
    c.text((lx0 + lx1) / 2, ly + 46, "ratio of long side to short side", 11.5, "middle", INK2)
    c.text(16, 390, "shapes drawn with a common short side", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 25
def fig_25_1():
    band = 1.2
    path = [(1.0, 1.5), (2.0, 1.8), (2.5, 3.2), (3.5, 3.6), (4.2, 5.0), (5.5, 5.2), (6.0, 6.8), (7.2, 7.0),
            (7.8, 8.5), (9.0, 8.7)]
    assert all(abs(cy - sk) <= band for sk, cy in path)
    p = reg(_ch(25), "25.1",
            "Csikszentmihalyi's flow channel as the chapter describes it: experience is optimal while challenge "
            "matches skill within a narrow band, anxious when challenge runs above it and boring when it falls "
            "below. The band width and the session path are illustrative. The chapter restates flow as a property of "
            "the session trajectory, its curvature and step variance (Prediction 25.2); that restatement is "
            "conjectured and untested (Appendix F, F25 to F28).",
            "## 25.5 Genre, as Ever")
    c = Canvas(720, 400, "The flow channel: challenge kept level with skill")
    ax = Axes(c, 80, 52, 360, 300, (0, 10), (0, 10), [], [], "", "challenge")
    c.text(ax.x0 + ax.w / 2, ax.y0 + ax.h + 20, "skill", 11.5, "middle", INK2)
    _rect(c, ax.x0, ax.y0, ax.w, ax.h, stroke=GRID, width=1)
    poly = [(0, 0), (band, 0), (10, 10 - band), (10, 10), (10 - band, 10), (0, band)]
    _poly(c, [(ax.X(x), ax.Y(y)) for x, y in poly], SERIES[0], "none", 0, 0.18)
    c.line(ax.X(band), ax.Y(0), ax.X(10), ax.Y(10 - band), SERIES[0], 1.5, dash="4 4")
    c.line(ax.X(0), ax.Y(band), ax.X(10 - band), ax.Y(10), SERIES[0], 1.5, dash="4 4")
    c.polyline([(ax.X(x), ax.Y(y)) for x, y in path], SERIES[1], 2, title="illustrative session")
    for x, y in path:
        c.dot(ax.X(x), ax.Y(y), SERIES[1], 3.5)
    c.text(ax.X(2.2), ax.Y(8.2), "anxiety", 13, "middle", INK2, italic=True)
    c.text(ax.X(7.8), ax.Y(1.8), "boredom", 13, "middle", INK2, italic=True)
    ang = -math.degrees(math.atan2(ax.h / 10, ax.w / 10))
    c.text(ax.X(3.9), ax.Y(3.06), "flow channel", 12, "middle", INK, rotate=ang)
    xr = 480
    c.text(xr, 110, "challenge above skill: anxiety", 11.5, "start", INK2)
    c.text(xr, 132, "challenge below skill: boredom", 11.5, "start", INK2)
    c.text(xr, 154, "within the band: flow", 11.5, "start", INK2)
    legend(c, xr, 196, [("an illustrative session", SERIES[1])])
    c.text(xr, 236, "the chapter reads flow as a", 11.5, "start", INK2, italic=True)
    c.text(xr, 254, "property of this trajectory", 11.5, "start", INK2, italic=True)
    c.text(16, 390, "schematic; band width and session illustrative", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 26
def fig_26_1():
    P = [((-1.4, 0.3), 1.0, 0.9), ((1.5, -0.2), 0.8, 0.8)]

    def s(x, y):
        return sum(hgt * math.exp(-((x - px) ** 2 + (y - py) ** 2) / (2 * w * w)) for (px, py), hgt, w in P)

    def grad(x, y):
        gx = gy = 0.0
        for (px, py), hgt, w in P:
            e = hgt * math.exp(-((x - px) ** 2 + (y - py) ** 2) / (2 * w * w))
            gx += -e * (x - px) / (w * w)
            gy += -e * (y - py) / (w * w)
        return gx, gy

    def ascend(x, y):
        pts = [(x, y)]
        for _ in range(4000):
            gx, gy = grad(x, y)
            gn = math.hypot(gx, gy)
            if gn < 1e-4:
                break
            st = min(0.04, 0.5 * gn)
            x, y = x + st * gx / gn, y + st * gy / gn
            pts.append((x, y))
        return pts

    starts = [(-3.2, 1.9), (-3.2, -1.8), (-0.6, 2.0), (-0.5, -2.0), (0.0, 1.0), (0.25, -0.9), (0.6, 2.0),
              (3.2, 1.8), (3.2, -1.9), (0.7, -2.0)]
    paths = [ascend(*q) for q in starts]
    ends = [pt[-1] for pt in paths]
    basin = [0 if math.dist(e, P[0][0]) < math.dist(e, P[1][0]) else 1 for e in ends]
    assert all(min(math.dist(e, P[0][0]), math.dist(e, P[1][0])) < 0.05 for e in ends)
    assert 0 in basin and 1 in basin
    p = reg(_ch(26), "26.1",
            "Schematic: an illustrative engagement surface over a two-dimensional user space, with two peaks; the "
            "curves are its contour lines. Each user path starts at a marked point and climbs greedily, always in "
            "the locally steepest direction, and ends at the peak of the basin it started in, coloured by that "
            "peak. No path crosses into the other basin. This is the chapter's reading of the filter bubble as "
            "basin convergence; Proposition 26.2 is argued in the chapter, not proved or tested.",
            "## 26.4 What the Geometric Framework Prescribes {#26-4-what-the-geometric-framework-prescribes}")
    c = Canvas(720, 400, "Greedy ascent ends at the top of the basin it starts in")
    x0, y0, w, h = 60, 56, 440, 300
    xl, yl = (-3.5, 3.5), (-2.386, 2.386)
    X = lambda u: x0 + w * (u - xl[0]) / (xl[1] - xl[0])
    Y = lambda v: y0 + h * (1 - (v - yl[0]) / (yl[1] - yl[0]))
    _rect(c, x0, y0, w, h, stroke=GRID, width=1)
    nx, ny = 88, 60
    gx = [xl[0] + (xl[1] - xl[0]) * i / nx for i in range(nx + 1)]
    gy = [yl[0] + (yl[1] - yl[0]) * j / ny for j in range(ny + 1)]
    val = [[s(x, y) for x in gx] for y in gy]
    for lev in (0.15, 0.3, 0.45, 0.6, 0.75, 0.9):
        segs = []
        for j in range(ny):
            for i in range(nx):
                corners = [(gx[i], gy[j], val[j][i]), (gx[i + 1], gy[j], val[j][i + 1]),
                           (gx[i + 1], gy[j + 1], val[j + 1][i + 1]), (gx[i], gy[j + 1], val[j + 1][i])]
                cuts = []
                for k in range(4):
                    (xa, ya, va), (xb, yb, vb) = corners[k], corners[(k + 1) % 4]
                    if (va - lev) * (vb - lev) < 0:
                        f = (lev - va) / (vb - va)
                        cuts.append((xa + f * (xb - xa), ya + f * (yb - ya)))
                if len(cuts) == 2:
                    segs.append(cuts)
                elif len(cuts) == 4:
                    segs.append(cuts[:2])
                    segs.append(cuts[2:])
        d = " ".join(f"M{X(a[0]):.1f},{Y(a[1]):.1f} L{X(b[0]):.1f},{Y(b[1]):.1f}" for a, b in segs)
        c.add(f'<path d="{d}" fill="none" stroke="{BORDER}" stroke-width="1"/>')
    for pts, bsn in zip(paths, basin):
        c.polyline([(X(x), Y(y)) for x, y in pts[::4] + [pts[-1]]], SERIES[bsn], 2)
        c.dot(X(pts[0][0]), Y(pts[0][1]), SERIES[bsn], 3.5)
    for k, ((px, py), hgt, _) in enumerate(P):
        c.dot(X(px), Y(py), INK, 5.5, title=f"peak {k + 1}")
    xr = 530
    legend(c, xr, 110, [("ends at the left peak", SERIES[0])])
    legend(c, xr, 134, [("ends at the right peak", SERIES[1])])
    c.dot(xr + 6, 166, INK, 5)
    c.text(xr + 18, 170, "a peak", 11.5, "start", INK2)
    c.text(xr, 194, "small dots: starting points", 11.5, "start", INK2)
    c.text(xr, 212, "lines: contours of the", 11.5, "start", INK2)
    c.text(xr, 230, "engagement surface", 11.5, "start", INK2)
    c.text(xr, 266, "no greedy path leaves", 11.5, "start", INK2, italic=True)
    c.text(xr, 284, "the basin it starts in", 11.5, "start", INK2, italic=True)
    c.text(16, 390, "schematic: illustrative surface; greedy steps along the gradient", 10.5, "start", INK3,
           italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 27
def fig_27_1():
    mu = [(1.2 + 0.9 * t, 1.1 + 3.0 * math.sin(math.pi * t / 10)) for t in range(9)]
    classic = (4.2, 5.7)
    lens = [math.dist(classic, m) for m in mu]
    p = reg(_ch(27), "27.1",
            f"Schematic with an illustrative path: the industry-average centroid μ(t) drifts across a two-dimensional "
            f"design space over eight seasons while a classic design φ(B) stays where it is. The relative position "
            f"δ(t) = φ(B) − μ(t), the chapter's measure of a classic's distinctiveness, changes length (from "
            f"{min(lens):.1f} to {max(lens):.1f} units here) and direction although the design never moves. The "
            f"tangent to the centroid path is the trend vector T(t). Conjectured and untested (Appendix F, F25 to "
            f"F28).",
            "## 27.6 Brand Repositioning as Manifold Navigation {#27-6-brand-repositioning}")
    c = Canvas(720, 400, "A classic holds still while the industry centroid moves")
    x0, y0, k = 60, 52, 44
    X = lambda u: x0 + k * u
    Y = lambda v: y0 + k * (7 - v)
    _rect(c, x0, y0, 10 * k, 7 * k, stroke=GRID, width=1)
    for t in (0, 2, 4, 6, 8):
        c.line(X(mu[t][0]), Y(mu[t][1]), X(classic[0]), Y(classic[1]), INK3, 1.2, dash="4 4")
    c.polyline([(X(x), Y(y)) for x, y in mu], SERIES[0], 2.5, title="industry centroid mu(t)")
    for t, (x, y) in enumerate(mu):
        c.dot(X(x), Y(y), SERIES[0], 3.5, title=f"season {t}")
    t4 = 4
    tx, ty = mu[t4 + 1][0] - mu[t4 - 1][0], mu[t4 + 1][1] - mu[t4 - 1][1]
    tn = math.hypot(tx, ty)
    nx_, ny_ = -ty / tn * 0.45, tx / tn * 0.45          # drawn parallel to the tangent, offset below the path
    bx0, by0 = mu[t4][0] - nx_, mu[t4][1] - ny_
    c.arrow(X(bx0), Y(by0), X(bx0 + 1.4 * tx / tn), Y(by0 + 1.4 * ty / tn), SERIES[2], 2.5)
    c.text(X(bx0) + 4, Y(by0) + 20, "trend T(t)", 11, "start", INK)
    c.text(X(mu[0][0]) - 4, Y(mu[0][1]) + 18, "season 0", 11, "start", INK2)
    c.text(X(mu[8][0]) - 4, Y(mu[8][1]) + 18, "season 8", 11, "middle", INK2)
    c.dot(X(classic[0]), Y(classic[1]), CRITICAL, 6, title="classic phi(B)")
    c.text(X(classic[0]) + 12, Y(classic[1]) - 8, "classic φ(B), fixed", 11.5, "start", INK)
    mx = (mu[2][0] + classic[0]) / 2
    my = (mu[2][1] + classic[1]) / 2
    c.text(X(mx) - 10, Y(my), "δ(2)", 11, "end", INK2, italic=True)
    xr = 520
    legend(c, xr, 110, [("industry centroid μ(t)", SERIES[0])])
    legend(c, xr, 134, [("trend vector T(t)", SERIES[2])])
    legend(c, xr, 158, [("classic φ(B)", CRITICAL)])
    c.text(xr, 196, "dashed: δ(t) = φ(B) − μ(t)", 11.5, "start", INK2)
    c.text(xr, 214, "at seasons 0, 2, 4, 6, 8", 11.5, "start", INK2)
    c.text(xr, 250, "|δ| " + ", ".join(f"{lens[t]:.1f}" for t in (0, 2, 4, 6, 8)), 11.5, "start", INK)
    c.text(16, 390, "schematic; path and positions illustrative", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 28
def fig_28_1():
    courses = [(1.0, 3.0), (2.3, 3.3), (3.6, 3.05), (4.9, 3.35), (6.2, 3.1), (7.5, 3.3), (5.2, 8.2)]
    steps = [math.dist(a, b) for a, b in zip(courses[:-1], courses[1:])]
    build = steps[:-1]
    mb = sum(build) / len(build)
    sd = math.sqrt(sum((s_ - mb) ** 2 for s_ in build) / len(build))
    (ax_, ay_), (bx_, by_), (cx_, cy_) = courses[-3], courses[-2], courses[-1]
    v1, v2 = (bx_ - ax_, by_ - ay_), (cx_ - bx_, cy_ - by_)
    turn = math.degrees(math.acos((v1[0] * v2[0] + v1[1] * v2[1]) / (math.hypot(*v1) * math.hypot(*v2))))
    assert steps[-1] > 3 * mb and turn > 90
    p = reg(_ch(28), "28.1",
            f"Schematic: the menu intuitions of §28.3 drawn as a path through two of the chapter's flavour axes, "
            f"richness and acidity, with illustrative course positions. The first six courses build richness in "
            f"near-equal steps (mean {mb:.2f}, standard deviation {sd:.2f}); the last takes one step of {steps[-1]:.1f} "
            f"in a new direction, turning {turn:.0f} degrees, a high-curvature close. Conjecture 28.1, that meals "
            f"reward contrast as music does, is untested.",
            "## 28.4 Gardening and the Slow Trajectory {#28-4-gardening-and-the-slow-trajectory}")
    c = Canvas(720, 400, "A menu as a trajectory: light start, steady build, contrasting close")
    ax = Axes(c, 80, 52, 400, 300, (0, 10), (0, 10), [], [], "", "acidity")
    c.text(ax.x0 + ax.w / 2, ax.y0 + ax.h + 20, "richness", 11.5, "middle", INK2)
    _rect(c, ax.x0, ax.y0, ax.w, ax.h, stroke=GRID, width=1)
    for (xa, ya), (xb, yb) in zip(courses[:-1], courses[1:]):
        c.arrow(ax.X(xa), ax.Y(ya), ax.X(xb), ax.Y(yb), SERIES[0] if yb < 5 else SERIES[1], 2)
    for k, (x, y) in enumerate(courses):
        c.dot(ax.X(x), ax.Y(y), INK, 4)
        c.text(ax.X(x), ax.Y(y) + 22, str(k + 1), 11, "middle", INK)
    c.text(ax.X(1.0), ax.Y(3.0) - 14, "light start", 11, "start", INK2, italic=True)
    c.text(ax.X(4.3), ax.Y(3.3) - 14, "steady build", 11, "middle", INK2, italic=True)
    c.text(ax.X(5.2) - 10, ax.Y(8.2) - 10, "contrasting close", 11, "end", INK2, italic=True)
    xr = 520
    c.text(xr, 110, "courses 1 to 6:", 11.5, "start", INK)
    c.text(xr, 128, f"steps of {mb:.2f} on average,", 11.5, "start", INK2)
    c.text(xr, 146, f"step_std {sd:.2f}", 11.5, "start", INK2)
    c.text(xr, 182, "course 6 to 7:", 11.5, "start", INK)
    c.text(xr, 200, f"one step of {steps[-1]:.1f}, turning {turn:.0f}°", 11.5, "start", INK2)
    c.text(16, 390, "schematic; course positions illustrative", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 29
def fig_29_1():
    rows = [("Finnish", 288), ("French", 227), ("German", 138), ("Dutch", 88), ("Italian", 49), ("Spanish", 38),
            ("Greek", 33), ("Esperanto", 24), ("Hungarian", 21), ("Latin", 20), ("Portuguese", 10), ("Chinese", 5),
            ("Japanese", 4), ("Polish", 2), ("Swedish", 2), ("Russian", 1), ("Czech", 1)]
    above = [r for r in rows if r[1] >= 20]
    assert len(above) == 10 and len(rows) == 17
    p = reg(_ch(29), "29.1",
            "Matched translation bundles per language in the cross-lingual study, as Chapter 17 and the reference "
            "record them, on a logarithmic scale. Ten languages reach the threshold of 20 bundles (dashed line) and "
            "carry the invariance result. Seven are exploratory, among them Chinese with 5 bundles, all classical "
            "originals rather than translations: the Sinitic gap of this section.",
            "## 29.3 The Origin of the Cross-Modal Sign Flip {#cross-modal-sign-flip}")
    c = Canvas(720, 430, "Matched translation bundles per language: ten reach the threshold")
    x0, w = 170, 470
    lo, hi = 0.8, 400
    X = lambda v: x0 + w * (math.log10(v) - math.log10(lo)) / (math.log10(hi) - math.log10(lo))
    top, rh = 52, 19
    bot = top + rh * len(rows)
    for v in (1, 3, 10, 30, 100, 300):
        c.line(X(v), top - 4, X(v), bot, GRID, 1)
        c.text(X(v), bot + 16, str(v), 11, "middle", INK2)
    c.text(x0 + w / 2, bot + 34, "bundles (logarithmic scale)", 11.5, "middle", INK2)
    for i, (lang, n) in enumerate(rows):
        y = top + rh * (i + 0.5)
        col = SERIES[0] if n >= 20 else (CRITICAL if lang == "Chinese" else INK3)
        c.text(x0 - 12, y + 4, lang, 11.5, "end", INK if n >= 20 or lang == "Chinese" else INK2)
        c.line(X(lo), y, X(n), y, col, 2)
        c.dot(X(n), y, col, 4, title=f"{lang} {n}")
        c.text(X(n) + 10, y + 4, str(n), 10.5, "start", INK)
    c.line(X(20), top - 8, X(20), bot, INK2, 1.5, dash="4 4")
    c.text(X(20) - 6, bot - 6, "threshold 20", 10.5, "end", INK2, italic=True)
    c.text(16, 420, "Chinese: classical originals, not translations (§29.2)", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 30
def fig_30_1():
    rb, rm = 0.126, -0.076
    assert rb > 0 > rm
    p = reg(_ch(30), "30.1",
            "Schematic of the two-panel figure the running example describes. Each panel shows only the sign of the "
            "measured rank correlation between internal coherence, pair_sim_mean, and reception; the lines are not "
            "fitted and no data points are drawn. Books (n = 4,998): ρ = +0.126, 8.4σ, with Goodreads rating. "
            "Music (n = 24,801): ρ = −0.076, p = 5×10⁻³³, with log(1 + listens).",
            "## 30.1 Return to the Scalar {#return-to-the-scalar}")
    c = Canvas(720, 400, "Priya's plot: the same axis, opposite signs")
    size_w, size_h, y0 = 270, 230, 70
    for k, (x0, mod, ylab, sign, lab1, lab2) in enumerate((
            (80, "books", "Goodreads rating", 1, "ρ = +0.126, 8.4σ", "n = 4,998"),
            (410, "music", "log(1 + listens)", -1, "ρ = −0.076, p = 5×10⁻³³", "n = 24,801"))):
        _rect(c, x0, y0, size_w, size_h, stroke=GRID, width=1)
        ya = y0 + size_h * (0.5 + 0.22 * sign)
        yb = y0 + size_h * (0.5 - 0.22 * sign)
        c.line(x0 + 20, ya, x0 + size_w - 20, yb, SERIES[k], 3)
        c.text(x0 + size_w / 2, y0 + size_h + 18, "pair_sim_mean (coherence)", 11.5, "middle", INK2)
        c.text(x0 - 14, y0 + size_h / 2, ylab, 11.5, "middle", INK2, rotate=-90)
        c.text(x0 + size_w / 2, 58, mod, 12, "middle", INK, "600")
        ty = y0 + 26 if sign < 0 else y0 + size_h - 34
        c.text(x0 + size_w - 16 if sign < 0 else x0 + 16, ty, lab1, 11, "end" if sign < 0 else "start", INK)
        c.text(x0 + size_w - 16 if sign < 0 else x0 + 16, ty + 18, lab2, 11, "end" if sign < 0 else "start", INK2)
    c.text(16, 390, "schematic: direction of the measured correlation only; no data points", 10.5, "start", INK3,
           italic=True)
    c.save(p)


# ------------------------------------------------------------------ appendix B
def fig_B_1():
    sizes = [4, 3, 3, 2, 2, 2, 1, 1]
    books = [a for a, n in enumerate(sizes) for _ in range(n)]
    order = list(range(len(books)))
    random.Random(3).shuffle(order)
    plain = [[] for _ in range(5)]
    for k, i in enumerate(order):
        plain[k % 5].append(books[i])
    group = [[] for _ in range(5)]
    for a in sorted(range(len(sizes)), key=lambda a: -sizes[a]):
        f = min(range(5), key=lambda f: (len(group[f]), f))
        group[f].extend([a] * sizes[a])
    split_plain = [a for a in range(len(sizes)) if sum(1 for f in plain if a in f) > 1]
    assert all(sum(1 for f in group if a in f) == 1 for a in range(len(sizes)))
    assert len(split_plain) >= 1
    p = reg(APP + "appendix-b-reproduction-cookbook.md", "B.1",
            f"Schematic of §B.7.1 with 8 illustrative authors (colours) and their books (squares). A plain 5-fold "
            f"split scatters an author's books across folds ({len(split_plain)} of the 8 authors here), so a model "
            f"can learn an author's rating from the training folds and be scored on the same author in the test "
            f"fold. GroupKFold puts every book of an author in one fold, so each test fold holds only unseen "
            f"authors. For music the group is the artist.",
            "### B.7.2 Genre Residualization (Phase 2 / Phase 4 Within-Genre)")
    c = Canvas(720, 290, "Group-disjoint folds keep each author's books in one fold")
    sq, gapx = 18, 56
    for k, (folds, name, x0) in enumerate(((plain, "plain 5-fold: authors split", 50),
                                           (group, "GroupKFold: one fold per author", 400))):
        c.text(x0 + 2.5 * gapx - 10, 64, name, 12, "middle", INK, "600")
        base = 196
        for f, items in enumerate(folds):
            fx = x0 + f * gapx
            for r, a in enumerate(sorted(items)):
                _rect(c, fx, base - (r + 1) * (sq + 4), sq, sq, SERIES[a], rx=3)
            c.text(fx + sq / 2, base + 18, f"fold {f + 1}", 10.5, "middle", INK2)
        c.line(x0 - 8, base + 2, x0 + 4 * gapx + sq + 8, base + 2, GRID, 1)
    c.text(16, 276, "illustrative authors and books; squares of one colour are one author's books", 10.5, "start",
           INK3, italic=True)
    c.save(p)


def fig_B_2():
    zf = lambda r, n: r * math.sqrt(n - 2) / math.sqrt(1 - r * r)
    pts = [("books", 0.241, 17.0, 4998), ("books, residualized", 0.093, 6.5, 4998), ("fiction", 0.131, 6.2, 2250),
           ("music, spectrum", 0.302, 49.8, 24801), ("music, spectrum, resid.", 0.177, 28.3, 24801),
           ("music, hand, resid.", 0.043, 6.7, 24801)]
    for _, r, z, n in pts:
        assert abs(zf(r, n) - z) < 0.6, (r, z, zf(r, n))
    p = reg(APP + "appendix-b-reproduction-cookbook.md", "B.2",
            "The conversion of §B.9, z ≈ R √(n − 2) / √(1 − R²), drawn for the three sample sizes of the headline "
            "results, with the six printed pairs of R and z: books 0.241 and 17σ, residualized 0.093 and 6.5σ; "
            "fiction 0.131 and 6.2σ; the music spectrum Lasso 0.302 and 49.8σ, residualized 0.177 and 28.3σ; music "
            "hand features, residualized, 0.043 and 6.7σ. Each printed z lies within 0.6 of its curve. At a fixed R, "
            "z grows as the square root of n.",
            "## B.10 End-to-End Compute Budget")
    c = Canvas(720, 400, "The printed z-scores follow from R and the sample size")
    ax = Axes(c, 70, 52, 520, 280, (0, 0.32), (0, 55), [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3], [0, 10, 20, 30, 40, 50],
              "correlation R", "z-score")
    rs = [0.32 * i / 160 for i in range(161)]
    for j, n in enumerate((24801, 4998, 2250)):
        c.polyline([(ax.X(r), ax.Y(zf(r, n))) for r in rs], SERIES[j], 2, title=f"n = {n}")
        c.text(ax.X(0.32) + 8, ax.Y(zf(0.32, n)) + 4, f"n = {n:,}", 11, "start", INK2)
    col = {24801: SERIES[0], 4998: SERIES[1], 2250: SERIES[2]}
    keys = {  # number, label offset, key text
        "books": ("1", (-9, -7, "end"), "books, raw: R 0.241, 17σ"),
        "books, residualized": ("2", (-9, -7, "end"), "books, genre-residualized: 0.093, 6.5σ"),
        "fiction": ("3", (9, 15, "start"), "fiction only: 0.131, 6.2σ"),
        "music, spectrum": ("4", (-9, -7, "end"), "music spectrum Lasso, raw: 0.302, 49.8σ"),
        "music, spectrum, resid.": ("5", (-9, -7, "end"), "music spectrum Lasso, resid.: 0.177, 28.3σ"),
        "music, hand, resid.": ("6", (-9, -7, "end"), "music hand features, resid.: 0.043, 6.7σ"),
    }
    for name, r, z, n in pts:
        c.dot(ax.X(r), ax.Y(z), col[n], 5, title=f"{name}: R {r}, z {z}")
        num, (dx, dy, anc), _ = keys[name]
        c.text(ax.X(r) + dx, ax.Y(z) + dy, num, 11, anc, INK, "600")
    for i, (name, r, z, n) in enumerate(pts):
        num, _, txt = keys[name]
        c.text(92, 74 + 17 * i, f"{num}  {txt}", 11, "start", INK2)
    c.save(p)
