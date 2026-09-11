"""Draw 2.1_voltage.png: the voltage U = 5 - j2 V in the complex plane (solution to 2.1).

Usage: python3 2.1_voltage.py (requires matplotlib). The image is written next to this script.
"""
import cmath
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from matplotlib.ticker import FuncFormatter

OUT = Path(__file__).with_suffix(".png")
AXIS = "#FFA500"
plt.rcParams.update({"font.size": 15, "axes.titlesize": 20, "axes.labelsize": 16})


def num(x, d=2):
    """Format a number with a decimal comma and a proper minus sign."""
    return f"{x:.{d}f}".replace(".", ",").replace("-", "−")


def plane(ax, xlim, ylim, title):
    """Set up the complex plane in the course's style: orange axes and a dashed grid."""
    ax.axhline(0, color=AXIS, lw=3, zorder=1)
    ax.axvline(0, color=AXIS, lw=3, zorder=1)
    ax.grid(True, ls="--", color="#BBBBBB", lw=0.8, zorder=0)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")
    ax.set_title(title, color="#333333")
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: num(v, 0)))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: num(v, 0)))


def phasor(ax, z, color, label, lw=2.8, offset=(8, 4), ha="left"):
    """Draw z as an arrow from the origin, with a cross and a label at its tip."""
    ax.annotate("", xy=(z.real, z.imag), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=18),
                zorder=3)
    ax.plot(z.real, z.imag, "x", color=color, ms=12, mew=2.5, zorder=4)
    ax.annotate(label, (z.real, z.imag), textcoords="offset points", xytext=offset,
                color="#222222", ha=ha, zorder=5)


U = 5 - 2j
fig, ax = plt.subplots(figsize=(9, 5.6), dpi=150)
plane(ax, (-0.8, 6.8), (-3.2, 1.6), "Spänningen U = 5 − j2 V i det komplexa talplanet")
# Components: the real part along the Re axis, the imaginary part down to U.
ax.plot([0, 5], [0, 0], color="#0072B2", lw=4, zorder=2, solid_capstyle="butt")
ax.plot([5, 5], [0, -2], color="#56B4E9", lw=3, zorder=2)
ax.plot([4.75, 4.75, 5], [0, -0.25, -0.25], color="#E6D72A", lw=2.5, zorder=2)
phasor(ax, U, "#009E73", "U = 5 − j2 V", offset=(10, -6))
ax.text(2.5, 0.22, "Re(U) = 5 V", ha="center", color="#0072B2")
ax.text(5.15, -1.0, "Im(U) = −2 V", ha="left", va="center", color="#1F77B4")
ax.text(2.2, -1.45, f"|U| = √29 ≈ {num(abs(U))} V", ha="center", color="#009E73",
        rotation=math.degrees(math.atan2(-2, 5)), rotation_mode="anchor")
delta = math.degrees(cmath.phase(U))
ax.add_patch(Arc((0, 0), 2.2, 2.2, theta1=delta, theta2=0, color="#0072B2", lw=2.5, zorder=3))
ax.text(1.25, -0.28, f"δᵤ ≈ {num(delta, 1)}°", color="#0072B2", va="center")
fig.tight_layout()
fig.savefig(OUT)
plt.close(fig)
