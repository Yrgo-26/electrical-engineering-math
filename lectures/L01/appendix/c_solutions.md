# L01 – Lösningsförslag

## Del 1 – Inledande uppgifter
### 1.1 – Beräkningar med räkneordning
**a)** $3 + 2 \times 5$

**b)** $(3 + 2) \times 5$

**c)** $12 - 4 \times 2 + 1$

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
**a)** $40\char37$ av $250$

**b)** Vilket procenttal är $18$ av $72$?

**c)** Resistor $100\thinspace\Omega$ med tolerans $\pm 5\char37$

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

**c)** $5\char37$ av $100\thinspace\Omega$ är $5\thinspace\Omega$. Det tillåtna intervallet är:

```math
100 - 5 = 95\,\Omega \quad \text{till} \quad 100 + 5 = 105\,\Omega
```

---

## Del 2 – Nytt stoff
### 2.1 – Parallellkopplade motstånd
$R_1 = 12\thinspace\Omega$, $R_2 = 6\thinspace\Omega$

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
$R_1 = 4\thinspace\text{k}\Omega$ i serie med parallellkopplingen av $R_2 = 24\thinspace\text{k}\Omega$ och $R_3 = 8\thinspace\text{k}\Omega$.

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

Additionen kan inte utföras förrän parentesens värde är känt – precis som att parenteser beräknas före addition i räkneordningen. Adderas alla tre resistanserna direkt fås $36\thinspace\text{k}\Omega$, vilket är fel.

---

### 2.3 – Ström och spänning i kretsen
$U = 20\thinspace\text{V}$ över kretsen i uppgift 2.2, där $R_{\text{TOT}} = 10\thinspace\text{k}\Omega$.

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

Kontroll med $R_{\text{p}}$: $U_{\text{p}} = 6 \times 2 = 12\thinspace\text{V}$.

**d)** Båda motstånden har samma spänning $U_{\text{p}}$ över sig:

```math
I_2 = \frac{U_{\text{p}}}{R_2} = \frac{12}{24} = 0{,}5\,\text{mA}
\qquad
I_3 = \frac{U_{\text{p}}}{R_3} = \frac{12}{8} = 1{,}5\,\text{mA}
```

Kontroll: $I_2 + I_3 = 0{,}5 + 1{,}5 = 2\thinspace\text{mA} = I$. Strömmen in i parallellkopplingen är alltså lika stor som summan av strömmarna ut ur den.

---

### 2.4 – Absolutbelopp
Växelspänning varierar mellan $-8\thinspace\text{V}$ och $+8\thinspace\text{V}$.

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
$P_{\text{in}} = 24\thinspace\text{W}$, $P_{\text{ut}} = 18\thinspace\text{W}$

---

### Lösning
**a)**

```math
\eta = \frac{P_{\text{ut}}}{P_{\text{in}}} \times 100\% = \frac{18}{24} \times 100\% = 75\%
```

**b)** Med $\eta = 90\char37$ och $P_{\text{in}} = 24\thinspace\text{W}$:

```math
P_{\text{ut}} = 0{,}90 \times 24 = 21{,}6\,\text{W}
```

---

### 2.6 – Talmängder

---

### Lösning
**a)** $7 \in \mathbb{N}$ (naturligt tal)

**b)** $-3 \in \mathbb{Z}$ (heltal, ej naturligt)

**c)** $\dfrac{3}{4} \in \mathbb{Q}$ (rationellt tal)

**d)** $\sqrt{2}$ – irrationellt tal

**e)** $0{,}25 = \dfrac{1}{4} \in \mathbb{Q}$ (rationellt tal)

**f)** $\pi$ – irrationellt tal

---

## Del 3 – Extrauppgifter
### 3.1 – Räkneordning med negativa tal
**a)** $-3 + 5 \times (-2)$

**b)** $(-4)^2 - 4^2$

**c)** $\dfrac{-12}{-3} + 2 \times (-5)$

**d)** $8 - 2(3 - 7)$

**e)** $\dfrac{(-2)^3 + 10}{2}$

---

### Lösning
**a)** Multiplikationen först:

```math
-3 + 5 \times (-2) = -3 - 10 = -13
```

