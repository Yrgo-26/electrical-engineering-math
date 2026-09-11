"""Draw 2.1_currents.png: the phasors I1, I2, I3 and their sum Itot in the complex plane
(solution to 2.1 c). The dashed arrows show the addition, head to tail.

Usage: python3 2.1_currents.py (requires matplotlib). The image is written next to this script.
"""
import cmath
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

OUT = Path(__file__).with_suffix(".png")
AXIS = "#FFA500"
plt.rcParams.update({"font.size": 15, "axes.titlesize": 20, "axes.labelsize": 16})


def num(x, d=2):
    """Format a number with a decimal comma and a proper minus sign."""
    return f"{x:.{d}f}".replace(".", ",").replace("-", "−")


def rect(z):
    """Format z on rectangular form, a + jb."""
    sign = "+" if z.imag >= 0 else "−"
    return f"{num(z.real)} {sign} j{num(abs(z.imag))}"


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


# i1(t) = 5 sin(wt + 30°), i2(t) = 3 sin(wt - 30°), i3(t) = 4 sin(wt + 120°) mA.
I1 = cmath.rect(5, math.radians(30))
I2 = cmath.rect(3, math.radians(-30))
I3 = cmath.rect(4, math.radians(120))
Itot = I1 + I2 + I3

fig, ax = plt.subplots(figsize=(9, 7.8), dpi=150)
plane(ax, (-3.2, 8.4), (-2.4, 7.0), "Fasorerna I₁, I₂, I₃ och Iₜₒₜ (mA)")
# Head to tail, dashed: I1, then I3 from the tip of I1, then I2 from the tip of I1 + I3.
for a, b in ((I1, I1 + I3), (I1 + I3, Itot)):
    ax.annotate("", xy=(b.real, b.imag), xytext=(a.real, a.imag),
                arrowprops=dict(arrowstyle="-|>", color="#555555", lw=1.6, ls="--",
                                mutation_scale=14),
                zorder=2)
ax.text(3.45, 4.55, "I₃", color="#555555")
ax.text(3.75, 5.55, "I₂", color="#555555")
phasor(ax, I1, "#0072B2", f"I₁ = 5∠30° ≈ {rect(I1)}", offset=(10, -2))
phasor(ax, I2, "#D55E00", f"I₂ = 3∠−30° ≈ {rect(I2)}", offset=(10, -14))
phasor(ax, I3, "#CC79A7", f"I₃ = 4∠120° ≈ {rect(I3)}", offset=(-8, 10))
phasor(ax, Itot, "#009E73",
       f"Iₜₒₜ ≈ {rect(Itot)}\n        ≈ {num(abs(Itot))}∠"
       f"{num(math.degrees(cmath.phase(Itot)), 1)}°", lw=3.6, offset=(10, 2))
fig.tight_layout()
fig.savefig(OUT)
plt.close(fig)
