# Bear Deterrence in the Carpathians — Page Revamp

**Date:** 2026-06-15
**Status:** Approved
**Base:** latest `origin/main` (worktree `worktree-bear-deterrence-revamp`). One PR per project page.

## Goal

Bring the page in line with the other project pages: tightened non-technical copy, card grids + interactive pills for the bullet sections, one new animated SVG diagram for the detect-and-deter system. Keep the strong real assets (field photos, sky-dancer gallery, camera-trap gallery, the two HackThePlanet videos, the field-testing narrative).

## Front matter

Add `tagline` + `stats`: `Real-time` detection · `Low-power` edge device · `Non-lethal` deterrent. Tagline: *"Spotting bears at the farm's edge and scaring them off — harmlessly — before conflict starts."*

## Body structure

1. **Lede** (keep — it's strong) + **Diagram A** + keep the village photo, the brown-bear photo, and the "Living With Bears" video.
2. **Why bears matter** ("Bears are vital", 5 bullets) → 3-card grid (apex predator & prey control · seed dispersal & nutrient cycling · ecosystem engineer / indicator). Keep the BearID gallery.
3. **Conservation concerns** (6 bullets) → interactive **pills** (`{{< threats "pressures" >}}`): habitat loss & fragmentation · human–wildlife conflict · poaching & trade · climate change · habitat degradation · weak legal protection.
4. **How the system works** (Project scope) → short intro + **Diagram A** (the detect→deter pipeline replaces `pipeline_overview.png`); keep the real AI-camera install photo.
5. **Built for the field** (the detection challenges) → 3-card grid (low-power & low-maintenance · safe for animals & people · few false alarms); keep the camera-trap gallery.
6. **The deterrent: a sky-dancer** → keep prose + the sky-dancer gallery.
7. **Field-testing the sky-dancer** → keep the narrative (great story).
8. **Conclusion** + the demo video + `demo_cta` (drop the redundant "try the live demo" line).

## Diagram (new animated SVG, house teal/coral + night palette)

New primitives: a flat **brown bear**, an **AI camera on a pole** (night-vision), a **night-vision frame**, a **microcontroller** board, and an inflatable **sky-dancer** (swaying tube man).

- **Diagram A — `pipeline.svg` "Detect and deter"** — 4 cards: **Watch** (AI camera watches the farm edge at night, a bear approaching) → **Detect** (night-vision frame, bear boxed, on a low-power on-device chip) → **Trigger** (the microcontroller fires the deterrent) → **Deter** (the sky-dancer inflates and the bear turns away).

Positioning transform on an outer `<g>`, animation on an inner `<g>`; `prefers-reduced-motion` guard.

## Reuse / non-goals

- Reuse `threats` pills, `support__grid`, `gallery`, `demo_cta`.
- Keep all the real photos/videos/galleries and the field-testing narrative. The existing `pipeline_overview.png` is superseded by Diagram A.
- No template/shortcode changes.

## Verification

- `hugo` builds clean; screenshot hero+stats, Diagram A, pills, card grids, galleries, videos; diagram animates + degrades with reduced motion.
