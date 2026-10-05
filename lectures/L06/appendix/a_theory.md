# Bilaga A – Andragradsekvationer

## 1. Definition
En **andragradsekvation** (kvadratisk ekvation) är en ekvation på formen:

```math
ax^2 + bx + c = 0, \quad a \neq 0
```

Koefficienterna $a$, $b$ och $c$ är reella tal. Ekvationen kan ha **0, 1 eller 2 reella rötter**.

**Exempel:** $2x^2 - 3x - 5 = 0$ är en andragradsekvation med $a=2$, $b=-3$, $c=-5$.

---

## 2. Lösningsmetoder
### 2.1 Faktoriseringsmetoden
Om $ax^2 + bx + c$ kan faktoriseras till $a(x - r_1)(x - r_2)$ är rötterna $x = r_1$ och $x = r_2$.

**Exempel:** Lös $x^2 - 5x + 6 = 0$.

Faktorisera: $(x-2)(x-3) = 0$

Rötterna ges av: $x - 2 = 0$ eller $x - 3 = 0$

```math
x_1 = 2, \quad x_2 = 3
```

**Exempel (konjugatregeln):** Lös $x^2 - 9 = 0$.

```math
(x+3)(x-3) = 0 \quad \Rightarrow \quad x = -3 \text{ eller } x = 3
```

### 2.2 PQ-formeln
Gäller för ekvationer på *normerad* form $x^2 + px + q = 0$ (dvs. $a = 1$):

```math
x = -\frac{p}{2} \pm \sqrt{\left(\frac{p}{2}\right)^2 - q}
```

**Exempel:** Lös $x^2 - 4x + 3 = 0$ ($p = -4$, $q = 3$):

```math
x = \frac{4}{2} \pm \sqrt{\left(\frac{4}{2}\right)^2 - 3} = 2 \pm \sqrt{4 - 3} = 2 \pm 1
```

```math
x_1 = 3, \quad x_2 = 1
```

Uttrycket under rottecknet kallas **diskriminanten** och avgör antalet reella rötter: är det positivt finns två rötter, är det noll sammanfaller de till en dubbelrot, och är det negativt saknas reella rötter.

**Alternativ form:** PQ-formeln kan också användas genom att flytta över allt utom $x^2$ till högerledet, så att ekvationen står på formen $x^2 = px + q$. Då sätts $p$ och $q$ in i formeln med de tecken de har i högerledet:

```math
x^2 = px + q \quad \Rightarrow \quad x = \frac{p}{2} \pm \sqrt{\left(\frac{p}{2}\right)^2 + q}
```

**Exempel:** Lös $x^2 + 2x + 2 = 26$. Flytta över allt utom $x^2$ till högerledet:

```math
x^2 = -2x + 24 \quad (p = -2, \; q = 24)
```

```math
x = \frac{-2}{2} \pm \sqrt{\left(\frac{-2}{2}\right)^2 + 24} = -1 \pm \sqrt{1 + 24} = -1 \pm 5
```

```math
x_1 = 4, \quad x_2 = -6
```

De två formerna ger samma räkning; $p$ och $q$ har bara motsatta tecken. Välj den form du föredrar och håll dig till den.

**Om $a \neq 1$:** Dividera först alla termer med $a$, så att ekvationen blir normerad.

**Exempel:** Lös $2x^2 + 5x - 3 = 0$. Dividera med $2$:

```math
x^2 + 2{,}5x - 1{,}5 = 0 \quad (p = 2{,}5, \; q = -1{,}5)
```

```math
x = -1{,}25 \pm \sqrt{1{,}25^2 + 1{,}5} = -1{,}25 \pm \sqrt{3{,}0625} = -1{,}25 \pm 1{,}75
```

```math
x_1 = 0{,}5, \quad x_2 = -3
```

### 2.3 Kvadratkomplettering
Varje andragradsekvation kan skrivas på formen $(x + k)^2 = m$ genom att "komplettera till en kvadrat".

**Procedur för $x^2 + bx + c = 0$:**
1. Flytta konstanten: $x^2 + bx = -c$
2. Lägg till $\left(\dfrac{b}{2}\right)^2$ på båda sidor
3. Vänsterledet blir en perfekt kvadrat

**Exempel:** Lös $x^2 + 6x + 5 = 0$:

```math
x^2 + 6x = -5
```

Lägg till $\left(\frac{6}{2}\right)^2 = 9$:

```math
x^2 + 6x + 9 = -5 + 9 = 4
```

```math
(x + 3)^2 = 4 \quad \Rightarrow \quad x + 3 = \pm 2 \quad \Rightarrow \quad x_1 = -1, \quad x_2 = -5
```

---

## 3. Tillämpning i elektroteknik
### Ström från effekt och resistans
Effekten i ett motstånd $R$ ges av $P = RI^2$. Givet $P$ och $R$ kan strömmen $I$ beräknas:

```math
RI^2 = P \quad \Rightarrow \quad I^2 = \frac{P}{R} \quad \Rightarrow \quad I = \sqrt{\frac{P}{R}}
```

Det är en *ren* andragradsekvation (ingen linjär term).

**Exempel:** $P = 8\thinspace\text{W}$, $R = 50\thinspace\Omega$:

```math
I = \sqrt{\frac{8}{50}} = \sqrt{0{,}16} = 0{,}4\,\text{A}
```

### Resistans från seriekoppling
Två motstånd $R_1$ och $R_2$ är seriekopplade med $R_1 + R_2 = 10\thinspace\Omega$ och $R_1 \cdot R_2 = 24\thinspace\Omega^2$. Lös ut $R_2 = 10 - R_1$ ur den första ekvationen och sätt in i den andra:

```math
R_1(10 - R_1) = 24 \quad \Rightarrow \quad R_1^2 - 10R_1 + 24 = 0
```

PQ-formeln ger:

```math
R_1 = 5 \pm \sqrt{25 - 24} = 5 \pm 1
```

Roten $R_1 = 6\thinspace\Omega$ ger $R_2 = 10 - 6 = 4\thinspace\Omega$. Den andra roten, $R_1 = 4\thinspace\Omega$, ger samma par i omvänd ordning:

```math
R_1 = 6\,\Omega, \quad R_2 = 4\,\Omega
```

---

## 4. Sammanfattning

| Metod | Bäst när... |
|-------|-------------|
| Faktorisering | Heltalsrötter kan identifieras snabbt |
| PQ-formeln | Generell tillämpning; normera först om $a \neq 1$ |
| Kvadratkomplettering | Härledning av formler och förståelse av processen |

```math
\boxed{x = -\frac{p}{2} \pm \sqrt{\left(\frac{p}{2}\right)^2 - q}}
```

---

## 5. Extra – ABC-formeln
ABC-formeln (kvadratiska formeln) är ett alternativ till PQ-formeln som ingår som överkurs. Den ger samma rötter, men kan användas direkt på $ax^2 + bx + c = 0$ utan att ekvationen först normeras.

```math
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
```

**Exempel:** Lös $2x^2 + 5x - 3 = 0$ ($a=2$, $b=5$, $c=-3$):

```math
x = \frac{-5 \pm \sqrt{5^2 - 4 \cdot 2 \cdot (-3)}}{2 \cdot 2} = \frac{-5 \pm \sqrt{49}}{4} = \frac{-5 \pm 7}{4} \quad \Rightarrow \quad x_1 = 0{,}5, \quad x_2 = -3
```

Rötterna är desamma som PQ-formeln gav för samma ekvation i avsnitt 2.2.

---
