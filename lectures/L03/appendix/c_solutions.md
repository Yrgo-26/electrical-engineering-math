# L03 – Lösningsförslag

## Del 1 – Repetitionsuppgifter
### 1.1 – Förenkling
**a)** $3(2R + 4) - 2(R - 1)$

**b)** $(U + 3)^2 - 9$

**c)** $\dfrac{6I^2 + 4I}{2I}$, antag $I \neq 0$

---

### Lösning
**a)** Multiplicera ut parenteserna:

```math
3(2R + 4) - 2(R - 1) = 6R + 12 - 2R + 2 = 4R + 14
```

**b)** Använd kvadreringsregeln $(U+3)^2 = U^2 + 6U + 9$:

```math
(U + 3)^2 - 9 = U^2 + 6U + 9 - 9 = U^2 + 6U
```

Alternativt faktorisera: $U^2 + 6U = U(U + 6)$.

**c)** Dela varje term i täljaren med $2I$:

```math
\frac{6I^2 + 4I}{2I} = \frac{6I^2}{2I} + \frac{4I}{2I} = 3I + 2
```

---

### 1.2 – Faktorisering
**a)** $R^2 - 25$

**b)** $3U^2 + 6U$

**c)** $I^2 - 8I + 16$

---

### Lösning
**a)** Konjugatregeln: $R^2 - 5^2$:

```math
R^2 - 25 = (R + 5)(R - 5)
```

**b)** Gemensam faktor $3U$:

```math
3U^2 + 6U = 3U(U + 2)
```

**c)** Kvadrat av differens: $(I - 4)^2 = I^2 - 8I + 16$:

```math
I^2 - 8I + 16 = (I - 4)^2
```

---

## Del 2 – Nytt stoff
### 2.1 – Ohms lag – sök motståndet
$U = 15\thinspace\text{V}$, $I = 0{,}3\thinspace\text{A}$

---

### Lösning
**a)** Ekvationen är $15 = R \cdot 0{,}3$. Dividera med $0{,}3$:

```math
R = \frac{15}{0{,}3} = 50\,\Omega
```

**b)** Kontroll: $U = R \cdot I = 50 \times 0{,}3 = 15\thinspace\text{V}$ ✓

---

### 2.2 – Seriekrets – ekvation med parentes
$U = 24\thinspace\text{V}$, $I = 0{,}4\thinspace\text{A}$, $R_2 = 40\thinspace\Omega$

---

### Lösning
**a)** Insättning i $U = (R_1 + R_2) \cdot I$ ger:

```math
24 = (R_1 + 40) \times 0{,}4
```

Dividera båda led med $0{,}4$ (multiplikationsprincipen):

```math
\frac{24}{0{,}4} = R_1 + 40 \quad \Rightarrow \quad 60 = R_1 + 40
```

Subtrahera $40$ i båda led (additionsprincipen):

```math
R_1 = 20\,\Omega
```

**b)** Multiplicera ut parentesen först:

```math
24 = 0{,}4R_1 + 16
```

Subtrahera $16$ i båda led:

```math
8 = 0{,}4R_1
```

Dividera med $0{,}4$:

```math
R_1 = \frac{8}{0{,}4} = 20\,\Omega
```

Samma svar – vilken väg man väljer spelar ingen roll, båda följer ekvationsprinciperna.

**c)** Kontroll:

```math
I = \frac{U}{R_1 + R_2} = \frac{24}{20 + 40} = \frac{24}{60} = 0{,}4\,\text{A} \quad ✓
```

---

### 2.3 – Spänningsdelning
$U_{\text{in}} = 9\thinspace\text{V}$, $R_2 = 3\thinspace\Omega$, $U_{\text{ut}} = 3\thinspace\text{V}$

---

### Lösning
**a)** Vi sätter upp ekvationen:

```math
3 = \frac{3}{R_1 + 3} \times 9
```

Dividera båda led med $9$:

```math
\frac{3}{9} = \frac{3}{R_1 + 3} \quad \Rightarrow \quad \frac{1}{3} = \frac{3}{R_1 + 3}
```

Korsvis multiplikation:

```math
R_1 + 3 = 9 \quad \Rightarrow \quad R_1 = 6\,\Omega
```

**b)** Kontroll: $U_{\text{ut}} = \dfrac{3}{6+3} \times 9 = \dfrac{3}{9} \times 9 = 3\thinspace\text{V}$ ✓

---

