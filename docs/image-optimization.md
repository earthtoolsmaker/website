# Image Optimization Guide

This document explains how image optimization works on the EarthToolsMaker website.

## Overview

The site uses Hugo's built-in image processing to automatically generate:
- **Responsive images** (multiple sizes for different screen widths)
- **WebP format** (modern, smaller file format with fallback)
- **LQIP** (Low Quality Image Placeholder) for blur-up effect

## How It Works

### 1. Image Location

**All images live in `/assets/images/`** - this is the single source of truth.

```
assets/
  images/
    clients/           # Partner logos
    logos/             # Site logos
    pages/             # Page-specific images
    posts/             # Blog post images
    projects/          # Project images
    social/            # Social media icons
    spaces/            # Space images
    subscribe/         # Subscribe section
    team/              # Team photos
    testimonials/      # Testimonial avatars
```

Hugo serves all images at the `/images/` URL path. Images used with the `responsive-image.html` partial get processed (WebP, multiple sizes, LQIP), while others are served as-is.

### 2. The Responsive Image Partial

The core of the system is `layouts/partials/responsive-image.html`. It:

1. Takes an image path from `/assets/`
2. Generates multiple sizes (400w, 600w, 800w by default)
3. Creates WebP versions for modern browsers
4. Creates a tiny 20px LQIP placeholder
5. Outputs a `<picture>` element with proper srcset

### 3. Generated Output

For a single source image, Hugo generates:

```
Original: cover.jpg (7.1MB)
    ↓
Generated:
  - cover_..._400x0_resize_q80_h2_lanczos.webp  (7KB)   # WebP 400w
  - cover_..._600x0_resize_q80_h2_lanczos.webp  (15KB)  # WebP 600w
  - cover_..._800x0_resize_q80_h2_lanczos.webp  (23KB)  # WebP 800w
  - cover_..._400x0_resize_q85_lanczos.jpg     (13KB)  # Fallback 400w
  - cover_..._600x0_resize_q85_lanczos.jpg     (27KB)  # Fallback 600w
  - cover_..._800x0_resize_q85_lanczos.jpg     (45KB)  # Fallback 800w
  - cover_..._20x0_resize_q20_h2_lanczos.webp  (86B)   # LQIP placeholder
```

### 4. HTML Output

The partial generates:

```html
<picture>
  <source
    type="image/webp"
    data-srcset="cover_400w.webp 400w, cover_600w.webp 600w, cover_800w.webp 800w"
    sizes="(max-width: 600px) 100vw, (max-width: 900px) 50vw, 400px">
  <source
    data-srcset="cover_400w.jpg 400w, cover_600w.jpg 600w, cover_800w.jpg 800w"
    sizes="...">
  <img
    class="lazy"
    src="cover_20px_lqip.webp"    <!-- Tiny placeholder shown immediately -->
    data-src="cover_600w.jpg"     <!-- Fallback for lazy load -->
    width="600"
    height="400"
    loading="lazy"
    decoding="async">
</picture>
```

### 5. Browser Behavior

1. **Initial load**: Browser shows the tiny LQIP (blurred)
2. **Lazy load triggers**: When image enters viewport, LazyLoad.js activates
3. **Format selection**: Browser picks WebP if supported, otherwise JPG/PNG
4. **Size selection**: Browser picks appropriate size based on viewport width
5. **Blur transition**: CSS transitions from blurred LQIP to sharp image

## Adding New Optimized Images

### For Project/Post Cover Images

1. **Add the source image** to `/assets/images/`:
   ```
   assets/images/projects/my-new-project/cover.jpg
   ```

2. **Reference it in front matter** (same path as before):
   ```yaml
   image: /images/projects/my-new-project/cover.jpg
   ```

3. **Build the site** - Hugo automatically generates all variants:
   ```bash
   hugo
   ```

### Using the Partial Directly

In any template:

```html
{{ partial "responsive-image.html" (dict
  "src" "images/projects/myproject/cover.jpg"
  "alt" "Project description"
  "sizes" "(max-width: 600px) 100vw, 400px"
  "widths" (slice 400 600 800)
  "lazy" true
  "lqip" true
) }}
```

#### Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `src` | required | Path relative to `/assets/` |
| `alt` | `""` | Alt text for accessibility |
| `class` | `""` | Additional CSS classes |
| `sizes` | `"(max-width: 600px) 100vw, (max-width: 900px) 50vw, 400px"` | Responsive sizes hint |
| `widths` | `[400, 600, 800]` | Widths to generate |
| `lazy` | `true` | Enable lazy loading |
| `lqip` | `true` | Enable blur-up placeholder |

## Where Optimization is Applied

Currently optimized:
- **Project cards** on homepage (`section-projects.html`)
- **Blog/post cards** on homepage (`article.html`)

Not optimized (using simple `<img>` tags):
- Partner logos
- Testimonial avatars
- Images inside post/project content

## File Structure

```
layouts/
  partials/
    responsive-image.html    # Core image processing partial

assets/
  images/                    # ALL images (single source of truth)
    clients/                 # Partner logos
    logos/                   # Site logos
    pages/                   # Page-specific images
    posts/                   # Blog post images
    projects/                # Project images
    social/                  # Social media icons
    spaces/                  # Space images
    subscribe/               # Subscribe section
    team/                    # Team photos
    testimonials/            # Testimonial avatars
  sass/
    3-modules/
      _lazy-images.scss      # LQIP blur CSS + grayscale effects

resources/
  _gen/
    images/                  # CACHE of generated images (auto-created)
```

## Configuration

Hugo imaging settings in `config.toml`:

```toml
[imaging]
  quality = 80              # WebP/JPEG quality (0-100)
  resampleFilter = "Lanczos" # High-quality resampling

  [imaging.exif]
    disableDate = true      # Strip EXIF date
    disableLatLong = true   # Strip GPS data
```

## Performance Results

| Metric | Before | After |
|--------|--------|-------|
| Largest image | 7.1MB | 23KB (WebP 800w) |
| Typical cover | 1-3MB | 50-150KB |
| Mobile load | 7.1MB | 7KB (WebP 400w) |
| LQIP placeholder | - | 86 bytes |

## Troubleshooting

### Image not being processed

1. Check the image is in `/assets/images/`
2. Verify the path in the partial matches the file location
3. Run `hugo --gc` to clear cache and regenerate

### Image not found

If an image path is incorrect, check:
- The file exists in `/assets/images/`
- The path in front matter matches (e.g., `image: /images/projects/foo/cover.jpg`)
- Check browser's Network tab for 404 errors

### Build errors

```bash
# Clear Hugo's cache and rebuild
hugo --gc --minify
```

## Development Setup

### Install Git Hooks

To automatically optimize large images before each commit, install the pre-commit hook:

```bash
./scripts/install-hooks.sh
```

This installs a pre-commit hook that:
- Runs `scripts/optimize-images.sh` when committing images in `content/posts/`
- Resizes images larger than 1200px wide
- Creates WebP versions for better compression
- Automatically stages the optimized files

### Requirements

The optimization scripts require:
- **ImageMagick** - for image resizing
  ```bash
  # Ubuntu/Debian
  sudo apt install imagemagick

  # macOS
  brew install imagemagick
  ```
- **WebP tools** - for WebP conversion
  ```bash
  # Ubuntu/Debian
  sudo apt install webp

  # macOS
  brew install webp
  ```

### Manual Optimization

To optimize images manually (e.g., before a large batch commit):

```bash
# Dry run - see what would be optimized
./scripts/optimize-images.sh --dry-run

# Actually optimize
./scripts/optimize-images.sh
```

## CSS Effects

The grayscale hover effect on project/article cards is preserved by combining filters in `_lazy-images.scss`:

```scss
.project__image .lazy,
.article__image .lazy {
  @media (min-width: 769px) {
    filter: blur(10px) grayscale(50%);  // Loading: blurred + grayscale

    &.loaded {
      filter: grayscale(50%);            // Loaded: grayscale only
    }
  }
}

// On hover: full color
.project__content:hover .project__image .lazy.loaded {
  filter: grayscale(0%);
}
```
