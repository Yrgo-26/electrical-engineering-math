# L18 – Handberäkningar
Uppgifterna nedan räknas **för hand**. Det rekommenderas starkt, men är inget krav, att de är klara **före** laborationen i L18. Ta med beräkningarna till lektionen, handskrivna eller digitala och med tydliga mellansteg. Under lektionen skrivs programmen, och resultaten jämförs med era handberäkningar.

> **OBS!** Handberäkningarna kan göras under lektionen, men då ska både beräkning och programmering hinnas med, vilket kan bli stressigt. Gör dem därför gärna i förväg.

Ni får arbeta i grupper om två. Uppgifterna har samma nummer som i [bilaga B](./b_exercises.md), där även programmeringsdelarna finns.

---

## Del 1 – Grunder

### 1.1 – Resistans och effekt
Två resistorer, $R_1 = 220\ \Omega$ och $R_2 = 330\ \Omega$, parallellkopplas över spänningen $U = 12$ V.

**a)** Beräkna parallellresistansen $R_p$.

**b)** Beräkna strömmen $I$ och den utvecklade effekten $P = \dfrac{U^2}{R_p}$.

---

### 1.2 – Decibel
En förstärkare har inspänningen $U_{\text{in}} = 25$ mV och utspänningen $U_{\text{ut}} = 1{,}6$ V.

**a)** Beräkna förstärkningen i dB.

**b)** Ett filter dämpar signalen med $-3$ dB. Beräkna kvoten $U_{\text{ut}}/U_{\text{in}}$ för filtret.

---

### 1.3 – Vinklar och trigonometri
En växelspänning ges av $u(t) = 325\sin(2\pi \cdot 50t)$ V.

**a)** Beräkna $u(t)$ vid $t = 2{,}0$ ms.

**b)** Ange vinkeln $2\pi \cdot 50t$ i både radianer och grader vid denna tidpunkt.

---

## Del 2 – Derivata och integraler

### 2.1 – Derivata
Låt $f(x) = x^3 - 2x + 1$.

**a)** Derivera $f(x)$ analytiskt och beräkna $f'(2)$.

---

### 2.2 – Spänning över en spole
Strömmen genom en spole ges av $i(t) = 5t^2$ A. Spolens induktans är $L = 0{,}20$ H. Spänningen över spolen ges av

```math
u(t) = L \cdot i'(t).
```

**a)** Bestäm $i'(t)$ analytiskt och därmed ett uttryck för $u(t)$.

**b)** Beräkna $u(3)$.

---

### 2.3 – Bestämd integral
Låt $f(x) = x^2$.

**a)** Beräkna $\displaystyle\int_0^3 x^2\thinspace dx$ analytiskt.

---

## Del 3 – Komplexa tal och fasorer

### 3.1 – Räkning med komplexa tal
Låt $z_1 = 4 + 3j$ och $z_2 = 2 - 5j$.

**a)** Beräkna $z_1 + z_2$, $z_1 \cdot z_2$ och $\dfrac{z_1}{z_2}$.

**b)** Beräkna $|z_1|$ och $\arg(z_1)$ i radianer och grader.

---

### 3.2 – Polär och rektangulär form
Ett komplext tal ges på polär form som $z = 10\thinspace\angle\thinspace\dfrac{\pi}{6}$.

**a)** Omvandla $z$ till rektangulär form.

---

### 3.3 – Impedans i en RLC-krets
En seriekrets består av $R = 47\thinspace\Omega$, $L = 100\thinspace\text{mH}$ och $C = 10\thinspace\mu\text{F}$. Kretsen matas med $U = 230\thinspace\text{V}$ vid $f = 50\thinspace\text{Hz}$.

**a)** Beräkna $\omega$, $X_L = \omega L$ och $X_C = \dfrac{1}{\omega C}$.

**b)** Ange den totala impedansen $Z = R + j(X_L - X_C)$ på rektangulär form.

**c)** Beräkna $|Z|$ och $\arg(Z)$ i grader. Är kretsen induktiv eller kapacitiv?

**d)** Beräkna strömmens belopp $|I| = \dfrac{|U|}{|Z|}$.

---

## Del 6 – Linjär regression
En **linjär regressionsmodell** tränas att hitta den räta linjen $y = kx + m$ utifrån ett antal mätpunkter, så kallade **träningsuppsättningar** $(x,\ y_{\text{ref}})$. Modellen går igenom träningsuppsättningarna en i taget, och en genomgång av samtliga kallas en **epok**. Båda parametrarna är noll vid start.

