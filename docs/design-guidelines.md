# Design Guidelines

How the earthtoolsmaker site looks, reads and is built. These rules describe the
site as it is today, distilled from the SCSS, the layouts and the design specs in
`docs/specs/`. When a spec and this document disagree, the more recent decision
wins; update this file when you make a new one.

**Reference pages.** When in doubt, match these: About (`/about/`), Support
(`/support/`), a revamped project page (e.g. `/projects/wild-salmon/`), and the
listing cards on the homepage.

---

## 1. Principles

1. **Calm and credible.** A conservation nonprofit talking to scientists and
   funders. Real photos, real numbers, named partners. No hype, no decoration
   for its own sake.
2. **One accent at a time.** Deep teal carries interaction. Terracotta is rare
   and means "act now" or "this is a step". Everything else is white, hairlines
   and ink.
3. **Serif for voice, sans for work.** Newsreader headings give the editorial
   tone; Mulish handles body, UI and labels.
4. **Reuse before you invent.** Cards, CTAs, heroes and stats already exist as
   partials. A new page is mostly assembly.
5. **Light, fast, accessible.** Responsive WebP images, lazy loading, reduced
   motion respected, visible focus everywhere.

---

## 2. Color

Tokens live in `assets/sass/0-settings/_color-scheme.scss`. Use `var(--token)`,
never a raw hex, for anything the tokens cover.

| Token | Value | Use it for |
|---|---|---|
| `--secondary-color` | `#006d77` deep teal | Primary buttons, links on hover, nav active underline, card title hover, focus rings, eyebrows on light backgrounds |
| `--button-background-hover` | `#00444c` | Hover state of teal buttons |
| `--primary-color` | `#83c5be` mint | Eyebrows and italic accents on dark photo washes, tints, input focus |
| `--tertiary-color` | `#e29578` terracotta | `.button--cta`, diagram arrows and step labels. Sparingly. Hover `#d77f5e` |
| `--accent-color` | `#ffddd2` peach | Default logo tint behind tool cards (`card_tint` overrides) |
| `--dark` / `--text-color` | `#161616` | Body text, headings, button offset shadow |
| `--gray` / `--text-alt-color` | `#60626a` | Secondary text, excerpts, meta |
| `--light-gray` | `#e1e4e9` | Card and surface hairline borders |
| `--border-color` | `#ede0d4` sand | Header hairline, diagram card strokes |
| `--light-blue` / `--background-alt-color` | `#fbf6f6` | Alt backgrounds, diagram card fill (legacy cream) |
| `--white` | `#fff` | Card and page surfaces |

**Photo wash** (heroes and CTA bands):
`linear-gradient(90deg, rgba(8,32,36,.88) 0%, rgba(8,32,36,.6) 55%, rgba(8,32,36,.2) 100%)`.
Text on it is white, with 85% white for descriptions and mint for eyebrows.

**Scoped palettes** are fine when they are local to one component and declared
as custom properties at its root, like the footer's `--soil-*` palette in
`_footer.scss`. IUCN status colors in `_nature.scss` are an accepted exception
(they follow the IUCN standard).

**Don't**
- Use gradients on text or as placeholders. `--text-gradient` and the purple to
  red `#e66465 / #9198e5` placeholders are legacy.
- Introduce a new brand color. If a tint is needed, derive it from teal, mint or
  terracotta.
- Rely on dark mode. The site is light only (`color_scheme = "light"` in
  `config.toml`); the `:root[dark]` block is leftover template code.

---

## 3. Typography

Fonts are loaded from Google Fonts in `layouts/partials/head.html`.

| Role | Family | Weights loaded |
|---|---|---|
| Headings, hero titles, card titles in diagrams | Newsreader (`$heading-font-family`), optical size 6..72 | 400, 600, 700; italic 400, 500 |
| Body, UI, labels | Mulish (`$base-font-family`) | 400, 600, 700 |
| Footer labels only | IBM Plex Mono (`--soil-mono`) | 500 |

The wordmark is a baked PNG (`assets/images/logos/logo-word-*.png`), not live text.

Only use weights that are loaded. `font-weight: 800` renders as synthesized
bold; use 700.

**Scale** (`_variables.scss`): body 19px / 1.6. h1 36, h2 28, h3 24, h4 20,
h5 18, h6 16, line-height 1.3.

| Element | Size |
|---|---|
| `.section__title` | 28px / 600 (24px on mobile) |
| Homepage hero title | about 64 to 72px |
| CTA band title | 32px (26px on phones) |
| CTA card title | 24px (22px on phones) |
| Card title | 19px / 1.2 |
| Card excerpt | 14.5px / 1.55 |
| Card meta, date | 12.5px / 600 |

**Italic accent.** One phrase in a display title can be set in teal (or mint on
a photo) italic with `<span><i>...</i></span>`. One per title, never a whole
sentence.

