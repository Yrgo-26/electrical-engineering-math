# Bilaga A – Funktioner (del I)

## 1. Vad är en funktion?
En **funktion** $f$ är en regel som för varje tillåtet värde på $x$ ger exakt ett värde $f(x)$:

```math
f : x \mapsto f(x)
```

Funktioner kan representeras som algebraiska uttryck, tabeller eller grafer.

**Exempel:** $f(x) = 2x + 1$ ger $f(3) = 7$, $\thinspace f(-1) = -1$.

---

## 2. Definitionsmängd och värdemängd
**Definitionsmängden** $D_f$ är mängden av alla $x$-värden för vilka $f(x)$ är definierat.

**Värdemängden** $V_f$ är mängden av alla möjliga funktionsvärden $f(x)$.

| Funktion | Definitionsmängd | Värdemängd |
|----------|-----------------|------------|
| $f(x) = 2x + 3$ | $\mathbb{R}$ | $\mathbb{R}$ |
| $f(x) = x^2$ | $\mathbb{R}$ | $[0, \infty)$ |
| $f(x) = \sqrt{x}$ | $[0, \infty)$ | $[0, \infty)$ |
| $f(x) = \dfrac{1}{x}$ | $\mathbb{R} \setminus \lbrace 0\rbrace$ | $\mathbb{R} \setminus \lbrace 0\rbrace$ |

---

## 3. Vanliga funktionstyper

### Linjär funktion
```math
f(x) = kx + m
```
$k$ = lutning, $m$ = y-skärningspunkt.

### Potensfunktion
```math
f(x) = x^n
```

### Exponentialfunktion
```math
f(x) = C \cdot a^x, \quad a > 0,\, a \neq 1
```
* $a > 1$: växande funktion
* $0 < a < 1$: avtagande funktion
* $f(0) = C$ (startvärde)

### Exponentialekvationer
När det okända $x$ står i exponenten, till exempel $2^x = 8$, löser vi ekvationen med logaritmer. Vi använder två logaritmer, som båda finns på miniräknaren:
* $\log$ är tiologaritmen (basen $10$), så $\log 10 = 1$.
* $\ln$ är den naturliga logaritmen (basen $e \approx 2{,}718$), så $\ln e = 1$.

Nyckeln är logaritmlagen som flyttar ner exponenten framför logaritmen:

```math
\log(a^x) = x \cdot \log a, \qquad \ln(a^x) = x \cdot \ln a
```

**Exempel:** Lös ekvationen $2^x = 8$.

Logaritmera båda led med tiologaritmen:

```math
\log(2^x) = \log 8
```

Flytta ner exponenten:

```math
x \cdot \log 2 = \log 8
```

Dividera båda led med $\log 2$:

```math
x = \frac{\log 8}{\log 2} = 3
```

Kontroll: $2^3 = 8$. Allmänt gäller alltså att

```math
a^x = b \quad \Rightarrow \quad x = \frac{\log b}{\log a}
```

**OBS!** Samma logaritm måste användas i båda led. Det spelar ingen roll vilken: med $\ln$ blir svaret detsamma, $x = \frac{\ln 8}{\ln 2} = 3$. Däremot går det inte att blanda, till exempel $\frac{\log 8}{\ln 2}$.

**Basen $e$:** När basen är $e$ är $\ln$ enklast att använda, eftersom $\ln e = 1$:

```math
e^x = 5 \quad \Rightarrow \quad \ln(e^x) = \ln 5 \quad \Rightarrow \quad x \cdot \ln e = \ln 5 \quad \Rightarrow \quad x = \ln 5 \approx 1{,}61
```

Med $\log$ fungerar det också, $x = \frac{\log 5}{\log e} \approx 1{,}61$, men det blir krångligare.

### Polynomfunktion
```math
f(x) = a_n x^n + a_{n-1}x^{n-1} + \cdots + a_0
```

---

## 4. Att läsa en graf
Från en graf avläser man:
* Definitionsmängd (vilka $x$-värden som finns)
* Värdemängd (vilka $y$-värden som uppnås)
* Nollställen: $x$ där $f(x) = 0$
* Maximum- och minimumpunkter

---

## 5. Typexempel

### Typexempel 1 – Temperatursensor
Temperatursensorn `TMP36` ger temperaturen $f(x)$ (°C) som funktion av inspänningen $x$ (V):

```math
f(x) = 100x - 50, \quad 0 \leq x \leq 5\,\text{V}
```

**a)** Bestäm definitionsmängd och värdemängd.

**Lösning:** $D_f = [0, 5]\thinspace\text{V}$

```math
f(0) = -50\,°\text{C}, \quad f(5) = 450\,°\text{C} \quad \Rightarrow \quad V_f = [-50, 450]\,°\text{C}
```

**b)** Beräkna inspänningen när temperaturen är $30\thinspace°\text{C}$.

```math
100x - 50 = 30 \quad \Rightarrow \quad x = 0{,}8\,\text{V}
```

---

### Typexempel 2 – Linjär funktion från två punkter
En linjär funktion passerar genom $(1, 3)$ och $(3, 7)$. Bestäm funktionens ekvation $f(x) = kx + m$.

**Lösning:**

```math
k = \frac{7 - 3}{3 - 1} = 2
```

Sätt in $(1, 3)$: $m = 3 - 2 \cdot 1 = 1$

```math
f(x) = 2x + 1
```

---

### Typexempel 3 – Exponentialfunktion och tillväxt
En datamängd startar med $6 \times 10^6$ datapunkter och växer med 3 % per år:

```math
f(x) = 6 \times 10^6 \cdot 1{,}03^x
```

**a)** Beräkna $f(5)$.

```math
f(5) = 6 \times 10^6 \cdot 1{,}03^5 \approx 6{,}96 \times 10^6
```

**b)** När har datamängden fördubblats?

```math
1{,}03^x = 2 \quad \Rightarrow \quad x = \frac{\log 2}{\log 1{,}03} \approx 23{,}5\,\text{år}
```

---

## 6. Sammanfattning

| Begrepp | Förklaring |
|---------|-----------|
| Funktion | Varje $x$ ger exakt ett $f(x)$ |
| Definitionsmängd | Tillåtna $x$-värden |
| Värdemängd | Möjliga $f(x)$-värden |
| Linjär funktion | $f(x) = kx + m$ |
| Exponentialfunktion | $f(x) = C \cdot a^x$ |
| Exponentialekvation | $a^x = b \Rightarrow x = \frac{\log b}{\log a}$ |

---
