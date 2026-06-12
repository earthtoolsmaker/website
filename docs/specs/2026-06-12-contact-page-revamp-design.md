# Contact Page Revamp — Design

**Date:** 2026-06-12
**Status:** Approved

## Goal

Improve the contact page (`/contact/`) in two ways:

1. Rework the page layout and form visual design.
2. Replace the hero image with the homepage hero illustration.

## Current state

- `content/contact.md` renders via `layouts/_default/contact.html`: hero image,
  page title, then the markdown content which embeds the form through the
  `contact_form` shortcode.
- The form (`layouts/shortcodes/contact_form.html`) is a bare Formspree form:
  Name, Email, Message with placeholder-only labels (visible labels are
  screen-reader-only), no card treatment, and a stray trailing `</div>`.
- The shortcode is also used by `content/sponsor.md`.
- The hero is `assets/images/pages/contact/hero.jpg`, a cartoon desert-canyon
  illustration that clashes with the site's teal/green branding.
- The site publishes no email address; Formspree is the only mail channel.

## Decisions

- **Layout:** two-column ("option B"): left column = intro text + direct
  channels (GitHub, HuggingFace); right column = the form in an elevated card.
  Columns stack on mobile, info first.
- **Channels:** social links only, built from `params.social`. No public email
  address (avoids scraping/spam; the form is the email channel).
- **Hero:** reuse the homepage hero `/images/pages/home/hero.jpg` via front
  matter. No file copies.
- **Structure:** the layout owns the page structure; a partial owns the form
  markup. The shortcode stays as a thin wrapper so `sponsor.md` keeps working.

## Changes

### 1. Form partial — `layouts/partials/contact-form.html` (new)

Move the form markup out of the shortcode. Same three fields and Formspree
action (`params.contact.contact_email` form id), improved presentation:

- Visible `<label>` above each input (drop the `screen-reader-text` class —
  labels are no longer hidden).
- Keep `required` attributes and the `_replyto` field name.
- Remove the stray trailing `</div>`.

`layouts/shortcodes/contact_form.html` becomes a one-liner that calls the
partial, so the sponsor page automatically gets the improved fields (but not
the contact page's two-column layout or card).

### 2. Contact layout — `layouts/_default/contact.html`

After the hero and page title, render a `contact-grid`:

- **Left column:** the page's `.Content` (intro paragraph) followed by
  `contact-channels` rows — one per `params.social` entry, showing the icon
  (`icon` class or `image` resource, same handling as
  `partials/social-links.html`) plus the channel name, linked.
- **Right column:** the contact-form partial wrapped in a `.form-card`.

`content/contact.md` drops the `{{< contact_form >}}` shortcode (the layout
places the form) and changes its front matter image to
`/images/pages/home/hero.jpg`.

### 3. Styling — `assets/sass/3-modules/_contact.scss`

Append new rules, using existing CSS custom properties only:

- `.contact-grid`: CSS grid, `1fr 1.2fr` columns, generous gap; single column
  below the tablet breakpoint (info first).
- `.contact-channels`: vertical list of icon + name rows.
- `.form-card`: white card with border, soft shadow, 12px radius (matches site
  card treatment).
- `.form__label`: visible label styling (small, semibold).
- `.form__input` refinements: defined border, focus ring in
  `--primary-color`; keep existing background/radius conventions.

## Out of scope

- New form fields (subject/topic, organization).
- Client-side validation or custom success state (Formspree default behavior
  unchanged).
- Any change to the sponsor page beyond inheriting the improved form fields.

## Verification

- `hugo` builds with no errors.
- Visual check of `/contact/` and `/sponsor/` with `hugo -D server`: two-column
  on desktop, stacked on mobile; sponsor form still renders correctly without
  the stray `</div>`.
