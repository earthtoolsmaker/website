# Rename "Spaces" → "Live Demos"

**Date:** 2026-06-15
**Status:** Approved

## Problem

The interactive ML model demos live in a section labelled **Spaces** (`/spaces/`).
The name was inherited from HuggingFace Spaces and is opaque to non-technical
visitors — it doesn't convey that these are runnable, interactive demos of our
conservation models.

## Goal

Rename the section to **Live Demos** with a clearer URL `/demos/`, without
breaking inbound links or touching the real HuggingFace integration.

"Live" signals the demos are interactive/runnable rather than a video or
screenshot, and reads instantly for a non-technical audience.

## Scope

Three categories of "spaces" references exist; they are treated differently.

### 1. User-facing label & title (change)

- `config.toml`: both menu entries `name = "Spaces"` → `"Live Demos"` (the main
  nav entry ~line 58 and the footer entry ~line 95). URLs in these entries
  become `/demos/` (see §2).
- `content/spaces/_index.md` (moves to `content/demos/_index.md`):
  `title: Spaces` → `title: Live Demos`. The existing `description` already
  reads clearly and is left unchanged.
- Body copy: the "*try out the model from the [ML Space]*" link text in posts
  and projects (~7 occurrences) → "*[live demo]*", so user-facing terminology
  matches the new name.

### 2. URL `/spaces/` → `/demos/` (full directory rename)

A full directory rename is chosen over a permalink/`url`-only override because
the `space:` front-matter field is consumed two different ways — as a raw
`href` (`layouts/partials/sidebar-widgets/widget-project-meta.html`) and as a
content-path lookup via `site.GetPage`
(`layouts/partials/sidebar-widgets/widget-recent-projects-and-related-posts.html`).
A partial rename (output URL changed but `content/spaces/` kept) would make
those two consumers disagree. After a full rename, content path = output URL =
`/demos/`, so every consumer stays consistent.

Changes:

- `git mv content/spaces content/demos`
- `git mv layouts/spaces layouts/demos`
- Update the 3 Hugo section queries `where … "Section" "spaces"` → `"demos"`:
  `layouts/demos/list.html` (×2) and `layouts/page/partners.html`.
- Update internal `{{< ref "/spaces/…" >}}` links (~16, across posts and
  projects) → `{{< ref "/demos/…" >}}`.
- Update the 9 `space:` front-matter paths in `content/projects/*`
  (`/spaces/<slug>/` → `/demos/<slug>/`).

### 3. Redirect (no broken inbound links)

- Add a 301 redirect to `netlify.toml`: `/spaces/*` → `/demos/:splat`.

## Explicitly NOT touched

- **External HuggingFace URLs** — `hf_space_code` values and the `hf_space`
  shortcode `src` (`https://huggingface.co/spaces/…`, `https://….hf.space`).
  These are real HF links, unrelated to our section name.
- **Asset paths** `/images/pages/spaces/<slug>/…` — internal file paths,
  invisible to visitors. Renaming is pure churn.
- **Internal names** — CSS classes (`spaces-cta`, `spaces-stats`), partial and
  shortcode filenames (`spaces-cta.html`, `space-image.html`, `space_card.html`,
  `space_partners.html`), and the `space:` / `hf_space` front-matter field
  *keys*. Invisible to visitors. They keep saying "spaces" internally; a
  cosmetic follow-up can unify them later if desired.

## Verification

- `hugo` builds with no errors or warnings.
- `/demos/` renders (list page, title "Live Demos") and a sample detail page
  `/demos/bear_identification/` renders.
- `/spaces/` and `/spaces/bear_identification/` redirect (301) to the `/demos/`
  equivalents.
- `grep` confirms no internal `]({{< ref "/spaces/` refs and no raw `/spaces/`
  hrefs remain in `content/` or `layouts/` (external `huggingface.co/spaces/`
  and `/images/pages/spaces/` paths are expected to remain).
- Nav and footer show "Live Demos" pointing at `/demos/`.
