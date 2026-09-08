# L04 – Lektionsuppgifter

## Del 1 – Repetitionsuppgifter
### 1.1 – Ohms lag – sök spänning
En krets har $R = 47\thinspace\Omega$ och $I = 200\thinspace\text{mA} = 0{,}2\thinspace\text{A}$.

**a)** Beräkna spänningen $U$.

**b)** Effekten i motståndet ges av $P = U \cdot I$. Beräkna effekten.

---

### 1.2 – Linjär ekvation i RC-krets
Laddningstiden $\tau$ i en RC-krets ges av $\tau = R \cdot C$.

Tidskonstanten $\tau = 20\thinspace\text{ms}$ och $C = 10\thinspace\mu\text{F}$.

**a)** Sätt upp ekvationen och lös för $R$.

**b)** Ange $R$ i $\text{k}\Omega$.

---

### 1.3 – Olikhet
En förstärkare levererar en utspänning $U_{\text{ut}} = 5 \cdot U_{\text{in}}$. Utspänningen får inte överstiga $15\thinspace\text{V}$.

Sätt upp och lös en olikhet för $U_{\text{in}}$.

---

## Del 2 – Nytt stoff
### 2.1 – Algebraiskt ekvationssystem
Lös följande ekvationssystem:

```math
\begin{cases}
3x + y = 11 \\
x - 2y = -2
\end{cases}
```

---

### 2.2 – Strömsystem med Kirchhoffs strömlag
I en nod gäller KCL: summan av inströmmar är lika med summan av utströmmar.

En nod har inströmmarna $I_1$ och $I_2$ samt utströmmen $I_3 = 5\thinspace\text{A}$.

Dessutom vet vi att $I_1 = 2 I_2$.

**a)** Sätt upp ett ekvationssystem för $I_1$ och $I_2$.

**b)** Lös systemet och ange strömmarnas värden.

---

### 2.3 – Spänning och ström via KVL
En krets med en spänningskälla $E = 12\thinspace\text{V}$ och två motstånd $R_1$ och $R_2$ i serie.

KVL ger: $E = U_1 + U_2$ (dvs. $U_1 + U_2 = 12$).

Därtill gäller att spänningsfallet över $R_2$ är tre gånger så stort som över $R_1$: $U_2 = 3 U_1$.

**a)** Sätt upp ekvationssystemet.

**b)** Lös systemet och beräkna $U_1$ och $U_2$.

**c)** Om strömmen $I = 2\thinspace\text{A}$, beräkna $R_1$ och $R_2$ via Ohms lag.

---

## Del 3 – Extrauppgifter
Uppgifterna nedan är extra träning och görs med fördel på egen hand efter lektionen. De flesta går att räkna i huvudet eller med papper och penna.

### 3.1 – Substitutionsmetoden
Lös systemen med substitutionsmetoden:

**a)**

```math
\begin{cases}
y = 2x + 1 \\
3x + y = 11
\end{cases}
```

**b)**

```math
\begin{cases}
x = 3y \\
x + 2y = 15
\end{cases}
```

**c)**

```math
\begin{cases}
x + y = 10 \\
x - y = 4
\end{cases}
```

---

### 3.2 – Additionsmetoden
Lös systemen med additionsmetoden:

**a)**

```math
\begin{cases}
2x + y = 7 \\
x - y = 2
\end{cases}
```

**b)**

```math
\begin{cases}
3x + 2y = 16 \\
x - 2y = 0
\end{cases}
```

**c)**

```math
\begin{cases}
5x + 3y = 21 \\
2x - y = 4
\end{cases}
```

**d)**

```math
\begin{cases}
3x + 4y = 10 \\
2x - 3y = 1
\end{cases}
```

---

### 3.3 – Antal lösningar
Avgör om systemet har exakt en lösning, ingen lösning eller oändligt många. Motivera med hur linjerna ligger.

**a)**

```math
\begin{cases}
x + y = 4 \\
2x + 2y = 8
\end{cases}
```

**b)**

```math
\begin{cases}
x + y = 4 \\
x + y = 6
\end{cases}
```

**c)**

```math
\begin{cases}
x + y = 4 \\
x - y = 0
\end{cases}
```

**d)**

```math
\begin{cases}
2x - 4y = 6 \\
-x + 2y = -3
\end{cases}
```

---

### 3.4 – Grafisk tolkning
Betrakta systemet:

```math
\begin{cases}
y = 2x - 1 \\
y = -x + 5
\end{cases}
```

**a)** Gör en värdetabell för båda linjerna med $x = 0, 1, 2, 3, 4$.

**b)** Vid vilket $x$ ger de båda uttrycken samma $y$? Avläs skärningspunkten ur tabellen.

**c)** Lös systemet algebraiskt och kontrollera avläsningen.

**d)** Hur skulle tabellen se ut om systemet saknade lösning?

---

### 3.5 – System med bråk och decimaltal
Lös systemen:

**a)**

```math
\begin{cases}
0{,}5x + y = 4 \\
x - y = 2
\end{cases}
```

**b)**

