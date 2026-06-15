# Bird Flu Monitoring — Page Revamp

**Date:** 2026-06-15
**Status:** Approved
**Base:** latest `origin/main` (worktree `worktree-birdflu-revamp`). One PR per project page.

## Goal

Bring the bird-flu page in line with the other revamped project pages, and fix a
content gap: the current body explains avian influenza in general but never
describes the actual project (drones + computer vision counting seabirds). Add a
tagline + stats band, a 4-card workflow diagram, a card grid + interactive pills
for the prose sections, and a "how we monitor it" section. Fundraising status,
cover image only — diagram + cards + pills carry the visuals.

## Front matter

- `tagline`: *"Counting every bird in a seabird colony — alive or lost — from a drone overhead, to measure avian flu's toll without setting foot inside."*
- `stats`: **Aerial survey** · **Adults & chicks** · **Non-invasive**.
- `impacts` list for the pills. Keep `status: fundraising`.

## Body structure

1. **Lede** — tighten the context; bring the drone solution up front (seabird colonies, why they're vulnerable, the flu threat).
2. **The monitoring challenge** → 3-card `support__grid`: remote & fragile sites · counting by hand harms them · flu moves fast.
3. **How bird flu hits a colony** → interactive pills (`{{< threats "impacts" >}}`): mortality · breeding disruption · spread to chicks · population decline · ecological ripple.
4. **How we monitor it** → new section describing the drone + CV + photogrammetry approach + the **diagram**.
5. **Conclusion** — management strategies, tightened, ending on the role of monitoring/data.

## Diagram (new animated SVG, house teal/coral)

`pipeline.svg` (1062×380, 4 cards) — **Survey → Map → Detect & count → Assess**:
- **Survey** — a quadcopter drone hovering over a beach colony, downward scan beam; "drone" chip.
- **Map** — drone photos stitched into one orthomosaic (tiled top-down map, one tile snapping in); "orthomosaic" chip.
- **Detect & count** — top-down aerial with gulls boxed: live (teal), chicks (smaller, green), dead (coral); live/dead legend.
- **Assess** — a colony-count panel (Adults 1,240 · Chicks 380 · Dead 56) with a glowing "97% survival" chip.

New primitives: top-down `gull` (stroke set per `<use>`), `drone`. Animation classes on inner `<g>`, positioning on outer `<g>`; `prefers-reduced-motion` guard.

## Reuse / non-goals

- Reuse `threats` pills + `support__grid`. No new photos (none exist); keep the cover.
- No template/shortcode/SCSS changes.

## Verification

- `hugo` builds clean; rendered HTML has the diagram, 3 cards, pills; diagram animates and degrades under reduced motion.
