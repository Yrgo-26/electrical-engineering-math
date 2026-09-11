# L02 – Lösningsförslag

## Del 1 – Repetitionsuppgifter
### 1.1 – Parallellkoppling av tre motstånd
$R_1 = 6\thinspace\Omega$, $R_2 = 3\thinspace\Omega$, $R_3 = 2\thinspace\Omega$

---

### Lösning

```math
\frac{1}{R_{\text{TOT}}} = \frac{1}{6} + \frac{1}{3} + \frac{1}{2}
```

Gemensam nämnare är $6$:

```math
\frac{1}{R_{\text{TOT}}} = \frac{1}{6} + \frac{2}{6} + \frac{3}{6} = \frac{6}{6} = 1
```

```math
R_{\text{TOT}} = 1\,\Omega
```

---

### 1.2 – Verkningsgrad och effekt
$\eta = 92\thinspace\char37$, $P_{\text{in}} = 500\thinspace\text{W}$

---

### Lösning
**a)**

```math
P_{\text{ut}} = \eta \times P_{\text{in}} = 0{,}92 \times 500 = 460\,\text{W}
```

**b)**

```math
P_{\text{förl}} = P_{\text{in}} - P_{\text{ut}} = 500 - 460 = 40\,\text{W}
```

---

### 1.3 – Räkneordning i kretsformel
$U_{\text{in}} = 12\thinspace\text{V}$, $R_1 = 8\thinspace\Omega$, $R_2 = 4\thinspace\Omega$

---

### Lösning

```math
U_{\text{ut}} = 12 \times \frac{4}{8 + 4} = 12 \times \frac{4}{12} = 12 \times \frac{1}{3} = 4\,\text{V}
```

---

## Del 2 – Nytt stoff
### 2.1 – Förenkling av algebraiska uttryck
**a)** $5I_1 + 3I_2 - 2I_1 + 7I_2$

**b)** $4R_1 - 3R_2 + R_1 + 5R_2 - 2R_1$

**c)** $3I^2 - 2I + 4I^2 + 5I - 1$

---

### Lösning
**a)** Sammanfatta likartade termer ($I_1$-termer och $I_2$-termer):

```math
5I_1 - 2I_1 + 3I_2 + 7I_2 = 3I_1 + 10I_2
```

**b)** Sammanfatta $R_1$-termer och $R_2$-termer:

```math
(4 + 1 - 2)R_1 + (-3 + 5)R_2 = 3R_1 + 2R_2
```

**c)** Sammanfatta $I^2$-termer, $I$-termer och konstanterna:

```math
(3 + 4)I^2 + (-2 + 5)I - 1 = 7I^2 + 3I - 1
```

**d)** Insättning av $I = 2$ i det ursprungliga uttrycket:

```math
3 \times 2^2 - 2 \times 2 + 4 \times 2^2 + 5 \times 2 - 1 = 12 - 4 + 16 + 10 - 1 = 33
```

Insättning i det förenklade uttrycket:

```math
7 \times 2^2 + 3 \times 2 - 1 = 28 + 6 - 1 = 33
```

Samma värde, alltså är förenklingen korrekt. Insättning av ett värde är ett snabbt sätt att kontrollera en förenkling.

---

### 2.2 – Distributivlagen i kretsar
$U_R = R(I_1 + I_2 + I_3)$, $R = 100\thinspace\Omega$, $I_1 = 20\thinspace\text{mA}$, $I_2 = 30\thinspace\text{mA}$, $I_3 = 50\thinspace\text{mA}$

---

### Lösning
**a)** Vi multiplicerar ut parentesen med distributivlagen:

```math
U_R = R \cdot I_1 + R \cdot I_2 + R \cdot I_3 = RI_1 + RI_2 + RI_3
```

Varje term $R \cdot I_k$ har enheten $\Omega \cdot \text{A} = \text{V}$ och representerar det spänningsfall över $R$ som orsakas av respektive grenström.

**b)** Summera strömmarna först:

```math
U_R = 100 \times (0{,}020 + 0{,}030 + 0{,}050) = 100 \times 0{,}100 = 10\,\text{V}
```

