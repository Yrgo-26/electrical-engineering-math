# Boken

Kursen satt som en bok med LuaLaTeX: ett kapitel per lektion, L01–L19, med övningsduggorna och
övningstentamen där kursen använder dem, och ett facit med svaren på samtliga uppgifter längst
bak. Lösningsförslagen finns inte i boken; de publiceras i repot efter respektive lektion.

---

## Bygga boken

```bash
sudo apt -y install make texlive-luatex texlive-latex-extra texlive-lang-european \
                    fonts-texgyre fonts-texgyre-math fonts-dejavu-core poppler-utils
make -C book                   # Skriver book/elteknisk-matematik.pdf (även: make -C book sv).
make -C book VERSION=v1.1.0    # Samma sak, med versionen på titelsidan.
make -C book clean             # Tar bort book/build/ och PDF:erna.
```

`texlive-lang-european` ger den svenska avstavningen. Utan den byggs boken ändå, men avstavas då
med engelska regler.

Bygget kör LuaLaTeX två gånger (tre om sidnumren i facit flyttade sig), så att innehållsförteckningen
och korsreferenserna hinner sätta sig, skriver sedan ut de överfulla och underfulla rader och de
LaTeX-varningar det hittade, och avbryts om någon referens är odefinierad. Eftersom varje uppgift
hänvisar till sidan med sitt svar, och varje svar till sin uppgift, avbryts bygget också om en
uppgift saknar svar i facit eller ett svar saknar sin uppgift.

---

## Ge ut en ny upplaga

PDF:en är incheckad i repot, så den går att läsa direkt på GitHub. En skarp upplaga
publiceras dessutom som en release: pusha en versionstagg.

```bash
git tag v1.1.0
git push origin v1.1.0
```

[Book-arbetsflödet](../.github/workflows/book.yml) bygger då PDF:en med taggen på titelsidan och
lägger upp den i en release med samma namn.

Boken ska kunna användas i många år, så ingen sida i den nämner en klass, ett år eller ett datum;
titelsidan visar bara versionen, och bara när en anges.

---

## Vad som finns var

En katalog per utgåva, `sv/` och `en/`, med samma filer på samma sökvägar, och ovanför dem
designen som de delar:

```text
mathbook.sty            Alla visuella beslut: sida, typsnitt, färger, exempel, uppgifter, facit.
mathbook.lua            Hur \code{...} sätter C-kod i löptext (#, \n och radbrytningar).
sv/                     Den svenska utgåvan, Elteknisk matematik:
sv/book.tex               Boken: förord, 19 kapitel och facit, i ordning.
sv/front/                 Titelsidor och förord.
sv/chapters/NN/           Kapitel NN, satt från lektion LNN: chapter.tex (inledningen),
                          theory.tex (bilaga A), summary.tex (sammanfattningen, från bilaga A
                          och lektionens README) och exercises.tex (bilaga B), och i kapitel 6,
                          11 och 19 övningsduggan respektive övningstentamen.
sv/back/facit.tex         Bilagan Facit, som läser in sv/back/facit/NN.tex, ett per kapitel.
en/                     Den engelska utgåvan, Electrical Engineering Mathematics, med samma
                        filer på samma sökvägar som sv/; se nedan.
```

Varje `.tex`-fil som är satt från kursmaterial börjar med en kommentar som anger källan, till
exempel:

```tex
% Sections 1.1 to 1.5, from lectures/L01/appendix/a_theory.md.
```

---

## Uppdatera innehållet

Kursmaterialet är källan, och boken följer det. **Två sorters innehåll beter sig olika:**

* **Bilderna uppdaterar sig själva.** Boken innehåller inga egna kopior; `\bild{lectures/...}`
  läser in lektionens PNG-fil direkt, så en ändrad bild är ändrad i boken vid nästa bygge.
* **Text, formler och svar gör det inte.** Ett kapitels text är en satt kopia av lektionens
  markdown. När du ändrar i en lektions bilaga gör du samma ändring i den `.tex`-fil vars
  sidhuvud nämner den, och ändras en uppgift ändras dess svar i `sv/back/facit/NN.tex`.

Några konventioner, så att en ändring ser ut som resten av boken:

* **Formler:** `\[ ... \]` för en fristående formel, `align*` eller `gather*` för flera rader.
  Decimalkomma skrivs `4{,}7`, enheter `4{,}7\,\text{k}\Omega` och procent `30\,\%`.
  Absolutbelopp skrivs `\abs{x}` (inte `|x|`, som ger fel mellanrum kring ett minustecken),
  parallellkoppling `R_1 \parallell R_2` och grader `30^{\circ}`. Resistans skrivs före ström:
  $RI$ och $RI^2$, aldrig $I^2R$.
