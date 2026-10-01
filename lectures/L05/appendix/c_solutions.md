# L05 – Lösningsförslag

## Del 1 – Repetitionsuppgifter
### 1.1 – Ekvationssystem: ström

```math
\begin{cases}
2I_1 + 3I_2 = 13 \\
4I_1 - I_2 = 5
\end{cases}
```

---

### Lösning
Vi använder additionsmetoden. Multiplicera ekvation (2) med $3$:

```math
\begin{cases}
2I_1 + 3I_2 = 13 \\
12I_1 - 3I_2 = 15
\end{cases}
```

Addera:

```math
14I_1 = 28 \quad \Rightarrow \quad I_1 = 2\,\text{A}
```

Sätt in i ekvation (1):

```math
4 + 3I_2 = 13 \quad \Rightarrow \quad I_2 = 3\,\text{A}
```

Kontroll i ekvation (2): $4 \cdot 2 - 3 = 8 - 3 = 5$ ✓

---

### 1.2 – Nodspänningar

```math
\begin{cases}
3U_A - U_B = 12 \\
-U_A + 4U_B = 6
\end{cases}
```

---

### Lösning
Multiplicera ekvation (1) med $4$ och addera med ekvation (2):

```math
\begin{cases}
12U_A - 4U_B = 48 \\
-U_A + 4U_B = 6
\end{cases}
```

Addera:

```math
11U_A = 54 \quad \Rightarrow \quad U_A = \frac{54}{11} \approx 4{,}91\,\text{V}
```

Ur ekvation (2):

```math
4U_B = 6 + U_A = 6 + \frac{54}{11} = \frac{120}{11} \quad \Rightarrow \quad U_B = \frac{30}{11} \approx 2{,}73\,\text{V}
```

---

## Del 2 – Nytt stoff
### 2.1 – Potensregler
**a)** $x^3 \cdot x^5$

**b)** $\dfrac{R^6}{R^2}$

**c)** $(I^2)^3$

**d)** $U^{-2} \cdot U^5$

**e)** $\left(\dfrac{2}{R}\right)^3$

---

### Lösning
**a)** Produktregeln:

```math
x^3 \cdot x^5 = x^{3+5} = x^8
```

**b)** Kvotregeln:

```math
\frac{R^6}{R^2} = R^{6-2} = R^4
```

**c)** Potens av potens:

```math
(I^2)^3 = I^{2 \cdot 3} = I^6
```

**d)** Produktregeln med negativ exponent:

```math
U^{-2} \cdot U^5 = U^{-2+5} = U^3
```

**e)** Potens av kvot:

```math
\left(\frac{2}{R}\right)^3 = \frac{2^3}{R^3} = \frac{8}{R^3}
```

---

### 2.2 – Standardform

---

### Lösning
**a)** $47\thinspace 000 = 4{,}7 \times 10^4\thinspace\Omega$

**b)** $0{,}000\thinspace 022 = 2{,}2 \times 10^{-5}\thinspace\text{F}$

**c)** $3\thinspace 300\thinspace 000 = 3{,}3 \times 10^6\thinspace\text{Hz}$

**d)** $0{,}000\thinspace 000\thinspace 015 = 1{,}5 \times 10^{-8}\thinspace\text{A}$

---

### 2.3 – Effektberäkning

---

### Lösning
**a)** $U = 5\thinspace\text{V}$, $R = 100\thinspace\Omega$:

```math
P = \frac{U^2}{R} = \frac{25}{100} = 0{,}25\,\text{W} = 250\,\text{mW}
```

**b)** $I = 40\thinspace\text{mA} = 0{,}04\thinspace\text{A}$, $R = 50\thinspace\Omega$:

```math
P = RI^2 = 50 \times (0{,}04)^2 = 50 \times 0{,}0016 = 0{,}08\,\text{W} = 80\,\text{mW}
```

---

### 2.4 – Från binärt och hexadecimalt till decimalt
**a)** $1010_2$

**b)** $11001_2$

**c)** $\mathrm{3A}_{16}$

**d)** `0xC8`

---

### Lösning
Multiplicera varje siffra med positionens värde och summera.

**a)**

```math
1010_2 = 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 0 \cdot 2^0 = 8 + 2 = 10
```

**b)**

```math
11001_2 = 1 \cdot 2^4 + 1 \cdot 2^3 + 0 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 = 16 + 8 + 1 = 25
```

**c)** A betyder $10$:

```math
\mathrm{3A}_{16} = 3 \cdot 16^1 + 10 \cdot 16^0 = 48 + 10 = 58
```

**d)** Prefixet `0x` betyder att talet är hexadecimalt, och C betyder $12$:

```math
\mathrm{C8}_{16} = 12 \cdot 16^1 + 8 \cdot 16^0 = 192 + 8 = 200
```

---

### 2.5 – Från decimalt till binärt och hexadecimalt

---

### Lösning
**a)** Dividera upprepade gånger med $2$:

| Division | Kvot | Rest |
|----------|------|------|
| $22 / 2$ | $11$ | $0$ |
| $11 / 2$ | $5$ | $1$ |
| $5 / 2$ | $2$ | $1$ |
| $2 / 2$ | $1$ | $0$ |
| $1 / 2$ | $0$ | $1$ |

Resterna nerifrån och upp ger $22 = 10110_2$. Kontroll: $16 + 4 + 2 = 22$ ✓

**b)**

| Division | Kvot | Rest |
|----------|------|------|
| $100 / 2$ | $50$ | $0$ |
| $50 / 2$ | $25$ | $0$ |
| $25 / 2$ | $12$ | $1$ |
| $12 / 2$ | $6$ | $0$ |
| $6 / 2$ | $3$ | $0$ |
| $3 / 2$ | $1$ | $1$ |
| $1 / 2$ | $0$ | $1$ |

Resterna nerifrån och upp ger $100 = 1100100_2$. Kontroll: $64 + 32 + 4 = 100$ ✓

**c)** Dela in bitarna i grupper om fyra från höger och fyll på med en nolla till vänster:

```math
1100100_2 = \underbrace{0110}_{6}\;\underbrace{0100}_{4} = \mathrm{64}_{16}
```

Kontroll: $6 \cdot 16 + 4 = 100$ ✓. Observera att $\mathrm{64}_{16}$ och $64$ är olika tal – basen måste framgå.

**d)** Byt varje hexadecimal siffra mot sina fyra bitar, $5 = 0101$ och $\mathrm{A} = 1010$:

```math
\mathrm{5A}_{16} = 0101\,1010_2
```

---

## Del 3 – Extrauppgifter
### 3.1 – Beräkna potenser
**a)** $3^4$

**b)** $(-2)^5$

**c)** $10^{-2}$

**d)** $5^0$

**e)** $2^{-3}$

**f)** $0{,}1^3$

---

### Lösning
**a)** $3^4 = 3 \times 3 \times 3 \times 3 = 81$

**b)** Udda exponent bevarar minustecknet:

```math
(-2)^5 = -32
```

**c)** Negativ exponent ger ett bråk:

```math
10^{-2} = \frac{1}{10^2} = \frac{1}{100} = 0{,}01
```

**d)** Allt (utom noll) upphöjt till noll är ett: $5^0 = 1$

**e)**

```math
2^{-3} = \frac{1}{2^3} = \frac{1}{8} = 0{,}125
```

**f)**

```math
0{,}1^3 = \left(10^{-1}\right)^3 = 10^{-3} = 0{,}001
```

---

### 3.2 – Potensregler
**a)** $a^7 \cdot a^{-3}$

**b)** $\dfrac{U^5}{U^8}$

**c)** $(2R^3)^2$

**d)** $\dfrac{(I^2)^4}{I^3}$

**e)** $\left(\dfrac{R^2}{3}\right)^3$

**f)** $\dfrac{6x^5}{2x^2}$

---

### Lösning
**a)** Produktregeln – exponenterna adderas:

```math
a^7 \cdot a^{-3} = a^{7-3} = a^4
```

**b)** Kvotregeln, sedan negativ exponent:

```math
\frac{U^5}{U^8} = U^{5-8} = U^{-3} = \frac{1}{U^3}
```

**c)** Potens av produkt – **båda** faktorerna kvadreras:

```math
(2R^3)^2 = 2^2 \cdot (R^3)^2 = 4R^6
```

**d)** Först potens av potens, sedan kvotregeln:

```math
\frac{(I^2)^4}{I^3} = \frac{I^8}{I^3} = I^5
```

**e)** Potens av kvot:

```math
\left(\frac{R^2}{3}\right)^3 = \frac{(R^2)^3}{3^3} = \frac{R^6}{27}
```

**f)** Koefficienterna divideras för sig och potenserna för sig:

```math
\frac{6x^5}{2x^2} = 3x^{5-2} = 3x^3
```

---

### 3.3 – Tiopotenser
**a)** $10^4 \cdot 10^{-7}$

**b)** $\dfrac{10^{-2}}{10^{-5}}$

**c)** $\left(10^3\right)^{-2}$

**d)** $\dfrac{10^6 \cdot 10^{-2}}{10^{-3}}$

**e)** $\sqrt{10^{-6}}$

---

### Lösning
**a)**

```math
10^4 \cdot 10^{-7} = 10^{4-7} = 10^{-3}
```

**b)** Kvotregeln – minus minus blir plus:

```math
\frac{10^{-2}}{10^{-5}} = 10^{-2-(-5)} = 10^{3}
```

**c)**

```math
\left(10^3\right)^{-2} = 10^{-6}
```

**d)** Räkna ut täljaren först:

```math
\frac{10^6 \cdot 10^{-2}}{10^{-3}} = \frac{10^{4}}{10^{-3}} = 10^{4+3} = 10^{7}
```

**e)** En kvadratrot är exponenten $\tfrac{1}{2}$:

```math
\sqrt{10^{-6}} = \left(10^{-6}\right)^{1/2} = 10^{-3}
```

---

### 3.4 – Rötter

---

### Lösning
**a)** $\sqrt{81} = 9$, eftersom $9^2 = 81$.

**b)** $\sqrt{0{,}25} = 0{,}5$, eftersom $0{,}5^2 = 0{,}25$.

**c)** $\sqrt[3]{27} = 3$, eftersom $3^3 = 27$.

**d)** Dela upp roten i två faktorer:

```math
\sqrt{16 \times 10^{-4}} = \sqrt{16} \times \sqrt{10^{-4}} = 4 \times 10^{-2} = 0{,}04
```

**e)** Bryt ut den största kvadraten ur $50$:

```math
\sqrt{50} = \sqrt{25 \times 2} = \sqrt{25} \times \sqrt{2} = 5\sqrt{2} \approx 7{,}07
```

**f)** Insättning:

```math
\sqrt{9 + 16} = \sqrt{25} = 5
\qquad \text{men} \qquad
\sqrt{9} + \sqrt{16} = 3 + 4 = 7
```

Roten ur en **summa** kan alltså inte delas upp. Regeln $\sqrt{ab} = \sqrt{a}\sqrt{b}$ gäller bara för produkter och kvoter.

---

### 3.5 – Bråkexponenter
**a)** $16^{1/2}$

**b)** $27^{1/3}$

**c)** $9^{3/2}$

**d)** $8^{-1/3}$

**e)** $\left(\dfrac{1}{4}\right)^{-1/2}$

---

### Lösning
**a)** Nämnaren i exponenten anger rotens ordning:

```math
16^{1/2} = \sqrt{16} = 4
```

**b)**

```math
27^{1/3} = \sqrt[3]{27} = 3
```

**c)** Ta roten först, upphöj sedan – då blir talen små:

```math
9^{3/2} = \left(\sqrt{9}\right)^3 = 3^3 = 27
```

**d)** Negativ exponent ger reciproken:

```math
8^{-1/3} = \frac{1}{8^{1/3}} = \frac{1}{\sqrt[3]{8}} = \frac{1}{2}
```

**e)** Negativ exponent vänder på bråket:

```math
\left(\frac{1}{4}\right)^{-1/2} = 4^{1/2} = \sqrt{4} = 2
```

---

### 3.6 – Från prefix till grundenhet

---

### Lösning
Prefixet byts mot sin tiopotens, och mantissan justeras så att $1 \leq a < 10$.

**a)** $2{,}2\thinspace\text{k}\Omega = 2{,}2 \times 10^3\thinspace\Omega$

**b)** $470\thinspace\mu\text{F} = 470 \times 10^{-6}\thinspace\text{F} = 4{,}7 \times 10^{-4}\thinspace\text{F}$

**c)** $15\thinspace\text{pF} = 15 \times 10^{-12}\thinspace\text{F} = 1{,}5 \times 10^{-11}\thinspace\text{F}$

**d)** $250\thinspace\text{mA} = 250 \times 10^{-3}\thinspace\text{A} = 2{,}5 \times 10^{-1}\thinspace\text{A}$

**e)** $1{,}8\thinspace\text{MHz} = 1{,}8 \times 10^6\thinspace\text{Hz}$

