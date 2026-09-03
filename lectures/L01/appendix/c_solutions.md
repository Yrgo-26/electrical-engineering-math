# L01 – Lösningsförslag

## Del 1 – Inledande uppgifter
### 1.1 – Beräkningar med räkneordning
**a)** $3 + 2 \times 5$\
**b)** $(3 + 2) \times 5$\
**c)** $12 - 4 \times 2 + 1$\
**d)** $\dfrac{10 + 2}{3} \times 4 - 1$

---

### Lösning
**a)** Multiplikation före addition:

```math
3 + 2 \times 5 = 3 + 10 = 13
```

**b)** Parentesen beräknas först:

```math
(3 + 2) \times 5 = 5 \times 5 = 25
```

**c)** Multiplikation före addition och subtraktion:

```math
12 - 4 \times 2 + 1 = 12 - 8 + 1 = 5
```

**d)** Täljaren i bråket beräknas som en parentes, sedan multipliceras och subtraheras:

```math
\frac{10 + 2}{3} \times 4 - 1 = \frac{12}{3} \times 4 - 1 = 4 \times 4 - 1 = 16 - 1 = 15
```

---

### 1.2 – Bråkräkning
**a)** $\dfrac{1}{4} + \dfrac{1}{6}$


**b)** $\dfrac{3}{5} - \dfrac{1}{4}$


**c)** $\dfrac{2}{3} \times \dfrac{9}{4}$


**d)** $\dfrac{5}{6} \div \dfrac{5}{12}$

---

### Lösning
**a)** Gemensam nämnare är $12$:

```math
\frac{1}{4} + \frac{1}{6} = \frac{3}{12} + \frac{2}{12} = \frac{5}{12}
```

**b)** Gemensam nämnare är $20$:

```math
\frac{3}{5} - \frac{1}{4} = \frac{12}{20} - \frac{5}{20} = \frac{7}{20}
```

**c)** Täljare × täljare, nämnare × nämnare, sedan förkortas:

```math
\frac{2}{3} \times \frac{9}{4} = \frac{18}{12} = \frac{3}{2} = 1{,}5
```

**d)** Division = multiplikation med reciproken:

```math
\frac{5}{6} \div \frac{5}{12} = \frac{5}{6} \times \frac{12}{5} = \frac{60}{30} = 2
```

---

### 1.3 – Procenträkning
**a)** $40\%$ av $250$\
**b)** Vilket procenttal är $18$ av $72$?\
**c)** Resistor $100\,\Omega$ med tolerans $\pm 5\%$

---

### Lösning
**a)**

```math
\frac{40}{100} \times 250 = 0{,}4 \times 250 = 100
```

**b)**

```math
\frac{18}{72} \times 100\% = 0{,}25 \times 100\% = 25\%
```

**c)** $5\%$ av $100\,\Omega$ är $5\,\Omega$. Det tillåtna intervallet är:

```math
100 - 5 = 95\,\Omega \quad \text{till} \quad 100 + 5 = 105\,\Omega
```

---

## Del 2 – Nytt stoff
### 2.1 – Parallellkopplade motstånd
$R_1 = 12\,\Omega$, $R_2 = 6\,\Omega$

---

### Lösning
**a)**

```math
\frac{1}{R_{\text{TOT}}} = \frac{1}{12} + \frac{1}{6} = \frac{1}{12} + \frac{2}{12} = \frac{3}{12} = \frac{1}{4}
```

**b)**

```math
R_{\text{TOT}} = 4\,\Omega
```

---

### 2.2 – Serie- och parallellkoppling
$R_1 = 4\,\text{k}\Omega$ i serie med parallellkopplingen av $R_2 = 24\,\text{k}\Omega$ och $R_3 = 8\,\text{k}\Omega$.

---

### Lösning
Kretsen förenklas i två steg: först ersätts parallellkopplingen med $R_{\text{p}}$, därefter adderas $R_1$.

![](./images/circuit_simplification.png)

**a)** Med den första formeln är gemensam nämnare $24$:

