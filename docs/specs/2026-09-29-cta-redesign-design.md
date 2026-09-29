# CTA redesign

## Goal

Bring the site's calls to action in line with the newer design (photo heroes, stats card, partner and listing cards), and stop claiming that all earthtoolsmaker tools are open source.

The site has two CTA families; both are restyled in CSS so the ~40 existing uses (many written as raw HTML inside content pages) change without content edits:

| Family | Where | Becomes |
|--------|-------|---------|
| `.support__cta-band` | End of the homepage (`build-cta.html`), About closing (`section-about-closing.html`), project pages (both CTAs in `projects/single.html`), AI-BIRD and Biowatch tool pages (raw HTML) | **Photo band** (end of page) |
| `.about-cta` | Projects / Tools / Demos listing bottoms (`projects-cta`, `tools-cta`, `spaces-cta`), `demo_cta` shortcode, tool pages, Support and Partners pages, demo pages, posts (raw HTML) | **White card** (mid page) |

The Projects / Tools / Demos listing bottoms stay white cards (chosen explicitly).

## 1. Photo band (`.support__cta-band`)

- **Surface:** the Support page elephants photo (`assets/images/pages/support/hero.jpg`) as a cover background, under the heroes' dark teal wash: `linear-gradient(90deg, rgba(8, 32, 36, 0.88) 0%, rgba(8, 32, 36, 0.6) 55%, rgba(8, 32, 36, 0.2) 100%)` (the `.hero__overlay` values). `border-radius: 14px`, `overflow: hidden`. Padding about `48px 48px` desktop, `32px 24px` at `$tablet` and below. Falls back to `var(--secondary-color)` if the photo is missing.
- **Layout:** stacked and left-aligned (column flex), replacing today's text-left / buttons-right row:
  1. optional eyebrow `.support__cta-band-eyebrow`: 12px, 700, `letter-spacing: 0.12em`, uppercase, `var(--primary-color)`;
  2. title `.support__cta-band-title`: `$heading-font-family`, about 32px (26px on phones), white; an accent written as `<span><i>...</i></span>` renders italic in `var(--primary-color)`, as in `.hero__title`;
  3. description: white at 85% opacity, `max-width: 560px`;
  4. buttons, wrapping on small screens.
- **Buttons:** `.button` stays white with teal text and the offset shadow; on hover it fills teal (`var(--secondary-color)`) with white text. `.button--ghost` becomes a white outline pill: `border-radius: 999px`, `box-shadow: inset 0 0 0 1.5px rgba(255, 255, 255, 0.8)`, white text, 12% white fill on hover, no press motion.
- **Photo delivery:** `layouts/partials/head.html` gets the image with `resources.Get`, makes two WebP resizes (about 900px and 1600px wide), and emits an inline `<style>` defining `--cta-band-photo` on `:root` (the 900px version, switching to the 1600px version from `min-width: 901px`). The SCSS uses `background-image: var(--cta-band-photo)` beneath the gradient. Every band, including the raw-HTML ones, gets the photo with no markup change.
- **Homepage band (`build-cta.html`):** eyebrow "Support our work"; title `Help us build technology <span><i>that matters</i></span>.`; primary button "Support our work" with `fa-arrow-right` instead of the 🌍 emoji. Other bands keep their titles and have no eyebrow.
- Existing per-page tweaks keep working: `.project-single__col > .support__cta-band` margins, `.about-closing__funders`. `.support__cta-band.about-closing__band .button:hover` becomes redundant with the new default hover and is removed.

## 2. White card (`.about-cta`)

- **Surface:** `background: var(--white)`, `border: 1px solid var(--light-gray)`, `border-radius: 14px`, `box-shadow: 0 14px 32px -22px rgba(0, 0, 0, 0.3)`. Padding about `32px 36px` (24px 20px on phones). Margins unchanged (`.about-cta`, `.about-cta.demo-cta`, `.post__content .about-cta` keep their current spacing rules).
- **Layout:** left-aligned. Every `.about-cta` is a title, a description, then the actions as its last child (one button, or a wrapper div with two).
  - Screens 1024px and wider: CSS grid `minmax(0, 1fr) auto`, title and description in column 1, the last child in column 2 spanning both rows, vertically centred.
  - Blog posts (780px text column), tablets and phones: stacked, buttons under the description. Project pages share `.post__content` but are wider, so they keep the columns.
  - (Revised during implementation: a container query was tried first, but the size containment it needs on the card's parent stops margins collapsing and doubled the gaps around cards, so a media query is used instead.)
- **Type:** title `$heading-font-family`, about 24px (22px on phones); description 16px, `line-height: 1.6`, `var(--text-alt-color)`, `max-width: 560px`, no auto-centering margins.
- **Buttons inside the card:** `.button`, `.button--middle` and `.button--cta` render as the solid teal button with the offset shadow (so the peach `.button--cta` turns teal here). `.button--ghost` and `.button--secondary` render as the teal outline pill (the `.button--pill` look). The existing button wrappers (`.projects-cta__buttons`, `.tools-cta__buttons`, `.spaces-cta__buttons` and similar) lay out as a wrapping flex row with a 12px gap, left-aligned.

## 3. Copy: no blanket open-source claims

| Where | New copy |
|-------|----------|
| `layouts/partials/build-cta.html` description | "Support our work or partner with us, and help bring conservation technology to the field teams who need it." |
| `layouts/partials/section-tools.html` intro | "Software we build with field teams, from free downloads to hosted services. Explore each one and try it for yourself." |
| `config.toml` `footer_description` | "Developing technology to address conservation and environmental challenges for wildlife and the planet." |
| `data/support.yaml` offer | "Yours to run and keep" (was "Open source, yours to run") |
| `content/support.md` `hero_description` | "Many of our tools are free to use, built for the people protecting wild places. None of them get built without support." |

Claims that are true for their subject stay: the GitHub link description, Pyronear's blurb, Biowatch's own page, and the hedged listing CTAs ("much of the code is open source", "from free, open-source downloads to hosted services").

## Out of scope

- The `support-cta.html` / `donate_sponsor_cta` inline block (a paragraph and a button, not a card).
- Hero, stats card, cards and testimonials.
- Rewriting CTA copy beyond the open-source fixes.

## Verification

- `hugo` builds with no warnings.
- Built HTML/CSS checks: `--cta-band-photo` defined in the page head and the resized WebP files exist in the output; the homepage band has the eyebrow, the accent and no emoji; none of the four blanket claims remain in the built site; `.about-cta` rules carry the new surface.
- Screenshots at 1280, 900 and 375px of: home, About, a project page, AI-BIRD and Biowatch (bands); /projects/, /tools/, /demos/, a demo page, a post with a two-button card, Support, Partners (cards).
