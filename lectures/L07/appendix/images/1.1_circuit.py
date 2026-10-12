"""Draw 1.1_circuit.png: a 12 V supply, a protective resistor and a sensor module in series.

Usage: python3 1.1_circuit.py (requires matplotlib and schemdraw). The images are written next
to this script: 1.1_circuit.png with Swedish labels and 1.1_circuit_en.png with English ones.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import schemdraw
import schemdraw.elements as elm

OUT = Path(__file__).with_suffix(".png")
# Output file -> label on the sensor module.
VARIANTS = {OUT: "Sensormodul", OUT.with_name(OUT.stem + "_en.png"): "Sensor module"}


def draw(out, module):
    """Draw the series circuit with the given label on the sensor module, and save it as out."""
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=16, lw=2.4)
        elm.SourceV().up().length(4.4).label("12 V")
        elm.Line().right().length(1)
        elm.RBox().right().label(r"4 k$\Omega$")
        wire = elm.Line().right().length(2.5)
        elm.CurrentLabel(top=True, ofst=0.3, length=1.4).at(wire).label("$I$")
        pins = [elm.IcPin(anchorname="plus", side="top"), elm.IcPin(anchorname="minus", side="bottom")]
        sensor = elm.Ic(pins=pins, size=(4.4, 2.2)).anchor("plus")
        sensor.label(f"{module}\n5 mW", loc="center")
        elm.Line().at(sensor.minus).down().toy(0)
        elm.Line().left().tox(0)
    d.save(str(out), dpi=200)


if __name__ == "__main__":
    for path, label in VARIANTS.items():
        draw(path, label)
