# L18 – Lektionsuppgifter

Uppgifterna löses i två steg:
1. **Räkna för hand** och skriv ned mellanstegen. Detta görs **före lektionen**.
2. **Skriv ett program i C** som utför samma beräkning och jämför resultaten. Detta görs under lektionen.

> **OBS!** Handberäkningarna för del 1–3, samt uppgift 6.1, 6.4 a, 7.1 och 7.4, ska vara gjorda före lektionen och tas med dit. Lektionstiden räcker inte till både beräkning och programmering.

Koden skrivs och körs i **OnlineGDB**: <https://www.onlinegdb.com/online_c_compiler>. Kontrollera att språket är inställt på **C** och tryck på **Run**. Ingen installation krävs.

Vid felmeddelandet `undefined reference to 'sqrt'` saknas matematikbiblioteket. Lägg då till `-lm` under **Extra Compiler Flags** i inställningarna (kugghjulet).

Skriv ut flyttal med tre decimaler, exempelvis `printf("R = %.3f ohm\n", r);`.

**OBS!** Koden sparas inte automatiskt. Kopiera den till en egen fil innan ni stänger fliken.

Del 1–3 är obligatoriska och bedöms **U/G**, liksom handberäkningarna i uppgift 6.1, 6.4 a, 7.1 och 7.4. Övriga uppgifter i del 4–7 är frivillig fördjupning för den som hinner, och påverkar inte bedömningen.

---

## Arbetssätt – en fil per uppgift
Samtliga uppgifter samlas i **ett och samma OnlineGDB-projekt**, med en fil per uppgift:

```text
assignment1_1.c   assignment2_1.c   assignment3_1.c
assignment1_2.c   assignment2_2.c   assignment3_2.c
assignment1_3.c   assignment2_3.c   assignment3_3.c
main.c
```

Nya filer skapas med knappen **New file** i verktygsfältet, eller med `Ctrl + M`.

**OBS!** OnlineGDB kompilerar och länkar samtliga filer i projektet tillsammans. Därför får endast **en** fil innehålla `main()`. Varje uppgift skrivs i stället som en egen funktion, med samma namn som filen:

```c
/* assignment1_1.c */
#include <stdio.h>

void assignment1_1(void)
{
    printf("--- Uppgift 1.1 ---\n");
    /* Er kod här. */
}
```

I `main.c` deklareras uppgifterna överst och anropas sedan i tur och ordning. Lägg till en rad per uppgift allteftersom ni blir klara – en funktion som deklareras men inte finns ger ett länkfel:

```c
/* main.c */
void assignment1_1(void);
void assignment1_2(void);

int main(void)
{
    assignment1_1();
    assignment1_2();
    return 0;
}
```

Vid redovisningen räcker det då att trycka på **Run** en gång: samtliga uppgifter körs och skriver ut sina resultat i ordning.

**OBS!** Projektet sparas inte automatiskt. Kopiera filerna till egen dator innan ni stänger fliken.

### Arbeta i WSL (rekommenderat)
Katalogen [`code/math/`](../code/math/) är ett exempel på hur ett projekt kan se ut i WSL. Den består av två filer:

| Fil | Innehåll |
|-----|----------|
| [`main.c`](../code/math/main.c) | Ett litet exempelprogram som dividerar två tal och skriver ut kvoten. |
| [`Makefile`](../code/math/Makefile) | Bygger och kör programmet med `make`. |

Hämta koden genom att klona kursens repository till er Linux-hemkatalog. Gå sedan in i katalogen och bygg och kör exemplet:

```bash
cd ~
git clone https://github.com/Yrgo-26/electrical-engineering-math.git
cd electrical-engineering-math/lectures/L18/code/math
make
```

Klonen innehåller även koden till del 6 och 7, så den behöver bara hämtas en gång.

Använd sedan katalogen som utgångspunkt för uppgifterna. Ersätt exemplet i `main.c` med deklarationerna och anropen av uppgifterna enligt ovan, och lägg till varje ny fil under `SRC_FILES` i makefilen, en fil per rad:

```makefile
SRC_FILES := assignment1_1.c \
             assignment1_2.c \
             main.c \
```