**c)** Multiplicera ut först och summera sedan:

```math
U_R = 100 \times 0{,}020 + 100 \times 0{,}030 + 100 \times 0{,}050 = 2 + 3 + 5 = 10\,\text{V}
```

Samma svar. Distributivlagen säger att ordningen inte spelar någon roll – men här är den ursprungliga formen snabbast, eftersom multiplikationen bara behöver göras en gång.

---

### 2.3 – Faktorisering
**a)** $6I + 9RI$

**b)** $P_1^2 - P_2^2$

**c)** $U^2 - 10U + 25$

**d)** $4R^2 - 1$

---

### Lösning
**a)** Gemensam faktor är $3I$:

```math
6I + 9RI = 3I(2 + 3R)
```

**b)** Konjugatregeln: $a^2 - b^2 = (a+b)(a-b)$:

```math
P_1^2 - P_2^2 = (P_1 + P_2)(P_1 - P_2)
```

**c)** Identifiera kvadrat av differens: $(U - 5)^2 = U^2 - 10U + 25$:

```math
U^2 - 10U + 25 = (U - 5)^2
```

**d)** Konjugatregeln: $(2R)^2 - 1^2$:

```math
4R^2 - 1 = (2R + 1)(2R - 1)
```

---

### 2.4 – Gemensam faktor: total effekt i en seriekrets
$R_1 = 120\thinspace\Omega$, $R_2 = 180\thinspace\Omega$, $R_3 = 200\thinspace\Omega$, $I = 50\thinspace\text{mA} = 0{,}050\thinspace\text{A}$

---

### Lösning
**a)** Alla tre termer innehåller den gemensamma faktorn $I^2$, som bryts ut:

```math
P_{\text{TOT}} = R_1I^2 + R_2I^2 + R_3I^2 = (R_1 + R_2 + R_3)I^2
```

Parentesen är kretsens totala resistans $R_{\text{TOT}}$, så uttrycket säger att $P_{\text{TOT}} = R_{\text{TOT}}I^2$.

**b)** Summera resistanserna först:

```math
R_1 + R_2 + R_3 = 120 + 180 + 200 = 500\,\Omega
```

```math
P_{\text{TOT}} = 500 \times 0{,}050^2 = 500 \times 0{,}0025 = 1{,}25\,\text{W}
```

**c)** Var för sig:

```math
P_1 = 120 \times 0{,}0025 = 0{,}30\,\text{W}, \qquad
P_2 = 180 \times 0{,}0025 = 0{,}45\,\text{W}, \qquad
P_3 = 200 \times 0{,}0025 = 0{,}50\,\text{W}
```

```math
P_1 + P_2 + P_3 = 0{,}30 + 0{,}45 + 0{,}50 = 1{,}25\,\text{W}
```

Samma svar, men den faktoriserade formen krävde bara **en** multiplikation med $I^2$ i stället för tre. Att bryta ut en gemensam faktor är alltså inte bara "snyggare" – det sparar räknearbete.

---

### 2.5 – Konjugatregeln: skillnad i effekt
$U_1 = 24\thinspace\text{V}$, $U_2 = 20\thinspace\text{V}$, $R = 8\thinspace\Omega$

---

### Lösning
**a)** Sätt in effektformeln för båda spänningarna och bryt ut $\dfrac{1}{R}$:

```math
P_1 - P_2 = \frac{U_1^2}{R} - \frac{U_2^2}{R} = \frac{U_1^2 - U_2^2}{R}
```

Täljaren är en differens av två kvadrater, så konjugatregeln ger:

```math
P_1 - P_2 = \frac{(U_1 + U_2)(U_1 - U_2)}{R}
```

**b)** Med konjugatregeln behöver vi aldrig kvadrera $24$ och $20$:

```math
P_1 - P_2 = \frac{(24 + 20)(24 - 20)}{8} = \frac{44 \times 4}{8} = \frac{176}{8} = 22\,\text{W}
```

**c)** Kontroll:

```math
P_1 = \frac{24^2}{8} = \frac{576}{8} = 72\,\text{W}, \qquad
P_2 = \frac{20^2}{8} = \frac{400}{8} = 50\,\text{W}
```

```math
P_1 - P_2 = 72 - 50 = 22\,\text{W}
```

---

### 2.6 – Kvadreringsregeln: effekt vid en strömändring
$R = 10\thinspace\Omega$, $I_0 = 2\thinspace\text{A}$, $\Delta I = 0{,}1\thinspace\text{A}$

---

### Lösning
**a)** Kvadrat av summa: $(a + b)^2 = a^2 + 2ab + b^2$:

```math
P = R(I_0 + \Delta I)^2 = R\left(I_0^2 + 2I_0\,\Delta I + \Delta I^2\right)
     = \underbrace{RI_0^2}_{P_0} + \underbrace{2RI_0\,\Delta I + R\,\Delta I^2}_{\Delta P}
```

**b)**

```math
P = 10 \times \left(2^2 + 2 \times 2 \times 0{,}1 + 0{,}1^2\right) = 10 \times (4 + 0{,}4 + 0{,}01) = 10 \times 4{,}41 = 44{,}1\,\text{W}
```

**c)** Ursprungseffekten är $P_0 = RI_0^2 = 10 \times 4 = 40\thinspace\text{W}$, alltså:

```math
\Delta P = 2RI_0\,\Delta I + R\,\Delta I^2 = 10 \times (0{,}4 + 0{,}01) = 4{,}0 + 0{,}1 = 4{,}1\,\text{W}
```

**d)** Utan den kvadratiska termen fås $\Delta P \approx 2RI_0\thinspace\Delta I = 4{,}0\thinspace\text{W}$, ett fel på $0{,}1\thinspace\text{W}$:

```math
\frac{0{,}1}{4{,}1} \approx 0{,}024 = 2{,}4\,\%
```

En strömändring på $5\thinspace\char37$ ger alltså en effektändring på drygt $10\thinspace\char37$, och den kvadratiska termen $R\thinspace\Delta I^2$ är liten så länge $\Delta I \ll I_0$. Det är därför man ofta kan räkna med enbart den linjära termen vid små ändringar.

---

### 2.7 – Effektuttryck och Ohms lag
$R = 6\thinspace\Omega$, $U = 12\thinspace\text{V}$

---

### Lösning
**a)** $P = RI^2 = R \cdot I \cdot I = (RI) \cdot I$. Eftersom Ohms lag ger $U = RI$ gäller att $RI$ representerar **spänningen** $U$ över motståndet. Alltså $P = I \cdot U$, vilket är den välkända effektformeln.

**b)** Insättning av $I = \dfrac{U}{R}$:

```math
P = RI^2 = R \cdot \left(\frac{U}{R}\right)^2 = R \cdot \frac{U^2}{R^2} = \frac{U^2}{R}
```

**c)** Ohms lag ger strömmen:

```math
I = \frac{U}{R} = \frac{12}{6} = 2\,\text{A}
```

```math
P = UI = 12 \times 2 = 24\,\text{W}
```

```math
P = RI^2 = 6 \times 2^2 = 6 \times 4 = 24\,\text{W}
```

```math
P = \frac{U^2}{R} = \frac{12^2}{6} = \frac{144}{6} = 24\,\text{W}
```

Alla tre formerna ger samma svar – de är samma formel, omskriven med algebra.

---

## Del 3 – Extrauppgifter
### 3.1 – Termer, faktorer och koefficienter
$7R^2 - 4R + 9$

---

### Lösning
**a)** Tre termer: $7R^2$, $-4R$ och $9$. Termer separeras av $+$ och $-$.

**b)** Koefficienten till $R^2$ är $7$ och koefficienten till $R$ är $-4$. Tecknet hör till koefficienten.

**c)** Konstanttermen är $9$, den enda term som saknar variabel.

**d)** Termen $7R^2$ är produkten $7 \cdot R \cdot R$, alltså faktorerna $7$ och $R^2$ (eller $7$, $R$ och $R$).

**e)** Insättning av $R = 2$:

```math
7 \times 2^2 - 4 \times 2 + 9 = 28 - 8 + 9 = 29
```

---

### 3.2 – Förenkling med parenteser
**a)** $2(3I + 4) - 3(I - 2)$

**b)** $-(U - 5) + 2(U + 1)$

**c)** $5R_1 - \left[2R_1 - (R_1 + 3)\right]$

**d)** $3(2P - 1) - 2(3P - 4)$

---

### Lösning
**a)** Multiplicera ut båda parenteserna. Observera att $-3$ multipliceras in i hela den andra parentesen:

```math
2(3I + 4) - 3(I - 2) = 6I + 8 - 3I + 6 = 3I + 14
```

**b)** Ett minustecken framför en parentes byter tecken på samtliga termer i den:

```math
-(U - 5) + 2(U + 1) = -U + 5 + 2U + 2 = U + 7
```

**c)** Arbeta inifrån och ut, precis som i räkneordningen:

```math
5R_1 - \left[2R_1 - (R_1 + 3)\right] = 5R_1 - \left[2R_1 - R_1 - 3\right] = 5R_1 - \left[R_1 - 3\right] = 4R_1 + 3
```

**d)** Här försvinner variabeln helt:

```math
3(2P - 1) - 2(3P - 4) = 6P - 3 - 6P + 8 = 5
```

Uttrycket har alltså värdet $5$ oavsett vad $P$ är.

---

### 3.3 – Multiplicera ut
**a)** $(R + 3)(R + 5)$

**b)** $(2I - 1)(I + 4)$

**c)** $(U + 2)(U - 2)$

**d)** $(3R - 2)(3R - 2)$

**e)** $2I(I + 3) - I(2I - 1)$

---

### Lösning
Varje term i den första parentesen multipliceras med varje term i den andra.

**a)**

```math
(R + 3)(R + 5) = R^2 + 5R + 3R + 15 = R^2 + 8R + 15
```

**b)**

```math
(2I - 1)(I + 4) = 2I^2 + 8I - I - 4 = 2I^2 + 7I - 4
```

**c)** Detta är konjugatregeln, mittentermerna tar ut varandra:

```math
(U + 2)(U - 2) = U^2 - 2U + 2U - 4 = U^2 - 4
```

**d)** Detta är kvadraten av en differens, $(3R - 2)^2$:

```math
(3R - 2)(3R - 2) = 9R^2 - 6R - 6R + 4 = 9R^2 - 12R + 4
```

**e)**

```math
2I(I + 3) - I(2I - 1) = 2I^2 + 6I - 2I^2 + I = 7I
```

---

### 3.4 – Kvadreringsreglerna
**a)** $(I + 4)^2$

**b)** $(R - 6)^2$

**c)** $(2U + 3)^2$

**d)** $(5 - I)^2$

---

### Lösning
**a)** $(a + b)^2 = a^2 + 2ab + b^2$ med $a = I$ och $b = 4$:

```math
(I + 4)^2 = I^2 + 8I + 16
```

**b)** $(a - b)^2 = a^2 - 2ab + b^2$ med $a = R$ och $b = 6$:

```math
(R - 6)^2 = R^2 - 12R + 36
```

**c)** Här är $a = 2U$, så $a^2 = 4U^2$ och $2ab = 2 \times 2U \times 3 = 12U$:

```math
(2U + 3)^2 = 4U^2 + 12U + 9
```

**d)** Med $a = 5$ och $b = I$:

```math
(5 - I)^2 = 25 - 10I + I^2
```

**e)** Insättning av $a = 3$ och $b = 4$:

```math
(a + b)^2 = (3 + 4)^2 = 7^2 = 49
\qquad \text{men} \qquad
a^2 + b^2 = 9 + 16 = 25
```

Skillnaden är just den dubbla produkten $2ab = 2 \times 3 \times 4 = 24$, eftersom $25 + 24 = 49$. Att "kvadrera term för term" är ett av de vanligaste algebrafelen.

---

### 3.5 – Konjugatregeln som huvudräkningstrick
**a)** $102 \times 98$

**b)** $45 \times 35$

