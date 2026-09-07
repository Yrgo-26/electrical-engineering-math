# Lösningsförslag – Övningsdugga 2

### Uppgift 1 (1,0 poäng)
$\mathbf{u} = (1;\thinspace 2)$, $\mathbf{v} = (-3;\thinspace 4)$.

---
### Lösning
**a)** $\mathbf{u}$ har x-koordinat 1 och y-koordinat 2. $\mathbf{v}$ har x-koordinat $-3$ och y-koordinat 4. Rita upp i koordinatsystemet.

**b)** Absolutbeloppen beräknas med Pythagoras sats:

```math
|\mathbf{u}| = \sqrt{1^2 + 2^2} = \sqrt{5} \approx 2{,}24
```

```math
|\mathbf{v}| = \sqrt{(-3)^2 + 4^2} = \sqrt{25} = 5
```

**c)** Vinklarna beräknas med $v = \arctan(y/x) \pm 180°$:

```math
v_u = \arctan\!\left(\frac{2}{1}\right) \approx 63{,}4°
```

$\mathbf{v}$ ligger i kvadrant II – lägg till $180°$:

```math
v_v = \arctan\!\left(\frac{4}{-3}\right) + 180° \approx -53{,}1° + 180° = 126{,}9°
```

**d)**

```math
\mathbf{w} = 2(1;\,2) - (-3;\,4) = (2;\,4) + (3;\,-4) = (5;\,0)
```

---
### Uppgift 2 (1,0 poäng)
Förenkla $f(x) = \dfrac{x^2 - x - 2}{x - 2}$.

---
### Lösning
Nämnaren är noll när $x = 2$, så $x \neq 2$.

Faktorisera täljaren med PQ-formeln ($x^2 - x - 2 = 0 \Rightarrow x = 2$ eller $x = -1$):

```math
x^2 - x - 2 = (x + 1)(x - 2)
```

Förkorta faktorn $(x - 2)$:

```math
f(x) = \frac{(x+1)(x-2)}{x-2} = x + 1, \quad x \neq 2
```

---
### Uppgift 3 (1,0 poäng)
Kondensator $C = 470\thinspace\mu\text{F}$, $R = 10\thinspace\text{k}\Omega$, $U_0 = 12\thinspace\text{V}$.

---
### Lösning
Tidskonstanten $RC = 470 \times 10^{-6} \cdot 10 \times 10^3 = 4{,}7\thinspace\text{s}$.

```math
u(t) = 12e^{-t/4{,}7}\,\text{V}
```

**a)**

```math
u(5) = 12e^{-5/4{,}7} \approx 4{,}14\,\text{V}
```

**b)** Definitionsmängd: $0 \leq t \leq 20\thinspace\text{s}$.

```math
u(0) = 12\,\text{V}, \quad u(20) = 12e^{-20/4{,}7} \approx 0{,}17\,\text{V}
```

Värdemängd: $0{,}17\thinspace\text{V} \leq u(t) \leq 12\thinspace\text{V}$

**c)** Sätt $u(t) = 6\thinspace\text{V}$:

```math
12e^{-t/4{,}7} = 6 \quad \Rightarrow \quad e^{-t/4{,}7} = 0{,}5
```

Ta naturliga logaritmen i båda led:

```math
-\frac{t}{4{,}7} = \ln 0{,}5 \quad \Rightarrow \quad t = -4{,}7 \cdot \ln 0{,}5 \approx 3{,}26\,\text{s}
```

---
### Uppgift 4 (1,0 poäng)
Amplitud $5\thinspace\text{V}$, frekvens $100\thinspace\text{Hz}$, fas $90°$.

---
### Lösning
**a)** Omvandla fasen: $\delta = 90° \cdot \dfrac{\pi}{180°} = \dfrac{\pi}{2}\thinspace\text{rad}$

Vinkelhastigheten: $\omega = 2\pi f = 2\pi \cdot 100 = 200\pi\thinspace\text{rad/s}$

```math
u(t) = 5\sin\!\left(200\pi t + \frac{\pi}{2}\right)\,\text{V}
```

**b)** Periodtiden: $T = 1/f = 10\thinspace\text{ms}$. Fasen $\pi/2$ innebär att kurvan är $T/4 = 2{,}5\thinspace\text{ms}$ förskjuten till vänster (tidigt). Rita sinuskurvan med amplituden $5\thinspace\text{V}$ och perioden $10\thinspace\text{ms}$, med toppvärdet vid $t = 0$.

---
### Uppgift 5 (1,0 poäng)
Förstärkning $G_{\text{dB}} = 32\thinspace\text{dB}$.

---
### Lösning
Använd formeln för linjär spänningsförstärkning:

```math
G_{\text{dB}} = 20\log_{10} G_{\text{lin}} \quad \Rightarrow \quad \log_{10} G_{\text{lin}} = \frac{G_{\text{dB}}}{20}
```

Upphöj med basen 10 i båda led:

```math
G_{\text{lin}} = 10^{G_{\text{dB}}/20} = 10^{32/20} = 10^{1{,}6} \approx 39{,}8
```

Förstärkningen motsvarar ungefär $\mathbf{40}$ gångers spänningsförstärkning.

---