```math
\begin{cases}
\frac{x}{2} + \frac{y}{3} = 4 \\
x - y = 3
\end{cases}
```

> **Tips:** Multiplicera bort nämnarna innan du väljer metod.

---

### 3.6 – KCL i en nod
I en nod flyter strömmarna $I_1$ och $I_2$ in, medan $I_3 = 12\thinspace\text{A}$ flyter ut. Mätning visar dessutom att $I_1$ är $4\thinspace\text{A}$ större än $I_2$.

**a)** Sätt upp ett ekvationssystem för $I_1$ och $I_2$.

**b)** Lös systemet.

**c)** Kontrollera lösningen i båda ekvationerna.

---

### 3.7 – Strömdelning i en parallellkoppling
Två motstånd $R_1$ och $R_2$ är parallellkopplade över spänningen $U = 24\thinspace\text{V}$. Den totala strömmen är $I = 3\thinspace\text{A}$, och grenströmmen genom $R_1$ är dubbelt så stor som den genom $R_2$.

**a)** Sätt upp ett ekvationssystem för grenströmmarna $I_1$ och $I_2$.

**b)** Lös systemet.

**c)** Beräkna $R_1$ och $R_2$ med Ohms lag.

**d)** Kontrollera att parallellresistansen $R_1 // R_2$ stämmer med $\dfrac{U}{I}$.

---

### 3.8 – KVL i en seriekrets
En seriekrets med två motstånd matas med $E = 15\thinspace\text{V}$. Spänningsfallen uppfyller KVL, och $U_1$ är $3\thinspace\text{V}$ större än $U_2$.

**a)** Sätt upp ekvationssystemet.

**b)** Lös systemet.

**c)** Strömmen är $I = 0{,}3\thinspace\text{A}$. Beräkna $R_1$ och $R_2$.

**d)** Kontrollera att $R_1 + R_2 = \dfrac{E}{I}$.

---

### 3.9 – Arbetspunkt: källa och last
En spänningskälla med inre resistans ger klämspänningen $U = 12 - 2I$, där $I$ är strömmen i ampere. Källan belastas med ett motstånd på $4\thinspace\Omega$, vilket enligt Ohms lag ger $U = 4I$.

**a)** Sätt upp ekvationssystemet för $U$ och $I$.

**b)** Lös systemet.

**c)** Kontrollera lösningen i båda ekvationerna.

**d)** Vad kallas den punkt där källans och lastens karaktäristik skär varandra?

---

### 3.10 – Dimensionera en spänningsdelare
Två motstånd är seriekopplade och den totala resistansen är $R_1 + R_2 = 900\thinspace\Omega$. När serien matas med $U = 9\thinspace\text{V}$ blir spänningen över $R_1$ lika med $6\thinspace\text{V}$.

**a)** Använd spänningsdelningen $\dfrac{U_1}{U} = \dfrac{R_1}{R_1 + R_2}$ för att få en andra ekvation.

**b)** Lös systemet och ange $R_1$ och $R_2$.

**c)** Kontrollera svaret med spänningsdelarformeln.

---

### 3.11 – System med tre obekanta
I en krets gäller följande samband mellan tre grenströmmar (i ampere):

```math
\begin{cases}
I_1 + I_2 + I_3 = 9 \\
I_1 - I_2 = 1 \\
I_3 = 4
\end{cases}
```

**a)** Lös systemet.

**b)** Kontrollera lösningen i alla tre ekvationerna.

**c)** Varför är den tredje ekvationen särskilt bekväm att börja med?

---

### 3.12 – Ställ upp systemet ur en text
Ett kretskort byggs med två resistortyper, A och B. Fem resistorer av typ A tillsammans med tre av typ B ger seriekopplat $4\thinspace 390\thinspace\Omega$. Två av typ A tillsammans med fyra av typ B ger $3\thinspace 660\thinspace\Omega$.

**a)** Inför beteckningarna $R_A$ och $R_B$ och sätt upp ekvationssystemet.

**b)** Lös systemet.

**c)** Kontrollera svaret i båda ekvationerna.

---

### 3.13 – Kontrollera en föreslagen lösning
Avgör **utan** att lösa systemet om det angivna talparet är en lösning:

**a)** $(x, y) = (2, 3)$ till $x + y = 5$ och $2x - y = 1$.

**b)** $(x, y) = (1, 4)$ till $3x + y = 7$ och $x - y = -3$.

**c)** $(x, y) = (5, 1)$ till $x - 2y = 3$ och $x + y = 7$.

**d)** Varför räcker det inte att kontrollera i bara en av ekvationerna?

---

### 3.14 – Blandade system
Lös med den metod du tycker passar bäst:

**a)**

```math
\begin{cases}
4x - y = 5 \\
2x + 3y = 13
\end{cases}
```

**b)**

```math
\begin{cases}
x + 3y = 1 \\
2x - y = 9
\end{cases}
```

**c)**

```math
\begin{cases}
6x + 2y = 10 \\
3x - y = 7
\end{cases}
```

**d)** Motivera kort varför du valde respektive metod.

---
