"""Draw 2.1_voltage_sine.png and 2.2_current_sine.png: GeoGebra-style graphs of the sinusoids in
exercises 2.1 e) and 2.2 e) (solutions in c_solutions.md), with the start value, the zero
crossings and the extreme points marked.

Usage: python3 2.1_2.2_sines.py (requires matplotlib and numpy). The images are written next to
this script.
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


# ------------------------------------------- 2.1: u(t) = 12,6 sin(200 pi t + 2,82) V
U = math.sqrt(160)
d = math.pi - math.atan(1 / 3)
w = 200 * math.pi
fig, ax = plt.subplots(figsize=(8.6, 5.4), dpi=170)
setup(ax, (-0.8, 11.2), (-15.5, 15.5), "$t$ (ms)", "$u(t)$ (V)", xstep=1, ystep=5, minor=1)
t = np.linspace(0, 10, 800)
ax.plot(t, U * np.sin(w * t / 1000 + d), color=CURVE, lw=2.6, zorder=4)
mark(ax, 0, 4, "$u(0) = 4$ V", 10, 6, ha="left")
t_min = (1.5 * math.pi - d) / w * 1000
t_max = (2.5 * math.pi - d) / w * 1000
mark(ax, t_min, -U, f"Minimum ({comma(t_min, 2)}; −12,6)", 0, -12, ha="center", va="top")
mark(ax, t_max, U, f"Maximum ({comma(t_max, 2)}; 12,6)", 0, 12, ha="center")
ax.text(8.6, -10.0, "$u(t) = 12{,}6\\sin(200\\pi t + 2{,}82)$", ha="center", va="center",
        color=CURVE, fontsize=13, zorder=7,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=MAJOR))
finish(fig, ax, OUT / "2.1_voltage_sine.png")

# ------------------------------------------- 2.2: i(t) = 10 sin(100 pi t - 3 pi / 4) mA
d = -3 * math.pi / 4
w = 100 * math.pi
fig, ax = plt.subplots(figsize=(8.6, 5.4), dpi=170)
setup(ax, (-1.6, 22.4), (-12.5, 12.5), "$t$ (ms)", "$i(t)$ (mA)", xstep=2.5, ystep=5, minor=2.5)
t = np.linspace(0, 20, 800)
ax.plot(t, 10 * np.sin(w * t / 1000 + d), color=CURVE, lw=2.6, zorder=4)
mark(ax, 0, 10 * math.sin(d), "$i(0) \\approx$ −7,07 mA", 10, 8, ha="left", va="bottom")
mark(ax, 2.5, -10, "Minimum (2,5; −10)", 0, -12, ha="center", va="top")
mark(ax, 12.5, 10, "Maximum (12,5; 10)", 0, 12, ha="center")
ax.text(16.5, -8.6, "$i(t) = 10\\sin(100\\pi t - 3\\pi/4)$", ha="center", va="center",
        color=CURVE, fontsize=13, zorder=7,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=MAJOR))
finish(fig, ax, OUT / "2.2_current_sine.png")
