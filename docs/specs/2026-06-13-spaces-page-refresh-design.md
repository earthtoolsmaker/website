# Spaces Page Refresh — Design

**Date:** 2026-06-13
**Status:** Approved (brainstorm) — ready for implementation plan

## Overview

Refresh the Spaces listing page (`/spaces/`) by replacing the emoji-in-a-box card
visuals with bespoke flat-vector illustrations in the style of the site hero image,
and by tightening the card copy. Each illustration is adapted to the subject's
**ecosystem** while sharing one visual language so the set feels cohesive.

The hero image (`assets/images/pages/home/hero.jpg`) is the reference style: soft
vertical gradient sky, a coral sun, layered rolling hills, flat stylized pines, a
pale river, simple silhouettes (elephant, fish), muted teal/sage + coral palette.

## Goals

- Replace every space card's emoji with a custom illustration in the hero style.
- Adapt each scene to the subject's ecosystem (forest, underwater, river, snow, etc.).
- Rewrite card copy: add a short tag (subtitle) + a tightened 1–2 sentence summary.
- Rewrite the Spaces page intro copy.
- Keep changes surgical; no unrelated refactors.

## Non-Goals

- No changes to the individual space pages' content/behaviour beyond front matter.
- No AI-generated raster images; all art is hand-authored SVG.
- No redesign of the card grid layout itself.

## Locked Decisions

1. **Production method:** hand-authored SVG scenes + recolored open-license
   silhouettes. No external image-gen tool.
2. **Silhouette sourcing:** prefer **PhyloPic CC0** (public domain, no attribution
   required) for organisms; hand-draw abstract subjects (fire, smoke, sonar, sound).
3. **Per-ecosystem scenes**, unified by shared flat-vector language and palette family.
4. **Copy:** short uppercase tag (subtitle) + tightened summary; drop emojis.
5. **Grayscale filter:** remove the `grayscale(50%)`-until-hover effect; cards show
   full-color art. Keep the subtle `translateY` hover lift.
6. **SVG storage:** `assets/images/pages/spaces/<slug>/card.svg`, referenced via a new
   `card_image` front-matter field, rendered as `<img>`.
7. **Rollout:** write this spec, then implement **one card at a time** with approval at
   each step. Bear is the locked template.

## Image System

