# Kod för L16 – Rotation med j i C
Programmet multiplicerar det komplexa talet $z = 3 + j4$ med $j$ fyra gånger och skriver ut talet på både rektangulär och polär form före den första multiplikationen och efter varje multiplikation, se uppgift 4.1 i [bilaga B](../b_exercises.md). Programmet bygger vidare på koden från L15, som förklaras i [L15:s kod-README](../../../L15/appendix/code/README.md).

---

## Idén
Den imaginära enheten uppfyller $j^2 = -1$. Multipliceras talet $z = a + jb$ med $j$ blir resultatet

```math
jz = j(a + jb) = ja + j^2 b = -b + ja
```

Den nya realdelen är alltså den gamla imaginärdelen med omvänt tecken, och den nya imaginärdelen är den gamla realdelen. Geometriskt vrids talet ett kvarts varv, $90^{\circ}$, moturs i det komplexa talplanet, medan beloppet är oförändrat. Fyra kvarts varv blir ett helt varv, vilket stämmer med att

```math
j^4 = (j^2)^2 = (-1)^2 = 1
```

---

## Så fungerar koden

### Från L15
Strukten `complex_t` och funktionerna `to_deg()`, `complex_magnitude()`, `complex_angle_deg()` och `complex_print()` är desamma som i L15 och förklaras i [L15:s kod-README](../../../L15/appendix/code/README.md). Funktionerna tar emot talet via en pekare och kontrollerar inte att pekaren är skild från `NULL`. Det är utelämnat för att hålla koden enkel.

### Konstanten `ROTATIONS`

```c
#define ROTATIONS 4U
```

`ROTATIONS` är antalet multiplikationer med $j$. Fyra kvarts varv blir ett helt varv, så efter den sista multiplikationen ska talet vara tillbaka där det startade. Suffixet `U` gör konstanten till ett heltal utan tecken, precis som loopvariabeln den jämförs med.

### Funktionen `complex_rotate_j()`

```c
static complex_t complex_rotate_j(const complex_t* z)
{
    const double im   = z->re;
    const double re   = -z->im;
    complex_t rotated = {re, im};
    return rotated;
}
```

Funktionen beräknar $jz = -b + ja$: den nya imaginärdelen är den gamla realdelen, och den nya realdelen är den gamla imaginärdelen med omvänt tecken. Resultatet sparas i en ny strukt, `rotated`, som returneras. Parametertypen `const complex_t*` anger att funktionen inte ändrar talet `z`, så det roterade talet kan bara nå anroparen via returvärdet.

### Funktionen `main()`

```c
complex_t z = {3.0, 4.0};
complex_print(&z);

for (uint8_t i = 0U; i < ROTATIONS; ++i)
{
    z = complex_rotate_j(&z);
    complex_print(&z);
}
```

Talet $z = 3 + j4$ skrivs först ut som det är. Sedan multipliceras det med $j$ fyra gånger, och efter varje multiplikation skrivs det nya talet ut. Returvärdet från `complex_rotate_j()` tilldelas tillbaka till `z` med `z =`, så att nästa varv i loopen roterar det redan roterade talet. Därför deklareras `z` utan `const`. Loopvariabeln har typen `uint8_t` från `stdint.h`, ett heltal utan tecken på åtta bitar, vilket räcker gott för fyra varv.

---

## Utskrift

```
--------------------------------------------------------------------------------
Rectangular form:	Z = 3 + j4
Polar form:		    Z = 5 < 53.1301
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
Rectangular form:	Z = -4 + j3
Polar form:		    Z = 5 < 143.13
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
Rectangular form:	Z = -3 - j4
Polar form:		    Z = 5 < -126.87
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
Rectangular form:	Z = 4 - j3
Polar form:		    Z = 5 < -36.8699
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
Rectangular form:	Z = 3 + j4
Polar form:		    Z = 5 < 53.1301
--------------------------------------------------------------------------------

```

**Argumentet** ökar med $90^{\circ}$ vid varje multiplikation: från $53{,}13^{\circ}$ till $143{,}13^{\circ}$, $233{,}13^{\circ}$ och $323{,}13^{\circ}$. `atan2()` ger vinkeln mellan $-180^{\circ}$ och $180^{\circ}$, så $233{,}13^{\circ}$ skrivs ut som $-126{,}87^{\circ}$ och $323{,}13^{\circ}$ som $-36{,}87^{\circ}$. Det är samma riktningar, eftersom $233{,}13^{\circ} - 360^{\circ} = -126{,}87^{\circ}$.

**Beloppet** är $5$ hela tiden, eftersom en rotation inte ändrar talets längd.

**Efter fyra multiplikationer** är talet tillbaka i $3 + j4$, vilket stämmer med att $j^4 = 1$ (uppgift 4.1 c).

---

## Utan tilldelning (uppgift 4.1 d)
Ändras anropet i loopen till

```c
complex_rotate_j(&z);
```

alltså utan `z =`, skrivs $3 + j4$ ut alla fem gångerna. `complex_rotate_j()` tar emot talet som `const complex_t*` och kan därför inte ändra `z`. Den returnerar i stället det roterade talet som ett nytt tal, och utan `z =` tas returvärdet aldrig om hand. Kompilatorn varnar inte för detta, inte ens med `-Wall`, så det är ett misstag som är lätt att göra.

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
