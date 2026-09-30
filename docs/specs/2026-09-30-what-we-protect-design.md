# What we protect: species and ecosystem pages

## Goal

Add a browsable hub of the species and ecosystems earthtoolsmaker protects or monitors. Each page is light: a short header, a sourced fact sheet, then everything we have built for that species or ecosystem (projects, live demos, tools, blog posts). It is a navigation layer, not a storytelling or SEO effort.

## 1. Data model

- **One combined Hugo taxonomy** named `nature`, living at `/nature/`. Species and ecosystems share it and are told apart by a `nature_kind` field on the term page. `config.toml` gets:
  ```toml
  [taxonomies]
    tag = "tags"
    nature = "nature"
  ```
  (Declaring `[taxonomies]` replaces Hugo's defaults, so `tags` is listed explicitly. `categories` is unused in the content and is dropped.)
- **Tagging:** projects, demos, tools and posts carry `nature: [slug, ...]` in front matter, any mix of species and ecosystem slugs.
- **Term pages:** `content/nature/<slug>/_index.md`, front matter:
  ```yaml
  title: Snow leopard
  nature_kind: species           # species | ecosystem (`kind` is reserved by Hugo)
  scientific_name: Panthera uncia  # species only; omitted for group terms that span several species
  iucn_status: VU                # species only: LC | NT | VU | EN | CR; omitted for group terms
  summary: One or two sentences, shown in the hero and as the card excerpt.
  image: /images/nature/snow-leopard/hero.jpg
  photo_credit:
    name: Photographer Name
    url: https://unsplash.com/photos/...
  facts:
    - label: Population
      value: "4,000 to 6,500 adults"
      source: iucn               # must match a key in sources
  sources:
    - key: iucn
      name: IUCN Red List
      url: https://www.iucnredlist.org/...
  ```
  Every fact names a source; every source is listed under "Learn more".
- **Section page:** `content/nature/_index.md` holds the index hero copy.
- **Photos:** `assets/images/nature/<slug>/hero.jpg` (one photo per term, used for both hero and card, through `responsive-image.html`). Source: Unsplash, downloaded (never hotlinked), at least 2000px wide, photographer credited via `photo_credit`. Where the repo already holds a better, licensed photo of the exact species (for example a project photo), it may be used instead, credited the same way.

## 2. Terms

Rule: one term per species when a project is really about that animal; a group term when a model covers a whole group of species (the group page names the species in its summary or facts). Terms that would list identical content to another term are not created.

**Species (9)**

| Slug | Title | Notes |
|------|-------|-------|
| `brown-bear` | Brown bear | *Ursus arctos* |
| `snow-leopard` | Snow leopard | *Panthera uncia* |
| `african-forest-elephant` | African forest elephant | *Loxodonta cyclotis* |
| `harbour-seal` | Harbour seal | *Phoca vitulina* |
| `grey-seal` | Grey seal | *Halichoerus grypus* |
| `rainbow-trout` | Rainbow trout | *Oncorhynchus mykiss* |
| `pacific-salmon` | Pacific salmon | group: Chinook, Coho, Sockeye, Pink, Chum, Steelhead |
| `seabirds` | Seabirds | group: the ten seabird species AI-BIRD recognises |
| `cambodian-bats` | Cambodian bats | group: about 31 species recorded, incl. Lyle's flying fox |

**Ecosystems (6)**

| Slug | Title |
|------|-------|
| `coral-reefs` | Coral reefs |
| `rivers` | Rivers |
| `temperate-forests` | Temperate forests |
| `tropical-rainforests` | Tropical rainforests |
| `high-mountains` | High mountains |
| `wadden-sea-and-coasts` | Wadden Sea and coasts |

15 terms in total.

Reef-building corals as a species term was dropped: it would list exactly the same content as Coral reefs.

## 3. Tagging map

Only content specifically about a term is tagged. Left untagged: Biowatch (project and tool), EarthRanger scaling (project and post), the metric-learning guide, the identification data-prep post, the volunteering post.

| Content | `nature` terms |
|---------|----------------|
| project `bear_identification` | brown-bear, temperate-forests |
| project `carpathian-bear-deterrence` | brown-bear, temperate-forests, high-mountains |
| project `snow_leopard_monitoring` | snow-leopard, high-mountains |
| project `elephants_passive_acoustic_monitoring` | african-forest-elephant, tropical-rainforests |
| project `wadden_sea_seal_monitoring` | harbour-seal, grey-seal, wadden-sea-and-coasts |
| project `trout_identification` | rainbow-trout, rivers |
| project `wild_salmon_migration_monitoring` | pacific-salmon, rivers |
| project `monitoring_smolt_salmon_migration_with_sonar` | pacific-salmon, rivers |
| project `bird_flu_monitoring` | seabirds, wadden-sea-and-coasts |
| project `bat_calls_classification` | cambodian-bats |
| project `coral_reef_health_monitoring` | coral-reefs |
| project `early_forest_fire_detection` | temperate-forests |
| project `coastal_erosion_monitoring` | wadden-sea-and-coasts |
| demo `bear_identification` | brown-bear, temperate-forests |
| demo `human_wildlife_bear_conflict` | brown-bear, temperate-forests |
| demo `snowleopard_identification` | snow-leopard, high-mountains |
| demo `forest_elephant_rumble_detection` | african-forest-elephant, tropical-rainforests |
| demo `seal_identification` | harbour-seal, grey-seal, wadden-sea-and-coasts |
| demo `trout_identification` | rainbow-trout, rivers |
| demo `wild_salmon_migration_monitoring` | pacific-salmon, rivers |
| demo `smolt_sonar_monitoring` | pacific-salmon, rivers |
| demo `coral_reef_health_monitoring` | coral-reefs |
| demo `early_forest_fire_detection` | temperate-forests |
| demo `temporal_smoke_verification` | temperate-forests |
| tool `animal-reid` | brown-bear, harbour-seal, grey-seal, rainbow-trout |
| tool `salmonvision` | pacific-salmon, rivers |
| tool `ai-bird` | seabirds, wadden-sea-and-coasts |
| tool `pyronear` | temperate-forests |
| post `bear-face-segmentation-guide` | brown-bear |
| post `bear-identification-with-metric-learning-guide` | brown-bear |
| post `how-to-build-a-real-time-bear-detection-system` | brown-bear |
| post `how-to-analyze-elephant-rumbles-at-scale` | african-forest-elephant, tropical-rainforests |
| post `how-to-build-a-benthic-coral-reefs-analyser` | coral-reefs |
| post `local-feature-matching-lightglue` | rainbow-trout |
| post `tracking-the-journey-how-to-monitor-wild-salmon-migrations` | pacific-salmon, rivers |
| post `protecting-the-forest-early-forest-fire-detector` | temperate-forests |
| post `racing-models-not-opinions` | temperate-forests |
| post `smoke-is-a-behavior` | temperate-forests |
| post `mapping-a-salt-marsh-centimetre-by-centimetre` | wadden-sea-and-coasts |
| post `watching-a-coastline-move` | wadden-sea-and-coasts |

Before tagging, the implementer checks each item's body for the species it actually covers (for example, whether `local-feature-matching-lightglue` uses trout or another animal, and whether `animal-reid` covers seals and trout) and adjusts the row if the content says otherwise.

## 4. Index page `/nature/` (`layouts/nature/terms.html`, Hugo 0.145's lookup name for a taxonomy list)

1. `photo-hero.html`: eyebrow "What we protect", a title with the usual italic accent, a one-line description, buttons "Start a project" (`/contact/`) and "Browse projects" (`/projects/`). Copy in `content/nature/_index.md`, hero photo at `assets/images/pages/nature/hero.jpg` (Unsplash).
2. **Species** grid, then **Ecosystems** grid, split on `nature_kind`. Each tile is the shared `card.html`: photo, title, scientific name (or summary for group terms and ecosystems) as excerpt, and a footer meta such as "3 projects · 2 demos" (only non-zero counts, over projects, demos, tools, posts).
3. Species sorted by number of tagged items (descending, then title); ecosystems sorted by title.
4. Section titles follow the site's current emoji-free style.

## 5. Term page `/nature/<slug>/` (`layouts/nature/term.html`)

1. **Hero:** `photo-hero.html` with the term photo; eyebrow "Species" or "Ecosystem"; title; scientific name in italics under it (species only); summary as the description. Species with `iucn_status` show a small pill badge with the full category name ("Vulnerable"), coloured by category (LC green, NT yellow-green, VU yellow, EN orange, CR red), linking to its IUCN source when one has key `iucn`. Photo credit appears as small text at the bottom of the hero ("Photo: Name / Unsplash", linked).
2. **About:** a compact grid of facts (label over value), each value followed by a superscript number linking to its entry in "Learn more".
3. **Our work:** up to four sections in this order, each hidden when empty: Projects, Live demos, Tools, Blog posts. All use `card-for-page.html`, which already picks the right card look per section (project, demo, tool, post).
4. **Learn more:** numbered list of sources (name, linked, `target="_blank" rel="noopener"`), numbering matching the fact superscripts.
5. `projects-cta.html` at the bottom, as on the projects listing.

## 6. Links into and out of the section

- `config.toml`: new `[[menu.main]]` entry under `work`, name "What we protect", url `/nature/`, weight 4 (after Live Demos). No footer entry for now.
- `layouts/partials/site-stats.html`: the Species tile links to `/nature/` instead of `/posts/`. Its value stays the hand-set "10+" from `data/about.yaml` (a term count would undercount, since group terms stand for several species).
- **Project pages** (`layouts/projects/single.html`): the project's `nature` terms render as small linked chips (term title) near the top of the page, as small teal outline pills (project pages show no tag chips today, so this is a new element). Other page types get no chips for now.

## 7. Facts and sources

- Drafted by Claude from IUCN Red List, GBIF, Wikipedia, and reputable conservation sources (WWF, NOAA, partner sites); reviewed by Arthur before merge.
- 3 to 5 facts per term. Species: IUCN status, population, range, habitat, plus one ecological role fact. Groups and ecosystems: extent, diversity, main threats.
- No figure without a source. Where sources disagree, give the range and cite the more authoritative source.
- Copy follows site rules: `earthtoolsmaker` lowercase, no em-dashes.

## 8. Verification

- `hugo` builds with no errors or warnings.
- Every term page renders, is non-empty, and lists exactly the items from the tagging map.
- Every fact's `source` key resolves to a listed source; every source URL returns HTTP 200 (curl).
- Screenshots of `/nature/`, one species page (snow leopard) and one ecosystem page (rivers), at desktop and phone widths; no horizontal scroll on phones. (The site is light-only, `color_scheme = "light"`, so there is no dark mode to check.)
- The Work dropdown entry, the stats band Species tile, and project-page chips all resolve to the right pages.