För varje träningsuppsättning:

**1.** Beräkna modellens prediktion $y_p$ för indatan $x$:

```math
y_p = k \cdot x + m
```

**2.** Beräkna avvikelsen $\delta$ mellan referensvärdet och prediktionen:

```math
\delta = y_{\text{ref}} - y_p
```

**3.** Beräkna justeringsmängden $\Delta e$, där $LR$ är **lärhastigheten** (*learning rate*):

```math
\Delta e = \delta \cdot LR
```

**4.** Justera parametrarna:

```math
m = m + \Delta e, \qquad k = k + \Delta e \cdot x
```

### 6.1 – Träning för hand
Träningsdatan följer linjen $y = 2x + 2$:

| $x$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|-----|-----|-----|-----|-----|-----|
| $y_{\text{ref}}$ | $2$ | $4$ | $6$ | $8$ | $10$ |

**a)** Genomför en epok med lärhastigheten $LR = 0{,}1$, med start i $k = 0$ och $m = 0$. Redovisa $y_p$, $\delta$, $\Delta e$, $k$ och $m$ efter varje träningsuppsättning. Avrunda till fyra decimaler.

**b)** Har $k$ och $m$ närmat sig de rätta värdena $k = 2$ och $m = 2$?

---

### 6.4 – Egen träningsdata
I L08, uppgift 2.6, mättes spänningen $U(t)$ under en urladdning:

| $t$ (s) | $0$ | $1$ | $2$ | $3$ | $4$ |
|---------|-----|-----|-----|-----|-----|
| $U(t)$ (V) | $12$ | $9$ | $6$ | $3$ | $0$ |

**a)** Bestäm $k$ och $m$ i $U(t) = kt + m$, eller hämta dem från er lösning i L08.

---

## Del 7 – Ett neuralt nätverk
I ett **neuralt nätverk** har varje **nod** flera insignaler, var och en med en egen vikt. För en nod med insignalerna $x_1$ och $x_2$, vikterna $w_1$ och $w_2$ samt biasvärdet $b$ beräknas först den viktade summan

```math
z = w_1 x_1 + w_2 x_2 + b
```

Summan skickas sedan genom en **aktiveringsfunktion** $f$, så att nodens utsignal blir $y = f(z)$. Två vanliga aktiveringsfunktioner är:
* **ReLU**, som nollställer negativa summor: $f(z) = \max(0, z)$.
* **Tangens hyperbolicus**, som pressar ihop alla reella tal till intervallet $(-1, 1)$:

```math
\tanh(z) = \frac{e^{z} - e^{-z}}{e^{z} + e^{-z}}
```

### 7.1 – Feedforward för hand
En nod har vikterna $w_1 = 0{,}5$ och $w_2 = -1$ samt biasvärdet $b = 0{,}2$.

**a)** Beräkna summan $z$ för insignalerna $(x_1, x_2) = (1, 0)$ och $(x_1, x_2) = (1, 1)$.

**b)** Beräkna nodens utsignal med ReLU för båda fallen.

**c)** Beräkna nodens utsignal med $\tanh$ för fallet $(1, 0)$. Avrunda till fyra decimaler.

---

### 7.4 – Varför räcker inte en rät linje?
I laborationen tränas ett nätverk att ge utsignalen $1$ när de två insignalerna är olika, och $0$ när de är lika:

| $x_1$ | $x_2$ | $y$ |
|-------|-------|-----|
| $0$ | $0$ | $0$ |
| $0$ | $1$ | $1$ |
| $1$ | $0$ | $1$ |
| $1$ | $1$ | $0$ |

En enda nod utan aktiveringsfunktion ger $z = w_1 x_1 + w_2 x_2 + b$, och sambandet $z = 0$ är en rät linje i $x_1 x_2$-planet. Noden kan alltså bara skilja punkter på olika sidor om en linje.

**a)** Rita de fyra punkterna $(0, 0)$, $(0, 1)$, $(1, 0)$ och $(1, 1)$ i ett koordinatsystem, och markera vilka som ska ge utsignalen $1$.

**b)** Går det att dra en enda rät linje som skiljer punkterna som ska ge $1$ från punkterna som ska ge $0$? Vad säger det om varför nätverket behöver ett dolt lager?
