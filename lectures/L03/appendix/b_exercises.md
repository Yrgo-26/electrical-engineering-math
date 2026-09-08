# L03 – Lektionsuppgifter

## Del 1 – Repetitionsuppgifter
### 1.1 – Förenkling
Förenkla följande uttryck:

**a)** $3(2R + 4) - 2(R - 1)$

**b)** $(U + 3)^2 - 9$

**c)** $\dfrac{6I^2 + 4I}{2I}$, antag $I \neq 0$

---

### 1.2 – Faktorisering
Faktorisera:

**a)** $R^2 - 25$

**b)** $3U^2 + 6U$

**c)** $I^2 - 8I + 16$

---

## Del 2 – Nytt stoff
### 2.1 – Ohms lag – sök motståndet
Spänningen över ett motstånd är $U = 15\thinspace\text{V}$ och strömmen är $I = 0{,}3\thinspace\text{A}$.

![](./images/2.1_circuit.png)

Ohms lag anger att $U = R \cdot I$.

**a)** Sätt upp ekvationen och lös för $R$.

**b)** Kontrollera svaret.

---

### 2.2 – Seriekrets – ekvation med parentes
Två motstånd är seriekopplade. Kretsen matas med $U = 24\thinspace\text{V}$ och strömmen är $I = 0{,}4\thinspace\text{A}$. Det ena motståndet är $R_2 = 40\thinspace\Omega$, det andra är okänt.

![](./images/2.2_circuit.png)

Ohms lag för hela kretsen ger:

```math
U = (R_1 + R_2) \cdot I
```

**a)** Sätt in värdena och lös ekvationen för $R_1$ **utan** att multiplicera ut parentesen.

**b)** Lös ekvationen en gång till, men multiplicera ut parentesen först. Kontrollera att du får samma svar.

**c)** Kontrollera lösningen genom att beräkna strömmen $I = \dfrac{U}{R_1 + R_2}$.

---

### 2.3 – Spänningsdelning
I en spänningsdelare ges utspänningen av:

```math
U_{\text{ut}} = \frac{R_2}{R_1 + R_2} \cdot U_{\text{in}}
```

![](./images/2.3_circuit.png)

Antag $U_{\text{in}} = 9\thinspace\text{V}$, $R_2 = 3\thinspace\Omega$ och $U_{\text{ut}} = 3\thinspace\text{V}$.

**a)** Sätt upp ekvationen för $U_{\text{ut}}$ och lös för $R_1$.

**b)** Kontrollera svaret.

---

### 2.4 – Tidskonstant i RC-krets
Laddningstiden $\tau$ (tau) i en RC-krets är:

```math
\tau = R \cdot C
```

![](./images/2.4_circuit.png)

Kondensatorns kapacitans är $C = 100\thinspace\mu\text{F} = 100 \times 10^{-6}\thinspace\text{F}$ och tidskonstanten $\tau = 0{,}05\thinspace\text{s}$.

Beräkna motståndet $R$.

---

### 2.5 – Säkert driftområde
En transistors effektdissipation beräknas som $P = U_{CE} \cdot I_C$.

![](./images/2.5_circuit.png)

Transistorn tål maximalt $P_{\max} = 500\thinspace\text{mW}$ och kollektorströmmen är $I_C = 50\thinspace\text{mA}$.

**a)** Sätt upp en olikhet för att bestämma det maximalt tillåtna spänningsfallet $U_{CE}$.

**b)** Lös olikheten och ange det maximalt tillåtna $U_{CE}$ i volt.

---

### 2.6 – Belastat batteri – olikhet med teckenvändning
Ett batteri har tomgångsspänningen $E = 12\thinspace\text{V}$ och den inre resistansen $R_i = 0{,}8\thinspace\Omega$. När batteriet belastas med strömmen $I$ blir klämspänningen:

```math
U = E - R_i \cdot I
```

![](./images/2.6_circuit.png)

**a)** Beräkna klämspänningen $U$ då $I = 2\thinspace\text{A}$.

**b)** Den anslutna enheten kräver minst $9\thinspace\text{V}$ för att fungera. Sätt upp olikheten $U \geq 9$ och lös den för $I$.

> **Tips:** Tänk på vad som händer med olikhetstecknet när du dividerar med ett negativt tal.

**c)** Ett annat batteri har $E = 13\thinspace\text{V}$ och $R_i = 1{,}0\thinspace\Omega$. Vid vilken ström ger de båda batterierna samma klämspänning? Ställ upp en ekvation med obekant i båda led och lös den.

**d)** Vilket av batterierna ger högst klämspänning vid $I = 8\thinspace\text{A}$?

---

### 2.7 – Absolutbelopp i signalanalys
En signal kan ha positiv eller negativ avvikelse från en referensspänning. Avvikelsen $\delta$ uppfyller $|\delta| \leq 0{,}5\thinspace\text{V}$.

**a)** Skriv om absolutbeloppsolikheten som ett dubbelsidat intervall utan absolutbelopp.

**b)** Om referensspänningen är $5\thinspace\text{V}$, ange det tillåtna intervallet för den faktiska spänningen.

---

### 2.8 – Strömreglering – absolutbeloppsekvation
En strömregulator jämför den uppmätta strömmen $I$ (i ampere) med sitt börvärde och ger felspänningen:

```math
u_e = 0{,}4I - 2
```

**a)** Vid vilken ström är felspänningen noll, dvs. vilket är börvärdet?

**b)** Regulatorn larmar när felspänningen har beloppet $1{,}2\thinspace\text{V}$. Lös ekvationen $|0{,}4I - 2| = 1{,}2$ som två fall och ange de två strömmar där larmet triggar.

