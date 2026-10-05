"""Draw 1.4_circuit.png: an MCU with eight digital pins, with LEDs on D2 and D6.

Usage: python3 1.4_circuit.py (requires matplotlib and schemdraw). The image is written next
to this script. The labels are the same in Swedish and English, so there is no _en variant.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import schemdraw
import schemdraw.elements as elm

OUT = Path(__file__).with_suffix(".png")
PINS = 8
# Pin number -> (resistor label, LED label).
LEDS = {2: ("$R_1$", "LED1"), 6: ("$R_2$", "LED2")}


def draw(out):
    """Draw the MCU with a resistor and an LED to ground on each pin in LEDS, and save it as out."""
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=16, lw=2.4)
        # D0 at the top, as the pins are listed from the bottom up.
        pins = [elm.IcPin(name=f"D{n}", side="right") for n in reversed(range(PINS))]
        mcu = elm.Ic(pins=pins, size=(3, 7.2), pinspacing=0.8).label("MCU", loc="center")
        for n, (resistor, led) in LEDS.items():
            elm.Resistor().at(getattr(mcu, f"D{n}")).right().label(resistor)
            elm.LED().right().label(led)
            elm.Line().down().length(0.8)
            elm.Ground()
    d.save(str(out), dpi=200)


if __name__ == "__main__":
    draw(OUT)
