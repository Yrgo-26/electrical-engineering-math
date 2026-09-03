# L17 – Komplexa tal (del III)

## Dagordning
* Komplexa tal för beräkningar med sinusformade signaler.

---

## Mål med lektionen
* Förstå hur komplexa tal kan användas för beräkningar med sinusformade signaler.

---

## Instruktioner

### Innan lektionen
* Läs igenom kursmaterialet i [bilaga A](./appendix/a_theory.md).

### Under lektionen
* Närvara under genomgången.
* Genomför lektionsuppgifterna i [bilaga B](./appendix/b_exercises.md):
    * Ni får några minuter på er att genomföra respektive uppgift, därefter sker genomgång i helklass.
    * Lösningsförslag laddas upp efter lektionen.

---

## Demonstration
* Fasoraddition med två sinusspänningar:

```math
u_1(t) = 2\sin(\omega t + 45^{\circ})\,\text{V}
```

```math
u_2(t) = 3\sin(\omega t - 60^{\circ})\,\text{V}
```

* Detta innefattar:
    * Omvandling av $u_1(t)$ och $u_2(t)$ till motsvarande fasorer $U_1$ och $U_2$.
    * Summering av fasorerna i komplex form: $U_{tot} = U_1 + U_2$.
    * Ritande av fasorerna i det komplexa talplanet.
    * Omvandling tillbaka till tidsdomänen: $U_{tot} \rightarrow u_{tot}(t)$.

---

## Utvärdering
* En ström ges av $i(t) = 5\sin(100\pi t + \pi/3)\,\text{A}$. Ange motsvarande fasor $I$ i polär form.
* Addera fasorerna $U_1 = 4\,\angle\,0$ och $U_2 = 3\,\angle\,\pi/2$. Ange summan i polär form.

---

## Nästa lektion
* Laboration – Matematik i C med math.h.

---