**c)** Vilket strömintervall uppfyller $|0{,}4I - 2| \leq 1{,}2$, dvs. när larmar regulatorn *inte*?

---

## Del 3 – Extrauppgifter
Uppgifterna nedan är extra träning och görs med fördel på egen hand efter lektionen. De flesta går att räkna i huvudet eller med papper och penna.

### 3.1 – Enkla linjära ekvationer
Lös ekvationerna:

**a)** $x + 7 = 12$

**b)** $5x = 45$

**c)** $3x - 4 = 11$

**d)** $\dfrac{x}{4} = 6$

**e)** $8 - 2x = 0$

**f)** $-3x = 18$

---

### 3.2 – Obekant i båda led
Lös ekvationerna och kontrollera svaret:

**a)** $5x - 3 = 2x + 9$

**b)** $7 - 2x = x + 1$

**c)** $4(x - 1) = 2(x + 3)$

**d)** $3(2x + 1) = 6x + 3$

**e)** $2(x + 4) = 2x + 5$

> **Tips:** Två av uppgifterna beter sig annorlunda än de övriga. Fundera på vad det betyder.

---

### 3.3 – Ekvationer med bråk
Lös ekvationerna:

**a)** $\dfrac{x}{3} + \dfrac{x}{6} = 3$

**b)** $\dfrac{2x - 1}{5} = 3$

**c)** $\dfrac{x}{2} - \dfrac{x}{5} = 3$

**d)** $\dfrac{12}{x} = 4$, antag $x \neq 0$

---

### 3.4 – Proportionsekvationer
**a)** Lös $\dfrac{x}{8} = \dfrac{3}{4}$.

**b)** Lös $\dfrac{5}{x} = \dfrac{2}{6}$.

**c)** I en spänningsdelare gäller $\dfrac{U_1}{U_2} = \dfrac{R_1}{R_2}$. Beräkna $R_1$ då $U_1 = 4\thinspace\text{V}$, $U_2 = 8\thinspace\text{V}$ och $R_2 = 2\thinspace\text{k}\Omega$.

**d)** Ett motstånd har spänningen $6\thinspace\text{V}$ vid strömmen $0{,}2\thinspace\text{A}$. Vilken spänning krävs för strömmen $0{,}5\thinspace\text{A}$? Ställ upp en proportion och lös den.

---

### 3.5 – Lös ut en variabel ur en formel
Lös ut den variabel som anges:

**a)** $U = RI$, lös ut $I$.

**b)** $P = RI^2$, lös ut $R$.

**c)** $R_{\text{TOT}} = R_1 + R_2$, lös ut $R_2$.

**d)** $\tau = RC$, lös ut $C$.

**e)** $U = E - R_iI$, lös ut $R_i$.

**f)** $\eta = \dfrac{P_{\text{ut}}}{P_{\text{in}}}$, lös ut $P_{\text{in}}$.

---

### 3.6 – Olikheter
Lös olikheterna och beskriv lösningen som ett intervall på tallinjen:

**a)** $x + 3 < 8$

**b)** $2x - 1 \geq 7$

**c)** $-x > 4$

**d)** $-2x + 6 \leq 0$

**e)** $5 - 3x > 14$

---

### 3.7 – Dubbelsidiga olikheter
**a)** Lös $2 < x + 1 < 7$.

**b)** Lös $-3 \leq 2x - 1 \leq 5$.

**c)** En komponent matas med $U = 5\thinspace\text{V}$ och tål högst $P_{\max} = 0{,}25\thinspace\text{W}$. Sätt upp och lös en olikhet för den tillåtna strömmen $I$.

**d)** En logisk etta tolkas när insignalen ligger i intervallet $2{,}0\thinspace\text{V} \leq u \leq 3{,}3\thinspace\text{V}$. Insignalen ges av $u = 0{,}5x$ volt. Vilka värden på $x$ ger en logisk etta?

---

### 3.8 – Absolutbelopp i ekvationer
Lös ekvationerna:

**a)** $|x| = 6$

**b)** $|x - 3| = 5$

**c)** $|2x + 1| = 7$

**d)** $|x + 4| = 0$

**e)** $|3x - 2| = -5$

---

### 3.9 – Absolutbelopp i olikheter och toleranser
**a)** Skriv $|x - 5| \leq 2$ utan absolutbelopp och lös olikheten.

**b)** Lös $|2x - 6| < 4$.

**c)** En matningsspänning ska vara $5\thinspace\text{V}$ med toleransen $\pm 2\thinspace\char37$. Skriv kravet som en absolutbeloppsolikhet och ange det tillåtna spänningsintervallet.

**d)** En resistor är märkt $1\thinspace\text{k}\Omega \pm 1\thinspace\char37$ och mäts till $1\thinspace 015\thinspace\Omega$. Uppfyller den kravet $|R - 1000| \leq 10$?

---

### 3.10 – Temperaturberoende resistans
En resistors resistans varierar med temperaturen enligt:

```math
R = R_0(1 + \alpha \cdot \Delta T)
```

Här är $R_0 = 100\thinspace\Omega$ resistansen vid $20^\circ\text{C}$, $\alpha = 0{,}004\thinspace^\circ\text{C}^{-1}$ och $\Delta T$ är temperaturändringen räknad från $20^\circ\text{C}$.

**a)** Beräkna $R$ vid $70^\circ\text{C}$.

**b)** Vid vilken temperatur är $R = 110\thinspace\Omega$?

**c)** Kretsen fungerar så länge $R \leq 130\thinspace\Omega$. Vilket temperaturintervall är tillåtet?

**d)** Lös ut $\Delta T$ ur formeln allmänt.

---