**Eyebrows and kickers.** The standard label is Mulish **12px, 700, uppercase,
`letter-spacing: 0.12em`**, teal on light backgrounds and mint on photos. Join
multiple items with ` · `. Use it for hero eyebrows, CTA band eyebrows, tags and
section labels. Don't invent a new size or tracking for a new label.

**Emoji.** None in headings, section titles, body copy, tab labels, buttons or
cards. Use Font Awesome icons (`fa-solid ...`) or nothing. For emoji-free tabs
use the `::Label` form of the `tabs` shortcode.

---

## 4. Layout and spacing

**Breakpoints** (`assets/sass/1-tools/_grid.scss`). Styles are desktop first
with `max-width` queries:

| Variable | Value |
|---|---|
| `$wide` | 1400px |
| `$desktop` | 1024px |
| `$tablet` | 768px |
| `$mobile` | 576px |
| `$nav-collapse` | 900px (header only) |

Always use the variables, not hardcoded pixel values. Everything stacks to one
column at `$mobile`.

**Widths**
- `.container`: max 1332px, steps down per breakpoint, 16px gutters (20px on mobile).
- Reading column: 780px for posts, pages and project bodies. Prose blocks on
  About cap at 760px. Covers can go to 1000px.
- Tool and demo pages: 1280px frame.

**Vertical rhythm**
- `.section`: 80px apart (60px on mobile). Section heading to content: 36px.
- Block elements get a 32px bottom margin from `_shared.scss`; don't fight it
  with ad hoc margins.
- Base unit is 16px (`$base-spacing-unit`). Prefer multiples of 8.

**Grid.** 12 columns: `.col-N`, with `-w-`, `-d-`, `-t-`, `-m-` breakpoint
variants. A listing card is `col col-4 col-w-6 col-t-12`.

---

## 5. Surfaces: radius, border, shadow

There is one card surface. Reuse it for anything that sits on the page as a
panel.

```scss
background: var(--white);
border: 1px solid var(--light-gray);
border-radius: 14px;
box-shadow: 0 14px 32px -22px rgba(0, 0, 0, .3);
```

- **Elevated** (a panel overlapping a hero, like the hero stats card):
  `0 18px 40px -18px rgba(0,0,0,.35), 0 1px 0 var(--light-gray)`.
- **Radius scale:** 14px surfaces, 12px prose images, 8px chips and small logos,
  6px buttons, 999px pills, 50% avatars. `$global-radius: 22px` is legacy.
- **No hover lift.** Don't use `translateY(-4px/-8px)` on cards; that is the old
  template look. Hover changes color, not position.
- Divided groups (stats, partner grids) use `gap: 1px` over a border-colored
  background rather than individual borders.

---

## 6. Components

### Buttons (`_buttons.scss`)

The base `.button` has a crisp offset shadow that "presses" on hover:
teal background, white 15px/700 text, 6px radius, `4px 4px 0 #161616` shadow;
hover translates 3px and shrinks the shadow; active translates 4px with no
shadow.

| Class | When |
|---|---|
| `.button` | The primary action on a light background |
| `.button--secondary` | Secondary action next to a primary (white, teal text) |
| `.button--cta` | Terracotta. The one conversion action in a CTA partial |
| `.button--pill` | Quiet "see all" links in section headers, with a trailing icon |
| `.button--ghost` | Only inside `.about-cta` or `.support__cta-band` (it has no standalone style) |
| `.button--middle` | Wider padding for a lone centered button |

- Buttons are `<a class="button">` or `<button class="button">`, never a
  `<button>` inside an `<a>`.
- At most one primary and one secondary per group, 12px gap.
- Arrow icons: `fa-arrow-right` on primary, `fa-chevron-right` on secondary.

### Cards (`_card.scss`, `layouts/partials/card.html`)

One partial renders every listing card (posts, projects, tools, demos, nature):
`card-for-page.html` → `card.html`. In content, use the `article_card`,
`project_card` or `space_card` shortcodes, which render the same partial.

- Media band 10:7, full bleed: photo for projects and posts, logo on a tint for
  tools, SVG illustration for demos.
- Body: title (19px), excerpt clamped to 2 lines (posts) or 3 (others), footer
  pinned with `margin-top: auto` so rows align. Date on posts only, format
  `2 Jan, 2006`. Gray chevron that turns teal on hover.
- The whole card is clickable via `.card__link::after`; focus draws a teal
  outline around the card.
- Photos are 50% grayscale on desktop and full color on hover.
- Don't hand-write card markup. If a card needs a new field, extend
  `card.html` so every listing gets it.

### Calls to action

Two families, and nothing else:

1. **CTA band** (`.support__cta-band`, e.g. `build-cta.html`): the closing
   moment of a page. Photo under the teal wash, 14px radius, 48px padding, left
   aligned: eyebrow, title, description, buttons. Use once per page, at the end.
