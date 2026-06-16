# Design: A Visual Guide to Metric Learning

**Date:** 2026-06-16
**Type:** Blog post (foundational reference)
**Slug:** `a-visual-guide-to-metric-learning`

## Concept & Positioning

A foundational, intuition-first, canonical reference on **metric learning** — the
"theory hub" that earthtoolsmaker's applied posts link back to. It teaches the
general idea, grounded throughout in real conservation projects (bear faces,
trout, salmon, seals), and stays deliberately one level above the existing
[bear face recognition guide](../../content/posts/bear-identification-with-metric-learning-guide/index.md),
which remains the applied case study.

The post does **not** re-tread the bear post's project specifics (dataset,
hyperparameter search, results tables). It explains the *why* and *how* of
metric learning as a paradigm, so any future re-ID post (trout, seal, salmon)
can link to it instead of re-explaining embeddings and losses.

### Audience & depth

- **Primary reader:** conservation technologists and curious practitioners.
- **Depth:** intuition-first. Lead with diagrams and analogies; equations stay
  light/optional. No heavy code — a tiny pseudocode aside at most, only if it
  earns its place.

### Title

- **Primary:** "Learning to Compare: A Visual Guide to Metric Learning for Wildlife Re-ID"
- Alternatives: "Metric Learning, Visually: How Machines Learn to Tell Individuals Apart" · "What Is Metric Learning? A Visual Guide for Conservation"

### Front matter

```yaml
title: "Learning to Compare: A Visual Guide to Metric Learning for Wildlife Re-ID"
description: An intuition-first, visual guide to metric learning — how machines learn to tell individual animals apart for conservation re-identification.
date: 2026-06-16
image: /images/posts/a-visual-guide-to-metric-learning/cover.png
tags: ["AI", "vision", "metric learning", "identification"]
metric_losses:
  - name: Contrastive
    desc: "..."
  - name: Triplet Margin
    desc: "..."
  - name: Circle
    desc: "..."
  - name: ArcFace
    desc: "..."
distances:
  - name: Euclidean
    desc: "..."
  - name: Cosine
    desc: "..."
```

(Reuse the `threats` shortcode pattern from the bear post for tap-through cards;
front-matter list keys `metric_losses` and `distances`.)

## Structure (4 pillars + conservation bookends)

| # | Section | Core idea | Visual |
|---|---------|-----------|--------|
| — | **Hook / intro** | Wildlife populations keep growing — new bears, new trout appear constantly. You cannot retrain a fixed classifier every time. Frame the re-ID problem. | Cover SVG |
| 1 | **Why classification breaks** | Softmax/classification needs fixed, known classes; a new individual means a new output slot and a retrain. The open-set wall. | SVG: fixed class slots vs ever-growing gallery |
| 2 | **The core idea: embeddings & distance** | Map each image to a vector; "same individual" becomes "close together" in the embedding space. Euclidean vs cosine distance. | SVG: embedding space (centerpiece) + distance panel; `distances` tap-through cards |
| 3 | **Shaping the space: the loss zoo** | Told as an evolution of ideas: pairs (Contrastive) → triplets (Triplet Margin) → adaptive boundaries (Circle) → angular margins (ArcFace). Intuition for each. | SVG: pull/push + triplet geometry + angular margin; `metric_losses` tap-through cards |
| 4 | **Making it work in practice** | Hard-negative mining (why hard examples teach the most), evaluation (accuracy@k / recall@k), and visualizing the space (UMAP / t-SNE). | SVG: easy / semi-hard / hard negatives around an anchor |
| — | **Closing** | Conservation payoff; cross-links to applied posts; interactive demo. | `demo_cta` |

## SVG Diagrams

All authored to match the established visual language seen in
`content/posts/*/images/*.svg` and `assets/images/projects/*/diagrams/*.svg`:

- Responsive `viewBox`; fonts Mulish (sans) + Newsreader (serif titles).
- Coral accent `#e29578` for arrows and step tags; text `#161616`; muted desc `#60626a`.
- Linear gradients, soft drop shadows, rounded rects.
- Any motion guarded by `@media (prefers-reduced-motion: reduce)`.
- Reuse existing animal glyphs (bear, trout `<use>` defs) so figures feel of-a-piece.

Proposed set (5–6 new SVGs; #4 may merge into #3 or #5 to trim):

1. **Cover** — embedding-space hero.
2. **Classification wall** — fixed class slots vs an ever-growing gallery of new individuals.
3. **Embedding space** (centerpiece) — images → dots, same individual clustered, a query pulling its nearest neighbours.
4. **Distance** — Euclidean vs cosine, two panels.
5. **Loss intuition** — multi-panel: contrastive pull/push · triplet (anchor / positive / negative + margin) · ArcFace angular margin on a sphere.
6. **Mining** — easy / semi-hard / hard negatives around an anchor.

Stored as a page bundle: `content/posts/a-visual-guide-to-metric-learning/images/`.

## Cross-linking (the hub role)

- → [bear face recognition guide]({{< ref "posts/bear-identification-with-metric-learning-guide" >}}) — applied case study + demo.
- → [how to prepare data for identification]({{< ref "posts/how-to-prepare-data-for-identification" >}}).
- → [identify individuals with local feature matching]({{< ref "posts/local-feature-matching-lightglue" >}}) — contrast: local features vs learned global embeddings.
- Closing nod to trout / seal / salmon re-ID projects.
- Interactive demo via `{{< demo_cta "/demos/bear_identification/" >}}`.

## Out of Scope (YAGNI)

- No project-specific dataset/EDA, hyperparameter search, or results tables (those live in the bear post).
- No heavy code tutorial or training-loop walkthrough.
- No new shortcodes or layout changes — reuse `threats` and `demo_cta` as-is.

## Success Criteria

- Reads as a standalone, intuition-first explainer that a newcomer can follow without the bear post.
- Every pillar (why-not-classification, embeddings & distance, loss zoo, mining/eval/viz) is covered.
- Diagrams are visually consistent with existing posts (palette, fonts, motion guard).
- Tap-through cards render via `threats`; demo CTA renders via `demo_cta`.
- Builds cleanly with `hugo` (no broken refs, images resolve).
