# L17 - Lektionsuppgifter

## Del 1 - Repetitionsuppgifter

### 1.1 - Vektorer i det komplexa talplanet

Du har följande vektorer: $a = (2;1)$, $b = (2;-1)$ samt $c = (-3; 4)$. \
I uppgifterna nedan ska varje vektor $(x;y)$ tolkas som ett komplext tal $z = x + jy$.

**a)** Skriv vektorerna på komplex rektangulär form.

**b)** Rita ut vektorerna i det komplexa talplanet (x-axeln = reell del, y-axeln = imaginär del).

**c)** Bestäm vektorernas längder, dvs. absolutbeloppet av respektive tal.

**d)** Bestäm längden (absolutbeloppet) av $a + b + c$, dvs. $|a + b + c|$.

**e)** Bestäm vektorernas vinklar.

**f)** Bestäm en vektor $d$ med längden $8$ som är motsatt riktad $c$.

---

### 1.2 - Rektangulär form => Eulers form

En spänning $u(t)$ i en växelströmskrets kan representeras av en fasor U, som på rektangulär form skrivs enligt nedan:

```math
U = 3 - j6\,\,V
```

**a)** Rita ut fasorn $U$ i det komplexa talplanet (x-axeln = reell del, y-axeln = imaginär del).

**b)** Uttryck fasorn $U$ på Eulers form, dvs. bestäm absolutbeloppet $|U|$ samt fasvinkeln $δ$ så att $U = |U|e^{jδ}$.

**c)** Anta att spänningens frekvens $f = 50$ $Hz$. Bestäm vinkelhastigheten $w$.

**d)** Skriv $u(t)$ som en tidsberoende funktion $u(t)=|U|*e^{j(wt+δ)}$.

---

## Del 2 - Nytt stoff

### 2.1 - Addition av tre strömmar i AC-krets

En nod i en elektrisk krets matas med tre sinusformade strömmar: 

```math
i_1(t) = 5{\sin (\omega t + 30^{\circ})}\,\,mA
```

```math
i_2(t) = 3{\sin (\omega t - 30^{\circ})}\,\,mA
```

```math
i_3(t) = 4{\sin (\omega t + 120^{\circ})}\,\,mA
```

Den totala strömmen i kretsen $I_{tot}$ beräknas enligt nedan:

```math
I_{tot}(t) = i_1(t) + i_2(t) + i_3(t)
```

**a)** Skriv om strömmarna $i_1(t)$, $i_2(t)$ samt $i_3(t)$ till fasor $I_1$, $I_2$ samt $I_3$ i komplex rektangulär form.

**b)** Beräkna fasorsumman $I_{tot} = I_1 + I_2 + I_3$.

**c)** Rita ut fasorerna i det komplexa talplanet (x-axeln = reell del, y-axeln = imaginär del).

**d)** Omvandla tillbaka resultatet till en sinusformad ström i tidsdomänen på följande form:

```math
i_{tot}(t) = |I_{tot}|{\sin}(\omega t + δ)
```

---
## Del 3 – Extrauppgifter
Uppgifterna nedan är extra träning och görs med fördel på egen hand efter lektionen. De flesta går att räkna i huvudet eller med papper och penna.

### 3.1 – Fasor ur sinussignal
Ange fasorn på polär form:

**a)** $u(t) = 12\sin(\omega t + 60°)$

**b)** $u(t) = 5\sin(\omega t - 45°)$

**c)** $i(t) = 2\sin(\omega t)$

**d)** $i(t) = 7\sin(\omega t + 180°)$

---

### 3.2 – Fasor på rektangulär form
Skriv fasorerna på rektangulär form:

**a)** $10\thinspace\angle\thinspace 0°$

**b)** $4\thinspace\angle\thinspace 90°$

**c)** $6\thinspace\angle\thinspace 30°$

**d)** $5\thinspace\angle\thinspace -53{,}1°$

---

### 3.3 – Addition av två spänningar
Två spänningar med samma frekvens ges av $u_1(t) = 3\sin(\omega t)$ V och $u_2(t) = 4\sin(\omega t + 90°)$ V.

**a)** Ange fasorerna på polär form.

**b)** Skriv dem på rektangulär form.

**c)** Beräkna fasorsumman och ange den på polär form.

**d)** Skriv $u_{\text{tot}}(t)$.

---

### 3.4 – Addition av tre fasorer
Tre spänningar ges av $U_1 = 10\thinspace\angle\thinspace 0°$, $U_2 = 5\thinspace\angle\thinspace 90°$ och $U_3 = 5\thinspace\angle\thinspace -90°\thinspace\text{V}$.

**a)** Skriv samtliga på rektangulär form.

**b)** Beräkna summan.

**c)** Ange summan på polär form.

**d)** Förklara varför $U_2$ och $U_3$ tar ut varandra.

---

### 3.5 – Summa och differens av två fasorer
Två spänningar ges av $U_1 = 8\thinspace\angle\thinspace 30°\thinspace\text{V}$ och $U_2 = 8\thinspace\angle\thinspace -30°\thinspace\text{V}$.

**a)** Skriv båda på rektangulär form.

**b)** Beräkna $U_1 + U_2$ och ange svaret på polär form.

**c)** Beräkna $U_1 - U_2$ och ange svaret på polär form.

**d)** Kommentera resultaten.

---

### 3.6 – Multiplikation och division av fasorer
Beräkna:

**a)** $(5\thinspace\angle\thinspace 20°)(4\thinspace\angle\thinspace 40°)$

**b)** $\dfrac{20\thinspace\angle\thinspace 100°}{5\thinspace\angle\thinspace 40°}$

**c)** $(6\thinspace\angle\thinspace -30°)(2\thinspace\angle\thinspace -30°)$

