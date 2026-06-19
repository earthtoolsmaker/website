# Better Related Content on Project Pages

**Date:** 2026-06-19
**Status:** Approved design, ready for implementation plan

## Problem

Project single pages (`layouts/projects/single.html`) currently surface related
content in two places:

- **"Related reading"** — renders the curated `related_posts` frontmatter list.
  Shows nothing when a project has no `related_posts` (3 of 13 projects:
  `wadden_sea_seal_monitoring`, `snow_leopard_monitoring`, `bird_flu_monitoring`).
- **"Next project"** — renders `.PrevInSection`, i.e. the chronologically
  adjacent project. This is sequential, not semantic: a bear project can be
  followed by a coral project purely by date.

Projects have no `tags` field, so there is no way to compute relatedness between
projects, or to fall back to relevant posts when curation is absent.

## Goals

1. Replace the arbitrary "Next project" with genuinely **related projects**.
2. Give **"Related reading"** a fallback so every project shows relevant posts.
3. Add a curated **"Try these demos"** section cross-promoting related demos.
4. Reuse the theme-tag vocabulary already added to blog posts so posts and
   projects share one relatedness vocabulary (enables cross-type fallback).

## Non-goals

- No embeddings / similarity scripts / build-time computation.
- No redesign of the card markup (`project-card.html`, `article.html`) or the
  hero/CTA/partner sections of the project template.
- No change to the sidebar widget
  (`widget-recent-projects-and-related-posts.html`) — it is not rendered on
  project pages and stays as-is.

## Approach

Mirror the blog-posts solution: **theme tags + curation override** (curated
first, then tag-fill). This unifies posts and projects under one theme-tag
vocabulary, which is what makes the project→post fallback possible.

Three frontmatter signals per project:
- `tags` — theme tags (shared vocabulary with posts) drive automatic fallback.
- `related_projects` — optional ordered override for the related-projects list.
- `related_spaces` — curated ordered list of demo paths for "Try these demos".
- `related_posts` — existing field, kept; now gets a tag-fill fallback.

### Theme-tag vocabulary

Reuse the post theme tags: `wildfire`, `bear`, `marine`, `edge`, `acoustics`,
plus the existing shared coarse/axis tags `vision`, `audio`, `identification`,
`camera traps`. No new tags are introduced. Emoji entries for all of these
already exist in `data/tags.yaml` on this branch (verified — the blog-posts
theme-tag commit is an ancestor of HEAD), so **no `data/tags.yaml` change is
required**.

## Detailed Design

### Component 1 — Per-project frontmatter

Add theme `tags`, optional `related_projects` (ordered), and `related_spaces`
(ordered demo paths) to each project. `related_projects` values are project
filename slugs (without `.md`). `related_spaces` values are demo paths that must
resolve to a real page under `content/demos/`.

Also fix: `snow_leopard_monitoring` is missing a `space` field though a demo
exists — add `space: /demos/snowleopard_identification/`.

| Project (slug) | Add `tags` | `related_projects` (ordered) | `related_spaces` (ordered) |
| --- | --- | --- | --- |
| bear_identification | bear, identification, vision | carpathian-bear-deterrence, trout_identification, snow_leopard_monitoring | /demos/trout_identification/, /demos/snowleopard_identification/ |
| carpathian-bear-deterrence | bear, edge, camera traps, vision | bear_identification, early_forest_fire_detection | /demos/bear_identification/, /demos/early_forest_fire_detection/ |
| trout_identification | marine, identification, vision | wild_salmon_migration_monitoring, bear_identification, snow_leopard_monitoring | /demos/wild_salmon_migration_monitoring/, /demos/bear_identification/ |
| coral_reef_health_monitoring | marine, vision | wild_salmon_migration_monitoring, monitoring_smolt_salmon_migration_with_sonar | /demos/wild_salmon_migration_monitoring/, /demos/smolt_sonar_monitoring/ |
| monitoring_smolt_salmon_migration_with_sonar | marine, vision | wild_salmon_migration_monitoring, coral_reef_health_monitoring | /demos/wild_salmon_migration_monitoring/, /demos/coral_reef_health_monitoring/ |
| wild_salmon_migration_monitoring | marine, vision | monitoring_smolt_salmon_migration_with_sonar, trout_identification, coral_reef_health_monitoring | /demos/smolt_sonar_monitoring/, /demos/trout_identification/ |
| wadden_sea_seal_monitoring | marine, identification, vision | trout_identification, wild_salmon_migration_monitoring | /demos/seal_identification/, /demos/trout_identification/ |
| snow_leopard_monitoring (+ `space: /demos/snowleopard_identification/`) | identification, camera traps, vision | bear_identification, trout_identification, biowatch-app | /demos/bear_identification/, /demos/trout_identification/ |
| elephants_passive_acoustic_monitoring | acoustics, audio | bat_calls_classification, early_forest_fire_detection | /demos/forest_elephant_rumble_detection/ |
| bat_calls_classification | acoustics, audio | elephants_passive_acoustic_monitoring | /demos/forest_elephant_rumble_detection/ |
| early_forest_fire_detection | wildfire, edge, vision | carpathian-bear-deterrence, coral_reef_health_monitoring | /demos/temporal_smoke_verification/ |
| bird_flu_monitoring | vision, identification | wadden_sea_seal_monitoring, wild_salmon_migration_monitoring | /demos/seal_identification/ |
| biowatch-app | camera traps, vision | snow_leopard_monitoring, bear_identification, bird_flu_monitoring | /demos/bear_identification/, /demos/snowleopard_identification/ |

