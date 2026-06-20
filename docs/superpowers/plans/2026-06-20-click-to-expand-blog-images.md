# Click-to-expand Blog Images Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Let readers click any standalone content image in a blog post to view it fullscreen, on desktop only, by reusing the carousel lightbox.

**Architecture:** Extract the carousel's per-carousel lightbox into one shared page-level lightbox (`#page-lightbox`) rendered once in the post layout. Generalize the lightbox open logic in `common.js` so both carousels (gallery mode) and standalone images (single mode) feed the same overlay. Standalone-image click handlers are attached only when a desktop media query matches.

**Tech Stack:** Hugo 0.145.0 (templates + shortcodes), SCSS (4-layer architecture), vanilla JS (`assets/js/common.js`), Tiny Slider (carousels). No JS test framework — verification is Hugo build + local serve + browser observation.

## Global Constraints

- **Desktop gate (verbatim):** `(min-width: 768px) and (pointer: fine)` — used for both the JS `matchMedia` guard and the CSS `cursor: zoom-in` affordance.
- **Caption source:** image `alt` text only.
- **Opt-out classes:** `.no-zoom` (new) and `.no-lightense` (existing) both exclude an image from standalone expand.
- **Single shared lightbox id:** `page-lightbox`.
- **Target scope:** `.post__content img` only (post hero image lives outside `.post__content` and stays excluded).
- **No new dependency.** Do not enable Lightense.
- **Commit style:** no Co-Authored-By / generated-by-Claude attribution in commit messages.
- **No JS unit tests exist.** Each task's "test" is a Hugo build plus a specific browser observation. Use `hugo` to build and `hugo server` to serve.

## Verification setup (read once before Task 1)

Build check: `hugo --quiet` (must exit 0, no template errors).
Serve for manual check: `hugo server -D` then open the printed `http://localhost:1313`.

Two reference posts for manual checks:
- **Image-heavy, no carousel:** any post under `content/posts/` with many body `![]()` images (e.g. an early-forest-fire or trout post). Pick one with standalone images in `.post__content`.
- **Carousel post:** `content/posts/how-to-build-a-benthic-coral-reefs-analyser/index.md` (uses `image_carousel`).

To emulate mobile/touch in Chromium: DevTools → toggle device toolbar (Ctrl+Shift+M), pick a phone preset (sets `pointer: coarse` + narrow width).

## File Structure

- **Create** `layouts/partials/image-lightbox.html` — the shared lightbox markup (one fixed id), extracted from the carousel shortcode. Single responsibility: the overlay DOM.
- **Modify** `layouts/_default/single.html` — render the shared lightbox once, inside the post branch.
- **Modify** `layouts/shortcodes/image_carousel.html` — remove its inline lightbox div; keep carousel container only.
- **Modify** `assets/js/common.js` — generalize lightbox open into a reusable function; carousels call it (gallery mode); add desktop-gated standalone-image wiring (single mode).
- **Modify** `assets/sass/3-modules/_image-carousel.scss` — `cursor: zoom-in` under the desktop media query for expandable content images; hide prev/next/counter in single mode via an `is-single` modifier.

---

### Task 1: Extract the shared lightbox partial and render it once per post

**Files:**
- Create: `layouts/partials/image-lightbox.html`
- Modify: `layouts/_default/single.html` (post branch, after the `<!-- end post -->` block, before `related-posts`)
- Modify: `layouts/shortcodes/image_carousel.html` (remove inline lightbox)
- Modify: `assets/js/common.js` (point carousel JS at the shared lightbox id)

**Interfaces:**
- Produces: a single DOM element `#page-lightbox` with class `image-lightbox`, containing `.image-lightbox__overlay`, `.image-lightbox__close`, `.image-lightbox__prev`, `.image-lightbox__next`, `.image-lightbox__content > (.image-lightbox__image, .image-lightbox__caption)`, and `.image-lightbox__counter > (.image-lightbox__current, .image-lightbox__separator, .image-lightbox__total)`. Class/structure are identical to the old per-carousel lightbox so existing CSS in `_image-carousel.scss` applies unchanged.

- [ ] **Step 1: Create the shared lightbox partial**

Create `layouts/partials/image-lightbox.html` with the exact markup the carousel shortcode used, but with the fixed id `page-lightbox` (no per-carousel id):