En fil som inte står under `SRC_FILES` kompileras inte, och anropet av dess funktion ger då ett länkfel. Mer om WSL och make finns i [`code/README.md`](../code/README.md#kompilering-på-egen-dator-rekommenderat).

---

## Del 1 – Grunder i math.h

### 1.1 – Resistans och effekt
Två resistorer, $R_1 = 220\ \Omega$ och $R_2 = 330\ \Omega$, parallellkopplas över spänningen $U = 12$ V.

**a)** Beräkna parallellresistansen $R_p$.

**b)** Beräkna strömmen $I$ och den utvecklade effekten $P = \dfrac{U^2}{R_p}$.

**c)** Skriv ett program som beräknar $R_p$, $I$ och $P$. Använd `pow()` för kvadreringen.

**d)** Utöka programmet så att det även beräknar den spänning som krävs för att effekten ska bli $2{,}0$ W, enligt $U = \sqrt{P R_p}$.

---

### 1.2 – Decibel
En förstärkare har inspänningen $U_{\text{in}} = 25$ mV och utspänningen $U_{\text{ut}} = 1{,}6$ V.

**a)** Beräkna förstärkningen i dB.

**b)** Ett filter dämpar signalen med $-3$ dB. Beräkna kvoten $U_{\text{ut}}/U_{\text{in}}$ för filtret.

**c)** Skriv ett program som beräknar båda värdena med `log10()` respektive `pow()`.

---

### 1.3 – Vinklar och trigonometri
En växelspänning ges av $u(t) = 325\sin(2\pi \cdot 50t)$ V.

**a)** Beräkna $u(t)$ vid $t = 2{,}0$ ms.

**b)** Ange vinkeln $2\pi \cdot 50t$ i både radianer och grader vid denna tidpunkt.

**c)** Skriv ett program som beräknar $u(t)$ för $t = 0$, $2{,}0$ ms, $5{,}0$ ms och $10{,}0$ ms. Skriv ut tiden, vinkeln i grader och spänningen på varje rad.

**d)** Bestäm vinkeln för vektorn $\vec{v} = (-3, 4)$ med `atan2()`, i radianer och grader. Förklara varför `atan(4.0 / -3.0)` ger ett annat svar.

---

## Del 2 – Derivata och integraler

### 2.1 – Numerisk derivering
Låt $f(x) = x^3 - 2x + 1$.

**a)** Derivera $f(x)$ analytiskt och beräkna $f'(2)$.

**b)** Skriv en funktion `derivative()` som beräknar derivatan numeriskt med centraldifferensen

```math
f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}.
```

**c)** Beräkna $f'(2)$ numeriskt med $h = 10^{-2}$, $h = 10^{-6}$ och $h = 10^{-12}$. Skriv ut det absoluta felet mot det analytiska värdet för varje $h$.

**d)** Vilket $h$ ger minst fel? Förklara varför både för stora och för små värden på $h$ ger sämre resultat.

---

### 2.2 – Spänning över en spole
Strömmen genom en spole ges av $i(t) = 5t^2$ A. Spolens induktans är $L = 0{,}20$ H. Spänningen över spolen ges av

```math
u(t) = L \cdot i'(t).
```

**a)** Bestäm $i'(t)$ analytiskt och därmed ett uttryck för $u(t)$.

**b)** Beräkna $u(3)$ för hand.

**c)** Skriv ett program som beräknar $u(3)$ genom att derivera $i(t)$ numeriskt, och jämför med handberäkningen.

---

### 2.3 – Numerisk integrering
Låt $f(x) = x^2$.

**a)** Beräkna $\displaystyle\int_0^3 x^2\thinspace dx$ analytiskt.

**b)** Skriv en funktion `integral()` som beräknar den bestämda integralen med trapetsmetoden:

```math
\int_a^b f(x)\,dx \approx h\left[\frac{f(a) + f(b)}{2} + \sum_{k=1}^{n-1} f(a + kh)\right], \qquad h = \frac{b - a}{n}.
```

**c)** Beräkna integralen med $n = 10$, $n = 100$ och $n = 1000$. Skriv ut det absoluta felet för varje $n$.

**d)** Hur förändras felet när $n$ tiodubblas?

---

## Del 3 – Komplexa tal och fasorer

### 3.1 – Räkning med komplexa tal
Låt $z_1 = 4 + 3j$ och $z_2 = 2 - 5j$.

