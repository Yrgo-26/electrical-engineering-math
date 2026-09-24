# L04 – Lösningsförslag

## Del 1 – Repetitionsuppgifter
### 1.1 – Ohms lag – sök spänning
$R = 47\thinspace\Omega$, $I = 0{,}2\thinspace\text{A}$

---

### Lösning
**a)**

```math
U = R \cdot I = 47 \times 0{,}2 = 9{,}4\,\text{V}
```

**b)**

```math
P = U \cdot I = 9{,}4 \times 0{,}2 = 1{,}88\,\text{W}
```

---

### 1.2 – Linjär ekvation i RC-krets
$\tau = 20\thinspace\text{ms} = 0{,}02\thinspace\text{s}$, $C = 10\thinspace\mu\text{F} = 10 \times 10^{-6}\thinspace\text{F}$

---

### Lösning
**a)** Ur $\tau = R \cdot C$:

```math
R = \frac{\tau}{C} = \frac{0{,}02}{10 \times 10^{-6}} = \frac{0{,}02}{10^{-5}} = 2\,000\,\Omega
```

**b)**

```math
R = 2\,000\,\Omega = 2\,\text{k}\Omega
```

---

### 1.3 – Olikhet
$U_{\text{ut}} = 5 U_{\text{in}} \leq 15\thinspace\text{V}$

---

### Lösning

```math
5 U_{\text{in}} \leq 15 \quad \Rightarrow \quad U_{\text{in}} \leq 3\,\text{V}
```

Insignalen får inte överstiga $3\thinspace\text{V}$.

---

## Del 2 – Nytt stoff
### 2.1 – Algebraiskt ekvationssystem

```math
\begin{cases}
3x + y = 11 \\
x - 2y = -2
\end{cases}
```

---

### Lösning
Vi använder **additionsmetoden**. Multiplicera ekvation (1) med $2$ och addera med ekvation (2):

```math
\begin{cases}
6x + 2y = 22 \\
x - 2y = -2
\end{cases}
```

Addera:

```math
7x = 20 \quad \Rightarrow \quad x = \frac{20}{7} \approx 2{,}86
```

Ur ekvation (1): $y = 11 - 3x = 11 - \dfrac{60}{7} = \dfrac{17}{7} \approx 2{,}43$

Kontroll i ekvation (2): $\dfrac{20}{7} - 2 \cdot \dfrac{17}{7} = \dfrac{20 - 34}{7} = -2$ ✓

---

### 2.2 – Strömsystem med KCL
KCL: $I_1 + I_2 = I_3 = 5\thinspace\text{A}$, samt $I_1 = 2 I_2$

---

### Lösning
**a)** Systemet är:

```math
\begin{cases}
I_1 + I_2 = 5 \\
I_1 = 2 I_2
\end{cases}
```

**b)** Substituera $I_1 = 2I_2$ i ekvation (1):

```math
2I_2 + I_2 = 5 \quad \Rightarrow \quad 3I_2 = 5 \quad \Rightarrow \quad I_2 = \frac{5}{3} \approx 1{,}67\,\text{A}
```

```math
I_1 = 2 \times \frac{5}{3} = \frac{10}{3} \approx 3{,}33\,\text{A}
```

Kontroll: $I_1 + I_2 = \dfrac{10}{3} + \dfrac{5}{3} = \dfrac{15}{3} = 5\thinspace\text{A}$ ✓

---

### 2.3 – Spänning och ström via KVL
$E = 12\thinspace\text{V}$, $U_2 = 3 U_1$

---

### Lösning
**a)** Systemet är:

```math
\begin{cases}
U_1 + U_2 = 12 \\
U_2 = 3 U_1
\end{cases}
```

**b)** Substituera $U_2 = 3 U_1$ i ekvation (1):

```math
U_1 + 3U_1 = 12 \quad \Rightarrow \quad 4U_1 = 12 \quad \Rightarrow \quad U_1 = 3\,\text{V}
```

