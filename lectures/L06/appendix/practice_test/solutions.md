# Övningsdugga 1 – Lösningsförslag

### Uppgift 1 (1,0 poäng)
$R_1 = 10\thinspace\text{k}\Omega$, $R = 4{,}5\thinspace\text{k}\Omega$

---

### Lösning
Vi härleder en formel för resistansen $R_2$. Vi skriver om högerledet med gemensam nämnare:

```math
\frac{1}{R_1} + \frac{1}{R_2} = \frac{R_2}{R_1 R_2} + \frac{R_1}{R_1 R_2} = \frac{R_1 + R_2}{R_1 R_2}
```

Vi sätter in detta i formeln för parallellresistans:

```math
\frac{1}{R} = \frac{R_1 + R_2}{R_1 R_2} \quad \Rightarrow \quad \frac{R_1 R_2}{R} = R_1 + R_2
```

Vi multiplicerar med $R$ i båda led:

```math
R_1 R_2 = R(R_1 + R_2) = RR_1 + RR_2
```

Vi samlar alla termer med $R_2$ i vänsterledet och bryter ut $R_2$:

```math
R_1 R_2 - RR_2 = RR_1 \quad \Rightarrow \quad R_2(R_1 - R) = RR_1
```

Vi dividerar med $(R_1 - R)$:

```math
R_2 = \frac{RR_1}{R_1 - R}
```

Slutligen sätter vi in värdena:

```math
R_2 = \frac{4{,}5\,\text{k} \times 10\,\text{k}}{10\,\text{k} - 4{,}5\,\text{k}} \approx 8{,}18\,\text{k}\Omega
```

Avrundat till en värdesiffra:

```math
R_2 \approx 8\,\text{k}\Omega
```

---

### Uppgift 2 (1,0 poäng)

```math
\dfrac{\dfrac{c^8 - c^4}{c^2}}{c(c^2 - 1)}
```

---

### Lösning
Vi förenklar täljaren först:

```math
\frac{c^8 - c^4}{c^2} = c^{8-2} - c^{4-2} = c^6 - c^2
```

Vi faktoriserar:

```math
c^6 - c^2 = c^2(c^4 - 1)
```

Uttrycket blir därmed:

```math
\frac{c^2(c^4-1)}{c(c^2-1)}
```

Vi förkortar $c^2/c = c$:

```math
\frac{c(c^4-1)}{c^2-1}
```

Vi faktoriserar täljaren med konjugatregeln, $c^4 - 1 = (c^2+1)(c^2-1)$, och förkortar bort $(c^2-1)$:

```math
\frac{c(c^2+1)(c^2-1)}{c^2-1} = c(c^2+1)
```

**Svar:**

```math
c(c^2+1) = c^3 + c
```

---

### Uppgift 3 (1,0 poäng)

```math
\begin{cases}
4y - 2x + 6 = 0 \\
3y = 5x + 4
\end{cases}
```

---

### Lösning
Vi löser den första ekvationen för $x$:

```math
4y - 2x + 6 = 0 \quad \Rightarrow \quad 2x = 4y + 6 \quad \Rightarrow \quad x = 2y + 3
```

Vi sätter in i den andra ekvationen:

```math
3y = 5(2y+3) + 4 = 10y + 15 + 4 = 10y + 19
```

```math
3y - 10y = 19 \quad \Rightarrow \quad -7y = 19 \quad \Rightarrow \quad y = -\frac{19}{7}
```

Vi sätter in $y$ i uttrycket för $x$:

```math
x = 2\left(-\frac{19}{7}\right) + 3 = -\frac{38}{7} + \frac{21}{7} = -\frac{17}{7}
```

**Svar:**

```math
x = -\frac{17}{7}, \quad y = -\frac{19}{7}
```