**a)** Beräkna $z_1 + z_2$, $z_1 \cdot z_2$ och $\dfrac{z_1}{z_2}$ för hand.

**b)** Beräkna $|z_1|$ och $\arg(z_1)$ i radianer och grader.

**c)** Skriv ett program som utför samtliga beräkningar med `complex.h`. Skriv ut varje resultat på formen `a + bj` med hjälp av `creal()` och `cimag()`.

---

### 3.2 – Polär och rektangulär form
Ett komplext tal ges på polär form som $z = 10\thinspace\angle\thinspace\dfrac{\pi}{6}$.

**a)** Omvandla $z$ till rektangulär form för hand.

**b)** Skriv ett program som utför omvandlingen med `cexp()`, och omvandlar tillbaka med `cabs()` och `carg()`.

**c)** Kontrollera att du får tillbaka det ursprungliga talet. Varför bör resultaten jämföras med `fabs(a - b) < 1e-9` i stället för med `==`?

---

### 3.3 – Impedans i en RLC-krets
En seriekrets består av $R = 47\thinspace\Omega$, $L = 100\thinspace\text{mH}$ och $C = 10\thinspace\mu\text{F}$. Kretsen matas med $U = 230\thinspace\text{V}$ vid $f = 50\thinspace\text{Hz}$.

**a)** Beräkna $\omega$, $X_L = \omega L$ och $X_C = \dfrac{1}{\omega C}$.

**b)** Ange den totala impedansen $Z = R + j(X_L - X_C)$ på rektangulär form.

**c)** Beräkna $|Z|$ och $\arg(Z)$ i grader. Är kretsen induktiv eller kapacitiv?

**d)** Beräkna strömmens belopp $|I| = \dfrac{|U|}{|Z|}$.

**e)** Skriv ett program som beräknar allt ovanstående med `complex.h`. Låt $f$ vara en variabel, och kör programmet även för $f = 500$ Hz. Vad händer med kretsens karaktär?

---

## Del 4 – Fördjupning (frivillig)

### 4.1 – Sampling av en sinussignal
En signal ges av $u(t) = 5\sin(2\pi \cdot 50t + \dfrac{\pi}{4})$ V och samplas med $f_s = 800$ Hz.

**a)** Kontrollera att samplingsteoremet är uppfyllt.

**b)** Beräkna antalet sampel per period, $N = \dfrac{f_s}{f}$.

**c)** Beräkna sampelvärdena $u_0$, $u_1$ och $u_2$ för hand enligt

```math
u_k = |U| \sin\!\left(\frac{2\pi k}{N} + \delta\right).
```

**d)** Skriv ett program som beräknar och skriver ut samtliga $N$ sampelvärden för en period, som CSV med en rad per sampel:

```text
k,u
0,3.536
1,4.619
```

**e)** Kopiera utskriften till ett kalkylprogram och rita upp $u_k$ som funktion av $k$. Kontrollera att kurvan är sinusformad och att värdena upprepar sig efter $N$ sampel.

---

### 4.2 – Addition av fasorer
Tre spänningar med samma frekvens ges av fasorerna

```math
U_1 = 10\,\angle\,0, \qquad U_2 = 6\,\angle\,\frac{\pi}{3}, \qquad U_3 = 4\,\angle\,{-\frac{\pi}{2}}.
```

**a)** Omvandla samtliga fasorer till rektangulär form för hand.

**b)** Beräkna summan $U = U_1 + U_2 + U_3$ på rektangulär form.

**c)** Ange summan på polär form, $|U|\thinspace\angle\thinspace\delta$, med $\delta$ i både radianer och grader.

**d)** Skriv ett program som utför additionen med `complex.h` och skriver ut summan på både rektangulär och polär form.

**e)** Rita fasorerna och deras summa i det komplexa talplanet.

---

### 4.3 – Den sammansatta signalen
**a)** Skriv ett program som samplar den sammansatta signalen

```math
u(t) = u_1(t) + u_2(t) + u_3(t),
```

där varje delsignal ges av motsvarande fasor i uppgift 4.2 och samtliga har frekvensen $f = 50$ Hz.

**b)** Skriv ut sampelvärdena som CSV med $f_s = 1600$ Hz.

