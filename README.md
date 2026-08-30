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
* Ur- och urladdning av kondensatorer i RC-kretsar.
* Växelspänningar: amplitud, frekvens, fas och sinusekvationer.
* Impedansberäkningar med komplexa tal och fasoraddition.
* Sinusrekonstruktion med en digital-till-analog-omvandlare (DAC), i det avslutande projektet [P01](./projects/P01/README.md).

Efter genomförd kurs ska studenten kunna:
* Lösa algebraiska uttryck, ekvationer och ekvationssystem som uppstår i eltekniska sammanhang.
* Räkna med potenser, rötter, logaritmer och decibel.
* Beräkna och tolka derivator och integraler för vanligt förekommande funktioner.
* Räkna med komplexa tal och fasorer för att analysera växelströmskretsar.
* Koppla matematiska modeller till mätningar på verklig hårdvara.

---

## Struktur

```text
ci/          Skript för kodformattering (clang-format).
exam/        Tentameninformation och övningstentamen.
info/        Kursinformation, schema och examination.
lectures/    Föreläsningar, litteratur och övningsuppgifter.
projects/    Projektbeskrivningar, krav och inlämningsinstruktioner.
```

---

## Kodformattering
`ci/format.sh` formaterar C/C++-kod (t.ex. [P01](./projects/P01/README.md)s DAC-driver) med `clang-format`:

```bash
ci/format.sh          # Formatera alla filer.
ci/format.sh --check  # Kontrollera formattering utan att ändra filer.
```

Innan skriptet körs behöver `clang-format` finnas installerat och tillgängligt i `PATH`:

```bash
sudo apt -y update
sudo apt -y install clang-format
```

Formatteringen kontrolleras automatiskt via CI (se [.github/workflows/ci.yml](./.github/workflows/ci.yml)) vid push och pull request mot `main`.

---

## Licens
Kursmaterialet är licensierat under [CC BY 4.0](./LICENSE) – Erik Pihl.

Källkoden i [P01](./projects/P01/code/) är licensierad separat under [MIT](./projects/P01/code/LICENSE), eftersom CC BY 4.0 inte är avsedd för mjukvara.

---