### 2.4 – Tidskonstant i RC-krets
$\tau = 0{,}05\thinspace\text{s}$, $C = 100 \times 10^{-6}\thinspace\text{F}$

---

### Lösning
Ur $\tau = R \cdot C$ löser vi för $R$:

```math
R = \frac{\tau}{C} = \frac{0{,}05}{100 \times 10^{-6}} = \frac{0{,}05}{10^{-4}} = 500\,\Omega
```

---

### 2.5 – Säkert driftområde
$P_{\max} = 500\thinspace\text{mW} = 0{,}5\thinspace\text{W}$, $I_C = 50\thinspace\text{mA} = 0{,}05\thinspace\text{A}$

---

### Lösning
**a)** Olikheten är:

```math
U_{CE} \cdot I_C \leq P_{\max} \quad \Rightarrow \quad U_{CE} \cdot 0{,}05 \leq 0{,}5
```

**b)** Dividera med $0{,}05$:

```math
U_{CE} \leq \frac{0{,}5}{0{,}05} = 10\,\text{V}
```

Transistorns $U_{CE}$ får inte överstiga $10\thinspace\text{V}$.

---

### 2.6 – Belastat batteri – olikhet med teckenvändning
$E = 12\thinspace\text{V}$, $R_i = 0{,}8\thinspace\Omega$

---

### Lösning
**a)** Insättning av $I = 2\thinspace\text{A}$:

```math
U = 12 - 0{,}8 \times 2 = 12 - 1{,}6 = 10{,}4\,\text{V}
```

**b)** Kravet $U \geq 9$ ger olikheten:

```math
12 - 0{,}8I \geq 9
```

Subtrahera $12$ i båda led:

```math
-0{,}8I \geq -3
```

Dividera med $-0{,}8$. Eftersom vi dividerar med ett **negativt tal vänder olikhetstecknet**:

```math
I \leq \frac{-3}{-0{,}8} = 3{,}75\,\text{A}
```

Strömmen får alltså inte överstiga $3{,}75\thinspace\text{A}$. Kontroll: vid $I = 3{,}75$ blir $U = 12 - 0{,}8 \times 3{,}75 = 12 - 3 = 9\thinspace\text{V}$ ✓

**c)** Klämspänningarna sätts lika:

```math
12 - 0{,}8I = 13 - 1{,}0I
```

Addera $1{,}0I$ i båda led och subtrahera $12$:

```math
0{,}2I = 1 \quad \Rightarrow \quad I = \frac{1}{0{,}2} = 5\,\text{A}
```

Kontroll: batteri 1 ger $12 - 0{,}8 \times 5 = 8\thinspace\text{V}$ och batteri 2 ger $13 - 1{,}0 \times 5 = 8\thinspace\text{V}$ ✓

**d)** Vid $I = 8\thinspace\text{A}$:

```math
U_1 = 12 - 0{,}8 \times 8 = 5{,}6\,\text{V}, \qquad U_2 = 13 - 1{,}0 \times 8 = 5{,}0\,\text{V}
```

Det första batteriet ger högst klämspänning. Trots att batteri 2 har högre tomgångsspänning sjunker dess spänning snabbare, eftersom den inre resistansen är större.

---

### 2.7 – Absolutbelopp i signalanalys
$|\delta| \leq 0{,}5\thinspace\text{V}$, referensspänning $5\thinspace\text{V}$

---

### Lösning
**a)** $|\delta| \leq 0{,}5$ innebär:

```math
-0{,}5 \leq \delta \leq 0{,}5
```

**b)** Den faktiska spänningen $u = 5 + \delta$ (referens plus avvikelse):

```math
5 - 0{,}5 \leq u \leq 5 + 0{,}5 \quad \Rightarrow \quad 4{,}5\,\text{V} \leq u \leq 5{,}5\,\text{V}
```

---

### 2.8 – Strömreglering – absolutbeloppsekvation
$u_e = 0{,}4I - 2$

---

### Lösning
**a)** Sätt $u_e = 0$:

```math
0{,}4I - 2 = 0 \quad \Rightarrow \quad 0{,}4I = 2 \quad \Rightarrow \quad I = \frac{2}{0{,}4} = 5\,\text{A}
```

Börvärdet är alltså $5\thinspace\text{A}$.

**b)** $|0{,}4I - 2| = 1{,}2$ ger två fall:

Fall 1:

```math
0{,}4I - 2 = 1{,}2 \quad \Rightarrow \quad 0{,}4I = 3{,}2 \quad \Rightarrow \quad I = 8\,\text{A}
```

