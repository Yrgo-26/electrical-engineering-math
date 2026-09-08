# L13 – Lektionsuppgifter

## Del 1 - Repetitionsuppgifter

### 1.1 – Analys av en kubisk funktion

Betrakta följande funktion:

```math
f(x) = -0,5x^3 + 1,5x^2 + 4,5x - 3
```

**a)** Derivera funktionen $f(x)$ och bestäm uttrycket för $f'(x)$.  
**b)** Bestäm var funktionen är stationär, dvs. lös ekvationen $f'(x) = 0$.  
**c)** Avgör med hjälp av den andra derivatan om respektive stationär punkt är ett maximum eller minimum.  
**d)** Beräkna funktionens största och minsta värde.  
**e)** Rita upp grafen för $f(x)$ via [Geogebra](https://www.geogebra.org/graphing?lang=en), kontrollera att
dina svar stämmer.

---

### 1.2 - Analys av spänning över en kondensator

En kondensator i en RC-krets laddas och urladdas upprepade gånger. Spänningen över kondensatorn kan beskrivas med följande funktion:

```math
u(t)= -0,2t^3 + 1,2t^2 - 1,4625t + 3,
```

där
* $u(t)$ = spänningen över kondensatorn i $V$,
* $t$ = tiden i sekunder, där $0 ≤ t ≤ 6$.

**a)** Derivera funktionen och bestäm uttrycket för spänningens förändringshastighet $u'(t)$.

**b)** Bestäm den tidpunkt (eller tidpunkter) då spänningen är stationär, dvs. när $u'(t) = 0$.

**c)** Avgör med hjälp av den andra derivatan om punkterna är maximi- eller minimipunkter.

**d)** Beräkna spänningens största och minsta värde.

**e)** Rita upp grafen för $u(t)$ via [Geogebra](https://www.geogebra.org/graphing?lang=en), kontrollera att
dina svar stämmer.

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

## Del 3 – Extrauppgifter
Uppgifterna nedan är extra träning och görs med fördel på egen hand efter lektionen. De flesta går att räkna i huvudet eller med papper och penna.

### 3.1 – Derivera trigonometriska funktioner
Derivera:

**a)** $f(x) = \sin(3x)$

**b)** $f(x) = \cos(5x)$

**c)** $f(x) = 4\sin(x)$

**d)** $f(x) = -2\cos(2x)$

**e)** $f(x) = \sin(x) + \cos(x)$

---

### 3.2 – Derivera exponentialfunktioner
Derivera:

**a)** $f(x) = e^{5x}$

**b)** $f(x) = 3e^{-2x}$

**c)** $f(x) = e^x + x^2$

**d)** $f(x) = 2^x$

**e)** $f(x) = 10e^{-x/4}$

---

### 3.3 – Derivera logaritmfunktioner
Derivera:

**a)** $f(x) = \ln x$

**b)** $f(x) = \ln(7x)$

**c)** $f(x) = 3\ln x$

**d)** $f(x) = \log_{10} x$

**e)** $f(x) = \ln x + e^x$

---

### 3.4 – Blandad derivering
Derivera:

**a)** $f(x) = 2e^{3x} - \sin(4x)$

**b)** $f(x) = x^2 + \ln(2x)$

**c)** $f(x) = 5\cos(x) - 3e^{-x}$

**d)** $f(x) = 4\sin(2x) + 4\cos(2x)$

---

### 3.5 – Derivatan i en punkt
Beräkna derivatan i den angivna punkten:

**a)** $f(x) = e^{2x}$ vid $x = 0$

**b)** $f(x) = \sin x$ vid $x = \dfrac{\pi}{2}$

**c)** $f(x) = \ln x$ vid $x = 2$

**d)** $f(x) = \cos(3x)$ vid $x = 0$

**e)** $f(x) = 3e^{-x}$ vid $x = 1$

---

### 3.6 – Ström genom en kondensator
Spänningen över en kondensator med $C = 47\thinspace\mu\text{F}$ ges av $u(t) = 10\sin(100\pi t)$ volt. Strömmen ges av $i_C(t) = C\dfrac{du}{dt}$.

**a)** Bestäm $u'(t)$.

**b)** Bestäm ett uttryck för $i_C(t)$.

**c)** Hur stor är strömmens amplitud?

**d)** Vid vilken tidpunkt är strömmen störst för första gången?