```math
U_2 = 3 \times 3 = 9\,\text{V}
```

Kontroll: $U_1 + U_2 = 3 + 9 = 12\thinspace\text{V}$ ✓

**c)** Med $I = 2\thinspace\text{A}$ och Ohms lag $R = U/I$:

```math
R_1 = \frac{U_1}{I} = \frac{3}{2} = 1{,}5\,\Omega
```

```math
R_2 = \frac{U_2}{I} = \frac{9}{2} = 4{,}5\,\Omega
```

---

## Del 3 – Extrauppgifter
### 3.1 – Substitutionsmetoden

---

### Lösning
**a)** Ekvation (1) ger redan $y$ uttryckt i $x$. Sätt in i ekvation (2):

```math
3x + (2x + 1) = 11 \quad \Rightarrow \quad 5x = 10 \quad \Rightarrow \quad x = 2
```

```math
y = 2 \times 2 + 1 = 5
```

Kontroll: $3 \times 2 + 5 = 11$ ✓ Lösningen är $(x, y) = (2, 5)$.

**b)** Sätt in $x = 3y$ i ekvation (2):

```math
3y + 2y = 15 \quad \Rightarrow \quad 5y = 15 \quad \Rightarrow \quad y = 3
```

```math
x = 3 \times 3 = 9
```

Lösningen är $(x, y) = (9, 3)$.

**c)** Ur ekvation (1): $x = 10 - y$. Sätt in i ekvation (2):

```math
(10 - y) - y = 4 \quad \Rightarrow \quad 10 - 2y = 4 \quad \Rightarrow \quad y = 3
```

```math
x = 10 - 3 = 7
```

Lösningen är $(x, y) = (7, 3)$.

---

### 3.2 – Additionsmetoden

---

### Lösning
**a)** Termerna $+y$ och $-y$ tar ut varandra direkt. Addera ekvationerna:

```math
3x = 9 \quad \Rightarrow \quad x = 3
```

Ur ekvation (2): $y = x - 2 = 1$. Lösningen är $(3, 1)$.

**b)** Även här försvinner $y$ direkt vid addition:

```math
4x = 16 \quad \Rightarrow \quad x = 4
```

Ur ekvation (2): $2y = x = 4 \Rightarrow y = 2$. Lösningen är $(4, 2)$.

**c)** Multiplicera ekvation (2) med $3$ så att $y$-termerna blir motsatta:

```math
\begin{cases}
5x + 3y = 21 \\
6x - 3y = 12
\end{cases}
```

Addera:

```math
11x = 33 \quad \Rightarrow \quad x = 3
```

Ur ekvation (2): $y = 2x - 4 = 2$. Lösningen är $(3, 2)$.

**d)** Multiplicera ekvation (1) med $3$ och ekvation (2) med $4$:

```math
\begin{cases}
9x + 12y = 30 \\
8x - 12y = 4
\end{cases}
```

Addera:

```math
17x = 34 \quad \Rightarrow \quad x = 2
```

Ur ekvation (1): $4y = 10 - 3 \times 2 = 4 \Rightarrow y = 1$. Lösningen är $(2, 1)$.

Kontroll i ekvation (2): $2 \times 2 - 3 \times 1 = 1$ ✓

---

### 3.3 – Antal lösningar

---

### Lösning
**a)** Ekvation (2) är ekvation (1) multiplicerad med $2$. Linjerna **sammanfaller**, så systemet har **oändligt många lösningar** – varje punkt på linjen $x + y = 4$ duger.

**b)** Samma vänsterled men olika högerled. Summan $x + y$ kan inte vara både $4$ och $6$. Linjerna är **parallella** och systemet **saknar lösning**.

**c)** Linjerna har olika lutning och skär varandra i **exakt en punkt**. Addition ger:

```math
2x = 4 \quad \Rightarrow \quad x = 2, \quad y = 2
```

**d)** Multiplicera ekvation (2) med $-2$:

