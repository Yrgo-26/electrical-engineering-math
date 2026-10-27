# L11 – Lösningsförslag till repetitionsuppgifter

## Del 1 – Vektorer (L07)
### 1.1 – Räkning med vektorer
$\mathbf{u} = (2;\thinspace 5)$, $\mathbf{v} = (-3;\thinspace 1)$

---

### Lösning
Vektorer adderas och multipliceras komponentvis.

**a)**

```math
\mathbf{u} + \mathbf{v} = (2 - 3;\; 5 + 1) = (-1;\, 6)
```

**b)**

```math
\mathbf{u} - \mathbf{v} = (2 + 3;\; 5 - 1) = (5;\, 4)
```

**c)**

```math
3\mathbf{u} = (6;\, 15)
```

**d)**

```math
2\mathbf{u} - 3\mathbf{v} = (4;\, 10) - (-9;\, 3) = (13;\, 7)
```

---

### 1.2 – Belopp och vinkel

---

### Lösning
**a)**

```math
|(8;\, 6)| = \sqrt{64 + 36} = \sqrt{100} = 10
```

**b)**

```math
|(-5;\, -12)| = \sqrt{25 + 144} = \sqrt{169} = 13
```

**c)** Kvadrant I, ingen korrigering:

```math
v = \arctan\!\left(\frac{6}{8}\right) \approx 36{,}9°
```

**d)** Båda komponenterna är negativa, alltså kvadrant III – lägg till $180°$:

```math
v = \arctan\!\left(\frac{-12}{-5}\right) + 180° \approx 67{,}4° + 180° = 247{,}4°
```

---

### 1.3 – Skalärprodukt

---

### Lösning
**a)**

```math
\mathbf{u} \cdot \mathbf{v} = 3 \cdot 2 + 1 \cdot (-6) = 6 - 6 = 0
```

**b)** Skalärprodukten är noll, alltså är $\cos\alpha = 0$ och vektorerna **vinkelräta**.

**c)** Skalärprodukten och beloppen ger:

```math
\mathbf{u} \cdot \mathbf{v} = 1 \cdot 3 + 2 \cdot 1 = 5, \qquad |\mathbf{u}| = \sqrt{5}, \qquad |\mathbf{v}| = \sqrt{10}
```

```math
\cos\alpha = \frac{5}{\sqrt{5}\sqrt{10}} = \frac{5}{\sqrt{50}} \approx 0{,}707 \quad \Rightarrow \quad \alpha = 45°
```

---

### 1.4 – Enhetsvektor och given längd
$\mathbf{v} = (-8;\thinspace 6)$

---

### Lösning
**a)** Först längden, sedan division:

```math
|\mathbf{v}| = \sqrt{64 + 36} = 10 \quad \Rightarrow \quad \hat{\mathbf{v}} = \frac{1}{10}(-8;\, 6) = (-0{,}8;\, 0{,}6)
```

**b)** Multiplicera enhetsvektorn med $25$:

```math
25 \cdot (-0{,}8;\, 0{,}6) = (-20;\, 15)
```

Kontroll: $\sqrt{400 + 225} = \sqrt{625} = 25$ ✓

**c)** Multiplicera med $-5$:

```math
-5 \cdot (-0{,}8;\, 0{,}6) = (4;\, -3)
```

---

### 1.5 – Spänningar som visare
$\mathbf{U}_R = (9;\thinspace 0)\thinspace\text{V}$, $\mathbf{U}_C = (0;\thinspace -12)\thinspace\text{V}$

---

### Lösning
**a)**

```math
\mathbf{U} = (9;\, -12)\,\text{V}
```

**b)**

```math
|\mathbf{U}| = \sqrt{81 + 144} = \sqrt{225} = 15\,\text{V}
```

**c)** Kvadrant IV, ingen korrigering:

```math
v = \arctan\!\left(\frac{-12}{9}\right) \approx -53{,}1°
```

Den negativa vinkeln visar att den totala spänningen ligger efter motståndets spänning – kretsen är kapacitiv.

**d)** Spänningarna är vinkelräta mot varandra, så de adderas geometriskt och inte aritmetiskt. Resultatet är hypotenusan i en rätvinklig triangel, vilket alltid är kortare än summan av kateterna.

---

## Del 2 – Funktioner (L08)
### 2.1 – Definitions- och värdemängd

---

### Lösning
**a)** Uttrycket under roten måste vara icke-negativt, och roten själv är alltid icke-negativ:

```math
D_f = [2, \infty), \qquad V_f = [0, \infty)
```

**b)** Nämnaren får inte vara noll, och kvoten kan aldrig bli noll:

```math
D_f = \mathbb{R} \setminus \lbrace -1 \rbrace, \qquad V_f = \mathbb{R} \setminus \lbrace 0 \rbrace
```

**c)** En nedåtvänd parabel med maximum $f(0) = 4$:

```math
D_f = \mathbb{R}, \qquad V_f = (-\infty, 4]
```

---

### 2.2 – Linjär modell för en termistor
$R(0) = 200\thinspace\Omega$, $R(40) = 120\thinspace\Omega$

---

