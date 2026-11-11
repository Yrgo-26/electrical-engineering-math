# L16 - Lektionsuppgifter

## Del 1 - Repetitionsuppgifter

### 1.1 – Ström i en RL-krets
En resistor $R = 100\thinspace\Omega$ och en spole $L = 1\thinspace mH$ är seriekopplade och matas med spänningen $U = 10\angle 0°\thinspace V$, med frekvensen $f = 50\thinspace kHz$. Spolens impedans ges av

```math
Z_L = j\omega L = j2\pi f L
```

**a)** Beräkna spolens impedans $Z_L$. Behåll $\pi$ i svaret och avrunda först på slutet.

**b)** Beräkna kretsens totala impedans $Z = R + Z_L$ på både rektangulär och polär form.

**c)** Beräkna strömmen $I = \frac{U}{Z}$ på både polär och rektangulär form.

---

### 1.2 – Ström i en RC-krets
Spolen i uppgift 1.1 byts mot en kondensator $C = 10\thinspace nF$. Spänningen $U = 10\angle 0°\thinspace V$, frekvensen $f = 50\thinspace kHz$ och resistorn $R = 100\thinspace\Omega$ är desamma. Kondensatorns impedans ges av

```math
Z_C = \frac{1}{j\omega C} = -\frac{j}{2\pi f C}
```

**a)** Beräkna kondensatorns impedans $Z_C$. Behåll $\pi$ i svaret och avrunda först på slutet.

**b)** Beräkna kretsens totala impedans $Z = R + Z_C$ på både rektangulär och polär form.

**c)** Beräkna strömmen $I = \frac{U}{Z}$ på både polär och rektangulär form.

**d)** Jämför strömmen med strömmen i uppgift 1.1. Vad är nästan lika, och vad skiljer sig?

---

## Del 2 - Nytt stoff

### 2.1 - Rektangulär form => Eulers form

En spänning $u(t)$  i en växelströmskrets kan representeras av en fasor U, som på rektangulär form skrivs enligt nedan:

```math
U = -12 + j4 V
```

**a)** Rita ut fasorn $U$ i det komplexa talplanet (x-axeln = reell del, y-axeln = imaginär del).

**b)** Uttryck fasorn $U$ på Eulers form, dvs. bestäm absolutbeloppet $|U|$ samt fasvinkeln $δ$ så att $U = |U|e^{jδ}$.

**c)** Anta att spänningens frekvens $f = 100$ $Hz$. Bestäm vinkelhastigheten $w$.

**d)** Skriv motsvarande komplexa tidsfunktion för spänningen på Eulers form, dvs $u(t)=|U|*e^{j(wt+δ)}$.

**e)** Rita spänningens sinuskurva $u(t) = |U|\sin(wt + δ)$ över en period $T$.

**Notering**: Fasorn $U$ utgör den komplexa spänningen $u(t)$ utan tidsberoendet.

---

### 2.2 - Eulers form => rektangulär form

En ström $i(t)$ i en växelströmskrets beskrivs av följande komplexa tidsfunktion på Eulers form:

```math
i(t) = 10e^{j(100\pi t - 3\pi/4)}\,mA
```

**a)** Ange strömmens absolutbelopp $|I|$, fasvinkel $\delta$ (i grader) samt vinkelhastighet $\omega$.

**b)** Bestäm strömmens frekvens $f$.

**c)** Skriv fasorn $I = |I|e^{j\delta}$ på rektangulär form.

**d)** Rita ut fasorn $I$ i det komplexa talplanet (x-axeln = reell del, y-axeln = imaginär del).

**e)** Rita strömmens sinuskurva $i(t) = |I|\sin(\omega t + \delta)$ över en period $T$.

---

## Del 3 – Extrauppgifter
Uppgifterna nedan är extra träning och görs med fördel på egen hand efter lektionen. De flesta går att räkna i huvudet eller med papper och penna.

### 3.1 – Eulers formel
Skriv på rektangulär form:

**a)** $e^{j\pi/6}$

**b)** $e^{j\pi/4}$

**c)** $e^{j2\pi/3}$

**d)** $e^{-j\pi/3}$

**e)** $e^{-j3\pi/4}$

---

### 3.2 – Eulerform till rektangulär form
Skriv på rektangulär form:

**a)** $z = 4e^{j\pi/6}$

**b)** $z = 5e^{j\pi/3}$

**c)** $z = 2e^{-j\pi/4}$

**d)** $z = 10e^{j2\pi/3}$

---

### 3.3 – Rektangulär form till Eulerform
Skriv på Eulerform $|z|e^{j\delta}$:

**a)** $z = 3 + j3$

**b)** $z = -2 + j2$

**c)** $z = 1 - j\sqrt{3}$

**d)** $z = -4 - j3$

---

### 3.4 – Multiplikation och division i polär form
Med $z_1 = 4\thinspace\angle\thinspace 30°$ och $z_2 = 3\thinspace\angle\thinspace 45°$, beräkna:

**a)** $z_1z_2$

**b)** $\dfrac{z_1}{z_2}$

**c)** $z_1^2$

**d)** Varför är polär form bekvämare än rektangulär vid multiplikation?

---

### 3.5 – Jämför metoderna
De komplexa talen $z_1 = 3 + j4$ och $z_2 = 1 + j$ är givna.

**a)** Beräkna $z_1z_2$ på rektangulär form.

**b)** Skriv båda talen på polär form.

**c)** Multiplicera talen i polär form.

**d)** Kontrollera att svaren i **a)** och **c)** är samma tal.

