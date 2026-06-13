# Logo wordmark redesign

**Date:** 2026-06-13
**Status:** Approved design, pending implementation

## Goal

Replace the EarthToolsMaker text wordmark with a cleaner, more distinctive
treatment. Keep the existing pangolin-and-globe icon; change only the text.

The current logo sets the name in a flowing three-color script
(charcoal / coral / magenta), which reads as informal and generic. The new
wordmark is a single, deliberate serif in one color.

## The new wordmark

A horizontal lockup where the pangolin reads as the leading "e":

- **Icon:** existing `assets/images/logos/etm-logo.png` (pangolin + globe),
  unchanged.
- **Word:** `arthtoolsmaker` set immediately after the icon, so the pangolin
  stands in for the first "e" — reading `(e)arthtoolsmaker`.
- **Typeface:** Fraunces (serif), weight 600.
- **Case:** all lowercase.
- **Letter-spacing:** −0.015em.
- **Color:** charcoal `#1f2937` (single unified color).
- **Spacing of word relative to icon:** word offset **−5px horizontally**
  (pulled toward the icon) and **+5px vertically** (dropped down) so it nests
  into the pangolin's body. These offsets are at the mockup reference size
  (icon height 58px, font-size 38px); they scale proportionally with the
  rendered size.

This is the lockup decided during the visual brainstorm
(`.superpowers/brainstorm/.../pangolin-e-v7.html`, option "down 5px").

## What changes in the site

The horizontal lockup lives in one file:

- `assets/images/logos/etm-logo-text.png` (currently 1041×276, RGBA).

It is referenced via `params.logo = "/images/logos/etm-logo-text.png"` in
`config.toml` and rendered in two places:

- Site header — `layouts/partials/header.html` (`logo__image`)
- Footer — `layouts/partials/footer-widgets/widget-info.html`

Replacing that single asset updates both. The icon-only `etm-logo.png` is not
touched. No template or config changes are required if the new file keeps the
same path and a compatible aspect ratio.

## Deliverables

Produce the new lockup in **two formats**:

1. **PNG** — `assets/images/logos/etm-logo-text.png` (drop-in replacement).
   Transparent background, rendered at ~3× for crispness, auto-cropped to
   content. This is the file the site actually loads.
2. **SVG** — `assets/images/logos/etm-logo-text.svg` (crisp, scalable, for
   future use). Pangolin embedded as base64; the Fraunces text converted to
   vector outlines (paths) so it renders identically without the font
   installed.

Both must be visually identical to the approved mockup, so both should be
generated from the same source geometry / the same locally-installed Fraunces
font to avoid drift.

## Production approach

To keep PNG and SVG identical, install the Fraunces font locally first
(download the weight-600 TTF from Google Fonts into `~/.fonts`, run
`fc-cache`). Then:

- **PNG:** build the lockup HTML using the local Fraunces font, render with
  headless Chromium on a transparent background at high resolution, auto-crop
  to the non-transparent bounds.
- **SVG:** assemble an SVG with the pangolin embedded as a base64 PNG and the
  word as `<text>` in Fraunces, then convert the text to paths. Prefer
  Inkscape (`--export-text-to-path`) if available; otherwise convert glyph
  outlines with `fontTools`. If neither tool is available, fall back to
  embedding an `@font-face` with the base64 font (note the weaker renderer
  support) and flag it.

## Out of scope

- The icon-only mark (`etm-logo.png`) — unchanged.
- The favicon and any other brand assets.
- The "icon + full word" variant (separate pangolin + full `earthtoolsmaker`
  with a visible "e"); liked during brainstorming but not needed for the site
  logo slot. Can be added later if wanted.

## Verification

- New PNG matches the approved mockup (pangolin-as-"e", lowercase Fraunces,
  charcoal, −5px / +5px offsets).
- `hugo` builds cleanly; header and footer show the new logo at a sensible
  size (no layout overflow). Confirm against a static build, not the live
  `hugo server` (which can serve stale pages).
- SVG renders identically to the PNG when opened directly.
