# Lösningsförslag till övningstentamen 1

### Uppgift 1 (1,0 poäng)
Lös ekvationssystemet nedan för att beräkna strömmarna $I_1$ och $I_2$, angivna i $mA$:

```math
\begin{cases}
3I_1 - I_2 = 7 \\
3I_2 = I_1 + 3
\end{cases}
```

---

### Lösning
Vi börjar med att lösa ut $I_2$ ur den första ekvationen:

```math
3I_1 - I_2 = 7 \quad \Rightarrow \quad I_2 = 3I_1 - 7
```

Vi sätter in uttrycket för $I_2$ i den andra ekvationen:

```math
3(3I_1 - 7) = I_1 + 3,
```

vilket kan förenklas till

```math
9I_1 - 21 = I_1 + 3 \quad \Rightarrow \quad 8I_1 = 24 \quad \Rightarrow \quad I_1 = 3
```

Vi sätter in $I_1 = 3$ i uttrycket för $I_2$:

```math
I_2 = 3 \cdot 3 - 7 = 2
```

**Kontroll:** I den första ekvationen är vänsterledet $3 \cdot 3 - 2 = 7$, vilket stämmer med högerledet. I den andra ekvationen är vänsterledet $3 \cdot 2 = 6$ och högerledet $3 + 3 = 6$.

**Svar:**

