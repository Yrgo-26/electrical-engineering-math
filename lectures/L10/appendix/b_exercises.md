# L10 - Lektionsuppgifter

## Del 1 - Repetitionsuppgifter

### 1.1 - Vinklar till radianer
Omvandla följande vinklar till radianer:

**a)** $15°$

**b)** $-75°$

---

### 1.2 – Vinklar till grader
Omvandla följande vinklar till grader:

**a)** $-π/6$

**b)** $3π/2$

---

### 1.3 – Bestämning av en växelspännings egenskaper
En växelspänning visas i figuren nedan.

![Växelspänning med okända egenskaper](./images/1.3_sine_wave.png)

Bestäm spänningens ekvation på formen $u(t)=|U|sin⁡(wt+δ)$.

---

### 1.4 – Ekvation samt graf för en växelspänning
En växelspänning har amplituden $4$ $V$, frekvensen $50$ $Hz$ och fasen $-30°$.

Bestäm växelspänningens ekvation $u(t)$ (fasen i $rad$) och rita sinuskurvan över en period $T$.

---

### 1.5 – Beräkning av en växelströms fas
Ekvationen för en given växelspänning är:

```math
u(t)=6sin⁡(80πt+δ)
```

Vid tiden $t=15$ $ms$ gäller att $u(t) = 3$ $V$. Beräkna fasen $δ$.

---

## Del 2 - Nytt stoff

### 2.1 - Logaritmiska ekvationer
Lös följande logaritmiska ekvationer:

**a)** $3^x = 81$

**b)** $2^{x-1} = 64$

**c)** $e^{x-2} = 150$

---

### 2.2 - Halveringstid för laddning i ett batteri  
Laddningen för ett batteri kan beskrivas via motsvarande spänning i enlighet med följande funktion:

```math
u(t) = U_0 * a^t
```

där 
* $u(t)$ är nuvarande laddning,
* $U_0$ är den ursprungliga laddningen,
* $a$ är förändringsfaktorn,
* $t$ är antalet passerade timmar.

Ett batteri tappar halva sin laddning på $30$ timmar. Beräkna efter hur lång tid endast $20$ % av laddningen återstår.

---

### 2.3 -  Linjär förstärkning

Två signaler har spänningsnivåerna $L_1 = 20$ $dB$ och $L_2 = 46$ $dB$.

Beräkna den linjära spänningsförstärkningen $G_{lin}$ mellan dessa två nivåer.  

Använd följande formel:

```math
G_{dB} = 20\log_{10}(G_{lin})  
```

och tänk på att

```math
G_{dB} = L_2 - L_1.
```

---

### 2.4 - Beräkning av effektivvärde i $dBV$ 
Sambandet mellan en spännings effektivvärde samt motsvarande värde i $dBV$ (decibel Volt) visas nedan:

```math
U_{dBV} = 20 \log_{10} \left( \frac{U_{RMS}}{1\,V} \right)
```
där 
* $U_{RMS}$ = spänningens effektivvärde i $V$,
* $U_{dBV}$ = spänningen i $dBV$.

En sinusspänning har amplitud = $31,0$ $dBV$. Bestäm amplituden i $V$.

---

## Del 3 – Extrauppgifter
Uppgifterna nedan är extra träning och görs med fördel på egen hand efter lektionen. De flesta går att räkna i huvudet eller med papper och penna.

### 3.1 – Logaritmer utan miniräknare
Beräkna:

**a)** $\log 100$

**b)** $\log 1000$

**c)** $\log 1$

**d)** $\log 0{,}01$

**e)** $\ln e$

**f)** $\ln 1$

---

### 3.2 – Logaritmlagarna
Skriv som en enda logaritm och förenkla så långt som möjligt:

**a)** $\log 3 + \log 4$

**b)** $\log 20 - \log 4$

**c)** $2\log 5$

**d)** $\log 2 + \log 5$

**e)** $3\log 2 - \log 4$

---

### 3.3 – Exponentialekvationer
Lös ekvationerna:

**a)** $2^x = 32$

**b)** $10^x = 0{,}001$

**c)** $5^x = 100$

**d)** $e^x = 20$

**e)** $4^{x+1} = 64$

---

### 3.4 – Logaritmiska ekvationer
Lös ekvationerna:

**a)** $\log x = 2$

**b)** $\ln x = 0$

**c)** $\log(x + 5) = 1$

**d)** $2\log x = 4$

**e)** $\ln(2x) = 1$

---

### 3.5 – Spänningsförstärkning i dB
Använd $G_{\text{dB}} = 20\log_{10}\!\left(\dfrac{U_{\text{ut}}}{U_{\text{in}}}\right)$.

