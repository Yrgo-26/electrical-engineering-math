# Elteknisk matematik - Ee26 och Eh26
Kursrepo för `Elteknisk matematik` med klasserna Ee26 samt Eh26, ht26.

## Om kursen
Kursen behandlar den matematik som används inom elektroteknik, med fokus på:
* Aritmetik, algebra samt linjära ekvationer och ekvationssystem.
* Potenser, rötter, andragradsekvationer samt exponentialfunktioner och logaritmer (inklusive decibel).
* Vektorer, funktioner och trigonometriska funktioner.
* Derivata och integraler, samt tillämpningar inom kretsteori.
* Komplexa tal på rektangulär, polär och Eulerform, samt fasorer för växelströmsberäkningar.

Under kursens gång tillämpas matematiken bland annat på:
* Parallell- och seriekopplade motstånd, spänningsdelare samt effektberäkningar.
* Upp- och urladdning av kondensatorer i RC-kretsar.
* Växelspänningar: amplitud, frekvens, fas och sinusekvationer.
* Impedansberäkningar med komplexa tal och fasoraddition.
* Sampling av sinussignaler samt beräkning av derivator, integraler och komplexa tal i C, i den avslutande laborationen [L18](./lectures/L18/README.md).

Efter genomförd kurs ska studenten kunna:
* Lösa algebraiska uttryck, ekvationer och ekvationssystem som uppstår i eltekniska sammanhang.
* Räkna med potenser, rötter, logaritmer och decibel.
* Beräkna och tolka derivator och integraler för vanligt förekommande funktioner.
* Räkna med komplexa tal och fasorer för att analysera växelströmskretsar.
* Implementera kursens matematik i C med `math.h` och `complex.h`.

---

## Boken
Hela kursen finns också som en bok: [Elteknisk matematik](./book/elteknisk-matematik.pdf).
Den innehåller teorin, uppgifterna, övningsduggorna och övningstentamen, med svaren på samtliga uppgifter i ett facit. Den byggs från källorna i [`book/`](./book/README.md), där det också står hur du bygger den själv (`make -C book`) och hur en ny upplaga ges ut.

Boken finns också tillgänglig på engelska: [Electrical Engineering Mathematics](./book/electrical-engineering-mathematics.pdf).

---

## Struktur

```text
book/        Kursen satt som en bok med LuaLaTeX; `make -C book` bygger PDF:en.
ci/          Skript för kodformatering (clang-format).
exam/        Tentameninformation och övningstentamen.
info/        Kursinformation, schema och examination.
lectures/    Föreläsningar, litteratur och övningsuppgifter.
```

---

## Kodformatering
`ci/format.sh` formaterar C/C++-kod (t.ex. koden till [L18](./lectures/L18/code/README.md)) med `clang-format`:

```bash
ci/format.sh          # Formatera alla filer.
ci/format.sh --check  # Kontrollera formateringen utan att ändra filer.
```

Innan skriptet körs behöver `clang-format` finnas installerat och tillgängligt i `PATH`:

```bash
sudo apt -y update
sudo apt -y install clang-format
```

Formateringen kontrolleras automatiskt via CI (se [.github/workflows/ci.yml](./.github/workflows/ci.yml)) vid push och pull request mot `main`.

---

## Figurer
Några figurer ritas med Python-skript som ligger bredvid bilden och har samma namn, till exempel [`2.1_voltage.py`](./lectures/L15/appendix/images/2.1_voltage.py), som ritar `2.1_voltage.png`. Ändra i skriptet och kör det för att rita om bilden, som då skrivs bredvid skriptet:

```bash
sudo apt -y install python3-matplotlib python3-numpy
python3 lectures/L15/appendix/images/2.1_voltage.py
```

Kretsfigurerna med engelska etiketter, till exempel
[`2.5_circuit_en.py`](./lectures/L03/appendix/images/2.5_circuit_en.py), ritas dessutom med
[schemdraw](https://schemdraw.readthedocs.io/), som inte finns i apt. Installera det i en virtuell
miljö:

```bash
python3 -m venv ~/.venvs/schemdraw
~/.venvs/schemdraw/bin/pip install matplotlib schemdraw
~/.venvs/schemdraw/bin/python lectures/L03/appendix/images/2.5_circuit_en.py
```

---

## Licens
Kursmaterialet är licensierat under [CC BY 4.0](./LICENSE) – Erik Pihl.

Källkoden i [lectures/L18/code/](./lectures/L18/code/) är licensierad separat under [MIT](./lectures/L18/code/LICENSE), eftersom CC BY 4.0 inte är avsedd för mjukvara.

---
