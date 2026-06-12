"""Generate the custom figures for the 'Smoke Is a Behavior' blog post.

Usage:
    uv run --with matplotlib --with pillow --with numpy python make_figures.py

The photographic figures are reused from the pyronear/temporal-model docs
(docs/assets/, regenerable with the scripts there). This script generates:
  - pipeline.png      six-stage pipeline overview
  - classifier.png    ViT backbone + transformer head architecture
  - cover.png         10:7 text-free cover tiled from real stabilized patches
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from PIL import Image

HERE = Path(__file__).resolve().parent
SITE = HERE.parent.parent.parent
BUNDLE = SITE / "content" / "posts" / "smoke-is-a-behavior" / "images"
COVER_DIR = SITE / "assets" / "images" / "posts" / "smoke-is-a-behavior"

INK = "#1e293b"
MUTED = "#64748b"
FAINT = "#cbd5e1"
ORANGE = "#ea580c"
AMBER = "#f59e0b"
GREEN = "#15803d"
BLUE = "#2563eb"
PAPER = "#ffffff"

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "text.color": INK,
        "figure.facecolor": PAPER,
        "savefig.facecolor": PAPER,
        "savefig.dpi": 200,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.25,
    }
)


def rounded_box(ax, xy, w, h, fc, ec, lw=1.4, radius=1.8):
    box = FancyBboxPatch(
        xy, w, h, boxstyle=f"round,pad=0,rounding_size={radius}", fc=fc, ec=ec, lw=lw, mutation_aspect=1
    )
    ax.add_patch(box)
    return box


def arrow(ax, p0, p1, color=MUTED, lw=2.2):
    ax.add_patch(
        FancyArrowPatch(p0, p1, arrowstyle="-|>", color=color, lw=lw, mutation_scale=16, shrinkA=3, shrinkB=3)
    )


def bare_axes(fig_w, fig_h, xlim=(0, 100), ylim=(0, 100)):
    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    return fig, ax


# -------------------------------------------------------- pipeline overview
def make_pipeline(path):
    stages = [
        ("1 · Sequence", "up to 20 frames,\n~30 s apart", FAINT, INK),
        ("2 · Detect", "a detector proposes\nboxes on every frame", FAINT, INK),
        ("3 · Link", "boxes chained into\ntubes across frames", FAINT, INK),
        ("4 · Crop", "one stabilized window\nper tube, 224×224", ORANGE, "white"),
        ("5 · Score", "image model per patch +\ntransformer over time", FAINT, INK),
        ("6 · Decide", "calibrated probability\nvs threshold", FAINT, INK),
    ]
    fig, ax = bare_axes(13.6, 3.4)
    bw, bh, by = 14.6, 62, 19
    x0, gap = 1.2, 2.0
    for i, (title, sub, ec, _tc) in enumerate(stages):
        x = x0 + i * (bw + gap)
        highlight = ec == ORANGE
        rounded_box(
            ax,
            (x, by),
            bw,
            bh,
            fc="#fff7ed" if highlight else PAPER,
            ec=ORANGE if highlight else FAINT,
            lw=2.0 if highlight else 1.5,
        )
        ax.text(
            x + bw / 2,
            by + bh - 14,
            title,
            ha="center",
            fontsize=12,
            fontweight="bold",
            color=ORANGE if highlight else INK,
        )
        ax.text(x + bw / 2, by + 18, sub, ha="center", va="center", fontsize=9.3, color=MUTED, linespacing=1.4)
        if i:
            arrow(ax, (x - gap - 0.4, by + bh / 2), (x + 0.4, by + bh / 2))
    ax.text(
        x0 + 3 * (bw + gap) + bw / 2,
        by - 11,
        "the trick that makes the temporal signal legible",
        ha="center",
        fontsize=9,
        color=ORANGE,
        fontstyle="italic",
    )
    fig.savefig(path)
    plt.close(fig)


# --------------------------------------------------- classifier architecture
def make_classifier(path):
    fig, ax = bare_axes(8.6, 9.2)

    def stage(y, h, label, sub, fc, ec, tc=INK, w=56, x=22):
        rounded_box(ax, (x, y), w, h, fc=fc, ec=ec, lw=1.6)
        if sub:
            ax.text(x + w / 2, y + h - 4.5, label, ha="center", va="center",
                    fontsize=11.5, fontweight="bold", color=tc)
            ax.text(x + w / 2, y + 5, sub, ha="center", va="center",
                    fontsize=9.2, color=MUTED, linespacing=1.45)
        else:
            ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
                    fontsize=11.5, fontweight="bold", color=tc)

    # patches at the top: small stacked squares
    for dx in (4.4, 2.2, 0):
        rounded_box(ax, (38 + dx, 88 - dx * 0.9), 14, 9.5, fc="#f1f5f9", ec=FAINT, lw=1.2, radius=1.0)
    ax.text(66, 88.5, "one tube =\n20 patches\n3×224×224", fontsize=9.2, color=MUTED, va="center", linespacing=1.4)

    arrow(ax, (50, 84.5), (50, 80.5))
    stage(65, 15, "DINOv2 ViT-S/14 backbone", "applied to each patch independently\n(frozen except its last block)", PAPER, BLUE)
    arrow(ax, (50, 64.5), (50, 60.5))
    stage(52, 8, "20 embeddings · 384-dim each", "", "#f1f5f9", FAINT)
    arrow(ax, (50, 51.5), (50, 47.5))
    stage(32, 15, "Temporal transformer · 2 layers", "a learned summary token attends over time,\npadded frames masked out of attention", "#fff7ed", ORANGE, ORANGE)
    arrow(ax, (50, 31.5), (50, 27.5))
    stage(19, 8, "one logit per tube", "", "#f1f5f9", FAINT)
    arrow(ax, (50, 18.5), (50, 13.5))
    stage(5, 8, "calibrated probability", "", GREEN, GREEN, tc="white")

    ax.text(11, 72.5, "what is in\neach patch?", fontsize=9.5, color=BLUE, ha="center", fontstyle="italic", linespacing=1.4)
    ax.text(11, 39.5, "how does it\nevolve in time?", fontsize=9.5, color=ORANGE, ha="center", fontstyle="italic", linespacing=1.4)

    fig.savefig(path)
    plt.close(fig)


# ------------------------------------------------------------------- cover
def find_patches(img):
    """Split a horizontal strip of patches on its near-white gutter columns."""
    arr = np.asarray(img.convert("L"))
    is_gap = arr.min(axis=0) > 235
    bounds, start = [], None
    for x, gap in enumerate(is_gap):
        if not gap and start is None:
            start = x
        elif gap and start is not None:
            bounds.append((start, x))
            start = None
    if start is not None:
        bounds.append((start, len(is_gap)))
    return [b for b in bounds if b[1] - b[0] > 50]


def trim_bars(patch):
    """Trim the letterbox bars and the t-label overlay framing a patch."""
    arr = np.asarray(patch.convert("L"))
    is_bar = (arr < 40).mean(axis=1) > 0.6
    rows = np.where(~is_bar)[0]
    patch = patch.crop((0, rows[0], patch.width, rows[-1] + 1))
    # the "t = N" label overlay sits in the top-left corner: drop the top band,
    # then center-crop to a square
    patch = patch.crop((0, int(patch.height * 0.12), patch.width, patch.height))
    side = min(patch.size)
    cx, cy = patch.width // 2, patch.height // 2
    return patch.crop((cx - side // 2, cy - side // 2, cx - side // 2 + side, cy - side // 2 + side))


def make_cover(path, strip_path):
    strip = Image.open(strip_path)
    bounds = find_patches(strip)
    # 6 chronological patches in a 3x2 grid (10:7 canvas, generous margins)
    idx = np.linspace(0, len(bounds) - 1, 6).round().astype(int)
    W, H = 2000, 1400
    cols, rows, g = 3, 2, 24
    tile = (W - 2 * 140 - (cols - 1) * g) // cols
    x0 = (W - cols * tile - (cols - 1) * g) // 2
    y0 = (H - rows * tile - (rows - 1) * g) // 2
    canvas = Image.new("RGB", (W, H), "white")
    for k, i in enumerate(idx):
        left, right = bounds[i]
        patch = trim_bars(strip.crop((left, 0, right, strip.height))).resize((tile, tile), Image.LANCZOS)
        r, c = divmod(k, cols)
        canvas.paste(patch, (x0 + c * (tile + g), y0 + r * (tile + g)))
    canvas.save(path)


if __name__ == "__main__":
    BUNDLE.mkdir(parents=True, exist_ok=True)
    COVER_DIR.mkdir(parents=True, exist_ok=True)
    make_pipeline(BUNDLE / "pipeline.png")
    make_classifier(BUNDLE / "classifier.png")
    make_cover(COVER_DIR / "cover.png", BUNDLE / "brison_patches.jpg")
    print("done")
