# Logo wordmark redesign

**Date:** 2026-06-13
**Status:** Implemented

## Goal

Replace the EarthToolsMaker text wordmark with a cleaner, more distinctive
treatment, and add a playful animated brandmark. Keep the existing
pangolin-and-globe icon; change the text and add motion.

The old logo set the name in a flowing three-color script
(charcoal / coral / magenta), which read as informal and generic. The new
wordmark is a single, deliberate serif in one color, and the header/footer
logos animate the pangolin + word on hover.

## Type treatment

- **Icon:** existing `assets/images/logos/etm-logo.png` (pangolin + globe),
  unchanged. It doubles as the spinning element in the animated brandmark.
- **Typeface:** Fraunces (serif), weight 600.
- **Case:** all lowercase.
- **Letter-spacing:** −0.015em.
- **Color:** charcoal `#1f2937`.

Two word lockups are used: compact `etm` and full `earthtoolsmaker`.

## The animated brandmark

A reusable component (`.brandmark`): a square pangolin element beside a word.
On hover the pangolin **rolls** (one continuous 360° spin) while the word
swaps from `etm` to the full `earthtoolsmaker`. Two text-transition modifiers:

- **`--unroll`** (header): `etm` fades out as `earthtoolsmaker` unrolls
  left→right (clip-path). On mouse-out the full word folds back, then `etm`
  waits for the fold to finish and fades in — staggered so the two words never
  overlap.
- **`--slide`** (footer): an odometer — `etm` slides up and out while
  `earthtoolsmaker` rises up into place (and reverses on exit).

The full word sits **in-flow** (reserving its width) with `etm` overlaid
absolutely, so the surrounding layout never shifts when the word changes. Both
word images share the same height and baseline, so they stack pixel-aligned.
Animations also trigger on keyboard `:focus-visible`.

## Where each form appears

- **Home header:** static `.brandmark` (no modifier) showing the full
  `earthtoolsmaker` — no spin, no swap. Same pangolin+word spacing as the
  other pages.
- **Other page headers:** `.brandmark--unroll`, default `etm`.
- **Footer (all pages):** `.brandmark--slide.brandmark--sm`, default `etm`.

Header height 60px (responsive 54/48/44); footer 44px.

## Deliverables

Assets under `assets/images/logos/` (SVG + PNG):

| Asset | Purpose |
|---|---|
| `etm-logo.png` | Pangolin icon (existing) — spinning element + home/footer |
| `logo-word-etm` | Tight `etm` word image (no pangolin) |
| `logo-word-full` | Tight `earthtoolsmaker` word image (no pangolin) |
| `etm-logo-text` | Baked full lockup — kept only as a fallback |

The word images are cropped tight to the word, share a constant
ascender..descender canvas height and baseline (so `etm` and `earthtoolsmaker`
align when stacked), and are placed beside the standalone pangolin with an 8px
CSS gap.

Site wiring:

- `layouts/partials/header.html` — home → static brandmark; other pages →
  `--unroll` brandmark; fallback → baked lockup.
- `layouts/partials/footer-widgets/widget-info.html` — `--slide --sm`
  brandmark.
- `assets/sass/3-modules/_header.scss` — the shared `.brandmark` component
  (layout, `bm-roll` keyframe, `--unroll` / `--slide` modifiers); removed the
  stale 40px nav/CTA top padding so they align with the logo.

## Production approach

Generator in the gitignored `.superpowers/logobuild/gen_logo.py` (Python +
fontTools + headless Chromium). `build_word_tight(word)` instances Fraunces at
`wght=600`, outlines the word to vector paths, and renders an SVG on a constant
metric canvas; Chromium rasterizes it at 8× and PIL crops it tight
horizontally (constant height). The standalone pangolin uses the existing
`etm-logo.png`.

## Out of scope

- Favicon and other brand assets.
- Dark-mode logo variant (`params.logo_dark` remains unset, as before).

## Verification

- `hugo` builds cleanly. Home shows static `earthtoolsmaker`; interior pages
  show `etm`; footer shows `etm`.
- Hover end-states verified with the real assets: both `--unroll` and
  `--slide` reveal `earthtoolsmaker` fully and aligned; the `--unroll` exit
  staggers with no word overlap.
- Home and interior share the same pangolin→word spacing and 60px size; nav and
  Support button align with the logo.
