# L06 – Lösningsförslag

## Del 1 – Repetitionsuppgifter
### 1.1 – Potensregler
**a)** $\dfrac{10^6 \cdot 10^{-3}}{10^2}$

**b)** $(2 \cdot 10^3)^2$

**c)** $\sqrt{4 \times 10^6}$

---

### Lösning
**a)** Täljaren: $10^6 \cdot 10^{-3} = 10^3$. Sedan dividera:

```math
\frac{10^3}{10^2} = 10^{3-2} = 10^1 = 10
```

**b)** Potens av produkt:

```math
(2 \cdot 10^3)^2 = 2^2 \cdot (10^3)^2 = 4 \cdot 10^6
```

**c)**

```math
\sqrt{4 \times 10^6} = \sqrt{4} \times \sqrt{10^6} = 2 \times 10^3 = 2\,000
```

---

### 1.2 – Standardform i kretsberäkning
$U = 3{,}3\thinspace\text{V}$, $R = 4{,}7 \times 10^3\thinspace\Omega$

---

### Lösning
**a)**

```math
I = \frac{U}{R} = \frac{3{,}3}{4{,}7 \times 10^3} \approx 7{,}02 \times 10^{-4}\,\text{A} \approx 0{,}702\,\text{mA}
```

**b)**

```math
P = \frac{U^2}{R} = \frac{3{,}3^2}{4{,}7 \times 10^3} = \frac{10{,}89}{4700} \approx 2{,}32 \times 10^{-3}\,\text{W} \approx 2{,}32\,\text{mW}
```

---

### 1.3 – Kvadratrot
**a)** $\sqrt{144} = 12$ (eftersom $12^2 = 144$)

**b)** $\sqrt{0{,}0049} = \sqrt{49 \times 10^{-4}} = 7 \times 10^{-2} = 0{,}07$

**c)** Ur $P = \dfrac{U^2}{R}$:

```math
U^2 = P \cdot R = 2 \times 200 = 400 \quad \Rightarrow \quad U = \sqrt{400} = 20\,\text{V}
```

---

### 1.4 – Lysdioder på en mikrokontroller
LED1 är ansluten till D2 och LED2 till D6, via var sin resistor till jord:

![](./images/1.4_circuit.png)

$V_{CC} = 5{,}0\thinspace\text{V}$, $U_F = 2{,}0\thinspace\text{V}$, önskad ström ca $10\thinspace\text{mA}$.

---

### Lösning
**a)** Bitarna 2 och 6 ska vara $1$, övriga $0$:

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|-----|---|---|---|---|---|---|---|---|
| `DDRD` | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |

```math
\text{DDRD} = 0100\,0100_2 = \mathrm{44}_{16}
```

I C skrivs det `DDRD = 0b01000100;` eller `DDRD = 0x44;`. Kontroll: $2^6 + 2^2 = 64 + 4 = 68 = 4 \cdot 16 + 4$ ✓

**b)** Endast bit 2 ska vara $1$:

```math
\text{PORTD} = 0000\,0100_2 = \mathrm{04}_{16}
```

I C skrivs det `PORTD = 0b00000100;` eller `PORTD = 0x04;`.

**c)** Endast bit 6 ska läggas till, så $x$ har en etta i bit 6 och nollor i övrigt:

```math
x = 0100\,0000_2 = \mathrm{40}_{16}
```

Det nya värdet av `PORTD` blir:

```math
\text{PORTD} = 0000\,0100_2 + 0100\,0000_2 = 0100\,0100_2 = \mathrm{44}_{16}
```

Bit 2 är fortfarande $1$, så LED1 fortsätter att lysa. I C skrivs det `PORTD |= 0b01000000;` eller `PORTD |= 0x40;`.

Hade vi i stället skrivit `PORTD = 0x40;` hade bit 2 nollställts och LED1 släckts.

> **OBS!** `|=` fungerar som addition här eftersom bit 6 är $0$ från början. Är biten redan $1$ förblir den $1$ med `|=`, medan en addition hade gett en minnessiffra som ändrar bit 7.

**d)** Spänningen över resistorn är

```math
U_R = V_{CC} - U_F = 5{,}0 - 2{,}0 = 3{,}0\,\text{V}
```

Ohms lag ger resistansen för $I = 10\thinspace\text{mA}$:

```math
R = \frac{U_R}{I} = \frac{3{,}0}{10 \times 10^{-3}} = 300\,\Omega
```