```html
{{/*
  Shared page-level image lightbox.
  Rendered once per post. Fed by both carousels (gallery mode) and
  standalone content images (single mode) via assets/js/common.js.
*/}}
<div class="image-lightbox" id="page-lightbox" aria-hidden="true" aria-modal="true" role="dialog" aria-label="Image viewer">
  <div class="image-lightbox__overlay"></div>
  <button class="image-lightbox__close" aria-label="Close lightbox">
    <i class="fa-solid fa-xmark"></i>
  </button>
  <button class="image-lightbox__prev" aria-label="Previous image">
    <i class="fa-solid fa-arrow-left-long"></i>
  </button>
  <button class="image-lightbox__next" aria-label="Next image">
    <i class="fa-solid fa-arrow-right-long"></i>
  </button>
  <div class="image-lightbox__content">
    <img class="image-lightbox__image no-lightense" src="" alt="" />
    <p class="image-lightbox__caption"></p>
  </div>
  <div class="image-lightbox__counter">
    <span class="image-lightbox__current">1</span>
    <span class="image-lightbox__separator">/</span>
    <span class="image-lightbox__total">1</span>
  </div>
</div>
```

- [ ] **Step 2: Render the shared lightbox once in the post layout**

In `layouts/_default/single.html`, in the post branch (the `if or (eq .Section "post") (eq .Section "posts")` block), add the partial right after the `<!-- end post -->` comment and before `{{ partial "related-posts.html" . }}`:

```html
<!-- end post -->

{{ partial "image-lightbox.html" . }}

{{ partial "related-posts.html" . }}
```

- [ ] **Step 3: Remove the inline lightbox from the carousel shortcode**

In `layouts/shortcodes/image_carousel.html`, delete the entire block from the `<!-- Fullscreen Lightbox for this carousel -->` comment through its closing `</div>` (the `<div class="image-lightbox" id="{{ $id }}-lightbox" ...> ... </div>`). Leave the `.image-carousel` container and its `</div>` intact. The shortcode now ends after the carousel container.

- [ ] **Step 4: Point the carousel JS at the shared lightbox id**

In `assets/js/common.js`, inside the `.image-carousel` forEach loop, change the lightbox lookup from the per-carousel id to the shared id. Replace:

```javascript
    var lightbox = document.getElementById(id + '-lightbox');
    if (!lightbox) return;
```

with:

```javascript
    var lightbox = document.getElementById('page-lightbox');
    if (!lightbox) return;
```

(Leave the rest of the carousel lightbox logic in this task — it still works because the shared lightbox has the same inner structure. Generalization happens in Task 2.)

- [ ] **Step 5: Build**

Run: `hugo --quiet`
Expected: exits 0, no template errors (no "partial not found", no shortcode error).

- [ ] **Step 6: Manual verify carousel still works**

Run: `hugo server -D`, open the carousel post (`how-to-build-a-benthic-coral-reefs-analyser`).
Expected: clicking a carousel image opens the fullscreen lightbox; prev/next arrows and the "1/N" counter work; Esc and the close button and clicking the backdrop all dismiss. Confirms the extracted shared lightbox is wired correctly.

- [ ] **Step 7: Commit**

```bash
git add layouts/partials/image-lightbox.html layouts/_default/single.html layouts/shortcodes/image_carousel.html assets/js/common.js
git commit -m "refactor(lightbox): extract shared page-level image lightbox"
```

---

### Task 2: Generalize the lightbox open logic into a reusable function

**Files:**
- Modify: `assets/js/common.js`

**Interfaces:**
- Produces: a function `openImageLightbox(images, startIndex, mode)` where:
  - `images` is an array of `{ src, alt, caption }` objects,
  - `startIndex` is a 0-based index into `images`,
  - `mode` is `'gallery'` (arrows + counter, navigation wraps) or `'single'` (no arrows, no counter).
  It targets `#page-lightbox`, sets the image/caption, toggles `is-active` (and `is-single` when `mode === 'single'`) on the lightbox, and adds `lightbox-open` to `document.body`. Esc / overlay / close dismiss; Arrow keys and prev/next navigate only in gallery mode.
- Consumes (refactor): the carousel forEach now builds an `images` array from its slides and calls `openImageLightbox(images, originalIndex, 'gallery')` on image click, instead of its own inline open/close/nav closures.

- [ ] **Step 1: Add the shared open function near the top of the DOM-ready block**

