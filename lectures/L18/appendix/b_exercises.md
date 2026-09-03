# L18 – Lektionsuppgifter

Uppgifterna löses i två steg:
1. **Räkna för hand** och skriv ned mellanstegen. Detta görs **före lektionen**.
2. **Skriv ett program i C** som utför samma beräkning och jämför resultaten. Detta görs under lektionen.

> **OBS!** Handberäkningarna för del 1–3 ska vara gjorda före lektionen och tas med dit. Lektionstiden räcker inte till både beräkning och programmering.

Koden skrivs och körs i **OnlineGDB**: <https://www.onlinegdb.com/online_c_compiler>. Kontrollera att språket är inställt på **C** och tryck på **Run**. Ingen installation krävs.

Vid felmeddelandet `undefined reference to 'sqrt'` saknas matematikbiblioteket. Lägg då till `-lm` under **Extra Compiler Flags** i inställningarna (kugghjulet).

Skriv ut flyttal med tre decimaler, exempelvis `printf("R = %.3f ohm\n", r);`.

**OBS!** Koden sparas inte automatiskt. Kopiera den till en egen fil innan ni stänger fliken.

Del 1–3 är obligatoriska och bedöms **U/G**. Del 4 är frivillig fördjupning för den som hinner, och påverkar inte bedömningen.

---

## Arbetssätt – en fil per uppgift
Samtliga uppgifter samlas i **ett och samma OnlineGDB-projekt**, med en fil per uppgift:

```text
assignment1_1.c   assignment2_1.c   assignment3_1.c
assignment1_2.c   assignment2_2.c   assignment3_2.c
assignment1_3.c   assignment2_3.c   assignment3_3.c
                  assignment2_4.c   main.c
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

---

## Del 1 – Grunder i math.h

### 1.1 – Resistans och effekt
Två resistorer, $R_1 = 220\ \Omega$ och $R_2 = 330\ \Omega$, parallellkopplas över spänningen $U = 12$ V.

**a)** Beräkna parallellresistansen $R_p$.\
**b)** Beräkna strömmen $I$ och den utvecklade effekten $P = \dfrac{U^2}{R_p}$.\
**c)** Skriv ett program som beräknar $R_p$, $I$ och $P$. Använd `pow()` för kvadreringen.\
**d)** Utöka programmet så att det även beräknar den spänning som krävs för att effekten ska bli $2{,}0$ W, enligt $U = \sqrt{P R_p}$.

---

### 1.2 – Decibel
En förstärkare har inspänningen $U_{\text{in}} = 25$ mV och utspänningen $U_{\text{ut}} = 1{,}6$ V.

**a)** Beräkna förstärkningen i dB.\
**b)** Ett filter dämpar signalen med $-3$ dB. Beräkna kvoten $U_{\text{ut}}/U_{\text{in}}$ för filtret.\
**c)** Skriv ett program som beräknar båda värdena med `log10()` respektive `pow()`.

---

### 1.3 – Vinklar och trigonometri
En växelspänning ges av $u(t) = 325\sin(2\pi \cdot 50t)$ V.

**a)** Beräkna $u(t)$ vid $t = 2{,}0$ ms.\
**b)** Ange vinkeln $2\pi \cdot 50t$ i både radianer och grader vid denna tidpunkt.\
**c)** Skriv ett program som beräknar $u(t)$ för $t = 0$, $2{,}0$ ms, $5{,}0$ ms och $10{,}0$ ms. Skriv ut tiden, vinkeln i grader och spänningen på varje rad.\
**d)** Bestäm vinkeln för vektorn $\vec{v} = (-3, 4)$ med `atan2()`, i radianer och grader. Förklara varför `atan(4.0 / -3.0)` ger ett annat svar.

---

## Del 2 – Derivata och integraler

### 2.1 – Numerisk derivering
Låt $f(x) = x^3 - 2x + 1$.

**a)** Derivera $f(x)$ analytiskt och beräkna $f'(2)$.\
**b)** Skriv en funktion `derivative()` som beräknar derivatan numeriskt med centraldifferensen

```math
f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}.
```

**c)** Beräkna $f'(2)$ numeriskt med $h = 10^{-2}$, $h = 10^{-6}$ och $h = 10^{-12}$. Skriv ut det absoluta felet mot det analytiska värdet för varje $h$.\
**d)** Vilket $h$ ger minst fel? Förklara varför både för stora och för små värden på $h$ ger sämre resultat.

---

### 2.2 – Spänning över en spole
Strömmen genom en spole ges av $i(t) = 5t^2$ A. Spolens induktans är $L = 0{,}20$ H. Spänningen över spolen ges av

```math
u(t) = L \cdot i'(t).
```

**a)** Bestäm $i'(t)$ analytiskt och därmed ett uttryck för $u(t)$.\
**b)** Beräkna $u(3)$ för hand.\
**c)** Skriv ett program som beräknar $u(3)$ genom att derivera $i(t)$ numeriskt, och jämför med handberäkningen.

---

### 2.3 – Numerisk integrering
Låt $f(x) = x^2$.

**a)** Beräkna $\displaystyle\int_0^3 x^2\,dx$ analytiskt.\
**b)** Skriv en funktion `integral()` som beräknar den bestämda integralen med trapetsmetoden:

```math
\int_a^b f(x)\,dx \approx h\left[\frac{f(a) + f(b)}{2} + \sum_{k=1}^{n-1} f(a + kh)\right], \qquad h = \frac{b - a}{n}.
```

**c)** Beräkna integralen med $n = 10$, $n = 100$ och $n = 1000$. Skriv ut det absoluta felet för varje $n$.\
**d)** Hur förändras felet när $n$ tiodubblas?

---

### 2.4 – Laddning genom en ledare
Strömmen ges av $i(t) = 3t + 2$ A.

**a)** Beräkna laddningen $q = \displaystyle\int_0^4 i(t)\,dt$ analytiskt.\
**b)** Beräkna samma laddning numeriskt med trapetsmetoden och $n = 4$.\
**c)** Varför blir det numeriska resultatet exakt i detta fall, men inte i uppgift 2.3?

---

## Del 3 – Komplexa tal och fasorer

### 3.1 – Räkning med komplexa tal
Låt $z_1 = 4 + 3j$ och $z_2 = 2 - 5j$.

**a)** Beräkna $z_1 + z_2$, $z_1 \cdot z_2$ och $\dfrac{z_1}{z_2}$ för hand.\
**b)** Beräkna $|z_1|$ och $\arg(z_1)$ i radianer och grader.\
**c)** Skriv ett program som utför samtliga beräkningar med `complex.h`. Skriv ut varje resultat på formen `a + bj` med hjälp av `creal()` och `cimag()`.

---

### 3.2 – Polär och rektangulär form
Ett komplext tal ges på polär form som $z = 10\,\angle\,\dfrac{\pi}{6}$.

**a)** Omvandla $z$ till rektangulär form för hand.\
**b)** Skriv ett program som utför omvandlingen med `cexp()`, och omvandlar tillbaka med `cabs()` och `carg()`.\
**c)** Kontrollera att du får tillbaka det ursprungliga talet. Varför bör resultaten jämföras med `fabs(a - b) < 1e-9` i stället för med `==`?

---

### 3.3 – Impedans i en RLC-krets
En seriekrets består av $R = 47\ \Omega$, $L = 100$ mH och $C = 10\ \mu$F. Kretsen matas med $U = 230$ V vid $f = 50$ Hz.

**a)** Beräkna $\omega$, $X_L = \omega L$ och $X_C = \dfrac{1}{\omega C}$.\
**b)** Ange den totala impedansen $Z = R + j(X_L - X_C)$ på rektangulär form.\
**c)** Beräkna $|Z|$ och $\arg(Z)$ i grader. Är kretsen induktiv eller kapacitiv?\
**d)** Beräkna strömmens belopp $|I| = \dfrac{|U|}{|Z|}$.\
**e)** Skriv ett program som beräknar allt ovanstående med `complex.h`. Låt $f$ vara en variabel, och kör programmet även för $f = 500$ Hz. Vad händer med kretsens karaktär?

---

## Del 4 – Fördjupning (frivillig)

### 4.1 – Sampling av en sinussignal
En signal ges av $u(t) = 5\sin(2\pi \cdot 50t + \dfrac{\pi}{4})$ V och samplas med $f_s = 800$ Hz.

**a)** Kontrollera att samplingsteoremet är uppfyllt.\
**b)** Beräkna antalet sampel per period, $N = \dfrac{f_s}{f}$.\
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

**a)** Omvandla samtliga fasorer till rektangulär form för hand.\
**b)** Beräkna summan $U = U_1 + U_2 + U_3$ på rektangulär form.\
**c)** Ange summan på polär form, $|U|\,\angle\,\delta$, med $\delta$ i både radianer och grader.\
**d)** Skriv ett program som utför additionen med `complex.h` och skriver ut summan på både rektangulär och polär form.\
**e)** Rita fasorerna och deras summa i det komplexa talplanet.

---

### 4.3 – Den sammansatta signalen
**a)** Skriv ett program som samplar den sammansatta signalen

```math
u(t) = u_1(t) + u_2(t) + u_3(t),
```

där varje delsignal ges av motsvarande fasor i uppgift 4.2 och samtliga har frekvensen $f = 50$ Hz.

**b)** Skriv ut sampelvärdena som CSV med $f_s = 1600$ Hz.\
**c)** Kontrollera att det största sampelvärdet överensstämmer med det $|U|$ som beräknades i uppgift 4.2. Motivera eventuell avvikelse.

---
