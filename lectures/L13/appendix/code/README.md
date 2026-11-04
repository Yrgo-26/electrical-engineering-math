# Kod för L13 – Derivator med funktionspekare i C
Programmet beräknar derivatan numeriskt för $e^x$, $\sin(v)$, $2^x$ och $\log_{10} x$ med en och samma funktion, `derive()`, som tar funktionen som argument. Programmet motsvarar uppgift 4.1 b) till e) i [bilaga B](../b_exercises.md).

---

## Idén
Derivatan approximeras med samma kvot som i [L12](../../../L12/appendix/code/README.md), men med ett fast litet $h$:

```math
f'(x) \approx \frac{f(x + h) - f(x)}{h}, \qquad h = 10^{-6}
```

I L12 stod funktionen $f(x) = x^2$ skriven direkt i derivatafunktionen. Här skickas funktionen i stället som argument, så att samma `derive()` fungerar för vilken funktion som helst.

---

## Så fungerar koden

### Konstanten

```c
#define H_STEP 1e-6
```

`H_STEP` är steget $h$ i kvoten ovan, alltså $10^{-6}$.

### Funktionspekaren

```c
typedef double (*math_func_t)(double);
```

`math_func_t` är en **funktionspekare**: en typ som kan peka på vilken funktion som helst som tar en `double` och returnerar en `double`. Precis som en vanlig variabel lagrar ett tal, lagrar en funktionspekare en funktion, som sedan kan anropas.

### Funktionerna `e_x()` och `two_x()`

```c
static inline double e_x(const double x) { return pow(M_E, x); }
static inline double two_x(const double x) { return pow(2.0, x); }
```
`e_x()` beräknar $e^x$ och `two_x()` beräknar $2^x$, båda med `pow()` från `math.h`. `M_E` är konstanten $e$. Funktionerna behövs eftersom `pow()` tar två argument och därför inte stämmer med `math_func_t`. `e_x()` och `two_x()` tar däremot ett argument, så de kan skickas till `derive()`.

### Funktionen `derive()`

```c
static inline double derive(math_func_t f, const double x)
{
    const double y1 = f(x);
    const double y2 = f(x + H_STEP);
    return (y2 - y1) / H_STEP;
}
```

Parametern `f` är funktionen som ska deriveras. Inne i `derive()` anropas den som en vanlig funktion, `f(x)`, oavsett vilken funktion som skickades in. `y1` och `y2` är funktionsvärdena i $x$ och $x + h$, och kvoten mellan skillnaden och $h$ är lutningen.

### Testfunktionerna och `main()`
Varje funktion testas i en egen funktion, och `main()` anropar dem i tur och ordning. Funktionens namn skrivs utan parenteser i anropet till `derive()`, eftersom funktionen ska skickas, inte anropas.

**`derive_e_x()`:** loopen går från $x = 0$ till $x = 4$ och anropar `derive(e_x, x)`. Loopvariabeln är en `double`, vilket fungerar här eftersom steget är $1$ och heltal lagras exakt.

**`derive_sinv()`:** `sin()` från `math.h` tar redan en `double` och returnerar en `double`, så den skickas direkt med `derive(sin, v)`, utan någon egen funktion. Här är steget $0{,}2$, som inte kan lagras exakt. Om $0{,}2$ adderades i varje varv skulle avrundningsfelen byggas upp, och $v$ skulle hamna nära men inte exakt på $0$. Därför går heltalet `i` från $-5$ till $5$, och $v$ beräknas som `i * 0.2` i varje varv.

**`derive_2_x()`:** loopen går från $x = 0$ till $x = 4$ och jämför `derive(two_x, x)` med $2^x \ln 2$. `log()` i `math.h` är den naturliga logaritmen, så $\ln 2$ skrivs `log(2.0)`.

**`derive_logx()`:** `log10()` från `math.h` stämmer med `math_func_t`, precis som `sin()`, och skickas direkt med `derive(log10, x)`. Lutningen jämförs med $\frac{1}{x \ln 10}$, beräknat med `1.0 / (x * log(10.0))`. Loopen börjar på $x = 1$, eftersom $\log_{10} x$ bara är definierad för $x > 0$.

---

## Utskrift
I utskriften står `f'(x)` för den numeriska derivatan.

