"""Draw 1.1_vectors.png: the phasors U = (4; -1) V and I = (-3; 4) A in a coordinate system.

Usage: python3 1.1_vectors.py (requires matplotlib). The image is written next to this script.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).with_suffix(".png")
# Phasor name -> (coordinates, color).
VECTORS = {"U": ((4, -1), "#d03c3c"), "I": ((-3, 4), "#6040b0")}


def draw(out):
    """Draw the phasors from the origin in a grid from -5 to 5, and save the figure as out."""
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-5.5, 5.5)
    ax.set_aspect("equal")
    ax.set_xticks(range(-5, 6))
    ax.set_yticks(range(-5, 6))
    ax.set_xticklabels([str(x) if x in (-5, 5) else "" for x in range(-5, 6)], fontsize=13)
    ax.set_yticklabels([str(y) if y in (-5, 5) else "" for y in range(-5, 6)], fontsize=13)
    ax.grid(color="#d0d0d0", lw=0.8)
    ax.axhline(0, color="black", lw=1.6)
    ax.axvline(0, color="black", lw=1.6)
    ax.text(-0.15, -0.15, "0", fontsize=13, ha="right", va="top")
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(length=0)

    for name, ((x, y), color) in VECTORS.items():
        ax.annotate("", xy=(x, y), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=2.5, mutation_scale=20))
        ax.text(x + 0.25 * (1 if x > 0 else -1), y + (0.3 if y > 0 else -0.3), rf"$\mathbf{{{name}}}$",
                fontsize=18, ha="center", va="bottom" if y > 0 else "top")
    fig.savefig(out, dpi=100, bbox_inches="tight")


if __name__ == "__main__":
    draw(OUT)
