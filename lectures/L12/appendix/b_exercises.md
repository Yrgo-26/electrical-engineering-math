# L12 – Lektionsuppgifter

## Del 1 - Repetitionsuppgifter

### 1.1 - Linjär förstärkning
Sambandet mellan den linjära förstärkningen samt förstärkningen mätt i dB visas nedan:

```math
G_{dB}=20*log_{10}G_{lin} 
```

där
* $G_{dB}$ = förstärkningen i $dB$,
* $G_{lin}$ = den linjära förstärkningen.

En ljudförstärkare har en förstärkning på $26$ $dB$. Beräkna den motsvarande linjära spänningsförstärkningen.

### 1.2 - Uteffekt i dBm samt mW
Sambandet mellan en given effekt i $W$ samt motsvarande effekt i $dBm$ ($dB$ i förhållande till $1$ $mW$) visas nedan:

```math
P_{dBm}=10*log_{10}⁡\frac{P}{1 mW},
```

där 
* $P$ = effekten i $mW$,
* $P_{dBm}$ = motsvarande effekt i $dBm$.

En radiosändare har en uteffekt på $17$ $dBm$. Ange uteffekten i $mW$.

### 1.3 - Ljudnivå från multipla ljudkällor
För ett godtyckligt antal lika starka ljudkällor gäller att den totala ljudnivån kan beräknas enligt nedan:

```math
L_{tot}=L_{enkel}+10*log_{10}n,
```

där
* $L_{tot}$ = den totala ljudnivån,  
* $L_{enkel}$ = ljudnivån orsakad av en ljudkälla,
* $n$ = antalet ljudkällor.

Beräkna antalet lika starka ljudkällor om ljudet från en ljudkälla är $68$ $dB$ och den totala ljudnivån uppgår till $72,8$ dB.

## Del 2 - Nytt stoff

### 2.1 - Derivering av funktioner
Derivera följande funktioner:

**a)** $f(x) = -3x^2 + 5x + 2$

**b)** $f(x) = 2x^3 - 5x^2 + \frac{2x}{3} - 4$

**c)** $f(x) = 2x^4 - x^3 + \frac{3x^2}{5} + 4x - 1$

### 2.2 – Analys av en parabel

Betrakta följande funktion:

```math
f(x) = -x^2 + 8x - 7
```

**a)** Derivera funktionen $f(x)$, dvs. bestäm uttrycket för $f'(x)$.

**b)** Bestäm var funktionen är stationär, dvs. lös ekvationen $f'(x) = 0$.

**c)** Avgör med hjälp av den andra derivatan om punkten är ett **maximum** eller **minimum**.

**d)** Beräkna funktionens största eller minsta värde.

**e)** Rita upp grafen till $f(x)$ via [Geogebra](https://www.geogebra.org/graphing?lang=en), kontrollera att
dina svar stämmer.

### 2.3 – Analys av strömförlopp i en RC-krets

Strömmen genom en viss RC-krets kan approximeras med följande polynomfunktion:

```math
i(t) = -0,2t^3 + 1,8t^2 - 3,6t + 2,5
```

där  
* $i(t)$ = strömmen genom kretsen i $A$,  
* $t$ = tiden i sekunder.

**a)** Derivera funktionen för att bestämma uttrycket för strömmens förändring (strömändringshastigheten) $i'(t)$.

**b)** Beräkna den tidpunkt (eller tidpunkter) då strömmen är stationär, dvs. när $i'(t) = 0$.

**c)** Bestäm med hjälp av den **andra derivatan** om respektive stationär punkt är ett **maximum** eller **minimum**.

**d)** Beräkna strömmens maximi- och minimivärde, dvs. strömmen $i(t)$ i de stationära punkterna.

**e)** Rita grafen till $i(t)$ via [Geogebra](https://www.geogebra.org/graphing?lang=en), kontrollera att
dina svar stämmer.

---

## Del 3 – Extrauppgifter
Uppgifterna nedan är extra träning och görs med fördel på egen hand efter lektionen. De flesta går att räkna i huvudet eller med papper och penna.

### 3.1 – Derivera polynom
Derivera följande funktioner:

**a)** $f(x) = x^5$

**b)** $f(x) = 4x^3$

**c)** $f(x) = 7$

**d)** $f(x) = 2x^2 - 5x + 1$

**e)** $f(x) = -3x^4 + x$

**f)** $f(x) = \dfrac{x^3}{3}$

---

### 3.2 – Ändringskvot och derivatans definition
Funktionen $f(x) = x^2$ är given.

**a)** Ställ upp ändringskvoten över intervallet $[2,\thinspace 2+h]$ och förenkla den.

**b)** Vilket värde närmar sig kvoten när $h \to 0$?

**c)** Kontrollera svaret med deriveringsregeln $f'(x) = 2x$.

**d)** Beräkna ändringskvoten för $h = 0{,}1$ och $h = 0{,}01$.

---

### 3.3 – Derivatan i en punkt
Funktionen $f(x) = x^3 - 3x$ är given.

**a)** Bestäm $f'(x)$.

**b)** Beräkna $f'(0)$.

**c)** Beräkna $f'(2)$.

