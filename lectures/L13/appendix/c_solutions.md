# L13 – Lösningsförslag till lektionsuppgifter

## Del 1 - Repetitionsuppgifter

### 1.1 – Analys av en kubisk funktion

Betrakta följande funktion:

```math
f(x) = -0,5x^3 + 1,5x^2 + 4,5x - 3
```

**a)** Derivera funktionen $f(x)$ och bestäm uttrycket för $f'(x)$.

**b)** Bestäm var funktionen är stationär, dvs. lös ekvationen $f'(x) = 0$.

**c)** Avgör med hjälp av den andra derivatan om respektive stationär punkt är ett maximum eller minimum.

**d)** Beräkna funktionens maximi- och minimivärde, dvs. funktionsvärdet i de stationära punkterna.

**e)** Rita upp grafen till $f(x)$ via [Geogebra](https://www.geogebra.org/graphing?lang=en), kontrollera att
dina svar stämmer.

---

### Lösning

**a)** Vi deriverar $f(x)$ för att bestämma $f'(x)$:

```math
f'(x) = -1,5x^2 + 3x + 4,5
```

**b)** Vi bestämmer när $f'(x) = 0$:

```math
f'(x) = -1,5x^2 + 3x + 4,5 = 0
```

Ovanstående uttryck kan skrivas om till

```math
1,5x^2 = 3x + 4,5
```

Vi dividerar med $1,5$ i respektive led och erhåller då följande uttryck:

```math
x^2 = 2x + 3
```

Vi beräknar rötterna för $x$ via PQ-formeln:

```math
x = \frac{2}{2} \pm \sqrt{(\frac{2}{2})^2 + 3},
```

vilket kan skrivas om till

```math
x = 1 \pm \sqrt{1 + 3},
```

där

```math
\sqrt{1 + 3} = \sqrt{4} = 2
```

Därmed gäller att

```math
x = 1 \pm 2
```

Därmed kan vi beräkna rötterna:

```math
x_1 = 1 + 2 = 3
```

```math
x_2 = 1 - 2 = -1
```

Funktionen är därmed stationär när $x = 3$ samt $x = -1$.

**c)** Vi bestämmer den andra derivatan $f''(x)$ genom att derivera $f'(x)$:

```math
f''(x) = -3x + 3
```

Vi är intresserade av den andra derivatan i extrempunkterna $x_1$ samt $x_2$.

Vi börjar med att bestämma $f''(x_1)$:

```math
f''(x_1) = f''(3) = -3 * 3 + 3 = -6 => maxvärde
```

Eftersom $f''(x_1) < 0 $ gäller att funktionen har ett maximum i denna punkt:
* $f'(x_1) = 0$ indikerar att lutningen i denna punkt är $0$ => kurvan vänder.
* $f''(x_1) < 0$ indikerar att lutningen är på väg att minska => aktuellt värde är ett maximum och kurvan är därmed på väg nedåt.

Vi bestämmer sedan $f''(x_2)$:

```math
f''(x_2) = f''(-1) = -3 * (-1) + 3 = 6 => minvärde
```

Eftersom $f''(x_2) > 0 $ gäller att funktionen har ett minimum i denna punkt:
* $f'(x_2) = 0$ indikerar att lutningen i denna punkt är $0$ => kurvan vänder.
* $f''(x_2) > 0$ indikerar att lutningen är på väg att öka => aktuellt värde är ett minimum och kurvan är därmed på väg uppåt.

**d)** Vi beräknar funktionens min- respektive maxvärde genom att sätta in extrempunkterna $x_1$ samt $x_2$ i den givna funktionen $f(x)$.

Vi börjar med att beräkna maximipunkten $f(x_1)$:

```math
f(x_1) = -0,5 * 3^3 + 1,5 * 3^2 + 4,5 * 3 - 3 = 10,5
```

Funktionen har därmed en maximipunkt i $(x; y)$ = $(3; 10,5)$.

Vi beräknar sedan minimipunkten $f(x_2)$:

```math
f(x_2) = -0,5 * (-1)^3 + 1,5 * (-1)^2 + 4,5 * (-1) - 3 = -5,5
```
Funktionen har därmed en minimipunkt i $(x; y)$ = $(-1; -5,5)$.

**e)** Funktionens graf visas nedan. Denna indikerar att våra beräkningar stämmer:

![Funktionens graf ritad i `Geogebra`](./images/1.1_geogebra.png)

---

### 1.2 - Analys av spänning över en kondensator

