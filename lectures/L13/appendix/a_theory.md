# Bilaga A – Derivata (del II)

## 1. Derivata för trigonometriska funktioner

| Funktion | Derivata |
|----------|----------|
| $\sin(x)$ | $\cos(x)$ |
| $\cos(x)$ | $-\sin(x)$ |
| $\sin(kx)$ | $k\cos(kx)$ |
| $\cos(kx)$ | $-k\sin(kx)$ |

**Exempel:**

```math
f(x) = 3\sin(2x) \quad \Rightarrow \quad f'(x) = 3 \cdot 2\cos(2x) = 6\cos(2x)
```

---

## 2. Derivata för exponentialfunktioner

| Funktion | Derivata |
|----------|----------|
| $e^x$ | $e^x$ |
| $e^{kx}$ | $k e^{kx}$ |
| $a^x$ | $a^x \ln a$ |

**Härledning av $\frac{d}{dx}e^x = e^x$:**

```math
\lim_{h \to 0} \frac{e^{x+h} - e^x}{h} = e^x \lim_{h \to 0} \frac{e^h - 1}{h} = e^x \cdot 1 = e^x
```

---

## 3. Derivata för logaritmfunktioner

| Funktion | Derivata |
|----------|----------|
| $\ln(x)$ | $\dfrac{1}{x}$ |
| $\ln(kx)$ | $\dfrac{1}{x}$ |
| $\log_{10}(x)$ | $\dfrac{1}{x \ln 10}$ |

**OBS!** $\ln(kx) = \ln k + \ln x$, vars derivata $= 1/x$ (konstanten $\ln k$ försvinner).

---

## 4. Produktregeln och kedjeregeln
Tabellerna ovan ger derivatan av en enskild funktion. När två funktioner multipliceras med varandra, eller när en funktion sätts in i en annan, behövs två regler till.

### Produktregeln
Derivatan av en produkt $f(x) = g(x) \cdot h(x)$ är

```math
f'(x) = g'(x) \cdot h(x) + g(x) \cdot h'(x)
```

Derivera alltså en faktor i taget medan den andra står kvar, och addera de två termerna.

**Exempel:** $f(x) = x^2 \sin(x)$ med $g(x) = x^2$ och $h(x) = \sin(x)$:

```math
f'(x) = 2x \cdot \sin(x) + x^2 \cdot \cos(x)
```

### Kedjeregeln
En sammansatt funktion $f(x) = g(u(x))$ består av en **yttre funktion** $g$ och en **inre funktion** $u(x)$. Derivatan är den yttre funktionens derivata, beräknad i den inre funktionen, gånger den inre funktionens derivata:

```math
f'(x) = g'(u(x)) \cdot u'(x)
```

**Exempel:** $f(x) = \ln(2x + 1)$ har den yttre funktionen $\ln u$ och den inre funktionen $u = 2x + 1$, med $u' = 2$:

```math
f'(x) = \frac{1}{2x + 1} \cdot 2 = \frac{2}{2x + 1}
```

Tabellraderna för $\sin(kx)$, $\cos(kx)$, $e^{kx}$ och $\ln(kx)$ ovan är specialfall av kedjeregeln, med den inre funktionen $u = kx$ och $u' = k$. Till exempel:

```math
\frac{d}{dx}\sin(kx) = \cos(kx) \cdot k = k\cos(kx), \qquad \frac{d}{dx}\ln(kx) = \frac{1}{kx} \cdot k = \frac{1}{x}
```

---

## 5. Samlad derivatatabell

| Funktion $f(x)$ | Derivata $f'(x)$ |
|-----------------|------------------|
| $x^n$ | $nx^{n-1}$ |
| $e^x$ | $e^x$ |
| $e^{kx}$ | $ke^{kx}$ |
| $\ln x$ | $1/x$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\sin(kx)$ | $k\cos(kx)$ |
| $\cos(kx)$ | $-k\sin(kx)$ |

---

## 6. Typexempel

### Typexempel 1 – Derivata av vanliga funktioner
Derivera:

**a)** $f(x) = 5e^{3x}$

**b)** $f(x) = \ln(4x)$

**c)** $f(x) = 2\cos(x) - 3\sin(x)$

**Lösning:**

**a)** $f'(x) = 5 \cdot 3e^{3x} = 15e^{3x}$

**b)** $f'(x) = 1/x$

**c)** $f'(x) = -2\sin(x) - 3\cos(x)$

---

### Typexempel 2 – Beräkna derivata i en punkt
Ström $i(t) = I_0 e^{-t/\tau}$ A beskriver urladdning av en kondensator. Beräkna $i'(0)$.

**Lösning:**

```math
i'(t) = -\frac{I_0}{\tau} e^{-t/\tau} \quad \Rightarrow \quad i'(0) = -\frac{I_0}{\tau}
```

$i'(0)$ är den momentana strömförändringshastigheten vid $t = 0$.

---

### Typexempel 3 – Stationär punkt för exponentialfunktion
Bestäm extrempunkten för $f(x) = xe^{-x}$.

**Lösning** (produktregeln, se avsnitt 4, med $g(x) = x$ och $h(x) = e^{-x}$):

```math
f'(x) = e^{-x} + x \cdot (-e^{-x}) = e^{-x}(1 - x)
```

$f'(x) = 0 \Rightarrow x = 1$ (ty $e^{-x} \neq 0$)

```math
f''(x) = -e^{-x}(1-x) + e^{-x}(-1) = e^{-x}(x - 2)
```

$f''(1) = e^{-1}(1-2) = -e^{-1} < 0$ → **maximum** vid $(1, e^{-1}) \approx (1, 0{,}37)$.

---

## 7. Sammanfattning

| Funktion | Derivata |
|----------|----------|
| $e^{kx}$ | $ke^{kx}$ |
| $\ln x$ | $1/x$ |
| $\sin(kx)$ | $k\cos(kx)$ |
| $\cos(kx)$ | $-k\sin(kx)$ |
| $g(x) \cdot h(x)$ | $g'(x) \cdot h(x) + g(x) \cdot h'(x)$ (produktregeln) |
| $g(u(x))$ | $g'(u(x)) \cdot u'(x)$ (kedjeregeln) |

---