2. **CTA card** (`.about-cta`, e.g. `projects-cta`, `tools-cta`, `demo_cta`):
   a white surface mid-page. Two columns (copy left, actions right) at
   ≥1024px, stacked otherwise.

Copy: the title is a question the reader might ask ("Have a conservation
challenge?"), the button is a verb ("Start a project", "Talk to us", "Try the
live demo"). Project bands are status aware: completed projects ask "Want a
system like this?", fundraising ones say "Help fund this project".

### Heroes

- **Photo hero** (`photo-hero.html`): full-bleed photo, teal wash, eyebrow,
  title with an italic accent, one line of description, up to two buttons. The
  header floats over it (`header--overlay`). A stats card may overlap its
  bottom edge.
- **Tool hero** (`.tool-hero`): a short looping video, muted, autoplay,
  `playsinline`, 1280x720 H.264, no audio, about 1MB, hosted locally.
- **Project hero without a photo:** teal to mint gradient.

### Other building blocks

| Need | Use |
|---|---|
| Key numbers | `stats_card` shortcode / `stats-card.html` (`--three`, `--wide`) |
| Short list of reasons or benefits | `support__grid` + `support__card` (3 cards) |
| Pressures, threats, FAQ that reveal on click | `threats` shortcode, plus a "tap each to learn more" hint |
| Alternate views | `tabs` / `tab` (`::Label` form) |
| Before/after | `compare` |
| Photo series | `image_carousel` / `carousel_image` |
| Live model | `hf_space` (iframe embed with the pangolin loader) |
| Partner logos | `partner_logos`, `partner-logo.html` |
| Citations | `cite` |
| Collapsible outline | native `<details>` (see `post-toc.html`) |

---

## 7. Imagery

**Photos**
- Real field photos over stock. Never AI-generated images.
- Stock: Unsplash (downloaded, ≥2000px wide, credited "Photo: Name / Unsplash")
  or Mixkit (source noted in an HTML comment).
- Don't repeat a post's cover image in its body.
- Captions: `.media-caption` or an italic line under the image. Alt text on
  every image.

**Illustrations** (demo cards, homepage hero)
- Flat vector SVG, viewBox 1000x700, soft sky gradient
  (`#e4f1ee → #f7ddd2 → #d3e9e0`), layered hills from `#bfe0d6` to `#15463f`,
  a coral sun `#ef9d78`, dark teal silhouettes `#143b35`.
- Silhouettes from PhyloPic, CC0 only. Log every source in
  `docs/specs/spaces-illustration-credits.md`.

**Diagrams** (how-it-works figures)
- Animated inline SVG pipelines of 3 or 4 cards: white hairline cards,
  terracotta arrows and letter-spaced step labels, Newsreader titles, gray
  descriptions, teal and mint for the content.
- Put the positioning transform on the outer `<g>` and the animation on the
  inner `<g>`.
- Embed with markdown image syntax; the render hook passes SVG through untouched.
- Prefer a diagram to a flat PNG pipeline figure, but never replace real photos.

**Blog covers and share cards** are SVGs rendered to PNG (`cover.png`, 1500x1050;
`og-default.png`, 1200x630). Editing the SVG alone changes nothing on the site:
re-render the PNG. Covers use the white to pale teal background
(`#ffffff → #e3f0ee`).

**Icons.** Font Awesome 6 only. Decorative icons get `aria-hidden="true"`.

---

## 8. Motion

- Motion is small and purposeful: color transitions (0.2s), the button press
  (0.12s), a chevron nudging 2px, hero silhouettes drifting 8 to 16px over
  9 to 15s, the pangolin brandmark rolling on hover.
- Every animation needs a `@media (prefers-reduced-motion: reduce)` guard that
  turns it off or makes it instant.
- No scroll parallax, no reading progress bars, no sticky tables of contents,
  no entrance animations on content.
- Image lightbox only on desktop with a fine pointer:
  `(min-width: 768px) and (pointer: fine)`. Opt out with `.no-zoom`.

---

## 9. Voice and copy

- **Brand name:** `earthtoolsmaker`, always lowercase.
- **No em-dashes**, anywhere: copy, templates, data files, commit messages. Use
  commas, colons, parentheses or two sentences.
- **Tone:** warm, honest, specific. Active voice, concrete nouns. Name the
  partner, give the number, say what the tool actually does.
- **Never invent claims.** Numbers must be sourced. Avoid blanket "open source"
  or "AI-powered" positioning.
- **Banned words:** holistic, innovative, seamless(ly), cutting-edge.
- **Naming:** "Live demos" at `/demos/` (not "Spaces"), "live demo" (not "ML
  Space").
- **Buttons** start with a verb. **CTA titles** are questions.

---

## 10. Page templates

Build new pages from these skeletons.

**Project page**
Photo hero (kicker `Status · Tool`, title, tagline, 1 to 3 stats, partner chips)
→ facts bar (GitHub, demo, tools, date) → 780px body → partner strip →
status-aware CTA band → related projects → demos → related reading.

Body pattern: lede with no heading → blockquote → diagram → "Why X matters"
(3 cards) → "Under pressure" (`threats` pills) → how it works (+ diagram) →
conclusion + `demo_cta`.

**Tool page**
Video hero → 3-stat band → intro → carousel → "Why" pills → how it works →
in action (videos, tabbed demos) → closing CTA card → resource footer →
partners.

**Demo page**
Centered title and summary → steps → embedded demo → content → resource footer.

**Post page**
Tag kicker → title → description → `date · author · N min read` → cover →
"On this page" (2+ headings) → body → share, prev/next → 2 related cards.

**Listing page**
Intro → cards → CTA.

**Resource footer** (tools, demos): Font Awesome icons (`fa-circle-info`,
`fa-github`, `fa-book`, `fa-arrow-up-right-from-square`), links joined by
` · `, thin top border.

---

## 11. Accessibility

- Visible `:focus-visible` on every interactive element:
  `outline: 2px solid var(--secondary-color); outline-offset: 2px` (white on
  dark photo backgrounds).
- Decorative SVG and icons: `aria-hidden="true"`. Meaningful images: real alt
  text.
- Form fields have visible labels, not placeholders only.
- Tooltip content is mirrored into `aria-label`.
- Headings in order; `scroll-margin-top` so anchors clear the sticky header.
- Prefer native elements (`<details>`, `<button>`, `<a>`) to scripted ones.
- Text on photos always sits on the wash, never on the raw image.

---

## 12. Engineering best practices

**SCSS**
- Settings in `0-settings/`, reusable modules in `3-modules/`, page-specific
  styles in `4-layouts/`. Import new files in `main.scss`.
- BEM naming: `.block__element--modifier`.
- Colors from tokens; breakpoints from variables. If a value repeats in three
  places, it deserves a token or a variable.
- Before styling a new panel, check whether it is the card surface (§5). It
  usually is.
- Before changing a shared class, grep `layouts/` and `content/` for every
  consumer. Cards, CTAs and `.support__*` classes are used across many pages.

**Templates**
- New listing: `card-for-page.html`. New CTA: one of the existing CTA partials.
  New hero: `photo-hero.html`.
- Put structured page data in front matter or `data/`, not in raw HTML in
  markdown.
- Add a shortcode only when a pattern appears on at least two pages.

**Images**
- All images live in `assets/images/` and go through `responsive-image.html`
  (WebP, srcset, LQIP, lazy). Above-the-fold images: `lazy: false` and
  `fetchpriority: high`.
- Don't put `class="lazy"` on a plain `<img>`; it stays invisible without the
  `data-src` swap. Use `loading="lazy"`.
- See `docs/image-optimization.md`.

**Process**
- Write a spec in `docs/specs/YYYY-MM-DD-<topic>-design.md` for any visible
  change, and update this file if the change sets a new rule.
- Check every change at three widths (about 1440, 900 and 390px) in a built
  site (`hugo`), not only the dev server.
- Check the pages that share the component, not just the one you edited.

---

## 13. Known drift and open questions

These don't match the rules above yet. Fix them opportunistically, or decide
and update this document.

**Cleanup candidates**
- Legacy lift hovers with 22px radius: `.project__nav*` (`_project.scss`),
  `_tool.scss`, `_space.scss`, `_gallery.scss`; -4px lifts in `_partners.scss`,
  `_section-tags.scss`, `_about.scss`. `.project__nav` looks unused.
- Purple to red placeholder gradients still in `_space.scss` and `_tool.scss`.
- `:root[dark]` palette and the theme toggle JS in `common.js` are dead code.
- `font-weight: 800` in `.post-kicker` and `.post-toc__label` (not loaded).
- Eyebrow drift: tracking of 0.08em, 0.1em, 0.14em and 1px / 1.4px alongside
  the standard 0.12em.
- Transitions have no standard (`.12s` to `.3s`, `all` vs a named property).
- `.animate` entrance and `.button` press have no reduced-motion guard.
- `build-cta.html` nests a `<button>` inside an `<a>`.
- Nine raw `#fff` where `var(--white)` would do.
- `docs/image-optimization.md` says content images aren't optimized; the
  markdown render hook now processes them.

**Undecided**
- Card photos: 50% grayscale until hover (current code) or full color (an
  earlier spec)?
- Partner logos: grayscale on project pages but full color on tool pages and
  "Trusted by". Pick one.
- Timeline order: newest first (current About) is assumed everywhere.