* **Exempel:** `\begin{exempel}[Rubrik] ... \end{exempel}` för bilagornas exempel och typexempel.
* **Rutor:** `\begin{aside}\note[Tips] ...\end{aside}` för tips och `\note[Obs]` för varningar.
* **Bilder:** `\bild[bredd]{lectures/LNN/appendix/images/NAMN.png}`.
* **Uppgifter:** `\uppgiftsdel{Del 2}{Nytt stoff}` för en del, `\uppgift{2.3}{Rubrik}` för en
  uppgift, med lektionens egen numrering. Deluppgifterna a), b), c) sätts med `parts` (`\item`)
  när de är meningar och med `delar` (`\task`, från paketet tasks) i flera spalter när de är
  korta: `\begin{delar}(4) \task $3 + 2 \times 5$ ... \end{delar}`.
* **Hänvisningar:** `\uppref{2.2}` är uppgift 2.2 i samma kapitel, `\kapref{5}` är kapitel 5 och
  `\secref{c1:sec:parallell}` är ett avsnitt. Kapitel har etiketten `cN:ch` och avsnitt
  `cN:sec:namn`.
* **Övningsprov:** `\prov{od1}` namnger provet och `\provuppgift{3}{1,0}` är uppgift 3 värd
  1,0 poäng.
* **Facit:** `\facitavsnitt{c1}{Kapitel 1}{Rubrik}`, sedan i miljön `facit` en rad
  `\svar{2.3} \sv{a} ... \sv{b} ...` per uppgift; självtestet i sammanfattningen är
  `\svar[Testa dig själv]{T}`. Facit innehåller svar, inte lösningar: där uppgiften ber om en
  motivering eller ett bevis anges slutsatsen och det avgörande skälet.

Lösningsförslagen finns inte i boken. Varje kapitels uppgifter anger var de publiceras
(`lectures/LNN/appendix/c_solutions.md`), så flyttas eller byter en lösningsfil namn behöver
`\facitnotis{LNN}` i kapitlets `exercises.tex` inte ändras, men makrot i `mathbook.sty` gör det.

---

## Den engelska utgåvan

`en/` är bokens engelska utgåva, *Electrical Engineering Mathematics*, för studenter som hellre
läser på engelska. Den delar `mathbook.sty`, `mathbook.lua` och bilderna med den svenska, och
`\usepackage[english]{mathbook}` byter rubrikerna, avstavningen och orden som makrona skriver ut
(Exercise, Example, answer p.):

```bash
make -C book en                # Skriver book/electrical-engineering-mathematics.pdf.
```

* **Varje fil i `en/` är översättningen av filen med samma sökväg i `sv/`**, till exempel
  `en/chapters/03/theory.tex` av `sv/chapters/03/theory.tex`, och dess sidhuvud säger det. Den
  svenska boken är källan för den engelska, som lektionerna är källan för den svenska: ändras ett
  kapitel på svenska ändras dess översättning likadant.
* **Makron och etiketter är desamma** (`\uppgift`, `\svar`, `exempel`, `c3:sec:olikheter`), så att
  utgåvorna kan jämföras fil för fil och korsreferenserna fungerar oförändrade.
* **Alla kapitel är översatta.** Ett kapitel som ännu inte är översatt kan stå som
  `\pendingchapter{N}` i `en/book.tex`: det behåller sitt nummer, så att kapitlen efter det behåller
  sina, och en hänvisning till det skriver ut numret utan länk. När kapitlet översätts byts raden
  mot `\input{en/chapters/NN/chapter}`, och dess svar läggs till i `en/back/facit.tex`.
* **Beteckningar:** decimalpunkt (`0.5`, inte `0{,}5`), brittisk stavning och engelska index
  (`U_{\text{out}}`, `P_{\text{out}}`). Resten är som i den svenska boken: $U$ för spänning, $j$
  för den imaginära enheten och resistans före ström.
* **Figurer med svensk text** har engelska versioner bredvid originalen, med ändelsen `_en`
  (till exempel `lectures/L03/appendix/images/2.5_circuit_en.png`), och den engelska utgåvans
  `\bild` pekar på dem. De ritas av skript med samma namn; se repots README.
* **Brittisk avstavning** kräver `texlive-lang-english`. Utan den avstavas boken med de amerikanska
  mönstren, som skiljer sig i få ord.

Den engelska utgåvan ingår inte i releasen än: `make -C book` och Book-arbetsflödet bygger bara den
svenska.

---

## Licens

Bokens text och figurer, och PDF:en som byggs från dem, är licensierade under
[CC BY 4.0](../LICENSE), liksom kursmaterialet de är satta från. C-koden i kapitel 18 får även
användas under [MIT-licensen](../lectures/L18/code/LICENSE).
