# Kod för L14 – Integralen som en summa i C
Programmet beräknar den bestämda integralen numeriskt, som en summa av smala rektanglar. Funktionen `integrate()` tar funktionen som argument, precis som `derive()` i [L13](../../../L13/appendix/code/README.md), och testas med tre funktioner:

* $f(x) = 2x$ på intervallet $[0, 2]$,
* $f(x) = \sin(x)$ på intervallet $[0, \pi]$, se uppgift 4.1 b) och c) i [bilaga B](../b_exercises.md),
* $f(x) = e^{2x}$ på intervallet $[0, 1]$, se uppgift 4.1 d).

---

## Idén
Den bestämda integralen är arean under kurvan. Arean kan approximeras genom att intervallet $[a, b]$ delas upp i $n$ smala rektanglar med bredden

```math
\Delta x = \frac{b - a}{n}
```

Varje rektangel får höjden $f(x)$ i sin vänstra kant, och rektanglarnas areor summeras:

```math
\int_a^b f(x)\,dx \approx \sum_{i=0}^{n-1} f(a + i\,\Delta x) \cdot \Delta x
```

Ju fler rektanglar, desto närmare den exakta arean hamnar summan.

---

## Så fungerar koden

### Konstanterna
```c
#define EXACT_2X 4.0
#define EXACT_SIN 2.0
#define EXACT_E_2X 3.194528049465325
```
Makrona är integralernas exakta värden, beräknade med primitiva funktioner (se avsnittet Utskrift). De används för att beräkna felet i varje approximation.

### Funktionspekaren
```c
typedef double (*math_func_t)(double);
```
`math_func_t` är samma funktionspekare som i L13: en typ som kan peka på vilken funktion som helst som tar en `double` och returnerar en `double`. Därmed fungerar `integrate()` för vilken sådan funktion som helst.

### Funktionen `integrate()`
```c
static double integrate(math_func_t f, const double a, const double b, size_t n)
{
    if (0U == n)
    {
        printf("Cannot divide by 0!\n");
        return -1.0;
    }

    const double dx = (b - a) / n;
    double area     = 0.0;

    for (size_t i = 0U; i < n; ++i)
    {
        area += f(a + i * dx);
    }
    return area * dx;
}
```
Parametrarna är funktionen `f`, den undre och den övre gränsen `a` och `b` samt antalet rektanglar `n`. Typen `size_t` från `stddef.h` används för `n`, eftersom ett antal aldrig kan vara negativt.

**Kontroll av `n`:** bredden beräknas som `(b - a) / n`, så `n = 0` skulle innebära division med noll. Funktionen skriver då ut ett felmeddelande och returnerar `-1.0`.

**Summan:** loopen går igenom rektanglarna en i taget. Rektangel nummer `i` har sin vänstra kant i `a + i * dx`, och höjden där, `f(a + i * dx)`, läggs till i `area`.

**Multiplikation med `dx`:** alla rektanglar har samma bredd, så i stället för att multiplicera varje höjd med `dx` summeras höjderna först, och summan multipliceras med `dx` en gång på slutet. Det ger samma resultat, eftersom

```math
\sum_{i=0}^{n-1} f(x_i) \cdot \Delta x = \Delta x \cdot \sum_{i=0}^{n-1} f(x_i)
```

### Funktionerna som integreras
```c
static inline double two_x(const double x) { return 2.0 * x; }
static inline double e_2x(const double x) { return pow(M_E, 2.0 * x); }
```
`two_x()` är funktionen $f(x) = 2x$ och `e_2x()` funktionen $f(x) = e^{2x}$, beräknad med `pow()` och konstanten `M_E` från `math.h`. Båda stämmer med `math_func_t`. `sin()` från `math.h` tar redan en `double` och returnerar en `double`, så den behöver ingen egen funktion utan skickas direkt.

### Funktionen `test_integration()`
```c
static void test_integration(math_func_t func, const size_t* samples, const size_t sample_count,
                             const double a, const double b, const double exact,
                             const char* output)
```
`test_integration()` integrerar funktionen `func` från `a` till `b` en gång för varje antal rektanglar i arrayen `samples`, och skriver ut arean för varje antal. `exact` är integralens exakta värde, och felet skrivs ut som avståndet mellan summan och det exakta värdet, `fabs(area - exact)`. Funktionen `fabs()` från `math.h` ger absolutbeloppet, så felet blir aldrig negativt. `sample_count` är antalet element i arrayen, och `output` är funktionen som text, till exempel `"sin(x)"`, som används i utskriften. Arrayen skickas som en pekare till sitt första element, så funktionen kan inte själv ta reda på hur lång den är. Därför skickas längden med som en egen parameter.

