"""Draw 2.2_current.png: the current phasor I = 10e^(-j3pi/4) mA in the complex plane (solution
to 2.2 d)).

Usage: python3 2.2_current.py (requires matplotlib). The image is written next to this script.
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


I = cmath.rect(10, -3 * math.pi / 4)
fig, ax = plt.subplots(figsize=(9.4, 6.6), dpi=150)
plane(ax, (-13.0, 2.4), (-9.0, 2.0), "Strömmen I i det komplexa talplanet")
# Components: the real part along the Re axis, the imaginary part down to I.
ax.plot([0, I.real], [0, 0], color="#0072B2", lw=4, zorder=2, solid_capstyle="butt")
ax.plot([I.real, I.real], [0, I.imag], color="#56B4E9", lw=3, zorder=2)
phasor(ax, I, "#009E73", f"I ≈ {num(I.real)} − j{num(-I.imag)} mA", offset=(-10, -22), ha="left")
ax.text(I.real / 2, 0.35, f"Re(I) ≈ {num(I.real)} mA", ha="center", color="#0072B2")
ax.text(I.real - 0.25, I.imag / 2, f"Im(I) ≈ {num(I.imag)} mA", ha="right", va="center",
        color="#1F77B4")
ax.text(-4.9, -3.4, "|I| = 10 mA", ha="center", color="#009E73",
        rotation=45, rotation_mode="anchor")
ax.add_patch(Arc((0, 0), 3.0, 3.0, theta1=-135, theta2=0, color="#0072B2", lw=2.5, zorder=3))
ax.text(1.0, -1.45, "δ = −135°", color="#0072B2", va="center")
fig.tight_layout()
fig.savefig(OUT)
plt.close(fig)
