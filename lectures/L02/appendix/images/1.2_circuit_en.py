"""Draw 1.2_circuit_en.png: the transformer of 1.2_circuit.png, with English labels.

Usage: python3 1.2_circuit_en.py (requires matplotlib and schemdraw). The image is written next
to this script. The drawing matches 1.2_circuit.png, which has no script of its own, to within a
few pixels; draw() takes the labels, so the Swedish ones (P_ut, P_förl) give that figure back.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import schemdraw
import schemdraw.elements as elm

OUT = Path(__file__).with_suffix(".png")
LABELS = {"in": r"$P_\mathrm{in}$", "out": r"$P_\mathrm{out}$", "loss": r"$P_\mathrm{loss}$"}


def draw(labels, out):
    """Draw the transformer with the power flowing in, out and lost, and save it as out."""
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=16, lw=2.4)
        t = elm.Transformer(t1=4, t2=4, core=True)
        # Each winding's two leads, ending in terminals.
        for anchor, dx in ((t.p1, -2), (t.p2, -2), (t.s1, 2), (t.s2, 2)):
            elm.Line().at(anchor).to((anchor.x + dx, anchor.y))
            elm.Dot(open=True)
        core = (t.p1.x + t.s1.x) / 2
        top = t.p1.y + 0.78
        elm.Arrow().at((core - 2.40, top)).right().length(1.2).label(labels["in"])
        elm.Arrow().at((core + 1.20, top)).right().length(1.2).label(labels["out"])
        elm.Arrow().at((core, t.p2.y - 0.5)).down().length(1.10).label(labels["loss"], loc="bot")
    d.save(str(out), dpi=200)


if __name__ == "__main__":
    draw(LABELS, OUT)