Fall 2:

```math
0{,}4I - 2 = -1{,}2 \quad \Rightarrow \quad 0{,}4I = 0{,}8 \quad \Rightarrow \quad I = 2\,\text{A}
```

Larmet triggar vid $I = 2\thinspace\text{A}$ och $I = 8\thinspace\text{A}$.

**c)** Olikheten skrivs som ett dubbelsidat intervall:

```math
-1{,}2 < 0{,}4I - 2 < 1{,}2
```

Addera $2$ i alla tre led:

```math
0{,}8 < 0{,}4I < 3{,}2
```

Dividera med $0{,}4$ (positivt tal – tecknen behålls):

```math
2\,\text{A} < I < 8\,\text{A}
```

Gränserna $2\thinspace\text{A}$ och $8\thinspace\text{A}$ ingår inte: där är beloppet exakt $1{,}2\thinspace\text{V}$, och då larmar regulatorn enligt **b)**.

Regulatorn larmar alltså inte så länge strömmen ligger mellan $2\thinspace\text{A}$ och $8\thinspace\text{A}$, dvs. inom $\pm 3\thinspace\text{A}$ från börvärdet.

---

## Del 3 – Extrauppgifter
### 3.1 – Enkla linjära ekvationer
**a)** $x + 7 = 12$

**b)** $5x = 45$

**c)** $3x - 4 = 11$

**d)** $\dfrac{x}{4} = 6$

**e)** $8 - 2x = 0$

**f)** $-3x = 18$

---

### Lösning
**a)** Subtrahera $7$ i båda led:

```math
x = 12 - 7 = 5
```

**b)** Dividera med $5$ i båda led:

```math
x = \frac{45}{5} = 9
```

**c)** Addera $4$, dividera sedan med $3$:

```math
3x = 15 \quad \Rightarrow \quad x = 5
```

**d)** Multiplicera med $4$ i båda led:

```math
x = 6 \times 4 = 24
```

**e)** Addera $2x$ i båda led och dividera med $2$:

```math
8 = 2x \quad \Rightarrow \quad x = 4
```

**f)** Dividera med $-3$:

```math
x = \frac{18}{-3} = -6
```

---

### 3.2 – Obekant i båda led
**a)** $5x - 3 = 2x + 9$

**b)** $7 - 2x = x + 1$

**c)** $4(x - 1) = 2(x + 3)$

**d)** $3(2x + 1) = 6x + 3$

**e)** $2(x + 4) = 2x + 5$

---

### Lösning
Strategin är densamma varje gång: samla obekanta i ett led och konstanter i det andra.

**a)** Subtrahera $2x$ och addera $3$:

```math
3x = 12 \quad \Rightarrow \quad x = 4
```

Kontroll: $5 \cdot 4 - 3 = 17$ och $2 \cdot 4 + 9 = 17$ ✓

**b)** Addera $2x$ och subtrahera $1$:

```math
6 = 3x \quad \Rightarrow \quad x = 2
```

Kontroll: $7 - 4 = 3$ och $2 + 1 = 3$ ✓

**c)** Multiplicera ut båda parenteserna först:

```math
4x - 4 = 2x + 6 \quad \Rightarrow \quad 2x = 10 \quad \Rightarrow \quad x = 5
```

Kontroll: $4(5 - 1) = 16$ och $2(5 + 3) = 16$ ✓

**d)** Multiplicera ut:

```math
6x + 3 = 6x + 3
```

Leden är identiska. Ekvationen är sann för **alla** $x$ – den har oändligt många lösningar och kallas en *identitet*.

**e)** Multiplicera ut:

```math
2x + 8 = 2x + 5 \quad \Rightarrow \quad 8 = 5
```

Ett falskt påstående. Ekvationen **saknar lösning**. Att den obekanta försvinner betyder alltså antingen "alla lösningar" (om det som återstår är sant) eller "ingen lösning" (om det är falskt).

---

### 3.3 – Ekvationer med bråk
**a)** $\dfrac{x}{3} + \dfrac{x}{6} = 3$

**b)** $\dfrac{2x - 1}{5} = 3$

**c)** $\dfrac{x}{2} - \dfrac{x}{5} = 3$

**d)** $\dfrac{12}{x} = 4$

---

### Lösning
**a)** Multiplicera båda led med den gemensamma nämnaren $6$:

```math
2x + x = 18 \quad \Rightarrow \quad 3x = 18 \quad \Rightarrow \quad x = 6
```