**d)** $\dfrac{9\thinspace\angle\thinspace 0°}{3\thinspace\angle\thinspace 90°}$

---

### 3.7 – Impedans för R, L och C
Vid $\omega = 2000\thinspace\text{rad/s}$ gäller $R = 100\thinspace\Omega$, $L = 50\thinspace\text{mH}$ och $C = 5\thinspace\mu\text{F}$.

**a)** Ange $Z_R$ och dess fasvinkel.

**b)** Beräkna $Z_L = j\omega L$ och ange fasvinkeln.

**c)** Beräkna $Z_C = -\dfrac{j}{\omega C}$ och ange fasvinkeln.

**d)** Vad innebär fasvinklarna för strömmen genom respektive komponent?

---

### 3.8 – Serie-RL-krets
En seriekrets har $R = 40\thinspace\Omega$ och $X_L = 30\thinspace\Omega$.

**a)** Ange impedansen $Z$ på rektangulär form.

**b)** Beräkna $|Z|$ och fasvinkeln.

**c)** Kretsen matas med $U = 100\thinspace\angle\thinspace 0°\thinspace\text{V}$. Beräkna strömmen.

**d)** Ligger strömmen före eller efter spänningen?

---

### 3.9 – Serie-RC-krets
En seriekrets har $R = 60\thinspace\Omega$ och $X_C = 80\thinspace\Omega$.

**a)** Ange impedansen $Z$ på rektangulär form.

**b)** Beräkna $|Z|$ och fasvinkeln.

**c)** Kretsen matas med $U = 200\thinspace\angle\thinspace 0°\thinspace\text{V}$. Beräkna strömmen.

**d)** Ligger strömmen före eller efter spänningen?

---

### 3.10 – Serie-RLC-krets
En seriekrets har $R = 20\thinspace\Omega$, $X_L = 60\thinspace\Omega$ och $X_C = 45\thinspace\Omega$.

**a)** Ange impedansen $Z$ på rektangulär form.

**b)** Beräkna $|Z|$ och fasvinkeln.

**c)** Kretsen matas med $U = 50\thinspace\angle\thinspace 0°\thinspace\text{V}$. Beräkna strömmen.

**d)** Är kretsen induktiv eller kapacitiv?

---

### 3.11 – Resonans
En seriekrets har $R = 10\thinspace\Omega$, $L = 100\thinspace\text{mH}$ och $C = 10\thinspace\mu\text{F}$. Resonans inträffar vid $\omega_0 = \dfrac{1}{\sqrt{LC}}$.

**a)** Beräkna $\omega_0$.

**b)** Beräkna resonansfrekvensen $f_0$.

**c)** Beräkna $X_L$ och $X_C$ vid $\omega_0$.

**d)** Vilken impedans har kretsen vid resonans?

---

### 3.12 – Spänningsdelning i en AC-krets
En seriekrets med $Z_R = 30\thinspace\Omega$ och $Z_L = j40\thinspace\Omega$ matas med $U = 100\thinspace\angle\thinspace 0°\thinspace\text{V}$.

**a)** Beräkna $Z_{\text{tot}}$ och $|Z_{\text{tot}}|$.

**b)** Beräkna strömmen $I$.

**c)** Beräkna spänningen $U_R$ över motståndet.

**d)** Beräkna spänningen $U_L$ över spolen.

**e)** Visa att $U_R + U_L = U$ som fasorer, trots att $|U_R| + |U_L| \neq |U|$.

---

### 3.13 – Beräkna fasen ur en ekvation
En växelspänning ges av $u(t) = 10\sin(100\pi t + \delta)$ volt. Vid $t = 5\thinspace\text{ms}$ är $u = 5\thinspace\text{V}$.

**a)** Ställ upp ekvationen för $\delta$.

**b)** Lös ekvationen som två fall.

**c)** Kontrollera båda lösningarna.

---

### 3.14 – Parallellkopplade impedanser
Impedanserna $Z_1 = 10\thinspace\Omega$ och $Z_2 = j10\thinspace\Omega$ är parallellkopplade.

**a)** Beräkna $Z = \dfrac{Z_1Z_2}{Z_1 + Z_2}$ på rektangulär form.

**b)** Beräkna $|Z|$ och fasvinkeln.

**c)** Jämför med seriekopplingen av samma impedanser.

**d)** Vad är gemensamt för de två fasvinklarna?

---

### 3.15 – Från fasordomän till tidsdomän
En krets genomflyts av $i(t) = 4\sin(500t - 30°)$ A och har impedansen $Z = 25\thinspace\angle\thinspace 60°\thinspace\Omega$.

**a)** Ange strömmens fasor.

**b)** Beräkna spänningens fasor $U = ZI$.

**c)** Skriv $u(t)$.

**d)** Vilken fasskillnad har spänningen relativt strömmen?

---

### 3.16 – Två strömmar i en nod
En nod matas med $i_1(t) = 6\sin(\omega t + 45°)$ mA och $i_2(t) = 8\sin(\omega t - 45°)$ mA.

**a)** Ange fasorerna på polär form.

**b)** Skriv dem på rektangulär form.

**c)** Beräkna fasorsumman och ange den på polär form.

**d)** Skriv $i_{\text{tot}}(t)$.

---

### 3.17 – Sant eller falskt
Avgör om påståendet är sant eller falskt och motivera kortfattat:

**a)** Fasorer med olika vinkelhastighet får adderas.

**b)** En induktans har impedansen med fasvinkeln $+90°$.

**c)** $|Z| = R + X$

**d)** I en rent resistiv krets är ström och spänning i fas.

**e)** I en kapacitiv krets ligger strömmen efter spänningen.

**f)** Vid resonans är kretsens impedans rent resistiv.

---
