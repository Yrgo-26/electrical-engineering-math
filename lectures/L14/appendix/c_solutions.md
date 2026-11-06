# L14 - Lösningsförslag till lektionsuppgifter

## Del 1 - Repetitionsuppgifter

### 1.1 - Urladdning av kondensator
Spänningen över en kondensator som laddas ur ges av funktionen

```math
u(t) = 24e^{-0{,}25t},
```

där
* $u(t)$ = spänningen över kondensatorn i $V$,
* $t$ = tiden i sekunder.

Derivatans definition lyder

```math
u'(t) = \lim_{h \to 0} \frac{u(t + h) - u(t)}{h}
```

**a)** Bestäm derivatan $u'(t)$ med derivatans definition.

**b)** Beräkna spänningens förändringshastighet vid $t = 4$ $s$.

**c)** Bestäm $u''(4)$. Ökar eller minskar förändringshastigheten i denna punkt, och vad innebär det för urladdningen?

---

### Lösning

**a)** Funktionsvärdena i $t$ och $t + h$ är

```math
u(t) = 24e^{-0{,}25t}, \qquad u(t + h) = 24e^{-0{,}25(t + h)} = 24e^{-0{,}25t - 0{,}25h}
```

Insatta i kvoten:

```math
\frac{u(t + h) - u(t)}{h} = \frac{24e^{-0{,}25t - 0{,}25h} - 24e^{-0{,}25t}}{h}
```

Med $e^{-0{,}25t - 0{,}25h} = e^{-0{,}25t} \cdot e^{-0{,}25h}$ kan $24e^{-0{,}25t}$ brytas ut:

```math
\frac{u(t + h) - u(t)}{h} = 24e^{-0{,}25t} \cdot \frac{e^{-0{,}25h} - 1}{h}
```

Faktorn $24e^{-0{,}25t}$ beror inte på $h$, så bara kvoten till höger påverkas när $h \to 0$. Med $s = -0{,}25h$, som också går mot $0$, blir den

```math
\frac{e^{-0{,}25h} - 1}{h} = -0{,}25 \cdot \frac{e^{s} - 1}{s} \to -0{,}25 \cdot 1 = -0{,}25
```

Alltså är

```math
u'(t) = 24e^{-0{,}25t} \cdot (-0{,}25) = -6e^{-0{,}25t}
```

Svaret kan kontrolleras med **kedjeregeln**, som säger att om $f(t) = g(v(t))$ är

```math
f'(t) = g'(v(t)) \cdot v'(t),
```

alltså den yttre funktionens derivata, beräknad i den inre funktionen, gånger den inre funktionens derivata. Här är den yttre funktionen $24e^{v}$ och den inre funktionen $v(t) = -0{,}25t$, med derivatan $v'(t) = -0{,}25$:

```math
u'(t) = 24e^{-0{,}25t} \cdot (-0{,}25) = -6e^{-0{,}25t}
```

Samma uttryck, men på en rad. Derivatan av $e^{kt}$ är alltså $ke^{kt}$: exponenten står kvar, och konstanten $k$ kommer ut som en faktor.

**b)** Sätt in $t = 4$:

```math
u'(4) = -6e^{-1} \approx -6 \cdot 0{,}3679 \approx -2{,}21 \text{ V/s}
```

Spänningen sjunker alltså med ungefär $2{,}21$ V per sekund vid $t = 4$ s.

**c)** Derivera $u'(t)$ en gång till, återigen med kedjeregeln:

```math
u''(t) = -6e^{-0{,}25t} \cdot (-0{,}25) = 1{,}5e^{-0{,}25t}
```

```math
u''(4) = 1{,}5e^{-1} \approx 0{,}552 \text{ V/s}^2
```

Eftersom $u''(4) > 0$ ökar förändringshastigheten, det vill säga $u'(t)$ blir mindre negativ. Spänningen sjunker fortfarande, men allt långsammare. Det stämmer med en urladdning: kondensatorn tappar spänning snabbast i början, och kurvan planar ut mot $0$ V.

## Del 2 - Nytt stoff

