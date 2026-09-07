# L02 – Lektionsuppgifter

## Del 1 – Repetitionsuppgifter
### 1.1 – Parallellkoppling av tre motstånd
Tre motstånd $R_1 = 6\thinspace\Omega$, $R_2 = 3\thinspace\Omega$ och $R_3 = 2\thinspace\Omega$ är parallellkopplade. Den totala resistansen ges av:

```math
\frac{1}{R_{\text{TOT}}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}
```

Beräkna $R_{\text{TOT}}$.

---

### 1.2 – Verkningsgrad och effekt
En transformator med verkningsgraden $\eta = 92\thinspace\char37$ tar in $P_{\text{in}} = 500\thinspace\text{W}$.

**a)** Beräkna uteffekten $P_{\text{ut}}$.\
**b)** Hur stor effekt $P_{\text{förl}}$ förloras som värme?

---

### 1.3 – Räkneordning i kretsformel
Beräkna spänningsdelaren $U_{\text{ut}}$ för nedanstående formel då $U_{\text{in}} = 12\thinspace\text{V}$, $R_1 = 8\thinspace\Omega$ och $R_2 = 4\thinspace\Omega$:

```math
U_{\text{ut}} = U_{\text{in}} \times \frac{R_2}{R_1 + R_2}
```

---

## Del 2 – Nytt stoff
### 2.1 – Förenkling av algebraiska uttryck
Förenkla följande uttryck:

**a)** $5I_1 + 3I_2 - 2I_1 + 7I_2$

**b)** $4R_1 - 3R_2 + R_1 + 5R_2 - 2R_1$

**c)** $3I^2 - 2I + 4I^2 + 5I - 1$

**d)** Sätt in $I = 2$ i både det ursprungliga och det förenklade uttrycket i **c)** och kontrollera att de ger samma värde.

---

### 2.2 – Distributivlagen i kretsar
Motståndet $R$ i kretsen nedan genomflyts av summan av de tre grenströmmarna $I_1$, $I_2$ och $I_3$.

![](./images/2.2_circuit.png)

Spänningsfallet över $R$ ges därmed av:

```math
U_R = R(I_1 + I_2 + I_3)
```

**a)** Multiplicera ut parentesen och ange varje term med enhet.\
**b)** Beräkna $U_R$ med den ursprungliga formen då $R = 100\thinspace\Omega$, $I_1 = 20\thinspace\text{mA}$, $I_2 = 30\thinspace\text{mA}$ och $I_3 = 50\thinspace\text{mA}$.\
**c)** Beräkna $U_R$ en gång till med det utmultiplicerade uttrycket och kontrollera att svaren stämmer överens.

---

### 2.3 – Faktorisering
Faktorisera följande uttryck:

**a)** $6I + 9IR$

**b)** $P_1^2 - P_2^2$

**c)** $U^2 - 10U + 25$

**d)** $4R^2 - 1$

---

### 2.4 – Gemensam faktor: total effekt i en seriekrets
Tre motstånd $R_1 = 120\thinspace\Omega$, $R_2 = 180\thinspace\Omega$ och $R_3 = 200\thinspace\Omega$ är seriekopplade och genomflyts därmed av samma ström $I = 50\thinspace\text{mA}$.

![](./images/2.4_circuit.png)

Effekten i respektive motstånd ges av $P_k = I^2 R_k$.

**a)** Skriv ett uttryck för den totala effekten $P_{\text{TOT}} = P_1 + P_2 + P_3$ och bryt ut den gemensamma faktorn.

**b)** Beräkna $P_{\text{TOT}}$ med det faktoriserade uttrycket.

**c)** Beräkna $P_1$, $P_2$ och $P_3$ var för sig och kontrollera att summan blir densamma. Vilken väg krävde minst räknearbete?

---

### 2.5 – Konjugatregeln: skillnad i effekt
Ett värmeelement med resistansen $R$ matas först med spänningen $U_1$ och sedan med $U_2$.

![](./images/2.5_circuit.png)

Effekten ges av $P = \dfrac{U^2}{R}$.

**a)** Visa att effektskillnaden kan skrivas:

```math
P_1 - P_2 = \frac{(U_1 + U_2)(U_1 - U_2)}{R}
```

**b)** Beräkna $P_1 - P_2$ **utan** miniräknare då $U_1 = 24\thinspace\text{V}$, $U_2 = 20\thinspace\text{V}$ och $R = 8\thinspace\Omega$.

**c)** Kontrollera svaret genom att beräkna $P_1$ och $P_2$ var för sig.

---

### 2.6 – Kvadreringsregeln: effekt vid en strömändring
Genom ett motstånd $R = 10\thinspace\Omega$ flyter strömmen $I_0 = 2\thinspace\text{A}$. Strömmen ökar med $\Delta I = 0{,}1\thinspace\text{A}$, så att den nya strömmen blir $I_0 + \Delta I$.

![](./images/2.6_circuit.png)

Effekten ges av $P = I^2 R$.

**a)** Multiplicera ut $P = R(I_0 + \Delta I)^2$ med kvadreringsregeln.

**b)** Beräkna den nya effekten med det utmultiplicerade uttrycket.

**c)** Hur stor är effektökningen $\Delta P$ jämfört med $P_0 = I_0^2 R$?

**d)** Hur stort blir felet om man struntar i termen $R\thinspace\Delta I^2$? Ange felet i procent av $\Delta P$.

---

### 2.7 – Effektuttryck och Ohms lag
Effekten som utvecklas i motståndet nedan kan skrivas $P = I^2 R$.

![](./images/2.7_circuit.png)

**a)** Visa att $P = I^2R$ kan faktoriseras till $P = I \cdot (IR)$ och identifiera vilken storhet $IR$ representerar.

**b)** Sätt in $I = \dfrac{U}{R}$ i $P = I^2R$ och visa att uttrycket kan förenklas till $P = \dfrac{U^2}{R}$.

**c)** Ett motstånd $R = 6\thinspace\Omega$ matas med $U = 12\thinspace\text{V}$. Beräkna effekten med alla tre formerna $P = UI$, $P = I^2R$ och $P = \dfrac{U^2}{R}$ och kontrollera att de ger samma svar.

---