$300\thinspace\Omega$ finns inte i E12-serien; de närmaste värdena är $270\thinspace\Omega$ och $330\thinspace\Omega$. Vi väljer det större värdet, så att strömmen hamnar strax under i stället för strax över $10\thinspace\text{mA}$:

```math
R_1 = R_2 = 330\,\Omega \quad \Rightarrow \quad I = \frac{3{,}0}{330} \approx 9{,}1\,\text{mA}
```

Med $270\thinspace\Omega$ hade strömmen blivit $\dfrac{3{,}0}{270} \approx 11{,}1\thinspace\text{mA}$, vilket också är ett godtagbart svar.

**e)** Hela matningsspänningen ligger över resistor och lysdiod tillsammans, så effekten i en krets med tänd lysdiod är

```math
P = V_{CC} \cdot I = 5{,}0 \times 9{,}09 \times 10^{-3} \approx 45\,\text{mW}
```

Kontroll: effekten fördelas mellan resistorn och lysdioden:

```math
P_R = U_R \cdot I = 3{,}0 \times 9{,}09 \times 10^{-3} \approx 27\,\text{mW} \qquad P_{LED} = U_F \cdot I = 2{,}0 \times 9{,}09 \times 10^{-3} \approx 18\,\text{mW}
```

$27 + 18 = 45\thinspace\text{mW}$ ✓

Kretsarna är likadana, så de förbrukar $45\thinspace\text{mW}$ var när respektive lysdiod är tänd. Med $270\thinspace\Omega$ hade effekten blivit $5{,}0 \times 11{,}1 \times 10^{-3} \approx 56\thinspace\text{mW}$.

---

## Del 2 – Nytt stoff
### 2.1 – Ren andragradsekvation
$50I^2 = 8$

---

### Lösning
**a)** Dividera med $50$:

```math
I^2 = \frac{8}{50} = 0{,}16
```

Ta kvadratroten:

```math
I = \pm\sqrt{0{,}16} = \pm 0{,}4\,\text{A}
```

**b)** Ström i ett motstånd ges av en riktningskonvention. Eftersom $P = RI^2$ är positiv oavsett tecken väljer vi den positiva roten:

```math
I = 0{,}4\,\text{A}
```

---

### 2.2 – PQ-formeln
**a)** $x^2 - 5x + 6 = 0$

**b)** $x^2 + 3x - 10 = 0$

**c)** $x^2 - 6x + 9 = 0$

---

### Lösning
Vi använder den alternativa formen av PQ-formeln: flytta över allt utom $x^2$ till högerledet, så att ekvationen står på formen $x^2 = px + q$. Då är

```math
x = \frac{p}{2} \pm \sqrt{\left(\frac{p}{2}\right)^2 + q}
```

**a)**

```math
x^2 = 5x - 6 \quad (p = 5, \; q = -6)
```

```math
x = \frac{5}{2} \pm \sqrt{\left(\frac{5}{2}\right)^2 - 6} = 2{,}5 \pm \sqrt{0{,}25} = 2{,}5 \pm 0{,}5
```

```math
x_1 = 3, \quad x_2 = 2
```

**b)**

```math
x^2 = -3x + 10 \quad (p = -3, \; q = 10)
```

```math
x = \frac{-3}{2} \pm \sqrt{\left(\frac{-3}{2}\right)^2 + 10} = -1{,}5 \pm \sqrt{12{,}25} = -1{,}5 \pm 3{,}5
```

```math
x_1 = 2, \quad x_2 = -5
```

**c)**

```math
x^2 = 6x - 9 \quad (p = 6, \; q = -9)
```

Uttrycket under rottecknet blir $(6/2)^2 - 9 = 9 - 9 = 0$ → dubbelrot:

```math
x = \frac{6}{2} \pm 0 = 3 \quad \Rightarrow \quad x_1 = x_2 = 3
```

---

### 2.3 – Icke normerad andragradsekvation
**a)** $2x^2 - 7x + 3 = 0$

**b)** $3x^2 + 5x - 2 = 0$

---

### Lösning
PQ-formeln kräver att koefficienten framför $x^2$ är $1$.

**a)** Dividera med $2$ och flytta över allt utom $x^2$:

```math
x^2 - 3{,}5x + 1{,}5 = 0 \quad \Rightarrow \quad x^2 = 3{,}5x - 1{,}5 \quad (p = 3{,}5, \; q = -1{,}5)
```

```math
x = 1{,}75 \pm \sqrt{1{,}75^2 - 1{,}5} = 1{,}75 \pm \sqrt{1{,}5625} = 1{,}75 \pm 1{,}25
```