**b)** Multiplicera båda led med $5$:

```math
2x - 1 = 15 \quad \Rightarrow \quad 2x = 16 \quad \Rightarrow \quad x = 8
```

**c)** Multiplicera båda led med $10$:

```math
5x - 2x = 30 \quad \Rightarrow \quad 3x = 30 \quad \Rightarrow \quad x = 10
```

**d)** Multiplicera båda led med $x$ och dividera med $4$:

```math
12 = 4x \quad \Rightarrow \quad x = 3
```

---

### 3.4 – Proportionsekvationer

---

### Lösning
**a)** Korsvis multiplikation:

```math
4x = 24 \quad \Rightarrow \quad x = 6
```

**b)** Korsvis multiplikation:

```math
2x = 30 \quad \Rightarrow \quad x = 15
```

**c)** Sätt in värdena i proportionen:

```math
\frac{4}{8} = \frac{R_1}{2} \quad \Rightarrow \quad 8R_1 = 8 \quad \Rightarrow \quad R_1 = 1\,\text{k}\Omega
```

Spänningarna förhåller sig som resistanserna: hälften så stor spänning betyder hälften så stor resistans.

**d)** Ohms lag gör spänningen proportionell mot strömmen så länge $R$ är konstant:

```math
\frac{6}{0{,}2} = \frac{U}{0{,}5} \quad \Rightarrow \quad 0{,}2U = 3 \quad \Rightarrow \quad U = 15\,\text{V}
```

Kontroll: kvoten $\dfrac{6}{0{,}2} = 30\thinspace\Omega$ är motståndet, och $30 \times 0{,}5 = 15\thinspace\text{V}$ ✓

---

### 3.5 – Lös ut en variabel ur en formel

---

### Lösning
Samma ekvationsprinciper används, men nu med bokstäver i stället för tal.

**a)** Dividera med $R$:

```math
I = \frac{U}{R}
```

**b)** Dividera med $I^2$:

```math
R = \frac{P}{I^2}
```

**c)** Subtrahera $R_1$:

```math
R_2 = R_{\text{TOT}} - R_1
```

**d)** Dividera med $R$:

```math
C = \frac{\tau}{R}
```

**e)** Flytta över termerna och dividera med $I$:

```math
R_iI = E - U \quad \Rightarrow \quad R_i = \frac{E - U}{I}
```

**f)** Multiplicera med $P_{\text{in}}$ och dividera med $\eta$:

```math
\eta P_{\text{in}} = P_{\text{ut}} \quad \Rightarrow \quad P_{\text{in}} = \frac{P_{\text{ut}}}{\eta}
```

---

### 3.6 – Olikheter
**a)** $x + 3 < 8$

**b)** $2x - 1 \geq 7$

**c)** $-x > 4$

**d)** $-2x + 6 \leq 0$

**e)** $5 - 3x > 14$

---

### Lösning
**a)** Subtrahera $3$ (tecknet behålls):

```math
x < 5
```

Alla tal till vänster om $5$ på tallinjen, $5$ ej medräknat.

**b)** Addera $1$ och dividera med $2$:

```math
2x \geq 8 \quad \Rightarrow \quad x \geq 4
```

Alla tal från och med $4$ och uppåt.

**c)** Dividera med $-1$ – **tecknet vänder**:

```math
x < -4
```

**d)** Subtrahera $6$ och dividera med $-2$ – **tecknet vänder**:

```math
-2x \leq -6 \quad \Rightarrow \quad x \geq 3
```

**e)** Subtrahera $5$ och dividera med $-3$ – **tecknet vänder**:

```math
-3x > 9 \quad \Rightarrow \quad x < -3
```

Notera att tecknet vänder i **c)**, **d)** och **e)** – alltid när man dividerar med ett negativt tal.

---

### 3.7 – Dubbelsidiga olikheter

---

### Lösning
**a)** Subtrahera $1$ i alla tre led:

```math
1 < x < 6
```

**b)** Addera $1$ i alla led och dividera med $2$:

```math
-2 \leq 2x \leq 6 \quad \Rightarrow \quad -1 \leq x \leq 3
```

**c)** Effekten får inte överstiga $P_{\max}$:

```math
UI \leq P_{\max} \quad \Rightarrow \quad 5I \leq 0{,}25 \quad \Rightarrow \quad I \leq 0{,}05\,\text{A} = 50\,\text{mA}
```

**d)** Sätt in $u = 0{,}5x$ i intervallet och dividera alla led med $0{,}5$:

```math
2{,}0 \leq 0{,}5x \leq 3{,}3 \quad \Rightarrow \quad 4{,}0 \leq x \leq 6{,}6
```

---

### 3.8 – Absolutbelopp i ekvationer
**a)** $|x| = 6$

**b)** $|x - 3| = 5$

**c)** $|2x + 1| = 7$

**d)** $|x + 4| = 0$

**e)** $|3x - 2| = -5$

---

### Lösning
**a)** Två tal ligger på avståndet $6$ från noll:

```math
x = 6 \quad \text{eller} \quad x = -6
```

**b)** Två fall:

```math
x - 3 = 5 \quad \Rightarrow \quad x = 8
\qquad \text{eller} \qquad
x - 3 = -5 \quad \Rightarrow \quad x = -2
```

**c)** Två fall:

```math
2x + 1 = 7 \quad \Rightarrow \quad x = 3
\qquad \text{eller} \qquad
2x + 1 = -7 \quad \Rightarrow \quad x = -4
```

**d)** Endast noll har absolutbeloppet noll, så de två fallen sammanfaller:

```math
x + 4 = 0 \quad \Rightarrow \quad x = -4
```

Ekvationen har alltså **en enda** lösning.

**e)** Ett absolutbelopp är alltid icke-negativt och kan aldrig vara $-5$. Ekvationen **saknar lösning**.

---

### 3.9 – Absolutbelopp i olikheter och toleranser

---

### Lösning
**a)** $|x - 5| \leq 2$ betyder att avståndet från $x$ till $5$ är högst $2$:

```math
-2 \leq x - 5 \leq 2 \quad \Rightarrow \quad 3 \leq x \leq 7
```

**b)**

```math
-4 < 2x - 6 < 4 \quad \Rightarrow \quad 2 < 2x < 10 \quad \Rightarrow \quad 1 < x < 5
```

**c)** $2\char37$ av $5\thinspace\text{V}$ är $0{,}1\thinspace\text{V}$, så kravet är:

```math
|u - 5| \leq 0{,}1 \quad \Rightarrow \quad 4{,}9\,\text{V} \leq u \leq 5{,}1\,\text{V}
```

**d)** Nej. Avvikelsen är:

```math
|1015 - 1000| = 15 > 10
```

Resistorn ligger utanför toleransen $\pm 1\char37$, som motsvarar intervallet $990$–$1010\thinspace\Omega$.

---

### 3.10 – Temperaturberoende resistans
$R_0 = 100\thinspace\Omega$, $\alpha = 0{,}004\thinspace^\circ\text{C}^{-1}$, referenstemperatur $20^\circ\text{C}$

---

### Lösning
**a)** Vid $70^\circ\text{C}$ är $\Delta T = 70 - 20 = 50^\circ\text{C}$:

```math
R = 100(1 + 0{,}004 \times 50) = 100(1 + 0{,}2) = 120\,\Omega
```

**b)** Sätt $R = 110$ och lös för $\Delta T$:

```math
110 = 100(1 + 0{,}004\,\Delta T)
```

Dividera med $100$ och subtrahera $1$:

```math
1{,}1 = 1 + 0{,}004\,\Delta T \quad \Rightarrow \quad 0{,}004\,\Delta T = 0{,}1 \quad \Rightarrow \quad \Delta T = 25^\circ\text{C}
```

Temperaturen är alltså $20 + 25 = 45^\circ\text{C}$.

**c)** Samma räkning, men med en olikhet:

```math
100(1 + 0{,}004\,\Delta T) \leq 130 \quad \Rightarrow \quad 0{,}004\,\Delta T \leq 0{,}3 \quad \Rightarrow \quad \Delta T \leq 75^\circ\text{C}
```

Eftersom vi dividerar med positiva tal behålls olikhetstecknet. Temperaturen får alltså vara högst $20 + 75 = 95^\circ\text{C}$.

**d)** Dividera med $R_0$, subtrahera $1$ och dividera med $\alpha$:

```math
\frac{R}{R_0} = 1 + \alpha\,\Delta T \quad \Rightarrow \quad \Delta T = \frac{\frac{R}{R_0} - 1}{\alpha} = \frac{R - R_0}{R_0\,\alpha}
```

Kontroll med **b)**: $\Delta T = \dfrac{110 - 100}{100 \times 0{,}004} = \dfrac{10}{0{,}4} = 25^\circ\text{C}$ ✓

---