```math
I_1 = 3\,mA, \quad I_2 = 2\,mA
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

### Lösning
**a)** Vi sätter in de givna värdena:

```math
18 = \frac{24^2 \cdot R}{(R + 6)^2} = \frac{576R}{(R + 6)^2}
```

Vi multiplicerar båda led med $(R + 6)^2$, vilket går eftersom $R > 0$ och nämnaren därmed aldrig blir noll:

```math
18(R + 6)^2 = 576R
```

Division med 18 i båda led ger

```math
(R + 6)^2 = 32R
```

Vi utvecklar kvadraten i vänsterledet:

```math
R^2 + 12R + 36 = 32R \quad \Rightarrow \quad R^2 - 20R + 36 = 0
```

Vi löser ekvationen med PQ-formeln ($p = -20$, $q = 36$):

```math
R = 10 \pm \sqrt{10^2 - 36} = 10 \pm \sqrt{64} = 10 \pm 8
```

Därmed gäller att

```math
\begin{cases}
R_1 = 10 + 8 = 18\,\Omega \\
R_2 = 10 - 8 = 2\,\Omega
\end{cases}
```

**Kontroll:** För $R = 18\thinspace\Omega$ blir $P = \frac{576 \cdot 18}{24^2} = 18\thinspace W$, och för $R = 2\thinspace\Omega$ blir $P = \frac{576 \cdot 2}{8^2} = 18\thinspace W$.

**b)** För $R = 18\thinspace\Omega$ blir strömmen

```math
I = \frac{24}{18 + 6} = 1\,A
```

och för $R = 2\thinspace\Omega$

```math
I = \frac{24}{2 + 6} = 3\,A
```

Lasten får samma effekt i båda fallen, men med $R = 18\thinspace\Omega$ drar den bara en tredjedel av strömmen. Den inre resistansen utvecklar då effekten $R_i I^2 = 6 \cdot 1^2 = 6\thinspace W$ i stället för $6 \cdot 3^2 = 54\thinspace W$, så mycket mindre energi går förlorad som värme i batteriet.

**Svar:** a) $R = 2\thinspace\Omega$ eller $R = 18\thinspace\Omega$. b) $I = 3\thinspace A$ respektive $1\thinspace A$. $R = 18\thinspace\Omega$ är att föredra, eftersom den ger samma effekt med en tredjedel av strömmen.

---

### Uppgift 3 (1,5 poäng)
Spänningen $U$ i volt över en komponent beror av strömmen $I$ i ampere enligt

```math
U(I) = \frac{4I^2 - 36}{I^2 - I - 6}
```

**a)** Förenkla uttrycket och ange vilka värden på $I$ som uttrycket inte får anta.

**b)** Beräkna spänningen $U$ när strömmen är $I = 2\thinspace A$.

---

### Lösning
**a)** Vi faktoriserar täljaren genom att bryta ut 4 och använda konjugatregeln:

```math
4I^2 - 36 = 4(I^2 - 9) = 4(I + 3)(I - 3)
```

För att ta reda på vilka värden $I$ inte får anta undersöker vi när nämnaren blir noll:

```math
I^2 - I - 6 = 0
```

Vi löser ekvationen med PQ-formeln ($p = -1$, $q = -6$):

```math
I = \frac{1}{2} \pm \sqrt{\left(\frac{1}{2}\right)^2 + 6} = 0{,}5 \pm \sqrt{6{,}25} = 0{,}5 \pm 2{,}5
```

Nämnaren är alltså noll för $I = 3$ och $I = -2$, vilket innebär att

```math
I \neq 3, \quad I \neq -2
```

Med nollställena kan nämnaren faktoriseras som $I^2 - I - 6 = (I - 3)(I + 2)$. Vi sätter in den faktoriserade täljaren och nämnaren:

```math
U(I) = \frac{4(I + 3)(I - 3)}{(I - 3)(I + 2)}
```

För $I \neq 3$ kan vi förkorta faktorn $(I - 3)$, som förekommer både i täljaren och nämnaren:

```math
U(I) = \frac{4(I + 3)}{I + 2}
```

**b)** Vi sätter in $I = 2$ i det förenklade uttrycket:

```math
U(2) = \frac{4(2 + 3)}{2 + 2} = \frac{20}{4} = 5\,V
```

**Kontroll:** Med det ursprungliga uttrycket blir $U(2) = \frac{4 \cdot 4 - 36}{4 - 2 - 6} = \frac{-20}{-4} = 5\thinspace V$.

**Svar:** a) $U(I) = \frac{4(I + 3)}{I + 2}$, där $I \neq -2$ och $I \neq 3$. b) $U(2) = 5\thinspace V$.

---

### Uppgift 4 (1,5 poäng)
När en kondensator urladdas genom ett motstånd minskar spänningen över kondensatorn exponentiellt med tiden. Spänningen $u(t)$ kan beskrivas med följande funktion:

```math
u(t) = U_0 e^{-t/(RC)}
```

En kondensator med kapacitansen $680\thinspace\mu F$ är ansluten till ett motstånd på $10\thinspace\text{k}\Omega$. Den är initialt laddad till $10\thinspace V$ och börjar urladdas vid tiden $t = 0$.

**a)** Beräkna spänningen efter tre sekunder.

**b)** Bestäm funktionens definitionsmängd och värdemängd för tidsintervallet $0 - 10$ sekunder.

**c)** Beräkna efter hur lång tid spänningen har sjunkit till 40 % av sitt ursprungliga värde.

---

### Lösning
**a)** Med angivna värden kan ovanstående formel skrivas om enligt nedan:

```math
u(t) = 10 e^{-t/(680\mu \cdot 10\text{k})} = 10 e^{-t/6{,}8}\,V
```

Vi beräknar $u(3)$ för att beräkna spänningen efter tre sekunder:

```math
u(3) = 10 e^{-3/6{,}8} \approx 6{,}43\,V
```

**b)** Definitionsmängden är given i uppgiftsbeskrivningen:

```math
0 \leq t \leq 10\,s
```

Värdemängden erhålls genom att beräkna $u(0)$ samt $u(10)$:

```math
u(0) = 10 e^{-0/6{,}8} = 10 \cdot e^0 = 10\,V
```

```math
u(10) = 10 e^{-10/6{,}8} \approx 2{,}30\,V
```

Därmed gäller att

```math
2{,}30\,V \leq u(t) \leq 10\,V
```

**c)** För att beräkna efter hur lång tid $t$ som spänningen har minskat till 40 % av ursprungsvärdet $10\thinspace V$ sätter vi $u(t) = 10 \cdot 0{,}4 = 4\thinspace V$:

```math
u(t) = 10 e^{-t/6{,}8} = 4
```

Genom att dividera med 10 i båda led kan ovanstående uttryck skrivas om till

```math
e^{-t/6{,}8} = 0{,}4
```

För att lösa ut $t$ tar vi den naturliga logaritmen $\ln$ i båda led:

```math
-\frac{t}{6{,}8} = \ln 0{,}4
```

Genom att multiplicera med $-6{,}8$ i båda led kan $t$ beräknas, då

```math
t = -6{,}8 \cdot \ln 0{,}4 \approx 6{,}23\,s
```

**Svar:** Efter ungefär 6,23 sekunder har spänningen minskat till 40 % av ursprungsvärdet.

> **Notering om källan:** I originallösningen anges texten "kan $t$ beräknas till ca 3,26 sekunder" precis innan samma formel räknas ut till $\approx 6{,}23\thinspace s$. De två talen stämmer inte överens — $-6{,}8 \cdot \ln 0{,}4 \approx 6{,}23$, inte 3,26 — så "3,26 sekunder" är sannolikt ett skrivfel i originalet. Det korrekta svaret, 6,23 s, används konsekvent i resten av lösningen och är det som redovisas ovan.

---

### Uppgift 5 (1,0 poäng)
En växelspänning har amplituden $5\thinspace V$, frekvensen $100\thinspace Hz$ samt fasen 90°.

**a)** Bestäm växelspänningens ekvation $u(t)$. Ange fasen i radianer.

**b)** Rita växelspänningens sinuskurva över en period $T$.

---

### Lösning
**a)** Formeln för en växelspänning $u(t)$ är följande:

```math
u(t) = |U| \sin(wt + \delta),
```

där $|U|$ är amplituden (toppvärdet), $w$ är vinkelhastigheten, $t$ är tiden och $\delta$ är fasen.

Sinuskurvans amplitud/toppvärde $|U|$ är enligt uppgift lika med $5\thinspace V$:

```math
|U| = 5\,V
```

Sinuskurvans frekvens $f$ är enligt uppgift lika med $100\thinspace Hz$. Motsvarande vinkelhastighet $w$ är därmed lika med $200\pi\thinspace\text{rad/s}$:

```math
w = 2\pi f = 2\pi \cdot 100 = 200\pi\,\text{rad/s}
```

Fasen $\delta$ är enligt uppgift lika med 90°, vilket motsvarar $\pi/2\thinspace\text{rad}$, då

```math
\delta_{rad} = \delta_{deg} \cdot \frac{\pi}{180°} = 90 \cdot \frac{\pi}{180} = \frac{90\pi}{180} = \frac{\pi}{2}\,\text{rad}
```

För växelspänningen $u(t)$ gäller därmed följande:

```math
u(t) = 5 \sin\left(200\pi t + \frac{\pi}{2}\right)\,V
```

**b)** Vi utgår från sinuskurvans attribut. Eftersom frekvensen $f$ är lika med $100\thinspace Hz$ gäller att periodtiden $T$ är $10\thinspace ms$, då

```math
T = \frac{1}{f} = \frac{1}{100} = 0{,}01\,s = 10\,ms
```

Vi ska då rita ut en sinuskurva som repeteras var 10:e millisekund. För en sinuskurva gäller följande:
* Spänningen är lika med 0 i början av varje varv samt efter ett halvt varv.
* Spänningens maximivärde $|U| = 5\thinspace V$ nås efter en fjärdedel av ett varv.
* Spänningens minimivärde $-|U| = -5\thinspace V$ nås efter tre fjärdedelar av ett varv.

Fasen $\delta$ är lika med 90°, vilket innebär att kurvan är $90°/360° = 1/4$, alltså en fjärdedel av ett varv "före" i x-axeln. Detta motsvarar $2{,}5\thinspace ms$, då

```math
\frac{T}{4} = \frac{10\text{m}}{4} = 2{,}5\,ms
```

Sinuskurvan har alltså periodtiden $T = 10\thinspace ms$, startar vid $u(0) = 5\sin(\pi/2) = 5\thinspace V$ (redan vid sitt maximivärde eftersom fasen är 90°), passerar noll vid $t = 2{,}5\thinspace ms$ och $t = 7{,}5\thinspace ms$, och når sitt minimivärde $-5\thinspace V$ vid $t = 5\thinspace ms$.

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

### Lösning
**a)** Vi deriverar term för term:

```math
P'(I) = 24 - 12I
```

**b)** Vi löser $P'(I) = 0$:

```math
24 - 12I = 0 \quad \Rightarrow \quad 12I = 24 \quad \Rightarrow \quad I = \frac{24}{12} = 2\,A
```

**c)** Vi beräknar andraderivatan, alltså derivatan av $P'(I)$:

```math
P''(I) = -12
```

Eftersom andraderivatan är negativ för alla $I$, även för $I = 2\thinspace A$, är punkten en maximipunkt:

```math
P''(2) = -12 < 0 \quad \Rightarrow \quad \text{maximipunkt}
```

**d)** Vi beräknar maxeffekten genom att sätta $I = 2$ i funktionen:

```math
P(2) = 24 \cdot 2 - 6 \cdot 2^2 = 48 - 24 = 24\,W
```

Lasten kan alltså som mest få effekten $24\thinspace W$ från batteriet.

**e)** Nollställena ges av $P(I) = 6I(4 - I) = 0$, alltså $I = 0$ och $I = 4\thinspace A$. Dessutom är $P(1) = 18\thinspace W$ och $P(3) = 18\thinspace W$. Grafen är en nedåtöppnande parabel med maximipunkten $(2; 24)$, som skär $I$-axeln i $(0; 0)$ och $(4; 0)$. Vid $I = 4\thinspace A$ är batteriet kortslutet: klämspänningen är noll, så ingen effekt utvecklas i lasten.

Grafen visar också varför uppgift 2 har två lösningar: effekten $18\thinspace W$ är mindre än maxeffekten $24\thinspace W$ och nås vid två strömmar, $I = 1\thinspace A$ och $I = 3\thinspace A$.

**f)** I den stationära punkten är klämspänningen

```math
U = 24 - 6 \cdot 2 = 12\,V
```

och lastresistansen

```math
R = \frac{U}{I} = \frac{12}{2} = 6\,\Omega
```

Lastresistansen är alltså lika med den inre resistansen $R_i = 6\thinspace\Omega$. Lasten får störst effekt när $R = R_i$, vilket kallas effektanpassning.

**Svar:** Maxeffekten är $P(2) = 24\thinspace W$ och nås vid $I = 2\thinspace A$, alltså när $R = R_i = 6\thinspace\Omega$.

---

### Uppgift 7 (1,5 poäng)
Laddningen $q(t)$ som passerar genom en ledare inom ett tidsintervall $(0, t)$ kan beräknas via följande funktion:

```math
q(t) = \int_0^t i(t)\,dt = \big[I(t)\big]_0^t,
```

där $I(t)$ är den primitiva funktionen (obestämda integralen) av $i(t)$. Strömmen $i(t)$ i en kondensator ges av:

```math
i(t) = 0{,}03t^2 + 0{,}1t + 0{,}5
```

där $t$ är tiden i sekunder. Kondensatorn har redan laddningen $q_0 = 1\thinspace C$ vid start.

**a)** Bestäm ett uttryck för den primitiva funktionen $I(t) = \int i(t)\thinspace dt$.

**b)** Bestäm ett uttryck för kondensatorns laddning $q(t)$ genom att integrera över intervallet $[0, t]$.

**c)** Bestäm en formel för den totala laddningen $q_{tot}(t)$ i kondensatorn, inklusive startladdningen $q_0$.

**d)** Hur stor total laddning (inklusive startladdningen) har flödat in i kondensatorn efter 4 sekunder?

---

### Lösning
**a)** Vi bestämmer den primitiva funktionen $I(t)$ genom att integrera $i(t)$ term för term, utan att ange några gränser. Exponenten ökar med ett för varje term, och termen delas med den nya exponenten:

```math
I(t) = \int \left(0{,}03t^2 + 0{,}1t + 0{,}5\right)dt = 0{,}03 \cdot \frac{t^3}{3} + 0{,}1 \cdot \frac{t^2}{2} + 0{,}5t + C,
```

vilket kan skrivas om till

```math
I(t) = 0{,}01t^3 + 0{,}05t^2 + 0{,}5t + C
```

**Kontroll:** Derivering av $I(t)$ ger $0{,}03t^2 + 0{,}1t + 0{,}5 = i(t)$.

**b)** Vi integrerar strömmen $i(t)$ för intervallet $(0, t)$:

```math
q(t) = \int_0^t i(t)\,dt = \big[I(t)\big]_0^t = \big[0{,}01t^3 + 0{,}05t^2 + 0{,}5t + C\big]_0^t
```

Vi utvecklar $q(t)$. Alla termer i den undre gränsen blir noll när $t = 0$, så bara $C$ finns kvar där:

```math
q(t) = \left(0{,}01t^3 + 0{,}05t^2 + 0{,}5t + C\right) - \left(0 + 0 + 0 + C\right) = 0{,}01t^3 + 0{,}05t^2 + 0{,}5t
```

**c)** För att bestämma en formel för laddningen $q_{tot}(t)$ måste vi ta reda på integrationskonstanten $C$. Vi tolkar konstanten som $C$ i den primitiva funktionen $I(t)$, där $q_{tot}(t) = I(t) = 0{,}01t^3 + 0{,}05t^2 + 0{,}5t + C$, och bestämmer $q_{tot}(0) = I(0)$:

```math
q_{tot}(0) = I(0) = 0{,}01 \cdot 0^3 + 0{,}05 \cdot 0^2 + 0{,}5 \cdot 0 + C = C
```

Enligt uppgiften är startladdningen $q_{tot}(0) = q_0 = 1\thinspace C$. Därmed är integrationskonstanten $C = 1$, och den totala laddningen $q_{tot}(t)$ efter en viss tid $t$ kan beräknas med följande formel:

```math
q_{tot}(t) = 0{,}01t^3 + 0{,}05t^2 + 0{,}5t + 1
```

Samma resultat fås om startladdningen $q_0 = 1\thinspace C$ läggs till laddningen $q(t)$ från b), som räknas från noll:

```math
q_{tot}(t) = q(t) + q_0 = 0{,}01t^3 + 0{,}05t^2 + 0{,}5t + 1
```

**d)** Den totala laddningen efter 4 sekunder beräknas genom att beräkna $q_{tot}(4)$:

```math
q_{tot}(4) = 0{,}01 \cdot 4^3 + 0{,}05 \cdot 4^2 + 0{,}5 \cdot 4 + 1 = 0{,}64 + 0{,}8 + 2 + 1 = 4{,}44\,C
```

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

### Lösning
**a)** För att beräkna strömmen $I$ måste spänningen $U$ samt impedansen $Z$ omvandlas till polär form.

Vi börjar med att omvandla spänningen $U$, vars absolutbelopp $|U|$ beräknas via Pythagoras sats:

```math
|U| = \sqrt{3^2 + (-4)^2} = \sqrt{9 + 16} = \sqrt{25} = 5\,V
```

Vi beräknar sedan spänningens fasvinkel $\delta_u$ med $\tan^{-1}$:

```math
\delta_u = \tan^{-1}\left(\frac{-4}{3}\right) \pm k\pi \approx -0{,}9 \pm k\pi\,\text{rad} \approx -53{,}1° \pm k \cdot 180°
```

Eftersom $U$ ligger i fjärde kvadranten ($270° \leq \delta_u \leq 360°$) samt att $-53{,}1° = 360° - 53{,}1° = 306{,}9°$ är den beräknade fasvinkeln $\delta_u$ korrekt. Därmed gäller att

```math
U = 3 - j4 \approx 5\,\angle\,{-0{,}9}\,\text{rad}\,V
```

Vi omvandlar sedan impedansen $Z$, vars absolutbelopp $|Z|$ beräknas via Pythagoras sats:

```math
|Z| = \sqrt{2^2 + 2^2} = \sqrt{8} \approx 2{,}8\,\Omega
```

Vi beräknar sedan impedansens fasvinkel $\delta_z$ med $\tan^{-1}$:

```math
\delta_z = \tan^{-1}\left(\frac{2}{2}\right) \pm k\pi \approx 0{,}8 \pm k\pi\,\text{rad} = 45° \pm k \cdot 180°
```

Eftersom $Z$ ligger i första kvadranten ($0° \leq \delta_z \leq 90°$) är den beräknade fasvinkeln $\delta_z$ korrekt. Därmed gäller att

```math
Z = 2 + j2 \approx 2{,}8\,\angle\,0{,}8\,\text{rad}\,\Omega
```

Vi beräknar sedan strömmen $I$ på polär form:

```math
I = \frac{U}{Z} \approx \frac{5\,\angle\,{-0{,}9}}{2{,}8\,\angle\,0{,}8} = \frac{5}{2{,}8}\,\angle\,(-0{,}9 - 0{,}8) \approx 1{,}8\,\angle\,{-1{,}7}\,\text{rad}\,A
```

Strömmen kan därmed uttryckas på polär form enligt nedan:

```math
I \approx 1{,}8\,\angle\,{-1{,}7}\,\text{rad}\,A,
```

där strömmens absolutbelopp $|I| = 1{,}8\thinspace A$ och strömmens fasvinkel $\delta_i \approx -1{,}7\thinspace\text{rad} \approx -98{,}1°$.

Vi omvandlar sedan strömmen till rektangulär form, $I = I_{re} + jI_{im}$. Vi beräknar först den reella delen $I_{re}$ med cosinus:

```math
I_{re} = |I| \cdot \cos\delta_i \approx 1{,}8 \cdot \cos(-1{,}7) \approx -0{,}25\,A
```

Vi beräknar sedan den imaginära delen $I_{im}$ med sinus:

```math
I_{im} = |I| \cdot \sin\delta_i \approx 1{,}8 \cdot \sin(-1{,}7) \approx -1{,}75\,A
```

**Svar:**

```math
I = -0{,}25 - j1{,}75\,A \approx 1{,}8\,\angle\,{-1{,}7}\,\text{rad}\,A
```

**b)** Med $Z = 2 + j2$ är resistansen $R = 2\thinspace\Omega$ och reaktansen $X = 2\thinspace\Omega$. Reaktansen är positiv, så kretsen är **induktiv**.

**c)** För en spole gäller $X_L = \omega L$, där vinkelhastigheten är

```math
\omega = 2\pi f = 2\pi \cdot 50 = 100\pi\,\text{rad/s}
```

Vi löser ut induktansen:

```math
L = \frac{X_L}{\omega} = \frac{2}{100\pi} = \frac{1}{50\pi} \approx 6{,}37 \cdot 10^{-3}\,H = 6{,}37\,mH
```

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

### Lösning
**a)** Fasorn $I = 10 - j5\thinspace mA$ ligger i fjärde kvadranten i det komplexa talplanet (positiv reell del, negativ imaginär del).

**b)** Vi bestämmer först strömmens absolutbelopp $|I|$ med Pythagoras sats:

```math
|I| = \sqrt{10^2 + (-5)^2} = \sqrt{100 + 25} = \sqrt{125} \approx 11{,}2\,mA
```

Vi bestämmer sedan fasvinkeln $\delta$ med $\tan^{-1}$:

```math
\delta = \tan^{-1}\left(\frac{-5}{10}\right) \pm k\pi \approx -0{,}46 \pm k\pi\,\text{rad} \approx -26{,}6° \pm k \cdot 180°
```

Eftersom $I$ ligger i fjärde kvadranten ($270° \leq \delta \leq 360°$) samt att $-26{,}6° = 360° - 26{,}6° = 333{,}4°$ är den beräknade fasvinkeln $\delta$ korrekt. Vi kan därefter uttrycka fasorn $I$ med Eulers form:

```math
I \approx 11{,}2 e^{-j0{,}46}\,mA
```

**c)** Vinkelhastigheten $w$ beräknas med hjälp av frekvensen $f = 10\thinspace Hz$:

```math
w = 2\pi f = 2\pi \cdot 10 = 20\pi\,\text{rad/s}
```

**d)** Vi sätter in tidskomponenten $wt$, där $w = 20\pi\thinspace\text{rad/s}$, i uttrycket för fasorn $I$ och erhåller då följande:

```math
i(t) \approx 11{,}2 e^{j(20\pi t - 0{,}46)}\,mA
```

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

**d)** Omvandla tillbaka resultatet till en sinusformad spänning i tidsdomänen på formen $u_{tot}(t) = |U_{tot}| \sin(wt + \delta_{tot})$.

---

### Lösning
**a)** Vi omvandlar sinusspänningarna till motsvarande fasorer en efter en:

```math
U_1 = 2\cos(25°) + j2\sin(25°) \approx 1{,}81 + j0{,}85\,V
```

```math
U_2 = 5\cos(-45°) + j5\sin(-45°) \approx 3{,}54 - j3{,}54\,V
```

```math
U_3 = 1{,}5\cos(36°) + j1{,}5\sin(36°) \approx 1{,}21 + j0{,}88\,V
```

**b)** Vi beräknar fasorsumman $U_{tot}$ genom att addera de beräknade fasorerna:

```math
U_{tot} \approx (1{,}81 + j0{,}85) + (3{,}54 - j3{,}54) + (1{,}21 + j0{,}88),
```

vilket kan skrivas om till

```math
U_{tot} \approx 6{,}56 - j1{,}81\,V
```

**c)** Fasorerna $U_1$, $U_2$, $U_3$ samt summan $U_{tot}$ ritas ut i det komplexa talplanet: $U_1$ och $U_3$ ligger i första kvadranten, $U_2$ i fjärde kvadranten, och resultanten $U_{tot}$ ligger i fjärde kvadranten strax under den reella axeln.

**d)** Vi omvandlar fasorsumman $U_{tot}$ till motsvarande sinusformad spänning i tidsdomänen:

```math
u_{tot}(t) = |U_{tot}| \sin(wt + \delta_{tot}),
```

där

```math
|U_{tot}| \approx \sqrt{6{,}56^2 + (-1{,}81)^2} \approx 6{,}81\,V
```

samt

```math
\delta_{tot} = \tan^{-1}\left(\frac{-1{,}81}{6{,}56}\right) \pm k\pi \approx -0{,}27 \pm k\pi\,\text{rad} \approx -15{,}4° \pm k \cdot 180°
```

Eftersom $U_{tot}$ ligger i fjärde kvadranten ($270° \leq \delta_{tot} \leq 360°$) samt att $-15{,}4° = 360° - 15{,}4° = 344{,}6°$ är den beräknade fasvinkeln $\delta_{tot}$ korrekt.

**Svar:**

```math
u_{tot}(t) \approx 6{,}81 \sin(wt - 15{,}4°)\,V
```

> **Notering om källan:** Originallösningen angav $-14{,}9°$, men en fullprecisionsberäkning av $\tan^{-1}(1{,}8086/6{,}5617)$ ger $\approx 15{,}41°$. Det är ett litet (ca 0,5°) avrundnings-/räknefel i originalet som här har korrigerats till $-15{,}4°$.

---