```math
2x - 4y = 6
```

Det är exakt ekvation (1). Linjerna **sammanfaller** och systemet har **oändligt många lösningar**.

En snabb tumregel: skriv båda ekvationerna på formen $ax + by = c$ och jämför. Är hela raderna proportionella sammanfaller linjerna; är bara vänsterleden proportionella är linjerna parallella.

---

### 3.4 – Grafisk tolkning
$y = 2x - 1$ och $y = -x + 5$

---

### Lösning
**a)** Värdetabell:

| $x$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|-----|-----|-----|-----|-----|-----|
| $y = 2x - 1$ | $-1$ | $1$ | $3$ | $5$ | $7$ |
| $y = -x + 5$ | $5$ | $4$ | $3$ | $2$ | $1$ |

**b)** Vid $x = 2$ ger båda uttrycken $y = 3$. Skärningspunkten är $(2, 3)$.

**c)** Sätt uttrycken lika:

```math
2x - 1 = -x + 5 \quad \Rightarrow \quad 3x = 6 \quad \Rightarrow \quad x = 2
```

```math
y = 2 \times 2 - 1 = 3
```

Samma svar som avläsningen ✓

**d)** Då skulle raderna aldrig få samma värde – differensen mellan dem vore konstant. Det motsvarar två parallella linjer, alltså linjer med samma lutning men olika skärning med $y$-axeln.

---

### 3.5 – System med bråk och decimaltal

---

### Lösning
**a)** Termerna $+y$ och $-y$ tar ut varandra vid addition:

```math
1{,}5x = 6 \quad \Rightarrow \quad x = 4
```

Ur ekvation (2): $y = x - 2 = 2$. Lösningen är $(4, 2)$.

Kontroll i ekvation (1): $0{,}5 \times 4 + 2 = 4$ ✓

**b)** Multiplicera ekvation (1) med den gemensamma nämnaren $6$:

```math
3x + 2y = 24
```

Ur ekvation (2): $x = y + 3$. Substituera:

```math
3(y + 3) + 2y = 24 \quad \Rightarrow \quad 5y + 9 = 24 \quad \Rightarrow \quad y = 3
```

```math
x = 3 + 3 = 6
```

Kontroll i ekvation (1): $\dfrac{6}{2} + \dfrac{3}{3} = 3 + 1 = 4$ ✓ Lösningen är $(6, 3)$.

---

### 3.6 – KCL i en nod
$I_3 = 12\thinspace\text{A}$, $I_1$ är $4\thinspace\text{A}$ större än $I_2$

---

### Lösning
**a)** KCL säger att summan in är lika med summan ut:

```math
\begin{cases}
I_1 + I_2 = 12 \\
I_1 - I_2 = 4
\end{cases}
```

**b)** Addera ekvationerna – $I_2$ försvinner:

```math
2I_1 = 16 \quad \Rightarrow \quad I_1 = 8\,\text{A}
```

```math
I_2 = 12 - 8 = 4\,\text{A}
```

**c)** Kontroll: $8 + 4 = 12$ ✓ och $8 - 4 = 4$ ✓

Att addera respektive subtrahera ekvationerna är den snabbaste vägen när systemet har formen "summa" och "differens".

---

### 3.7 – Strömdelning i en parallellkoppling
$U = 24\thinspace\text{V}$, $I = 3\thinspace\text{A}$, $I_1 = 2I_2$

---

### Lösning
**a)** KCL i noden plus det givna förhållandet:

```math
\begin{cases}
I_1 + I_2 = 3 \\
I_1 = 2I_2
\end{cases}
```

**b)** Substituera:

```math
2I_2 + I_2 = 3 \quad \Rightarrow \quad I_2 = 1\,\text{A}, \qquad I_1 = 2\,\text{A}
```

**c)** Båda motstånden har samma spänning $U = 24\thinspace\text{V}$ över sig:

```math
R_1 = \frac{24}{2} = 12\,\Omega, \qquad R_2 = \frac{24}{1} = 24\,\Omega
```

**d)** Produkt genom summa:

```math
R_1 // R_2 = \frac{12 \times 24}{12 + 24} = \frac{288}{36} = 8\,\Omega
```

```math
\frac{U}{I} = \frac{24}{3} = 8\,\Omega \quad ✓
```

Den gren som har dubbelt så stor ström har alltså hälften så stor resistans – strömmen tar den lättaste vägen.

---

### 3.8 – KVL i en seriekrets
$E = 15\thinspace\text{V}$, $U_1 = U_2 + 3$

---

### Lösning
**a)**

```math
\begin{cases}
U_1 + U_2 = 15 \\
U_1 - U_2 = 3
\end{cases}
```

**b)** Addera ekvationerna:

```math
2U_1 = 18 \quad \Rightarrow \quad U_1 = 9\,\text{V}, \qquad U_2 = 15 - 9 = 6\,\text{V}
```

**c)** Samma ström går genom båda motstånden i en seriekrets:

```math
R_1 = \frac{U_1}{I} = \frac{9}{0{,}3} = 30\,\Omega, \qquad R_2 = \frac{U_2}{I} = \frac{6}{0{,}3} = 20\,\Omega
```

**d)** Kontroll:

```math
R_1 + R_2 = 30 + 20 = 50\,\Omega, \qquad \frac{E}{I} = \frac{15}{0{,}3} = 50\,\Omega \quad ✓
```

---

### 3.9 – Arbetspunkt: källa och last
$U = 12 - 2I$ och $U = 4I$

---

### Lösning
**a)**

```math
\begin{cases}
U = 12 - 2I \\
U = 4I
\end{cases}
```

**b)** Båda leden är uttryck för samma $U$, så de kan sättas lika:

```math
4I = 12 - 2I \quad \Rightarrow \quad 6I = 12 \quad \Rightarrow \quad I = 2\,\text{A}
```

```math
U = 4 \times 2 = 8\,\text{V}
```

**c)** Kontroll: $12 - 2 \times 2 = 8\thinspace\text{V}$ ✓ och $4 \times 2 = 8\thinspace\text{V}$ ✓

**d)** Skärningspunkten kallas kretsens **arbetspunkt**. Den anger den enda kombination av ström och spänning som både källan kan leverera och lasten kan ta emot.

---

### 3.10 – Dimensionera en spänningsdelare
$R_1 + R_2 = 900\thinspace\Omega$, $U = 9\thinspace\text{V}$, $U_1 = 6\thinspace\text{V}$

---

### Lösning
**a)** Sätt in de kända värdena i spänningsdelningen:

```math
\frac{6}{9} = \frac{R_1}{900} \quad \Rightarrow \quad R_1 = \frac{2}{3} \times 900 = 600\,\Omega
```

Systemet är alltså:

```math
\begin{cases}
R_1 + R_2 = 900 \\
R_1 = 600
\end{cases}
```

**b)**

```math
R_2 = 900 - 600 = 300\,\Omega
```

**c)** Kontroll med spänningsdelarformeln:

```math
U_1 = 9 \times \frac{600}{600 + 300} = 9 \times \frac{2}{3} = 6\,\text{V} \quad ✓
```

Spänningen delas i förhållandet $2:1$, precis som resistanserna.

---

### 3.11 – System med tre obekanta

---

### Lösning
**a)** Börja med den enklaste ekvationen: $I_3 = 4$. Sätt in i ekvation (1):

```math
I_1 + I_2 + 4 = 9 \quad \Rightarrow \quad I_1 + I_2 = 5
```

Tillsammans med $I_1 - I_2 = 1$ ger addition:

```math
2I_1 = 6 \quad \Rightarrow \quad I_1 = 3\,\text{A}, \qquad I_2 = 2\,\text{A}
```

**b)** Kontroll: $3 + 2 + 4 = 9$ ✓, $3 - 2 = 1$ ✓ och $I_3 = 4$ ✓

