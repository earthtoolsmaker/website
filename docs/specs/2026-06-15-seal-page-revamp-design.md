# Wadden Sea Seal Monitoring — Page Revamp

**Date:** 2026-06-15
**Status:** Approved
**Base:** latest `origin/main` (worktree `worktree-seal-revamp`). One PR per project page.

## Goal

Rewrite the bullet-heavy seal page into the established hybrid-editorial system (fire/salmon/elephant/smolt): tightened non-technical copy, card grids and interactive pills replacing bullet dumps, two new animated SVG diagrams, hero stats. Keep the real assets (web-app screens, the re-ID example-match carousel, Wadden Sea photos/map).

## Front matter

Add `tagline` + `stats`: `2` seal species · `5` attributes per seal · `90%` less manual work. Tagline: *"Counting, classifying and recognising individual seals from aerial surveys of the Wadden Sea."*

## Body structure

1. **Lede** — tighten the 3 intro paragraphs; keep the intro carousel (Wadden Sea / seals / map). Add **Diagram A** as the overview.
2. **Why seals matter** ("Vital for Marine Ecosystems", 6 bullets) → 3-card grid (apex predator · ecosystem-health indicator · biodiversity & heritage).
3. **The monitoring challenge** (6 bullets) → interactive **pills** (`{{< threats "challenges" >}}`): labour-intensive · multi-attribute · breeding-season counts · image-quality variation · individual tracking · long-term consistency.
4. **Two AI systems** (Project scope) — short intro to the detection/classification system + the re-ID system.
5. **Counting & classifying** — Diagram A reference; the 5 classification attributes as numbered `.services` columns (Species · Life stage · Location · Vitality · Sex); keep the web-app review carousel; tighten the web-app feature list.
6. **Recognising individuals** (re-ID) — **Diagram B** + tightened 2-stage explanation; keep the real example-match carousel (whisker/spot/facial). Conservation insights (6 bullets) → 3-card grid.
7. **Impact** (6 bullets) → tightened prose / small grid (headline already in stats).
8. **Demo** — `{{< demo_cta >}}`.

## Diagrams (new animated SVG, house teal/coral + warm sand)

New primitives: a top-down **seal** (grey blob with a head), a **sandbank/tidal flat** (tan), an **aircraft** + camera cone, aerial **bounding boxes**, attribute **chips**, a seal **face** (whiskers + spots), a feature **fingerprint** (embedding bars), a **database** stack.

- **Diagram A — `pipeline.svg` "From aerial survey to seal census"** — 4 cards: **Survey** (aircraft photographs the colony) → **Detect** (every seal boxed on the sandbank) → **Classify** (one seal tagged five ways) → **Review** (web-app counts, exported).
- **Diagram B — `reid.svg` "Recognising an individual"** — 3 cards: **A face** (whisker + spot pattern) → **A fingerprint** (model turns the pattern into an embedding) → **A match** (compared against the database → same individual, e.g. across seasons).

Positioning transform on an outer `<g>`, animation on an inner `<g>`; `prefers-reduced-motion` guard.

## Reuse / non-goals

- Reuse the `threats` pills shortcode, `.services` columns, `support__grid`, `.media-caption`, `demo_cta`, `image_carousel` — all on `main`.
- Keep the real photographic assets; the existing `pipeline.png` / `reid/pipeline.png` may be retired in favour of the SVGs (decide during build).
- No template/shortcode changes.

## Verification

- `hugo` builds clean; screenshot hero+stats, both diagrams, pills, columns, carousels; diagrams animate + degrade with reduced motion.
