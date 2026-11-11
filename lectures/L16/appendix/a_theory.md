# Bilaga A – Komplexa tal (del II)

## 1. Eulers formel
**Eulers formel** kopplar samman komplexa exponenter och trigonometri:

```math
e^{j\delta} = \cos\delta + j\sin\delta
```

Det innebär att varje komplext tal kan skrivas på **Eulerform**:

```math
z = |z| \cdot e^{j\delta}
```

---

## 2. Tre former av komplexa tal

| Form | Notation | Kommentar |
|------|---------|-----------|
| Rektangulär | $x + jy$ | Bäst för addition/subtraktion |
| Polär | $\lvert z\rvert\thinspace\angle\thinspace\delta$ | Tydlig geometrisk tolkning |
| Eulerform | $\lvert z\rvert\thinspace e^{j\delta}$ | Bäst för multiplikation/division |

**Multiplikation i polär form:**

```math
z_1 \cdot z_2 = |z_1||z_2|\,\angle\,(\delta_1 + \delta_2)
```

**Division i polär form:**

```math
\frac{z_1}{z_2} = \frac{|z_1|}{|z_2|}\,\angle\,(\delta_1 - \delta_2)
```

---

## 3. Fasor
En **fasor** är ett komplext tal som representerar en sinusformad signal. En spänning $u(t) = |U|\sin(\omega t + \delta)$ representeras av fasorn:

```math
U = |U|\,\angle\,\delta = |U|e^{j\delta}
```

Fasorer förenklar beräkningar med sinusvågor i elektriska kretsar – addition av sinusvågor reduceras till addition av komplexa tal.

---

## 4. Omskrivning: Eulerform ↔ tidsdomän

**Fasor → tidsdomän:**

```math
U = |U|e^{j\delta} \quad \Rightarrow \quad u(t) = |U|\sin(\omega t + \delta)
```

**Tidsdomän → fasor:**

```math
u(t) = |U|\sin(\omega t + \delta) \quad \Rightarrow \quad U = |U|\,\angle\,\delta
```

---

## 5. Varför Eulerform?
Vid beräkningar är polär form, $|U|\thinspace\angle\thinspace\delta$, oftast enklast att skriva. Eulerformen förklarar varför den fungerar.

**Multiplikation och division följer av potenslagarna.** Exponenterna adderas vid multiplikation och subtraheras vid division:

```math
|z_1|e^{j\delta_1} \cdot |z_2|e^{j\delta_2} = |z_1||z_2|\,e^{j(\delta_1 + \delta_2)}
```

Det är därför vinklarna adderas när två tal multipliceras på polär form.

**Frekvensen kan utelämnas.** Alla spänningar och strömmar i en krets har samma frekvens. Det enda som skiljer dem åt är amplituden och fasen, och de ryms i fasorn $U = |U|e^{j\delta}$. Därför räknar vi med fasorer och lägger tillbaka $\omega t$ först när svaret ska skrivas som $u(t) = |U|\sin(\omega t + \delta)$.

### Derivering med Eulers formel
Det här ligger utanför kursen, men visar varför Eulers formel förenklar derivering och integrering så mycket. Vi skriver den komplexa spänningen på rektangulär form med hjälp av Eulers formel:

```math
u(t) = |U|\cos(\omega t + \delta) + j|U|\sin(\omega t + \delta)
```

Vi deriverar med kedjeregeln, där den inre derivatan är $(\omega t + \delta)' = \omega$:

```math
u'(t) = -|U|\sin(\omega t + \delta) \cdot (\omega t + \delta)' + j|U|\cos(\omega t + \delta) \cdot (\omega t + \delta)' = -\omega|U|\sin(\omega t + \delta) + j\omega|U|\cos(\omega t + \delta)
```

Eftersom $j^2 = -1$ kan $-\omega|U|\sin(\omega t + \delta)$ skrivas som $j\omega \cdot j|U|\sin(\omega t + \delta)$, så $j\omega$ kan brytas ut:

```math
u'(t) = j\omega\left(|U|\cos(\omega t + \delta) + j|U|\sin(\omega t + \delta)\right) = j\omega \cdot u(t)
```

På Eulerform blir samma derivering ett enda steg. Med $u(t) = |U|e^{j(\omega t + \delta)}$ är den inre derivatan $\left(j(\omega t + \delta)\right)' = j\omega$:

```math
u'(t) = \left(j(\omega t + \delta)\right)' \cdot |U|e^{j(\omega t + \delta)} = j\omega \cdot |U|e^{j(\omega t + \delta)} = j\omega \cdot u(t)
```

Resultatet blir detsamma, men på Eulerform räcker det att multiplicera med $j\omega$. Integrering fungerar på samma sätt fast tvärtom: att integrera motsvarar att dividera med $j\omega$.

### Impedans för spole och kondensator
Med resultatet ovan blir impedanserna enkla att härleda. Spänningen över en spole är $u = L\frac{di}{dt}$. Med strömmen $i(t) = |I|e^{j(\omega t + \delta)}$ ger deriveringen ovan $\frac{di}{dt} = j\omega \cdot i(t)$, så

```math
u(t) = L\frac{di}{dt} = L \cdot j\omega \cdot i(t) \quad \Rightarrow \quad Z_L = \frac{u(t)}{i(t)} = j\omega L
```

Strömmen genom en kondensator är $i = C\frac{du}{dt}$, och på samma sätt gäller $\frac{du}{dt} = j\omega \cdot u(t)$, så

```math
i(t) = C\frac{du}{dt} = C \cdot j\omega \cdot u(t) \quad \Rightarrow \quad Z_C = \frac{u(t)}{i(t)} = \frac{1}{j\omega C}
```

Spolens och kondensatorns impedanser följer alltså direkt av att derivering motsvarar multiplikation med $j\omega$. Impedanserna behandlas vidare i L17.

---

## 6. Typexempel

### Typexempel 1 – Multiplikation på Eulerform
Beräkna $z_1 \cdot z_2$ då $z_1 = 2e^{j\pi/6}$ och $z_2 = 3e^{j\pi/4}$. Svara på både Eulerform och rektangulär form.

**Lösning:**

Beloppen multipliceras och exponenterna adderas:

```math
z_1 \cdot z_2 = 2 \cdot 3 \cdot e^{j(\pi/6 + \pi/4)} = 6e^{j5\pi/12}
```

Vinkeln är $\frac{\pi}{6} + \frac{\pi}{4} = \frac{2\pi}{12} + \frac{3\pi}{12} = \frac{5\pi}{12}$, alltså $75°$. Eulers formel ger rektangulär form:

```math
6e^{j5\pi/12} = 6\left(\cos 75° + j\sin 75°\right) \approx 6(0{,}259 + j0{,}966) \approx 1{,}55 + j5{,}80
```

---

### Typexempel 2 – Eulerform till rektangulär form
Skriv $u(t) = 3e^{j(100\pi t - \pi/4)}\thinspace\text{V}$ på rektangulär form vid $t = 0$.

**Lösning:**

```math
u(0) = 3e^{-j\pi/4} = 3\left(\cos\left(-\frac{\pi}{4}\right) + j\sin\left(-\frac{\pi}{4}\right)\right) = 3\left(\frac{\sqrt{2}}{2} - j\frac{\sqrt{2}}{2}\right) \approx 2{,}12 - j2{,}12\,\text{V}
```

---

### Typexempel 3 – Fasor till tidsdomän
Fasorn $I = 5 - j4\thinspace\text{mA}$, $\omega = 100\pi\thinspace\text{rad/s}$. Skriv $i(t)$ på Eulers form.

**Lösning:**

```math
|I| = \sqrt{25 + 16} = \sqrt{41} \approx 6{,}40\,\text{mA}
```

```math
\delta = \arctan\left(\frac{-4}{5}\right) \approx -38{,}7° \approx -0{,}675\,\text{rad}
```

```math
i(t) = 6{,}40 \cdot e^{j(100\pi t - 0{,}675)}\,\text{mA}
```

---

## 7. Sammanfattning

| Begrepp | Formel |
|---------|--------|
| Eulers formel | $e^{j\delta} = \cos\delta + j\sin\delta$ |
| Eulerform | $z = \lvert z\rvert\thinspace e^{j\delta}$ |
| Multiplikation | $z_1 z_2 = \lvert z_1\rvert\lvert z_2\rvert\thinspace\angle\thinspace(\delta_1+\delta_2)$ |
| Division | $z_1/z_2 = (\lvert z_1\rvert/\lvert z_2\rvert)\thinspace\angle\thinspace(\delta_1-\delta_2)$ |
| Fasor → tidsdomän | $u(t) = \lvert U\rvert\sin(\omega t + \delta)$ |

---