In `assets/js/common.js`, before the `.image-carousel` forEach loop, add a single shared implementation that owns the `#page-lightbox` element and its controls. It must bind its keydown/close/nav handlers exactly once (guard so re-running setup does not double-bind):

```javascript
  /* ============================
  // Shared image lightbox (used by carousels and standalone images)
  ============================ */
  var pageLightbox = document.getElementById('page-lightbox');
  var openImageLightbox = function () {}; // no-op default if no lightbox on page

  if (pageLightbox) {
    var lbImage = pageLightbox.querySelector('.image-lightbox__image');
    var lbCaption = pageLightbox.querySelector('.image-lightbox__caption');
    var lbClose = pageLightbox.querySelector('.image-lightbox__close');
    var lbOverlay = pageLightbox.querySelector('.image-lightbox__overlay');
    var lbPrev = pageLightbox.querySelector('.image-lightbox__prev');
    var lbNext = pageLightbox.querySelector('.image-lightbox__next');
    var lbCurrent = pageLightbox.querySelector('.image-lightbox__current');
    var lbTotal = pageLightbox.querySelector('.image-lightbox__total');

    var lbImages = [];
    var lbIndex = 0;
    var lbMode = 'single';

    function lbRender() {
      var item = lbImages[lbIndex];
      if (!item) return;
      lbImage.src = item.src;
      lbImage.alt = item.alt || '';
      if (lbCaption) lbCaption.textContent = item.caption || '';
      if (lbCurrent) lbCurrent.textContent = lbIndex + 1;
      if (lbTotal) lbTotal.textContent = lbImages.length;
    }

    function lbNextImage() {
      if (lbMode !== 'gallery') return;
      lbIndex = (lbIndex + 1) % lbImages.length;
      lbRender();
    }

    function lbPrevImage() {
      if (lbMode !== 'gallery') return;
      lbIndex = (lbIndex - 1 + lbImages.length) % lbImages.length;
      lbRender();
    }

    function lbCloseFn() {
      pageLightbox.classList.remove('is-active');
      pageLightbox.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('lightbox-open');
    }

    openImageLightbox = function (images, startIndex, mode) {
      lbImages = images || [];
      lbIndex = startIndex || 0;
      lbMode = mode === 'gallery' ? 'gallery' : 'single';
      if (!lbImages.length) return;
      pageLightbox.classList.toggle('is-single', lbMode === 'single');
      lbRender();
      pageLightbox.classList.add('is-active');
      pageLightbox.setAttribute('aria-hidden', 'false');
      document.body.classList.add('lightbox-open');
      if (lbClose) lbClose.focus();
    };

    if (lbClose) lbClose.addEventListener('click', lbCloseFn);
    if (lbOverlay) lbOverlay.addEventListener('click', lbCloseFn);
    if (lbNext) lbNext.addEventListener('click', lbNextImage);
    if (lbPrev) lbPrev.addEventListener('click', lbPrevImage);

    document.addEventListener('keydown', function (e) {
      if (!pageLightbox.classList.contains('is-active')) return;
      if (e.key === 'Escape') { lbCloseFn(); e.preventDefault(); }
      if (e.key === 'ArrowRight') { lbNextImage(); e.preventDefault(); }
      if (e.key === 'ArrowLeft') { lbPrevImage(); e.preventDefault(); }
    });
  }
```

- [ ] **Step 2: Refactor the carousel loop to use the shared function**

In the `.image-carousel` forEach loop, remove the now-duplicated lightbox closures and handlers (the local `var lightbox`, `lightboxImage`, `lightboxCaption`, `lightboxClose`, `lightboxOverlay`, `lightboxPrev`, `lightboxNext`, `lightboxCurrent`, `lightboxTotal`, `openLightbox`, `closeLightbox`, `updateLightboxImage`, `nextImage`, `prevImage`, the per-carousel click handlers wiring close/overlay/next/prev, and the per-carousel keydown listener). Keep the Tiny Slider init and the carousel's own ArrowLeft/ArrowRight slide navigation.

Replace the image-collection + click wiring with: build an `images` array of `{src, alt, caption}` from the original (non-clone) slides, and on click of any slide image (including clones) open the shared lightbox in gallery mode at the matching index:

```javascript
    // Build the gallery image list from original (non-clone) slides
    var originalImages = Array.from(
      carouselContainer.querySelectorAll('.image-carousel__slide:not(.tns-slide-cloned) img')
    );
    var galleryItems = originalImages.map(function (img) {
      return { src: img.src, alt: img.alt, caption: img.dataset.caption || '' };
    });

    // Click ANY slide image (including clones) -> open shared lightbox at matching index
    var allSlideImages = Array.from(carouselContainer.querySelectorAll('.image-carousel__slide img'));
    allSlideImages.forEach(function (img) {
      img.addEventListener('click', function () {
        var idx = originalImages.findIndex(function (o) { return o.src === img.src; });
        if (idx !== -1) openImageLightbox(galleryItems, idx, 'gallery');
      });
    });
```

- [ ] **Step 3: Build**

Run: `hugo --quiet`
Expected: exits 0, no errors.

- [ ] **Step 4: Manual verify carousel parity**

Run: `hugo server -D`, open the carousel post.
Expected: identical behavior to Task 1 — open on click, arrows + "1/N" counter navigate (wrapping), captions show, Esc/close/backdrop dismiss. No JS console errors.

- [ ] **Step 5: Commit**

```bash
git add assets/js/common.js
git commit -m "refactor(lightbox): generalize open into shared gallery/single function"
```

---

### Task 3: Wire standalone content images with a desktop gate

**Files:**
- Modify: `assets/js/common.js`

**Interfaces:**
- Consumes: `openImageLightbox(images, startIndex, mode)` from Task 2.
- Produces: desktop-only click handlers on standalone `.post__content img` (excluding carousel images, `.no-zoom`, `.no-lightense`, and images inside an `<a>`), each opening the shared lightbox in single mode with `{src, alt, caption: alt}`.

- [ ] **Step 1: Add the standalone-image wiring after the carousel loop**

In `assets/js/common.js`, after the `.image-carousel` forEach loop, add the desktop-gated wiring. The media query string must match the Global Constraint verbatim:

```javascript
  /* ============================
  // Standalone content images: click-to-expand (desktop only)
  ============================ */
  (function () {
    if (!pageLightbox) return;
    var desktop = window.matchMedia('(min-width: 768px) and (pointer: fine)');
    if (!desktop.matches) return; // mobile / touch: no handlers, no zoom cursor

    var content = document.querySelector('.post__content');
    if (!content) return;

    var candidates = Array.from(content.querySelectorAll('img'));
    candidates.forEach(function (img) {
      if (img.closest('.image-carousel')) return;      // carousels handle their own
      if (img.classList.contains('no-zoom')) return;   // explicit opt-out
      if (img.classList.contains('no-lightense')) return; // existing opt-out convention
      if (img.closest('a')) return;                    // linked image: let the link win

      img.classList.add('is-zoomable');
      img.addEventListener('click', function () {
        openImageLightbox([{ src: img.src, alt: img.alt, caption: img.alt }], 0, 'single');
      });
    });
  })();
```

- [ ] **Step 2: Build**

Run: `hugo --quiet`
Expected: exits 0, no errors.

- [ ] **Step 3: Manual verify standalone expand on desktop**

Run: `hugo server -D`, open the image-heavy (non-carousel) post in a normal desktop window.
Expected: clicking a body image opens it fullscreen with NO prev/next arrows and NO counter; the `alt` text shows as the caption; Esc, the close button, and clicking the backdrop all dismiss. An SVG diagram image also expands and scales cleanly.

- [ ] **Step 4: Manual verify mobile/touch is inert**

In the same post, open Chromium DevTools device toolbar (Ctrl+Shift+M), select a phone preset, reload.
Expected: clicking a body image does nothing (no overlay opens). (Carousels keep their own behavior — not in scope here.)

- [ ] **Step 5: Commit**

```bash
git add assets/js/common.js
git commit -m "feat(lightbox): desktop click-to-expand for standalone post images"
```

---

### Task 4: CSS affordance and single-mode hiding

**Files:**
- Modify: `assets/sass/3-modules/_image-carousel.scss`

**Interfaces:**
- Consumes: the `is-zoomable` class added to expandable images (Task 3) and the `is-single` modifier on `#page-lightbox` (Task 2).
- Produces: a `zoom-in` cursor on expandable images under the desktop media query, and hidden prev/next/counter when the lightbox is in single mode.

- [ ] **Step 1: Add the zoom-in cursor under the desktop media query**

In `assets/sass/3-modules/_image-carousel.scss`, append (media query string matches the Global Constraint verbatim):

