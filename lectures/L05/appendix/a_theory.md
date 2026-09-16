# Bilaga A – Potenser, rötter och talsystem

## 1. Potenser
En **potens** är upprepad multiplikation av ett tal med sig självt:

```math
a^n = \underbrace{a \times a \times \cdots \times a}_{n \text{ faktorer}}
```

Här kallas $a$ **bas** och $n$ **exponent**.

**Exempel:**

```math
2^4 = 2 \times 2 \times 2 \times 2 = 16, \qquad 10^3 = 1\,000
```

---

## 2. Potensregler
Följande sju regler gäller för alla $a \neq 0$ och $b \neq 0$.

| # | Regel | Formel |
|---|-------|--------|
| 1 | Produktregeln | $a^m \cdot a^n = a^{m+n}$ |
| 2 | Kvotregeln | $\dfrac{a^m}{a^n} = a^{m-n}$ |
| 3 | Potens av potens | $(a^m)^n = a^{m \cdot n}$ |
| 4 | Potens av produkt | $(a \cdot b)^n = a^n \cdot b^n$ |
| 5 | Potens av kvot | $\left(\dfrac{a}{b}\right)^n = \dfrac{a^n}{b^n}$ |
| 6 | Nollexponent | $a^0 = 1$ |
| 7 | Negativ exponent | $a^{-n} = \dfrac{1}{a^n}$ |

**Exempel på regel 1:**

```math
10^3 \cdot 10^4 = 10^{3+4} = 10^7
```

**Exempel på regel 7:**

```math
10^{-3} = \frac{1}{10^3} = \frac{1}{1000} = 0{,}001
```

---

## 3. Rötter
**Kvadratroten** av $a$ ($a \geq 0$) är det icke-negativa tal vars kvadrat är $a$:

```math
\sqrt{a} = a^{1/2} \quad \text{eftersom} \quad \left(\sqrt{a}\right)^2 = a
```

**n:te roten** av $a$ är det tal vars n:te potens är $a$:

```math
\sqrt[n]{a} = a^{1/n}
```

### Bråkexponenter
Rötter och potenser kombineras via bråkexponenter:

```math
a^{m/n} = \sqrt[n]{a^m} = \left(\sqrt[n]{a}\right)^m
```

**Exempel:**

```math
8^{2/3} = \left(\sqrt[3]{8}\right)^2 = 2^2 = 4
```

### Räkneregler för rötter

```math
\sqrt{a \cdot b} = \sqrt{a} \cdot \sqrt{b}, \qquad \sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}
```

**OBS!** $\sqrt{a + b} \neq \sqrt{a} + \sqrt{b}$ – detta är ett vanligt misstag!

---

## 4. Standardform (vetenskaplig notation)
I elektroteknik förekommer extremt stora och extremt små tal: $R = 1\thinspace 000\thinspace 000\thinspace\Omega$, $C = 0{,}000\thinspace 000\thinspace 001\thinspace\text{F}$.

**Standardform** skriver talet som $a \times 10^n$ där $1 \leq a < 10$:

```math
1\,000\,000 = 1{,}0 \times 10^6, \qquad 0{,}000\,000\,001 = 1{,}0 \times 10^{-9}
```

### SI-prefix

| Prefix | Symbol | Faktor |
|--------|--------|--------|
| Giga | G | $10^9$ |
| Mega | M | $10^6$ |
| Kilo | k | $10^3$ |
| Milli | m | $10^{-3}$ |
| Mikro | μ | $10^{-6}$ |
| Nano | n | $10^{-9}$ |
| Piko | p | $10^{-12}$ |

**Exempel:** $4{,}7\thinspace\text{k}\Omega = 4{,}7 \times 10^3\thinspace\Omega = 4\thinspace 700\thinspace\Omega$

**Exempel:** $33\thinspace\text{nF} = 33 \times 10^{-9}\thinspace\text{F} = 3{,}3 \times 10^{-8}\thinspace\text{F}$

---

## 5. Räkning med standardform
**Multiplikation:**

```math
(3 \times 10^4) \times (2 \times 10^3) = 6 \times 10^7
```

**Division:**

