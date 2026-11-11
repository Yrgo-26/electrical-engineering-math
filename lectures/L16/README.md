# L16 – Komplexa tal (del II)

## Dagordning
* Eulers formel.
* Fasorer: sinusformade signaler som komplexa tal.

---

## Mål med lektionen
* Förstå Eulers formel.
* Känna till skillnaden mellan en komplex storhet och en fasor.
* Kunna multiplicera och dividera komplexa tal på Eulerform.

---

## Instruktioner

### Innan lektionen
* Vänligen läs följande litteratur:
    * [Eulers formel](https://sv.wikipedia.org/wiki/Eulers_formel)
* Läs igenom kursmaterialet i [bilaga A](./appendix/a_theory.md) eller kapitel 16 i boken ([svenska](../../book/elteknisk-matematik.pdf) eller [engelska](../../book/electrical-engineering-mathematics.pdf)).

### Under lektionen
* Närvara under genomgången.
* Genomför lektionsuppgifterna i Del 1 och Del 2 i [bilaga B](./appendix/b_exercises.md):
    * Ni får några minuter på er att genomföra respektive uppgift, därefter sker genomgång i helklass.
    * Lösningsförslag laddas upp efter lektionen.

### Efter lektionen
* Extrauppgifterna i Del 3 i [bilaga B](./appendix/b_exercises.md) är frivillig träning på egen hand.
* Hinns uppgiften i Del 4 (matematik i C) inte med under lektionen kan du göra den på egen hand, se [bilaga B](./appendix/b_exercises.md).
* **Inför laborationen i L18:** installera **WSL** med `gcc` och `make` och klona kursens repository, enligt [`L18/code/README.md`](../L18/code/README.md#kompilering-på-egen-dator-rekommenderat) och avsnittet *Arbeta i WSL* i [L18:s bilaga B](../L18/appendix/b_exercises.md#arbeta-i-wsl-rekommenderat). Gör det i god tid: uppstår problem, till exempel saknade administratörsrättigheter eller avstängd virtualisering, hinner de lösas före laborationen.

---

## Demonstration
* Multiplikation på Eulerform: $2e^{j\pi/6} \cdot 3e^{j\pi/4}$, och omskrivning av svaret till rektangulär form.
* Omskrivning av $u(t) = 3e^{j(100\pi t - \frac{\pi}{4})}\thinspace\text{V}$ till rektangulär form.
* Omskrivning av fasor $I = 5 - j4\thinspace\text{mA}$ till komplex ström $i(t)$ på Eulers form.
* Rotation med $j$ i C, se uppgift 4.1 i [bilaga B](./appendix/b_exercises.md) (om tiden räcker).

---

## Utvärdering
* Skriv $Z = 10\thinspace\angle\thinspace\pi/6$ på rektangulär form.
* Vad händer geometriskt med ett komplext tal när det multipliceras med $2e^{j\pi/6}$?

---

## Nästa lektion
* Komplexa tal för beräkningar med sinusformade signaler.

---