**d)** I vilka punkter är tangenten vågrät?

---

### 3.4 – Tangentens ekvation
Funktionen $f(x) = x^2 - 4x + 5$ är given. Betrakta punkten där $x_0 = 3$.

**a)** Beräkna $f(3)$.

**b)** Beräkna $f'(3)$.

**c)** Bestäm tangentens ekvation.

**d)** Var skär tangenten x-axeln?

---

### 3.5 – Stationär punkt hos en parabel
Funktionen $f(x) = x^2 - 6x + 8$ är given.

**a)** Bestäm $f'(x)$.

**b)** Lös $f'(x) = 0$.

**c)** Avgör med $f''(x)$ om punkten är ett maximum eller ett minimum.

**d)** Beräkna funktionens extremvärde.

---

### 3.6 – Stationära punkter hos en tredjegradsfunktion
Funktionen $f(x) = x^3 - 3x^2 - 9x + 5$ är given.

**a)** Bestäm $f'(x)$ och faktorisera uttrycket.

**b)** Bestäm de stationära punkternas $x$-värden.

**c)** Avgör med $f''(x)$ vilken punkt som är maximum respektive minimum.

**d)** Beräkna funktionsvärdena i båda punkterna.

---

### 3.7 – Växande och avtagande
Funktionen $f(x) = x^2 - 4x$ är given.

**a)** Bestäm $f'(x)$.

**b)** För vilka $x$ är funktionen växande?

**c)** För vilka $x$ är den avtagande?

**d)** Vad händer vid $x = 2$?

---

### 3.8 – Andra derivatan
Bestäm $f'(x)$ och $f''(x)$:

**a)** $f(x) = x^4 - 2x^2$

**b)** $f(x) = 5x^3 + 2x$

**c)** $f(x) = -x^2 + 7x - 1$

**d)** Vad säger tecknet på $f''(x)$ om kurvans form?

---

### 3.9 – Ström genom en kondensator
Strömmen genom en kondensator ges av $i_C(t) = C\dfrac{du}{dt}$. En kondensator med $C = 100\thinspace\mu\text{F}$ har spänningen $u(t) = 4t^2 + 2t$ volt.

**a)** Bestäm $u'(t)$.

**b)** Bestäm ett uttryck för $i_C(t)$ i mA.

**c)** Beräkna strömmen vid $t = 1\thinspace\text{s}$.

**d)** Vid vilken tidpunkt är strömmen $2\thinspace\text{mA}$?

---

### 3.10 – Spänning över en spole
Spänningen över en spole ges av $u_L(t) = L\dfrac{di}{dt}$. En spole med $L = 0{,}5\thinspace\text{H}$ genomflyts av strömmen $i(t) = 2t^2 - 4t + 3$ ampere.

**a)** Bestäm $i'(t)$.

**b)** Bestäm ett uttryck för $u_L(t)$.

**c)** Vid vilken tidpunkt är $u_L = 0$?

**d)** Vad händer med strömmen vid denna tidpunkt?

---

### 3.11 – Maximal effekt
Effekten som en generator levererar till en last varierar med strömmen enligt $P(I) = 24I - 3I^2$ watt.

**a)** Bestäm $P'(I)$.

**b)** Vid vilken ström är effekten stationär?

**c)** Avgör med $P''(I)$ om det är ett maximum eller ett minimum.

**d)** Beräkna den maximala effekten.

---

### 3.12 – Förändringshastighet i en signal
En spänning ges av $u(t) = -2t^2 + 12t$ volt för $0 \leq t \leq 6\thinspace\text{s}$.

**a)** Bestäm $u'(t)$.

**b)** Vid vilken tidpunkt är spänningen störst, och hur stor är den då?

**c)** Hur snabbt ändras spänningen vid $t = 1\thinspace\text{s}$?

**d)** Vid vilken tidpunkt minskar spänningen med $4\thinspace\text{V/s}$?

---

### 3.13 – Tolkning av derivatans tecken
För en funktion $f$ gäller följande: $f'(1) = 3$, $f'(2) = 0$, $f'(3) = -2$ och $f''(2) = -5$.

**a)** Är $f$ växande eller avtagande vid $x = 1$?

**b)** Är $f$ växande eller avtagande vid $x = 3$?

**c)** Vilken typ av punkt är $x = 2$?

**d)** Beskriv med ord hur grafen ser ut kring $x = 2$.

---

### 3.14 – Hitta felet
Varje rad innehåller ett vanligt deriveringsfel. Förklara felet och ange det korrekta svaret.

**a)** $f(x) = x^3 \quad \Rightarrow \quad f'(x) = 3x^2 \cdot x$

**b)** $f(x) = 5 \quad \Rightarrow \quad f'(x) = 5$

**c)** $f(x) = 4x \quad \Rightarrow \quad f'(x) = 4x$

**d)** $f(x) = 3x^2 + 2x \quad \Rightarrow \quad f'(x) = 6x + 2x$

**e)** Om $f'(x_0) = 0$ är $x_0$ alltid en maximipunkt.

**f)** $f''(x)$ fås genom att kvadrera $f'(x)$.

---
