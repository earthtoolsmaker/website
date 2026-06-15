# Coral Reefs Health Monitoring — Page Revamp

**Date:** 2026-06-15
**Status:** Approved
**Base:** latest `origin/main` (worktree `worktree-coral-revamp`). One PR per project page.

## Goal

Rewrite the bullet-heavy coral page into the established hybrid-editorial system (fire/salmon/elephant/smolt/seal): tightened non-technical copy, card grids + interactive pills replacing the three big bullet dumps, two new animated SVG diagrams, hero stats. Keep the real assets (reef photo gallery, `instance_segmentation.png`, the `coral_ai.gif` demo).

## Front matter

`tagline` + `stats`: `25%` of marine life · `<1%` of the seafloor · `open-source` models. Tagline: *"Mapping hard and soft coral in underwater imagery to track reef health over time."*

## Body structure

1. **Lede** (tightened) + **Diagram A** + the ReefSupport blockquote.
2. **Why coral reefs matter** (7 bullets) → 3-card grid (Biodiversity hotspots · Coastal & economic backbone · Climate, medicine & culture).
3. **Reefs under pressure** (Conservation concerns, 7 bullets) → interactive **pills** (`{{< threats "pressures" >}}`): warming & bleaching · pollution · overfishing · coastal development · unsustainable tourism · invasive species · weak governance.
4. **Mapping coral, colony by colony** (Project scope + Developed tools) — short intro + **Diagram B** (segmentation close-up) + keep `instance_segmentation.png`; the model maps hard vs soft coral, building toward finer functional groups.
5. **Why underwater vision is hard** (7 bullets) → 3-card grid (light & colour loss · haze & artifacts · variable conditions / scarce labels) + keep the real **reef gallery**.
6. **Conclusion** + keep the `coral_ai.gif`; `demo_cta`.

## Diagrams (new animated SVG, house teal/coral)

New primitives: a **reef scene** (hard coral = teal boulder/branching shapes, soft coral = coral-orange bushy shapes, on a blue seabed), instance-segmentation **outlines/masks**, a **diver** with a camera, a **% coral-cover** gauge.

- **Diagram A — `pipeline.svg` "From a dive photo to coral cover"** — 4 cards: **Capture** (diver photographs the reef) → **Segment** (each coral colony outlined) → **Classify** (hard vs soft) → **Measure** (% coral cover, tracked over time).
- **Diagram B — `segmentation.svg` "Mapping each colony"** — 3 cards: **Photo** (benthic image) → **Model** (reused neural net) → **Map** (each colony outlined and filled, hard teal / soft coral, with a cover %).

Positioning transform on an outer `<g>`, animation on an inner `<g>`; `prefers-reduced-motion` guard.

## Reuse / non-goals

- Reuse `threats` pills, `support__grid`, `.media-caption`, `demo_cta`, `gallery`.
- Keep the real reef photos, instance_segmentation.png, coral_ai.gif. The existing `pipeline_overview.png` is superseded by Diagram A.
- No template/shortcode changes.

## Verification

- `hugo` builds clean; screenshot hero+stats, both diagrams, pills, card grids, reef gallery, gif; diagrams animate + degrade with reduced motion.
