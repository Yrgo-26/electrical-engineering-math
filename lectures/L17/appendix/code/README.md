# Kod för L17 – Fasoraddition i C
Programmet adderar sinusspänningarna

```math
u_1(t) = 2\sin(\omega t + 45^{\circ})\,\text{V}, \qquad u_2(t) = 3\sin(\omega t - 60^{\circ})\,\text{V}
```

med fasorer och skriver ut summan på både rektangulär och polär form, se uppgift 4.1 i [bilaga B](../b_exercises.md). Programmet bygger vidare på koden från L15, som förklaras i [L15:s kod-README](../../../L15/appendix/code/README.md).

---

## Idén
Två sinusspänningar med samma vinkelfrekvens $\omega$ kan adderas med fasorer. Varje spänning $|U|\sin(\omega t + \delta)$ representeras av fasorn $U = |U|\angle\delta$:

```math
U_1 = 2\angle 45^{\circ}, \qquad U_2 = 3\angle{-60^{\circ}}
```

Fasorerna omvandlas till rektangulär form, där summan beräknas genom att realdelarna och imaginärdelarna adderas var för sig. Summan $U_{tot}$ omvandlas sedan tillbaka till polär form, och ger amplituden och fasen för den totala spänningen:

```math
u_{tot}(t) = |U_{tot}|\sin(\omega t + \delta_{tot})
```

---

## Så fungerar koden

### Från L15
Strukten `complex_t` och funktionerna `to_deg()`, `to_rad()`, `complex_magnitude()`, `complex_angle_deg()`, `complex_from_polar()` och `complex_print()` är desamma som i L15 och förklaras i [L15:s kod-README](../../../L15/appendix/code/README.md). Funktionerna tar emot talen via pekare och kontrollerar inte att pekarna är skilda från `NULL`. Det är utelämnat för att hålla koden enkel.

### Funktionen `complex_add()`

```c
static complex_t complex_add(const complex_t* a, const complex_t* b)
{
    const double re   = a->re + b->re;
    const double im   = a->im + b->im;
    const complex_t z = {re, im};
    return z;
}
```

På rektangulär form adderas två komplexa tal genom att realdelarna och imaginärdelarna adderas var för sig:

```math
(a_{re} + ja_{im}) + (b_{re} + jb_{im}) = (a_{re} + b_{re}) + j(a_{im} + b_{im})
```

Båda talen skickas som pekare av typen `const complex_t*`, så funktionen ändrar inget av dem. Summan är ett nytt tal och returneras därför direkt.

### Funktionen `main()`

```c
const sine_t u1 = {2.0, OMEGA, 45.0};
const sine_t u2 = {3.0, OMEGA, -60.0};

const complex_t a = complex_from_polar(u1.amplitude, u1.deg);
const complex_t b = complex_from_polar(u2.amplitude, u2.deg);

const complex_t z = complex_add(&a, &b);
complex_print(&z);
```

De två sinusspänningarna skapas först som variabler av typen `sine_t`, se nästa avsnitt. Fasorerna skapas sedan från varje spännings amplitud och fas, eftersom fasorn $|U|\angle\delta$ kommer direkt från sinusspänningen $|U|\sin(\omega t + \delta)$. Talen står därmed bara på ett ställe i koden. `complex_from_polar()` omvandlar fasorerna till rektangulär form, där `complex_add()` adderar dem, och summan skrivs ut på både rektangulär och polär form.

### Strukten `sine_t` och funktionen `sine_value()` (uppgift 4.1 c)

```c
typedef struct
{
    double amplitude;
    double omega;
    double deg;
} sine_t;
```

Strukten beskriver en sinussignal $u(t) = |U|\sin(\omega t + \delta)$ med amplituden `amplitude`, vinkelfrekvensen `omega` i rad/s och fasen `deg` i grader. På samma sätt som `complex_t` samlar real- och imaginärdelen samlar `sine_t` det som beskriver en sinussignal under ett gemensamt namn.

```c
static double sine_value(const sine_t* s, const double t)
{
    const double rad = to_rad(s->deg);
    return s->amplitude * sin(s->omega * t + rad);
}
```

Funktionen beräknar signalens värde $|U|\sin(\omega t + \delta)$ vid tiden $t$. Fasen omvandlas först till radianer med `to_rad()`, eftersom `sin()` räknar i radianer. Signalen skickas som en pekare av typen `const sine_t*`, så funktionen ändrar den inte.

I `main()` beräknas $u_1(0) + u_2(0)$ med de två signalerna och skrivs ut tillsammans med imaginärdelen av $U_{tot}$, så att de två värdena kan jämföras:

```c
const double u0 = sine_value(&u1, 0.0) + sine_value(&u2, 0.0);
printf("u1(0) + u2(0) = %g\n", u0);
printf("Im(Utot)      = %g\n", z.im);
```

`OMEGA` är vinkelfrekvensen för $50\,\text{Hz}$, $2\pi \cdot 50\,\text{rad/s}$, men vilket värde som helst fungerar här, eftersom $\omega t = 0$ vid $t = 0$.

---

## Utskrift
```
--------------------------------------------------------------------------------
Rectangular form:	Z = 2.91421 - j1.18386
Polar form:		Z = 3.1455 < -22.1088
--------------------------------------------------------------------------------

u1(0) + u2(0) = -1.18386
Im(Utot)      = -1.18386
```

**Summan:** fasorerna på rektangulär form är $U_1 \approx 1{,}414 + j1{,}414$ och $U_2 \approx 1{,}5 - j2{,}598$, så $U_{tot} \approx 2{,}914 - j1{,}184\,\text{V}$, vilket stämmer med utskriften. På polär form är $U_{tot} \approx 3{,}146\angle{-22{,}11^{\circ}}$, så den totala spänningen blir

```math
u_{tot}(t) \approx 3{,}15\sin(\omega t - 22{,}1^{\circ})\,\text{V}
```

Amplituden $3{,}15\,\text{V}$ är mindre än $2 + 3 = 5\,\text{V}$, eftersom spänningarna inte är i fas: deras toppar inträffar vid olika tidpunkter.

**Uppgift 4.1 c:** $u_1(0) + u_2(0)$ och imaginärdelen av $U_{tot}$ är lika, $-1{,}184\,\text{V}$. Vid $t = 0$ är en sinusspänning $|U|\sin\delta$, och det är just imaginärdelen av fasorn $|U|\angle\delta = |U|\cos\delta + j|U|\sin\delta$. När fasorerna adderas, adderas även imaginärdelarna, så imaginärdelen av $U_{tot}$ är summan av spänningarna vid $t = 0$. Värdet på $\omega$ spelar ingen roll, eftersom $\omega t = 0$ vid $t = 0$.

---

## Kör programmet

### I OnlineGDB
Klistra in innehållet i `main.c` på <https://www.onlinegdb.com/online_c_compiler>, kontrollera att språket är inställt på **C** och tryck på **Run**.

### I WSL
Stå i den här katalogen och kör:

```bash
make
```

Kommandot kompilerar programmet till den körbara filen `complex_example` och kör det sedan. Med `make clean` tas filen bort.

---