### 2.1 - Energi lagrad i en spole
Strömmen genom en spole är tidsberoende och ges av följande funktion:

```math
i(t) = 5t,
```

där $t$ = tiden i sekunder. Strömmen mäts i $A$ $(Ampere)$.

Spolens induktans $L = 0,20$ $H$ $(Henry)$.

Effektutvecklingen $p(t)$ i spolen ges av följande funktion:

```math
p(t) = L * i(t) * i'(t),
```

där
* p(t) = effektutvecklingen i $W$ $(Watt)$,
* $L$ = spolens induktans i $H$ $(Henry)$,
* $i(t)$ = strömmen genom spolen i $A$ $(Ampere)$,
* $i'(t)$ = strömförändringen genom spolen i $A/s$.

Energin $w(t)$ som lagras i spolen mellan tiden $0 - t$ ges av följande funktion:

```math
w(t) = \int_0^t p(t)\,dt
```

Energin mäts i $J$ $(Joule)$.

**a)** Bestäm $p(t)$.

**b)** Bestäm den primitiva funktionen $P(t)$ till $p(t)$.

**c)** Bestäm ett uttryck för energin i spolen $w(t)$ som en funktion av tiden.

**d)** Spolen är oladdad vid start, dvs. $w(0) = 0$. Bestäm integrationskonstanten $C$.

**e)** Bestäm hur mycket energi som har lagrats i spolen under de första $3$ sekunderna $(0{\le}\thinspace t\thinspace{\le}\thinspace 3)$.

---

### Lösning

**a)** För att bestämma $p(t)$ måste vi bestämma $i'(t)$:

```math
i'(t) = (5t)' = 5
```

Därmed kan vi bestämma ett uttryck för $p(t)$:

```math
p(t) = L * i(t) * i'(t) = 0,2 * 5t * 5 = 5t
```

**b)** För att bestämma $P(t)$ integrerar vi $p(t)$ utan tidsintervall:

```math
P(t) = \int p(t)\,dt = \int (5t)\,dt = \frac{5t^2}{2} + C,
```

där $C$ = integrationskonstanten.

**c)** Eftersom energin $w(t)$ som lagras i spolen mellan tiden $0 - t$ ges av funktionen

```math
w(t) = \int_0^t p(t)\,dt
```

så gäller att energin i spolen $w(t)$ som en funktion av tiden, dvs. utan tidsintervall, är ekvivalent
med den primitiva funktionen $P(t)$, då

```math
w(t) = \int p(t)\,dt = \int (5t)\,dt = \frac{5t^2}{2} + C
```

Notera att uttrycket är identiskt med $P(t)$.

**d)** Genom att bestämma $w(0)$ via det framtagna uttrycket ser vi att $C = 0$, då

```math
w(0) = \frac{5 * 0^2}{2} + C = 0 => C = 0
```

Därmed kan uttrycket $w(t)$ slutligen fastställas:

```math
w(t) = \frac{5t^2}{2}
```

**e)** Vi integrerar $p(t)$ för $0$ $\le$ $t$ $\le$ $3$:

```math
w(3) = \int_0^3 p(t)\,dt = \int_0^3 (5t)\,dt = \big[\frac{5t^2}{2} + C\big]_0^3,
```

som kan utvecklas till

```math
w(3) = \big(\frac{5 * 3^2}{2} + C\big) - \big(\frac{5*0^2}{2} + C\big),
```

vilket kan förenklas till

```math
w(3) = \big(\frac{5 * 9}{2} + C\big) - C = 22,5 J
```

Under de tre första sekunderna lagras alltså $22,5$ $J$ i spolen.

---
## Del 3 – Extrauppgifter
### 3.1 – Primitiva funktioner till polynom

---

### Lösning
Regeln är $\displaystyle\int x^n\thinspace dx = \dfrac{x^{n+1}}{n+1} + C$ – exponenten ökas med ett och man dividerar med den nya exponenten.

**a)** $\dfrac{x^4}{4} + C$

**b)** $2x^2 + C$

**c)** $5x + C$

**d)** $x^2 + 3x + C$