```math
x_1 = 3, \quad x_2 = 0{,}5
```

**b)** Dividera med $3$ och flytta över allt utom $x^2$:

```math
x^2 + \frac{5}{3}x - \frac{2}{3} = 0 \quad \Rightarrow \quad x^2 = -\frac{5}{3}x + \frac{2}{3} \quad \left(p = -\frac{5}{3}, \; q = \frac{2}{3}\right)
```

```math
x = -\frac{5}{6} \pm \sqrt{\left(-\frac{5}{6}\right)^2 + \frac{2}{3}} = -\frac{5}{6} \pm \sqrt{\frac{25}{36} + \frac{24}{36}} = -\frac{5}{6} \pm \frac{7}{6}
```

```math
x_1 = \frac{1}{3}, \quad x_2 = -2
```

---

### 2.4 – Seriekopplade motstånd
$R_1 + R_2 = 13\thinspace\Omega$, $R_1 \cdot R_2 = 36\thinspace\Omega^2$

---

### Lösning
**a)** Den första ekvationen ger $R_2 = 13 - R_1$. Insatt i den andra:

```math
R_1(13 - R_1) = 36 \quad \Rightarrow \quad R_1^2 - 13R_1 + 36 = 0
```

**b)** Flytta över allt utom $R_1^2$ till högerledet:

```math
R_1^2 = 13R_1 - 36 \quad (p = 13, \; q = -36)
```

```math
R_1 = \frac{13}{2} \pm \sqrt{\left(\frac{13}{2}\right)^2 - 36} = 6{,}5 \pm \sqrt{42{,}25 - 36} = 6{,}5 \pm \sqrt{6{,}25} = 6{,}5 \pm 2{,}5
```

Roten $R_1 = 9\thinspace\Omega$ ger $R_2 = 13 - 9 = 4\thinspace\Omega$. Den andra roten, $R_1 = 4\thinspace\Omega$, ger samma par i omvänd ordning:

```math
R_1 = 9\,\Omega, \quad R_2 = 4\,\Omega
```

Kontroll: $9 + 4 = 13$ ✓ och $9 \times 4 = 36$ ✓

---

## Del 3 – Extrauppgifter
### 3.1 – Rena andragradsekvationer
**a)** $x^2 = 49$

**b)** $3x^2 = 27$

**c)** $x^2 - 5 = 20$

**d)** $2x^2 + 8 = 0$

**e)** $\dfrac{x^2}{4} = 9$

---

### Lösning
En ren andragradsekvation saknar linjär term och löses genom att isolera $x^2$ och ta roten – med **båda** tecknen.

**a)**

```math
x = \pm\sqrt{49} \quad \Rightarrow \quad x_1 = 7, \quad x_2 = -7
```

**b)** Dividera med $3$:

```math
x^2 = 9 \quad \Rightarrow \quad x_1 = 3, \quad x_2 = -3
```

**c)** Addera $5$:

```math
x^2 = 25 \quad \Rightarrow \quad x_1 = 5, \quad x_2 = -5
```

**d)** Subtrahera $8$ och dividera med $2$:

```math
x^2 = -4
```

Ingen reell kvadrat är negativ, så ekvationen **saknar reella lösningar**.

**e)** Multiplicera med $4$:

```math
x^2 = 36 \quad \Rightarrow \quad x_1 = 6, \quad x_2 = -6
```

---

### 3.2 – Faktoriseringsmetoden
**a)** $x^2 - 7x = 0$

**b)** $x^2 - 16 = 0$

**c)** $x^2 + 5x + 6 = 0$

**d)** $2x^2 - 8x = 0$

**e)** $x^2 - 4x + 4 = 0$

---

### Lösning
Nollproduktmetoden: är en produkt noll måste minst en faktor vara noll.

**a)** Bryt ut $x$:

```math
x(x - 7) = 0 \quad \Rightarrow \quad x_1 = 0, \quad x_2 = 7
```

Notera att $x = 0$ är en fullgod rot – dividera aldrig bort $x$, då tappar man den.

**b)** Konjugatregeln:

```math
(x + 4)(x - 4) = 0 \quad \Rightarrow \quad x_1 = -4, \quad x_2 = 4
```

**c)** Sök två tal med summan $5$ och produkten $6$, nämligen $2$ och $3$:

```math
(x + 2)(x + 3) = 0 \quad \Rightarrow \quad x_1 = -2, \quad x_2 = -3
```

**d)** Bryt ut $2x$:

```math
2x(x - 4) = 0 \quad \Rightarrow \quad x_1 = 0, \quad x_2 = 4
```

**e)** Kvadrat av differens:

```math
(x - 2)^2 = 0 \quad \Rightarrow \quad x_1 = x_2 = 2
```

En **dubbelrot** – de båda rötterna sammanfaller.

---

### 3.3 – PQ-formeln
**a)** $x^2 + 2x - 8 = 0$

**b)** $x^2 - 8x + 12 = 0$

**c)** $x^2 + x - 12 = 0$

**d)** $x^2 - 2x - 15 = 0$

---

### Lösning
PQ-formeln lyder $x = -\dfrac{p}{2} \pm \sqrt{\left(\dfrac{p}{2}\right)^2 - q}$.

**a)** $p = 2$, $q = -8$:

```math
x = -1 \pm \sqrt{1 + 8} = -1 \pm 3 \quad \Rightarrow \quad x_1 = 2, \quad x_2 = -4
```

**b)** $p = -8$, $q = 12$:

```math
x = 4 \pm \sqrt{16 - 12} = 4 \pm 2 \quad \Rightarrow \quad x_1 = 6, \quad x_2 = 2
```

**c)** $p = 1$, $q = -12$:

```math
x = -0{,}5 \pm \sqrt{0{,}25 + 12} = -0{,}5 \pm 3{,}5 \quad \Rightarrow \quad x_1 = 3, \quad x_2 = -4
```

**d)** $p = -2$, $q = -15$:

```math
x = 1 \pm \sqrt{1 + 15} = 1 \pm 4 \quad \Rightarrow \quad x_1 = 5, \quad x_2 = -3
```

---

### 3.4 – Normera först
**a)** $2x^2 - 10x + 12 = 0$

**b)** $3x^2 + 12x - 15 = 0$

**c)** $-x^2 + 4x - 3 = 0$

---

### Lösning
PQ-formeln kräver att koefficienten framför $x^2$ är $1$.

**a)** Dividera med $2$:

```math
x^2 - 5x + 6 = 0 \quad \Rightarrow \quad x = 2{,}5 \pm \sqrt{6{,}25 - 6} = 2{,}5 \pm 0{,}5
```

```math
x_1 = 3, \quad x_2 = 2
```

**b)** Dividera med $3$:

```math
x^2 + 4x - 5 = 0 \quad \Rightarrow \quad x = -2 \pm \sqrt{4 + 5} = -2 \pm 3
```

```math
x_1 = 1, \quad x_2 = -5
```

**c)** Multiplicera med $-1$:

```math
x^2 - 4x + 3 = 0 \quad \Rightarrow \quad x = 2 \pm \sqrt{4 - 3} = 2 \pm 1
```

```math
x_1 = 3, \quad x_2 = 1
```

Att dividera eller multiplicera hela ekvationen med ett tal skilt från noll ändrar inte rötterna.

---

### 3.5 – Antal reella rötter

---

### Lösning
Uttrycket under rottecknet i PQ-formeln är $\left(\dfrac{p}{2}\right)^2 - q$.

**a)** $p = -6$, $q = 5$: $(-3)^2 - 5 = 4 > 0$ → **två skilda reella rötter**.

**b)** $p = 4$, $q = 4$: $2^2 - 4 = 0$ → **en dubbelrot**.

**c)** $p = 1$, $q = 3$: $0{,}5^2 - 3 = -2{,}75 < 0$ → **inga reella rötter**.

**d)** Dividera med $2$: $x^2 - 2x + 1 = 0$, så $p = -2$, $q = 1$: $(-1)^2 - 1 = 0$ → **en dubbelrot**.

**e)** Dividera med $3$: $x^2 + \dfrac{2}{3}x - \dfrac{1}{3} = 0$, så $p = \dfrac{2}{3}$, $q = -\dfrac{1}{3}$: $\left(\dfrac{1}{3}\right)^2 + \dfrac{1}{3} = \dfrac{4}{9} > 0$ → **två skilda reella rötter**.

Är uttrycket under rottecknet negativt finns ingen reell kvadratrot, och därmed ingen reell lösning.

---

### 3.6 – Kvadratkomplettering
**a)** $x^2 + 4x - 5 = 0$

**b)** $x^2 - 10x + 21 = 0$

**c)** $x^2 + 6x + 4 = 0$

---

### Lösning
**a)** Flytta konstanten och addera $\left(\tfrac{4}{2}\right)^2 = 4$ i båda led:

```math
x^2 + 4x = 5 \quad \Rightarrow \quad x^2 + 4x + 4 = 9 \quad \Rightarrow \quad (x + 2)^2 = 9
```

```math
x + 2 = \pm 3 \quad \Rightarrow \quad x_1 = 1, \quad x_2 = -5
```

**b)** Addera $\left(\tfrac{10}{2}\right)^2 = 25$:

```math
x^2 - 10x = -21 \quad \Rightarrow \quad (x - 5)^2 = 4
```

```math
x - 5 = \pm 2 \quad \Rightarrow \quad x_1 = 7, \quad x_2 = 3
```

**c)** Addera $\left(\tfrac{6}{2}\right)^2 = 9$:

```math
x^2 + 6x = -4 \quad \Rightarrow \quad (x + 3)^2 = 5
```

```math
x + 3 = \pm\sqrt{5} \quad \Rightarrow \quad x = -3 \pm \sqrt{5}
```

```math
x_1 \approx -0{,}76, \quad x_2 \approx -5{,}24
```

Kvadratkompletteringen är samma räkning som PQ-formeln – det är faktiskt så formeln härleds.

---

### 3.7 – Ström ur effekt
$P = RI^2$

---

### Lösning
**a)**

```math
I^2 = \frac{P}{R} = \frac{12{,}5}{50} = 0{,}25 \quad \Rightarrow \quad I = 0{,}5\,\text{A}
```

**b)**

```math
I^2 = \frac{0{,}18}{200} = 9 \times 10^{-4} \quad \Rightarrow \quad I = 3 \times 10^{-2}\,\text{A} = 30\,\text{mA}
```

**c)**

```math
I = \sqrt{\frac{0{,}5}{470}} = \sqrt{1{,}064 \times 10^{-3}} \approx 3{,}3 \times 10^{-2}\,\text{A} \approx 33\,\text{mA}
```

**d)** Ekvationen $I^2 = P/R$ har alltid två rötter, $\pm\sqrt{P/R}$. Den negativa roten motsvarar bara att strömmen går åt andra hållet i kretsen – effekten blir densamma, eftersom $I$ kvadreras. När uppgiften efterfrågar strömmens **storlek** anges därför den positiva roten.

---

### 3.8 – Spänning ur effekt
$P = \dfrac{U^2}{R}$

---

### Lösning
**a)**

```math
U^2 = PR = 5 \times 20 = 100 \quad \Rightarrow \quad U = 10\,\text{V}
```

**b)**

```math
U^2 = 0{,}125 \times 2000 = 250 \quad \Rightarrow \quad U = \sqrt{250} \approx 15{,}8\,\text{V}
```

**c)** Lös ut $R$ i stället:

```math
R = \frac{U^2}{P} = \frac{230^2}{1000} = \frac{52\,900}{1000} = 52{,}9\,\Omega
```

---

### 3.9 – Två motstånd ur summa och produkt

---

### Lösning
Lös ut $R_2$ ur summan och sätt in i produkten, som i uppgift 2.4. Det ger en andragradsekvation i $R_1$, vars två rötter är de två motstånden.

**a)** $R_2 = 20 - R_1$ ger $R_1(20 - R_1) = 96$:

```math
R_1^2 - 20R_1 + 96 = 0 \quad \Rightarrow \quad R_1 = 10 \pm \sqrt{100 - 96} = 10 \pm 2
```

```math
R_1 = 12\,\Omega, \quad R_2 = 8\,\Omega
```

Kontroll: $12 + 8 = 20$ ✓ och $12 \times 8 = 96$ ✓

**b)** $R_2 = 15 - R_1$ ger $R_1(15 - R_1) = 56$:

```math
R_1^2 - 15R_1 + 56 = 0 \quad \Rightarrow \quad R_1 = 7{,}5 \pm \sqrt{56{,}25 - 56} = 7{,}5 \pm 0{,}5
```

```math
R_1 = 8\,\Omega, \quad R_2 = 7\,\Omega
```

**c)** $R_2 = 10 - R_1$ ger $R_1(10 - R_1) = 30$, alltså $R_1^2 - 10R_1 + 30 = 0$. Uttrycket under rottecknet i PQ-formeln blir:

```math
\left(\frac{-10}{2}\right)^2 - 30 = 25 - 30 = -5 < 0
```

Inga reella rötter, alltså **nej** – det finns inga två reella motstånd med den summan och den produkten. Generellt gäller att produkten aldrig kan överstiga kvadraten på halva summan, här $5^2 = 25\thinspace\Omega^2$.

