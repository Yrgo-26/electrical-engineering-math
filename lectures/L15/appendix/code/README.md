# Kod för L15 – Polär form i C
Programmet representerar komplexa tal med en egen strukt, `complex_t`, och skriver ut talen på både rektangulär och polär form. Det testas med tre tal, se uppgift 4.1 i [bilaga B](../b_exercises.md):

* $z_1 = 3 + j4$ i kvadrant I,
* $z_2 = -2 - j3$ i kvadrant III,
* $z_3 = 10\angle 45^{\circ}$, som skapas från polär form.

---

## Idén
Ett komplext tal $z = a + jb$ har beloppet och argumentet

```math
|z| = \sqrt{a^2 + b^2}, \qquad \theta = \arg(z)
```

Omvänt ger beloppet $r$ och argumentet $\theta$ talet på rektangulär form:

```math
z = r\angle\theta = r\cos\theta + j\,r\sin\theta
```

Argumentet kan inte beräknas med enbart $\arctan\frac{b}{a}$, eftersom kvoten inte visar i vilken kvadrant talet ligger. Funktionen `atan2()` tar emot $b$ och $a$ var för sig och ger därför rätt vinkel direkt.

---

## Så fungerar koden

### Konstanterna

```c
#define PI_DEG 180.0
#define SQUARE 2.0
```

`PI_DEG` är ett halvt varv i grader: $\pi$ radianer motsvarar $180^{\circ}$. Konstanten används vid omvandling mellan radianer och grader. `SQUARE` är exponenten som skickas till `pow()` för att kvadrera ett tal.

### Strukten `complex_t`

```c
typedef struct
{
    double re;
    double im;
} complex_t;
```

Strukten samlar realdelen `re` och imaginärdelen `im` under ett gemensamt namn. Talet $3 + j4$ skapas med `const complex_t z1 = {3.0, 4.0};`, där värdena tilldelas fälten i den ordning de är deklarerade.

### Omvandling mellan radianer och grader

```c
static inline double to_deg(const double rad) { return rad * PI_DEG / M_PI; }
static inline double to_rad(const double deg) { return deg * M_PI / PI_DEG; }
```

De trigonometriska funktionerna i `math.h` räknar i radianer, men uppgiften anger vinklar i grader. Eftersom $\pi$ radianer motsvarar $180^{\circ}$ multipliceras med $\frac{180}{\pi}$ vid omvandling till grader och med $\frac{\pi}{180}$ vid omvandling till radianer. Konstanten `M_PI` från `math.h` används för $\pi$.

### Funktionen `complex_magnitude()`

```c
static inline double complex_magnitude(const complex_t* z)
{
    const double re = pow(z->re, SQUARE);
    const double im = pow(z->im, SQUARE);
    return sqrt(re + im);
}
```

Beloppet beräknas med Pythagoras sats: real- och imaginärdelen kvadreras med `pow()`, och roten ur summan tas med `sqrt()`. Talet skickas som en pekare, och fälten nås med pil: `z->re` och `z->im`. Parametertypen `const complex_t*` anger att funktionen inte ändrar talet.

Funktionerna kontrollerar inte att pekaren är giltig, det vill säga skild från `NULL`, innan fälten läses. Det är utelämnat för att hålla koden enkel. I ett riktigt program bör en pekare som kan vara `NULL` kontrolleras först, eftersom `z->re` med en `NULL`-pekare får programmet att krascha.

### Funktionen `complex_angle_deg()`

```c
static inline double complex_angle_deg(const complex_t* z)
{
    const double rad = atan2(z->im, z->re);
    return to_deg(rad);
}
```

`atan2()` tar imaginärdelen först och realdelen sedan, precis som $\arctan\frac{b}{a}$ har $b$ i täljaren. Eftersom den får delarna var för sig ser den deras tecken och ger vinkeln i rätt kvadrant. Svaret ligger mellan $-\pi$ och $\pi$, det vill säga mellan $-180^{\circ}$ och $180^{\circ}$, och omvandlas till grader med `to_deg()`.

