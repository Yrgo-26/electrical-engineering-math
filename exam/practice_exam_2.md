# Övningstentamen 2

## Tillåtna hjälpmedel
* Skrivmaterial och valfri miniräknare.
* Ett hand- eller datorskrivet A4-ark (båda sidor) med valfria formler, exempel och egna anteckningar.

> **OBS!** Mobiltelefoner får inte användas under den tid som tentamen pågår och ska placeras på angiven plats.

## Poäng
Totalt 16 poäng. Därtill kan upp till 1,0 bonuspoäng erhållas från dugga 1–2.

## Betygsgränser
* IG < 6,5 poäng
* G >= 6,5 poäng
* VG >= 11 poäng

## Övrigt
Alla uppgifter kräver lösningar/motiveringar med redovisat svar (inklusive enhet där det är aktuellt). Du måste alltså förklara hur du kom fram till dina resultat! Lycka till!

---

### Uppgift 1 (1,0 poäng)
Lös ekvationssystemet nedan för att beräkna strömmarna $I_1$ och $I_2$, angivna i $mA$:

```math
\begin{cases}
2I_1 + 3I_2 = 16 \\
4I_1 = I_2 + 4
\end{cases}
```

---

### Uppgift 2 (2,0 poäng)
Ett batteri med tomgångsspänningen $E = 20\thinspace V$ och den inre resistansen $R_i = 4\thinspace\Omega$ är anslutet till en last. Strömmen är $I = \frac{E - U}{R_i}$, där $U$ är klämspänningen, så effekten i lasten ges av

```math
P(U) = U \cdot I = \frac{U(20 - U)}{4}
```

**a)** Bestäm klämspänningen $U$ så att effekten i lasten blir $P = 16\thinspace W$. Ekvationen har två lösningar.

**b)** Beräkna strömmen $I$ och lastresistansen $R = \frac{U}{I}$ för respektive lösning. Vilken lösning är att föredra om batteriet ska räcka så länge som möjligt? Motivera svaret.

---

### Uppgift 3 (1,5 poäng)
Spänningen $U$ i volt över en komponent beror av strömmen $I$ i ampere enligt

```math
U(I) = \frac{3I^2 - 3I - 18}{I^2 - 9}
```

**a)** Förenkla uttrycket och ange vilka värden på $I$ som uttrycket inte får anta.

**b)** Bestäm strömmen $I$ då spänningen är $U = 2{,}7\thinspace V$.

---

### Uppgift 4 (1,5 poäng)
När en kondensator urladdas genom ett motstånd minskar spänningen över kondensatorn exponentiellt med tiden. Spänningen $u(t)$ kan beskrivas med följande funktion:

```math
u(t) = U_0 e^{-t/(RC)}
```

där

* $u(t)$ = spänningen över kondensatorn vid tiden $t$,
* $U_0$ = begynnelsespänningen i $V$,
* $RC$ = kretsens tidskonstant i sekunder,
* $t$ = tiden i sekunder.

En kondensator med kapacitansen $100\thinspace\mu F$ urladdas genom ett motstånd på $100\thinspace\text{k}\Omega$ från tiden $t = 0$. Efter 5 sekunder mäts spänningen till $6{,}0\thinspace V$.

**a)** Beräkna kretsens tidskonstant $RC$.

**b)** Bestäm begynnelsespänningen $U_0$.

**c)** Beräkna efter hur lång tid spänningen har sjunkit till hälften av $U_0$. Beror svaret på $U_0$?

---

### Uppgift 5 (1,0 poäng)
En växelspänning beskrivs av följande funktion:

```math
u(t) = 325 \sin\left(100\pi t + \frac{\pi}{6}\right)\,V
```

**a)** Ange spänningens amplitud, effektivvärde, frekvens, periodtid och fas. Effektivvärdet ges av $U_{RMS} = \frac{|U|}{\sqrt{2}}$. Ange fasen i grader.

**b)** Rita växelspänningens sinuskurva över en period $T$.

---

### Uppgift 6 (2,0 poäng)
Strömmen genom en spole varierar under en mätning enligt

```math
i(t) = t^3 - 9t^2 + 24t\,mA,
```

där $t$ är tiden i sekunder och $0 \leq t \leq 5$.

**a)** Derivera funktionen $i(t)$ och bestäm uttrycket för $i'(t)$.

**b)** Bestäm de tidpunkter då funktionen är stationär, dvs. lös $i'(t) = 0$.

**c)** Avgör med hjälp av andraderivatan om respektive punkt är ett maximum eller ett minimum.

