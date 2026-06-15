# Trout Identification — Page Revamp

**Date:** 2026-06-15
**Status:** Approved
**Base:** latest `origin/main` (worktree `worktree-trout-revamp`). One PR per project page.

## Goal

Bring the trout re-identification page in line with the other project pages: tightened non-technical copy, card grids + interactive pills for the bullet sections, one new animated SVG overview diagram. **Keep the strong real image tables** (raw → normalized → keypoints, and the match / non-match keypoint pairs) — they're compelling actual results, like the smolt page's real figures.

## Front matter

Add `tagline` only (no stats band — the source has no strong numbers). Tagline: *"Recognising individual trout by their spot patterns — like fingerprints — without ever touching the fish."*

## Body structure

1. **Lede** (tighten the Context: trout / Westslope Cutthroat as an indicator species / spots are unique like fingerprints) + **Diagram A** + keep the WCT photo and Elk River map woven in.
2. **Why this trout matters** ("A vital role", 6 bullets) → 3-card grid (food-web role · indicator species · cultural & habitat value).
3. **Under pressure** (conservation concerns, 6 bullets) → interactive **pills** (`{{< threats "pressures" >}}`): habitat loss · fragmentation (dams) · pollution · invasive species · climate change · overfishing.
4. **How the system works** — short intro + Diagram A reference, then keep the real **preprocessing table** (raw → normalized → keypoints) and the real **match / non-match** keypoint table; tighten the copy around them.
5. **Conclusion** + `demo_cta` (drop the redundant "try the live demo" line).

## Diagram (new animated SVG, house teal/coral)

New primitive: a **trout** (olive-gold body, black spots denser toward the tail, the cutthroat's red throat slash). Plus a **keypoint constellation** overlay and a **database match** panel (reuse the seal re-ID pattern).

- **Diagram A — `pipeline.svg` "From a photo to an identity"** — 4 cards: **Photo** (a raw trout photo) → **Normalize** (straightened & cut out on a clean background) → **Keypoints** (its spot pattern extracted as keypoints) → **Match** (compared against the database → a known individual, or a new one).

Positioning transform on an outer `<g>`, animation on an inner `<g>`; `prefers-reduced-motion` guard.

## Reuse / non-goals

- Reuse `threats` pills, `support__grid`, `demo_cta`, and the existing markdown image tables.
- Keep all the real trout imagery (raw/normalized/keypoints, match/non-match, WCT photo, Elk River map). The existing `pipeline.png` is superseded by Diagram A.
- No template/shortcode changes.

## Verification

- `hugo` builds clean; screenshot hero, Diagram A, pills, card grids, the real image tables; diagram animates + degrades with reduced motion.