**b)** Parentesen i $(-4)^2$ gör att hela $-4$ kvadreras, medan $4^2$ bara kvadrerar fyran:

```math
(-4)^2 - 4^2 = 16 - 16 = 0
```

**c)** Division av två negativa tal ger ett positivt tal:

```math
\frac{-12}{-3} + 2 \times (-5) = 4 - 10 = -6
```

**d)** Parentesen först, sedan multiplikationen. Minus gånger minus ger plus:

```math
8 - 2(3 - 7) = 8 - 2 \times (-4) = 8 + 8 = 16
```

**e)** Täljaren beräknas som en parentes:

```math
\frac{(-2)^3 + 10}{2} = \frac{-8 + 10}{2} = \frac{2}{2} = 1
```

---

### 3.2 – Tallinjen och absolutbelopp
$-2{,}5$, $|-3|$, $\dfrac{7}{2}$, $-|4|$, $0$

---

### Lösning
**a)** Beräkna först absolutbeloppen: $|-3| = 3$, $-|4| = -4$ och $\dfrac{7}{2} = 3{,}5$. Sorterat:

```math
-|4| < -2{,}5 < 0 < |-3| < \frac{7}{2}
```

**b)**

```math
|-7| - |3| = 7 - 3 = 4
```

**c)**

```math
|3 - 8| = |-5| = 5, \qquad |8 - 3| = |5| = 5
```

Båda ger $5$. Absolutbeloppet av en differens är **avståndet** mellan talen på tallinjen, och ett avstånd är detsamma oavsett från vilket håll man mäter.

**d)** Skillnadens storlek skrivs $|U_1 - U_2|$:

```math
|U_1 - U_2| = |4{,}8 - 5{,}1| = |-0{,}3| = 0{,}3\,\text{V}
```

---

### 3.3 – Bråk, decimaltal och procent

---

### Lösning
Ett bråk görs om till decimaltal genom division, och till procent genom multiplikation med $100\thinspace\char37$.

| Bråk | Decimaltal | Procent |
|------|------------|---------|
| $\dfrac{1}{4}$ | $0{,}25$ | $25\thinspace\char37$ |
| $\dfrac{3}{5}$ | $0{,}6$ | $60\thinspace\char37$ |
| $\dfrac{1}{8}$ | $0{,}125$ | $12{,}5\thinspace\char37$ |
| $\dfrac{3}{8}$ | $0{,}375$ | $37{,}5\thinspace\char37$ |

Exempel på uträkningarna:

```math
\frac{1}{4} = 0{,}25 = 25\%, \qquad
0{,}6 = \frac{6}{10} = \frac{3}{5}, \qquad
12{,}5\% = \frac{12{,}5}{100} = \frac{1}{8}
```

---

### 3.4 – Bråkuttryck i flera steg
**a)** $\dfrac{2}{3} + \dfrac{1}{6} - \dfrac{1}{2}$

**b)** $\dfrac{3}{4} \times \dfrac{8}{9} \div \dfrac{2}{3}$

**c)** $\dfrac{\frac{1}{2} + \frac{1}{3}}{\frac{5}{6}}$

**d)** $\dfrac{1}{\frac{1}{4} + \frac{1}{4}}$

---

### Lösning
**a)** Gemensam nämnare är $6$:

```math
\frac{2}{3} + \frac{1}{6} - \frac{1}{2} = \frac{4}{6} + \frac{1}{6} - \frac{3}{6} = \frac{2}{6} = \frac{1}{3}
```

**b)** Multiplikation och division räknas från vänster till höger:

```math
\frac{3}{4} \times \frac{8}{9} = \frac{24}{36} = \frac{2}{3}
\qquad \Rightarrow \qquad
\frac{2}{3} \div \frac{2}{3} = \frac{2}{3} \times \frac{3}{2} = 1
```

**c)** Täljaren beräknas först:

```math
\frac{1}{2} + \frac{1}{3} = \frac{3}{6} + \frac{2}{6} = \frac{5}{6}
\qquad \Rightarrow \qquad
\frac{5/6}{5/6} = 1
```

**d)**

```math
\frac{1}{\frac{1}{4} + \frac{1}{4}} = \frac{1}{\frac{2}{4}} = \frac{1}{\frac{1}{2}} = 2
```

