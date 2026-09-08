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

**a)** Bestäm $p(t)$.

**b)** Bestäm den primitiva funktionen $P(t)$ till $p(t)$.

**c)** Bestäm ett uttryck för energin i spolen $w(t)$ som en funktion av tiden.

**d)** Spolen är oladdad vid start, dvs. $w(0) = 0$. Bestäm integrationskonstanten $C$.

**e)** Bestäm hur mycket energi som har lagrats i spolen under de första $3$ sekunderna $(0{\le}\thinspace t\thinspace{\le}\thinspace 3)$.\

---

## Del 3 – Extrauppgifter
Uppgifterna nedan är extra träning och görs med fördel på egen hand efter lektionen. De flesta går att räkna i huvudet eller med papper och penna.

### 3.1 – Primitiva funktioner till polynom
Bestäm den primitiva funktionen:

**a)** $\displaystyle\int x^3\,dx$

**b)** $\displaystyle\int 4x\,dx$

**c)** $\displaystyle\int 5\,dx$

**d)** $\displaystyle\int (2x + 3)\,dx$

**e)** $\displaystyle\int (x^2 - 4x + 1)\,dx$

---

### 3.2 – Primitiva funktioner till övriga standardfunktioner
Bestäm den primitiva funktionen:

**a)** $\displaystyle\int e^x\,dx$

**b)** $\displaystyle\int e^{3x}\,dx$

**c)** $\displaystyle\int \frac{1}{x}\,dx$

**d)** $\displaystyle\int \sin(x)\,dx$

**e)** $\displaystyle\int \cos(2x)\,dx$

**f)** $\displaystyle\int \sin(4x)\,dx$

---

### 3.3 – Kontrollera genom derivering
**a)** Visa att $F(x) = \dfrac{x^3}{3}$ är en primitiv funktion till $f(x) = x^2$.

**b)** Visa att $F(x) = -\dfrac{\cos(2x)}{2}$ är en primitiv funktion till $f(x) = \sin(2x)$.

**c)** Visa att $F(t) = -2e^{-t/2}$ är en primitiv funktion till $f(t) = e^{-t/2}$.

**d)** Varför är svaret på en obestämd integral aldrig entydigt?

---

### 3.4 – Bestämda integraler: polynom
Beräkna:

**a)** $\displaystyle\int_0^2 3x^2\,dx$

**b)** $\displaystyle\int_1^3 2x\,dx$

**c)** $\displaystyle\int_0^4 (x + 1)\,dx$

**d)** $\displaystyle\int_{-1}^{1} x^2\,dx$

**e)** $\displaystyle\int_0^3 (6 - 2x)\,dx$

---

### 3.5 – Bestämda integraler: övriga funktioner
Beräkna:

**a)** $\displaystyle\int_0^1 e^x\,dx$

**b)** $\displaystyle\int_0^{\pi} \sin(x)\,dx$

**c)** $\displaystyle\int_0^{\pi/2} \cos(x)\,dx$

**d)** $\displaystyle\int_1^{e} \frac{1}{x}\,dx$

**e)** $\displaystyle\int_0^2 e^{-t}\,dt$

---

### 3.6 – Area under en kurva
**a)** Beräkna arean under $f(x) = x$ för $0 \leq x \leq 4$.

**b)** Kontrollera svaret i **a)** med formeln för en triangels area.

**c)** Beräkna arean under $f(x) = 3$ för $1 \leq x \leq 5$ och kontrollera med en rektangel.

**d)** Beräkna arean under $f(x) = x^2$ för $0 \leq x \leq 2$.

---

### 3.7 – Negativa areor
Funktionen $f(x) = x - 2$ är given.

**a)** Beräkna $\displaystyle\int_0^2 (x-2)\,dx$.

**b)** Beräkna $\displaystyle\int_2^4 (x-2)\,dx$.

**c)** Beräkna $\displaystyle\int_0^4 (x-2)\,dx$.

**d)** Förklara varför integralen i **c)** blir noll trots att kurvan inte ligger på x-axeln.

---

### 3.8 – Integrationskonstant med startvillkor
Det är känt att $f'(x) = 4x - 3$ och att $f(0) = 5$.

**a)** Bestäm den allmänna primitiva funktionen.

**b)** Bestäm integrationskonstanten $C$.

**c)** Skriv upp $f(x)$.

**d)** Beräkna $f(2)$.

---

### 3.9 – Spänning ur förändringshastighet
Spänningen över en kondensator ändras med $u'(t) = 6t$ V/s, och vid start gäller $u(0) = 2\thinspace\text{V}$.

**a)** Bestäm den allmänna primitiva funktionen.

**b)** Bestäm integrationskonstanten.

**c)** Skriv upp $u(t)$.

**d)** Beräkna $u(4)$.

---

### 3.10 – Laddning ur ström
Strömmen genom en ledare ges av $i(t) = 4t + 2$ ampere, och $q(0) = 0$.

