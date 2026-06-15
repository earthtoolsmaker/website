# Biowatch App — Page Revamp

**Date:** 2026-06-15
**Status:** Approved
**Base:** latest `origin/main` (worktree `worktree-biowatch-revamp`). One PR per project page.

## Goal

Bring the Biowatch project page in line with the other revamped project pages.
Unlike the species pages, this is a **product page** — it already has strong
copy, real product screenshots, and download CTAs. So the revamp is light-touch:
add the house tagline + stats band, one animated workflow diagram, convert the
feature bullet list to a card grid, and remove the section-title emoji.

## Front matter

- Add `tagline`: *"A free, open-source desktop app that turns a folder of camera-trap images into living ecological insight — entirely offline."*
- Add `stats`: **Free & open-source** · **100% offline** · **Win / macOS / Linux**.

## Body structure

1. **Biowatch is Here** — keep, **remove the 🦊 emoji** from the heading (section titles are emoji-free site-wide). Keep CTA buttons + intro.
2. **From Raw Footage to Real Insight** — keep prose; add the **workflow diagram** here (it shows how Biowatch bridges classification → insight).
3. **What Biowatch Does** — keep the short intro line, convert the 7 feature bullets to a 6-card `support__grid` (Import from anywhere · On-device species ID · Explore in space & time · Review & correct · Deployment insights · Standards-based export — species-filtering folded into Explore). Keep the screenshot carousel + its caption right after. **AI models stay as prose** (no pills, per request).
4. **Free, Open Source, and Built in the Open** — keep + CTAs.

## Diagram (new animated SVG, house teal/coral)

`workflow.svg` (1062×380, 4 cards) — **Import → Identify → Explore → Export**:
- **Import** — a stack of camera-trap photo tiles dropping in; chip "folder · GBIF · Camtrap DP".
- **Identify** — a forest camera-trap frame, a fox boxed with a "fox 0.97" label and an "on-device" chip.
- **Explore** — a map with location pins, a density heatmap blob, a pinging marker, and a species pie-chart.
- **Export** — a teal panel listing one folder per species (fox/ deer/ wild boar/) with a glowing "Publish to GBIF" chip.

New primitives: camera-trap `tile`, `fox`, mini `folder`, map `pin`. Animation classes on inner `<g>`, positioning on outer `<g>`; `prefers-reduced-motion` guard.

## Reuse / non-goals

- Reuse `support__grid`, `image_carousel`, existing button styles.
- Keep all 6 real product screenshots and both CTA button blocks.
- No template/shortcode/SCSS changes. No threats pills on this page.

## Verification

- `hugo` builds clean; rendered HTML has the diagram, the 6 cards, the carousel, both CTA blocks; no emoji in headings; diagram animates and degrades under reduced motion.