### Lösning
**a)** Lutningen ur de två punkterna, och $m$ direkt ur $R(0)$:

```math
k = \frac{120 - 200}{40 - 0} = \frac{-80}{40} = -2, \qquad m = 200
```

```math
R(T) = -2T + 200
```

**b)**

```math
R(25) = -50 + 200 = 150\,\Omega
```

**c)**

```math
-2T + 200 = 100 \quad \Rightarrow \quad T = 50^\circ\text{C}
```

**d)** Avtagande, eftersom $k < 0$. Resistansen sjunker med $2\thinspace\Omega$ per grad – det är en NTC-termistor.

---

### 2.3 – Exponentiell modell

---

### Lösning
**a)** Förändringsfaktorn är $1 - 0{,}15 = 0{,}85$:

```math
f(x) = 80 \cdot 0{,}85^{\,x}
```

**b)**

```math
f(6) = 80 \cdot 0{,}85^6 \approx 80 \cdot 0{,}377 \approx 30
```

**c)** Sätt $f(x) = 20$ och logaritmera:

```math
0{,}85^{\,x} = 0{,}25 \quad \Rightarrow \quad x = \frac{\log 0{,}25}{\log 0{,}85} \approx \frac{-0{,}602}{-0{,}0706} \approx 8{,}5
```

Efter **9 hela månader** är antalet fel under $20$.

---

### 2.4 – Effekt som potensfunktion
$P(I) = 25I^2$, $0 \leq I \leq 2\thinspace\text{A}$

---

### Lösning
**a)**

```math
P(0{,}4) = 25 \cdot 0{,}16 = 4\,\text{W}
```

**b)**

```math
P(2) = 25 \cdot 4 = 100\,\text{W}
```

**c)** Funktionen är växande på intervallet, så ändpunkterna ger värdemängden:

```math
V_P = [0, 100]\,\text{W}
```

**d)**

```math
25I^2 = 36 \quad \Rightarrow \quad I^2 = 1{,}44 \quad \Rightarrow \quad I = 1{,}2\,\text{A}
```

Den negativa roten förkastas eftersom strömmens storlek söks.

---

### 2.5 – Rationell funktion

---

### Lösning
**a)** Konjugatregeln:

```math
x^2 - 9 = (x + 3)(x - 3)
```

**b)** Nämnaren är noll när $x = 3$, alltså $x \neq 3$.

**c)** Förkorta den gemensamma faktorn:

```math
f(x) = \frac{(x + 3)(x - 3)}{x - 3} = x + 3, \qquad x \neq 3
```

**d)**

```math
x + 3 = 0 \quad \Rightarrow \quad x = -3
```

---

## Del 3 – Trigonometri (L09)
### 3.1 – Vinkelmått

---

### Lösning
**a)** $135° = \dfrac{135\pi}{180} = \dfrac{3\pi}{4}$

**b)** $-120° = -\dfrac{120\pi}{180} = -\dfrac{2\pi}{3}$

**c)** $\dfrac{5\pi}{6} = \dfrac{5 \cdot 180°}{6} = 150°$

**d)** $2\thinspace\text{rad} = \dfrac{2 \cdot 180°}{\pi} \approx 114{,}6°$

---

### 3.2 – Egenskaper ur ekvationen
$u(t) = 6\sin\left(400\pi t - \dfrac{\pi}{3}\right)$ V

---

### Lösning
**a)** $|U| = 6\thinspace\text{V}$

**b)**

```math
\omega = 400\pi\,\text{rad/s}, \qquad f = \frac{\omega}{2\pi} = 200\,\text{Hz}
```

**c)**

```math
T = \frac{1}{200} = 5\,\text{ms}
```

**d)** Fasen $-\dfrac{\pi}{3}$ motsvarar $-60°$, alltså en sjättedel av ett varv:

```math
\frac{60}{360} \cdot 5\,\text{ms} \approx 0{,}83\,\text{ms}
```

Fasen är **negativ**, så kurvan är **sen** – den når sina värden $0{,}83\thinspace\text{ms}$ senare än en ofasad sinuskurva.

---

### 3.3 – Skriv ekvationen
$|U| = 12\thinspace\text{V}$, $T = 2\thinspace\text{ms}$, $\delta = 30°$

---

### Lösning
Frekvensen ur periodtiden, sedan vinkelhastigheten och fasen i radianer:

```math
f = \frac{1}{2 \times 10^{-3}} = 500\,\text{Hz}, \qquad \omega = 2\pi \cdot 500 = 1000\pi\,\text{rad/s}
```

```math
\delta = 30° \cdot \frac{\pi}{180°} = \frac{\pi}{6}
```

```math
u(t) = 12\sin\!\left(1000\pi t + \frac{\pi}{6}\right)\,\text{V}
```

---

### 3.4 – Momentanvärde, effektivvärde och effekt
$u(t) = 8\sin(100\pi t)$ V

---

### Lösning
**a)** Vinkeln blir $100\pi \cdot 0{,}005 = \dfrac{\pi}{2}$:

```math
u(5\,\text{ms}) = 8\sin\frac{\pi}{2} = 8\,\text{V}
```

**b)**

