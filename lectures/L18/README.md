# L18 – Matematik i C med math.h

## Dagordning
* Standardbiblioteket `math.h`: funktioner, konstanter och länkning med `-lm`.
* Flyttal i C: `float` och `double`, samt skillnaden mot heltalstyperna från Tillämpad Elektronik.
* Potenser, rötter, logaritmer och decibel i kod.
* Trigonometriska funktioner samt omvandling mellan grader och radianer.
* Numerisk derivering och integrering.
* Komplexa tal och fasorer med `complex.h`.
* Sampling av en sinussignal – från formel till talföljd.

---

## Mål med lektionen
* Förstå skillnaden mellan heltal och flyttal i C, och kunna välja rätt typ och formatspecificerare.
* Kunna använda `math.h` för att beräkna potenser, rötter, logaritmer och decibel.
* Kunna räkna med vinklar i radianer och omvandla till och från grader.
* Kunna beräkna en derivata numeriskt och jämföra med den analytiska derivatan.
* Kunna beräkna en bestämd integral numeriskt med trapetsmetoden.
* Kunna representera komplexa tal och fasorer med `complex.h` samt beräkna belopp och argument.
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
* **Frivilligt:** den som hellre vill köra koden lokalt kan sätta upp **WSL** med `gcc`, se [`code/`](./code/README.md#kompilering-på-egen-dator-frivilligt). Det behövs inte för lektionen, men miljön används i senare kurser.

Ingen hårdvara krävs – all kod skrivs och körs i webbläsaren.

---

## Instruktioner

### Innan lektionen
* Läs igenom kursmaterialet i [bilaga A](./appendix/a_theory.md).
* **Genomför handberäkningarna för samtliga uppgifter i del 1–3** i [bilaga B](./appendix/b_exercises.md), och ta med dem till lektionen.
* Öppna <https://www.onlinegdb.com/online_c_compiler>, kontrollera att språket är inställt på **C** och tryck på **Run**. Exempelprogrammet ska skriva ut `Hello World`.

> **OBS!** Handberäkningarna ska vara gjorda **före** lektionen. Lektionstiden räcker inte till både beräkning och programmering, och beräkningarna krävs för att bli godkänd. Den som kommer oförberedd hinner inte klara laborationen.

### Under lektionen
* Närvara under genomgången.
* Genomför uppgifterna i [bilaga B](./appendix/b_exercises.md):
    * Del 1–3 är obligatoriska. Del 4 är frivillig fördjupning.
    * Handberäkningarna ska redan vara gjorda. Under lektionen skrivs koden, och resultaten jämförs med era beräkningar.
    * Lösningsförslag finns i [bilaga C](./appendix/c_solutions.md).
* Samla uppgifterna i ett OnlineGDB-projekt med en fil per uppgift, se [bilaga B](./appendix/b_exercises.md). Kopiera filerna till egen dator innan ni stänger fliken.

---

## Demonstration
Genomgången sker som **live-kodning** i OnlineGDB. Programmet byggs ut stegvis i samma fil, där varje steg läggs till som en egen funktion som anropas från `main()`. Stegen följer typexemplen i [bilaga A](./appendix/a_theory.md); lektionsuppgifterna använder andra värden.

Räkna med cirka fem minuter per steg.

### 1. Grundfunktioner och felsökning
* **Visas:** Skillnaden mellan `int` och `double`, följt av parallellresistansen för $R_1 = 100\ \Omega$ och $R_2 = 400\ \Omega$ samt effekten $P = \dfrac{U^2}{R_p}$ vid $U = 10$ V, med `pow()` och `sqrt()`.
* **Felsökning:** `undefined reference to 'sqrt'`, `%d` i stället för `%f`, samt heltalsdivisionen `1 / 2`.
* **Frågeställning:** Vad skiljer `1 / 2` från `1.0 / 2.0`, och varför spelar det roll här?
* **Koppling:** L01 samt bilaga A §1–3 och §11.

### 2. Grader och radianer
* **Visas:** `sin(30)` jämfört med `sin(30.0 * PI / 180.0)`.
* **Frågeställning:** Varför ger `sin(30)` inte $0{,}5$? Vilken vinkel räknar funktionen egentligen med?
* **Koppling:** L09 samt bilaga A §4.

### 3. Decibel
* **Visas:** Förstärkningen för $U_{\text{in}} = 0{,}5$ V och $U_{\text{ut}} = 8{,}0$ V med `log10()`, samt vägen tillbaka från dB till spänningskvot med `pow()`.
* **Frågeställning:** Hur många dB motsvarar en fördubbling av spänningen?
* **Koppling:** L10 samt bilaga A §5.

### 4. Numerisk derivering
* **Visas:** Centraldifferensen för $f(x) = x^2$ i $x = 3$, jämförd med den analytiska derivatan $f'(x) = 2x$. Beräkningen körs med $h = 10^{-2}$, $h = 10^{-6}$ och $h = 10^{-12}$, och felet skrivs ut för varje $h$.
* **Frågeställning:** Varför blir resultatet sämre både när $h$ är för stort och när det är för litet?
* **Koppling:** L12–L13 samt bilaga A §6. Förbereder uppgift 2.1.

### 5. Numerisk integrering
* **Visas:** Trapetsmetoden på $i(t) = 2t + 4$ över $0 \leq t \leq 2$, som ger exakt $12$ C. Därefter samma metod på $f(x) = x^2$ över $0 \leq x \leq 3$, där resultatet **inte** blir exakt, och där felet minskar när $n$ ökas.
* **Frågeställning:** Varför blir resultatet exakt för $i(t)$ men inte för $x^2$?
* **Koppling:** L14 samt bilaga A §7. Förbereder uppgift 2.3–2.4.

### 6. Komplexa tal och impedans
* **Visas:** Impedansen $Z = R + j\omega L$ för $R = 100\ \Omega$ och $L = 50$ mH vid $f = 50$ Hz, samt $|Z|$ och $\arg(Z)$ med `cabs()` och `carg()`, med argumentet omvandlat till grader.
* **Felsökning:** `printf()` kan inte skriva ut ett komplext tal direkt – real- och imaginärdel måste skrivas ut var för sig.
* **Frågeställning:** Vad innebär det att argumentet är positivt? Vad hade hänt om spolen byttes mot en kondensator?
* **Koppling:** L15–L17 samt bilaga A §8–9. Förbereder uppgift 3.3.

### 7. Sampling av en sinussignal
* **Visas:** Signalen $u(t) = 5\sin(2\pi \cdot 50t)$ samplas med $f_s = 400$ Hz. Loopen skriver ut de $N = 8$ sampelvärdena som CSV, varefter utskriften kopieras till ett kalkylprogram och ritas upp som ett diagram.
* **Frågeställning:** Vad händer med kurvan om $f_s$ sänks mot $2f$?
* **Koppling:** L09 samt bilaga A §10. Förbereder uppgift 4.1.

---

## Redovisning
Uppgifterna redovisas för läraren i klassrummet under lektionen:
* **Handberäkningarna** för respektive uppgift, gjorda före lektionen och medtagna till den (handskrivna eller digitala, med tydliga steg).
* **Koden**: OnlineGDB-projektet med en fil per uppgift, som ska vara körbart och kommenterat. Samtliga uppgifter ska köras med en enda tryckning på **Run**.
* En jämförelse mellan handberäknat och beräknat resultat, med motivering av eventuella avvikelser.

---

## Bedömning
Laborationen bedöms **U/G** och påverkar inte kursens betygspoäng. Den ingår i kravet att samtliga lärandemål ska vara uppnådda för godkänt betyg på kursen.

| Krav | Bedömning |
|------|-----------|
| Del 1–3 genomförda och korrekt redovisade | G |
| Del 1–3 ej genomförda eller ej redovisade | U |

Del 4 är frivillig fördjupning och påverkar inte bedömningen.

---

## Utvärdering
* Vad blir resultatet av `1 / 2` i C, och varför?
* Vad gör flaggan `-lm`, och vilket felmeddelande får man om matematikbiblioteket inte länkas?
* Varför ger `sin(30)` inte $0{,}5$?
* Hur beräknas derivatan av $f(x)$ i punkten $x$ numeriskt, och vad styr noggrannheten?
* Hur beräknas beloppet och argumentet för ett komplext tal i C?

---

## Nästa lektion
* Repetition och tentamensförberedelse (L19).

---
