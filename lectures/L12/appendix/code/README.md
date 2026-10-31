# Kod för L12 – Derivatans definition i C
Programmet visar hur derivatans definition fungerar i praktiken. Det beräknar lutningen 
för $f(x) = x^2$ i punkten $x = 3$ med allt mindre värden på $h$, se uppgift 3.1 i 
[bilaga B](../b_exercises.md).

---

## Idén
Derivatan är gränsvärdet av lutningen mellan punkterna $x$ och $x + h$ när $h$ går mot noll:

```math
f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
```

En dator kan inte låta $h$ gå ända till noll, eftersom det skulle innebära division med noll. I stället väljer vi ett litet $h$ och beräknar kvoten. Ju mindre $h$ är, desto närmare derivatan hamnar vi.

---

## Så fungerar koden

### Konstanterna

```c
#define H_MIN 1e-6
#define H_MAX 1.0
#define H_STEP 10.0
```

`H_MAX` är det första värdet på $h$ och `H_MIN` det minsta. `H_STEP` är talet som $h$ delas med i varje varv. `1e-6` betyder $10^{-6}$.

### Funktionen `f()`

```c
static inline double f(const double x) { return x * x; }
```

Detta är den matematiska funktionen $f(x) = x^2$ skriven i C. För att undersöka en annan funktion räcker det att ändra den här raden.

### Funktionen `derive()`

```c
static inline double derive(const double x, const double h) { return (f(x + h) - f(x)) / h; }
```

Här står kvoten från definitionen, nästan tecken för tecken. Funktionen ger ett närmevärde till $f'(x)$, och den anropar `f()` två gånger: en gång i $x + h$ och en gång i $x$.

### Funktionen `main()`

```c
const double x = 3.0;

for (double h = H_MAX; h >= H_MIN; h /= H_STEP)
{
    const double slope = derive(x, h);
    printf("x = %g, f'(%g) = %g when h = %g\n", x, x, slope, h);
}
```

Loopen börjar med $h = 1$. Efter varje varv delas $h$ med 10 (`h /= H_STEP` betyder `h = h / H_STEP`), och loopen fortsätter så länge $h$ är minst $10^{-6}$. Det ger sju varv. I varje varv beräknas lutningen, som lagras i `slope`, och skrivs ut.

---

## Utskrift
```
x = 3, f'(3) = 7 when h = 1
x = 3, f'(3) = 6.1 when h = 0.1
x = 3, f'(3) = 6.01 when h = 0.01
x = 3, f'(3) = 6.001 when h = 0.001
x = 3, f'(3) = 6.0001 when h = 0.0001
x = 3, f'(3) = 6.00001 when h = 1e-05
x = 3, f'(3) = 6 when h = 1e-06
```

Lutningen närmar sig 6, vilket stämmer med deriveringsreglerna: $f'(x) = 2x$ ger $f'(3) = 6$.

Att värdena ser ut som $6 + h$ är ingen slump. Kvoten kan förenklas algebraiskt:

```math
\frac{(3 + h)^2 - 3^2}{h} = \frac{9 + 6h + h^2 - 9}{h} = \frac{6h + h^2}{h} = 6 + h
```

På den sista raden är lutningen ungefär $6{,}000001$, men `%g` skriver som standard ut högst sex värdesiffror, och då avrundas värdet till `6`.

---

## Varför blir resultatet sämre när h blir mycket litet?
Ändra `H_MIN` till `1e-15` och kör programmet igen:

```
x = 3, f'(3) = 7 when h = 1
x = 3, f'(3) = 6.1 when h = 0.1
x = 3, f'(3) = 6.01 when h = 0.01
x = 3, f'(3) = 6.001 when h = 0.001
x = 3, f'(3) = 6.0001 when h = 0.0001
x = 3, f'(3) = 6.00001 when h = 1e-05
x = 3, f'(3) = 6 when h = 1e-06
x = 3, f'(3) = 6 when h = 1e-07
x = 3, f'(3) = 6 when h = 1e-08
x = 3, f'(3) = 6 when h = 1e-09
x = 3, f'(3) = 6 when h = 1e-10
x = 3, f'(3) = 6 when h = 1e-11
x = 3, f'(3) = 6.00053 when h = 1e-12
x = 3, f'(3) = 6.00409 when h = 1e-13
x = 3, f'(3) = 6.21725 when h = 1e-14
x = 3, f'(3) = 5.32907 when h = 1e-15
```

Ner till $h = 10^{-11}$ ser allt bra ut, men sedan blir resultatet sämre, och för 
$h = 10^{-15}$ är lutningen hela $5{,}33$ i stället för 6.

Talet $10^{-15}$ är inte för litet i sig: en `double` kan lagra tal ner till ungefär $10^{-308}$. 
Problemet är att en `double` bara har ungefär 16 värdesiffror. När ett mycket litet tal läggs till
ett mycket större tal får det inte plats, utan avrundas. Närmaste talen som går att lagra ligger 
på avståndet $4{,}4 \cdot 10^{-16}$ runt 3 och $1{,}8 \cdot 10^{-15}$ runt 9.

Så här går det för $h = 10^{-15}$:\
**1.** `x + h` ska bli $3 + 10^{-15}$, men avrundas till $3 + 8{,}88 \cdot 10^{-16}$.\
**2.** `f(x + h)` blir då $9 + 5{,}33 \cdot 10^{-15}$. Det rätta värdet hade varit ungefär $9 + 6 \cdot 10^{-15}$.\
**3.** `f(x + h) - f(x)` blir $5{,}33 \cdot 10^{-15}$, och det är bara tre steg över 9.\
**4.** Division med $h = 10^{-15}$ ger lutningen $5{,}33$.

Täljaren består alltså av några få avrundade steg, och när den delas med ett mycket litet $h$ blir
felet stort. För $h = 10^{-16}$ är det ännu tydligare: `x + h` avrundas till exakt 3, täljaren
blir 0 och lutningen blir 0.

Det finns alltså två fel som drar åt olika håll:
* **Stort $h$:** kvoten är inte derivatan, felet här är exakt $h$ eftersom kvoten är $6 + h$.
* **Litet $h$:** avrundningsfelet växer när $h$ minskar.

Det minsta felet får vi här runt $h = 10^{-8}$, där lutningen är ungefär $5{,}99999996$. Det syns 
inte i utskriften, eftersom `%g` avrundar till sex värdesiffror. Skriv `%.10g` i stället för `%g`
för att se fler siffror.

---

## Kör programmet

### I OnlineGDB
Klistra in innehållet i `main.c` på <https://www.onlinegdb.com/online_c_compiler>, kontrollera 
att språket är inställt på **C** och tryck på **Run**.

### I WSL
Stå i den här katalogen och kör:

```bash
make
```

Kommandot kompilerar programmet till den körbara filen `deriv_example` och kör det sedan.
Med `make clean` tas filen bort.

---
