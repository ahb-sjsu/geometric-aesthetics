#!/usr/bin/env python3
"""
Build HTML for Book 13: Geometric Aesthetics.

Reads markdown from ./book/src/ (+appendices/) in this repo, runs each
through pandoc with --katex, and wraps the resulting body HTML into a
page template derived from the existing Geometric Ethics / Geometric
Politics chapter pages.

Output goes to the erisml-lib website (sibling checkout) at
`../erisml-lib/docs/geometric-aesthetics/` by default. Override with
the `AESTHETICS_OUT_DIR` environment variable.
"""

from __future__ import annotations

import html
import os
import re
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
SRC = REPO_ROOT / "book" / "src"
APP_SRC = SRC / "appendices"

DEFAULT_OUT = (REPO_ROOT / ".." / "erisml-lib" / "docs" / "geometric-aesthetics").resolve()
OUT = Path(os.environ.get("AESTHETICS_OUT_DIR", str(DEFAULT_OUT)))
OUT.mkdir(parents=True, exist_ok=True)

BOOK_TITLE = "Geometric Aesthetics"
BOOK_SUBTITLE = "The Mathematical Structure of Judgment"
AUTHOR = "Andrew H. Bond"
AFFIL = "Senior Member, IEEE &middot; Department of Computer Science &middot; San Jose State University"
BOOK_NUMBER_LABEL = "Spring 2026 &middot; Book 13 of the Geometric Series"

# Parts (matches _BOOK_REFERENCE.md TOC)
PARTS = [
    ("Part I: The Problem (Ch. 1–3)", [1, 2, 3]),
    ("Part II: Foundations (Ch. 4–9)", [4, 5, 6, 7, 8, 9]),
    ("Part III: Dynamics (Ch. 10–15)", [10, 11, 12, 13, 14, 15]),
    ("Part IV: Meta (Ch. 16–19)", [16, 17, 18, 19]),
    ("Part V: Applications (Ch. 20–28)", [20, 21, 22, 23, 24, 25, 26, 27, 28]),
    ("Part VI: Conclusion (Ch. 29–30)", [29, 30]),
]

APPENDICES = [
    ("a", "Related Work and Differentiation", "appendix-a-related-work-and-differentiation.md"),
    ("b", "Reproduction Cookbook", "appendix-b-reproduction-cookbook.md"),
    ("c", "Human-Subjects Research Roadmap", "appendix-c-human-subjects-research-roadmap.md"),
    ("d", "End-to-End Case Studies", "appendix-d-end-to-end-case-studies.md"),
    ("e", "Skeptic's Appendix — Objections, Alternatives, Failure Modes",
     "appendix-e-skeptics-appendix-objections-alternatives-failure-modes.md"),
    ("f", "Mathematical Ledger — Status of Formal Claims",
     "appendix-f-mathematical-ledger-status-of-formal-claims.md"),
]


# -----------------------------------------------------------------------------
# Discover chapter source files and extract (number, title, short_title, slug)
# -----------------------------------------------------------------------------

CHAP_RE = re.compile(r"^# Chapter (\d+)(?:[:—\- ]+)(.+?)\s*(?:\{#.*\})?\s*$")


def read_title(md_path: Path) -> tuple[int, str, str]:
    """Return (chapter_number, full_title, slug_for_filename)."""
    with md_path.open(encoding="utf-8") as f:
        first = f.readline().strip()
    m = CHAP_RE.match(first)
    if not m:
        raise RuntimeError(f"Could not parse title line in {md_path}: {first!r}")
    num = int(m.group(1))
    # Clean up em-dash separators — normalize so we can drop a "Chapter N: " prefix
    rest = m.group(2).strip()
    # The title after "Chapter N — " or "Chapter N: " - normalize to use em-dash
    return num, rest, md_path.stem  # stem like "chapter-17-empirical-..."


def chapter_slug(num: int, stem: str) -> str:
    """Convert stem 'chapter-17-empirical-...' -> 'chapter-17-empirical-...' (strip zero-padding)."""
    # Strip leading zero: chapter-01-foo -> chapter-1-foo
    m = re.match(r"chapter-0*(\d+)-(.+)$", stem)
    if m:
        return f"chapter-{int(m.group(1))}-{m.group(2)}"
    return stem


def full_title(num: int, rest: str) -> str:
    """Build display title like 'Chapter 1: Introduction — Why Geometry?'."""
    # rest might already be "Introduction — Why Geometry?" (good) or subtitle only
    return f"Chapter {num}: {rest}"