- Each SVG: `viewBox="0 0 1000 700"` (matches the card's 10:7 slot, `padding-top:70%`),
  `preserveAspectRatio="xMidYMid slice"`.
- Composition = hand-built ecosystem background + recolored silhouette(s).
- Silhouette fill: dark teal `#143b35`.
- Shared palette tokens (from the validated bear proof):
  - Sky gradient: `#e4f1ee → #f7ddd2 → #f6d0c2 → #d3e9e0 → #c2e1d7`
  - Sun: `#ef9d78` with `#f6c7a9` halo
  - Hill bands light→dark: `#bfe0d6`, `#88c8b9`, `#4f9e8e`, `#2c7165`, `#15463f`
  - Underwater gradient: `#bfeae3 → #73c6bd → #2f8f86 → #13524d`
- Stored at `assets/images/pages/spaces/<slug>/card.svg`.

## Ecosystem & Card Catalog

Tag taxonomy: **Computer Vision · Bioacoustics · Underwater Vision · Wildfire · Sonar**.

| Slug | Ecosystem scene | Silhouette source | Tag | Draft summary |
|---|---|---|---|---|
| `bear_identification` | Forest sunset (BC) | PhyloPic *Ursus americanus* (CC0) ✓ | Computer Vision | Facial recognition that tells individual bears apart from photos — tracking British Columbia's population over time. |
| `coral_reef_health_monitoring` | Underwater reef | Hand-drawn coral fans | Underwater Vision | Spotting and identifying coral species in benthic imagery to track reef health over time. |
| `early_forest_fire_detection` | Forest dusk + fire glow/smoke | Hand-drawn fire/smoke + camera | Wildfire | Real-time camera analysis that detects wildfires early and raises the alarm fast. |
| `forest_elephant_rumble_detection` | Tropical forest + sound waves | PhyloPic *Loxodonta* (CC0) | Bioacoustics | Listening to African forests to detect and classify elephant rumbles from audio. |
| `human_wildlife_bear_conflict` | Forest/farm edge dusk | PhyloPic bear + fence | Computer Vision | Detecting and deterring bears near Romanian farms so people and predators can coexist. |
| `seal_identification` | Coastal shore (Wadden Sea) | PhyloPic seal (CC0) | Computer Vision | Re-identifying individual seals by whisker and face patterns — non-invasive, across seasons. |
| `smolt_sonar_monitoring` | Sonar scan (monochrome teal) | Hand-drawn sonar arc + fish blips | Sonar | Detecting, tracking and counting juvenile salmon in ARIS sonar as they migrate downstream. |
| `snowleopard_identification` | Snowy peaks (Central Asia) | PhyloPic *Panthera uncia* (CC0) | Computer Vision | Identifying individual snow leopards by coat patterns to support conservation across Central Asia. |
| `temporal_smoke_verification` | Forest ridge + watchtower + smoke | Hand-drawn smoke + tower | Wildfire | Watching camera sequences over time to tell genuine wildfire smoke from look-alikes. |
| `trout_identification` | Freshwater river surface | PhyloPic salmonid (CC0) | Underwater Vision | Reading the spot patterns on trout to identify individual fish — a non-invasive population monitor. |
| `wild_salmon_migration_monitoring` | Underwater stream | PhyloPic salmon (CC0) | Underwater Vision | Classifying and counting wild salmon from underwater camera streams as they return to spawn. |

Notes:
- The four fish-adjacent cards (coral, trout, wild salmon, smolt) get deliberately
  different treatments — reef vs. river surface vs. underwater stream vs. sonar scan —
  so they don't look identical.
- Summaries above are drafts; finalized per-card during rollout with the user.
- If a usable CC0 silhouette can't be found for a subject, fall back to hand-drawn.

## Copy

- **Page intro** (`content/spaces/_index.md`): rewrite `description` from
  "Interact with our latest ML models applied to conservation problems." to a warmer,
  clearer one-liner (finalized during rollout).
- **Per card:** `subtitle` = tag; `summary` = tightened 1–2 sentences.

## Template / CSS Changes (surgical)

1. `layouts/spaces/list.html` — replace the `.space__image-emoji` div with
   `<img class="lazy" src="{{ .Params.card_image | ... }}" alt="{{ .Params.title }}">`
   (use the existing responsive-image/img pattern). Remove emoji rendering.
2. `layouts/shortcodes/space_card.html` — same swap; add an `image` param. Update the
   4 usages in `content/tools/animal-reid/index.md` to pass `image=` and drop `emoji=`.
3. `assets/sass/3-modules/_spaces.scss`:
   - Remove the `grayscale(50%)` default filter + its hover reset.
   - Remove the `#e66465 → #9198e5` placeholder gradient on `.space__image`.
   - Ensure `img` fills the container (existing `img` rules already do `object-fit:cover`).
4. Front matter per space: add `subtitle` and `card_image`; stop using `emoji`.

## Licensing

Log each silhouette's source URL + license in
`docs/specs/spaces-illustration-credits.md`. PhyloPic CC0 needs no attribution, but we
keep a record. Any non-CC0 source would require a visible credit (avoid if possible).

## Rollout Process (one card at a time)

For each card: (1) source/confirm silhouette + license → (2) build ecosystem SVG →
(3) write tag + summary → (4) render a preview screenshot → (5) user approves →
(6) commit → next card. The shared system pieces (CSS/template/front-matter field)
land first, with the bear card as the reference implementation.

## Success Criteria

- All 11 cards show custom ecosystem SVGs; no emojis remain on the Spaces page or in
  the `animal-reid` tool page.
- Each card has a tag + tightened summary.
- `hugo` builds cleanly; the static page renders cards correctly (ground truth, not the
  dev server).
- Cards display full-color (no grayscale), with the hover lift intact.