### Funktionen `main()`
```c
const size_t samples[]    = {4U, 10U, 100U, 1000U};
const size_t sample_count = sizeof(samples) / sizeof(size_t);

test_integration(two_x, samples, sample_count, 0.0, 2.0, EXACT_2X, "2x");
test_integration(sin, samples, sample_count, 0.0, M_PI, EXACT_SIN, "sin(x)");
test_integration(e_2x, samples, sample_count, 0.0, 1.0, EXACT_E_2X, "e^2x");
```
Arrayen `samples` innehåller de antal rektanglar som testas. Antalet element beräknas med `sizeof`: arrayens storlek i byte delat med storleken på ett element. Sedan testas de tre funktionerna med samma antal rektanglar. De exakta värdena skickas med som makrona ovan. Funktionernas namn skrivs utan parenteser, eftersom funktionerna ska skickas, inte anropas.

---

## Utskrift
```
--------------------------------------------------------------------------------
Integrating f(x) = 2x:
Samples = 4, area = 3, error = 1
Samples = 10, area = 3.6, error = 0.4
Samples = 100, area = 3.96, error = 0.04
Samples = 1000, area = 3.996, error = 0.004
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
Integrating f(x) = sin(x):
Samples = 4, area = 1.89612, error = 0.103881
Samples = 10, area = 1.98352, error = 0.0164765
Samples = 100, area = 1.99984, error = 0.000164496
Samples = 1000, area = 2, error = 1.64493e-06
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
Integrating f(x) = e^2x:
Samples = 4, area = 2.46217, error = 0.732355
Samples = 10, area = 2.88572, error = 0.308811
Samples = 100, area = 3.16269, error = 0.0318388
Samples = 1000, area = 3.19133, error = 0.00319346
--------------------------------------------------------------------------------

```

De exakta värdena beräknas med primitiva funktioner:

```math
\int_0^2 2x\,dx = \Big[x^2\Big]_0^2 = 4, \qquad \int_0^{\pi} \sin(x)\,dx = \Big[-\cos(x)\Big]_0^{\pi} = 2, \qquad \int_0^1 e^{2x}\,dx = \left[\frac{e^{2x}}{2}\right]_0^1 = \frac{e^2 - 1}{2} \approx 3{,}1945
```

**$2x$ och $e^{2x}$:** felet blir ungefär $10$ gånger mindre när $n$ tiodubblas, vilket är det vanliga. Båda funktionerna växer på hela intervallet, så höjden i rektangelns vänstra kant är den lägsta på hela rektangeln, och varje rektangel ligger under kurvan. Summan blir därför alltid för liten. För $2x$ kan felet beräknas exakt. Med $\Delta x = \frac{2}{n}$ blir summan

```math
\sum_{i=0}^{n-1} 2 \cdot i\,\Delta x \cdot \Delta x = 2\left(\frac{2}{n}\right)^2 \cdot \frac{n(n - 1)}{2} = 4 - \frac{4}{n},
```

så felet är exakt $\frac{4}{n}$.

**$\sin(x)$:** felet blir ungefär $100$ gånger mindre när $n$ tiodubblas, vilket är ovanligt bra för rektanglar. Kurvan stiger på den första halvan av intervallet och sjunker på den andra, så rektanglarna ligger under kurvan på den stigande sidan och över den på den sjunkande. Eftersom kurvan är symmetrisk och $\sin(0) = \sin(\pi) = 0$ tar felen nästan ut varandra.

För $n = 1000$ är summan för $\sin(x)$ ungefär $1{,}9999984$, men `%g` skriver som standard ut högst sex värdesiffror, och då avrundas värdet till `2`.

---

## Kör programmet

### I OnlineGDB
Klistra in innehållet i `main.c` på <https://www.onlinegdb.com/online_c_compiler>, kontrollera att språket är inställt på **C** och tryck på **Run**.

### I WSL
Stå i den här katalogen och kör:

```bash
make
```

Kommandot kompilerar programmet till den körbara filen `integral_example` och kör det sedan. Med `make clean` tas filen bort.
