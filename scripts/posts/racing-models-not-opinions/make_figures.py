"""Generate all figures for the 'Racing Models, Not Opinions' blog post.

Usage:
    uv run --with matplotlib python make_figures.py

Outputs PNGs into the post's page bundle (content/posts/racing-models-not-opinions/images/)
and the cover into assets/images/posts/racing-models-not-opinions/.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon

HERE = Path(__file__).resolve().parent
SITE = HERE.parent.parent.parent
BUNDLE = SITE / "content" / "posts" / "racing-models-not-opinions" / "images"
COVER_DIR = SITE / "assets" / "images" / "posts" / "racing-models-not-opinions"

INK = "#1e293b"
MUTED = "#64748b"
FAINT = "#cbd5e1"
ORANGE = "#ea580c"
AMBER = "#f59e0b"
GREEN = "#15803d"
BLUE = "#2563eb"
PAPER = "#ffffff"
CARD = "#f8fafc"

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "text.color": INK,
        "axes.edgecolor": FAINT,
        "figure.facecolor": PAPER,
        "savefig.facecolor": PAPER,
        "savefig.dpi": 200,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.25,
    }
)


def rounded_box(ax, xy, w, h, fc, ec, lw=1.4, radius=0.12, ls="-", alpha=1.0):
    box = FancyBboxPatch(
        xy,
        w,
        h,
        boxstyle=f"round,pad=0,rounding_size={radius}",
        fc=fc,
        ec=ec,
        lw=lw,
        ls=ls,
        alpha=alpha,
        mutation_aspect=1,
    )
    ax.add_patch(box)
    return box


def arrow(ax, p0, p1, color=MUTED, lw=2.2, style="-|>", shrink=4, connectionstyle="arc3,rad=0"):
    a = FancyArrowPatch(
        p0,
        p1,
        arrowstyle=style,
        color=color,
        lw=lw,
        mutation_scale=18,
        shrinkA=shrink,
        shrinkB=shrink,
        connectionstyle=connectionstyle,
    )
    ax.add_patch(a)
    return a


def bare_axes(fig_w, fig_h, xlim, ylim):
    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    ax.set_aspect("auto")
    return fig, ax


# ------------------------------------------------------- cover: vertical funnel
# The site shows covers in a 10:7 box with object-fit: cover (post header and
# blog cards both use padding-top: 70%), and cards overlay dark gradients at
# the top and bottom — so the cover is text-free with generous safe margins.
def make_cover(path):
    stages = [
        ("28", "papers surveyed", "#fde68a", INK),
        ("7", "approaches shortlisted", "#fcd34d", INK),
        ("5", "models built & raced", "#fbbf24", INK),
        ("1", "winner promoted", "#f59e0b", "white"),
        ("v0.1.0", "packaged & released", ORANGE, "white"),
    ]
    fig, ax = bare_axes(10, 7, (0, 100), (0, 100))

    n = len(stages)
    band_h, gap = 12.4, 3.0
    total = n * band_h + (n - 1) * gap
    y_top = 50 + total / 2
    widths = [88, 71, 54, 37, 26]
    for i, (num, label, color, tc) in enumerate(stages):
        w_t = widths[i]
        w_b = widths[i + 1] if i + 1 < n else widths[i] - 6
        yt = y_top - i * (band_h + gap)
        yb = yt - band_h
        pts = [(50 - w_t / 2, yt), (50 + w_t / 2, yt), (50 + w_b / 2, yb), (50 - w_b / 2, yb)]
        ax.add_patch(Polygon(pts, closed=True, fc=color, ec="white", lw=2.0, zorder=2))
        cy = (yt + yb) / 2
        num_size = 23 if len(num) <= 2 else 16
        ax.text(50, cy + 2.2, num, ha="center", va="center", fontsize=num_size, fontweight="bold", color=tc, zorder=3)
        ax.text(50, cy - 3.6, label, ha="center", va="center", fontsize=10 - i * 0.4, color=tc, zorder=3)

    fig.savefig(path, pad_inches=0)
    plt.close(fig)


# ---------------------------------------------------------------- figure 1: funnel
def make_funnel(path, cover=False):
    stages = [
        ("28", "papers\nsurveyed", "Literature survey", "#fde68a"),
        ("7", "approaches\nshortlisted", "Ranked by promise,\neffort and compute", "#fcd34d"),
        ("5", "models\nbuilt & raced", "Self-contained\nexperiments", "#fbbf24"),
        ("1", "winner\npromoted", "Leaderboard on a\nfrozen test set", "#f59e0b"),
        ("v0.1.0", "packaged\n& released", "Versioned model,\nAPI, benchmarks", ORANGE),
    ]
    n = len(stages)
    fig, ax = bare_axes(13.4, 5.6 if not cover else 6.6, (0, 100), (0, 100))

    seg_w = 17.2
    gap = 2.4
    x0 = 2.6
    cy = 46 if not cover else 42
    h_top, h_bot = 62, 26  # funnel heights, shrinking

    for i, (num, sub, caption, color) in enumerate(stages):
        x = x0 + i * (seg_w + gap)
        h_l = h_top + (h_bot - h_top) * (i / n)
        h_r = h_top + (h_bot - h_top) * ((i + 1) / n)
        tip = 3.2
        pts = [
            (x, cy + h_l / 2),
            (x + seg_w - tip, cy + h_r / 2),
            (x + seg_w, cy),
            (x + seg_w - tip, cy - h_r / 2),
            (x, cy - h_bot / 2 - (h_l - h_bot) / 2),
        ]
        # simple chevron: left edge vertical, right edge pointed
        pts = [
            (x, cy + h_l / 2),
            (x + seg_w - tip, cy + h_r / 2),
            (x + seg_w, cy),
            (x + seg_w - tip, cy - h_r / 2),
            (x, cy - h_l / 2),
        ]
        ax.add_patch(Polygon(pts, closed=True, fc=color, ec="white", lw=2.5, zorder=2))
        num_size = 27 if len(num) <= 2 else 17
        ax.text(
            x + (seg_w - tip) / 2,
            cy + 4.5,
            num,
            ha="center",
            va="center",
            fontsize=num_size,
            fontweight="bold",
            color="white" if i >= 3 else INK,
            zorder=3,
        )
        ax.text(
            x + (seg_w - tip) / 2,
            cy - 9.5,
            sub,
            ha="center",
            va="center",
            fontsize=10.5,
            color="white" if i >= 3 else INK,
            zorder=3,
            linespacing=1.25,
        )
        ax.text(
            x + (seg_w - tip) / 2,
            cy - h_top / 2 - 7,
            caption,
            ha="center",
            va="top",
            fontsize=9.5,
            color=MUTED,
            linespacing=1.3,
        )

    if cover:
        ax.text(
            50,
            93,
            "Racing models, not opinions",
            ha="center",
            va="center",
            fontsize=23,
            fontweight="bold",
            color=INK,
        )
        ax.text(
            50,
            84.5,
            "How we ran wildfire ML R&D for Pyronear",
            ha="center",
            va="center",
            fontsize=13,
            color=MUTED,
        )
    fig.savefig(path)
    plt.close(fig)


# ------------------------------------------------- figure 2: system context
def make_system_context(path):
    fig, ax = bare_axes(12.8, 4.9, (0, 100), (0, 100))

    # zones
    rounded_box(ax, (1.5, 14), 44, 70, fc="#f1f5f9", ec=FAINT, lw=1.2, radius=2)
    rounded_box(ax, (50.5, 14), 48, 70, fc="#fff7ed", ec="#fed7aa", lw=1.2, radius=2)
    ax.text(23.5, 88.5, "ON THE TOWER  ·  EDGE", ha="center", fontsize=10, color=MUTED, fontweight="bold")
    ax.text(74.5, 88.5, "ON THE SERVER", ha="center", fontsize=10, color=ORANGE, fontweight="bold")

    boxes = [
        (4.5, "360° cameras", "1 frame every 30 s,\n30–60 km visibility", PAPER, FAINT, INK),
        (25.5, "YOLO detector", "Raspberry Pi,\nflags smoke candidates", PAPER, FAINT, INK),
        (53.5, "Temporal verifier", "judges the sequence,\nnot the frame  (this work)", ORANGE, ORANGE, "white"),
        (79.0, "Alert platform", "reviewed by the\nfire department", PAPER, FAINT, INK),
    ]
    bw, bh, by = 17.5, 42, 28
    for x, title, sub, fc, ec, tc in boxes:
        rounded_box(ax, (x, by), bw, bh, fc=fc, ec=ec, lw=1.6, radius=1.8)
        ax.text(x + bw / 2, by + bh - 11, title, ha="center", fontsize=12, fontweight="bold", color=tc)
        ax.text(
            x + bw / 2,
            by + 12,
            sub,
            ha="center",
            va="center",
            fontsize=9.5,
            color="#ffedd5" if fc == ORANGE else MUTED,
            linespacing=1.35,
        )

    ay = by + bh / 2
    arrow(ax, (22.4, ay), (25.2, ay), color=MUTED)
    arrow(ax, (43.4, ay), (53.2, ay), color=MUTED)
    arrow(ax, (71.4, ay), (78.7, ay), color=ORANGE)
    ax.text(48.2, ay + 6.5, "candidate\nsequences", ha="center", fontsize=9, color=MUTED, linespacing=1.25)
    ax.text(75.1, ay + 6.5, "confirmed\nalerts", ha="center", fontsize=9, color=ORANGE, linespacing=1.25)

    fig.savefig(path)
    plt.close(fig)


# ---------------------------------------------- figure 3: experiment anatomy
def make_experiment_anatomy(path):
    fig, ax = bare_axes(12.8, 6.4, (0, 100), (0, 100))

    # left: folder tree card
    rounded_box(ax, (2, 6), 46, 88, fc=CARD, ec=FAINT, lw=1.4, radius=2)
    ax.text(4.8, 87, "experiments/temporal-models/<name>/", fontsize=11, fontweight="bold", family="monospace", color=INK)
    tree = [
        ("├── pyproject.toml · uv.lock · .python-version", BLUE),
        ("├── Makefile  (install · lint · format · test)", MUTED),
        ("├── src/<package>/   ← implements TemporalModel", GREEN),
        ("├── configs/  ·  scripts/  ·  notebooks/", MUTED),
        ("└── data/            ← DVC-tracked, never in git", AMBER),
        ("      ├── 01_raw/          dataset @ pinned tag", AMBER),
        ("      ├── …                Kedro layers 02–07", AMBER),
        ("      └── 08_reporting/    metrics & figures", AMBER),
    ]
    y = 79
    for line, color in tree:
        ax.text(4.8, y, line, fontsize=10.3, family="monospace", color=color)
        y -= 9.2

    # right: three principles
    principles = [
        (
            "Isolated",
            "Own virtualenv, pinned Python,\npinned dependencies. Nothing\nshared, nothing to break.",
            BLUE,
            68.5,
        ),
        (
            "Pinned",
            "Data imported by version tag:\ndvc import pyro-dataset --rev v3.0.0.\nEvery result is reproducible.",
            AMBER,
            38.5,
        ),
        (
            "Comparable",
            "Every model implements the same\nTemporalModel protocol — same inputs,\nsame outputs, same test set.",
            GREEN,
            8.5,
        ),
    ]
    for title, body, color, y0 in principles:
        rounded_box(ax, (56, y0), 41, 25, fc=PAPER, ec=color, lw=1.8, radius=1.8)
        ax.text(58.5, y0 + 18.5, title, fontsize=12.5, fontweight="bold", color=color)
        ax.text(58.5, y0 + 9, body, fontsize=9.6, color=MUTED, va="center", linespacing=1.45)

    fig.savefig(path)
    plt.close(fig)


# ------------------------------------------------ figure 4: leaderboard chart
LEADERBOARD = [
    # name, precision, recall, f1, fpr, mean_ttd
    ("Bbox-Tube Temporal\n(ViT-DINOv2)", 0.9608, 0.9735, 0.9671, 0.0397, 3.4),
    ("FSM Tracking\nbaseline", 0.9474, 0.9536, 0.9505, 0.0530, 4.6),
    ("Bbox-Tube Temporal\n(GRU-ConvNeXt)", 0.9272, 0.9272, 0.9272, 0.0728, 2.0),
    ("Production baseline\n(pyro-detector)", 0.8580, 0.9603, 0.9063, 0.1589, 1.3),
    ("MTB change\ndetection", 0.7121, 0.9338, 0.8080, 0.3775, 3.0),
]


def make_leaderboard(path):
    fig, ax = plt.subplots(figsize=(11.4, 6.4))

    for name, _p, _r, f1, fpr, _ttd in LEADERBOARD:
        is_winner = "ViT-DINOv2" in name
        is_prod = "Production" in name
        if is_winner:
            ax.scatter(fpr, f1, s=460, marker="*", c=ORANGE, ec="white", lw=1.2, zorder=4)
        elif is_prod:
            ax.scatter(fpr, f1, s=170, marker="D", c=MUTED, ec="white", lw=1.2, zorder=4)
        else:
            ax.scatter(fpr, f1, s=170, marker="o", c="#94a3b8", ec="white", lw=1.2, zorder=3)

    offsets = {
        "Bbox-Tube Temporal\n(ViT-DINOv2)": (0.013, 0.004),
        "FSM Tracking\nbaseline": (0.013, -0.012),
        "Bbox-Tube Temporal\n(GRU-ConvNeXt)": (0.013, -0.004),
        "Production baseline\n(pyro-detector)": (0.013, -0.004),
        "MTB change\ndetection": (-0.013, 0.004),
    }
    for name, _p, _r, f1, fpr, _ttd in LEADERBOARD:
        dx, dy = offsets[name]
        ha = "left" if dx > 0 else "right"
        weight = "bold" if ("ViT" in name or "Production" in name) else "normal"
        color = INK if ("ViT" in name or "Production" in name) else MUTED
        ax.annotate(
            name.replace("\n", " "),
            (fpr, f1),
            xytext=(fpr + dx, f1 + dy),
            fontsize=10.5,
            ha=ha,
            color=color,
            fontweight=weight,
        )

    # 4x bracket between production and winner
    ax.annotate(
        "",
        xy=(0.0397 + 0.004, 0.962),
        xytext=(0.1589 - 0.004, 0.911),
        arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.0, ls="--", mutation_scale=16),
    )
    ax.text(
        0.20,
        0.947,
        "4× fewer false alarms,\nhigher recall",
        fontsize=10.5,
        color=ORANGE,
        ha="left",
        fontstyle="italic",
        linespacing=1.3,
    )

    ax.set_xlabel("False positive rate  (lower is better →  fewer false alarms)", fontsize=11.5)
    ax.set_ylabel("F1 score  (higher is better)", fontsize=11.5)
    ax.set_xlim(-0.02, 0.43)
    ax.set_ylim(0.78, 0.99)
    ax.grid(True, ls=":", lw=0.7, color=FAINT)
    ax.tick_params(colors=MUTED, labelsize=10)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.set_title(
        "Five candidate verifiers on the same frozen test set — 302 sequences, pyro-dataset v3.0.0",
        fontsize=12,
        color=INK,
        pad=14,
    )
    fig.savefig(path)
    plt.close(fig)


# -------------------------------------------------- figure 5: lifecycle
def make_lifecycle(path):
    fig, ax = bare_axes(13.2, 5.8, (0, 100), (0, 100))

    # stage 1: research repo
    rounded_box(ax, (1.5, 16), 27, 70, fc="#f1f5f9", ec=FAINT, lw=1.4, radius=2)
    ax.text(15, 79, "vision-rd", ha="center", fontsize=13, fontweight="bold", color=INK)
    ax.text(15, 73.5, "research repo", ha="center", fontsize=9.5, color=MUTED)
    inner = ["literature_survey/", "experiments/  (×5 models)", "leaderboard"]
    y = 59
    for label in inner:
        rounded_box(ax, (4.5, y - 5.5), 21, 11, fc=PAPER, ec=FAINT, lw=1.2, radius=1.4)
        ax.text(15, y, label, ha="center", va="center", fontsize=9.5, family="monospace", color=INK)
        y -= 15.5

    # stage 2: monorepo
    rounded_box(ax, (38.5, 16), 27, 70, fc="#fff7ed", ec="#fed7aa", lw=1.4, radius=2)
    ax.text(52, 79, "temporal-model", ha="center", fontsize=13, fontweight="bold", color=ORANGE)
    ax.text(52, 73.5, "production monorepo", ha="center", fontsize=9.5, color=MUTED)
    pkgs = ["core/  — the model", "train/ · eval/  — pipelines", "api/  — FastAPI service", "benchmark/  — latency"]
    y = 59
    for label in pkgs:
        rounded_box(ax, (41.5, y - 5), 21, 10, fc=PAPER, ec="#fed7aa", lw=1.2, radius=1.4)
        ax.text(52, y, label, ha="center", va="center", fontsize=8.8, family="monospace", color=INK)
        y -= 12.5

    # stage 3: release
    rounded_box(ax, (75.5, 16), 23, 70, fc="#f0fdf4", ec="#bbf7d0", lw=1.4, radius=2)
    ax.text(87, 79, "model.zip", ha="center", fontsize=13, fontweight="bold", color=GREEN, family="monospace")
    ax.text(87, 73.5, "self-contained release", ha="center", fontsize=9.5, color=MUTED)
    files = ["manifest.yaml", "yolo_weights.pt", "classifier.ckpt", "config.yaml", "calibrator.json"]
    y = 62
    for label in files:
        ax.text(87, y, label, ha="center", va="center", fontsize=9.3, family="monospace", color=INK)
        y -= 7.5
    ax.text(87, 21.5, "→ HuggingFace release\n→ Docker API", ha="center", fontsize=9.3, color=GREEN, linespacing=1.5)

    ay = 51
    arrow(ax, (29, ay), (38, ay), color=ORANGE, lw=2.6)
    ax.text(33.6, ay + 6, "promote\nthe winner", ha="center", fontsize=9.5, color=ORANGE, linespacing=1.3)
    arrow(ax, (66, ay), (75, ay), color=GREEN, lw=2.6)
    ax.text(70.6, ay + 6, "package\n& version", ha="center", fontsize=9.5, color=GREEN, linespacing=1.3)

    fig.savefig(path)
    plt.close(fig)


if __name__ == "__main__":
    BUNDLE.mkdir(parents=True, exist_ok=True)
    COVER_DIR.mkdir(parents=True, exist_ok=True)
    make_funnel(BUNDLE / "funnel.png")
    make_cover(COVER_DIR / "cover.png")
    make_system_context(BUNDLE / "system_context.png")
    make_experiment_anatomy(BUNDLE / "experiment_anatomy.png")
    make_leaderboard(BUNDLE / "leaderboard.png")
    make_lifecycle(BUNDLE / "lifecycle.png")
    print("done:", BUNDLE)