**c)** Kontrollera att det största sampelvärdet överensstämmer med det $|U|$ som beräknades i uppgift 4.2. Motivera eventuell avvikelse.

---

## Del 5 – Extrauppgifter (frivillig)
Uppgifterna nedan är extra träning för den som vill fördjupa sig ytterligare. De påverkar inte bedömningen. Precis som i del 1–3 görs handberäkningen först och programmet därefter.

### 5.1 – Avrundning och absolutbelopp
Betrakta talen $-2{,}7$, $3{,}2$ och $5{,}5$.

**a)** Ange för hand vad `floor()`, `ceil()` och `round()` ger för vart och ett av talen.

**b)** Skriv ett program som skriver ut alla nio värdena i en tabell.

**c)** Varför ger `round(-2.5)` värdet $-3$ och inte $-2$?

**d)** Vad är skillnaden mellan `fabs()` och `abs()`, och vilken bör användas i denna kurs?

---

### 5.2 – Toleranskontroll av resistorer
En resistor är märkt $4{,}7\ \text{k}\Omega$ ±5 %.

**a)** Beräkna det tillåtna intervallet för hand.

**b)** Skriv funktionen

```c
int within_tolerance(double nominal, double tol_percent, double measured);
```

som returnerar $1$ om det uppmätta värdet ligger inom toleransen, annars $0$.

**c)** Testa funktionen med de uppmätta värdena $4600\ \Omega$, $4950\ \Omega$ och $4465\ \Omega$.

**d)** Varför bör jämförelsen skrivas som `fabs(measured - nominal) <= nominal * tol_percent / 100.0` i stället för att jämföra mot två separata gränser?

---

### 5.3 – Serie- och parallellresistans
**a)** Beräkna för hand $R_s$ och $R_p$ för $R_1 = 100\ \Omega$ och $R_2 = 400\ \Omega$.

**b)** Skriv funktionerna `double series(double r1, double r2)` och `double parallel(double r1, double r2)`.

**c)** Skriv ett program som skriver ut båda värdena.

**d)** Utöka programmet med en funktion som beräknar parallellresistansen för $n$ motstånd i en array, via summan av $1/R$. Testa med $\lbrace 100, 400, 200 \rbrace\ \Omega$.

---

### 5.4 – Tabell över en RC-urladdning
Spänningen ges av $u(t) = 12e^{-t/\tau}$ V, där $\tau = RC$ med $R = 10\ \text{k}\Omega$ och $C = 100\ \mu\text{F}$.

**a)** Beräkna $\tau$ för hand.

**b)** Beräkna $u(0)$, $u(1)$ och $u(2)$ för hand.

**c)** Skriv ett program som med `exp()` skriver ut $u(t)$ för $t = 0$ till $5\ \text{s}$ i steg om $0{,}5\ \text{s}$.

**d)** Efter hur många tidskonstanter är spänningen under 1 % av startvärdet? Låt programmet leta upp svaret.

---

### 5.5 – Andragradsekvation med alla tre fallen
**a)** Skriv ett program som löser $ax^2 + bx + c = 0$ med hjälp av diskriminanten.

**b)** Programmet ska hantera de tre fallen $D > 0$, $D = 0$ och $D < 0$ separat.

**c)** Testa med koefficienterna $(1, -5, 6)$, $(1, -4, 4)$ och $(1, 2, 5)$. Räkna ut de förväntade svaren för hand först.

**d)** Skriv i fallet $D < 0$ ut rötterna på formen `a + bj` med hjälp av `sqrt(-D)`.

---

### 5.6 – Numerisk ekvationslösning med intervallhalvering
Sök roten till $f(x) = e^{-x} - x$ i intervallet $[0, 1]$.

**a)** Beräkna $f(0)$ och $f(1)$ för hand och visa att de har olika tecken.

**b)** Skriv en funktion `bisect()` som upprepat halverar intervallet tills dess bredd understiger $10^{-9}$.

**c)** Kör programmet. Vilket värde på roten fås?

**d)** Varför krävs det att $f(a)$ och $f(b)$ har olika tecken för att metoden ska fungera?

---

### 5.7 – Effektivvärde genom numerisk integrering
För en sinusspänning $u(t) = |U|\sin(\omega t)$ gäller

```math
U_{\text{RMS}} = \sqrt{\frac{1}{T}\int_0^T u(t)^2\,dt}.
```