**e)** Uttrycket i **d)** är precis parallellresistansen av två motstånd på $4\thinspace\Omega$:

```math
R_{\text{p}} = \frac{1}{\frac{1}{R_1} + \frac{1}{R_2}} = \frac{1}{\frac{1}{4} + \frac{1}{4}} = 2\,\Omega
```

---

### 3.5 – Procentuell förändring

---

### Lösning
En procentuell förändring beräknas alltid som $\dfrac{\text{förändring}}{\text{ursprungsvärde}}$.

**a)**

```math
\frac{15 - 12}{12} \times 100\% = \frac{3}{12} \times 100\% = 25\%
```

**b)**

```math
\frac{400 - 340}{400} \times 100\% = \frac{60}{400} \times 100\% = 15\%
```

**c)** Nej. En ökning med $10\char37$ är multiplikation med $1{,}10$ och en minskning med $10\char37$ är multiplikation med $0{,}90$:

```math
1{,}10 \times 0{,}90 = 0{,}99
```

Slutvärdet är $99\char37$ av ursprungsvärdet, alltså $1\char37$ lägre. Orsaken är att minskningen räknas på det *nya*, större värdet.

**d)**

```math
P = 1{,}25 \times 60 = 75\,\text{W}
```

---

### 3.6 – Tolerans och mätavvikelse
$4{,}7\thinspace\text{k}\Omega \pm 10\thinspace\char37$ respektive $220\thinspace\Omega \pm 5\thinspace\char37$

---

### Lösning
**a)** $10\char37$ av $4{,}7\thinspace\text{k}\Omega$ är $0{,}47\thinspace\text{k}\Omega$:

```math
4{,}7 - 0{,}47 = 4{,}23\,\text{k}\Omega
\quad \text{till} \quad
4{,}7 + 0{,}47 = 5{,}17\,\text{k}\Omega
```

**b)** Ja, $4{,}9\thinspace\text{k}\Omega$ ligger inom intervallet $4{,}23$–$5{,}17\thinspace\text{k}\Omega$.

**c)** Avvikelsen räknas mot det nominella värdet:

```math
\frac{4{,}9 - 4{,}7}{4{,}7} \times 100\% = \frac{0{,}2}{4{,}7} \times 100\% \approx 4{,}3\%
```

**d)** $5\char37$ av $220\thinspace\Omega$ är $11\thinspace\Omega$, så det tillåtna intervallet är $209$–$231\thinspace\Omega$. Det uppmätta värdet $208\thinspace\Omega$ ligger **utanför** intervallet – resistorn är alltså inte godkänd. Avvikelsen är:

```math
\frac{220 - 208}{220} \times 100\% = \frac{12}{220} \times 100\% \approx 5{,}5\%
```

---

### 3.7 – Talmängder: sant eller falskt

---

### Lösning
**a)** **Sant.** Varje heltal $n$ kan skrivas som bråket $\dfrac{n}{1}$, alltså $\mathbb{Z} \subset \mathbb{Q}$.

**b)** **Falskt.** Till exempel är $\dfrac{1}{2}$ rationellt men inte ett heltal.

**c)** **Falskt.** $\sqrt{9} = 3$, vilket är ett naturligt tal. Att ett tal skrivs med rottecken betyder inte att det är irrationellt.

**d)** **Falskt.** Till exempel är $\sqrt{2} + \left(-\sqrt{2}\right) = 0$, som är ett heltal.

**e)** **Sant.** $0{,}333\ldots = \dfrac{1}{3}$. Alla periodiska decimaltal är rationella.

**f)** **Falskt.** De irrationella talen, till exempel $\pi$ och $\sqrt{2}$, är reella men kan inte skrivas som ett bråk mellan två heltal.

---

### 3.8 – Lika stora motstånd i parallell
$R = 100\thinspace\Omega$

---

### Lösning
**a)** Produkt genom summa:

```math
R_{\text{p}} = \frac{100 \times 100}{100 + 100} = \frac{10\,000}{200} = 50\,\Omega
```

**b)** Med fyra lika stora motstånd:

```math
\frac{1}{R_{\text{p}}} = \frac{1}{100} + \frac{1}{100} + \frac{1}{100} + \frac{1}{100} = \frac{4}{100}
\quad \Rightarrow \quad
R_{\text{p}} = \frac{100}{4} = 25\,\Omega
```