**e)** $\dfrac{x^3}{3} - 2x^2 + x + C$

---

### 3.2 – Primitiva funktioner till övriga standardfunktioner

---

### Lösning
**a)** $e^x + C$

**b)** $\dfrac{e^{3x}}{3} + C$ – den inre faktorn hamnar i nämnaren, tvärtom mot vid derivering.

**c)** $\ln|x| + C$

**d)** $-\cos(x) + C$

**e)** $\dfrac{\sin(2x)}{2} + C$

**f)** $-\dfrac{\cos(4x)}{4} + C$

---

### 3.3 – Kontrollera genom derivering

---

### Lösning
En primitiv funktion kontrolleras alltid genom att derivera den och se om man får tillbaka $f$.

**a)**

```math
F'(x) = \frac{3x^2}{3} = x^2 = f(x) \quad ✓
```

**b)**

```math
F'(x) = -\frac{1}{2} \cdot \left(-2\sin(2x)\right) = \sin(2x) = f(x) \quad ✓
```

**c)**

```math
F'(t) = -2 \cdot \left(-\frac{1}{2}\right)e^{-t/2} = e^{-t/2} = f(t) \quad ✓
```

**d)** Eftersom derivatan av en konstant är noll ger $F(x) + C$ samma derivata för **varje** värde på $C$. Det finns därför oändligt många primitiva funktioner, och de skiljer sig bara med en konstant.

---

### 3.4 – Bestämda integraler: polynom

---

### Lösning
**a)**

```math
\int_0^2 3x^2\,dx = \left[x^3\right]_0^2 = 8 - 0 = 8
```

**b)**

```math
\int_1^3 2x\,dx = \left[x^2\right]_1^3 = 9 - 1 = 8
```

**c)**

```math
\int_0^4 (x + 1)\,dx = \left[\frac{x^2}{2} + x\right]_0^4 = (8 + 4) - 0 = 12
```

**d)**

```math
\int_{-1}^{1} x^2\,dx = \left[\frac{x^3}{3}\right]_{-1}^{1} = \frac{1}{3} - \left(-\frac{1}{3}\right) = \frac{2}{3}
```

**e)**

```math
\int_0^3 (6 - 2x)\,dx = \left[6x - x^2\right]_0^3 = 18 - 9 = 9
```

---

### 3.5 – Bestämda integraler: övriga funktioner

---

### Lösning
**a)**

```math
\int_0^1 e^x\,dx = \left[e^x\right]_0^1 = e - 1 \approx 1{,}72
```

**b)**

```math
\int_0^{\pi} \sin(x)\,dx = \left[-\cos(x)\right]_0^{\pi} = -(-1) - (-1) = 2
```

**c)**

```math
\int_0^{\pi/2} \cos(x)\,dx = \left[\sin(x)\right]_0^{\pi/2} = 1 - 0 = 1
```

**d)**

```math
\int_1^{e} \frac{1}{x}\,dx = \left[\ln x\right]_1^{e} = 1 - 0 = 1
```

**e)**

```math
\int_0^2 e^{-t}\,dt = \left[-e^{-t}\right]_0^2 = -e^{-2} + 1 \approx 0{,}865
```

---

### 3.6 – Area under en kurva

---

### Lösning
**a)**

```math
\int_0^4 x\,dx = \left[\frac{x^2}{2}\right]_0^4 = 8
```

**b)** Området är en rätvinklig triangel med bas $4$ och höjd $f(4) = 4$:

```math
A = \frac{4 \cdot 4}{2} = 8 \quad ✓
```

**c)**

```math
\int_1^5 3\,dx = \left[3x\right]_1^5 = 15 - 3 = 12
```

Rektangeln har bredden $4$ och höjden $3$, alltså arean $12$ ✓

**d)**

```math
\int_0^2 x^2\,dx = \left[\frac{x^3}{3}\right]_0^2 = \frac{8}{3} \approx 2{,}67
```

---

### 3.7 – Negativa areor
$f(x) = x - 2$

---

### Lösning
**a)** På $[0, 2]$ ligger kurvan under x-axeln:

```math
\int_0^2 (x-2)\,dx = \left[\frac{x^2}{2} - 2x\right]_0^2 = (2 - 4) - 0 = -2
```

**b)** På $[2, 4]$ ligger kurvan ovanför x-axeln:

```math
\int_2^4 (x-2)\,dx = (8 - 8) - (2 - 4) = 0 + 2 = 2
```

**c)**

```math
\int_0^4 (x-2)\,dx = -2 + 2 = 0
```

**d)** Integralen räknar area **med tecken**. Den del av kurvan som ligger under x-axeln bidrar negativt och den ovanför positivt. Här är de två delarna exakt lika stora, så de tar ut varandra. Vill man ha den totala arean måste man dela upp integralen vid nollstället $x = 2$ och addera beloppen: $|-2| + |2| = 4$.

---

### 3.8 – Integrationskonstant med startvillkor
$f'(x) = 4x - 3$, $f(0) = 5$

---

### Lösning
**a)**

```math
f(x) = \int (4x - 3)\,dx = 2x^2 - 3x + C
```

**b)** Sätt in $x = 0$:

```math
f(0) = 0 - 0 + C = 5 \quad \Rightarrow \quad C = 5
```

**c)**

```math
f(x) = 2x^2 - 3x + 5
```

**d)**

```math
f(2) = 8 - 6 + 5 = 7
```

---

### 3.9 – Spänning ur förändringshastighet
$u'(t) = 6t$ V/s, $u(0) = 2\thinspace\text{V}$

---

### Lösning
**a)**

```math
u(t) = \int 6t\,dt = 3t^2 + C
```

**b)**

```math
u(0) = C = 2
```

**c)**

```math
u(t) = 3t^2 + 2\,\text{V}
```

**d)**

```math
u(4) = 3 \cdot 16 + 2 = 50\,\text{V}
```

Startvillkoret är alltså det som skiljer den sökta funktionen från alla andra primitiva funktioner.

---

### 3.10 – Laddning ur ström
$i(t) = 4t + 2$ A, $q(0) = 0$

---

### Lösning
**a)**

```math
q(t) = \int (4t + 2)\,dt = 2t^2 + 2t + C
```

Med $q(0) = 0$ blir $C = 0$:

```math
q(t) = 2t^2 + 2t\,\text{C}
```

**b)**

```math
q(3) = 18 + 6 = 24\,\text{C}
```

**c)**

```math
q(5) = 50 + 10 = 60\,\text{C}
```

**d)**

```math
q(5) - q(3) = 60 - 24 = 36\,\text{C}
```

**e)**

```math
\int_3^5 (4t + 2)\,dt = \left[2t^2 + 2t\right]_3^5 = 60 - 24 = 36\,\text{C} \quad ✓
```

Att beräkna en bestämd integral är alltså detsamma som att ta skillnaden mellan två funktionsvärden hos den primitiva funktionen.

---

### 3.11 – Laddning ur en sinusström
$i(t) = 2\sin(100\pi t)$ A

---

### Lösning
**a)**

```math
\int 2\sin(100\pi t)\,dt = -\frac{2\cos(100\pi t)}{100\pi} + C
```

**b)** Halva perioden är $0{,}01\thinspace\text{s}$:

```math
\left[-\frac{2\cos(100\pi t)}{100\pi}\right]_0^{0{,}01} = \frac{-2\cos\pi + 2\cos 0}{100\pi} = \frac{2 + 2}{100\pi} = \frac{4}{100\pi} \approx 0{,}0127\,\text{C}
```

**c)** En hel period är $0{,}02\thinspace\text{s}$:

```math
\frac{-2\cos 2\pi + 2\cos 0}{100\pi} = \frac{-2 + 2}{100\pi} = 0
```

**d)** Under den första halvperioden är strömmen positiv och laddning transporteras åt ena hållet; under den andra halvperioden är den lika stor men negativ och laddningen transporteras tillbaka. Netto passerar därför **ingen** laddning under en hel period. Det är just därför växelström inte laddar upp något över tid.

---

