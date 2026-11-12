# Övningstentamen 1

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
3I_1 - I_2 = 7 \\
3I_2 = I_1 + 3
\end{cases}
```

---

### Uppgift 2 (2,0 poäng)
Ett batteri med tomgångsspänningen $E = 24\thinspace V$ och den inre resistansen $R_i = 6\thinspace\Omega$ är anslutet till en last med resistansen $R$. Effekten $P$ som utvecklas i lasten ges av

```math
P = \frac{E^2 R}{(R + R_i)^2}
```

**a)** Bestäm lastresistansen $R$ så att effekten i lasten blir $P = 18\thinspace W$. Ekvationen har två lösningar.

**b)** Beräkna strömmen $I = \frac{E}{R + R_i}$ för respektive lösning. Vilken lösning är att föredra om batteriet ska räcka så länge som möjligt? Motivera svaret.

---

### Uppgift 3 (1,5 poäng)
Spänningen $U$ i volt över en komponent beror av strömmen $I$ i ampere enligt

```math
U(I) = \frac{4I^2 - 36}{I^2 - I - 6}
```

**a)** Förenkla uttrycket och ange vilka värden på $I$ som uttrycket inte får anta.

**b)** Beräkna spänningen $U$ när strömmen är $I = 2\thinspace A$.

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

En kondensator med kapacitansen $680\thinspace\mu F$ är ansluten till ett motstånd på $10\thinspace\text{k}\Omega$. Den är initialt laddad till $10\thinspace V$ och börjar urladdas vid tiden $t = 0$.

**a)** Beräkna spänningen efter tre sekunder.

**b)** Bestäm funktionens definitionsmängd och värdemängd för tidsintervallet $0 - 10$ sekunder.

**c)** Beräkna efter hur lång tid spänningen har sjunkit till 40 % av sitt ursprungliga värde.

---

### Uppgift 5 (1,0 poäng)
En växelspänning har amplituden $5\thinspace V$, frekvensen $100\thinspace Hz$ samt fasen 90°.

**a)** Bestäm växelspänningens ekvation $u(t)$. Ange fasen i radianer.

**b)** Rita växelspänningens sinuskurva över en period $T$.

---

### Uppgift 6 (2,0 poäng)
Batteriet i uppgift 2, med tomgångsspänningen $E = 24\thinspace V$ och den inre resistansen $R_i = 6\thinspace\Omega$, levererar strömmen $I$ till en last. Klämspänningen är $U = E - R_i I$, så effekten i lasten som funktion av strömmen blir

```math
P(I) = U \cdot I = (24 - 6I) \cdot I = 24I - 6I^2
```

**a)** Derivera funktionen $P(I)$ och bestäm uttrycket för $P'(I)$.

**b)** Bestäm var funktionen är stationär, dvs. lös $P'(I) = 0$.

**c)** Avgör med hjälp av andraderivatan om punkten är ett maximum eller ett minimum.

**d)** Beräkna funktionens största eller minsta värde, dvs. bestäm $P(I)$ i den punkt där funktionen är stationär.

**e)** Rita grafen till $P(I)$ för intervallet $0 \leq I \leq 4\thinspace A$. Markera extrempunkten och skärningarna med axlarna.

**f)** Beräkna lastresistansen $R = \frac{U}{I}$ i den stationära punkten och jämför den med $R_i$.

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

Strömmen $i(t)$ i en kondensator ges av följande funktion:

```math
i(t) = 0{,}03t^2 + 0{,}1t + 0{,}5
```

där $t$ är tiden i sekunder. Kondensatorn har redan laddningen $q_0 = 1\thinspace C$ vid start.

**a)** Bestäm ett uttryck för den primitiva funktionen $I(t) = \int i(t)\thinspace dt$, dvs. integrera utan att ange några gränser.

**b)** Bestäm ett uttryck för kondensatorns laddning $q(t)$ genom att integrera över intervallet $[0, t]$.

**c)** Bestäm en formel för den totala laddningen $q_{tot}(t)$ i kondensatorn, inklusive startladdningen $q_0$.

**d)** Hur stor total laddning (inklusive startladdningen) har flödat in i kondensatorn efter 4 sekunder?

---

### Uppgift 8 (2,0 poäng)
En krets matas med spänningen $U = 3 - j4\thinspace V$. Kretsen har impedansen $Z = 2 + j2\thinspace\Omega$. Strömmen $I$ genom kretsen kan beräknas med "Ohms lag", dvs. Ohms lag anpassad för komplexa tal:

```math
I = \frac{U}{Z}
```

**a)** Beräkna strömmen $I$ och ange den både på rektangulär och polär form.

**b)** Impedansen kan skrivas $Z = R + jX$. Ange resistansen $R$ och reaktansen $X$, och avgör om kretsen är induktiv eller kapacitiv.

**c)** Frekvensen är $f = 50\thinspace Hz$. Beräkna den induktans eller kapacitans som ger kretsens reaktans.

---

### Uppgift 9 (1,5 poäng)
En ström $i(t)$ i en växelströmskrets kan representeras av en fasor $I$, som på rektangulär form skrivs enligt nedan:

```math
I = 10 - j5\,mA
```

**a)** Rita ut fasorn $I$ i det komplexa talplanet (x-axeln = reell del, y-axeln = imaginär del).

**b)** Uttryck fasorn $I$ på Eulers form, dvs. bestäm absolutbeloppet $|I|$ samt fasvinkeln $\delta$ så att $I = |I|e^{j\delta}$.

**c)** Anta att strömmens frekvens $f = 10\thinspace Hz$. Bestäm vinkelhastigheten $w$.

**d)** Skriv $i(t)$ som en tidsberoende funktion $i(t) = |I| \cdot e^{j(wt+\delta)}$.

---

### Uppgift 10 (2,0 poäng)
I en seriekoppling med tre komponenter mäts växelspänningen över respektive komponent till:

```math
u_1(t) = 2\sin(wt + 25°)\,V
```

```math
u_2(t) = 5\sin(wt - 45°)\,V
```

```math
u_3(t) = 1{,}5\sin(wt + 36°)\,V
```

Den totala spänningen i kretsen $u_{tot}(t)$ beräknas enligt nedan:

```math
u_{tot}(t) = u_1(t) + u_2(t) + u_3(t)
```

**a)** Skriv om spänningarna $u_1(t)$, $u_2(t)$ samt $u_3(t)$ till fasorer $U_1$, $U_2$ samt $U_3$ i komplex rektangulär form.

**b)** Beräkna fasorsumman $U_{tot} = U_1 + U_2 + U_3$.

**c)** Rita ut fasorerna i det komplexa talplanet (x-axeln = reell del, y-axeln = imaginär del).

**d)** Omvandla tillbaka resultatet till en sinusformad spänning i tidsdomänen på följande form:

```math
u_{tot}(t) = |U_{tot}| \sin(wt + \delta_{tot})
```

---