**a)** Ange det teoretiska värdet på $U_{\text{RMS}}$ då $|U| = 325$ V.

**b)** Skriv ett program som beräknar integralen numeriskt med trapetsmetoden och $n = 1000$ delintervall över en period.

**c)** Jämför med det teoretiska värdet och skriv ut det relativa felet.

**d)** Vad händer med felet om $n$ minskas till $10$? Förklara varför.

---

### 5.8 – Laddning genom en ledare
Strömmen ges av $i(t) = 3t + 2$ A.

**a)** Beräkna laddningen $q = \displaystyle\int_0^4 i(t)\thinspace dt$ analytiskt.

**b)** Beräkna samma laddning numeriskt med trapetsmetoden och $n = 4$.

**c)** Varför blir det numeriska resultatet exakt i detta fall, men inte i uppgift 2.3?

---

## Del 6 – Linjär regression
Här tränas en enkel maskininlärningsmodell, en **linjär regressionsmodell**, att hitta den räta linjen $y = kx + m$ utifrån ett antal mätpunkter. Inom maskininlärning kallas $k$ för modellens **vikt** och $m$ för dess **bias**.

Ee-klassen läser senare en egen kurs i maskininlärning, och för er ger del 6 och 7 en första försmak. För Eh-klassen är detta enda tillfället att lära sig hur maskininlärning fungerar, så ta tillfället i akt! Oavsett klass visar delarna att matematiken från kursen är grunden även där.

> **OBS!** Handberäkningarna i uppgift 6.1 och 6.4 a är obligatoriska och görs före lektionen, precis som i del 1–3. De kräver ingen dator. Övriga uppgifter i del 6 är frivilliga.

Koden finns i [`code/lin_reg/`](../code/lin_reg/) och består av fyra filer:

| Fil | Innehåll |
|-----|----------|
| [`include/ml/lin_reg.h`](../code/lin_reg/include/ml/lin_reg.h) | Struktarna för modellen, träningsdatan och träningsparametrarna, samt funktionsdeklarationerna. |
| [`source/ml/lin_reg.c`](../code/lin_reg/source/ml/lin_reg.c) | Implementationen av modellen. Funktionen `lin_reg_optimize()` är tom och ska implementeras av er. |
| [`source/main.c`](../code/lin_reg/source/main.c) | Huvudprogrammet, där träningsdatan och träningsparametrarna definieras. |
| [`include/ml/utils.h`](../code/lin_reg/include/ml/utils.h) | Hjälpmakron, bland annat för att beräkna antalet element i en array. |