```math
\frac{6 \times 10^6}{2 \times 10^2} = 3 \times 10^4
```

**Addition** (måste ha samma exponent):

```math
3{,}5 \times 10^3 + 2{,}0 \times 10^3 = 5{,}5 \times 10^3
```

---

## 6. Värdesiffror och avrundning
**Värdesiffror** är de siffror som bär meningsfull information i ett mätvärde.
* $4\thinspace 700\thinspace\Omega$ – kan ha 2, 3 eller 4 värdesiffror (oklart utan kontext)
* $4{,}70 \times 10^3\thinspace\Omega$ – har tydligt **3 värdesiffror**

Resultatet av en beräkning bör normalt anges med lika många värdesiffror som det minst exakta indata.

**Avrundningsregel:** Om siffran efter avrundningspositionen är $\geq 5$, runda upp; annars runda ned.

---

## 7. Tillämpning: Effektberäkning
Effekten dissiperad i ett motstånd $R$ vid spänningen $U$:

```math
P = \frac{U^2}{R}
```

**Exempel:** $U = 6\thinspace\text{V}$, $R = 50\thinspace\Omega$:

```math
P = \frac{6^2}{50} = \frac{36}{50} = 0{,}72\,\text{W}
```

**Effekten vid given ström:**

```math
P = RI^2
```

**Exempel:** $I = 20\thinspace\text{mA} = 20 \times 10^{-3}\thinspace\text{A}$, $R = 1\thinspace\text{k}\Omega = 10^3\thinspace\Omega$:

```math
P = 10^3 \times (20 \times 10^{-3})^2 = 10^3 \times 400 \times 10^{-6} = 0{,}4\,\text{W}
```

---

## 8. Binära och hexadecimala tal
Vårt vanliga talsystem är ett **positionssystem** med basen $10$: en siffras värde beror på var i talet den står, och varje position motsvarar en tiopotens. Positionen längst till höger har värdet $10^0 = 1$:

```math
4\,703 = 4 \cdot 10^3 + 7 \cdot 10^2 + 0 \cdot 10^1 + 3 \cdot 10^0
```

Samma idé fungerar med vilken bas som helst. Inom digitalteknik och programmering används, utöver det decimala talsystemet, även det **binära** och det **hexadecimala**. Tabellen visar talet $45$ i alla tre:

| Talsystem | Bas | Siffror | Skrivsätt | I C |
|-----------|-----|---------|-----------|-----|
| Decimalt | $10$ | 0–9 | $45$ | `45` |
| Binärt | $2$ | 0 och 1 | $101101_2$ | `0b101101` |
| Hexadecimalt | $16$ | 0–9 och A–F | $\mathrm{2D}_{16}$ | `0x2D` |

De hexadecimala siffrorna A–F betyder $10$–$15$. Den lilla siffran efter talet anger basen; saknas den är talet decimalt.

En binär siffra kallas **bit**, och åtta bitar kallas en **byte**. Med $n$ bitar kan $2^n$ olika värden lagras, från $0$ till $2^n - 1$. En byte rymmer alltså $2^8 = 256$ olika värden, $0$–$255$.

### Från binärt eller hexadecimalt till decimalt
Multiplicera varje siffra med positionens värde och summera. Positionerna numreras från höger med början på $0$, så position $n$ har värdet $2^n$ i ett binärtal och $16^n$ i ett hexadecimalt tal:

| Position $n$ | $7$ | $6$ | $5$ | $4$ | $3$ | $2$ | $1$ | $0$ |
|--------------|-----|-----|-----|-----|-----|-----|-----|-----|
| $2^n$ | $128$ | $64$ | $32$ | $16$ | $8$ | $4$ | $2$ | $1$ |

För hexadecimala tal räcker oftast $16^0 = 1$, $16^1 = 16$, $16^2 = 256$ och $16^3 = 4\thinspace 096$.

**Exempel:**

```math
1011_2 = 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0 = 8 + 0 + 2 + 1 = 11
```

**Exempel:** F betyder $15$:

```math
\mathrm{2F}_{16} = 2 \cdot 16^1 + 15 \cdot 16^0 = 32 + 15 = 47
```