```math
\frac{1}{R_{\text{p}}} = \frac{1}{24} + \frac{1}{8} = \frac{1}{24} + \frac{3}{24} = \frac{4}{24} = \frac{1}{6}
\quad \Rightarrow \quad
R_{\text{p}} = 6\,\text{k}\Omega
```

Med den andra formeln fås samma svar:

```math
R_{\text{p}} = \frac{R_2 \times R_3}{R_2 + R_3} = \frac{24 \times 8}{24 + 8} = \frac{192}{32} = 6\,\text{k}\Omega
```

**b)** Seriekopplade resistanser adderas:

```math
R_{\text{TOT}} = R_1 + R_{\text{p}} = 4 + 6 = 10\,\text{k}\Omega
```

**c)** Parallellkopplingen är en egen delberäkning och fungerar som en parentes i uttrycket:

```math
R_{\text{TOT}} = R_1 + \left( \frac{R_2 \times R_3}{R_2 + R_3} \right)
```

Additionen kan inte utföras förrän parentesens värde är känt – precis som att parenteser beräknas före addition i räkneordningen. Adderas alla tre resistanserna direkt fås $36\,\text{k}\Omega$, vilket är fel.

---

### 2.3 – Ström och spänning i kretsen
$U = 20\,\text{V}$ över kretsen i uppgift 2.2, där $R_{\text{TOT}} = 10\,\text{k}\Omega$.

---

### Lösning
**a)** Ohms lag löst för $I$. Resistansen är i k$\Omega$ och spänningen i V, så strömmen fås i mA:

```math
I = \frac{U}{R_{\text{TOT}}} = \frac{20}{10} = 2\,\text{mA}
```

**b)** Hela strömmen går genom $R_1$:

```math
U_1 = R_1 \times I = 4 \times 2 = 8\,\text{V}
```

**c)** Resten av matningsspänningen ligger över parallellkopplingen:

```math
U_{\text{p}} = U - U_1 = 20 - 8 = 12\,\text{V}
```

Kontroll med $R_{\text{p}}$: $U_{\text{p}} = 6 \times 2 = 12\,\text{V}$.

**d)** Båda motstånden har samma spänning $U_{\text{p}}$ över sig:

```math
I_2 = \frac{U_{\text{p}}}{R_2} = \frac{12}{24} = 0{,}5\,\text{mA}
\qquad
I_3 = \frac{U_{\text{p}}}{R_3} = \frac{12}{8} = 1{,}5\,\text{mA}
```

Kontroll: $I_2 + I_3 = 0{,}5 + 1{,}5 = 2\,\text{mA} = I$. Strömmen in i parallellkopplingen är alltså lika stor som summan av strömmarna ut ur den.

---

### 2.4 – Absolutbelopp
Växelspänning varierar mellan $-8\,\text{V}$ och $+8\,\text{V}$.

---

### Lösning
**a)** Amplituden är det maximala utslaget från noll:

```math
|U| = 8\,\text{V}
```

**b)**

```math
|u(t)| = |-5{,}3| = 5{,}3\,\text{V}
```

---

### 2.5 – Verkningsgrad
$P_{\text{in}} = 24\,\text{W}$, $P_{\text{ut}} = 18\,\text{W}$

---

### Lösning
**a)**

```math
\eta = \frac{P_{\text{ut}}}{P_{\text{in}}} \times 100\% = \frac{18}{24} \times 100\% = 75\%
```

**b)** Med $\eta = 90\%$ och $P_{\text{in}} = 24\,\text{W}$:

```math
P_{\text{ut}} = 0{,}90 \times 24 = 21{,}6\,\text{W}
```

---

### 2.6 – Talmängder

---

### Lösning
**a)** $7 \in \mathbb{N}$ (naturligt tal)\
**b)** $-3 \in \mathbb{Z}$ (heltal, ej naturligt)\
**c)** $\dfrac{3}{4} \in \mathbb{Q}$ (rationellt tal)\
**d)** $\sqrt{2}$ – irrationellt tal\
**e)** $0{,}25 = \dfrac{1}{4} \in \mathbb{Q}$ (rationellt tal)\
**f)** $\pi$ – irrationellt tal

---