# Build chapter registry
chapters: dict[int, dict] = {}
for md in sorted(SRC.glob("chapter-*.md")):
    num, rest, stem = read_title(md)
    slug = chapter_slug(num, stem)
    chapters[num] = {
        "num": num,
        "md": md,
        "title_rest": rest,
        "title": full_title(num, rest),
        "slug": slug,
        "html_name": slug + ".html",
    }

assert len(chapters) == 30, f"Expected 30 chapters, got {len(chapters)}"
print(f"Found {len(chapters)} chapters.")


# Appendix registry
appendices = []
for letter, title_rest, fname in APPENDICES:
    md = APP_SRC / fname
    if not md.exists():
        raise RuntimeError(f"Missing appendix file: {md}")
    slug = f"appendix-{letter}-" + re.sub(r"[^a-z0-9]+", "-",
        title_rest.lower()).strip("-")
    appendices.append({
        "letter": letter,
        "md": md,
        "title_rest": title_rest,
        "title": f"Appendix {letter.upper()}: {title_rest}",
        "html_name": slug + ".html",
    })


# -----------------------------------------------------------------------------
# Nav (prev/next) computation
# -----------------------------------------------------------------------------

ORDERED: list[dict] = [chapters[i] for i in sorted(chapters.keys())] + appendices


def nav_for(idx: int) -> tuple[str, str]:
    """Return (prev_link_html, next_link_html)."""
    if idx > 0:
        p = ORDERED[idx - 1]
        p_label = p["title"]
        p_short = (p["title"] if len(p["title"]) < 64 else p["title"][:60].rstrip() + "…")
        prev_html = f'<a href="{p["html_name"]}" class="nav-prev">&larr; {html.escape(p_short)}</a>'
    else:
        prev_html = '<span class="nav-prev"></span>'
    if idx < len(ORDERED) - 1:
        n = ORDERED[idx + 1]
        n_short = (n["title"] if len(n["title"]) < 64 else n["title"][:60].rstrip() + "…")
        next_html = f'<a href="{n["html_name"]}" class="nav-next">{html.escape(n_short)} &rarr;</a>'
    else:
        next_html = '<span class="nav-next"></span>'
    return prev_html, next_html


# -----------------------------------------------------------------------------
# Page template
# -----------------------------------------------------------------------------

NAV_LINKS = """
        <li><a href="../geometric-medicine/index.html">Medicine</a></li>
        <li><a href="../book/index.html">Ethics</a></li>
        <li><a href="../geometric-methods/index.html">Methods</a></li>
        <li><a href="../geometric-reasoning/index.html">Reasoning</a></li>
        <li><a href="../geometric-economics/index.html">Economics</a></li>
        <li><a href="../geometric-law/index.html">Law</a></li>
        <li><a href="../geometric-cognition/index.html">Cognition</a></li>
        <li><a href="../geometric-communication/index.html">Communication</a></li>
        <li><a href="../geometric-education/index.html">Education</a></li>
        <li><a href="../geometric-politics/index.html">Politics</a></li>
        <li><a href="../geometric-ai/index.html">AI</a></li>
        <li><a href="index.html" class="active">Aesthetics</a></li>
        <li><a href="../index.html">Home</a></li>
"""

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title} &mdash; Geometric Aesthetics</title>
  <meta name="description" content="{meta_desc}">
  <link rel="stylesheet" href="../assets/css/style.css">
  <link rel="stylesheet" href="../book/book.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,300;0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
</head>