> **OBS!** Programmeringsuppgifterna i del 6 kräver **WSL** med `gcc` och `make`, och kan inte genomföras i OnlineGDB. Programmet består av flera filer i underkataloger och byggs med en makefile. Följ instruktionerna för att sätta upp WSL i [`code/README.md`](../code/README.md#kompilering-på-egen-dator-rekommenderat) innan ni börjar.

Gå in i katalogen i er klon av kursens repository, se [Arbeta i WSL](#arbeta-i-wsl-rekommenderat), och bygg och kör programmet med `make`:

```bash
cd ~/electrical-engineering-math/lectures/L18/code/lin_reg
make
```

Utan någon implementation i `lin_reg_optimize()` tränas modellen inte alls, så samtliga prediktioner blir $0$ tills uppgift 6.2 är genomförd.

### Struktar i C
En **strukt** (`struct`), även kallat struktur, samlar flera variabler som hör ihop under ett gemensamt namn. Modellen består till exempel av två flyttal:

```c
typedef struct
{
    double bias;   // m-värdet.
    double weight; // k-värdet.
} lin_reg_t;
```

En variabel av typen `lin_reg_t` skapas och initieras som en vanlig variabel, och fälten nås med punkt:

```c
lin_reg_t model = {.bias = 0.0, .weight = 0.0};
printf("k = %.3f, m = %.3f\n", model.weight, model.bias);
```

När strukten i stället nås via en **pekare**, som i funktionerna i `lin_reg.c`, används pil: `self->bias` och `self->weight`.

### Träningsalgoritmen
Modellen tränas genom att gå igenom mätpunkterna, de så kallade **träningsuppsättningarna** $(x,\ y_{\text{ref}})$, en i taget. En genomgång av samtliga träningsuppsättningar kallas en **epok**. Båda parametrarna är noll vid start.

För varje träningsuppsättning:

**1.** Beräkna modellens prediktion $y_p$ för indatan $x$:

```math
y_p = k \cdot x + m
```

**2.** Beräkna avvikelsen $\delta$ mellan referensvärdet och prediktionen:

```math
\delta = y_{\text{ref}} - y_p
```

Är $\delta > 0$ är prediktionen för låg, och $k$ och $m$ bör ökas. Är $\delta < 0$ är den för hög, och $k$ och $m$ bör minskas.

**3.** Beräkna justeringsmängden $\Delta e$, där $LR$ är **lärhastigheten** (*learning rate*), ett litet tal som avgör hur kraftigt parametrarna justeras:

```math
\Delta e = \delta \cdot LR
```

**4.** Justera parametrarna:

```math
m = m + \Delta e
```

```math
k = k + \Delta e \cdot x
```

Notera att $k$ inte justeras när $x = 0$, eftersom $k$ inte påverkar prediktionen då. Ju större $x$ är, desto mer justeras $k$.

---

### 6.1 – Träning för hand (obligatorisk)
Träningsdatan i `main.c` följer linjen $y = 2x + 2$:

| $x$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|-----|-----|-----|-----|-----|-----|
| $y_{\text{ref}}$ | $2$ | $4$ | $6$ | $8$ | $10$ |

**a)** Genomför en epok för hand med lärhastigheten $LR = 0{,}1$, med start i $k = 0$ och $m = 0$. Redovisa $y_p$, $\delta$, $\Delta e$, $k$ och $m$ efter varje träningsuppsättning. Avrunda till fyra decimaler.

**b)** Har $k$ och $m$ närmat sig de rätta värdena $k = 2$ och $m = 2$?

---

### 6.2 – Implementera optimeringen (frivillig)
**a)** Implementera funktionen `lin_reg_optimize()` i `lin_reg.c` enligt träningsalgoritmen ovan. Kommentarerna i funktionen beskriver stegen.

**b)** Sätt antalet epoker till $1$ och lärhastigheten till $0{,}1$ i `main.c`. Skriv ut `model.weight` och `model.bias` efter träningen och jämför med er handberäkning i uppgift 6.1.

**c)** Återställ antalet epoker till $50$ och lärhastigheten till $0{,}25$. Predikterar modellen nu $y = 2x + 2$?

---

### 6.3 – Lärhastighet och epoker (frivillig)
**a)** Träna modellen med lärhastigheten $0{,}01$ under $50$ epoker. Hur nära de rätta värdena hamnar $k$ och $m$? Hur många epoker krävs för att komma lika nära som i uppgift 6.2 c)?

**b)** Träna modellen med lärhastigheten $0{,}5$. Vad händer? Förklara varför en för hög lärhastighet gör att modellen inte hittar linjen.

**c)** Multiplicera samtliga $x$-värden med $10$ och samtliga $y$-värden enligt $y = 2x + 2$, alltså $x = 0, 10, \ldots, 40$. Träna med lärhastigheten $0{,}1$. Vad händer, och varför? Ledning: se steg 4 i träningsalgoritmen.

---

### 6.4 – Egen träningsdata
I L08, uppgift 2.6, mättes spänningen $U(t)$ under en urladdning:

| $t$ (s) | $0$ | $1$ | $2$ | $3$ | $4$ |
|---------|-----|-----|-----|-----|-----|
| $U(t)$ (V) | $12$ | $9$ | $6$ | $3$ | $0$ |

**a)** *(Obligatorisk.)* Bestäm $k$ och $m$ i $U(t) = kt + m$ för hand, eller hämta dem från er lösning i L08.

**b)** *(Frivillig, även c–e.)* Ersätt träningsdatan i `main.c` med tabellen ovan. Välj antal epoker och lärhastighet så att modellen hittar $k$ och $m$ med minst tre korrekta decimaler.

**c)** Låt modellen prediktera $U(5)$. Stämmer svaret med er beräkning i L08?

**d)** Ändra mätvärdena något, till exempel till $12{,}2$, $8{,}9$, $6{,}1$, $2{,}8$ och $0{,}1$, och träna om modellen med lärhastigheten $0{,}25$ under $50$ epoker. Varför blir $k$ och $m$ inte längre exakt $-3$ och $12$?