En kondensator i en RC-krets laddas och urladdas upprepade gånger. Spänningen över kondensatorn kan beskrivas med följande funktion:

```math
u(t) = -0,2t^3 + 1,2t^2 - 1,4625t + 3,
```

där

* $u(t)$ = spänningen över kondensatorn i $V$,
* $t$ = tiden i sekunder, där $0 ≤ t ≤ 6$.

**a)** Derivera funktionen och bestäm uttrycket för spänningens förändringshastighet $u'(t)$.

**b)** Bestäm den tidpunkt (eller tidpunkter) då spänningen är stationär, dvs. när $u'(t) = 0$.

**c)** Avgör med hjälp av den andra derivatan om punkterna är maximi- eller minimipunkter.

**d)** Beräkna spänningens maximi- och minimivärde, dvs. spänningen i de stationära punkterna.

**e)** Rita upp grafen för $u(t)$ via [Geogebra](https://www.geogebra.org/graphing?lang=en), kontrollera att
dina svar stämmer.

---

### Lösning

**a)** Vi deriverar $u(t)$ för att bestämma $u'(t)$:

```math
u'(t) = -0,6t^2 + 2,4t - 1,4625
```

**b)** Vi bestämmer när $u'(t) = 0$:

```math
u'(t) = -0,6t^2 + 2,4t - 1,4625 = 0
```

Ovanstående uttryck kan skrivas om till

```math
0,6t^2 = 2,4t - 1,4625
```

Vi dividerar med $0,6$ i respektive led och erhåller då följande uttryck:

```math
t^2 = 4t - 2,4375
```

Vi beräknar rötterna för $t$ via PQ-formeln:

```math
t = \frac{4}{2} \pm \sqrt{(\frac{4}{2})^2 - 2,4375},
```

vilket kan skrivas om till

```math
t = 2 \pm \sqrt{1,5625},
```

där

```math
\sqrt{1,5625} = 1,25
```

Därmed gäller att

```math
t = 2 \pm 1,25
```

Därmed kan vi beräkna rötterna:

```math
t_1 = 2 - 1,25 = 0,75\,s
```

```math
t_2 = 2 + 1,25 = 3,25\,s
```

Spänningen är därmed stationär när $t$ = $0,75$ $s$ samt $t$ = $3,25$ $s$.

**c)** Vi bestämmer den andra derivatan $u''(t)$ genom att derivera $u'(t)$:

```math
u''(t) = -1,2t + 2,4
```

Vi är intresserade av den andra derivatan i extrempunkterna $t_1$ samt $t_2$.

Vi börjar med att bestämma $u''(t_1)$:

```math
u''(t_1) = u''(0,75) = -1,2 * 0,75 + 2,4 = 1,5 => minpunkt
```

Eftersom $u''(t_1) > 0 $ gäller att funktionen har ett minimum i denna punkt:
* $u'(t_1) = 0$ indikerar att lutningen i denna punkt är $0$ => kurvan vänder.
* $u''(t_1) > 0$ indikerar att lutningen är på väg att öka => aktuellt värde är ett minimum och kurvan är därmed på väg uppåt.

Vi bestämmer sedan $u''(t_2)$:

```math
u''(t_2) = u''(3,25) = -1,2 * 3,25 + 2,4 = -1,5 => maxpunkt
```

Eftersom $u''(t_2) < 0 $ gäller att funktionen har ett maximum i denna punkt:
* $u'(t_2) = 0$ indikerar att lutningen i denna punkt är $0$ => kurvan vänder.
* $u''(t_2) < 0$ indikerar att lutningen är på väg att minska => aktuellt värde är ett maximum och kurvan är därmed på väg nedåt.

**d)** Vi beräknar spänningens min- respektive maxvärde genom att sätta in extrempunkterna $t_1$ samt $t_2$ i den givna funktionen $u(t)$.

Vi börjar med att beräkna minimipunkten $u(t_1)$:

```math
u(t_1) = u(0,75) = -0,2 * 0,75^3 + 1,2 * 0,75^2 - 1,4625 * 0,75 + 3 \approx 2,49 V
```

Spänningen har därmed en minimipunkt i $(t; u(t)) \approx (0,75; 2,49)$.

Vi beräknar sedan maximipunkten $u(t_2)$:

```math
u(t_2) = u(3,25) = -0,2 * 3,25^3 + 1,2 * 3,25^2 - 1,4625 * 3,25 + 3 \approx 4,06 V
```
Spänningen har därmed en maximipunkt i $(t; u(t)) \approx (3,25; 4,06)$.

