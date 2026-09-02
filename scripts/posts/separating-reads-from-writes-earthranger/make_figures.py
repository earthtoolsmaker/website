"""Generate all figures for the 'Separating Reads from Writes' EarthRanger blog post.

Usage:
    uv run --with matplotlib python make_figures.py

Outputs PNGs into the post's page bundle
(content/posts/separating-reads-from-writes-earthranger/images/). The cover is
a hand-drawn SVG in assets/images/posts/separating-reads-from-writes-earthranger/,
rendered to cover.png with headless Chromium so the site's web fonts apply.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch, FancyBboxPatch, Rectangle

HERE = Path(__file__).resolve().parent
SITE = HERE.parent.parent.parent
SLUG = "separating-reads-from-writes-earthranger"
BUNDLE = SITE / "content" / "posts" / SLUG / "images"

INK = "#1e293b"
MUTED = "#64748b"
FAINT = "#cbd5e1"
PAPER = "#ffffff"
CARD = "#f8fafc"
# Same roles as the project page diagram: terracotta for writes, teal for reads.
WRITE = "#c2603f"
WRITE_LIGHT = "#f2c0a4"
READ = "#0e7c86"
READ_LIGHT = "#bfe0d6"
GREEN = "#15803d"
RED = "#b91c1c"
AMBER = "#f59e0b"

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


# ------------------------------------------------------------------ helpers
def canvas(w_in, h_in):
    """Axes with square data units: x in [0, 100], y in [0, 100 * h / w]."""
    fig, ax = plt.subplots(figsize=(w_in, h_in))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100 * h_in / w_in)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def box(ax, x, y, w, h, fc=CARD, ec=FAINT, lw=1.4, radius=1.6, ls="-", zorder=2):
    p = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={radius}",
        fc=fc, ec=ec, lw=lw, ls=ls, zorder=zorder,
    )
    ax.add_patch(p)
    return p


def arrow(ax, p0, p1, color=MUTED, lw=2.2, style="-|>", shrink=3, rad=0.0, ls="-", zorder=3):
    a = FancyArrowPatch(
        p0, p1, arrowstyle=style, color=color, lw=lw, mutation_scale=16,
        shrinkA=shrink, shrinkB=shrink, connectionstyle=f"arc3,rad={rad}",
        linestyle=ls, zorder=zorder,
    )
    ax.add_patch(a)
    return a


def cylinder(ax, cx, cy, w, h, color, light, zorder=3):
    """A database cylinder centred on (cx, cy)."""
    ry = w * 0.18
    ax.add_patch(Ellipse((cx, cy - h / 2), w, 2 * ry, fc=color, ec=color, zorder=zorder))
    ax.add_patch(Rectangle((cx - w / 2, cy - h / 2), w, h, fc=color, ec="none", zorder=zorder))
    ax.add_patch(Ellipse((cx, cy + h / 2), w, 2 * ry, fc=light, ec=color, lw=1.2, zorder=zorder + 1))


def label(ax, x, y, s, size=10, color=INK, weight="normal", ha="center", va="center", **kw):
    ax.text(x, y, s, ha=ha, va=va, fontsize=size, color=color, fontweight=weight, zorder=6, **kw)


# ---------------------------------------------------------- figure: 90 / 10
def make_traffic_split(path):
    fig, ax = canvas(13.4, 4.6)
    H = 100 * 4.6 / 13.4  # 34.3

    x0, x1, y, h = 6, 94, H / 2 - 1, 7.5
    w = x1 - x0
    ax.add_patch(Rectangle((x0, y), w * 0.9, h, fc=READ, ec="none", zorder=2))
    ax.add_patch(Rectangle((x0 + w * 0.9, y), w * 0.1, h, fc=WRITE, ec="none", zorder=2))
    box(ax, x0, y, w, h, fc="none", ec=PAPER, lw=2.5, radius=1.2, zorder=3)

    label(ax, x0 + w * 0.45, y + h / 2, "90% reads", size=15, color=PAPER, weight="bold")
    label(ax, x0 + w * 0.95, y + h / 2, "10%", size=12, color=PAPER, weight="bold")

    # read workloads (above)
    label(ax, x0 + w * 0.45, y + h + 6.5,
          "maps  ·  dashboards  ·  reports  ·  integrations pulling data",
          size=10.5, color=READ)
    label(ax, x0 + w * 0.45, y + h + 3.2,
          "bursty and heavy: one request can touch months of history",
          size=9, color=MUTED)

    # write workloads (below)
    label(ax, x0 + w * 0.95, y - 3.4, "writes", size=10.5, color=WRITE, weight="bold")
    label(ax, x0 + w * 0.95, y - 6.6, "collar positions  ·  events  ·  patrols",
          size=9.5, color=WRITE, ha="center")
    label(ax, x0 + w * 0.95, y - 9.6, "small, constant, must land", size=9, color=MUTED)

    label(ax, x0, y - 3.4, "one PostgreSQL primary, before the split", size=9, color=MUTED, ha="left")

    fig.savefig(path)
    plt.close(fig)


# ------------------------------------------------------ figure: architecture
def make_architecture(path):
    fig, ax = canvas(13.4, 6.6)
    H = 100 * 6.6 / 13.4  # 49.3

    # Kubernetes cluster
    kx, ky, kw, kh = 3, 5, 58, H - 9
    box(ax, kx, ky, kw, kh, fc=CARD, ec=FAINT, lw=1.6, radius=2.2, zorder=1)
    label(ax, kx + 2.2, ky + kh - 2.6, "KUBERNETES CLUSTER", size=9, color=MUTED, weight="bold", ha="left")

    # application pods
    def pods(x, y, n, title, sub):
        pw, ph, gap = 6.2, 4.4, 1.0
        for i in range(n):
            box(ax, x + i * (pw + gap), y, pw, ph, fc=PAPER, ec=FAINT, lw=1.2, radius=0.9)
            label(ax, x + i * (pw + gap) + pw / 2, y + ph / 2, "pod", size=7.5, color=MUTED)
        total = n * pw + (n - 1) * gap
        label(ax, x + total / 2, y + ph + 2.3, title, size=10, weight="bold")
        label(ax, x + total / 2, y - 2.2, sub, size=8, color=MUTED)
        return x + total, y + ph / 2

    ax_end, ay = pods(7, 30, 3, "API pods", "Django, autoscaled")
    wx_end, wy = pods(7, 13, 2, "Worker pods", "ingestion, background jobs")

    # pgcat
    px, py, pw, ph = 39, 15, 18, 20
    box(ax, px, py, pw, ph, fc=PAPER, ec=READ, lw=1.8, radius=1.6)
    label(ax, px + pw / 2, py + ph - 3.2, "pgcat", size=13, weight="bold", color=READ)
    label(ax, px + pw / 2, py + ph - 6.6, "Deployment, 3 replicas", size=8.5, color=MUTED)
    for i in range(3):
        box(ax, px + 2.2 + i * 4.7, py + 6.0, 4.0, 3.4, fc=READ_LIGHT, ec=READ, lw=1.0, radius=0.7)
    label(ax, px + pw / 2, py + 3.0, "ClusterIP Service :6432", size=8.5, color=MUTED)
    label(ax, px + pw / 2, py - 2.6, "ConfigMap + Secret", size=8, color=MUTED)

    arrow(ax, (ax_end + 1, ay), (px, py + ph * 0.66), color=MUTED, lw=2.0)
    arrow(ax, (wx_end + 1, wy), (px, py + ph * 0.34), color=MUTED, lw=2.0)
    label(ax, 33, 26.5, "one\nDATABASE_URL", size=8.5, color=MUTED, linespacing=1.3)

    # Cloud SQL
    cx, cy, cw, ch = 66, 5, 31, H - 9
    box(ax, cx, cy, cw, ch, fc=CARD, ec=FAINT, lw=1.6, radius=2.2, zorder=1)
    label(ax, cx + 2.2, cy + ch - 2.6, "CLOUD SQL", size=9, color=MUTED, weight="bold", ha="left")

    prim = (cx + cw / 2, cy + ch - 12)
    cylinder(ax, prim[0], prim[1], 9, 7, WRITE, WRITE_LIGHT)
    label(ax, prim[0], prim[1] - 6.2, "primary", size=10, weight="bold", color=WRITE)

    reps = [(cx + 6.5, cy + 10), (cx + cw / 2, cy + 10), (cx + cw - 6.5, cy + 10)]
    for r in reps:
        cylinder(ax, r[0], r[1], 6.2, 5.4, READ, READ_LIGHT)
        arrow(ax, (prim[0], prim[1] - 3.5), (r[0], r[1] + 3.6), color=FAINT, lw=1.4, ls="--", shrink=5, zorder=2)
    label(ax, cx + cw / 2, cy + 3.2, "read replicas, streaming replication", size=9, weight="bold", color=READ)

    # routed traffic
    arrow(ax, (px + pw, py + ph * 0.72), (prim[0] - 5, prim[1]), color=WRITE, lw=2.6, rad=-0.15)
    label(ax, 67, prim[1] + 3.6, "writes", size=9.5, color=WRITE, weight="bold")
    arrow(ax, (px + pw, py + ph * 0.32), (reps[0][0] - 4.5, reps[0][1]), color=READ, lw=3.2, rad=0.15)
    label(ax, 66, reps[0][1] - 4.2, "reads", size=9.5, color=READ, weight="bold")

    fig.savefig(path)
    plt.close(fig)


# ----------------------------------------------------------- figure: routing
def make_routing(path):
    fig, ax = canvas(13.4, 4.8)
    H = 100 * 4.8 / 13.4  # 35.8
    y = H / 2 + 3
    bw, bh = 17, 8

    def node(x, text, fc=PAPER, ec=FAINT, color=INK, size=9.5):
        box(ax, x - bw / 2, y - bh / 2, bw, bh, fc=fc, ec=ec, lw=1.6, radius=1.4)
        label(ax, x, y, text, size=size, color=color, linespacing=1.3)

    node(11, "statement\narrives at pgcat")
    node(38, "client pinned\na server role?", fc=CARD)
    node(65, "is it a\nSELECT?", fc=CARD)

    arrow(ax, (11 + bw / 2, y), (38 - bw / 2, y), lw=2.0)
    arrow(ax, (38 + bw / 2, y), (65 - bw / 2, y), lw=2.0)
    label(ax, 51.5, y + 1.6, "no", size=8.5, color=MUTED)

    # SELECT -> replica ; else -> primary
    rx, px = 90, 90
    ry, py = y + 7.5, y - 7.5
    cylinder(ax, rx, ry, 7.5, 5.2, READ, READ_LIGHT)
    label(ax, rx, ry - 5.4, "a replica", size=9.5, color=READ, weight="bold")
    cylinder(ax, px, py, 7.5, 5.2, WRITE, WRITE_LIGHT)
    label(ax, px, py - 5.4, "the primary", size=9.5, color=WRITE, weight="bold")

    arrow(ax, (65 + bw / 2, y + 1.5), (rx - 5, ry), color=READ, lw=2.6, rad=-0.2)
    label(ax, 77.5, y + 7.0, "yes", size=8.5, color=READ, weight="bold")
    arrow(ax, (65 + bw / 2, y - 1.5), (px - 5, py), color=WRITE, lw=2.6, rad=0.2)
    label(ax, 65, y - bh / 2 - 2.4, "no: INSERT, UPDATE, BEGIN, DDL ...", size=8, color=WRITE)

    # override path
    oy = y - 12.5
    arrow(ax, (38, y - bh / 2), (38, oy + 3), color=AMBER, lw=2.2)
    label(ax, 41.5, y - bh / 2 - 2.2, "yes", size=8.5, color=AMBER, weight="bold", ha="left")
    box(ax, 20, oy - 3.2, 36, 6.4, fc="#fff7ed", ec=AMBER, lw=1.4, radius=1.2)
    label(ax, 38, oy, "SET SERVER ROLE TO 'primary'  (or 'replica')", size=8, color="#9a3412", family="DejaVu Sans Mono")
    arrow(ax, (56, oy), (px - 5, py - 1.5), color=AMBER, lw=2.2, rad=0.12)
    label(ax, 72, oy - 2.6, "skip the parser, use the pinned role", size=8, color=MUTED)

    fig.savefig(path)
    plt.close(fig)


# -------------------------------------------------- figure: read-your-writes
def make_read_your_writes(path):
    fig, ax = canvas(13.4, 6.0)
    H = 100 * 6.0 / 13.4  # 44.8

    def panel(x0, title, pinned):
        w = 44
        box(ax, x0, 3, w, H - 6, fc=CARD, ec=FAINT, lw=1.4, radius=2.0, zorder=1)
        label(ax, x0 + w / 2, H - 6, title, size=10.5, weight="bold")

        cols = {"app": x0 + 8, "primary": x0 + 24, "replica": x0 + 38}
        top, bot = H - 10, 6.5
        for name, cx in cols.items():
            color = {"app": INK, "primary": WRITE, "replica": READ}[name]
            label(ax, cx, top, name, size=9, color=color, weight="bold")
            ax.plot([cx, cx], [top - 2, bot], color=FAINT, lw=1.2, zorder=1)

        # 1. write
        y1 = top - 7
        arrow(ax, (cols["app"], y1), (cols["primary"], y1), color=WRITE, lw=2.2)
        label(ax, (cols["app"] + cols["primary"]) / 2, y1 + 1.8, "INSERT event", size=8.5, color=WRITE)

        # replication, arriving late
        y_rep_start, y_rep_end = y1 - 1.5, bot + 3
        arrow(ax, (cols["primary"], y_rep_start), (cols["replica"], y_rep_end), color=FAINT, lw=1.6, ls="--", shrink=2, zorder=2)
        label(ax, cols["primary"] + 1.5, y1 - 4.6, "replication lag", size=7.5, color=MUTED, ha="left")

        # 2. read
        y2 = top - 17
        if not pinned:
            arrow(ax, (cols["app"], y2), (cols["replica"], y2), color=READ, lw=2.2)
            label(ax, (cols["app"] + cols["replica"]) / 2, y2 + 1.8, "SELECT event  (parser picks a replica)", size=8, color=READ)
            arrow(ax, (cols["replica"], y2 - 3.5), (cols["app"], y2 - 3.5), color=RED, lw=2.0)
            label(ax, (cols["app"] + cols["replica"]) / 2, y2 - 5.6, "row not there yet", size=9, color=RED, weight="bold")
        else:
            label(ax, cols["app"] + 1.2, y2 + 3.6, "SET SERVER ROLE TO 'primary'", size=8, color="#9a3412", ha="left", family="DejaVu Sans Mono")
            arrow(ax, (cols["app"], y2), (cols["primary"], y2), color=WRITE, lw=2.2)
            label(ax, (cols["app"] + cols["primary"]) / 2, y2 + 1.8, "SELECT event", size=8.5, color=WRITE)
            arrow(ax, (cols["primary"], y2 - 3.5), (cols["app"], y2 - 3.5), color=GREEN, lw=2.0)
            label(ax, (cols["app"] + cols["primary"]) / 2, y2 - 5.6, "row found", size=9, color=GREEN, weight="bold")

    panel(4, "automatic routing: stale read", pinned=False)
    panel(52, "call site pinned to the primary", pinned=True)

    fig.savefig(path)
    plt.close(fig)


# ----------------------------------------------------------- figure: rollout
def make_rollout(path):
    fig, ax = canvas(13.4, 5.0)
    H = 100 * 5.0 / 13.4  # 37.3

    steps = [
        ("Local and CI", "pgcat in the dev stack,\ntest suite through the pooler", FAINT, INK),
        ("Staging and test clusters", "stress tests: ingestion writes\nand dashboard reads at once", READ_LIGHT, READ),
        ("Prod cluster 1", "smallest and quietest,\none full daily cycle", WRITE_LIGHT, WRITE),
        ("Prod cluster 2 ...", "next by size,\nsame gate each time", WRITE_LIGHT, WRITE),
        ("Busiest cluster", "last, once every smaller\nversion of it has passed", WRITE, PAPER),
    ]
    n = len(steps)
    bw, gap = 16.4, 2.6
    x0 = (100 - (n * bw + (n - 1) * gap)) / 2
    y, bh = H / 2 + 1, 10.5
    for i, (title, sub, fc, tc) in enumerate(steps):
        x = x0 + i * (bw + gap)
        box(ax, x, y, bw, bh, fc=fc, ec=fc if fc != FAINT else FAINT, lw=1.4, radius=1.4)
        label(ax, x + bw / 2, y + bh - 2.8, title, size=9.5, weight="bold", color=tc)
        label(ax, x + bw / 2, y + 3.6, sub, size=7.6, color=tc if fc == WRITE else MUTED, linespacing=1.25)
        if i < n - 1:
            arrow(ax, (x + bw, y + bh / 2), (x + bw + gap, y + bh / 2), color=MUTED, lw=1.8, shrink=0.5)

    # gate above
    gy = y + bh + 5.2
    label(ax, 50, gy + 2.2, "each step changes one thing: pooling only first, then read/write splitting on",
          size=9, color=MUTED)
    ax.plot([x0, x0 + n * bw + (n - 1) * gap], [gy, gy], color=FAINT, lw=1.2)

    # monitoring and rollback below
    my = y - 4.6
    label(ax, 50, my, "gate at every step: primary and replica CPU, replication lag, Query Insights, pgcat metrics, API errors and latency",
          size=8.6, color=INK)
    ry = my - 4.6
    arrow(ax, (x0 + n * bw + (n - 1) * gap - 2, ry), (x0 + 2, ry), color=AMBER, lw=2.0, shrink=0)
    label(ax, 50, ry - 2.6, "rollback is a config change: parser off, default role back to primary, reload pgcat",
          size=8.6, color="#9a3412")

    fig.savefig(path)
    plt.close(fig)


if __name__ == "__main__":
    BUNDLE.mkdir(parents=True, exist_ok=True)
    make_traffic_split(BUNDLE / "traffic_split.png")
    make_architecture(BUNDLE / "architecture.png")
    make_routing(BUNDLE / "routing.png")
    make_read_your_writes(BUNDLE / "read_your_writes.png")
    make_rollout(BUNDLE / "rollout.png")
    print("done:", BUNDLE)