**e)** Träna om modellen med lärhastigheten $0{,}01$ under $1000$ epoker och jämför $k$ och $m$ med d). Varför spelar lärhastigheten roll när mätvärdena inte ligger på en rät linje? Ledning: modellen justeras efter varje träningsuppsättning, inte efter hela epoken.

---

### 6.5 – Precision (frivillig)
Hur väl modellen passar träningsdatan kan anges med medelabsolutfelet (MAE), alltså medelvärdet av absolutbeloppen av avvikelserna:

```math
\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_{\text{ref},i} - y_{p,i}|
```

Modellens **precision** definieras här som $1 - \text{MAE}$. En precision nära $1$ innebär att modellen predikterar mycket nära referensvärdena.

**a)** Skriv en funktion som beräknar precisionen för en tränad modell. Använd `fabs()` från `math.h`.

**b)** Skriv ut precisionen efter varje epok. Hur förändras den under träningen?

**c)** Avbryt träningen så snart precisionen överstiger $0{,}9999$. Efter hur många epoker sker det?

---

## Del 7 – Ett neuralt nätverk i C++
Den linjära regressionsmodellen i del 6 är i själva verket en **nod** med en enda insignal. I ett **neuralt nätverk** har varje nod flera insignaler, var och en med en egen vikt, och noderna är ordnade i **lager**. I ett så kallat **dense-lager** är varje nod kopplad till samtliga insignaler.

I del 7 tränas ett neuralt nätverk att lära sig ett mönster som ingen rät linje kan beskriva. Nätverket är skrivet i **C++**, som Ee-klassen läser i en senare kurs. Ni behöver inte förstå hela koden: målet är att ni implementerar en central del av nätverket själva och sedan ser det lära sig.

> **OBS!** Handberäkningarna i uppgift 7.1 och 7.4 är obligatoriska och görs före lektionen. De kräver ingen dator. Övriga uppgifter i del 7 är frivilliga.