**e)** Funktionens graf visas nedan. Denna indikerar att våra beräkningar stämmer:

![Funktionens graf ritad i `Geogebra`](./images/1.2_geogebra.png)

---

## Del 2 - Nytt stoff

### 2.1 - Ström genom en spole

Strömmen genom en spole varierar över tid enligt följande funktion:

```math
i(t) = 4sin(50t)
```

där
* $i(t)$ = strömmen genom spolen i $A$,
* $t$ = tiden i sekunder.

**a)** Derivera funktionen och bestäm uttrycket för $i'(t)$.

**b)** Bestäm den tidpunkt (eller tidpunkter) då strömmen är stationär, dvs. när $i'(t) = 0$.

**c)** Avgör med hjälp av den andra derivatan om punkterna är maximi- eller minimipunkter.

**d)** Beräkna strömmens största och minsta värde. Fundera om detta stämmer med våra förväntningar.

---

### Lösning

**a)** Vi deriverar $i(t)$ för att bestämma $i'(t)$. När $sin$ deriveras resulterar detta i $cos$. 
Vi tar också den så kallade inre derivatan i beaktning genom att multiplicera med derivatan av $50t$, vilket är $50$:

```math
i'(t) = 4cos(50t) * 50,
```

som kan skrivas om till

```math
i'(t) = 200cos(50t)
```

**Notering**: Ovan användes den så kallade kedjeregeln, som säger att för en given funktion $f(x)$:

```math
f(x) = a * sin(bx),
```

kan motsvarande derivata $f'(x)$ beräknas enligt nedan:

```math
f'(x) = a * cos(bx) * \frac{d}{dx}(bx),
```

där $\frac{d}{dx}(bx)$ är den inre derivatan av $sin(bx)$ och bestäms enligt nedan:

```math
\frac{d}{dx}(bx) = b
```

Därmed gäller att

```math
f'(x) = a * cos(bx) * b,
```

vilket kan skrivas om till

```math
f'(x) = ab * cos(bx)
```

**b)** Vi bestämmer när $i'(t)$ = $0$:

```math
i'(t) = 200cos(50t) = 0
```

Vi dividerar med $200$ i respektive led:

```math
cos(50t) = 0
```

För att få bort $cos$ ur vänsterledet lägger vi till $cos^{-1}$ i båda led. Detta ger oss följande:

```math
50t = cos^{-1}(0) \pm k{\pi} = \frac{\pi}{2} \pm k{\pi},
```

där $k = 0, 1, 2... n$.


Vi använder de två minsta rötterna, vilket vi får när $k$ = $0$ respektive $1$. 
Därmed gäller att vi kan beräkna tiderna $t_1$ samt $t_2$.

Vi börjar med att bestämma $t_1$ med $k$ = $0$:

```math
50t_1 = \frac{\pi}{2},
```

vilket via division med $50$ i båda led ger oss att $t_1$ är ca $31$ $ms$, då

```math
t_1 = \frac{\pi}{2 * 50} \approx 0,031 s 
```

Vi bestämmer sedan $t_2$ med $k$ = $1$:

```math
50t_2 = \frac{\pi}{2} + {\pi} = \frac{3{\pi}}{2},
```

vilket via division med $50$ i båda led ger oss att $t_2$ är ca $94$ $ms$, då

```math
t_2 = \frac{3{\pi}}{2 * 50} \approx 0,094 s 
```

**c)** Vi bestämmer andraderivatan $i''(t)$. När $cos$ deriveras resulterar detta i $-sin$. Vi tar
också den inre derivatan i beaktning genom att multiplicera med derivatan av $50t$, vilket är $50$:

```math
i''(t) = 200 * (-sin(50t)) * 50, 
```

vilket kan skrivas om till

```math
i''(t) = -10000sin(50t) 
```

Vi bestämmer sedan ifall $t_1$ samt $t_2$ är min- eller maxpunkter genom att sätta in dessa i $i''(t)$:

```math
i''(t_1) \approx i''(0,031) = -10000sin(50 * 0,031) = -10000 => max
```

```math
i''(t_2) \approx i''(0,094) = -10000sin(50 * 0,094) = 10000 => min
```

Vi ser då att strömmens maxvärde nås efter $t_1 \approx 0,031$ $s$. Vi ser då också att strömmens
minvärde nås efter $t_2 \approx 0,094$ $s$. Detta är rimligt, då en sinusström når sitt maxvärde efter en
fjärdedel av periodtiden, medan minvärdet nås efter tre fjärdedelar av periodtiden.