**f)** $6{,}8\thinspace\text{nH} = 6{,}8 \times 10^{-9}\thinspace\text{H}$

---

### 3.7 – Från standardform till prefix

---

### Lösning
**a)** $3{,}3 \times 10^{-6}\thinspace\text{F} = 3{,}3\thinspace\mu\text{F}$

**b)** $4{,}7 \times 10^{5}\thinspace\Omega = 470 \times 10^{3}\thinspace\Omega = 470\thinspace\text{k}\Omega$

**c)** $2{,}5 \times 10^{-4}\thinspace\text{A} = 250 \times 10^{-6}\thinspace\text{A} = 250\thinspace\mu\text{A}$

**d)** $8 \times 10^{7}\thinspace\text{Hz} = 80 \times 10^{6}\thinspace\text{Hz} = 80\thinspace\text{MHz}$

**e)** $1{,}2 \times 10^{-11}\thinspace\text{F} = 12 \times 10^{-12}\thinspace\text{F} = 12\thinspace\text{pF}$

Knepet är att flytta kommat i steg om **tre** tiopotenser, eftersom prefixen ligger tre steg isär.

---

### 3.8 – Räkning med standardform

---

### Lösning
**a)** Multiplicera mantissorna och addera exponenterna:

```math
\left(4 \times 10^5\right)\left(2 \times 10^{-8}\right) = 8 \times 10^{-3}
```

**b)** Dividera mantissorna och subtrahera exponenterna:

```math
\frac{9 \times 10^{-3}}{3 \times 10^{2}} = 3 \times 10^{-5}
```

**c)** Både mantissa och tiopotens kvadreras. Justera sedan till standardform:

```math
\left(5 \times 10^3\right)^2 = 25 \times 10^6 = 2{,}5 \times 10^7
```

**d)** Vid addition måste exponenterna vara lika. Skriv om den andra termen:

```math
7{,}5 \times 10^{-4} = 0{,}75 \times 10^{-3}
```

```math
2{,}5 \times 10^{-3} + 0{,}75 \times 10^{-3} = 3{,}25 \times 10^{-3}
```

**e)** Kvadrera täljaren först:

```math
\frac{\left(6 \times 10^{-2}\right)^2}{4 \times 10^{-5}} = \frac{36 \times 10^{-4}}{4 \times 10^{-5}} = 9 \times 10^{1} = 90
```

---

### 3.9 – Värdesiffror och avrundning

---

### Lösning
**a)** Tre värdesiffror: $4$, $7$ och den avslutande nollan. Nollan skrivs ut just för att visa att den är uppmätt – det är därför standardform är entydigt.

**b)** Den tredje värdesiffran är $6$, alltså rundas uppåt:

```math
0{,}024\,68 \approx 0{,}025
```

**c)** Den fjärde siffran är $4$, alltså rundas nedåt:

```math
12\,345\,\Omega \approx 12\,300\,\Omega = 1{,}23 \times 10^4\,\Omega
```

**d)** Spänningen har två värdesiffror och resistansen tre. Svaret bör anges med det minsta antalet, alltså **två**:

```math
I = \frac{5{,}0}{100} = 0{,}050\,\text{A} = 50\,\text{mA}
```

---

### 3.10 – Ohms lag med tiopotenser

---

### Lösning
**a)**

```math
I = \frac{U}{R} = \frac{3{,}3}{220} = 0{,}015\,\text{A} = 15\,\text{mA}
```

**b)** Multiplicera mantissorna och addera exponenterna:

```math
U = RI = \left(47 \times 10^{3}\right)\left(250 \times 10^{-6}\right) = 11\,750 \times 10^{-3} = 11{,}75\,\text{V}
```

**c)** Med spänningen i V och strömmen i mA fås resistansen direkt i k$\Omega$:

```math
R = \frac{U}{I} = \frac{12}{4} = 3\,\text{k}\Omega
```

---

### 3.11 – Effekt med tiopotenser

---

### Lösning
**a)**

```math
P = RI^2 = \left(1{,}5 \times 10^3\right)\left(20 \times 10^{-3}\right)^2 = 1500 \times 4 \times 10^{-4} = 0{,}6\,\text{W}
```

**b)**

```math
P = \frac{U^2}{R} = \frac{25}{2{,}2 \times 10^3} \approx 1{,}14 \times 10^{-2}\,\text{W} \approx 11{,}4\,\text{mW}
```

**c)** Lös ut strömmen ur $P = RI^2$:

```math
I = \sqrt{\frac{P}{R}} = \sqrt{\frac{0{,}25}{470}} = \sqrt{5{,}32 \times 10^{-4}} \approx 2{,}3 \times 10^{-2}\,\text{A} \approx 23\,\text{mA}
```

**d)** Lös ut spänningen ur $P = \dfrac{U^2}{R}$:

```math
U = \sqrt{PR} = \sqrt{0{,}25 \times 470} = \sqrt{117{,}5} \approx 10{,}8\,\text{V}
```

Kontroll: $\dfrac{10{,}8}{470} \approx 23\thinspace\text{mA}$, samma ström som i **c)** ✓

---

### 3.12 – Tidskonstant med prefix

---

### Lösning
**a)**

```math
\tau = RC = \left(10 \times 10^3\right)\left(4{,}7 \times 10^{-6}\right) = 47 \times 10^{-3}\,\text{s} = 47\,\text{ms}
```

**b)**

```math
R = \frac{\tau}{C} = \frac{1 \times 10^{-3}}{100 \times 10^{-9}} = \frac{10^{-3}}{10^{-7}} = 10^4\,\Omega = 10\,\text{k}\Omega
```

**c)**

```math
C = \frac{\tau}{R} = \frac{1{,}1}{2{,}2 \times 10^6} = 0{,}5 \times 10^{-6}\,\text{F} = 500 \times 10^{-9}\,\text{F} = 500\,\text{nF}
```

---

### 3.13 – Toppvärde, effektivvärde och effekt

---

### Lösning
**a)**

```math
U_{\text{RMS}} = \frac{10}{\sqrt{2}} \approx 7{,}07\,\text{V}
```

**b)**

```math
|U| = 230 \times \sqrt{2} \approx 325\,\text{V}
```

Det är därför nätspänningens toppvärde är ungefär $325\thinspace\text{V}$ trots att den anges som $230\thinspace\text{V}$.

**c)** Sätt in $U_{\text{RMS}} = \dfrac{|U|}{\sqrt{2}}$ och kvadrera:

```math
P = \frac{U_{\text{RMS}}^2}{R} = \frac{1}{R}\left(\frac{|U|}{\sqrt{2}}\right)^2 = \frac{1}{R} \cdot \frac{|U|^2}{2} = \frac{|U|^2}{2R}
```

Faktorn $2$ kommer alltså från kvadraten på $\sqrt{2}$.

**d)**

```math
P = \frac{12^2}{2 \times 8} = \frac{144}{16} = 9\,\text{W}
```

---

### 3.14 – Hitta felet

---

### Lösning
**a)** Vid multiplikation **adderas** exponenterna, de multipliceras inte:

```math
2^3 \cdot 2^4 = 2^{7} = 128
```

**b)** Vid potens av potens **multipliceras** exponenterna:

```math
\left(a^2\right)^3 = a^{6}
```

**c)** Vid division **subtraheras** exponenterna: $6 - 2 = 4$:

```math
\frac{10^6}{10^2} = 10^{4}
```

**d)** Exponenten gäller hela produkten, alltså även tvåan:

```math
(2a)^3 = 2^3a^3 = 8a^3
```

**e)** En rot kan inte delas upp över en summa:

```math
\sqrt{9 + 16} = \sqrt{25} = 5
```

**f)** En negativ exponent ger en reciprok, inte ett negativt tal:

```math
a^{-2} = \frac{1}{a^2}
```

---

### 3.15 – Binära tal
**a)** $111_2$

**b)** $10000_2$

**c)** $101010_2$

**d)** $37$

**e)** $64$

**f)** $255$

---

### Lösning
**a)**

```math
111_2 = 4 + 2 + 1 = 7
```

**b)** En etta följd av fyra nollor är $2^4$:

```math
10000_2 = 2^4 = 16
```

**c)**

```math
101010_2 = 32 + 8 + 2 = 42
```

**d)** Dividera upprepade gånger med $2$:

| Division | Kvot | Rest |
|----------|------|------|
| $37 / 2$ | $18$ | $1$ |
| $18 / 2$ | $9$ | $0$ |
| $9 / 2$ | $4$ | $1$ |
| $4 / 2$ | $2$ | $0$ |
| $2 / 2$ | $1$ | $0$ |
| $1 / 2$ | $0$ | $1$ |

Resterna nerifrån och upp ger $37 = 100101_2$. Kontroll: $32 + 4 + 1 = 37$ ✓