**a)** $U_{\text{in}} = 10\thinspace\text{mV}$ och $U_{\text{ut}} = 1\thinspace\text{V}$. Beräkna $G_{\text{dB}}$.

**b)** $U_{\text{in}} = 2\thinspace\text{V}$ och $U_{\text{ut}} = 2\thinspace\text{V}$. Beräkna $G_{\text{dB}}$.

**c)** $U_{\text{in}} = 5\thinspace\text{V}$ och $U_{\text{ut}} = 0{,}5\thinspace\text{V}$. Beräkna $G_{\text{dB}}$.

**d)** Vad betyder ett negativt värde på $G_{\text{dB}}$?

---

### 3.6 – Från dB till linjär förstärkning
Använd $G_{\text{lin}} = 10^{G_{\text{dB}}/20}$.

**a)** $G_{\text{dB}} = 20\thinspace\text{dB}$

**b)** $G_{\text{dB}} = 60\thinspace\text{dB}$

**c)** $G_{\text{dB}} = 6\thinspace\text{dB}$

**d)** $G_{\text{dB}} = -3\thinspace\text{dB}$

**e)** En förstärkare med $G_{\text{dB}} = 26\thinspace\text{dB}$ matas med $U_{\text{in}} = 50\thinspace\text{mV}$. Beräkna $U_{\text{ut}}$.

---

### 3.7 – Effektförstärkning i dB
Använd $G_{\text{dB}} = 10\log_{10}\!\left(\dfrac{P_{\text{ut}}}{P_{\text{in}}}\right)$.

**a)** $P_{\text{in}} = 1\thinspace\text{W}$ och $P_{\text{ut}} = 100\thinspace\text{W}$. Beräkna $G_{\text{dB}}$.

**b)** $P_{\text{in}} = 20\thinspace\text{W}$ och $P_{\text{ut}} = 10\thinspace\text{W}$. Beräkna $G_{\text{dB}}$.

**c)** Varför används faktorn $10$ för effekt men $20$ för spänning?

**d)** Hur många dB motsvarar en fördubbling av effekten? Och en fördubbling av spänningen?

---

### 3.8 – Kaskadkopplade steg
En signalkedja består av två förstärkarsteg med $G_1 = 12\thinspace\text{dB}$ och $G_2 = 18\thinspace\text{dB}$, samt en kabel som dämpar $4\thinspace\text{dB}$.

**a)** Beräkna den totala förstärkningen i dB.

**b)** Beräkna den totala linjära förstärkningen.

**c)** Beräkna varje delsteg linjärt och kontrollera att produkten stämmer med **b)**.

**d)** Varför är dB praktiskt att räkna med vid kaskadkoppling?

---

### 3.9 – Nivå i dBV
Använd $U_{\text{dBV}} = 20\log_{10}\!\left(\dfrac{U_{\text{RMS}}}{1\thinspace\text{V}}\right)$.

**a)** $U_{\text{RMS}} = 1\thinspace\text{V}$. Beräkna nivån i dBV.

**b)** $U_{\text{RMS}} = 10\thinspace\text{V}$. Beräkna nivån i dBV.

**c)** $U_{\text{RMS}} = 0{,}1\thinspace\text{V}$. Beräkna nivån i dBV.

**d)** En signal ligger på $12\thinspace\text{dBV}$. Beräkna $U_{\text{RMS}}$.

**e)** Beräkna amplituden $|U|$ för signalen i **d)**.

---

### 3.10 – Halverings- och fördubblingstid
En storhet beskrivs av $f(t) = C \cdot a^t$.

**a)** Ett batteri tappar $2\thinspace\char37$ av sin laddning per timme. Bestäm förändringsfaktorn $a$.

**b)** Efter hur många timmar återstår hälften av laddningen?

**c)** En mätdatamängd växer med $10\thinspace\char37$ per dygn. Efter hur många dygn har den fördubblats?

**d)** Visa allmänt att fördubblingstiden ges av $t = \dfrac{\log 2}{\log a}$.

---

### 3.11 – Hitta felet
Varje rad innehåller ett vanligt fel. Förklara felet och ange det korrekta svaret.

**a)** $\log(a + b) = \log a + \log b$

**b)** $\dfrac{\log 8}{\log 2} = \log 4$

**c)** $\log(a^n) = (\log a)^n$

**d)** $G_{\text{dB}} = 0$ betyder att signalen försvinner helt.

**e)** $10^{\log x} = 10x$

**f)** $\ln 0 = 1$

---