**c)** Med $n$ lika stora termer i summan:

```math
\frac{1}{R_{\text{p}}} = \underbrace{\frac{1}{R} + \frac{1}{R} + \cdots + \frac{1}{R}}_{n \text{ termer}} = \frac{n}{R}
\quad \Rightarrow \quad
R_{\text{p}} = \frac{R}{n}
```

**d)** Sätt $\dfrac{100}{n} = 20$, vilket ger $n = 5$ motstånd.

---

### 3.9 – Sök det okända motståndet
$R_1 = 30\thinspace\Omega$, $R_{\text{p}} = 12\thinspace\Omega$ respektive $R_1 = 220\thinspace\Omega$, $R_{\text{TOT}} = 500\thinspace\Omega$

---

### Lösning
**a)** Utgå från parallellformeln och flytta över den kända termen:

```math
\frac{1}{R_2} = \frac{1}{R_{\text{p}}} - \frac{1}{R_1} = \frac{1}{12} - \frac{1}{30}
```

Gemensam nämnare är $60$:

```math
\frac{1}{R_2} = \frac{5}{60} - \frac{2}{60} = \frac{3}{60} = \frac{1}{20}
\quad \Rightarrow \quad
R_2 = 20\,\Omega
```

**b)** Seriekopplade resistanser adderas:

```math
R_2 = R_{\text{TOT}} - R_1 = 500 - 220 = 280\,\Omega
```

**c)** Det minsta ingående motståndet i **a)** är $R_2 = 20\thinspace\Omega$, och $R_{\text{p}} = 12\thinspace\Omega < 20\thinspace\Omega$. Kontrollen stämmer.

**d)** Nej. En parallellkoppling ger alltid en resistans som är *mindre* än det minsta ingående motståndet, eftersom strömmen får fler vägar att gå. Med $R_1 = 30\thinspace\Omega$ måste därför $R_{\text{p}} < 30\thinspace\Omega$.

---

### 3.10 – Ohms lag: fyll i tabellen

---

### Lösning
| $U$ | $R$ | $I$ |
|-----|-----|-----|
| $12\thinspace\text{V}$ | $4\thinspace\text{k}\Omega$ | $3\thinspace\text{mA}$ |
| $11\thinspace\text{V}$ | $2{,}2\thinspace\text{k}\Omega$ | $5\thinspace\text{mA}$ |
| $9\thinspace\text{V}$ | $3\thinspace\text{k}\Omega$ | $3\thinspace\text{mA}$ |
| $5\thinspace\text{V}$ | $1\thinspace\text{k}\Omega$ | $5\thinspace\text{mA}$ |

Uträkningarna, rad för rad:

```math
I = \frac{12}{4} = 3\,\text{mA}, \qquad
U = 2{,}2 \times 5 = 11\,\text{V}, \qquad
R = \frac{9}{3} = 3\,\text{k}\Omega, \qquad
I = \frac{5}{1} = 5\,\text{mA}
```

Eftersom resistansen räknas i k$\Omega$ och spänningen i V fås strömmen direkt i mA.

---

### 3.11 – Verkningsgrad i två steg
$\eta_1 = 95\thinspace\char37$, $\eta_2 = 80\thinspace\char37$, $P_{\text{in}} = 200\thinspace\text{W}$

---

### Lösning
**a)**

```math
P_1 = \eta_1 \times P_{\text{in}} = 0{,}95 \times 200 = 190\,\text{W}
```

**b)** Likriktaren matas med $P_1$:

```math
P_{\text{ut}} = \eta_2 \times P_1 = 0{,}80 \times 190 = 152\,\text{W}
```

**c)**

```math
\eta_{\text{TOT}} = \frac{P_{\text{ut}}}{P_{\text{in}}} \times 100\% = \frac{152}{200} \times 100\% = 76\%
```

Samma svar fås direkt genom att multiplicera verkningsgraderna: $0{,}95 \times 0{,}80 = 0{,}76$. Verkningsgrader i flera steg **multipliceras**, de adderas inte.

**d)**

```math
P_{\text{förl}} = P_{\text{in}} - P_{\text{ut}} = 200 - 152 = 48\,\text{W}
```

---