### Från decimalt till binärt eller hexadecimalt
Dividera talet med basen upprepade gånger och anteckna resten varje gång, tills kvoten blir $0$. Resterna, lästa **nerifrån och upp**, är talet i den nya basen.

**Exempel:** Omvandla $13$ till binär form.

| Division | Kvot | Rest |
|----------|------|------|
| $13 / 2$ | $6$ | $1$ |
| $6 / 2$ | $3$ | $0$ |
| $3 / 2$ | $1$ | $1$ |
| $1 / 2$ | $0$ | $1$ |

Resterna nerifrån och upp ger $13 = 1101_2$. Kontroll: $8 + 4 + 0 + 1 = 13$ ✓

**Exempel:** Omvandla $470$ till hexadecimal form. En rest mellan $10$ och $15$ skrivs med en bokstav.

| Division | Kvot | Rest |
|----------|------|------|
| $470 / 16$ | $29$ | $6$ |
| $29 / 16$ | $1$ | $13 = \mathrm{D}$ |
| $1 / 16$ | $0$ | $1$ |

Resterna nerifrån och upp ger $470 = \mathrm{1D6}_{16}$. Kontroll: $1 \cdot 256 + 13 \cdot 16 + 6 = 470$ ✓

> **Tips:** Miniräknaren ger kvoten som decimaltal. $470 / 16 = 29{,}375$ betyder kvoten $29$ och resten $0{,}375 \cdot 16 = 6$.

### Mellan binärt och hexadecimalt
Eftersom $16 = 2^4$ motsvarar varje hexadecimal siffra exakt fyra bitar:

| Hex | Binärt | Hex | Binärt | Hex | Binärt | Hex | Binärt |
|-----|--------|-----|--------|-----|--------|-----|--------|
| 0 | 0000 | 4 | 0100 | 8 | 1000 | C | 1100 |
| 1 | 0001 | 5 | 0101 | 9 | 1001 | D | 1101 |
| 2 | 0010 | 6 | 0110 | A | 1010 | E | 1110 |
| 3 | 0011 | 7 | 0111 | B | 1011 | F | 1111 |

**Från binärt till hexadecimalt:** dela in bitarna i grupper om fyra, **från höger**, fyll vid behov på med nollor till vänster och byt varje grupp mot sin hexadecimala siffra:

```math
1011\,0110_2 = \underbrace{1011}_{\mathrm{B}}\;\underbrace{0110}_{6} = \mathrm{B6}_{16}
```

**Från hexadecimalt till binärt:** byt varje siffra mot sina fyra bitar:

```math
\mathrm{4D}_{16} = \underbrace{0100}_{4}\;\underbrace{1101}_{\mathrm{D}} = 0100\,1101_2
```

En byte motsvarar alltså exakt två hexadecimala siffror, från `0x00` till `0xFF`. Därför skrivs till exempel innehållet i en mikrokontrollers register ofta hexadecimalt: `0xB6` är lättare att läsa än `0b10110110`.

**OBS!** I datorsammanhang används ibland kilo för $2^{10} = 1\thinspace 024$ i stället för $1\thinspace 000$. Den entydiga beteckningen är **kibi** (Ki): $1\thinspace\text{KiB} = 1\thinspace 024$ byte.

---

## 9. Sammanfattning

| Begrepp | Nyckelformel |
|---------|-------------|
| Produktregeln | $a^m \cdot a^n = a^{m+n}$ |
| Kvotregeln | $a^m / a^n = a^{m-n}$ |
| Potens av potens | $(a^m)^n = a^{mn}$ |
| Negativ exponent | $a^{-n} = 1/a^n$ |
| Kvadratrot | $\sqrt{a} = a^{1/2}$ |
| Bråkexponent | $a^{m/n} = \sqrt[n]{a^m}$ |
| Standardform | $a \times 10^n$, $1 \leq a < 10$ |
| Positionssystem | $1011_2 = 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0 = 11$ |
| Binärt och hexadecimalt | En hexadecimal siffra motsvarar fyra bitar |
| Antal värden med $n$ bitar | $2^n$, från $0$ till $2^n - 1$ |

---