> **OBS!** Programmeringsuppgifterna i del 7 kräver, precis som i del 6, **WSL** med `g++` och `make`. Båda ingår i paketet `build-essential`, se [`code/README.md`](../code/README.md#kompilering-på-egen-dator-rekommenderat).

Koden finns i [`code/neural_network/`](../code/neural_network/). Gå in i katalogen i er klon av kursens repository och bygg och kör programmet med `make`:

```bash
cd ~/electrical-engineering-math/lectures/L18/code/neural_network
make
```

### Träningsdatan
Nätverket har två insignaler $x_1$ och $x_2$ samt en utsignal $y$. Utsignalen ska vara $1$ när insignalerna är olika, och $0$ när de är lika:

| $x_1$ | $x_2$ | $y$ |
|-------|-------|-----|
| $0$ | $0$ | $0$ |
| $0$ | $1$ | $1$ |
| $1$ | $0$ | $1$ |
| $1$ | $1$ | $0$ |

Nätverket består av två lager:
* Ett **dolt lager** med $15$ noder, som tar emot insignalerna $x_1$ och $x_2$.
* Ett **utgångslager** med en nod, som tar emot det dolda lagrets $15$ utsignaler.

Vikterna och biasvärdena får slumpmässiga startvärden och justeras sedan under träningen, på samma sätt som $k$ och $m$ i del 6.

### Feedforward
Att beräkna ett lagers utsignaler från dess insignaler kallas **feedforward**. För nod $i$ beräknas först den viktade summan $z_i$ av insignalerna plus nodens bias $b_i$:

```math
z_i = w_{i1} x_1 + w_{i2} x_2 + \cdots + b_i = \sum_j w_{ij} x_j + b_i
```

där $w_{ij}$ är vikten mellan insignal $j$ och nod $i$. Med en enda insignal blir detta $z = kx + m$, alltså samma sak som i del 6.

Summan skickas sedan genom en **aktiveringsfunktion** $f$, så att nodens utsignal blir $y_i = f(z_i)$. Nätverket använder två aktiveringsfunktioner:
* Det dolda lagret använder **ReLU**, som nollställer negativa summor: $f(z) = \max(0, z)$.
* Utgångslagret använder **tangens hyperbolicus**, som pressar ihop alla reella tal till intervallet $(-1, 1)$:

```math
\tanh(z) = \frac{e^{z} - e^{-z}}{e^{z} + e^{-z}}
```

### Koden i korthet
| Fil | Innehåll |
|-----|----------|
| [`source/main.cpp`](../code/neural_network/source/main.cpp) | Träningsdatan, nätverkets storlek samt träning och utskrift. |
| [`source/ml/dense_layer/dense.cpp`](../code/neural_network/source/ml/dense_layer/dense.cpp) | Dense-lagret. Här finns metoden `feedforward()`, som ni ska implementera. |
| [`source/ml/neural_network/shallow.cpp`](../code/neural_network/source/ml/neural_network/shallow.cpp) | Nätverket, som kopplar ihop lagren och tränar dem. |
| [`source/ml/utils.cpp`](../code/neural_network/source/ml/utils.cpp) | Aktiveringsfunktionerna och slumpmässiga startvärden. |

Några saker i C++ som skiljer sig från C:
* `ml::Matrix1d` är en `std::vector<double>`, en array som själv håller reda på sin storlek och kan ändra den. Storleken fås med `.size()`, och elementen nås med hakparenteser precis som i C, till exempel `input[j]`.
* `ml::Matrix2d` är en vektor av vektorer, alltså en tvådimensionell array. Vikterna nås med `myWeights[i][j]`.
* En **klass** fungerar som en strukt som även innehåller sina funktioner, så kallade **metoder**. Lagrets variabler, till exempel `myWeights`, `myBias` och `myOutput`, nås därför direkt inne i metoderna, utan `self->`.
* Lagrets storlek fås med metoderna `nodeCount()` och `weightCount()`, och aktiveringsfunktionen beräknas med `actFuncOutput(myActFunc, sum)`.

Läs gärna resten av koden, men det krävs inte för uppgifterna.

---

### 7.1 – Feedforward för hand (obligatorisk)
En nod har vikterna $w_1 = 0{,}5$ och $w_2 = -1$ samt biasvärdet $b = 0{,}2$.

**a)** Beräkna summan $z$ för insignalerna $(x_1, x_2) = (1, 0)$ och $(x_1, x_2) = (1, 1)$.

**b)** Beräkna nodens utsignal med ReLU för båda fallen.

**c)** Beräkna nodens utsignal med $\tanh$ för fallet $(1, 0)$. Avrunda till fyra decimaler.

---

### 7.2 – Implementera feedforward (frivillig)
**a)** Implementera metoden `feedforward()` i `dense.cpp`. Beräkna för varje nod $i$ summan $z_i$ med en inre loop över insignalerna, och spara sedan både summan $z_i$ i `myPreActOutput[i]` och utsignalen $f(z_i)$ i `myOutput[i]`. Summan behövs senare när nätverket tränas. Kommentarerna i metoden beskriver stegen.

**b)** Bygg och kör programmet. Programmet skriver ut nätverkets prediktioner före och efter träningen. Jämför dem med tabellen över träningsdatan. Har nätverket lärt sig mönstret?

**OBS!** Utan en fungerande feedforward blir samtliga prediktioner $0$, och träningen misslyckas efter flera försök.

---

### 7.3 – Experimentera (frivillig)
**a)** Kör programmet flera gånger. Varför varierar antalet epoker som krävs från gång till gång?

**b)** Minska antalet noder i det dolda lagret, `hiddenCount` i `main.cpp`, till $5$, $2$ och $1$. Vad händer med träningen?

---

### 7.4 – Varför räcker inte en rät linje? (obligatorisk)
En enda nod utan aktiveringsfunktion ger $z = w_1 x_1 + w_2 x_2 + b$, och sambandet $z = 0$ är en rät linje i $x_1 x_2$-planet. Noden kan alltså bara skilja punkter på olika sidor om en linje.

**a)** Rita de fyra punkterna $(0, 0)$, $(0, 1)$, $(1, 0)$ och $(1, 1)$ i ett koordinatsystem, och markera vilka som ska ge utsignalen $1$.

**b)** Går det att dra en enda rät linje som skiljer punkterna som ska ge $1$ från punkterna som ska ge $0$? Vad säger det om varför nätverket behöver ett dolt lager?

---