**d)** Vi beräknar strömmens min- och maxvärde genom att sätta in $t_1$ samt $t_2$ i formeln för $i(t)$:

```math
i(t_1) \approx i(0,031) = 4sin(50 * 0,031) \approx 4 A
```

```math
i(t_2) \approx i(0,094) = 4sin(50 * 0,094) \approx -4 A
```

Eftersom strömmens amplitud $|I|$ = $4$ $A$ är max- och minvärdet förväntat:
* Strömmens maxvärde $4$ $A$ nås efter en fjärdedel av periodtiden, vilket är efter $t_1 \approx 0,031$ $s$.
* Strömmens minvärde $-4$ $A$ nås efter tre fjärdedelar av periodtiden, vilket är efter $t_2 \approx 0,094$ $s$.

---

### 2.2 - Urladdning av kondensator
Spänningen över en kondensator som urladdas ges av följande funktion:

```math
u(t) = 12 e^{-0,4t}
```

där
* $u(t)$ = spänningen över kondensatorn i $V$,
* $t$ = tiden i sekunder.

**a)** Derivera funktionen och bestäm uttrycket för $u'(t)$.

**b)** Beräkna spänningens förändringshastighet vid $t = 2$ $s$.

**c)** Ange om spänningsförändringen ökar eller minskar i denna punkt, dvs. bestäm $u''(2)$.

---

### Lösning

**a)** Vi deriverar funktionen $u(t)$ för att bestämma $u'(t)$. Vi använder följande regel:

```math
\frac{d}{dx}(e^{ax}) = e^{ax} * a = ae^{ax}
```

Den yttre derivatan av $e^{ax}$ är alltid samma, dvs. $e^{ax}$. Vi tar den inre derivatan i åtanke
genom att multiplicera den yttre derivatan med derivatan av exponenten $ax$, vilket blir $a$:

```math
\frac{d}{dx}(ax) = a
```

Vi gör samma för aktuell ekvation $u(t)$:

```math
u'(t) = 12e^{-0,4t} * -0,4,
```

vilket kan skrivas om till

```math
u'(t) = -4,8e^{-0,4t}
```

**b)** Vi beräknar spänningens förändringshastighet vid $t = 2$ $s$ genom att beräkna $u'(2)$:

```math
u'(2) = -4,8e^{-0,4 * 2} \approx -2,16\,V/s
```

**c)** Vi bestämmer andraderivatan $u''(t)$ genom att derivera $u'(t)$. Vi använder samma tillvägagångssätt
för att derivera $e^{ax}$ som visades tidigare:

```math
u''(t) = -4,8e^{-0,4t} * (-0,4),
```

vilket kan skrivas om till

```math
u''(t) = 1,92e^{-0,4t}\,V/s^2
```

Vi bestämmer sedan $u''(2)$:

```math
u''(2) = 1,92e^{-0,4 * 2} \approx 0,86 \,V/s^2
```

Eftersom $u''(2)$ > $0$ gäller att spänningsförändringen ökar vid tiden $t$ = $2$ $s$.

---

### 2.3 - Förstärkning i dB
Den logaritmiska förstärkningen i ett förstärkarsystem beskrivs av följande funktion:

```math
G(x) = 10log_{10}(2x + 1)
```

där
* $G(x)$ = förstärkningen i $dB$,
* $x$ = insignalsnivån (dimensionslös faktor).

**a)** Beräkna för vilket värde på $x$ som förstärkningen $G(x)$ = $2$ $dB$.

**b)** Beräkna förstärkningens förändringshastighet $G'(x)$ i denna punkt.

***Notering**: Förändringshastigheten $G'(x)$ indikerar hur snabbt förstärkningen ändras när insignal $x$ förändras*.

---

### Lösning

**a)** Vi sätter upp en ekvation med $G(x)$ = $2$ $dB$:

```math
G(x) = 10log_{10}(2x + 1) = 2
```

Vi dividerar med $10$ i respektive led:

```math
log_{10}(2x + 1) = 0,2
```

Vi höjer båda led med basen $10$ för att få bort $log_{10}$ ur vänsterledet:

```math
2x + 1 = 10^{0,2}
```

Vi subtraherar sedan med $1$ i respektive led:


```math
2x = 10^{0,2} - 1
```

Slutligen dividerar vi med $2$ i båda led för att bestämma $x$:


```math
x = \frac{10^{0,2} - 1}{2} \approx 0,29
```

Vi kontrollräknar det beräknade värdet $x \approx 0,29$. Om vi har räknat rätt bör $G(x)$ bli $2$ $dB$
i denna punkt:

```math
G(0,29) = 10log_{10}(2 * 0,29 + 1) = 2 => OK
```

**b)** Vi utnyttjar följande regel för en given ekvation $f(x)$:

```math
f(x) = log_{10}(ax)
```

att dess derivata $f'(x)$ kan beräknas enligt nedan:

```math
f'(x) = \frac{1}{ax * \ln 10} * \frac{d}{dx}(ax)
```

där

```math
\frac{d}{dx}(ax) = a
```

Vi deriverar $G(x)$ med denna regel:

```math
G'(x) = 10 * \frac{1}{(2x + 1) * \ln 10} * \frac{d}{dx}(2x + 1), 
```

där

```math
\frac{d}{dx}(2x + 1) = 2
```

Därmed gäller att

```math
G'(x) = \frac{10 * 1}{(2x + 1) * \ln 10} * 2, 
```

vilket kan skrivas om till

```math
G'(x) = \frac{20}{(2x + 1) * \ln 10}
```

Slutligen beräknar vi förstärkningens förändringshastighet $G'(x)$ när $x \approx 0,29$, dvs. $G'(0,29)$. Eftersom $2x + 1 = 10^{0,2}$ enligt a) gäller att

```math
G'(0,29) \approx \frac{20}{10^{0,2} * \ln 10} \approx 5,48
```

---

## Del 3 – Extrauppgifter
### 3.1 – Derivera trigonometriska funktioner

---

### Lösning
Reglerna är $\dfrac{d}{dx}\sin(kx) = k\cos(kx)$ och $\dfrac{d}{dx}\cos(kx) = -k\sin(kx)$. Den inre faktorn $k$ blir alltså kvar som en faktor framför.

**a)** $f'(x) = 3\cos(3x)$

**b)** $f'(x) = -5\sin(5x)$

**c)** $f'(x) = 4\cos(x)$

**d)** $f'(x) = -2 \cdot \left(-2\sin(2x)\right) = 4\sin(2x)$

**e)** $f'(x) = \cos(x) - \sin(x)$

---

### 3.2 – Derivera exponentialfunktioner

---

### Lösning
Regeln är $\dfrac{d}{dx}e^{kx} = ke^{kx}$.

**a)** $f'(x) = 5e^{5x}$

**b)** $f'(x) = 3 \cdot (-2)e^{-2x} = -6e^{-2x}$

**c)** $f'(x) = e^x + 2x$

**d)** För en godtycklig bas gäller $\dfrac{d}{dx}a^x = a^x\ln a$:

```math
f'(x) = 2^x\ln 2
```

**e)** Här är $k = -\dfrac{1}{4}$:

```math
f'(x) = 10 \cdot \left(-\frac{1}{4}\right)e^{-x/4} = -2{,}5e^{-x/4}
```

---

### 3.3 – Derivera logaritmfunktioner

---

### Lösning
**a)** $f'(x) = \dfrac{1}{x}$

**b)** Eftersom $\ln(7x) = \ln 7 + \ln x$ och $\ln 7$ är en konstant:

```math
f'(x) = \frac{1}{x}
```

Konstanten inuti logaritmen påverkar alltså **inte** derivatan.

**c)** $f'(x) = \dfrac{3}{x}$

**d)** $f'(x) = \dfrac{1}{x\ln 10}$

**e)** $f'(x) = \dfrac{1}{x} + e^x$

---

### 3.4 – Blandad derivering

---

### Lösning
**a)**

```math
f'(x) = 6e^{3x} - 4\cos(4x)
```

**b)** Konstanten $\ln 2$ försvinner vid derivering:

```math
f'(x) = 2x + \frac{1}{x}
```

**c)**

```math
f'(x) = -5\sin(x) + 3e^{-x}
```

**d)**

```math
f'(x) = 8\cos(2x) - 8\sin(2x)
```

---

### 3.5 – Derivatan i en punkt

---

### Lösning
**a)** $f'(x) = 2e^{2x}$, alltså $f'(0) = 2$.

**b)** $f'(x) = \cos x$, alltså $f'\left(\dfrac{\pi}{2}\right) = 0$. Sinuskurvan har vågrät tangent i sitt toppvärde.

**c)** $f'(x) = \dfrac{1}{x}$, alltså $f'(2) = 0{,}5$.

**d)** $f'(x) = -3\sin(3x)$, alltså $f'(0) = 0$.

**e)** $f'(x) = -3e^{-x}$, alltså:

```math
f'(1) = -3e^{-1} \approx -1{,}10
```

---

### 3.6 – Ström genom en kondensator
$C = 47\thinspace\mu\text{F}$, $u(t) = 10\sin(100\pi t)$ V

---

### Lösning
**a)**

```math
u'(t) = 10 \cdot 100\pi\cos(100\pi t) = 1000\pi\cos(100\pi t)
```

**b)**

```math
i_C(t) = C\,u'(t) = 47 \times 10^{-6} \cdot 1000\pi\cos(100\pi t) \approx 0{,}148\cos(100\pi t)\,\text{A}
```

Alltså ungefär $148\cos(100\pi t)\thinspace\text{mA}$.

**c)** Amplituden är faktorn framför cosinus:

```math
|I| \approx 148\,\text{mA}
```

**d)** Cosinus är störst när argumentet är noll:

```math
100\pi t = 0 \quad \Rightarrow \quad t = 0
```

Strömmen är alltså som störst i det ögonblick spänningen passerar noll – det är där spänningen ändras snabbast.

---

### 3.7 – Spänning över en spole
$L = 25\thinspace\text{mH}$, $i(t) = 2\sin(200t)$ A

---

### Lösning
**a)**

```math
i'(t) = 2 \cdot 200\cos(200t) = 400\cos(200t)
```

**b)**

```math
u_L(t) = L\,i'(t) = 0{,}025 \cdot 400\cos(200t) = 10\cos(200t)\,\text{V}
```

**c)** Amplituden är $10\thinspace\text{V}$.

**d)** Strömmen är en sinus och spänningen en cosinus. Eftersom $\cos(x) = \sin(x + 90°)$ ligger spänningen **$90°$ före** strömmen. Det är den kända fasförskjutningen hos en spole.

---

### 3.8 – Urladdning av en kondensator
$u(t) = 20e^{-t/0{,}5} = 20e^{-2t}$ V

---

### Lösning
**a)** Med $k = -2$:

```math
u'(t) = 20 \cdot (-2)e^{-2t} = -40e^{-2t}\,\text{V/s}
```

**b)**

```math
u'(0) = -40\,\text{V/s}
```

**c)**

```math
u'(0{,}5) = -40e^{-1} \approx -14{,}7\,\text{V/s}
```

**d)** Derivatan är negativ, vilket betyder att spänningen **minskar**. Beloppet avtar med tiden – urladdningen går snabbast i början.

**e)** Sätt in $u(t) = 20e^{-2t}$ och $\tau = 0{,}5$:

```math
-\frac{u(t)}{\tau} = -\frac{20e^{-2t}}{0{,}5} = -40e^{-2t} = u'(t) \quad ✓
```

---

### 3.9 – Stationär punkt för en exponentialfunktion
$f(x) = xe^{-2x}$

---

### Lösning
**a)** Produktregeln på $x$ och $e^{-2x}$:

```math
f'(x) = 1 \cdot e^{-2x} + x \cdot (-2e^{-2x}) = e^{-2x}(1 - 2x)
```

**b)** Faktorn $e^{-2x}$ är aldrig noll, så det är parentesen som måste vara det:

```math
1 - 2x = 0 \quad \Rightarrow \quad x = 0{,}5
```

**c)** Derivera $f'(x)$ en gång till med produktregeln:

```math
f''(x) = -2e^{-2x}(1 - 2x) + e^{-2x}(-2) = e^{-2x}(4x - 4)
```

```math
f''(0{,}5) = e^{-1}(2 - 4) = -2e^{-1} \approx -0{,}736 < 0 \quad \Rightarrow \quad \text{maximum}
```

**d)**

```math
f(0{,}5) = 0{,}5e^{-1} \approx 0{,}184
```

---

### 3.10 – Maximal effekt i tiden
$p(t) = 100te^{-t}$ W

---

### Lösning
**a)** Produktregeln:

```math
p'(t) = 100e^{-t} + 100t(-e^{-t}) = 100e^{-t}(1 - t)
```

**b)**

```math
1 - t = 0 \quad \Rightarrow \quad t = 1\,\text{s}
```

**c)**

```math
p''(t) = -100e^{-t}(1 - t) + 100e^{-t}(-1) = 100e^{-t}(t - 2)
```

```math
p''(1) = 100e^{-1}(1 - 2) = -100e^{-1} < 0 \quad \Rightarrow \quad \text{maximum}
```

**d)**

```math
p(1) = 100e^{-1} \approx 36{,}8\,\text{W}
```

---