### 3.12 – Energi lagrad i en spole
$L = 0{,}4\thinspace\text{H}$, $i(t) = 3t$ A

---

### Lösning
**a)**

```math
i'(t) = 3
```

**b)**

```math
p(t) = L\,i(t)\,i'(t) = 0{,}4 \cdot 3t \cdot 3 = 3{,}6t\,\text{W}
```

**c)**

```math
w(t) = \int_0^t 3{,}6\tau\,d\tau = \left[1{,}8\tau^2\right]_0^t = 1{,}8t^2\,\text{J}
```

**d)**

```math
w(2) = 1{,}8 \cdot 4 = 7{,}2\,\text{J}
```

**e)** Vid $t = 2\thinspace\text{s}$ är $i(2) = 6\thinspace\text{A}$:

```math
w = \frac{Li^2}{2} = \frac{0{,}4 \cdot 36}{2} = 7{,}2\,\text{J} \quad ✓
```

Integreringen ger alltså samma svar som den kända energiformeln – vilket är rimligt, eftersom formeln själv härleds genom just denna integrering.

---

### 3.13 – Energi utvecklad i ett motstånd
$p(t) = 5 + 2t$ W, $0 \leq t \leq 10\thinspace\text{s}$

---

### Lösning
**a)**

```math
w(t) = \int_0^t (5 + 2\tau)\,d\tau = \left[5\tau + \tau^2\right]_0^t = 5t + t^2\,\text{J}
```

**b)**

```math
w(10) = 50 + 100 = 150\,\text{J}
```

**c)**

```math
w(10) - w(5) = 150 - (25 + 25) = 150 - 50 = 100\,\text{J}
```

Två tredjedelar av energin utvecklas alltså under den sista halvan av tiden, eftersom effekten växer med tiden.

**d)**

```math
\bar{p} = \frac{w(10)}{10} = \frac{150}{10} = 15\,\text{W}
```

---

### 3.14 – Medelvärde av en funktion

---

### Lösning
**a)**

```math
\frac{1}{3}\int_0^3 x^2\,dx = \frac{1}{3} \cdot \frac{27}{3} = \frac{9}{3} = 3
```

**b)** Medelvärdet av en konstant är konstanten själv:

```math
\frac{1}{4}\int_1^5 4\,dx = \frac{16}{4} = 4
```

**c)** Först integralen över halvperioden:

```math
\int_0^{0{,}01} 10\sin(100\pi t)\,dt = \left[-\frac{10\cos(100\pi t)}{100\pi}\right]_0^{0{,}01} = \frac{20}{100\pi} \approx 0{,}0637
```

Sedan divideras med intervallets längd:

```math
\bar{i} = \frac{0{,}0637}{0{,}01} \approx 6{,}37\,\text{A}
```

**d)**

```math
\frac{6{,}37}{10} \approx 0{,}637 = \frac{2}{\pi}
```

Medelvärdet över en halv period är alltså $\dfrac{2}{\pi} \approx 0{,}64$, det vill säga 64 % av amplituden. Notera att detta är något helt annat än effektivvärdet, som är $\dfrac{1}{\sqrt{2}} \approx 0{,}71$, det vill säga 71 % av amplituden.

---

### 3.15 – Integralens räkneregler

---

### Lösning
**a)** Integralen av en summa är summan av integralerna:

```math
5 + 3 = 8
```

**b)** En konstant faktor kan flyttas utanför:

```math
2 \cdot 5 = 10
```

**c)**

```math
3 \cdot 5 - 2 \cdot 3 = 15 - 6 = 9
```

**d)** Byter man plats på gränserna byter integralen tecken:

```math
\int_2^0 f(x)\,dx = -\int_0^2 f(x)\,dx = -5
```

---

### 3.16 – Derivering och integrering som motsatser

---

### Lösning
**a)**

```math
F'(x) = 3x^2 - 2
```

**b)**

```math
\int (3x^2 - 2)\,dx = x^3 - 2x + C
```

**c)** Derivering **förstör** information: konstanttermen i $F(x)$ försvinner, eftersom dess derivata är noll. När man integrerar tillbaka går det därför inte att veta vilken konstant som fanns från början, och man skriver ett allmänt $C$. Här råkade $F(x)$ ha $C = 0$, men det syns inte i derivatan.