**e)** $64 = 2^6$, alltså en etta följd av sex nollor:

```math
64 = 1000000_2
```

**f)** $255 = 256 - 1 = 2^8 - 1$, det största talet som ryms i en byte, alltså åtta ettor:

```math
255 = 1111\,1111_2
```

---

### 3.16 – Hexadecimala tal
**a)** $\mathrm{1F}_{16}$

**b)** `0x80`

**c)** $\mathrm{ABC}_{16}$

**d)** $175$

**e)** $4\thinspace 096$

**f)** $1\thinspace 000$

---

### Lösning
**a)** F betyder $15$:

```math
\mathrm{1F}_{16} = 1 \cdot 16 + 15 = 31
```

**b)**

```math
\mathrm{80}_{16} = 8 \cdot 16 + 0 = 128
```

**c)** A, B och C betyder $10$, $11$ och $12$:

```math
\mathrm{ABC}_{16} = 10 \cdot 16^2 + 11 \cdot 16^1 + 12 \cdot 16^0 = 2\,560 + 176 + 12 = 2\,748
```

**d)** $175 / 16 = 10$ med resten $15$, och $10 / 16 = 0$ med resten $10$. Resterna nerifrån och upp, skrivna med bokstäver:

```math
175 = \mathrm{AF}_{16}
```

Kontroll: $10 \cdot 16 + 15 = 175$ ✓

**e)** $4\thinspace 096 = 16^3$, alltså en etta följd av tre nollor:

```math
4\,096 = \mathrm{1000}_{16}
```

**f)**

| Division | Kvot | Rest |
|----------|------|------|
| $1\thinspace 000 / 16$ | $62$ | $8$ |
| $62 / 16$ | $3$ | $14 = \mathrm{E}$ |
| $3 / 16$ | $0$ | $3$ |

Resterna nerifrån och upp ger $1\thinspace 000 = \mathrm{3E8}_{16}$. Kontroll: $3 \cdot 256 + 14 \cdot 16 + 8 = 768 + 224 + 8 = 1\thinspace 000$ ✓

---

### 3.17 – Mellan binärt och hexadecimalt
**a)** $1001\thinspace 1110_2$

**b)** $1111\thinspace 0000_2$

**c)** $101011_2$

**d)** `0x3C`

**e)** `0xA5`

**f)** `0x7F`

---

### Lösning
Varje grupp om fyra bitar motsvarar en hexadecimal siffra.

**a)** $1001 = 9$ och $1110 = \mathrm{E}$, alltså $\mathrm{9E}_{16}$.

**b)** $1111 = \mathrm{F}$ och $0000 = 0$, alltså $\mathrm{F0}_{16}$.

**c)** Gruppera från höger och fyll på med nollor till vänster:

```math
101011_2 = \underbrace{0010}_{2}\;\underbrace{1011}_{\mathrm{B}} = \mathrm{2B}_{16}
```

**d)** $3 = 0011$ och $\mathrm{C} = 1100$, alltså $0011\thinspace 1100_2$.

**e)** $\mathrm{A} = 1010$ och $5 = 0101$, alltså $1010\thinspace 0101_2$.

**f)** $7 = 0111$ och $\mathrm{F} = 1111$, alltså $0111\thinspace 1111_2$.

---

### 3.18 – Bitar, byte och register

---

### Lösning
**a)** Med $4$ bitar kan $2^4 = 16$ olika värden lagras, från $0$ till $15$. Det största är $1111_2 = \mathrm{F}_{16} = 15$.

**b)** Med $10$ bitar kan $2^{10} = 1\thinspace 024$ olika värden lagras, från $0$ till $1\thinspace 023$.

**c)** Skriv registrets värde binärt och numrera bitarna från höger:

```math
\mathrm{24}_{16} = 0010\,0100_2
```

| Bit | $7$ | $6$ | $5$ | $4$ | $3$ | $2$ | $1$ | $0$ |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Värde | $0$ | $0$ | $1$ | $0$ | $0$ | $1$ | $0$ | $0$ |

Bit $2$ och bit $5$ är ettor. Kontroll: $2^5 + 2^2 = 32 + 4 = 36 = 2 \cdot 16 + 4$ ✓

**d)** Bit $7$ är längst till vänster och bit $0$ längst till höger:

```math
1000\,0001_2 = \mathrm{81}_{16} = 2^7 + 2^0 = 129
```

---