### 3.11 – Derivatan av en dB-funktion
$G(x) = 20\log_{10}(x)$

---

### Lösning
**a)** Med $\dfrac{d}{dx}\log_{10}x = \dfrac{1}{x\ln 10}$:

```math
G'(x) = \frac{20}{x\ln 10}
```

**b)**

```math
G'(1) = \frac{20}{\ln 10} \approx 8{,}69\,\text{dB per enhet}
```

**c)**

```math
G'(10) = \frac{20}{10\ln 10} \approx 0{,}869\,\text{dB per enhet}
```

**d)** Derivatan är tio gånger mindre vid $x = 10$ än vid $x = 1$. Förstärkningen i dB växer alltså allt **långsammare** när insignalen ökar – det är själva poängen med en logaritmisk skala: den komprimerar stora värden.

---

### 3.12 – Tangent till en exponentialkurva
$f(x) = e^{-x}$, $x_0 = 0$

---

### Lösning
**a)**

```math
f(0) = e^0 = 1
```

**b)**

```math
f'(x) = -e^{-x} \quad \Rightarrow \quad f'(0) = -1
```

**c)**

```math
y = -1(x - 0) + 1 = 1 - x
```

**d)**

```math
1 - x = 0 \quad \Rightarrow \quad x = 1
```

Tangenten i startpunkten skär alltså x-axeln vid $x = 1$, vilket motsvarar **en tidskonstant**. Det ger tidskonstanten en tydlig geometrisk tolkning: hade urladdningen fortsatt lika snabbt som i starten hade den varit klar efter tiden $\tau$.

---

### 3.13 – Derivatan hos en exponentiell urladdning
$u(t) = U_0e^{-t/\tau}$

---

### Lösning
**a)** Derivera med $k = -\dfrac{1}{\tau}$:

```math
u'(t) = U_0 \cdot \left(-\frac{1}{\tau}\right)e^{-t/\tau} = -\frac{U_0e^{-t/\tau}}{\tau} = -\frac{u(t)}{\tau}
```

**b)** Förändringshastigheten är proportionell mot det **aktuella värdet**. Ju mindre spänningen är, desto långsammare sjunker den. Det är den definierande egenskapen hos ett exponentiellt förlopp och förklarar varför kurvan planar ut.

**c)** Med $U_0 = 10\thinspace\text{V}$ och $\tau = 2\thinspace\text{s}$:

```math
u'(0) = -\frac{10}{2} = -5\,\text{V/s}
```

```math
u'(2) = -\frac{10e^{-1}}{2} \approx -1{,}84\,\text{V/s}
```

**d)**

```math
\frac{u(\tau)}{U_0} = e^{-1} \approx 0{,}37 = 37\%
```

Efter en tidskonstant återstår alltså ungefär 37 % av startvärdet, oavsett hur stort det var.

---

### 3.14 – Sant eller falskt

---

### Lösning
**a)** **Falskt.** Derivatan av $\sin x$ är $\cos x$. Minustecknet hör till derivatan av $\cos x$.

**b)** **Falskt.** Den inre faktorn följer med: $\dfrac{d}{dx}e^{3x} = 3e^{3x}$.

**c)** **Falskt.** $\ln(5x) = \ln 5 + \ln x$, och konstanten försvinner vid derivering. Svaret är $\dfrac{1}{x}$.

**d)** **Sant.** $\dfrac{d}{dx}\cos(kx) = -k\sin(kx)$, alltså $-2\sin(2x)$.

**e)** **Sant.** $e^x$ är den enda funktionen (bortsett från multipler av den) som är lika med sin egen derivata.

**f)** **Sant.** Konstanten kan flyttas utanför: $\dfrac{d}{dx}\left[Cf(x)\right] = Cf'(x)$.

---

### 3.15 – Hitta felet

---

### Lösning
**a)** Den inre faktorn $3$ måste följa med som en faktor:

```math
\frac{d}{dx}\sin(3x) = 3\cos(3x)
```

**b)** Exponenten på $e$ ändras **inte** vid derivering – bara en faktor tillkommer:

```math
\frac{d}{dx}e^{-2x} = -2e^{-2x}
```

**c)** Konstanten inuti logaritmen försvinner, eftersom $\ln(3x) = \ln 3 + \ln x$:

```math
\frac{d}{dx}\ln(3x) = \frac{1}{x}
```

**d)** Derivatan av cosinus är **minus** sinus:

```math
\frac{d}{dx}4\cos(x) = -4\sin(x)
```

