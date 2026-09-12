"""Draw 2.5_circuit_en.png: the transistor stage of 2.5_circuit.png, with English labels.

Usage: python3 2.5_circuit_en.py (requires matplotlib and schemdraw). The image is written next
to this script. The drawing follows 2.5_circuit.png, which has no script of its own, in style and
layout, but is 0.35 units wider: "control signal" is wider than "styr-signal", and would
otherwise run into the source.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import schemdraw
import schemdraw.elements as elm

OUT = Path(__file__).with_suffix(".png")
LABELS = {"ctrl": "control\nsignal"}


def draw(labels, out):
    """Draw the common-emitter stage with its control signal, and save it as out."""
    with schemdraw.Drawing(show=False) as d:
        d.config(unit=2, fontsize=16, lw=2.4)
        # The label offsets place each label where the original has it.
        elm.SourceV().up().length(5).label(r"$U_{CC}$", ofst=(0.1, 0.2))
        elm.Line().right().length(4.5)
        r = elm.ResistorIEC().down().label(r"$R_C$", loc="bot")
        elm.Arrow().at((r.start.x - 0.655, r.start.y - 0.43)).down().length(1.11).label(
            r"$I_C$", loc="top", ofst=(0.02, -0.14))
        elm.Line().at(r.end).down().length(0.1)
        q = elm.BjtNpn(circle=True).theta(0).anchor("collector")
        elm.Line().at(q.emitter).toy(0)
        elm.Line().tox(0)
        elm.Line().at(q.base).tox(q.base.x - 1.09)
        elm.Dot(open=True).label(labels["ctrl"], loc="left", halign="center", ofst=(-1.04, -0.1))
        elm.Gap().at((r.end.x + 0.625, r.end.y + 0.49)).toy(0.71).label(
            ["+", r"$U_{CE}$", "$-$"], halign="left")
        elm.Ground().at((2.25, 0))
    d.save(str(out), dpi=200)


if __name__ == "__main__":
    draw(LABELS, OUT)
