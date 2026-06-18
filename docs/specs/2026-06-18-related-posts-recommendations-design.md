# Better "Next Reads": Theme Tags + Curated Related Posts

**Date:** 2026-06-18
**Status:** Approved design, ready for implementation plan

## Problem

The site already shows a "You may also like" section at the bottom of each blog
post (`layouts/partials/related-posts.html`). It picks the 2 most-recent posts
that share *any* tag with the current post.

But the tag vocabulary is too coarse: 12 of 13 posts carry both `AI` and
`vision`. Tag-intersection therefore matches nearly every post to every other
post, so the recommendations collapse to "the 2 newest posts" rather than the
*semantically closest* ones. There is no real notion of relatedness.

## Goals

1. Recommendations at the bottom of a post should be genuinely related to that
   post (same topic cluster), not just the newest posts.
2. The tag system should differentiate posts so the `/tags/` browse pages and
   the on-post tag chips are meaningful, and so the automatic fallback is
   relevant.
3. Stay within the existing Hugo mechanisms; no new build tooling or external
   dependencies.

## Non-goals

- No embeddings / similarity scripts / build-time computation (revisit only if
  the corpus grows large enough that manual curation stops scaling).
- No redesign of the card markup or the sidebar widget.
- No change to existing `/tags/` URLs for tags that already exist.

## Approach

Two complementary layers, both using mechanisms already present in the repo:

1. **Theme tags** — a small controlled vocabulary of differentiating tags added
   on top of the existing tags. These create tight clusters and power the
   *fallback*.
2. **Manual curation** — per-post `related_posts:` frontmatter (ordered,
   best-match first). This is the primary, highest-quality signal.

The bottom-of-post section becomes **curated-first, then tag-fill**: show the
hand-picked posts in order, then fill any remaining slots (up to N=2, matching
today) with tag-intersection matches, excluding self and already-shown posts.

### Why this approach

Manual curation gives the best quality for a 13-post corpus and reuses the
`related_posts:` field the sidebar widget already understands. Theme tags make
the automatic fallback relevant and improve tag-browsing as a side benefit.
Together they mean every post always shows good recommendations with full
editorial control.

## Detailed Design

### Component 1 — Theme tags (`data/tags.yaml` + post frontmatter)

Introduce 5 new theme tags. Each gets an emoji entry in `data/tags.yaml` so the
"Explore Topics" / tag chips render consistently:

| Theme tag   | Meaning                          | Suggested emoji |
| ----------- | -------------------------------- | --------------- |
| `wildfire`  | smoke / forest-fire detection    | 🔥              |
| `bear`      | bear-focused projects            | 🐻              |
| `marine`    | aquatic species (coral, salmon, trout/whales/seals) | 🌊 |
| `edge`      | on-device / low-power deployment | 📟              |
| `acoustics` | audio / bioacoustic analysis     | 🔊              |

The existing `metric learning` and `identification` tags already serve the
individual-ID cluster and are reused rather than duplicated.

### Component 2 — Per-post frontmatter (theme tags + `related_posts`)

`related_posts` values are directory slugs, ordered best-match first. Apply to
each post's `content/posts/<slug>/index.md`:

| Post (slug)                                          | Add theme tags    | `related_posts` (in order)                                                        |
| ---------------------------------------------------- | ----------------- | --------------------------------------------------------------------------------- |
| smoke-is-a-behavior                                  | `wildfire`        | racing-models-not-opinions, protecting-the-forest-early-forest-fire-detector      |
| racing-models-not-opinions                           | `wildfire`        | smoke-is-a-behavior, protecting-the-forest-early-forest-fire-detector             |
| protecting-the-forest-early-forest-fire-detector     | `wildfire`, `edge`| smoke-is-a-behavior, racing-models-not-opinions                                   |
| bear-face-segmentation-guide                         | `bear`            | bear-identification-with-metric-learning-guide, how-to-prepare-data-for-identification |
| bear-identification-with-metric-learning-guide       | `bear`            | bear-face-segmentation-guide, a-visual-guide-to-metric-learning                   |
| how-to-build-a-real-time-bear-detection-system       | `bear`, `edge`    | bear-face-segmentation-guide, protecting-the-forest-early-forest-fire-detector    |
| a-visual-guide-to-metric-learning                    | — (reuse existing)| bear-identification-with-metric-learning-guide, local-feature-matching-lightglue  |
| local-feature-matching-lightglue                     | `marine`          | a-visual-guide-to-metric-learning, how-to-prepare-data-for-identification         |
| how-to-prepare-data-for-identification               | — (reuse existing)| a-visual-guide-to-metric-learning, local-feature-matching-lightglue               |
| how-to-build-a-benthic-coral-reefs-analyser          | `marine`          | tracking-the-journey-how-to-monitor-wild-salmon-migrations, how-to-build-a-real-time-bear-detection-system |
| tracking-the-journey-how-to-monitor-wild-salmon-migrations | `marine`, `edge` | how-to-build-a-benthic-coral-reefs-analyser, how-to-build-a-real-time-bear-detection-system |
| how-to-analyze-elephant-rumbles-at-scale             | `acoustics`       | how-to-build-a-benthic-coral-reefs-analyser, tracking-the-journey-how-to-monitor-wild-salmon-migrations |
| volunteering_wildlife_rescue_centers                 | — (no AI cluster) | how-to-analyze-elephant-rumbles-at-scale, tracking-the-journey-how-to-monitor-wild-salmon-migrations |

Rationale for edge cases:
- **elephant rumbles** is the only acoustics post; its curated links lean on the
  nearest conservation-monitoring neighbors so it is not isolated.
- **volunteering** has no AI/vision overlap; it links to the most human/field
  oriented monitoring posts so it is not a dead end.

### Component 3 — Template change (`layouts/partials/related-posts.html`)

This is the only code change. Today line 2 computes `$related` as pure
tag-intersection. Replace that single computation with curated-first logic; the
render loop (the card markup) is unchanged.

New logic for `$related`:

1. Resolve `.Params.related_posts` slugs (in order) to pages. A slug is matched
   against post directory slugs; resolve via `.Site.GetPage` or by matching
   `.File.ContentBaseName` / path. Keep only slugs that resolve to a real,
   published post. This ordered list comes **first**.
2. Compute the existing tag-intersection set (most-recent-first), excluding self
   and any page already in the curated list.
3. Concatenate curated + tag-fill, then take `first 2`.

Constant: N = 2 (unchanged from today).

### Data flow

```
post index.md frontmatter ──┐
   related_posts: [...]      ├─► related-posts.html
   tags: [...]               │      1. resolve curated slugs → pages (ordered)
                             │      2. tag-intersection fill (dedup, exclude self)
data/tags.yaml ──────────────┘      3. first 2 → render existing cards
   (emoji per theme tag)
```

### Error handling

- A `related_posts` slug that does not resolve to a published post is silently
  skipped — no broken card, no build error.
- If a post ends up with zero recommendations (should not happen given
  curation), the section renders nothing, matching today's empty state
  (`{{ if $related }}`).
- Self-reference is excluded (existing `Permalink != .Permalink` guard kept).

## Testing / Verification

Hugo has no unit-test harness in this repo, so verification is a local build:

1. `hugo` (or `hugo server`) builds clean with no errors/warnings.
2. Spot-check three representative posts in the browser:
   - a wildfire post (e.g. `smoke-is-a-behavior`) → shows the two curated
     wildfire posts, in order.
   - a bear post (e.g. `bear-face-segmentation-guide`) → shows curated bear
     posts in order.
   - `volunteering_wildlife_rescue_centers` → shows its curated links (verifies
     a post with no shared AI/vision tags still gets curated cards).
3. Confirm the new theme tags appear as chips on posts and render with their
   emoji on the relevant `/tags/<tag>/` pages.

## Files Touched

- `data/tags.yaml` — add 5 theme-tag emoji entries.
- `layouts/partials/related-posts.html` — curated-first + tag-fill logic (line 2
  region only).
- `content/posts/*/index.md` — 13 files: add theme tags (12 of them) and
  `related_posts` (all 13).
