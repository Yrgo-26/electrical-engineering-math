# Lösningsförslag till övningstentamen 2

### Uppgift 1 (1,0 poäng)
Lös ekvationssystemet nedan för att beräkna strömmarna $I_1$ och $I_2$, angivna i $mA$:

```math
\begin{cases}
2I_1 + 3I_2 = 16 \\
4I_1 = I_2 + 4
\end{cases}
```

---

### Lösning
Vi löser ut $I_2$ ur den andra ekvationen:

```math
4I_1 = I_2 + 4 \quad \Rightarrow \quad I_2 = 4I_1 - 4
```

Vi sätter in uttrycket för $I_2$ i den första ekvationen:

```math
2I_1 + 3(4I_1 - 4) = 16 \quad \Rightarrow \quad 14I_1 - 12 = 16 \quad \Rightarrow \quad I_1 = 2
```

Vi sätter in $I_1 = 2$ i uttrycket för $I_2$:

```math
I_2 = 4 \cdot 2 - 4 = 4
```

**Kontroll:** I den första ekvationen är vänsterledet $2 \cdot 2 + 3 \cdot 4 = 16$. I den andra ekvationen är vänsterledet $4 \cdot 2 = 8$ och högerledet $4 + 4 = 8$.

**Svar:**

```math
I_1 = 2\,mA, \quad I_2 = 4\,mA
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

### Lösning
**a)** Vi sätter $P = 16$ och multiplicerar båda led med 4:

```math
\frac{U(20 - U)}{4} = 16 \quad \Rightarrow \quad 20U - U^2 = 64 \quad \Rightarrow \quad U^2 - 20U + 64 = 0
```

Vi löser ekvationen med PQ-formeln ($p = -20$, $q = 64$):

```math
U = 10 \pm \sqrt{10^2 - 64} = 10 \pm \sqrt{36} = 10 \pm 6
```

Därmed gäller att

```math
\begin{cases}
U_1 = 10 + 6 = 16\,V \\
U_2 = 10 - 6 = 4\,V
\end{cases}
```

**Kontroll:** $P(16) = \frac{16 \cdot 4}{4} = 16\thinspace W$ och $P(4) = \frac{4 \cdot 16}{4} = 16\thinspace W$.

**b)** För $U = 16\thinspace V$ blir strömmen och lastresistansen

```math
I = \frac{20 - 16}{4} = 1\,A, \qquad R = \frac{16}{1} = 16\,\Omega
```

och för $U = 4\thinspace V$

```math
I = \frac{20 - 4}{4} = 4\,A, \qquad R = \frac{4}{4} = 1\,\Omega
```

Lasten får samma effekt i båda fallen, men med $U = 16\thinspace V$ drar den bara en fjärdedel av strömmen. Den inre resistansen utvecklar då effekten $R_i I^2 = 4 \cdot 1^2 = 4\thinspace W$ i stället för $4 \cdot 4^2 = 64\thinspace W$, så mycket mindre energi går förlorad som värme i batteriet.

**Svar:** a) $U = 4\thinspace V$ eller $U = 16\thinspace V$. b) $U = 16\thinspace V$ ger $I = 1\thinspace A$ och $R = 16\thinspace\Omega$, medan $U = 4\thinspace V$ ger $I = 4\thinspace A$ och $R = 1\thinspace\Omega$. $U = 16\thinspace V$ är att föredra.

---

### Uppgift 3 (1,5 poäng)
Spänningen $U$ i volt över en komponent beror av strömmen $I$ i ampere enligt

```math
U(I) = \frac{3I^2 - 3I - 18}{I^2 - 9}
```

**a)** Förenkla uttrycket och ange vilka värden på $I$ som uttrycket inte får anta.

**b)** Bestäm strömmen $I$ då spänningen är $U = 2{,}7\thinspace V$.

---

### Lösning
**a)** Vi faktoriserar nämnaren med konjugatregeln:

```math
I^2 - 9 = (I + 3)(I - 3)
```

Nämnaren är alltså noll för $I = \pm 3$, vilket innebär att

```math
I \neq 3, \quad I \neq -3
```

Vi bryter ut 3 ur täljaren och beräknar nollställena för $I^2 - I - 6$ med PQ-formeln ($p = -1$, $q = -6$):

```math
I = \frac{1}{2} \pm \sqrt{\left(\frac{1}{2}\right)^2 + 6} = 0{,}5 \pm \sqrt{6{,}25} = 0{,}5 \pm 2{,}5
```

vilket ger $I = 3$ och $I = -2$, så $3I^2 - 3I - 18 = 3(I - 3)(I + 2)$. För $I \neq 3$ kan vi förkorta faktorn $(I - 3)$:

```math
U(I) = \frac{3(I - 3)(I + 2)}{(I + 3)(I - 3)} = \frac{3(I + 2)}{I + 3}
```

**b)** Vi sätter $U = 2{,}7$ och multiplicerar båda led med $I + 3$:

```math
\frac{3(I + 2)}{I + 3} = 2{,}7 \quad \Rightarrow \quad 3I + 6 = 2{,}7I + 8{,}1 \quad \Rightarrow \quad 0{,}3I = 2{,}1 \quad \Rightarrow \quad I = 7
```

$I = 7$ är ett tillåtet värde.

**Kontroll:** Med det ursprungliga uttrycket blir $U(7) = \frac{3 \cdot 49 - 21 - 18}{49 - 9} = \frac{108}{40} = 2{,}7\thinspace V$.

**Svar:** a) $U(I) = \frac{3(I + 2)}{I + 3}$, där $I \neq \pm 3$. b) $I = 7\thinspace A$.

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

### Lösning
**a)** Tidskonstanten blir

```math
RC = 100 \cdot 10^3 \cdot 100 \cdot 10^{-6} = 10\,s
```

**b)** Vi sätter $u(5) = 6{,}0$ och löser ut $U_0$:

```math
U_0 e^{-5/10} = 6{,}0 \quad \Rightarrow \quad U_0 = 6{,}0 \cdot e^{0{,}5} \approx 9{,}89\,V
```

**c)** Vi sätter $u(t) = \frac{U_0}{2}$ och dividerar båda led med $U_0$:

```math
U_0 e^{-t/10} = \frac{U_0}{2} \quad \Rightarrow \quad e^{-t/10} = 0{,}5
```

Vi tar den naturliga logaritmen $\ln$ i båda led:

```math
-\frac{t}{10} = \ln 0{,}5 \quad \Rightarrow \quad t = -10 \cdot \ln 0{,}5 = 10 \cdot \ln 2 \approx 6{,}93\,s
```

$U_0$ försvinner när vi dividerar, så svaret beror inte på begynnelsespänningen. Spänningen halveras alltid efter $RC \cdot \ln 2$, oavsett var den startar.

**Svar:** a) $RC = 10\thinspace s$. b) $U_0 \approx 9{,}89\thinspace V$. c) Efter ungefär $6{,}93\thinspace s$, oberoende av $U_0$.

---

### Uppgift 5 (1,0 poäng)
En växelspänning beskrivs av följande funktion:

```math
u(t) = 325 \sin\left(100\pi t + \frac{\pi}{6}\right)\,V
```

**a)** Ange spänningens amplitud, effektivvärde, frekvens, periodtid och fas. Effektivvärdet ges av $U_{RMS} = \frac{|U|}{\sqrt{2}}$. Ange fasen i grader.

**b)** Rita växelspänningens sinuskurva över en period $T$.

---

### Lösning
**a)** Vi jämför med den allmänna formen $u(t) = |U|\sin(wt + \delta)$. Amplituden är $|U| = 325\thinspace V$, och effektivvärdet blir

```math
U_{RMS} = \frac{325}{\sqrt{2}} \approx 230\,V
```

Vinkelhastigheten är $w = 100\pi\thinspace\text{rad/s}$, vilket ger

```math
f = \frac{w}{2\pi} = \frac{100\pi}{2\pi} = 50\,Hz, \qquad T = \frac{1}{f} = 0{,}02\,s = 20\,ms
```

Fasen är $\delta = \frac{\pi}{6}\thinspace\text{rad} = 30°$. Det är alltså den vanliga nätspänningen, $230\thinspace V$ och $50\thinspace Hz$.

**b)** Den positiva fasen innebär att kurvan ligger $\frac{30°}{360°} = \frac{1}{12}$ period, alltså ungefär $1{,}67\thinspace ms$, "före" en vanlig sinuskurva. Kurvan startar i $u(0) = 325\sin 30° = 162{,}5\thinspace V$, når maximum $325\thinspace V$ vid $t \approx 3{,}33\thinspace ms$, passerar noll nedåt vid $t \approx 8{,}33\thinspace ms$, når minimum $-325\thinspace V$ vid $t \approx 13{,}33\thinspace ms$, passerar noll uppåt vid $t \approx 18{,}33\thinspace ms$ och är tillbaka i $162{,}5\thinspace V$ när $t = 20\thinspace ms$.

**Svar:** a) Amplituden $325\thinspace V$, effektivvärdet ungefär $230\thinspace V$, frekvensen $50\thinspace Hz$, periodtiden $20\thinspace ms$ och fasen $30°$.

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

### Lösning
**a)** Vi deriverar term för term:

```math
i'(t) = 3t^2 - 18t + 24
```

**b)** Vi löser $i'(t) = 0$ och dividerar med 3:

```math
3t^2 - 18t + 24 = 0 \quad \Rightarrow \quad t^2 - 6t + 8 = 0
```

Med PQ-formeln ($p = -6$, $q = 8$):

```math
t = 3 \pm \sqrt{3^2 - 8} = 3 \pm 1
```

Funktionen är alltså stationär vid $t = 2\thinspace s$ och $t = 4\thinspace s$.

**c)** Andraderivatan är

```math
i''(t) = 6t - 18
```

```math
i''(2) = -6 < 0 \quad \Rightarrow \quad \text{maximipunkt}, \qquad i''(4) = 6 > 0 \quad \Rightarrow \quad \text{minimipunkt}
```

**d)** Vi sätter in de stationära punkterna i funktionen:

```math
i(2) = 8 - 36 + 48 = 20\,mA, \qquad i(4) = 64 - 144 + 96 = 16\,mA
```

**e)** Dessutom är $i(0) = 0\thinspace mA$, $i(3) = 27 - 81 + 72 = 18\thinspace mA$ och $i(5) = 125 - 225 + 120 = 20\thinspace mA$. Grafen startar i origo, stiger till maximipunkten $(2; 20)$, sjunker till minimipunkten $(4; 16)$ och stiger sedan igen till $(5; 20)$.

**f)** Vi beräknar derivatan vid $t = 1$:

```math
i'(1) = 3 - 18 + 24 = 9\,mA/s = 0{,}009\,A/s
```

Spänningen blir därmed

```math
u(1) = L \cdot i'(1) = 0{,}5 \cdot 0{,}009 = 0{,}0045\,V = 4{,}5\,mV
```

**Svar:** Maximum $i(2) = 20\thinspace mA$, minimum $i(4) = 16\thinspace mA$ och $u(1) = 4{,}5\thinspace mV$.

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

### Lösning
**a)** Vi integrerar term för term:

```math
I(t) = \int \left(0{,}06t^2 + 0{,}4t + 1\right)dt = 0{,}06 \cdot \frac{t^3}{3} + 0{,}4 \cdot \frac{t^2}{2} + t + C = 0{,}02t^3 + 0{,}2t^2 + t + C
```

**Kontroll:** Derivering av $I(t)$ ger $0{,}06t^2 + 0{,}4t + 1 = i(t)$.

**b)** Alla termer blir noll vid den undre gränsen $t = 0$, så bara $C$ finns kvar där och tar ut konstanten i den övre gränsen:

```math
q(t) = \big[0{,}02t^3 + 0{,}2t^2 + t + C\big]_0^t = 0{,}02t^3 + 0{,}2t^2 + t
```

**c)** Laddningen mellan $t = 2$ och $t = 5$ är den bestämda integralen över det intervallet:

```math
\int_2^5 i(t)\,dt = \big[0{,}02t^3 + 0{,}2t^2 + t\big]_2^5 = (2{,}5 + 5 + 5) - (0{,}16 + 0{,}8 + 2) = 12{,}5 - 2{,}96 = 9{,}54\,C
```

**d)** Intervallet är $5 - 2 = 3$ sekunder långt, så medelströmmen blir

```math
i_{medel} = \frac{9{,}54}{3} = 3{,}18\,A
```

**Svar:** a) $I(t) = 0{,}02t^3 + 0{,}2t^2 + t + C$. b) $q(t) = 0{,}02t^3 + 0{,}2t^2 + t$. c) $9{,}54\thinspace C$. d) $3{,}18\thinspace A$.

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

### Lösning
**a)** Impedansen på rektangulär form är

```math
Z = R + jX_L = 30 + j40\,\Omega
```

Absolutbeloppet och fasvinkeln blir

```math
|Z| = \sqrt{30^2 + 40^2} = \sqrt{2500} = 50\,\Omega, \qquad \delta_z = \tan^{-1}\left(\frac{40}{30}\right) \approx 53{,}1° \approx 0{,}93\,\text{rad}
```

$Z$ ligger i första kvadranten, så vinkeln behöver inte korrigeras: $Z \approx 50\angle 53{,}1°\thinspace\Omega$.

**b)** Vid division på polär form divideras beloppen och vinklarna subtraheras:

```math
I = \frac{U}{Z} \approx \frac{100\angle 0°}{50\angle 53{,}1°} = 2\angle{-53{,}1°}\,A
```

På rektangulär form blir strömmen

```math
I \approx 2\cos(-53{,}1°) + j2\sin(-53{,}1°) \approx 1{,}2 - j1{,}6\,A
```

**Kontroll:** Med nämnarens konjugat blir $I = \frac{100(30 - j40)}{30^2 + 40^2} = \frac{3000 - j4000}{2500} = 1{,}2 - j1{,}6\thinspace A$.

**c)** Vinkelhastigheten är $\omega = 2\pi f = 100\pi\thinspace\text{rad/s}$. Vi löser ut $L$ ur $X_L = \omega L$:

```math
L = \frac{X_L}{\omega} = \frac{40}{100\pi} = \frac{2}{5\pi} \approx 0{,}127\,H = 127\,mH
```

**Svar:** a) $Z = 30 + j40 \approx 50\angle 53{,}1°\thinspace\Omega$. b) $I \approx 2\angle{-53{,}1°}\thinspace A = 1{,}2 - j1{,}6\thinspace A$. c) $L \approx 127\thinspace mH$.

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

### Lösning
**a)** Fasorn $I = -8 - j6\thinspace mA$ ligger i tredje kvadranten i det komplexa talplanet (negativ reell del, negativ imaginär del).

**b)** Vi bestämmer först absolutbeloppet med Pythagoras sats:

```math
|I| = \sqrt{(-8)^2 + (-6)^2} = \sqrt{100} = 10\,mA
```

Vi bestämmer sedan fasvinkeln med $\tan^{-1}$:

```math
\delta = \tan^{-1}\left(\frac{-6}{-8}\right) \pm k\pi \approx 0{,}64 \pm k\pi\,\text{rad} \approx 36{,}9° \pm k \cdot 180°
```

$36{,}9°$ pekar in i första kvadranten, men $I$ ligger i tredje. Vi drar därför bort $180°$:

```math
\delta \approx 36{,}9° - 180° = -143{,}1° \approx -2{,}50\,\text{rad}
```

Därmed gäller att

```math
I \approx 10e^{-j2{,}50}\,mA
```

**c)** Vinkelhastigheten blir

```math
\omega = 2\pi f = 2\pi \cdot 50 = 100\pi\,\text{rad/s}
```

**d)** Med amplituden $|I| = 10\thinspace mA$ och fasen $\delta \approx -2{,}50\thinspace\text{rad}$ blir

```math
i(t) \approx 10\sin(100\pi t - 2{,}50)\,mA
```

**Svar:** b) $I \approx 10e^{-j2{,}50}\thinspace mA$ ($\delta \approx -143{,}1°$). c) $\omega = 100\pi\thinspace\text{rad/s}$. d) $i(t) \approx 10\sin(100\pi t - 2{,}50)\thinspace mA$.

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

### Lösning
**a)** Vi omvandlar sinusspänningarna till fasorer en efter en:

```math
U_1 = 4\cos(60°) + j4\sin(60°) \approx 2{,}000 + j3{,}464\,V
```

```math
U_2 = 3\cos(-30°) + j3\sin(-30°) \approx 2{,}598 - j1{,}500\,V
```

```math
U_3 = 2\cos(150°) + j2\sin(150°) \approx -1{,}732 + j1{,}000\,V
```

**b)** Vi adderar realdelar och imaginärdelar var för sig:

```math
U_{tot} \approx (2{,}000 + 2{,}598 - 1{,}732) + j(3{,}464 - 1{,}500 + 1{,}000) = 2{,}866 + j2{,}964\,V
```

**c)** $U_1$ ligger i första kvadranten, $U_2$ i fjärde och $U_3$ i andra. Summan $U_{tot}$ ligger i första kvadranten, ungefär på diagonalen.

**d)** Absolutbeloppet och fasvinkeln blir

```math
|U_{tot}| \approx \sqrt{2{,}866^2 + 2{,}964^2} \approx 4{,}12\,V
```

```math
\delta_{tot} = \tan^{-1}\left(\frac{2{,}964}{2{,}866}\right) \approx 46{,}0°
```

$U_{tot}$ ligger i första kvadranten, så vinkeln behöver inte korrigeras.

**Svar:**

```math
u_{tot}(t) \approx 4{,}12\sin(wt + 46{,}0°)\,V
```

---