---

### 3.6 – Division i polär form
Beräkna:

**a)** $\dfrac{10\thinspace\angle\thinspace 80°}{2\thinspace\angle\thinspace 20°}$

**b)** $\dfrac{12\thinspace\angle\thinspace 0°}{4\thinspace\angle\thinspace 90°}$

**c)** $\dfrac{6\thinspace\angle\thinspace -30°}{3\thinspace\angle\thinspace 60°}$

**d)** Vad händer med fasvinkeln vid division med $j$?

---

### 3.7 – Potenser av komplexa tal
Talet $z = 2\thinspace\angle\thinspace 30°$ är givet.

**a)** Beräkna $z^2$.

**b)** Beräkna $z^3$ och skriv svaret även på rektangulär form.

**c)** Beräkna $z^4$.

**d)** Formulera den allmänna regeln för $z^n$ på polär form.

---

### 3.8 – Fasor ur tidsfunktion
Ange fasorn på polär form:

**a)** $u(t) = 10\sin\left(100\pi t + \dfrac{\pi}{6}\right)$

**b)** $u(t) = 4\sin\left(200\pi t - \dfrac{\pi}{2}\right)$

**c)** $i(t) = 6\sin(50t)$

**d)** Vad krävs för att två fasorer ska få adderas?

---

### 3.9 – Tidsfunktion ur fasor
Vinkelhastigheten är $\omega = 100\pi\thinspace\text{rad/s}$. Skriv motsvarande tidsfunktion:

**a)** $U = 8\thinspace\angle\thinspace 45°\thinspace\text{V}$

**b)** $U = 5\thinspace\angle\thinspace -90°\thinspace\text{V}$

**c)** $I = 3 + j4\thinspace\text{mA}$

**d)** $I = -2 - j2\thinspace\text{mA}$

---

### 3.10 – Fasoraddition
Två spänningar med samma frekvens ges av $U_1 = 6\thinspace\angle\thinspace 0°\thinspace\text{V}$ och $U_2 = 8\thinspace\angle\thinspace 90°\thinspace\text{V}$.

**a)** Skriv båda på rektangulär form.

**b)** Beräkna summan $U = U_1 + U_2$.

**c)** Ange summan på polär form.

**d)** Skriv $u(t)$ om $\omega = 100\pi\thinspace\text{rad/s}$.

---

### 3.11 – Impedans ur spänning och ström
En krets har $U = 20\thinspace\angle\thinspace 60°\thinspace\text{V}$ och $I = 4\thinspace\angle\thinspace 15°\thinspace\text{A}$.

**a)** Beräkna impedansen $Z = \dfrac{U}{I}$ på polär form.

**b)** Skriv $Z$ på rektangulär form.

**c)** Är kretsen induktiv eller kapacitiv?

**d)** Hur stor är resistansen respektive reaktansen?

---

### 3.12 – Impedans för spole och kondensator
Vid $\omega = 1000\thinspace\text{rad/s}$ gäller $L = 20\thinspace\text{mH}$ och $C = 50\thinspace\mu\text{F}$.

**a)** Beräkna $Z_L = j\omega L$.

**b)** Beräkna $Z_C = -\dfrac{j}{\omega C}$.

**c)** Ett motstånd $R = 15\thinspace\Omega$ seriekopplas med båda. Beräkna den totala impedansen.

**d)** Vad kallas detta tillstånd?

---

### 3.13 – Rotation med $j$
Talet $z = 3 + j4$ är givet.

**a)** Beräkna $jz$.

**b)** Jämför $|z|$ och $|jz|$.

**c)** Jämför de båda talens fasvinklar.

**d)** Vad gör multiplikation med $j$ geometriskt?

---

### 3.14 – Sant eller falskt
Avgör om påståendet är sant eller falskt och motivera kortfattat:

**a)** Två komplexa tal med samma absolutbelopp är alltid lika.

**b)** $|z_1z_2| = |z_1| + |z_2|$

**c)** Vid division subtraheras fasvinklarna.

**d)** En fasor innehåller information om signalens frekvens.

**e)** Fasvinkeln för $z = a + jb$ är alltid $\tan^{-1}\frac{b}{a}$.

**f)** Multiplikation av komplexa tal är enklast på rektangulär form.

---

## Del 4 – Matematik i C
Läraren visar uppgiften nedan under lektionen om tiden räcker, i VS Code och med `make`. Du kan också göra den själv i **OnlineGDB**, <https://www.onlinegdb.com/online_c_compiler>, med språket inställt på **C**. Strukten `complex_t` och funktionerna från L15, uppgift 4.1, används även här.

### 4.1 – Rotation med $j$ i C
Uppgiften bygger vidare på uppgift 3.13. Talet $z = 3 + j4$ är givet.

**a)** Beräkna $jz$, $j^2 z$, $j^3 z$ och $j^4 z$ för hand.

**b)** Visa att $j(a + jb) = -b + ja$. Skriv sedan funktionen `complex_t complex_rotate_j(const complex_t* z)`, som returnerar $jz$. Multiplicera $z$ med $j$ fyra gånger i en loop, med `z = complex_rotate_j(&z);`. Skriv ut talet på rektangulär form och dess argument i grader före den första multiplikationen och efter varje multiplikation.

**c)** Hur mycket ändras argumentet vid varje multiplikation? Varför blir $j^4 z = z$?

**d)** Ändra anropet till `complex_rotate_j(&z);`, utan `z =`. Vad skrivs ut nu? Förklara varför, utifrån att parametern är `const complex_t*`.

---