**c)** $2{,}1 \times 1{,}9$

**d)** $51^2 - 49^2$

---

### Lösning
Tricket är att skriva båda talen som "mittvärde $\pm$ avvikelse".

**a)** $102 = 100 + 2$ och $98 = 100 - 2$:

```math
102 \times 98 = (100 + 2)(100 - 2) = 100^2 - 2^2 = 10\,000 - 4 = 9996
```

**b)** $45 = 40 + 5$ och $35 = 40 - 5$:

```math
45 \times 35 = (40 + 5)(40 - 5) = 1600 - 25 = 1575
```

**c)** $2{,}1 = 2 + 0{,}1$ och $1{,}9 = 2 - 0{,}1$:

```math
2{,}1 \times 1{,}9 = 2^2 - 0{,}1^2 = 4 - 0{,}01 = 3{,}99
```

**d)** Här används regeln åt andra hållet, som faktorisering:

```math
51^2 - 49^2 = (51 + 49)(51 - 49) = 100 \times 2 = 200
```

**e)** Faktorisera täljaren med konjugatregeln:

```math
P_1 - P_2 = \frac{(U_1 + U_2)(U_1 - U_2)}{R} = \frac{(25 + 15)(25 - 15)}{5} = \frac{40 \times 10}{5} = 80\,\text{W}
```

Kontroll: $P_1 = \dfrac{625}{5} = 125\thinspace\text{W}$ och $P_2 = \dfrac{225}{5} = 45\thinspace\text{W}$, och $125 - 45 = 80\thinspace\text{W}$.

---

### 3.6 – Faktorisera
**a)** $8R + 12$

**b)** $RI^2 + RI$

**c)** $U^2 - 49$

**d)** $I^2 + 12I + 36$

**e)** $9R^2 - 16$

**f)** $2U^2 - 8$

---

### Lösning
**a)** Gemensam faktor $4$:

```math
8R + 12 = 4(2R + 3)
```

**b)** Gemensam faktor $RI$:

```math
RI^2 + RI = RI(I + 1)
```

**c)** Konjugatregeln med $b = 7$:

```math
U^2 - 49 = (U + 7)(U - 7)
```

**d)** Kvadrat av summa, eftersom $2 \times 6 = 12$ och $6^2 = 36$:

```math
I^2 + 12I + 36 = (I + 6)^2
```

**e)** Konjugatregeln med $a = 3R$ och $b = 4$:

```math
9R^2 - 16 = (3R + 4)(3R - 4)
```

**f)** Bryt först ut den gemensamma faktorn $2$, använd sedan konjugatregeln:

```math
2U^2 - 8 = 2(U^2 - 4) = 2(U + 2)(U - 2)
```

Att först bryta ut gemensamma faktorer och sedan leta efter kvadreringsregler är en bra arbetsordning.

---

### 3.7 – Förkorta algebraiska bråk
**a)** $\dfrac{6RI}{3R}$

**b)** $\dfrac{R^2 - 9}{R + 3}$

**c)** $\dfrac{2U^2 + 4U}{2U}$

**d)** $\dfrac{I^2 - 10I + 25}{I - 5}$

**e)** $\dfrac{4R^2 - 1}{2R - 1}$

---

### Lösning
Ett bråk får bara förkortas med **faktorer**, aldrig med enskilda termer. Därför måste täljaren först faktoriseras.

**a)**

```math
\frac{6RI}{3R} = \frac{3R \cdot 2I}{3R} = 2I
```

**b)** Konjugatregeln i täljaren:

```math
\frac{R^2 - 9}{R + 3} = \frac{(R + 3)(R - 3)}{R + 3} = R - 3
```

**c)** Bryt ut $2U$ i täljaren:

```math
\frac{2U^2 + 4U}{2U} = \frac{2U(U + 2)}{2U} = U + 2
```

**d)** Täljaren är kvadraten av en differens:

```math
\frac{I^2 - 10I + 25}{I - 5} = \frac{(I - 5)^2}{I - 5} = I - 5
```

**e)** Konjugatregeln med $a = 2R$ och $b = 1$:

```math
\frac{4R^2 - 1}{2R - 1} = \frac{(2R + 1)(2R - 1)}{2R - 1} = 2R + 1
```

---

### 3.8 – Insättning i effektformlerna
$R = 8\thinspace\Omega$, $I = 1{,}5\thinspace\text{A}$

---

### Lösning
**a)**

```math
U = RI = 8 \times 1{,}5 = 12\,\text{V}
```

**b)**

```math
P = RI^2 = 8 \times 1{,}5^2 = 8 \times 2{,}25 = 18\,\text{W}
```

**c)**

```math
P = \frac{U^2}{R} = \frac{12^2}{8} = \frac{144}{8} = 18\,\text{W}
```

Samma svar, vilket de måste ge eftersom formlerna är algebraiska omskrivningar av varandra.

**d)** Sätt in $2I$ i effektformeln:

```math
P_{\text{ny}} = R(2I)^2 = R \cdot 4I^2 = 4RI^2 = 4P
```

Effekten **fyrdubblas**, alltså $4 \times 18 = 72\thinspace\text{W}$. Det är kvadraten på strömmen som gör att en dubbling av $I$ ger fyra gånger så stor effekt.

---

### 3.9 – Spänningsdelarens algebra
$U_{\text{in}} = 15\thinspace\text{V}$, $R_1 = 1\thinspace\text{k}\Omega$, $R_2 = 4\thinspace\text{k}\Omega$

---

### Lösning
**a)** Bråken har samma nämnare och kan adderas direkt. Sedan bryts $U_{\text{in}}$ ut:

```math
U_1 + U_2 = U_{\text{in}}\frac{R_1}{R_1 + R_2} + U_{\text{in}}\frac{R_2}{R_1 + R_2}
          = U_{\text{in}}\frac{R_1 + R_2}{R_1 + R_2} = U_{\text{in}}
```

Delspänningarna summerar alltså alltid till matningsspänningen.

**b)** Vid division försvinner både $U_{\text{in}}$ och den gemensamma nämnaren:

```math
\frac{U_1}{U_2} = \frac{U_{\text{in}}\frac{R_1}{R_1 + R_2}}{U_{\text{in}}\frac{R_2}{R_1 + R_2}} = \frac{R_1}{R_2}
```

Spänningarna förhåller sig som resistanserna.

**c)** Med $R_1 = R_2 = R$:

```math
U_1 = U_{\text{in}}\frac{R}{R + R} = U_{\text{in}}\frac{R}{2R} = \frac{U_{\text{in}}}{2}
```

Två lika stora motstånd delar spänningen mitt itu.

**d)**

```math
U_1 = 15 \times \frac{1}{1 + 4} = 15 \times \frac{1}{5} = 3\,\text{V}
\qquad
U_2 = 15 \times \frac{4}{1 + 4} = 15 \times \frac{4}{5} = 12\,\text{V}
```

Kontroll: $U_1 + U_2 = 3 + 12 = 15\thinspace\text{V} = U_{\text{in}}$, och $\dfrac{U_1}{U_2} = \dfrac{3}{12} = \dfrac{1}{4} = \dfrac{R_1}{R_2}$.

---

### 3.10 – Hitta felet

---

### Lösning
**a)** Den dubbla produkten $2ab$ har fallit bort. Kvadreringsregeln ger:

```math
(R + 2)^2 = R^2 + 4R + 4
```

**b)** Distributivlagen kräver att faktorn multipliceras med **båda** termerna:

```math
3(I - 2) = 3I - 6
```

**c)** Ett bråk får bara förkortas med faktorer, inte med enskilda termer. Här måste båda termerna divideras:

```math
\frac{R + 4}{4} = \frac{R}{4} + 1
```

**d)** Minustecknet framför parentesen byter tecken på **alla** termer i den:

```math
-(U - 3) = -U + 3
```

**e)** Även variablerna multipliceras med varandra:

```math
2R \times 3R = 6R^2
```

**f)** Exponenten gäller hela parentesen, alltså både $2$ och $I$:

```math
(2I)^2 = 2^2I^2 = 4I^2
```

---
