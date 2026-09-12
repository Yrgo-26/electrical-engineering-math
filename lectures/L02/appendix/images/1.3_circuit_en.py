"""Draw 1.3_circuit_en.png: the voltage divider of 1.3_circuit.png, with English labels.

Usage: python3 1.3_circuit_en.py (requires matplotlib and schemdraw). The image is written next
to this script. The drawing matches 1.3_circuit.png, which has no script of its own, to within a
few pixels; draw() takes the labels, so the Swedish ones (U_ut) give that figure back. The same
figure is 2.3_circuit.png in L03, drawn by a copy of this script.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import schemdraw
import schemdraw.elements as elm

OUT = Path(__file__).with_suffix(".png")
LABELS = {"in": r"$U_{in}$", "out": r"$U_{out}$"}


def draw(labels, out):
    """Draw the voltage divider with its output terminals, and save it as out."""
    with schemdraw.Drawing(show=False) as d:
        d.config(unit=2, fontsize=16, lw=2.4)
        # The label 0.1 up and 0.28 out from the source, as in the original.
        elm.SourceV().up().length(4).label(labels["in"], ofst=(0.1, 0.28))
        elm.Line().right().length(3)
        elm.ResistorIEC().down().label(r"$R_1$", loc="top")
        mid = elm.Dot()
        elm.ResistorIEC().down().label(r"$R_2$", loc="top")
        elm.Line().left().length(3)
        # The output, taken across R2.
        elm.Line().at(mid.center).right().length(2.6)
        elm.Dot(open=True)
        elm.Gap().down().length(2).label(["+", labels["out"], "$-$"])
        elm.Dot(open=True)
        elm.Line().left().length(2.6)
        elm.Ground().at((1.5, 0))
    d.save(str(out), dpi=200)


if __name__ == "__main__":
    draw(LABELS, OUT)