<body>
  <nav id="main-nav">
    <div class="nav-inner">
      <a href="../index.html" class="nav-brand">
        <span class="brand-symbol">A</span>
        <span class="brand-text">Geometric Aesthetics</span>
      </a>
      <button class="nav-toggle" aria-label="Toggle menu">
        <span></span><span></span><span></span>
      </button>
      <ul class="nav-links">
{nav_links}
      </ul>
    </div>
  </nav>

  <article class="book-chapter">
    <div class="chapter-container">
      <nav class="breadcrumb" aria-label="Breadcrumb">
        <a href="../index.html">Geometric Series</a>
        <span class="breadcrumb-sep">&rsaquo;</span>
        <a href="index.html">Geometric Aesthetics</a>
        <span class="breadcrumb-sep">&rsaquo;</span>
        <span class="breadcrumb-current">{crumb_title}</span>
      </nav>
      <div class="chapter-nav-top">
        {prev_top}
        <a href="index.html" class="nav-toc">Contents</a>
        {next_top}
      </div>

      <div class="chapter-content">
{body_html}
      </div>

      <div class="chapter-nav-bottom">
        {prev_bot}
        <a href="index.html" class="nav-toc">Contents</a>
        {next_bot}
      </div>
    </div>
  </article>

  <footer class="book-footer">
    <p>&copy; 2026 Andrew H. Bond. <em>Geometric Aesthetics: The Mathematical Structure of Judgment.</em></p>
    <p class="footer-note">Beauty is not a number. It is a geometry.</p>
  </footer>

  <script>
    window.addEventListener('scroll', () => {{
      document.getElementById('main-nav').classList.toggle('scrolled', window.scrollY > 20);
    }});
    document.querySelector('.nav-toggle')?.addEventListener('click', function() {{
      document.querySelector('.nav-links').classList.toggle('open');
    }});
  </script>
  <script>
    // Pandoc --katex outputs <span class="math inline"> and <span class="math display">.
    // This script renders them with KaTeX once the library loads.
    document.addEventListener("DOMContentLoaded", function() {{
      if (typeof katex === 'undefined') return;
      var mathElements = document.getElementsByClassName("math");
      for (var i = 0; i < mathElements.length; i++) {{
        var texText = mathElements[i].firstChild;
        if (mathElements[i].tagName === "SPAN" && texText) {{
          katex.render(texText.data, mathElements[i], {{
            displayMode: mathElements[i].classList.contains('display'),
            throwOnError: false
          }});
        }}
      }}
    }});
  </script>
</body>
</html>
"""


# -----------------------------------------------------------------------------
# Markdown -> HTML via pandoc
# -----------------------------------------------------------------------------

def md_to_html(md_path: Path) -> str:
    """Run pandoc on the markdown file and return body HTML."""
    result = subprocess.run(
        ["pandoc",
         "--from=markdown+smart+tex_math_dollars+fenced_code_blocks+backtick_code_blocks+yaml_metadata_block",
         "--to=html5",
         "--katex",
         "--section-divs",
         "--shift-heading-level-by=0",
         str(md_path)],
        capture_output=True, text=True, check=True, encoding="utf-8"
    )
    return result.stdout


# -----------------------------------------------------------------------------
# Render chapters + appendices
# -----------------------------------------------------------------------------

written = []

for idx, item in enumerate(ORDERED):
    body = md_to_html(item["md"])
    prev_html, next_html = nav_for(idx)
    page_title = item["title"]
    meta_desc = html.escape(
        f"{page_title} from Geometric Aesthetics: The Mathematical Structure of Judgment by Andrew H. Bond.")
    html_out = PAGE_TEMPLATE.format(
        page_title=html.escape(page_title),
        meta_desc=meta_desc,
        nav_links=NAV_LINKS,
        crumb_title=html.escape(page_title),
        prev_top=prev_html,
        next_top=next_html,
        prev_bot=prev_html,
        next_bot=next_html,
        body_html=body,
    )
    out_path = OUT / item["html_name"]
    out_path.write_text(html_out, encoding="utf-8")
    written.append(out_path.name)
    print(f"  wrote {out_path.name}")


# -----------------------------------------------------------------------------
# Build the index.html
# -----------------------------------------------------------------------------

def short_title(num: int) -> str:
    return chapters[num]["title_rest"]


def short_title_for_toc(num: int) -> str:
    # Keep a short-ish form
    t = chapters[num]["title_rest"]
    # Drop subtitle after em-dash/colon if too long
    if len(t) > 80:
        t = t.split("—")[0].strip(" :")
    return t


parts_html_chunks = []
for pname, nums in PARTS:
    items = []
    for n in nums:
        c = chapters[n]
        label = f"Chapter {n}: {short_title_for_toc(n)}"
        items.append(f'            <li><a href="{c["html_name"]}">{html.escape(label)}</a></li>')
    parts_html_chunks.append(f"""        <div class="toc-part">
          <h3>{html.escape(pname)}</h3>
          <ol class="toc-chapters">
{chr(10).join(items)}
          </ol>
        </div>""")

# appendices part
app_items = []
for a in appendices:
    label = f"Appendix {a['letter'].upper()}: {a['title_rest']}"
    app_items.append(f'            <li><a href="{a["html_name"]}">{html.escape(label)}</a></li>')
parts_html_chunks.append(f"""        <div class="toc-part">
          <h3>Appendices</h3>
          <ol class="toc-chapters" style="list-style: upper-alpha;">
{chr(10).join(app_items)}
          </ol>
        </div>""")

parts_html = "\n".join(parts_html_chunks)

ABSTRACT = """
          <p class="body-text">Aesthetic judgment, this book argues, is not a point on a line.
          It is a location in a space &mdash; a space with dimensions, distances, directions,
          regimes, and curvature. When we flatten that structure into a scalar (a four-star
          rating, a Metacritic score, a number-one hit), we lose the information that matters
          most: which qualities are present, where uncertainty concentrates, how judgment
          shifts across genres, and where the rules discontinuously change.</p>

          <p class="body-text">The argument is empirical as well as philosophical. We
          present evidence from <strong>$n{=}4{,}998$ Gutenberg&#8596;Goodreads books</strong>
          (discovery $R{=}0.241$, $17\\sigma$) and <strong>$n{=}24{,}801$ music tracks</strong>
          from FMA-Medium ($28\\sigma$ after genre residualization), including a strong
          <strong>cross-lingual invariance</strong> signal ($\\rho \\approx 0.70$ on Hellinger
          and Mahalanobis features across six language families) and a
          <strong>cross-modality sign flip</strong>: the same geometric feature that rewards
          continuity in books ($\\rho{=}{+}0.126$, $8.4\\sigma$) punishes it in music
          ($\\rho{=}{-}0.076$, $p{=}5\\times10^{-33}$). Books reward coherence; music rewards
          contrast. The aesthetic geometry has directionality that is modality-specific,
          and that directionality is measurable.</p>
