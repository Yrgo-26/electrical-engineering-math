# L14 - Lektionsuppgifter

## Del 1 - Repetitionsuppgifter

### 1.1 - Deriveringsregler

Derivera följande funktioner:
* **a)** $f_1(x) = x^2 * e^{4x}$
* **b)** $f_2(x) = x^3 * \ln 2x$
* **c)** $f_3(x) = \frac{x^3}{\ln x^2}$

## Del 2 - Nytt stoff

### 2.1 - Energi lagrad i en spole
Strömmen genom en spole är tidsberoende och ges av följande funktion:

```math
i(t) = 5t,
```

där $t$ = tiden i sekunder. Strömmen mäts i $A$ $(Ampere)$.

Spolens induktans $L = 0,20$ $H$ $(Henry)$.

Effektutvecklingen $p(t)$ i spolen ges av följande funktion:

```math
p(t) = L * i(t) * i'(t),
```

där
* p(t) = effektutvecklingen i $W$ $(Watt)$,
* $L$ = spolens induktans i $H$ $(Henry)$,
* $i(t)$ = strömmen genom spolen i $A$ $(Ampere)$,
* $i'(t)$ = strömförändringen genom spolen i $A/s$.

Energin $w(t)$ som lagras i spolen mellan tiden $0 - t$ ges av följande funktion:

```math
w(t) = \int_0^t p(t)\,dt
```

Energin mäts i $J$ $(Joule)$.

**a)** Bestäm $p(t)$.\
**b)** Bestäm den primitiva funktionen $P(t)$ till $p(t)$.\
**c)** Bestäm ett uttryck för energin i spolen $w(t)$ som en funktion av tiden.\
**d)** Spolen är oladdad vid start, dvs. $w(0) = 0$. Bestäm integrationskonstanten $C$.\
**e)** Bestäm hur mycket energi som har lagrats i spolen under de första $3$ sekunderna $(0{\le}\,t\,{\le}\,3)$.\

---