All `related_spaces` paths above reference demos confirmed to exist:
`/demos/{bear_identification, coral_reef_health_monitoring,
early_forest_fire_detection, forest_elephant_rumble_detection,
human_wildlife_bear_conflict, seal_identification, smolt_sonar_monitoring,
snowleopard_identification, temporal_smoke_verification, trout_identification,
wild_salmon_migration_monitoring}/`.

### Component 2 — Template changes (`layouts/projects/single.html`)

Three sections. All use `where ... "intersect" ...` for tag overlap and
`site.GetPage` for slug/path resolution (the resolution helpers already used in
this template and the sidebar widget). Unresolved slugs/paths are skipped.

**2a. Related reading (replace existing section 6, lines 146–163).** Keep the
heading and markup. Change the inner logic to curated-first then tag-fill:

```go-html-template
{{/* ---------- 6. RELATED READING ---------- */}}
{{ $postLimit := 3 }}
{{ $curatedPosts := slice }}
{{ range .Params.related_posts }}
  {{ with site.GetPage "posts" . }}
    {{ $curatedPosts = $curatedPosts | append . }}
  {{ end }}
{{ end }}
{{ $postFill := slice }}
{{ if .Params.tags }}
  {{ range where ( where site.RegularPages "Section" "posts" ) ".Params.tags" "intersect" .Params.tags }}
    {{ if not (in $curatedPosts .) }}
      {{ $postFill = $postFill | append . }}
    {{ end }}
  {{ end }}
{{ end }}
{{ $relatedPosts := first $postLimit ( $curatedPosts | append $postFill ) }}
{{ if $relatedPosts }}
<section class="section project-related">
  ... existing markup ...
    <div class="row">
      {{ range $relatedPosts }}
        {{ partial "article.html" . }}
      {{ end }}
    </div>
  ...
</section>
{{ end }}
```

**2b. Related projects (replace existing section 7 "Next project", lines
165–178).** Rename heading to "Related projects". Curated-first, tag-fill to 3,
exclude self; if the result is empty, fall back to `.PrevInSection` so the
section is never empty:

```go-html-template
{{/* ---------- 7. RELATED PROJECTS ---------- */}}
{{ $projLimit := 3 }}
{{ $curatedProj := slice }}
{{ range .Params.related_projects }}
  {{ with site.GetPage "projects" . }}
    {{ if ne .Permalink $.Permalink }}
      {{ $curatedProj = $curatedProj | append . }}
    {{ end }}
  {{ end }}
{{ end }}
{{ $projFill := slice }}
{{ if .Params.tags }}
  {{ range where ( where ( where site.RegularPages "Section" "projects" ) ".Params.tags" "intersect" .Params.tags ) "Permalink" "!=" .Permalink }}
    {{ if not (in $curatedProj .) }}
      {{ $projFill = $projFill | append . }}
    {{ end }}
  {{ end }}
{{ end }}
{{ $relatedProj := first $projLimit ( $curatedProj | append $projFill ) }}
{{ if not $relatedProj }}
  {{ with .PrevInSection }}{{ $relatedProj = slice . }}{{ end }}
{{ end }}
{{ if $relatedProj }}
<section class="section project-next">
  ... existing markup, heading "Related projects" ...
    <div class="row">
      {{ range $relatedProj }}
        {{ partial "project-card.html" . }}
      {{ end }}
    </div>
  ...
</section>
{{ end }}
```

**2c. Try these demos (new section, inserted after related projects).** Render
curated `related_spaces`; show only if at least one resolves:

```go-html-template
{{/* ---------- 8. TRY THESE DEMOS ---------- */}}
{{ $demos := slice }}
{{ range .Params.related_spaces }}
  {{ with site.GetPage . }}
    {{ $demos = $demos | append . }}
  {{ end }}
{{ end }}
{{ if $demos }}
<section class="section project-demos">
  <div class="container"><div class="row"><div class="col col-12"><div class="container__inner">
    <div class="section__info">
      <div class="section__head"><h2 class="section__title">Try these demos</h2></div>
      <svg ...> (reuse the existing chevron svg markup) </svg>
    </div>
    <div class="row">
      {{ range $demos }}
        <div class="col col-6 col-t-12">
          <a href="{{ .RelPermalink }}">{{ .Title }}</a>
        </div>
      {{ end }}
    </div>
  </div></div></div></div>
</section>
{{ end }}
```