"""

INDEX_TEMPLATE = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Book Contents &mdash; Geometric Aesthetics</title>
  <meta name="description" content="Book Contents from Geometric Aesthetics: The Mathematical Structure of Judgment by Andrew H. Bond.">
  <link rel="stylesheet" href="../assets/css/style.css">
  <link rel="stylesheet" href="../book/book.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,300;0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
</head>
<body>
  <nav id="main-nav">
    <div class="nav-inner">
      <a href="../index.html" class="nav-brand">
        <span class="brand-symbol">A</span>
        <span class="brand-text">Geometric Aesthetics</span>
      </a>
      <button class="nav-toggle" aria-label="Toggle menu">
        <span></span><span></span><span></span>
      </button>
      <ul class="nav-links">
{NAV_LINKS}
      </ul>
    </div>
  </nav>

  <section class="book-index">
    <div class="chapter-container">
      <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; letter-spacing: 0.1em; color: var(--text-muted); margin-bottom: 8px;">BOOK 12 &middot; THE GEOMETRIC SERIES</div>
      <h1 class="book-main-title">{BOOK_TITLE}</h1>
      <h2 class="book-subtitle">{BOOK_SUBTITLE}</h2>
      <p class="book-author">{AUTHOR}<br>
        <span class="author-affiliation">{AFFIL}</span>
      </p>
      <p class="book-date">{BOOK_NUMBER_LABEL}</p>

      <div class="book-abstract" style="max-width: 780px; margin: 32px auto 48px; font-family: 'Crimson Pro', serif;">
{ABSTRACT}
      </div>

      <div class="toc-grid">
{parts_html}
      </div>
    </div>
  </section>

  <footer class="book-footer">
    <p>&copy; 2026 Andrew H. Bond. <em>Geometric Aesthetics: The Mathematical Structure of Judgment.</em></p>
    <p class="footer-note">Beauty is not a number. It is a geometry.</p>
  </footer>
  <script>document.querySelector('.nav-toggle')?.addEventListener('click', function() {{ document.querySelector('.nav-links').classList.toggle('open'); }});</script>
  <script>
    document.addEventListener("DOMContentLoaded", function() {{
      if (typeof renderMathInElement === 'undefined') return;
      renderMathInElement(document.body, {{
        delimiters: [
          {{left: "$$", right: "$$", display: true}},
          {{left: "$", right: "$", display: false}}
        ],
        throwOnError: false
      }});
    }});
  </script>
</body>
</html>
"""

index_out = OUT / "index.html"
index_out.write_text(INDEX_TEMPLATE, encoding="utf-8")
print(f"wrote {index_out.name}")
print(f"\nTotal files: {len(written) + 1} (including index.html)")