```scss
/* Standalone content images that are click-to-expand (desktop only) */
@media (min-width: 768px) and (pointer: fine) {
  .post__content img.is-zoomable {
    cursor: zoom-in;
  }
}
```

- [ ] **Step 2: Hide prev/next/counter in single mode**

In the same file, append a rule so the shared lightbox hides gallery-only chrome when showing a single image:

```scss
/* Single-image mode hides gallery navigation chrome */
.image-lightbox.is-single {
  .image-lightbox__prev,
  .image-lightbox__next,
  .image-lightbox__counter {
    display: none;
  }
}
```

- [ ] **Step 3: Build**

Run: `hugo --quiet`
Expected: exits 0, SCSS compiles with no errors.

- [ ] **Step 4: Manual verify cursor and single-mode chrome**

Run: `hugo server -D`.
Expected:
- On the non-carousel post (desktop window): hovering a body image shows a `zoom-in` (magnifier) cursor; opening it shows no arrows and no counter.
- On the carousel post: the gallery lightbox still shows arrows and the "1/N" counter (not hidden), confirming `is-single` is correctly scoped.

- [ ] **Step 5: Commit**

```bash
git add assets/sass/3-modules/_image-carousel.scss
git commit -m "style(lightbox): zoom-in cursor and single-mode chrome hiding"
```

---

### Task 5: Author opt-out documentation

**Files:**
- Modify: the project's shortcode/authoring doc. Locate it first: check `docs/` and the carousel shortcode's own header comment. If a spec/usage doc for media exists (e.g. under `docs/specs/` or a `docs/` authoring guide), add a short note there. Otherwise add the note to the top-of-file comment in `layouts/shortcodes/image_carousel.html` is NOT appropriate (that's carousel-specific) — instead create `docs/authoring-images.md`.

**Interfaces:**
- Produces: a one-paragraph author-facing note on the desktop click-to-expand behavior and the `.no-zoom` opt-out.

- [ ] **Step 1: Find the right home for the note**

Run: `ls docs && ls docs/specs 2>/dev/null | tail` and skim for an existing authoring/usage guide.
Decision rule: if an existing general authoring/media doc exists, add to it; otherwise create `docs/authoring-images.md`.

- [ ] **Step 2: Write the note**

Add (in the chosen file) the following content:

```markdown
## Click-to-expand images

On desktop (pointer + viewport ≥ 768px), readers can click any image in a post
body to view it fullscreen. This is automatic — no shortcode needed. The
overlay caption uses the image's alt text.

To exclude a specific image (e.g. a small icon or decorative graphic), add the
`no-zoom` class to it. Images inside a link, and the post hero image, are never
expandable. Carousels keep their own built-in fullscreen gallery.
```

If creating a new file, prefix it with a top-level `# Authoring images` heading.

- [ ] **Step 3: Commit**

```bash
git add docs/
git commit -m "docs: document desktop click-to-expand and no-zoom opt-out"
```

---

## Self-Review

**Spec coverage:**
- All standalone content images, automatic → Task 3 (`.post__content img` wiring). ✓
- Reuse carousel lightbox via shared extraction → Tasks 1–2. ✓
- Desktop gate `(min-width: 768px) and (pointer: fine)` → Task 3 (JS) + Task 4 (CSS), verbatim. ✓
- Caption = alt text → Task 3 (`caption: img.alt`). ✓
- Opt-out `.no-zoom` (+ existing `.no-lightense`) → Task 3. ✓
- Carousels re-point to shared lightbox, behavior preserved → Tasks 1–2 with parity checks. ✓
- Edge cases: SVG (Task 3 check), lazy-load resolved src (uses `img.src`), hero excluded (scoped to `.post__content`), linked images skipped (Task 3 `img.closest('a')`). ✓
- Author opt-out documentation → Task 5. ✓

**Placeholder scan:** No TBD/TODO; each code step shows full code; each verify step states an exact observable expectation. Task 5 Step 1 is a genuine locate-then-decide step with an explicit decision rule, not a placeholder.

**Type consistency:** `openImageLightbox(images, startIndex, mode)` is defined in Task 2 and consumed identically in Tasks 2 and 3. `is-active`, `is-single`, `is-zoomable`, `lightbox-open`, `page-lightbox` are used consistently across JS (Tasks 2–3) and SCSS (Task 4). Image item shape `{src, alt, caption}` is consistent between carousel (Task 2) and standalone (Task 3) callers.