---

### 3.7 – Spänning över en spole
Strömmen genom en spole med $L = 25\thinspace\text{mH}$ ges av $i(t) = 2\sin(200t)$ ampere. Spänningen ges av $u_L(t) = L\dfrac{di}{dt}$.

**a)** Bestäm $i'(t)$.

**b)** Bestäm ett uttryck för $u_L(t)$.

**c)** Hur stor är spänningens amplitud?

**d)** Vilken fasskillnad har spänningen jämfört med strömmen?

---

### 3.8 – Urladdning av en kondensator
Spänningen ges av $u(t) = 20e^{-t/0{,}5}$ volt.

**a)** Bestäm $u'(t)$.

**b)** Beräkna $u'(0)$.

**c)** Beräkna $u'(0{,}5)$.

**d)** Vad säger tecknet på derivatan?

**e)** Visa att $u'(t) = -\dfrac{u(t)}{\tau}$ med $\tau = 0{,}5\thinspace\text{s}$.

---

### 3.9 – Stationär punkt för en exponentialfunktion
Funktionen $f(x) = xe^{-2x}$ är given.

**a)** Bestäm $f'(x)$ med produktregeln och bryt ut $e^{-2x}$.

**b)** Lös $f'(x) = 0$.

**c)** Avgör med $f''(x)$ om punkten är ett maximum eller ett minimum.

**d)** Beräkna funktionens extremvärde.

---

### 3.10 – Maximal effekt i tiden
Effekten i en komponent ges av $p(t) = 100te^{-t}$ watt för $t \geq 0$.

**a)** Bestäm $p'(t)$.

**b)** Vid vilken tidpunkt är effekten stationär?

**c)** Avgör med $p''(t)$ om det är ett maximum eller ett minimum.

**d)** Beräkna den maximala effekten.

---

### 3.11 – Derivatan av en dB-funktion
Förstärkningen ges av $G(x) = 20\log_{10}(x)$ dB.

**a)** Bestäm $G'(x)$.

**b)** Beräkna $G'(1)$.

**c)** Beräkna $G'(10)$.

**d)** Tolka skillnaden mellan svaren i **b)** och **c)**.

---

### 3.12 – Tangent till en exponentialkurva
Funktionen $f(x) = e^{-x}$ är given. Betrakta punkten där $x_0 = 0$.

**a)** Beräkna $f(0)$.

**b)** Beräkna $f'(0)$.

**c)** Bestäm tangentens ekvation.

**d)** Var skär tangenten x-axeln? Jämför med tidskonstanten $\tau$ i en urladdning.

---

### 3.13 – Derivatan hos en exponentiell urladdning
Spänningen ges av $u(t) = U_0e^{-t/\tau}$.

**a)** Visa att $u'(t) = -\dfrac{u(t)}{\tau}$.

**b)** Vad betyder detta samband fysikaliskt?

**c)** Beräkna $u'(0)$ och $u'(\tau)$ då $U_0 = 10\thinspace\text{V}$ och $\tau = 2\thinspace\text{s}$.

**d)** Hur stor andel av startspänningen återstår efter tiden $\tau$?

---

### 3.14 – Sant eller falskt
Avgör om påståendet är sant eller falskt och motivera kortfattat:

**a)** Derivatan av $\sin x$ är $-\cos x$.

**b)** Derivatan av $e^{3x}$ är $e^{3x}$.

**c)** Derivatan av $\ln(5x)$ är $\dfrac{1}{5x}$.

**d)** Derivatan av $\cos(2x)$ är $-2\sin(2x)$.

**e)** $e^x$ är sin egen derivata.

**f)** Derivatan av en konstant gånger en funktion är konstanten gånger funktionens derivata.

---

### 3.15 – Hitta felet
Varje rad innehåller ett vanligt fel. Förklara felet och ange det korrekta svaret.

**a)** $\dfrac{d}{dx}\sin(3x) = \cos(3x)$

**b)** $\dfrac{d}{dx}e^{-2x} = -2e^{-2x-1}$

**c)** $\dfrac{d}{dx}\ln(3x) = \dfrac{1}{3x}$

**d)** $\dfrac{d}{dx}4\cos(x) = 4\sin(x)$

**e)** $\dfrac{d}{dx}2^x = x \cdot 2^{x-1}$

---
