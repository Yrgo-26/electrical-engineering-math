"""Draw 1.1_voltage.png: a GeoGebra-style graph of u(t) = 3t^2 - 4t + 2 in exercise 1.1 d)-g)
(solution in c_solutions.md), with the stationary point and the initial voltage marked.

Usage: python3 1.1_voltage.py (requires matplotlib and numpy). The image is written next to this
script.
"""
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter, MultipleLocator

OUT = Path(__file__).parent
CURVE = "#1f5fae"      # one strong colour for the curve and its points
INK = "#1d1d1f"        # text
AXIS = "#333333"
MAJOR = "#cfd3d8"
MINOR = "#eceef1"

plt.rcParams.update({
    "font.size": 13,
    "font.family": "DejaVu Sans",
    "mathtext.fontset": "dejavusans",
    "axes.unicode_minus": True,
})


def comma(v, decimals):
    s = f"{v:.{decimals}f}".replace(".", ",")
    return s.replace("-", "−")


def tick_fmt(v, _pos):
    if abs(v) < 1e-9:
        return ""                      # origin is labelled once, see below
    return comma(v, 0) if abs(v - round(v)) < 1e-9 else comma(v, 1)


def setup(ax, xlim, ylim, xlabel, ylabel, xstep=1, ystep=1, minor=0.5):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_facecolor("white")
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_position("zero")
        ax.spines[side].set_color(AXIS)
        ax.spines[side].set_linewidth(1.2)
        ax.spines[side].set_zorder(2)
    ax.xaxis.set_major_locator(MultipleLocator(xstep))
    ax.yaxis.set_major_locator(MultipleLocator(ystep))
    ax.xaxis.set_minor_locator(MultipleLocator(minor))
    ax.yaxis.set_minor_locator(MultipleLocator(minor))
    ax.xaxis.set_major_formatter(FuncFormatter(tick_fmt))
    ax.yaxis.set_major_formatter(FuncFormatter(tick_fmt))
    ax.tick_params(which="both", colors=AXIS, labelcolor=INK, direction="inout")
    ax.tick_params(which="major", length=6)
    ax.tick_params(which="minor", length=0)
    # grid drawn by hand beneath the axes, so the tick labels' white boxes cover it
    for v in np.arange(math.ceil(xlim[0] / minor) * minor, xlim[1], minor):
        major = abs(v / xstep - round(v / xstep)) < 1e-9
        ax.axvline(v, color=MAJOR if major else MINOR, lw=0.9 if major else 0.7, zorder=0.1)
    for v in np.arange(math.ceil(ylim[0] / minor) * minor, ylim[1], minor):
        major = abs(v / ystep - round(v / ystep)) < 1e-9
        ax.axhline(v, color=MAJOR if major else MINOR, lw=0.9 if major else 0.7, zorder=0.1)
    ax.set_axisbelow(False)
    # arrow heads and axis names at the positive ends
    ax.plot(1, 0, ">", color=AXIS, transform=ax.get_yaxis_transform(), clip_on=False, ms=7)
    ax.plot(0, 1, "^", color=AXIS, transform=ax.get_xaxis_transform(), clip_on=False, ms=7)
    ax.annotate(xlabel, xy=(1, 0), xycoords=ax.get_yaxis_transform(), xytext=(-4, 8),
                textcoords="offset points", ha="right", va="bottom", color=INK, fontsize=14)
    ax.annotate(ylabel, xy=(0, 1), xycoords=ax.get_xaxis_transform(), xytext=(10, -2),
                textcoords="offset points", ha="left", va="top", color=INK, fontsize=14)
    ax.annotate("0", xy=(0, 0), xytext=(-6, -6), textcoords="offset points",
                ha="right", va="top", color=INK, fontsize=13)


def finish(fig, ax, path):
    fig.tight_layout()
    fig.canvas.draw()
    for tick in ax.xaxis.get_major_ticks() + ax.yaxis.get_major_ticks():
        tick.label1.set_bbox(dict(boxstyle="square,pad=0.15", fc="white", ec="none"))
    fig.savefig(path, facecolor="white")
    plt.close(fig)


def mark(ax, x, y, text, dx, dy, ha="left", va="bottom"):
    ax.plot(x, y, "o", ms=9, color=CURVE, markeredgecolor="white", markeredgewidth=1.8,
            zorder=5)
    ax.annotate(text, xy=(x, y), xytext=(dx, dy), textcoords="offset points", ha=ha, va=va,
                color=INK, fontsize=13, zorder=6,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85))


# ------------------------------------------------------------ 1.1: u(t) = 3t^2 - 4t + 2
fig, ax = plt.subplots(figsize=(7.6, 5.6), dpi=170)
setup(ax, (-0.35, 2.85), (-0.7, 7.4), "$t$ (s)", "$u(t)$ (V)", xstep=0.5, ystep=1, minor=0.25)
t = np.linspace(0, 2.4, 800)
u = 3 * t**2 - 4 * t + 2
ax.plot(t, u, color=CURVE, lw=2.6, zorder=4)
tm = 2 / 3
um = 3 * tm**2 - 4 * tm + 2
mark(ax, tm, um, f"Minimum ({comma(tm, 2)}; {comma(um, 2)})", 0, -14, ha="center", va="top")
mark(ax, 0, 2, "$u(0) = 2$ V", 10, 4, ha="left")
ax.text(0.8, 5.2, "$u(t) = 3t^2 - 4t + 2$", ha="center", va="center", color=CURVE,
        fontsize=14, zorder=7,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=MAJOR))
finish(fig, ax, OUT / "1.1_voltage.png")