**d)**

```math
\frac{d}{dx}\left[\int 5x^4\,dx\right] = \frac{d}{dx}\left[x^5 + C\right] = 5x^4
```

Derivering och integrering tar alltså ut varandra – bortsett från just konstanten.

---

### 3.17 – Bestäm en okänd gräns eller konstant

---

### Lösning
**a)**

```math
\int_0^a 2x\,dx = \left[x^2\right]_0^a = a^2 = 25 \quad \Rightarrow \quad a = 5
```

**b)**

```math
\left[3x\right]_0^a = 3a = 12 \quad \Rightarrow \quad a = 4
```

**c)**

```math
\int_0^2 kx\,dx = k\left[\frac{x^2}{2}\right]_0^2 = 2k = 10 \quad \Rightarrow \quad k = 5
```

**d)** Med konstant ström är laddningen $q = it$:

```math
0{,}5t = 2 \quad \Rightarrow \quad t = 4\,\text{s}
```

---

### 3.18 – Hitta felet

---

### Lösning
**a)** Här har man deriverat i stället för att integrera. Exponenten ska **ökas**:

```math
\int x^2\,dx = \frac{x^3}{3} + C
```

**b)** Vid integrering hamnar den inre faktorn i nämnaren, inte i täljaren:

```math
\int e^{2x}\,dx = \frac{e^{2x}}{2} + C
```

**c)** Tecknet är fel. Kontrollera genom derivering: $\dfrac{d}{dx}\cos x = -\sin x$, inte $\sin x$:

```math
\int \sin(x)\,dx = -\cos(x) + C
```

**d)** Den undre gränsen har glömts bort. Båda gränserna måste sättas in:

```math
\left[x^3\right]_1^2 = 8 - 1 = 7
```

**e)** **Falskt.** I en bestämd integral tar konstanten ut sig själv:

```math
\left(F(b) + C\right) - \left(F(a) + C\right) = F(b) - F(a)
```

**f)** Absolutbeloppet saknas. För negativa $x$ är $\ln x$ odefinierat, medan $\ln|x|$ fungerar:

```math
\int \frac{1}{x}\,dx = \ln|x| + C
```

---

## Del 4 – Matematik i C

### 4.1 – Integralen som en summa i C

**a)**

```math
\int_0^{\pi} \sin(x)\,dx = \Big[-\cos(x)\Big]_0^{\pi} = -\cos(\pi) + \cos(0) = 1 + 1 = 2
```

**b)** Programmet ska skriva ut ungefär följande:

```text
     n      summa          fel
     4   1.896119     1.04e-01
    10   1.983524     1.65e-02
   100   1.999836     1.64e-04
  1000   1.999998     1.64e-06
```

**c)** Felet blir ungefär $100$ gånger mindre för varje tiodubbling av $n$. Det är ovanligt bra för rektanglar: för de flesta funktioner blir felet bara ungefär $10$ gånger mindre. Här är $\sin(0) = \sin(\pi) = 0$ och kurvan symmetrisk, så rektanglarnas fel på den stigande och den sjunkande sidan tar nästan ut varandra. Prova gärna med $f(x) = x$ på $[0, 2]$, där felet är exakt $\frac{2}{n}$.

**d)**

```math
\int_0^{1} e^{2x}\,dx = \left[\frac{e^{2x}}{2}\right]_0^{1} = \frac{e^2 - 1}{2} \approx 3{,}1945
```

Programmet ska skriva ut ungefär följande:

```text
     n      summa          fel
     4   2.462173     7.32e-01
    10   2.885717     3.09e-01
   100   3.162689     3.18e-02
  1000   3.191335     3.19e-03
```

Felet blir bara ungefär $10$ gånger mindre för varje tiodubbling av $n$, vilket är det vanliga. Eftersom $e^{2x}$ växer på hela intervallet ligger alla rektanglar under kurvan, så felen tar inte ut varandra som för $\sin(x)$.

---