### Funktionen `complex_from_polar()`

```c
static complex_t complex_from_polar(const double r, const double deg)
{
    const double rad = to_rad(deg);
    complex_t z;
    z.re = r * cos(rad);
    z.im = r * sin(rad);
    return z;
}
```

Vinkeln omvandlas först till radianer. Sedan beräknas realdelen som $r\cos\theta$ och imaginärdelen som $r\sin\theta$. Funktionen skapar ett nytt tal, så det returneras direkt i stället för via en pekare.

### Funktionen `complex_print()`

```c
static void complex_print(const complex_t* z)
{
    const char ch     = 0.0 <= z->im ? '+' : '-';
    const double im   = fabs(z->im);
    const double magn = complex_magnitude(z);
    const double deg  = complex_angle_deg(z);

    printf("Rectangular form:\tZ = %g %c j%g\n", z->re, ch, im);
    printf("Polar form:\t\tZ = %g < %g\n", magn, deg);
}

```
Talet skrivs ut på rektangulär form och sedan på polär form, med argumentet i grader. Imaginärdelens tecken skrivs ut för sig, som tecknet `ch`, följt av imaginärdelens absolutbelopp från `fabs()`. Därmed skrivs $z_2$ ut som `-2 - j3` i stället för `-2 + j-3`. Formatet `%g` skriver ut talet med högst sex värdesiffror och utan onödiga nollor, och `<` är en textversion av vinkeltecknet $\angle$. Raderna med bindestreck, som utelämnats ovan, ramar in varje tal i utskriften.

### Funktionen `main()`

```c
const complex_t z1 = {3.0, 4.0};
const complex_t z2 = {-2.0, -3.0};
const complex_t z3 = complex_from_polar(10.0, 45.0);

complex_print(&z1);
complex_print(&z2);
complex_print(&z3);
```

$z_1$ och $z_2$ skapas direkt på rektangulär form, medan $z_3$ skapas från polär form med `complex_from_polar()`. Varje tal skickas till `complex_print()` med `&`, det vill säga dess adress.

---

## Utskrift
```
--------------------------------------------------------------------------------
Rectangular form:	Z = 3 + j4
Polar form:		Z = 5 < 53.1301
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
Rectangular form:	Z = -2 - j3
Polar form:		Z = 3.60555 < -123.69
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
Rectangular form:	Z = 7.07107 + j7.07107
Polar form:		Z = 10 < 45
--------------------------------------------------------------------------------

```

**$z_1$ och $z_3$:** båda ligger i kvadrant I, så `atan2()` ger samma vinkel som $\arctan\frac{b}{a}$. För $z_3$ ger omvandlingen tillbaka till polär form ursprungsvärdena $10$ och $45^{\circ}$, vilket visar att `complex_from_polar()` och de andra funktionerna stämmer med varandra.

**$z_2$:** talet ligger i kvadrant III. `atan2()` ger $-123{,}69^{\circ}$, vilket anger samma riktning som $236{,}31^{\circ}$, eftersom $236{,}31^{\circ} - 360^{\circ} = -123{,}69^{\circ}$.

---

## Jämförelse med `atan()` (uppgift 4.1 c)
Programmet anropar inte `atan()`, men jämförelsen i uppgift c) kan provas genom att lägga till följande rad sist i `main()`, före `return 0;`:

```c
printf("atan(z2.im / z2.re) = %g\n", to_deg(atan(z2.im / z2.re)));
```

Raden skriver ut `atan(z2.im / z2.re) = 56.3099`, alltså $56{,}31^{\circ}$, vilket är vinkeln för $2 + j3$ i kvadrant I. Kvoten $\frac{-3}{-2} = \frac{3}{2}$ är densamma för båda talen, så tecknen och därmed kvadranten försvinner i divisionen. `atan2()` tar emot imaginär- och realdelen var för sig och ser deras tecken, så den ger rätt vinkel, $-123{,}69^{\circ}$. Med `atan()` måste $180^{\circ}$ läggas till eller dras bort för hand när realdelen är negativ.

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