**e)** Potensregeln gäller när $x$ står i **basen**, inte i exponenten. För $a^x$ gäller i stället:

```math
\frac{d}{dx}2^x = 2^x\ln 2
```

---

## Del 4 – Matematik i C

### 4.1 – Derivatan av $e^x$ och $\sin v$ i C

**a)** Funktionen beräknar `(f(x + DERIVATIVE_H) - f(x)) / DERIVATIVE_H`. Det är samma kvot som i L12, men funktionen `f()` är nu en parameter.

**b)** Programmet ska skriva ut ungefär följande:

```text
x = 0, slope = 1, e^0 = 1
x = 1, slope = 2.71828, e^1 = 2.71828
x = 2, slope = 7.38906, e^2 = 7.38906
x = 3, slope = 20.0855, e^3 = 20.0855
x = 4, slope = 54.5982, e^4 = 54.5982
```

Lutningen är lika med funktionsvärdet i varje punkt, vilket stämmer med $\frac{d}{dx}e^x = e^x$.

**c)** Programmet ska skriva ut ungefär följande:

```text
v = -1.00 rad, slope = 0.54, sin(v) = -0.84, cos(v) = 0.54
v = -0.80 rad, slope = 0.70, sin(v) = -0.72, cos(v) = 0.70
v = -0.60 rad, slope = 0.83, sin(v) = -0.56, cos(v) = 0.83
v = -0.40 rad, slope = 0.92, sin(v) = -0.39, cos(v) = 0.92
v = -0.20 rad, slope = 0.98, sin(v) = -0.20, cos(v) = 0.98
v =  0.00 rad, slope = 1.00, sin(v) =  0.00, cos(v) = 1.00
v =  0.20 rad, slope = 0.98, sin(v) =  0.20, cos(v) = 0.98
v =  0.40 rad, slope = 0.92, sin(v) =  0.39, cos(v) = 0.92
v =  0.60 rad, slope = 0.83, sin(v) =  0.56, cos(v) = 0.83
v =  0.80 rad, slope = 0.70, sin(v) =  0.72, cos(v) = 0.70
v =  1.00 rad, slope = 0.54, sin(v) =  0.84, cos(v) = 0.54
```

Lutningen stämmer med $\cos v$, vilket stämmer med $\frac{d}{dv}\sin v = \cos v$.

**d)** Programmet ska skriva ut ungefär följande:

```text
x = 0, slope = 0.693147, 2^0 = 1, slope / 2^0 = 0.693147, ln 2 = 0.693147
x = 1, slope = 1.38629, 2^1 = 2, slope / 2^1 = 0.693147, ln 2 = 0.693147
x = 2, slope = 2.77259, 2^2 = 4, slope / 2^2 = 0.693147, ln 2 = 0.693147
x = 3, slope = 5.54518, 2^3 = 8, slope / 2^3 = 0.693147, ln 2 = 0.693147
x = 4, slope = 11.0904, 2^4 = 16, slope / 2^4 = 0.693147, ln 2 = 0.693147
```

Kvoten är densamma för alla $x$ och lika med $\ln 2$, eftersom $\frac{d}{dx}2^x = 2^x \ln 2$. Lutningen är alltså proportionell mot funktionen men inte lika med den, medan $e^x$ har faktorn $\ln e = 1$ och därför är sin egen derivata. Ingenting behövde ändras i `derive()`, bara argumentet i anropet. Det är det funktionspekaren ger oss.

**e)** Programmet ska skriva ut ungefär följande:

```text
x = 1, slope = 0.434294, 1 / (x * ln 10) = 0.434294
x = 2, slope = 0.217147, 1 / (x * ln 10) = 0.217147
x = 3, slope = 0.144765, 1 / (x * ln 10) = 0.144765
x = 4, slope = 0.108574, 1 / (x * ln 10) = 0.108574
x = 5, slope = 0.0868589, 1 / (x * ln 10) = 0.0868589
```

Lutningen stämmer med $f'(x) = \dfrac{1}{x \ln 10}$ i varje punkt. Eftersom $\log_{10} x = \dfrac{\ln x}{\ln 10}$ är tiologaritmen den naturliga logaritmen delad med konstanten $\ln 10 \approx 2{,}303$, så derivatan blir

```math
\frac{d}{dx}\log_{10} x = \frac{1}{\ln 10} \cdot \frac{1}{x} = \frac{1}{x \ln 10}
```

$x$ kan inte börja på $0$, eftersom $\log_{10} x$ bara är definierad för $x > 0$. `log10(0.0)` ger $-\infty$.

---