The demo card markup should follow the simplest existing pattern that renders a
linked space title (reuse `recent-project` / `project-card` styling if a demo
page exposes the needed params; otherwise a titled link as above). Implementer
chooses the closest existing partial at build time; the contract is: a heading
"Try these demos" and one linked entry per resolved space, in order.

### Data flow

```
project .md frontmatter ──┐
  tags / related_projects  ├─► single.html
  related_posts            │     6. related reading: curated posts + tag-fill (≤3)
  related_spaces           │     7. related projects: curated + tag-fill (≤3), else PrevInSection
data/tags.yaml ────────────┘     8. try these demos: resolved related_spaces
  (emoji per theme tag)
```

### Error handling

- Unresolved `related_projects` slug, `related_posts` slug, or `related_spaces`
  path → silently skipped (`with site.GetPage` is a no-op when nil).
- Self-reference excluded from related projects (`ne .Permalink $.Permalink`).
- Related projects never empty: falls back to `.PrevInSection`.
- Related reading / demos sections render nothing if their list is empty
  (guarded by `{{ if ... }}`), matching today's behavior.

## Testing / Verification

No unit-test harness; verify via local build:

1. `hugo --gc --minify` builds clean (no errors/warnings new to this change).
2. Spot-check built HTML for representative projects:
   - `bear_identification` → Related projects shows carpathian-bear-deterrence,
     trout_identification, snow_leopard_monitoring (curated order); "Try these
     demos" shows trout + snow leopard demos.
   - `wadden_sea_seal_monitoring` (no curated `related_posts`) → Related reading
     is non-empty via tag-fill (marine/identification posts); Related projects
     shows trout + salmon.
   - `early_forest_fire_detection` → "Try these demos" shows the temporal smoke
     verification demo.
3. Confirm no project shows an empty "Related projects" section.

## Files Touched

- `layouts/projects/single.html` — sections 6, 7 rewritten; new section 8.
- `content/projects/*.md` — 13 files: add `tags`, `related_projects`,
  `related_spaces`; add `space` to `snow_leopard_monitoring`.

- `data/tags.yaml` — add `aquatic`/`freshwater` emoji entries and re-purpose
  `marine` (see implementation note 6).
- `content/posts/*/index.md` — 3 marine posts re-tagged to the aquatic scheme.

## Implementation notes (deviations from the draft above)

Two refinements were made and approved during implementation:

1. **Section order: Related projects → Try these demos → Related reading.** The
   draft placed reading first; the final order keeps visitors in the
   project/portfolio world first, with reading last.

2. **Fallback excludes broad axis tags and sorts by date.** Tag-fill (for both
   related reading and related projects) intersects on *theme* tags only —
   `vision`/`audio` are removed via
   `complement (slice "vision" "audio") .Params.tags` — and iterates
   `site.Pages.ByDate.Reverse`. Without this, the near-universal `vision` tag
   pulled unrelated newest posts (e.g. wildfire posts onto the seal project).

3. **Slug/path resolution avoids `site.GetPage` for projects and demos.** A
   project and a demo can share a basename (e.g. `trout_identification`), which
   makes `site.GetPage` raise "page reference … is ambiguous". Final code matches
   within the section instead: projects by `.File.ContentBaseName`, demos by
   `.RelPermalink`. Posts still use `site.GetPage "posts"` (no collisions).

4. **"Try these demos" always leads with the project's own demo.** The
   project's own `space` (if set) is prepended to `related_spaces`, then the
   combined list is resolved and deduped — so a project's own interactive demo
   always appears first, and a self-listed space never doubles up.

5. **Demo cards render `card_image`, not `image`.** Demo pages expose
   `card_image` (an SVG), so the demos section renders cards via the
   `space-image.html` partial rather than reusing `project-card.html` (which
   reads `image`).

6. **Aquatic tag scheme refined.** The single `marine` tag was inaccurate for
   freshwater species. Replaced with an umbrella `aquatic` tag (keeps water
   species clustered for fallback) plus precise habitat tags: `freshwater`
   (trout, wild salmon, smolt) and `marine` (coral, seal). Applied to both
   projects and the matching posts; new emoji entries added to `data/tags.yaml`.
   `bird_flu_monitoring` lost its `identification` tag (it counts/detects birds
   rather than identifying individuals; now `vision` only).

7. **No curated reciprocal back-links.** Sink-node projects (seal, bird_flu) are
   surfaced as related where tags overlap via the `aquatic` fallback rather than
   by hand-editing back-links into other projects' top-3 (which the 3-item cap
   would truncate anyway).