```math
U_{\text{RMS}} = \frac{8}{\sqrt{2}} \approx 5{,}66\,\text{V}
```

**c)** Effekten beräknas ur effektivvärdet:

```math
P = \frac{U_{\text{RMS}}^2}{R} = \frac{64/2}{50} = \frac{32}{50} = 0{,}64\,\text{W}
```

---

### 3.5 – Trigonometrisk ekvation
$u(t) = 10\sin(200\pi t)$ V

---

### Lösning
Periodtiden är $T = \dfrac{2\pi}{200\pi} = 10\thinspace\text{ms}$.

**a)** Sätt $u(t) = 5$ och dividera med $10$:

```math
\sin(200\pi t) = 0{,}5 \quad \Rightarrow \quad 200\pi t = \frac{\pi}{6} \quad \Rightarrow \quad t = \frac{1}{1200}\,\text{s} \approx 0{,}83\,\text{ms}
```

**b)** Den andra lösningen i samma halvperiod:

```math
200\pi t = \frac{5\pi}{6} \quad \Rightarrow \quad t = \frac{5}{1200}\,\text{s} \approx 4{,}17\,\text{ms}
```

**c)** Toppvärdet nås vid vinkeln $\dfrac{\pi}{2}$:

```math
200\pi t = \frac{\pi}{2} \quad \Rightarrow \quad t = 2{,}5\,\text{ms}
```

Det ligger mitt emellan svaren i **a)** och **b)**, precis som väntat av symmetriskäl.

---

## Del 4 – Logaritmer och decibel (L10)
### 4.1 – Exponential- och logaritmekvationer

---

### Lösning
**a)** $128 = 2^7$:

```math
x = 7
```

**b)**

```math
x = \log 500 \approx 2{,}70
```

**c)**

```math
2x = \ln 5 \approx 1{,}609 \quad \Rightarrow \quad x \approx 0{,}805
```

**d)**

```math
x - 1 = 10^2 = 100 \quad \Rightarrow \quad x = 101
```

---

### 4.2 – Logaritmlagarna

---

### Lösning
**a)**

```math
\log 4 + \log 25 = \log 100 = 2
```

**b)**

```math
\log 500 - \log 5 = \log 100 = 2
```

**c)**

```math
3\log 2 = \log 2^3 = \log 8
```

**d)**

```math
\ln e^3 = 3
```

---

### 4.3 – Förstärkning i dB
$U_{\text{in}} = 20\thinspace\text{mV}$, $U_{\text{ut}} = 2\thinspace\text{V}$

---

### Lösning
**a)** Kvoten är $\dfrac{2}{0{,}020} = 100$:

```math
G_{\text{dB}} = 20\log 100 = 40\,\text{dB}
```

**b)** Dämpningen räknas som negativ förstärkning:

```math
G_{\text{TOT}} = 40 - 12 = 28\,\text{dB}
```

**c)**

```math
G_{\text{lin}} = 10^{28/20} = 10^{1{,}4} \approx 25{,}1
```

**d)**

```math
U_{\text{ut}} = 25{,}1 \times 0{,}020 \approx 0{,}50\,\text{V}
```

---

### 4.4 – Effekt i dB och dBm

---

### Lösning
**a)** Effekt ger faktorn $10$, inte $20$:

```math
G_{\text{dB}} = 10\log\frac{50}{2} = 10\log 25 \approx 14{,}0\,\text{dB}
```

**b)** Lös ut effekten ur $P_{\text{dBm}} = 10\log\dfrac{P}{1\thinspace\text{mW}}$:

```math
P = 10^{20/10} = 10^2 = 100\,\text{mW}
```

**c)** $1\thinspace\text{W} = 1000\thinspace\text{mW}$:

```math
P_{\text{dBm}} = 10\log 1000 = 30\,\text{dBm}
```

---

### 4.5 – Urladdning av en kondensator
$u(t) = 12e^{-t/(RC)}$ V, $R = 22\thinspace\text{k}\Omega$, $C = 100\thinspace\mu\text{F}$

---

### Lösning
**a)**

```math
\tau = RC = \left(22 \times 10^3\right)\left(100 \times 10^{-6}\right) = 2{,}2\,\text{s}
```

**b)**

```math
u(3) = 12e^{-3/2{,}2} = 12e^{-1{,}364} \approx 12 \cdot 0{,}256 \approx 3{,}07\,\text{V}
```

**c)** Sätt $u(t) = 6$ och logaritmera:

```math
e^{-t/\tau} = 0{,}5 \quad \Rightarrow \quad -\frac{t}{\tau} = \ln 0{,}5 \quad \Rightarrow \quad t = \tau\ln 2 \approx 2{,}2 \cdot 0{,}693 \approx 1{,}53\,\text{s}
```

Halveringstiden beror alltså bara på tidskonstanten, inte på startspänningen.

**d)** Samma metod med $u(t) = 1$:

```math
e^{-t/\tau} = \frac{1}{12} \quad \Rightarrow \quad t = \tau\ln 12 \approx 2{,}2 \cdot 2{,}485 \approx 5{,}47\,\text{s}
```

Det är ungefär $2{,}5$ tidskonstanter.

---
