# Monitoring Smolt Salmon Migration with Sonar — Alignment

**Date:** 2026-06-15
**Status:** Approved
**Base:** latest `origin/main` (worktree `worktree-smolt-revamp`). One PR per project page.
**Scope:** The smolt page is already editorial/well-structured. This is an alignment pass to match the fire/salmon/elephant system — not a rewrite.

## Changes

1. **Front matter:** add `tagline` + `stats`. Stats: `8–14 cm` smolt detected · `day & night` (sonar) · `automated` counting. Tagline e.g. *"Counting juvenile salmon by sonar as they run the gauntlet downstream to the ocean."*
2. **One new animated SVG pipeline diagram** (house teal/coral system), placed right after the lede (the overview beat the page lacks). Steps: **Record → Detect → Measure → Count**:
   - Record — an ARIS sonar transducer casting a fan beam into the water, a smolt in the beam.
   - Detect — a dark sonar frame (range arcs + noise) with a bright smolt blob, red bounding box + AI chip.
   - Measure — the boxed smolt with a length caliper + "12 cm" pill (size estimation).
   - Count — a dashed trigger line with a smolt crossing it, a downstream arrow + "+1" badge.
   The existing technical figures (preprocess before/after, YOLO tasks, length estimation, counting trigger, ARIS frame) all stay in their sections — the diagram is a complementary overview.
3. **Pills:** convert the "Why accurate counting matters" 4-bullet list into the interactive pills component. Needs the key-argument shortcode (the version on fire PR #87): generalize `threats.html` here too (superset, default key `threats`, overridable positional arg) and call `{{< threats "why_count" >}}` with a `why_count:` front-matter list. Reuses the `.threats` CSS already on `main`.
4. **Polish:** switch the two inline-styled video captions (`<em style=...>`) to the `.media-caption` class (already on `main`).

## New primitives (in the diagram)

A **sonar frame** (deep blue-teal rounded tile + faint range arcs + light noise), a bright **smolt blob** (orange-red elongated mark, as fish appear in sonar), an **ARIS transducer + fan beam**, a length **caliper**, and a **trigger line + direction arrow**. Positioning transform on an outer `<g>`, animation class on an inner `<g>` (avoid the transform-attribute override).

## Non-goals

- No rewrite of the existing well-structured body; no removal of the technical figures.
- No second (detection close-up) diagram — the existing YOLO/tracking figures + video already cover that.

## Merge note

This PR generalizes `threats.html` with a positional key arg — the same superset as the open fire PR #87. Whichever merges second keeps this version (identical); trivial conflict.

## Verification

- `hugo` builds clean; screenshot the page (hero+stats, pipeline diagram, pills, captions); diagram animates and degrades with reduced motion.
