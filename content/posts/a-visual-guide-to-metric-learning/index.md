---
title: "Learning to Compare: A Visual Guide to Metric Learning for Wildlife Re-ID"
description: An intuition-first, visual guide to metric learning — how machines learn to tell individual animals apart for conservation re-identification.
date: 2026-06-16
image: /images/posts/a-visual-guide-to-metric-learning/cover.png
tags: ["AI", "vision", "metric learning", "identification"]
distances:
  - name: Euclidean
    desc: "Straight-line distance between two vectors. Intuitive, but sensitive to length — two embeddings can point the same way yet sit far apart if their magnitudes differ."
  - name: Cosine
    desc: "Measures the angle between two vectors, ignoring length. Two embeddings that point the same direction count as close regardless of magnitude — usually the better fit for normalized embeddings."
metric_losses:
  - name: Contrastive
    desc: "The original idea: take pairs. Pull two images of the same individual together; push two different individuals apart beyond a margin. Simple, but it judges each pair in isolation."
  - name: Triplet Margin
    desc: "Look at three images at once — an anchor, a positive (same individual), and a negative (different one). Force the anchor closer to the positive than to the negative by a margin. Relative comparison beats absolute thresholds."
  - name: Circle
    desc: "Not every pair deserves equal weight. Circle loss re-weights each similarity by how far it still has to move, giving a clearer, more adaptive decision boundary on noisy data."
  - name: ArcFace
    desc: "Place every embedding on a sphere and add an angular margin between classes. Working with angles instead of raw distance carves crisp, well-separated regions — the go-to for faces."
---

## The problem: a gallery that never stops growing

## Why classification hits a wall

![Classification needs fixed slots; metric learning just adds a point](./images/classification-wall.svg)
*A classifier needs a slot per identity — a new individual means a retrain. Metric learning just drops another point into the space.*

## The core idea: turn images into points

![Images are embedded as points; the same individual forms a cluster](./images/embedding-space.svg)
*Each image becomes a point. Same individual, nearby points — identification turns into nearest-neighbour search.*

## Shaping the space: a short history of losses

## Making it work in practice

## Where this shows up in conservation