**Kontroll:** $4y - 2x + 6 = -\frac{76}{7} + \frac{34}{7} + 6 = -6 + 6 = 0$ ✓ och $3y = -\frac{57}{7} = 5x + 4 = -\frac{85}{7} + \frac{28}{7} = -\frac{57}{7}$ ✓

---

### Uppgift 4 (0,5 poäng)
Ekvationerna i Uppgift 3 är exempel på räta linjens ekvation. Ange den första ekvationens lutning $k$ samt m-värdet $m$.

---

### Lösning
Räta linjens ekvation har formen $y = kx + m$. Vi skriver om den första ekvationen $4y - 2x + 6 = 0$:

```math
4y = 2x - 6 \quad \Rightarrow \quad y = \frac{2x-6}{4} = 0{,}5x - 1{,}5
```

**Svar:** $k = 0{,}5, \quad m = -1{,}5$

---

### Uppgift 5 (0,5 poäng)

```math
P = RI^2, \quad R = 4{,}7\,\text{k}\Omega, \quad I = 2{,}5\,\text{mA}
```

---

### Lösning
Vi skriver prefixen som tiopotenser: $R = 4{,}7 \cdot 10^3\thinspace\Omega$ och $I = 2{,}5 \cdot 10^{-3}\thinspace\text{A}$. Strömmen kvadreras med potensreglerna, där $(10^{-3})^2 = 10^{-6}$:

```math
I^2 = (2{,}5 \cdot 10^{-3})^2 = 2{,}5^2 \cdot 10^{-6} = 6{,}25 \cdot 10^{-6}\,\text{A}^2
```

Insättning i effektformeln ger

```math
P = RI^2 = 4{,}7 \cdot 10^3 \cdot 6{,}25 \cdot 10^{-6} = 29{,}375 \cdot 10^{-3}\,\text{W}.
```

Indata har två värdesiffror, så svaret avrundas till två värdesiffror och skrivs på standardform:

```math
P \approx 2{,}9 \cdot 10^{-2}\,\text{W}
```

**Svar:** $P \approx 2{,}9 \cdot 10^{-2}\thinspace\text{W}$, dvs. cirka $29\thinspace\text{mW}$.

---

### Uppgift 6 (1,0 p)

```math
8(x + 2)^2 - 5(x - 3)^2 = 4 - 20x
```

---

### Lösning
Vi utvecklar respektive kvadrat:

```math
8(x+2)^2 = 8(x^2+4x+4) = 8x^2 + 32x + 32
```

```math
5(x-3)^2 = 5(x^2-6x+9) = 5x^2 - 30x + 45
```

Vänsterledet blir:

```math
8x^2 + 32x + 32 - (5x^2 - 30x + 45) = 3x^2 + 62x - 13
```

Vi sätter lika med högerledet och samlar allt i vänsterledet:

```math
3x^2 + 62x - 13 = 4 - 20x \quad \Rightarrow \quad 3x^2 + 82x - 17 = 0
```

Vi löser med ABC-formeln ($a=3$, $b=82$, $c=-17$):

```math
D = 82^2 - 4 \cdot 3 \cdot (-17) = 6724 + 204 = 6928
```

```math
x = \frac{-82 \pm \sqrt{6928}}{6} \approx \frac{-82 \pm 83{,}23}{6}
```

**Svar:**

```math
x_1 \approx 0{,}21, \quad x_2 \approx -27{,}54
```

**Kontroll ($x_1$):** Med det oavrundade värdet $x_1 = 0{,}20577\ldots$ blir VL $= 8(x_1+2)^2 - 5(x_1-3)^2 \approx -0{,}115$ och HL $= 4-20x_1 \approx -0{,}115$ ✓ (med det avrundade $0{,}21$ blir kontrollen missvisande, eftersom termerna i VL nästan tar ut varandra)

**Kontroll ($x_2$):** VL $= 8(-27{,}54+2)^2 - 5(-27{,}54-3)^2 \approx 554{,}8$, HL $= 4-20(-27{,}54) \approx 554{,}8$ ✓

---