**a)** Bestäm ett uttryck för laddningen $q(t)$.

**b)** Beräkna $q(3)$.

**c)** Beräkna $q(5)$.

**d)** Hur stor laddning passerar mellan $t = 3\thinspace\text{s}$ och $t = 5\thinspace\text{s}$?

**e)** Kontrollera svaret i **d)** genom att beräkna $\displaystyle\int_3^5 i(t)\,dt$.

---

### 3.11 – Laddning ur en sinusström
Strömmen ges av $i(t) = 2\sin(100\pi t)$ ampere.

**a)** Bestäm den primitiva funktionen till $i(t)$.

**b)** Beräkna $\displaystyle\int_0^{0{,}01} i(t)\,dt$.

**c)** Beräkna $\displaystyle\int_0^{0{,}02} i(t)\,dt$.

**d)** Förklara resultatet i **c)**.

---

### 3.12 – Energi lagrad i en spole
Strömmen genom en spole med $L = 0{,}4\thinspace\text{H}$ ges av $i(t) = 3t$ ampere. Effekten ges av $p(t) = L\,i(t)\,i'(t)$.

**a)** Bestäm $i'(t)$.

**b)** Bestäm $p(t)$.

**c)** Bestäm energin $w(t) = \displaystyle\int_0^t p(\tau)\,d\tau$.

**d)** Beräkna energin efter $2$ sekunder.

**e)** Kontrollera svaret med formeln $w = \dfrac{Li^2}{2}$.

---

### 3.13 – Energi utvecklad i ett motstånd
Effekten i ett motstånd ges av $p(t) = 5 + 2t$ watt för $0 \leq t \leq 10\thinspace\text{s}$.

**a)** Bestäm energin $w(t) = \displaystyle\int_0^t p(\tau)\,d\tau$.

**b)** Beräkna den totala energin efter $10$ sekunder.

**c)** Hur mycket energi utvecklas under de sista $5$ sekunderna?

**d)** Beräkna medeleffekten under hela intervallet.

---

### 3.14 – Medelvärde av en funktion
Medelvärdet av $f$ över intervallet $[a, b]$ ges av $\dfrac{1}{b-a}\displaystyle\int_a^b f(x)\,dx$.

**a)** Beräkna medelvärdet av $f(x) = x^2$ över $[0, 3]$.

**b)** Beräkna medelvärdet av $f(x) = 4$ över $[1, 5]$.

**c)** Beräkna medelvärdet av $i(t) = 10\sin(100\pi t)$ över en halv period, $[0;\thinspace 0{,}01]$.

**d)** Hur stor andel av amplituden är medelvärdet i **c)**?

---

### 3.15 – Integralens räkneregler
Det är känt att $\displaystyle\int_0^2 f(x)\,dx = 5$ och $\displaystyle\int_0^2 g(x)\,dx = 3$. Beräkna:

**a)** $\displaystyle\int_0^2 \left[f(x) + g(x)\right]dx$

**b)** $\displaystyle\int_0^2 2f(x)\,dx$

**c)** $\displaystyle\int_0^2 \left[3f(x) - 2g(x)\right]dx$

**d)** $\displaystyle\int_2^0 f(x)\,dx$

---

### 3.16 – Derivering och integrering som motsatser
**a)** Derivera $F(x) = x^3 - 2x$.

**b)** Integrera resultatet från **a)**.

**c)** Varför dyker det upp en konstant i **b)** som inte fanns i $F(x)$?

**d)** Beräkna $\dfrac{d}{dx}\left[\displaystyle\int 5x^4\,dx\right]$.

---

### 3.17 – Bestäm en okänd gräns eller konstant
**a)** Bestäm $a$ så att $\displaystyle\int_0^a 2x\,dx = 25$.

**b)** Bestäm $a$ så att $\displaystyle\int_0^a 3\,dx = 12$.

**c)** Bestäm $k$ så att $\displaystyle\int_0^2 kx\,dx = 10$.

**d)** En kondensator laddas med den konstanta strömmen $i = 0{,}5\thinspace\text{A}$. Efter hur lång tid har laddningen $2\thinspace\text{C}$ passerat?

---

### 3.18 – Hitta felet
Varje rad innehåller ett vanligt fel. Förklara felet och ange det korrekta svaret.

**a)** $\displaystyle\int x^2\,dx = 2x + C$

**b)** $\displaystyle\int e^{2x}\,dx = 2e^{2x} + C$

**c)** $\displaystyle\int \sin(x)\,dx = \cos(x) + C$

**d)** $\displaystyle\int_1^2 3x^2\,dx = \left[x^3\right]_1^2 = 8$

**e)** En bestämd integral behöver en integrationskonstant.

**f)** $\displaystyle\int \frac{1}{x}\,dx = \ln x + C$ gäller för alla $x \neq 0$.

---
