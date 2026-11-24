# L18 – Matematik i C med math.h

## Dagordning
* Standardbiblioteket `math.h`: funktioner och konstanter.
* Flyttal i C: `float` och `double`, samt skillnaden mot heltalstyperna från Tillämpad Elektronik.
* Potenser, rötter, logaritmer och decibel i kod.
* Trigonometriska funktioner samt omvandling mellan grader och radianer.
* Numerisk derivering och integrering.
* Komplexa tal och fasorer i C, med real- och imaginärdelen som två variabler.
* Sampling av en sinussignal: från formel till talföljd.

---

## Mål med lektionen
* Förstå skillnaden mellan heltal och flyttal i C, och kunna välja rätt typ och formatspecificerare.
* Kunna använda `math.h` för att beräkna potenser, rötter, logaritmer och decibel.
* Kunna räkna med vinklar i radianer och omvandla till och från grader.
* Kunna beräkna en derivata numeriskt och jämföra med den analytiska derivatan.
* Kunna beräkna en bestämd integral numeriskt med trapetsmetoden.
* Kunna räkna med komplexa tal och fasorer i C samt beräkna belopp och argument med `sqrt()` och `atan2()`.
* Kunna beräkna sampelvärden för en sinussignal och skriva ut dem för vidare analys.

---

## Förutsättningar

### Förkunskaper
* Genomgång av L01–L17, särskilt:
    * Potenser, rötter och logaritmer (L05, L10).
    * Trigonometriska funktioner (L09).
    * Derivata (L12–L13) och integraler (L14).
    * Komplexa tal och fasorer (L15–L17).
* Grundläggande C-programmering: variabler, funktioner, `printf()` och loopar. Inga förkunskaper om flyttal krävs – `float` och `double` gås igenom på lektionen.

### Mjukvara
* **OnlineGDB** – en C-kompilator som körs direkt i webbläsaren: <https://www.onlinegdb.com/online_c_compiler>.
* Ingen installation krävs, och inget konto behövs. Se [`code/`](./code/README.md) för detaljer.
* **Rekommenderat:** sätt upp **WSL** med `gcc` och kör koden lokalt, se [`code/`](./code/README.md#kompilering-på-egen-dator-rekommenderat). Miljön används i senare kurser, så det lönar sig att sätta upp den redan nu. Den krävs för programmeringsuppgifterna i del 6 och 7, men inte för del 1–5, där OnlineGDB räcker.

Ingen hårdvara krävs; all kod skrivs och körs i webbläsaren.

---

## Instruktioner

### Innan lektionen
* Läs igenom kursmaterialet i [bilaga A](./appendix/a_theory.md) eller kapitel 18 i boken ([svenska](../../book/elteknisk-matematik.pdf) eller [engelska](../../book/electrical-engineering-mathematics.pdf)).
* **Gör gärna handberäkningarna nedan före lektionen** och ta med dem dit. Det rekommenderas starkt, men är inget krav. Samtliga uppgifter finns samlade i [`hand_calculations.md`](./appendix/hand_calculations.md):
    * **1.1 a–b:** parallellresistansen $R_p$, strömmen $I$ och effekten $P$.
    * **1.2 a–b:** förstärkningen i dB och spänningskvoten vid $-3$ dB.
    * **1.3 a–b:** $u(t)$ vid $t = 2{,}0$ ms samt vinkeln i radianer och grader.
    * **2.1 a:** $f'(x)$ och $f'(2)$.
    * **2.2 a–b:** $i'(t)$, $u(t)$ och $u(3)$.
    * **2.3 a:** $\int_0^3 x^2\,dx$.
    * **3.1 a–b:** $z_1 + z_2$, $z_1 \cdot z_2$, $\frac{z_1}{z_2}$ samt $|z_1|$ och $\arg(z_1)$.
    * **3.2 a:** $z$ på rektangulär form.
    * **3.3 a–d:** $\omega$, $X_L$, $X_C$, $Z$, $|Z|$, $\arg(Z)$ och $|I|$.
    * **6.1 a–b:** en epok av träningen för hand.
    * **6.4 a:** $k$ och $m$ i $U(t) = kt + m$.
    * **7.1 a–c:** nodens summa $z$ och utsignal med ReLU och $\tanh$.
    * **7.4 a–b:** rita de fyra punkterna och förklara varför en rät linje inte räcker.
* Öppna <https://www.onlinegdb.com/online_c_compiler>, kontrollera att språket är inställt på **C** och tryck på **Run**. Exempelprogrammet ska skriva ut `Hello World`.

> **OBS!** Det rekommenderas starkt att handberäkningarna görs före lektionen: görs de under lektionen ska både beräkning och programmering hinnas med, vilket kan bli stressigt.

### Under lektionen
* Närvara under genomgången.
* Genomför uppgifterna i [bilaga B](./appendix/b_exercises.md):
    * Del 1–3 samt handberäkningarna i uppgift 6.1, 6.4 a, 7.1 och 7.4 är laborationens grunduppgifter. Övriga uppgifter i del 4–7 är frivillig fördjupning, där del 6 tränar en linjär regressionsmodell och del 7 tränar ett neuralt nätverk i C++. Programmeringsuppgifterna i del 6 och 7 kräver **WSL**, se [`code/`](./code/README.md#kompilering-på-egen-dator-rekommenderat).
    * Har ni gjort handberäkningarna i förväg kan lektionen läggas på koden, och resultaten jämförs med era beräkningar. Annars görs handberäkningarna först.
    * Lösningsförslag finns i [bilaga C](./appendix/c_solutions.md).
* Samla uppgifterna i ett OnlineGDB-projekt med en fil per uppgift, se [bilaga B](./appendix/b_exercises.md). Kopiera filerna till egen dator innan ni stänger fliken.

---

## Demonstration
Genomgången är kort, högst cirka fem minuter, så att lektionstiden kan läggas på uppgifterna. Den visar i OnlineGDB bara de vanligaste fallgroparna:
* `1 / 2` jämfört med `1.0 / 2.0`: heltalsdivision ger `0`.
* `%d` i stället för `%f` vid utskrift av en `double`.
* `sin(30)` jämfört med `sin(30.0 * PI / 180.0)`: de trigonometriska funktionerna räknar i radianer.

Övrigt stoff, med typexempel för grader och radianer, decibel, numerisk derivering och integrering, komplexa tal och sampling, finns i [bilaga A](./appendix/a_theory.md).

---

## Bedömning
Laborationen bedöms inte och ingår inte i kraven för kursbetyget, som avgörs av tentamen. Den är ett tillfälle att se hur matematiken från kursen används i kod, med stöd av läraren. Visa gärna läraren vad ni har gjort och ställ frågor under lektionen.

**Grupparbete och AI.** Ni får gärna arbeta i grupper om två. AI-verktyg får användas som hjälpmedel, men skriv koden själva i stället för att klistra in den: det är så ni lär er.

---

## Utvärdering
* Vad blir resultatet av `1 / 2` i C, och varför?
* Varför ger `sin(30)` inte $0{,}5$?
* Hur beräknas derivatan av $f(x)$ i punkten $x$ numeriskt, och vad styr noggrannheten?
* Hur beräknas beloppet och argumentet för ett komplext tal i C?

---

## Nästa lektion
* Repetition och tentamensförberedelse (L19).

---