**d)** Beräkna strömmen i de stationära punkterna.

**e)** Rita grafen till $i(t)$ för intervallet $0 \leq t \leq 5\thinspace s$. Markera extrempunkterna.

**f)** Spänningen över spolen är $u(t) = L \cdot i'(t)$. Beräkna spänningen vid tiden $t = 1\thinspace s$ om induktansen är $L = 0{,}5\thinspace H$.

---

### Uppgift 7 (1,5 poäng)
Laddningen $q(t)$ som passerar genom en ledare inom ett tidsintervall $(0, t)$ kan beräknas via följande funktion:

```math
q(t) = \int_0^t i(t)\,dt = \big[I(t)\big]_0^t,
```

där

* $q(t)$ är laddningen genom ledaren i $C$ (Coulomb),
* $i(t)$ är strömmen som passerar genom ledaren i $A$ (Ampere),
* $I(t)$ är den primitiva funktionen (obestämda integralen) av $i(t)$.

Strömmen $i(t)$ in i ett batteri som laddas ges av följande funktion:

```math
i(t) = 0{,}06t^2 + 0{,}4t + 1
```

där $t$ är tiden i sekunder.

**a)** Bestäm ett uttryck för den primitiva funktionen $I(t) = \int i(t)\thinspace dt$, dvs. integrera utan att ange några gränser.

**b)** Bestäm ett uttryck för laddningen $q(t)$ genom att integrera över intervallet $[0, t]$.

**c)** Beräkna laddningen som flödar in i batteriet mellan $t = 2\thinspace s$ och $t = 5\thinspace s$.

**d)** Beräkna medelströmmen under samma intervall, dvs. laddningen delat med intervallets längd.

---

### Uppgift 8 (2,0 poäng)
En resistor $R = 30\thinspace\Omega$ och en spole med reaktansen $X_L = 40\thinspace\Omega$ är seriekopplade och matas med spänningen $U = 100\angle 0°\thinspace V$. Strömmen $I$ genom kretsen kan beräknas med "Ohms lag", dvs. Ohms lag anpassad för komplexa tal:

```math
I = \frac{U}{Z}
```

**a)** Bestäm kretsens impedans $Z = R + jX_L$ och ange den både på rektangulär och polär form.

**b)** Beräkna strömmen $I$ och ange den både på polär och rektangulär form.

**c)** Frekvensen är $f = 50\thinspace Hz$. Beräkna spolens induktans $L$, där $X_L = \omega L$.

---

### Uppgift 9 (1,5 poäng)
En ström $i(t)$ i en växelströmskrets kan representeras av en fasor $I$, som på rektangulär form skrivs enligt nedan:

```math
I = -8 - j6\,mA
```

**a)** Rita ut fasorn $I$ i det komplexa talplanet (x-axeln = reell del, y-axeln = imaginär del).

**b)** Uttryck fasorn $I$ på Eulers form, dvs. bestäm absolutbeloppet $|I|$ samt fasvinkeln $\delta$ så att $I = |I|e^{j\delta}$.

**c)** Anta att strömmens frekvens $f = 50\thinspace Hz$. Bestäm vinkelhastigheten $\omega$.

**d)** Skriv strömmen som en sinusformad funktion av tiden, $i(t) = |I|\sin(\omega t + \delta)$.

---

### Uppgift 10 (2,0 poäng)
I en seriekoppling med tre komponenter mäts växelspänningen över respektive komponent till:

```math
u_1(t) = 4\sin(wt + 60°)\,V
```

```math
u_2(t) = 3\sin(wt - 30°)\,V
```

```math
u_3(t) = 2\sin(wt + 150°)\,V
```

Den totala spänningen i kretsen $u_{tot}(t)$ beräknas enligt nedan:

```math
u_{tot}(t) = u_1(t) + u_2(t) + u_3(t)
```

**a)** Skriv om spänningarna $u_1(t)$, $u_2(t)$ samt $u_3(t)$ till fasorer $U_1$, $U_2$ samt $U_3$ i komplex rektangulär form.

**b)** Beräkna fasorsumman $U_{tot} = U_1 + U_2 + U_3$.

**c)** Rita ut fasorerna i det komplexa talplanet (x-axeln = reell del, y-axeln = imaginär del).

**d)** Omvandla tillbaka resultatet till en sinusformad spänning i tidsdomänen på formen $u_{tot}(t) = |U_{tot}|\sin(wt + \delta_{tot})$.

---
