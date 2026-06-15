# Bear Identification — Page Revamp

**Date:** 2026-06-15
**Status:** Approved
**Base:** latest `origin/main` (worktree `worktree-bear-id-revamp`). One PR per project page.

## Goal

Bring the Bear Identification page in line with the other revamped project pages:
tightened non-technical copy, card grids + interactive pills for the long bullet
lists, one new animated SVG diagram for the re-identification pipeline. Keep the
strong real assets (BearID individual photos, the same-individual gallery,
camera-trap photos). Replace the three flat PNG figures (`pipeline.png`,
`instance_segmentation.png`, `metric_learning_embed.png`) with the single
animated diagram + the real galleries.

## Front matter

Add a `tagline` (no stats band, per request):
*"Recognising individual brown bears by their faces — from a camera-trap photo, with no tags and no handling."*
Add a `pressures` list (for the threats pills). Keep clients/space/github/related_posts.

## Body structure

1. **Lede** (keep, tightened) + **Diagram** (re-ID pipeline SVG) replacing `pipeline.png`. Keep the BearID quote.
2. **Why bears matter** ("Bears are vital", 5 bullets) → 3-card `support__grid`
   (apex predator & prey control · gardener / seed & nutrient cycling · engineer & indicator).
   Keep the BearID individuals gallery → convert to `image_carousel`.
3. **Under pressure** (Conservation concerns, 6 bullets) → interactive **pills**
   (`{{< threats "pressures" >}}`): habitat loss & fragmentation · human–wildlife
   conflict · poaching & trade · climate change · habitat degradation · weak legal protection.
4. **Why identify individual bears** (benefits, 4 bullets) → 3-card grid
   (population & movement · behaviour & social · conflict & land management).
5. **Why bears are hard to tell apart** (the challenges, 3 bullets) → 3-card grid
   (no unique markings · morphological variation · seasonal/age change). Keep the
   same-individual (bf32) gallery → `image_carousel`, captioned.
6. **How the system works** → short non-technical intro + **Diagram**; two steps
   (detect the face · match the fingerprint) as short prose, keeping the camera-trap
   carousel. Drop the three PNG figures.
7. **Conclusion** + `demo_cta` (drop the redundant "try the live demo" line — the CTA covers it).

## Diagram (new animated SVG, house teal/coral)

`pipeline.svg` (1062×380, 4 cards) — **Photo → Detect face → Embed → Match**:
- **Photo** — a camera-trap image of a bear (forest scene, timestamp).
- **Detect face** — instance segmentation: a frontal bear face with a dashed
  segmentation contour + crop brackets, "face" chip (coral).
- **Embed** — metric learning: the face becomes a point in face-space; clusters
  of known individuals, the query point (coral) landing in its cluster, "fingerprint" chip.
- **Match** — nearest neighbour in the database of known bears; rows of bear IDs,
  the matched one (**BF32**, tying to the real same-individual gallery) highlighted
  with a check + "0.92 match".

New primitives: frontal **bearface**, mini **facemini** glyph; reuse the side-profile
**bear**. Positioning transform on outer `<g>`, animation on inner `<g>`;
`prefers-reduced-motion` guard.

## Reuse / non-goals

- Reuse `threats` pills, `support__grid`, `image_carousel`/`carousel_image`, `demo_cta`.
- Keep all real photos; convert the three galleries to carousels for consistency.
- No template/shortcode/SCSS changes (infra already on main).

## Verification

- `hugo` builds clean; rendered HTML contains the diagram, pills, card grids,
  carousels; diagram animates and degrades under reduced motion.