**c)** Den tredje ekvationen ger direkt värdet på en obekant utan något räknearbete. Genom att sätta in den först reduceras systemet från tre till två obekanta, vilket är en välkänd metod: leta alltid efter den ekvation som är enklast att utnyttja.

---

### 3.12 – Ställ upp systemet ur en text

---

### Lösning
**a)** Låt $R_A$ och $R_B$ vara resistansen hos respektive typ. Seriekopplade resistanser adderas:

```math
\begin{cases}
5R_A + 3R_B = 4390 \\
2R_A + 4R_B = 3660
\end{cases}
```

**b)** Multiplicera ekvation (1) med $4$ och ekvation (2) med $3$:

```math
\begin{cases}
20R_A + 12R_B = 17\,560 \\
6R_A + 12R_B = 10\,980
\end{cases}
```

Subtrahera den andra från den första:

```math
14R_A = 6580 \quad \Rightarrow \quad R_A = 470\,\Omega
```

Ur ekvation (2):

```math
4R_B = 3660 - 2 \times 470 = 2720 \quad \Rightarrow \quad R_B = 680\,\Omega
```

**c)** Kontroll:

```math
5 \times 470 + 3 \times 680 = 2350 + 2040 = 4390 \quad ✓
```

```math
2 \times 470 + 4 \times 680 = 940 + 2720 = 3660 \quad ✓
```

Både $470\thinspace\Omega$ och $680\thinspace\Omega$ är standardvärden ur E-serien, vilket är en rimlighetskontroll i sig.

---

### 3.13 – Kontrollera en föreslagen lösning

---

### Lösning
**a)** $2 + 3 = 5$ ✓ och $2 \times 2 - 3 = 1$ ✓ – **ja**, $(2, 3)$ är en lösning.

**b)** $3 \times 1 + 4 = 7$ ✓ och $1 - 4 = -3$ ✓ – **ja**, $(1, 4)$ är en lösning.

**c)** $5 - 2 \times 1 = 3$ ✓ men $5 + 1 = 6 \neq 7$ ✗ – **nej**, $(5, 1)$ är inte en lösning.

**d)** Ett talpar som uppfyller den ena ekvationen ligger på den ena linjen. Lösningen till systemet måste ligga på **båda** linjerna samtidigt, alltså i skärningspunkten. Uppgift **c)** visar just detta: punkten ligger på den första linjen men inte på den andra.

---

### 3.14 – Blandade system

---

### Lösning
**a)** Ekvation (1) ger enkelt $y = 4x - 5$ – **substitution** passar:

```math
2x + 3(4x - 5) = 13 \quad \Rightarrow \quad 14x = 28 \quad \Rightarrow \quad x = 2
```

```math
y = 4 \times 2 - 5 = 3
```

Lösningen är $(2, 3)$.

**b)** Ekvation (1) ger $x = 1 - 3y$ – **substitution**:

```math
2(1 - 3y) - y = 9 \quad \Rightarrow \quad 2 - 7y = 9 \quad \Rightarrow \quad y = -1
```

```math
x = 1 - 3 \times (-1) = 4
```

Lösningen är $(4, -1)$.

**c)** Multiplicera ekvation (2) med $2$ och använd **additionsmetoden**:

```math
\begin{cases}
6x + 2y = 10 \\
6x - 2y = 14
\end{cases}
```

Addera:

```math
12x = 24 \quad \Rightarrow \quad x = 2
```

Ur ekvation (2): $y = 3 \times 2 - 7 = -1$. Lösningen är $(2, -1)$.

**d)** Substitutionsmetoden är smidigast när en variabel redan står ensam eller har koefficienten $1$, som i **a)** och **b)**. Additionsmetoden passar bäst när koefficienterna enkelt kan göras lika stora och motsatta, som i **c)**. Båda metoderna ger alltid samma svar – valet handlar bara om räknearbete.

---