```
--------------------------------------------------------------------------------
Test f(x) = e^x for x = [0, 4]:

f(0) = 1, f'(0) = 1
f(1) = 2.71828, f'(1) = 2.71828
f(2) = 7.38906, f'(2) = 7.38906
f(3) = 20.0855, f'(3) = 20.0855
f(4) = 54.5982, f'(4) = 54.5982
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
Test f(v) = sin(v) for v = [-1, 1], expect f'(v) = cos(v):

sin(-1) = -0.841471, cos(-1) = 0.540302, f'(-1) = 0.540303
sin(-0.8) = -0.717356, cos(-0.8) = 0.696707, f'(-0.8) = 0.696707
sin(-0.6) = -0.564642, cos(-0.6) = 0.825336, f'(-0.6) = 0.825336
sin(-0.4) = -0.389418, cos(-0.4) = 0.921061, f'(-0.4) = 0.921061
sin(-0.2) = -0.198669, cos(-0.2) = 0.980067, f'(-0.2) = 0.980067
sin(0) = 0, cos(0) = 1, f'(0) = 1
sin(0.2) = 0.198669, cos(0.2) = 0.980067, f'(0.2) = 0.980066
sin(0.4) = 0.389418, cos(0.4) = 0.921061, f'(0.4) = 0.921061
sin(0.6) = 0.564642, cos(0.6) = 0.825336, f'(0.6) = 0.825335
sin(0.8) = 0.717356, cos(0.8) = 0.696707, f'(0.8) = 0.696706
sin(1) = 0.841471, cos(1) = 0.540302, f'(1) = 0.540302
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
Test f(x) = 2^x for x = [0, 4], expect f'(x) = 2^x * ln(2)

f(0) = 1, f'(0) = 0.693147, 2^0 * ln(2) = 0.693147
f(1) = 2, f'(1) = 1.38629, 2^1 * ln(2) = 1.38629
f(2) = 4, f'(2) = 2.77259, 2^2 * ln(2) = 2.77259
f(3) = 8, f'(3) = 5.54518, 2^3 * ln(2) = 5.54518
f(4) = 16, f'(4) = 11.0904, 2^4 * ln(2) = 11.0904
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
Test f(x) = log10(x) for x = [1, 5], expect f'(x) = 1 / (x * ln(10))

f(1) = 0, f'(1) = 0.434294, 1 / (1 * ln(10)) = 0.434294
f(2) = 0.30103, f'(2) = 0.217147, 1 / (2 * ln(10)) = 0.217147
f(3) = 0.477121, f'(3) = 0.144765, 1 / (3 * ln(10)) = 0.144765
f(4) = 0.60206, f'(4) = 0.108574, 1 / (4 * ln(10)) = 0.108574
f(5) = 0.69897, f'(5) = 0.0868589, 1 / (5 * ln(10)) = 0.0868589
--------------------------------------------------------------------------------

```

**$e^x$:** lutningen är lika med funktionsvärdet i varje punkt, vilket stämmer med $\frac{d}{dx}e^x = e^x$.

**$\sin(v)$:** lutningen är lika med $\cos(v)$, vilket stämmer med $\frac{d}{dv}\sin(v) = \cos(v)$.

**$2^x$:** lutningen är lika med $2^x \ln 2$. Lutningen är alltså proportionell mot funktionsvärdet, men med faktorn $\ln 2 \approx 0{,}693$ i stället för $1$ som för $e^x$. Det är därför $e$ är den naturliga basen.

**$\log_{10} x$:** lutningen är lika med $\frac{1}{x \ln 10}$. Eftersom $\log_{10} x = \frac{\ln x}{\ln 10}$ är derivatan $\frac{1}{x}$ delat med konstanten $\ln 10 \approx 2{,}303$.

På några rader för $\sin(v)$ skiljer sig den sista siffran, till exempel $0{,}540303$ mot $0{,}540302$ för $v = -1$. Kvoten mäter lutningen mellan $v$ och $v + h$ i stället för exakt i $v$, så resultatet avviker ungefär $\frac{h}{2} \cdot f''(v)$ från derivatan. För $\sin(v)$ är $f''(v) = -\sin(v)$, så lutningen blir något för stor där $\sin(v) < 0$ och något för liten där $\sin(v) > 0$. Avvikelsen är under $10^{-6}$ och syns bara i den sjätte värdesiffran.

---

## Kör programmet

### I OnlineGDB
Klistra in innehållet i `main.c` på <https://www.onlinegdb.com/online_c_compiler>, kontrollera att språket är inställt på **C** och tryck på **Run**.

### I WSL
Stå i den här katalogen och kör:

```bash
make
```

Kommandot kompilerar programmet till den körbara filen `deriv_example` och kör det sedan. Med `make clean` tas filen bort.

---