---

### 3.10 – Serie- och parallellresistans samtidigt
$R_1 + R_2 = 10\thinspace\Omega$, $R_1 // R_2 = 2{,}4\thinspace\Omega$

---

### Lösning
**a)** Utgå från produkt genom summa och multiplicera upp:

```math
R_1 // R_2 = \frac{R_1R_2}{R_1 + R_2} \quad \Rightarrow \quad R_1R_2 = (R_1 // R_2)(R_1 + R_2) = 2{,}4 \times 10 = 24\,\Omega^2
```

**b)** Summan ger $R_2 = 10 - R_1$. Insatt i produkten $R_1R_2 = 24$:

```math
R_1(10 - R_1) = 24 \quad \Rightarrow \quad R_1^2 - 10R_1 + 24 = 0 \quad \Rightarrow \quad R_1 = 5 \pm \sqrt{25 - 24} = 5 \pm 1
```

```math
R_1 = 6\,\Omega, \quad R_2 = 4\,\Omega
```

**c)** Kontroll:

```math
R_1 + R_2 = 6 + 4 = 10\,\Omega \quad ✓
```

```math
R_1 // R_2 = \frac{6 \times 4}{6 + 4} = \frac{24}{10} = 2{,}4\,\Omega \quad ✓
```

---

### 3.11 – Effekt i en belastning
$R_1 = 4\thinspace\Omega$, $E = 12\thinspace\text{V}$, $P = 8\thinspace\text{W}$

---

### Lösning
**a)** Sätt in strömmen i effektformeln:

```math
P = RI^2 = R\left(\frac{E}{R_1 + R}\right)^2 = \frac{144R}{(4 + R)^2}
```

Kravet $P = 8$ ger:

```math
\frac{144R}{(4 + R)^2} = 8 \quad \Rightarrow \quad 144R = 8(4 + R)^2 \quad \Rightarrow \quad 18R = (4 + R)^2
```

Utveckla kvadraten och samla alla termer i ett led:

```math
18R = R^2 + 8R + 16 \quad \Rightarrow \quad R^2 - 10R + 16 = 0
```

**b)** PQ-formeln med $p = -10$, $q = 16$:

```math
R = 5 \pm \sqrt{25 - 16} = 5 \pm 3 \quad \Rightarrow \quad R_1' = 8\,\Omega, \quad R_2' = 2\,\Omega
```

**c)** Båda lösningarna är positiva och därmed fysikaliskt möjliga:

```math
R = 2\,\Omega: \quad I = \frac{12}{4 + 2} = 2\,\text{A}, \quad P = 2 \times 2^2 = 8\,\text{W} \quad ✓
```

```math
R = 8\,\Omega: \quad I = \frac{12}{4 + 8} = 1\,\text{A}, \quad P = 8 \times 1^2 = 8\,\text{W} \quad ✓
```

Ett litet motstånd med stor ström ger alltså samma effekt som ett stort motstånd med liten ström.

**d)** Med $R = 4\thinspace\Omega$, alltså lika stort som $R_1$:

```math
I = \frac{12}{8} = 1{,}5\,\text{A}, \qquad P = 4 \times 1{,}5^2 = 9\,\text{W}
```

Det är mer än de $8\thinspace\text{W}$ som de båda rötterna ger. Effekten i lasten är alltså som störst när $R = R_1$, och de två rötterna i **b)** ligger symmetriskt på var sin sida om detta maximum. Sambandet kallas **effektanpassning** och återkommer i kretsteorin.

---

### 3.12 – Sant eller falskt

---

### Lösning
**a)** **Falskt.** Antalet reella rötter avgörs av uttrycket under rottecknet i PQ-formeln: två om det är positivt, en om det är noll och ingen om det är negativt.

**b)** **Falskt** – eller åtminstone ofullständigt. Ekvationen har två rötter, $x = 4$ och $x = -4$. En vanlig miss är att glömma den negativa roten.

**c)** **Falskt.** PQ-formeln kräver normerad form. Dividera först med $2$ till $x^2 + 2x - 3 = 0$, som ger $x = -1 \pm 2$, alltså $x_1 = 1$ och $x_2 = -3$.

**d)** **Sant.** Då försvinner rottermen och båda rötterna blir $-\dfrac{p}{2}$.

**e)** **Sant.** Det är nollproduktmetoden, och den är hela grunden för faktoriseringsmetoden.

**f)** **Sant.** Ekvationen ger $x^2 = -4$, och ingen reell kvadrat är negativ.

---
