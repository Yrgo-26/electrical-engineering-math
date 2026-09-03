# Bilaga A – Matematik i C med math.h

## 1. Standardbiblioteket math.h
`math.h` är den del av C:s standardbibliotek som innehåller matematiska funktioner. Funktionerna arbetar med flyttal av typen `double`.

```c
#include <math.h>
#include <stdio.h>
```

### Utvecklingsmiljö
Under lektionen används [OnlineGDB](https://www.onlinegdb.com/online_c_compiler#), en `gcc`-kompilator som körs direkt i webbläsaren. Ingen installation krävs.

* Kontrollera att språket är inställt på **C** i listan uppe till höger.
* Skriv koden i editorn och tryck på **Run**.
* Programmets utskrift hamnar i rutan under editorn.

**OBS!** Koden sparas inte automatiskt. Kopiera den till en egen fil innan ni stänger fliken.

Den som hellre vill köra koden lokalt kan sätta upp **WSL** med `gcc`, se [`code/`](../code/README.md). Det är frivilligt och behövs inte för lektionen.

### Länkning mot matematikbiblioteket
Funktionerna i `math.h` ligger i ett separat matematikbibliotek, `libm`. På egen dator måste programmet därför länkas med flaggan `-lm`, som placeras **sist** på kommandoraden:

```bash
gcc main.c -o main -lm
./main
```

Utan `-lm` kompilerar programmet, men länkningen misslyckas med felmeddelanden av typen `undefined reference to 'sqrt'`. Får ni det felet i OnlineGDB, lägg till `-lm` under **Extra Compiler Flags** i inställningarna (kugghjulet).

### Konstanter
`M_PI` ($\pi$) och `M_E` ($e$) finns i `math.h` på de flesta system, men de ingår inte i C-standarden och saknas därför i strikt standardläge (`-std=c11`). OnlineGDB använder `gcc`:s standardläge, så `M_PI` fungerar där. För att koden ska fungera överallt kan konstanten definieras direkt i programmet:

```c
#define PI 3.14159265358979323846
```

---

## 2. Flyttal i C: float och double
I **Tillämpad Elektronik** används heltalstyper som `int`, `uint8_t` och `uint16_t`. De kan endast lagra hela tal – `7 / 2` blir `3`, inte `3,5`. Matematiken i denna kurs kräver decimaltal, och då används **flyttal**.

**Varför undviks flyttal i mikrokontrollerkod?** En AVR-mikrokontroller saknar flyttalsenhet (FPU). Flyttalsberäkningar måste därför utföras i programvara, vilket är långsamt och tar stor plats i minnet. På AVR är `double` dessutom ofta bara 32 bitar, alltså samma precision som `float`. En vanlig dator har en FPU och räknar med flyttal utan extra kostnad – därför används de fritt i denna kurs.

### Typer

| Typ | Storlek | Ungefärlig precision | Användning |
|-----|---------|----------------------|------------|
| `float` | 32 bitar | ~7 signifikanta siffror | När minnet är begränsat |
| `double` | 64 bitar | ~15 signifikanta siffror | **Standard i denna kurs** |

Samtliga funktioner i `math.h` tar emot och returnerar `double`. Använd därför `double` genomgående.

### Litteraler
Hur ett tal skrivs avgör vilken typ det får:

```c
int    a = 2;      // Heltal.
double b = 2.0;    // Flyttal (double).
float  c = 2.0f;   // Flyttal (float).
```

**OBS!** Divideras två heltal utförs heltalsdivision, oavsett vilken typ resultatet lagras i:

```c
double x = 1 / 2;      // 0.0 - heltalsdivision!
double y = 1.0 / 2.0;  // 0.5
```

### Utskrift

| Typ | Formatspecificerare |
|-----|---------------------|
| `int`, `uint8_t`, `uint16_t` | `%d` |
| `float`, `double` | `%f`, exempelvis `%.3f` för tre decimaler |

`printf()` omvandlar automatiskt `float` till `double`, så `%f` fungerar för båda. Använd aldrig `%d` för ett flyttal – utskriften blir då meningslös.

### Omvandling mellan heltal och flyttal
Heltal omvandlas automatiskt till flyttal. Åt andra hållet **avkortas** talet, det avrundas inte:

```c
const double d = 7;           // 7.0
const int    n = 3.9;         // 3, inte 4!
const int    m = round(3.9);  // 4
```

### Precision
Flyttal lagras binärt och kan inte representera alla decimaltal exakt. Uttrycket `0.1 + 0.2` ger `0.30000000000000004`, inte exakt `0.3`.

Jämför därför aldrig flyttal med `==`. Kontrollera i stället att skillnaden är tillräckligt liten:

```c
if (fabs(a - b) < 1e-9) { /* Talen betraktas som lika. */ }
```

---

## 3. Grundläggande funktioner

| Matematik | C-funktion | Kommentar |
|-----------|------------|-----------|
| $\sqrt{x}$ | `sqrt(x)` | Kvadratrot, $x \geq 0$ |
| $x^y$ | `pow(x, y)` | Potens |
| $e^x$ | `exp(x)` | Exponentialfunktion |
| $\ln x$ | `log(x)` | Naturlig logaritm, $x > 0$ |
| $\lg x$ | `log10(x)` | Tiologaritm, $x > 0$ |
| $\lvert x \rvert$ | `fabs(x)` | Absolutbelopp för flyttal |
| $\sqrt{x^2 + y^2}$ | `hypot(x, y)` | Belopp för en vektor |
| Rest vid division | `fmod(x, y)` | Motsvarar `%` fast för flyttal |
| Avrundning | `round(x)` | `floor(x)` nedåt, `ceil(x)` uppåt |

**OBS!** `%` fungerar endast för heltal. För flyttal används `fmod()`.

```c
const double r = sqrt(pow(3.0, 2.0) + pow(4.0, 2.0)); // r = 5.0
printf("r = %.2f\n", r);
```

---

## 4. Trigonometriska funktioner

| Matematik | C-funktion | Returvärde |
|-----------|------------|------------|
| $\sin(x)$ | `sin(x)` | – |
| $\cos(x)$ | `cos(x)` | – |
| $\tan(x)$ | `tan(x)` | – |
| $\arcsin(x)$ | `asin(x)` | $[-\pi/2,\ \pi/2]$ |
| $\arccos(x)$ | `acos(x)` | $[0,\ \pi]$ |
| $\arctan(x)$ | `atan(x)` | $(-\pi/2,\ \pi/2)$ |
| $\arctan(y/x)$ | `atan2(y, x)` | $(-\pi,\ \pi]$ |

**Samtliga funktioner arbetar i radianer, aldrig i grader.** `sin(30)` tolkas som $\sin(30\ \text{rad})$ och ger $-0{,}988$, inte $0{,}5$.

### Omvandling mellan grader och radianer

```math
\text{rad} = \text{grader} \cdot \frac{\pi}{180}, \qquad
\text{grader} = \text{rad} \cdot \frac{180}{\pi}
```

```c
const double deg = 30.0;
const double rad = deg * PI / 180.0;
printf("sin(30 grader) = %.3f\n", sin(rad)); // 0.500
```

### atan2 i stället för atan
`atan(y / x)` kan inte skilja på kvadrant 1 och 3, eller på kvadrant 2 och 4, eftersom tecknen försvinner i divisionen. `atan2(y, x)` tar emot $y$ och $x$ var för sig och ger därför rätt vinkel i alla fyra kvadranter. Använd alltid `atan2()` vid omvandling från rektangulär till polär form (L15).

---

## 5. Potenser, logaritmer och decibel
Från L10 gäller för spänning respektive effekt:

```math
A_{\text{dB}} = 20\log_{10}\!\left(\frac{U_{\text{ut}}}{U_{\text{in}}}\right), \qquad
A_{\text{dB}} = 10\log_{10}\!\left(\frac{P_{\text{ut}}}{P_{\text{in}}}\right)
```

```c
const double gain_db = 20.0 * log10(u_out / u_in);
```

Vägen tillbaka från decibel till förhållande:

```math
\frac{U_{\text{ut}}}{U_{\text{in}}} = 10^{A_{\text{dB}}/20}
```

```c
const double ratio = pow(10.0, gain_db / 20.0);
```

Logaritmer med annan bas beräknas via basbytesregeln $\log_b x = \dfrac{\ln x}{\ln b}$:

```c
const double log2_x = log(x) / log(2.0);
```

---

## 6. Numerisk derivering
Derivatan definieras som gränsvärdet

```math
f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
```

En dator kan inte låta $h \to 0$, men med ett litet $h$ fås ett approximativt värde. **Centraldifferensen** ger bättre noggrannhet än formeln ovan eftersom felen på var sida om $x$ tar ut varandra:

```math
f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}
```

```c
double derivative(double (*f)(double), const double x, const double h)
{
    return (f(x + h) - f(x - h)) / (2.0 * h);
}
```

Anropet sker med en funktionspekare, det vill säga namnet på den funktion som ska deriveras:

```c
const double slope = derivative(square, 3.0, 1e-6);
```

### Val av h
* Ett för **stort** $h$ ger ett metodfel – approximationen ligger för långt från gränsvärdet.
* Ett för **litet** $h$ ger ett avrundningsfel – $f(x + h)$ och $f(x - h)$ blir så lika att de signifikanta siffrorna försvinner i subtraktionen.

För `double` är $h \approx 10^{-6}$ en bra kompromiss.

---

## 7. Numerisk integrering
Den bestämda integralen motsvarar arean under kurvan (L14). Delas intervallet $[a, b]$ upp i $n$ lika delar med bredden $h = \dfrac{b - a}{n}$, kan arean approximeras med **trapetsmetoden**:

```math
\int_a^b f(x)\,dx \approx h\left[\frac{f(a) + f(b)}{2} + \sum_{k=1}^{n-1} f(a + kh)\right]
```

Varje delintervall approximeras alltså med ett trapets i stället för en rektangel, vilket följer kurvan betydligt bättre. Noggrannheten ökar med antalet delintervall $n$.

```c
double integral(double (*f)(double), const double a, const double b, const int n)
{
    const double h = (b - a) / n;
    double sum     = (f(a) + f(b)) / 2.0;

    for (int k = 1; k < n; ++k)
    {
        sum += f(a + k * h);
    }
    return sum * h;
}
```

För ett förstagradspolynom ger trapetsmetoden ett **exakt** resultat, eftersom kurvan då är en rät linje. För övriga funktioner uppstår ett fel som minskar när $n$ ökar.

---

## 8. Komplexa tal med complex.h
Komplexa tal (L15–L17) hanteras av `complex.h`, som används tillsammans med `math.h`:

```c
#include <complex.h>
#include <math.h>
```

Typen heter `double complex` och den imaginära enheten heter `I`:

```c
const double complex z = 3.0 + 4.0 * I;
```

**OBS!** Inom elektrotekniken skrivs den imaginära enheten $j$ för att inte förväxlas med strömmen $i$. I C heter den alltid `I`.

### Funktioner

| Matematik | C-funktion | Beskrivning |
|-----------|------------|-------------|
| $\text{Re}(z)$ | `creal(z)` | Realdelen |
| $\text{Im}(z)$ | `cimag(z)` | Imaginärdelen |
| $\lvert z \rvert$ | `cabs(z)` | Beloppet |
| $\arg(z)$ | `carg(z)` | Argumentet i radianer, $(-\pi,\ \pi]$ |
| $\bar{z}$ | `conj(z)` | Konjugatet |
| $e^z$ | `cexp(z)` | Exponentialfunktionen |
| $\sqrt{z}$ | `csqrt(z)` | Kvadratroten |

De fyra räknesätten skrivs som vanligt med `+`, `-`, `*` och `/`.

### Rektangulär och polär form
Från rektangulär till polär form:

```c
const double magnitude = cabs(z);        // |z|
const double angle     = carg(z);        // arg(z) i radianer
```

Från polär till rektangulär form används Eulers formel $z = r e^{j\theta}$:

```c
const double complex z = r * cexp(I * theta);
```

**OBS!** `printf()` kan inte skriva ut ett komplext tal direkt. Real- och imaginärdel skrivs ut var för sig:

```c
printf("z = %.2f + %.2fj\n", creal(z), cimag(z));
```

---

## 9. Impedans och fasorer
Med komplexa tal beräknas impedanser direkt i kod (L16–L17). Med vinkelfrekvensen $\omega = 2\pi f$ gäller:

```math
Z_R = R, \qquad Z_L = j\omega L, \qquad Z_C = \frac{1}{j\omega C} = -\frac{j}{\omega C}
```

```c
const double omega          = 2.0 * PI * f;
const double complex z_r    = r;
const double complex z_l    = I * omega * l;
const double complex z_c    = -I / (omega * c);
const double complex z_tot  = z_r + z_l; // Seriekoppling.
```

En fasor $U = |U| \angle \delta$ skrivs som ett komplext tal på polär form. Addition av fasorer sker då med vanlig addition:

```c
const double complex u1 = a1 * cexp(I * d1);
const double complex u2 = a2 * cexp(I * d2);
const double complex u  = u1 + u2;
```

Resultatets amplitud och fasvinkel fås sedan med `cabs()` respektive `carg()`.

---

## 10. Sampling av en sinussignal
En sinusformad spänning beskrivs av

```math
u(t) = |U| \sin(2\pi f t + \delta),
```

där $|U|$ är amplituden i V, $f$ frekvensen i Hz, $t$ tiden i s och $\delta$ fasvinkeln i rad.

Vid **sampling** beräknas signalens värde vid jämnt fördelade tidpunkter. Med samplingsfrekvensen $f_s$ blir antalet sampel per period

```math
N = \frac{f_s}{f},
```

och det $k$:te sampelvärdet ($k = 0, 1, \ldots, N-1$) ges av

```math
u_k = |U| \sin\!\left(\frac{2\pi k}{N} + \delta\right).
```

För att signalen ska gå att återskapa ur sina sampel måste **samplingsteoremet** vara uppfyllt:

```math
f_s > 2f
```

```c
for (int k = 0; k < n; ++k)
{
    const double u_k = amplitude * sin(2.0 * PI * k / n + delta);
    printf("%d,%.6f\n", k, u_k);
}
```

### Utskrift för vidare analys
Skrivs sampelvärdena ut som **CSV** (kommaseparerade värden), en rad per sampel, kan de läsas in i ett annat program för att ritas upp:

```text
k,u
0,0.000000
1,3.535534
2,5.000000
```

I OnlineGDB markeras utskriften i utdatarutan och kopieras in i ett kalkylprogram, där signalen kan ritas upp som ett diagram.

Körs programmet på egen dator kan utskriften i stället sparas direkt till en fil genom omdirigering i terminalen:

```bash
./samples > samples.csv
```

Filen kan sedan öppnas i ett kalkylprogram, eller matas in i en simulator som ritar upp signalen.

---

## 11. Vanliga fallgropar

| Fallgrop | Konsekvens | Åtgärd |
|----------|------------|--------|
| Glömd `-lm` | `undefined reference to 'sqrt'` | Lägg flaggan sist vid kompilering, eller under *Extra Compiler Flags* i OnlineGDB |
| Grader i stället för radianer | Helt fel värde från `sin()`, `cos()`, `tan()` | Multiplicera med $\pi/180$ |
| Heltalsdivision, t.ex. `1 / 2` | Ger `0`, inte `0.5` | Skriv `1.0 / 2.0` |
| `atan(y / x)` vid polär form | Fel kvadrant | Använd `atan2(y, x)` |
| Jämförelse med `==` mellan flyttal | Ger sällan sant | Jämför med `fabs(a - b) < 1e-9` |
| `sqrt()` eller `log()` med otillåtet argument | Ger `nan` respektive `-inf` | Kontrollera argumentet först |
| `%d` för en `double` | Odefinierat beteende | Använd `%f`, exempelvis `%.3f` |

---

## 12. Typexempel

### Typexempel 1 – Effekt och decibel
En förstärkare har inspänningen $U_{\text{in}} = 0{,}5$ V och utspänningen $U_{\text{ut}} = 8{,}0$ V. Beräkna förstärkningen i dB.

**Lösning:**

```math
A_{\text{dB}} = 20\log_{10}\!\left(\frac{8{,}0}{0{,}5}\right) = 20\log_{10}(16) \approx 24{,}1\ \text{dB}
```

I kod:

```c
const double gain_db = 20.0 * log10(8.0 / 0.5); // 24.082 db.
```

---

### Typexempel 2 – Numerisk derivering
Derivera $f(x) = x^2$ i punkten $x = 3$ och jämför med den analytiska derivatan.

**Lösning:**

Analytiskt gäller $f'(x) = 2x$, alltså $f'(3) = 6$.

Numeriskt med $h = 10^{-6}$:

```math
f'(3) \approx \frac{(3{,}000001)^2 - (2{,}999999)^2}{2 \cdot 10^{-6}} = 6{,}000000
```

Avvikelsen ligger i storleksordningen $10^{-9}$ och beror på flyttalens ändliga precision.

---

### Typexempel 3 – Numerisk integrering
Strömmen $i(t) = 2t + 4$ A passerar under $0 \leq t \leq 2$ s. Beräkna laddningen $q$.

**Lösning:**

Analytiskt (L14):

```math
q = \int_0^2 (2t + 4)\,dt = \left[t^2 + 4t\right]_0^2 = 4 + 8 = 12\ \text{C}
```

Trapetsmetoden med $n = 4$ och $h = 0{,}5$:

```math
q \approx 0{,}5\left[\frac{4 + 8}{2} + (5 + 6 + 7)\right] = 0{,}5 \cdot 24 = 12\ \text{C}
```

Resultatet blir exakt, eftersom $i(t)$ är en rät linje.

---

### Typexempel 4 – Impedans i en RL-krets
En resistor $R = 100\ \Omega$ är seriekopplad med en spole $L = 50$ mH. Beräkna kretsens impedans vid $f = 50$ Hz.

**Lösning:**

```math
\omega = 2\pi \cdot 50 \approx 314{,}16\ \text{rad/s}
```

```math
Z = R + j\omega L = 100 + j15{,}71\ \Omega
```

```math
|Z| = \sqrt{100^2 + 15{,}71^2} \approx 101{,}23\ \Omega, \qquad
\arg(Z) = \arctan\!\left(\frac{15{,}71}{100}\right) \approx 0{,}156\ \text{rad} \approx 8{,}93^\circ
```

I kod beräknas beloppet och argumentet med `cabs(z)` respektive `carg(z)`.

---

### Typexempel 5 – Sampelvärden
En signal $u(t) = 5\sin(2\pi \cdot 50t)$ V samplas med $f_s = 400$ Hz. Beräkna de tre första sampelvärdena.

**Lösning:**

```math
N = \frac{400}{50} = 8 \text{ sampel per period}
```

```math
u_0 = 5\sin(0) = 0\ \text{V}
```

```math
u_1 = 5\sin\!\left(\frac{2\pi}{8}\right) = 5\sin\!\left(\frac{\pi}{4}\right) \approx 3{,}54\ \text{V}
```

```math
u_2 = 5\sin\!\left(\frac{2\pi \cdot 2}{8}\right) = 5\sin\!\left(\frac{\pi}{2}\right) = 5{,}00\ \text{V}
```

Samplingsteoremet är uppfyllt, eftersom $400 > 2 \cdot 50$.

---
