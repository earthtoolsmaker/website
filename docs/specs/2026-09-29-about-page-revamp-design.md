# About page revamp

## Goal

Rework the About page body for **prospective partners and clients** (NGOs, agencies, research labs) deciding whether earthtoolsmaker can take their problem, or their research, all the way to a system running in the field. The page argues one thing, **we bridge academia and field use**, and ends with a single ask: start a project.

The positioning also changes: earthtoolsmaker no longer builds only open-source software, so the page stops claiming everything is open source, and leans less on "AI" (matching the homepage refresh in #164).

## Already done on this branch (context)

- Homepage-style photo hero via the shared `partials/photo-hero.html`: eyebrow "About us", title "From the research lab *to the field*.", new description, buttons "Work with us" (`/contact/`) and "Meet the team" (`#team`).
- The site stats card overlaps the bottom of the hero, as on the homepage; the old in-body `about_stats` shortcode and `section-about-stats.html` are removed.
- Content sits in `.container` (the hero copy's left edge) via `.layout-about--wide`; prose is capped at 760px; 80px (60px mobile) below the stats card, matching the homepage.
- Open-source wording removed from the lead, the bold line, services card 04, the work-in-field closing line and Arthur's bio; "EarthToolsMaker" lowercased in the timeline.

Everything below replaces the body under the hero. The hero and stats card are not touched.

## Page structure

| # | Section | Replaces |
|---|---------|----------|
| 1 | Hero + stats card | (unchanged) |
| 2 | The gap | lead paragraph + bold line |
| 3 | How we work | What We Do (4 service cards) |
| 4 | From paper to field | Work in the Field (4 case-study rows) |
| 5 | The team | The Team (click-to-reveal bios) |
| 6 | The journey | The Journey (3 paragraphs) |
| 7 | Trusted by | Our Partners (full-bleed logo carousel) |
| 8 | Closing ask | "Help us keep these tools in the field" box **and** "Have a conservation challenge?" box |

Every section stacks to one column on phones (<= `$mobile`), and is checked at 1440, 900 and 390px.

## Sections

### 2. The gap

Two columns (5fr / 6fr): a serif statement on the left, body text on the right. Stacks on mobile, statement first.

- Statement: "A paper is not a tool *a ranger can run*." (accent in teal italic, same `<span><i>` convention as the hero)
- Body: "Conservation teams collect more data than they can ever look at: years of audio, millions of camera-trap photos, endless hours of underwater video. Research labs publish methods that could help, but they rarely leave the lab. We're a small team of engineers and ecologists who carry them the rest of the way."

Content lives in `content/about.md` front matter (`gap_statement`, `gap_body`), rendered by the layout.

### 3. How we work

Section title + intro, then a horizontal four-step path: a RESEARCH ... FIELD axis label above a gradient line (light teal to teal) with a dot per step, number, title and one sentence under each dot. On mobile the line turns vertical (left border) and steps stack, axis label hidden.

- Intro: "Every project follows the same path, from what the research makes possible to what runs in the field every day."
- 01 **Start from the field problem**: We sit down with the people collecting the data: what they record, where, and what decision it should feed.
- 02 **Build on the best research**: We start from published methods and models, adapt them to your species, sites and sensors, or train new ones on your data.
- 03 **Deploy where the data is**: A camera on a riverbank, a server in a ranger station, or the cloud: systems built for the power and connectivity you actually have.
- 04 **Keep it running**: Monitoring, retraining and support season after season, so the system still works when conditions change.

Data: `data/services.yaml` `services` list is replaced by `steps` (title, description). `section-services.html` becomes `section-how-we-work.html`.

### 4. From paper to field

Title + intro, then one featured story (left, ~1.35fr) and two smaller stories stacked (right, ~1fr). Featured: large photo, topic tag, serif title, RESEARCH / FIELD rows, partner line. Small: thumbnail beside tag, title, one sentence. Each story links to its project or tool (photo and title). Below: the existing "Explore all N projects on our projects page, or browse the tools behind them." line. On mobile: featured first at full width, the two small stories below with the thumbnail beside the text.

- Intro: "Three projects, three places where published research became something people rely on every day."
- Featured, WILDFIRE, "28 papers in, one smoke verifier out". Research: "We surveyed the literature, raced 28 published methods on a shared leaderboard, and kept what won." Field: "Pyronear's production smoke verifier: 4× fewer false alarms, smoke spotted 35 km away." With Pyronear. Link `/projects/early_forest_fire_detection/`, image `projects/early_forest_fire_detection/cover.jpg`.
- SEABIRDS, "Every bird in the colony, from the sky": "AI-BIRD surveys 10 seabird species, alive or dead, to track avian influenza." With Lumax AI and Sovon. Link `/tools/ai-bird/`, image `projects/bird_flu_monitoring/cover.png`.
- SALMON, "Counting every salmon, every river": "SalmonVision counts migrating salmon in real time at 34 sites." With the Pacific Salmon Foundation. Link `/projects/wild_salmon_migration_monitoring/`, image `projects/wild_salmon_migration_monitoring/cover.png`.

Data: `data/services.yaml` `examples` is replaced by `proof` (tag, title, research, field, with, link, image, featured flag). `section-work-in-field.html` becomes `section-paper-to-field.html`. The old `.case-study*` styles and the `.layout-about--wide .case-study__image` override go if nothing else uses them.

### 5. The team

Title + intro, then a 2 × 2 grid; each person is a row: round photo (84px) beside name, role, tags, bio (always visible), social links. One column on tablet and mobile, keeping the photo beside the text (64px photo on mobile). Keeps `id="team"` for the hero button.

- Intro: "Ecologists and engineers in one small team, so the research and the field problem are always in the same room."
- Tags, two kinds: research/ecology (teal tint) and engineering (terracotta tint).
  - Arthur Caillau: Engineering *(assumption: from the answer "Engineering"; confirm)*
  - Jeremy Vuillermet: Frontend, Product design
  - Eelke Folmer: Ecology, Geospatial, Drones
  - Thor Veen: Evolutionary biology, Computer vision
- Bios, shortened to one sentence:
  - Arthur: "Bridging conservation research and field use, turning promising methods into tools conservationists rely on."
  - Jeremy: "Puts conservation technology into the hands of field researchers, with interfaces that make complex tools simple."
  - Eelke: "Bridges ecology and technology through geospatial analytics, drone imagery and photogrammetry."
  - Thor: "Evolutionary biologist turned conservation technologist, building wildlife monitoring with computer vision."

Data: `data/team.yaml` gains `tags` (list of `{label, kind: research|engineering}`); `bio` is shortened. The click-to-reveal button, its JS and `.team-card--open` styles go.

### 6. The journey

Vertical timeline, **newest year first**, built to grow. Each year: a right-aligned year column (serif year, short title under it; the current year gets a "THIS YEAR" badge) and, on a vertical line, one entry per milestone: topic tag, one sentence, optional link. Current-year dots are filled, older ones hollow. The two most recent years are shown; older years sit in a `<details>` with a "Show 2024" / "Show earlier years" summary (no JS). On mobile the year sits above its entries.

Deviation from the mockup: the mockup showed one year on phones; with `<details>` and no JS, two years show on every size. Simpler, and still short.

- 2026, "From research to platforms" (THIS YEAR)
  - SEABIRDS: AI-BIRD, built with Lumax AI and Sovon, surveys seabird colonies from drone flights to track avian influenza. It started as a 2024 idea waiting for funding. Link AI-BIRD, `/tools/ai-bird/`.
  - COASTS: Drone monitoring of erosion and land cover on the Wadden Sea for Rijkswaterstaat. Link `/projects/coastal_erosion_monitoring/`.
  - WILDFIRE: 28 research papers raced head to head became Pyronear's production smoke verifier, with 4× fewer false alarms. Link `/projects/early_forest_fire_detection/`.
  - SALMON: Sonar counts smolt runs no camera could see. Link `/projects/monitoring_smolt_salmon_migration_with_sonar/`.
- 2025, "Tools others can run"
  - CAMERA TRAPS: BioWatch turns camera-trap archives into maps and insights.
  - SEALS: Seal surveys take off over the Wadden Sea.
  - SNOW LEOPARDS: Snow leopard monitoring begins in the mountains of Central Asia.
- 2024, "First field deployments" (folded)
  - CORAL REEFS: Coral reef health monitoring.
  - ELEPHANTS: Forest elephant acoustics with Cornell.
  - BEARS: Bear identification.
  - SALMON: SalmonVision starts counting fish on British Columbia rivers.

"This year" is the first entry in the list, not computed from the build date. Data: `data/about.yaml` `timeline` becomes `[{year, title, items: [{tag, text, link?, link_label?}]}]`, newest first.

### 7. Trusted by

A single row between thin top/bottom rules: "TRUSTED BY" label, logos, "All N partners ›" link to `/partners/` (N from `partner-count.html`). No section heading. Colour logos at a uniform height (~40px desktop, ~32px mobile); wraps on mobile. Seven logos: Pyronear, Wild Salmon Center, Pacific Salmon Foundation, Cornell Lab of Ornithology, Sovon, Rijkswaterstaat, Foundation Conservation Carpathia (chosen to cover the proof stories and the journey). Picked by name from `params.partner_item` via a `trusted_by` list in `data/about.yaml`, reusing the dark-variant and resize logic from `partners-logo-slider.html` (extracted into a small `partner-logo.html` partial so both use it).

`section-about-partners.html` and its `about_partners` shortcode are removed from the page; the homepage testimonials band keeps the carousel.

### 8. Closing ask

The Support page's warm band (`support__cta-band` look): text left, actions right; stacks on mobile.

- Title "Have a conservation challenge?", description "Tell us about your data and your field problem, and we'll give you an honest read on what's possible and what it would take."
- Primary button "Start a project" to `/contact/`.
- Under it, a text line for funders: "Funding conservation? Support our work" (link to `/support/`).

Replaces both boxes; `data/about.yaml` `support_cta` is removed.

## Implementation notes

- `content/about.md` stays the entry point: front matter holds hero + gap copy; the body lists the section shortcodes in order (`how_we_work`, `paper_to_field`, `team`, `about_timeline`, `trusted_by`, `about_closing`).
- Styles go in `assets/sass/4-layouts/_about.scss`, scoped under `.layout-about--wide` or new block classes, so Partners (which shares `.layout-about`) does not change. Remove styles orphaned by the removed sections.
- Section spacing stays the About value (`.layout-about .section`, 56px).
- Copy rules: `earthtoolsmaker` in lowercase, no em-dashes.

## Out of scope

- The hero and stats card.
- Site-wide "open source" wording elsewhere (tools page, CTAs incl. `build-cta.html`, Support tracks, `config.toml`): separate PR.
- `content/privacy-policy.md` "EarthToolsMaker".
- Bird Flu Monitoring project `status: fundraising` now that AI-BIRD shipped.

## Verification

- Clean `hugo` build (0.145 extended), no errors or warnings.
- All other pages render identical HTML to `main` (whitespace and CSS hash aside); Partners screenshot unchanged.
- About screenshots at 1440, 900, 390px for every section; `#team` button scrolls to the team; journey `<details>` opens; all links resolve (no 404 in the built site).
