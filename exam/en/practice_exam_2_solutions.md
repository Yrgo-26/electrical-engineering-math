# Worked solutions to practice exam 2

### Question 1 (1.0 points)
Solve the system of equations below to calculate the currents $I_1$ and $I_2$, in $mA$:

```math
\begin{cases}
2I_1 + 3I_2 = 16 \\
4I_1 = I_2 + 4
\end{cases}
```

---

### Solution
We solve the second equation for $I_2$:

```math
4I_1 = I_2 + 4 \quad \Rightarrow \quad I_2 = 4I_1 - 4
```

We substitute the expression for $I_2$ into the first equation:

```math
2I_1 + 3(4I_1 - 4) = 16 \quad \Rightarrow \quad 14I_1 - 12 = 16 \quad \Rightarrow \quad I_1 = 2
```

We substitute $I_1 = 2$ into the expression for $I_2$:

```math
I_2 = 4 \cdot 2 - 4 = 4
```

**Check:** In the first equation the left-hand side is $2 \cdot 2 + 3 \cdot 4 = 16$. In the second equation the left-hand side is $4 \cdot 2 = 8$ and the right-hand side is $4 + 4 = 8$.

**Answer:**

```math
I_1 = 2\,mA, \quad I_2 = 4\,mA
```

---

### Question 2 (2.0 points)
A battery with the open-circuit voltage $E = 20\thinspace V$ and the internal resistance $R_i = 4\thinspace\Omega$ is connected to a load. The current is $I = \frac{E - U}{R_i}$, where $U$ is the terminal voltage, so the power in the load is given by

```math
P(U) = U \cdot I = \frac{U(20 - U)}{4}
```

**a)** Find the terminal voltage $U$ such that the power in the load is $P = 16\thinspace W$. The equation has two solutions.

**b)** Calculate the current $I$ and the load resistance $R = \frac{U}{I}$ for each solution. Which solution is preferable if the battery is to last as long as possible? Justify your answer.

---

### Solution
**a)** We set $P = 16$ and multiply both sides by 4:

```math
\frac{U(20 - U)}{4} = 16 \quad \Rightarrow \quad 20U - U^2 = 64 \quad \Rightarrow \quad U^2 - 20U + 64 = 0
```

We solve the equation with the PQ-formula ($p = -20$, $q = 64$):

```math
U = 10 \pm \sqrt{10^2 - 64} = 10 \pm \sqrt{36} = 10 \pm 6
```

This means that

```math
\begin{cases}
U_1 = 10 + 6 = 16\,V \\
U_2 = 10 - 6 = 4\,V
\end{cases}
```

**Check:** $P(16) = \frac{16 \cdot 4}{4} = 16\thinspace W$ and $P(4) = \frac{4 \cdot 16}{4} = 16\thinspace W$.

**b)** For $U = 16\thinspace V$ the current and the load resistance are

```math
I = \frac{20 - 16}{4} = 1\,A, \qquad R = \frac{16}{1} = 16\,\Omega
```

and for $U = 4\thinspace V$

```math
I = \frac{20 - 4}{4} = 4\,A, \qquad R = \frac{4}{4} = 1\,\Omega
```

The load gets the same power in both cases, but with $U = 16\thinspace V$ it draws only a quarter of the current. The internal resistance then dissipates $R_i I^2 = 4 \cdot 1^2 = 4\thinspace W$ instead of $4 \cdot 4^2 = 64\thinspace W$, so far less energy is lost as heat in the battery.

**Answer:** a) $U = 4\thinspace V$ or $U = 16\thinspace V$. b) $U = 16\thinspace V$ gives $I = 1\thinspace A$ and $R = 16\thinspace\Omega$, while $U = 4\thinspace V$ gives $I = 4\thinspace A$ and $R = 1\thinspace\Omega$. $U = 16\thinspace V$ is preferable.

---

### Question 3 (1.5 points)
The voltage $U$ in volts across a component depends on the current $I$ in amperes as

```math
U(I) = \frac{3I^2 - 3I - 18}{I^2 - 9}
```

**a)** Simplify the expression and state which values of $I$ it is not defined for.

**b)** Find the current $I$ when the voltage is $U = 2.7\thinspace V$.

---

### Solution
**a)** We factorise the denominator using the difference of two squares:

```math
I^2 - 9 = (I + 3)(I - 3)
```

The denominator is therefore zero for $I = \pm 3$, which means that

```math
I \neq 3, \quad I \neq -3
```

We take out 3 from the numerator and find the zeros of $I^2 - I - 6$ with the PQ-formula ($p = -1$, $q = -6$):

```math
I = \frac{1}{2} \pm \sqrt{\left(\frac{1}{2}\right)^2 + 6} = 0.5 \pm \sqrt{6.25} = 0.5 \pm 2.5
```

which gives $I = 3$ and $I = -2$, so $3I^2 - 3I - 18 = 3(I - 3)(I + 2)$. For $I \neq 3$ we can cancel the factor $(I - 3)$:

```math
U(I) = \frac{3(I - 3)(I + 2)}{(I + 3)(I - 3)} = \frac{3(I + 2)}{I + 3}
```

**b)** We set $U = 2.7$ and multiply both sides by $I + 3$:

```math
\frac{3(I + 2)}{I + 3} = 2.7 \quad \Rightarrow \quad 3I + 6 = 2.7I + 8.1 \quad \Rightarrow \quad 0.3I = 2.1 \quad \Rightarrow \quad I = 7
```

$I = 7$ is an allowed value.

**Check:** With the original expression, $U(7) = \frac{3 \cdot 49 - 21 - 18}{49 - 9} = \frac{108}{40} = 2.7\thinspace V$.

**Answer:** a) $U(I) = \frac{3(I + 2)}{I + 3}$, where $I \neq \pm 3$. b) $I = 7\thinspace A$.

---

### Question 4 (1.5 points)
When a capacitor discharges through a resistor, the voltage across the capacitor decreases exponentially with time. The voltage $u(t)$ can be described by the following function:

```math
u(t) = U_0 e^{-t/(RC)}
```

where

* $u(t)$ = the voltage across the capacitor at time $t$,
* $U_0$ = the initial voltage in $V$,
* $RC$ = the circuit's time constant in seconds,
* $t$ = the time in seconds.

A capacitor with the capacitance $100\thinspace\mu F$ discharges through a $100\thinspace\text{k}\Omega$ resistor from time $t = 0$. After 5 seconds the voltage is measured as $6.0\thinspace V$.

**a)** Calculate the time constant $RC$ of the circuit.

**b)** Find the initial voltage $U_0$.

**c)** Calculate how long it takes for the voltage to fall to half of $U_0$. Does the answer depend on $U_0$?

---

### Solution
**a)** The time constant is

```math
RC = 100 \cdot 10^3 \cdot 100 \cdot 10^{-6} = 10\,s
```

**b)** We set $u(5) = 6.0$ and solve for $U_0$:

```math
U_0 e^{-5/10} = 6.0 \quad \Rightarrow \quad U_0 = 6.0 \cdot e^{0.5} \approx 9.89\,V
```

**c)** We set $u(t) = \frac{U_0}{2}$ and divide both sides by $U_0$:

```math
U_0 e^{-t/10} = \frac{U_0}{2} \quad \Rightarrow \quad e^{-t/10} = 0.5
```

We take the natural logarithm $\ln$ of both sides:

```math
-\frac{t}{10} = \ln 0.5 \quad \Rightarrow \quad t = -10 \cdot \ln 0.5 = 10 \cdot \ln 2 \approx 6.93\,s
```

$U_0$ disappears when we divide, so the answer does not depend on the initial voltage. The voltage always halves after $RC \cdot \ln 2$, wherever it starts.

**Answer:** a) $RC = 10\thinspace s$. b) $U_0 \approx 9.89\thinspace V$. c) After about $6.93\thinspace s$, independent of $U_0$.

---

### Question 5 (1.0 points)
An AC voltage is described by the following function:

```math
u(t) = 325 \sin\left(100\pi t + \frac{\pi}{6}\right)\,V
```

**a)** State the voltage's amplitude, RMS value, frequency, period and phase. The RMS value is given by $U_{RMS} = \frac{|U|}{\sqrt{2}}$. Give the phase in degrees.

**b)** Draw the sine wave of the AC voltage over one period $T$.

---

### Solution
**a)** We compare with the general form $u(t) = |U|\sin(wt + \delta)$. The amplitude is $|U| = 325\thinspace V$, and the RMS value is

```math
U_{RMS} = \frac{325}{\sqrt{2}} \approx 230\,V
```

The angular frequency is $w = 100\pi\thinspace\text{rad/s}$, which gives

```math
f = \frac{w}{2\pi} = \frac{100\pi}{2\pi} = 50\,Hz, \qquad T = \frac{1}{f} = 0.02\,s = 20\,ms
```

The phase is $\delta = \frac{\pi}{6}\thinspace\text{rad} = 30°$. This is the ordinary mains voltage, $230\thinspace V$ at $50\thinspace Hz$.

**b)** The positive phase means that the curve is $\frac{30°}{360°} = \frac{1}{12}$ of a period, about $1.67\thinspace ms$, "ahead" of an ordinary sine wave. The curve starts at $u(0) = 325\sin 30° = 162.5\thinspace V$, reaches its maximum $325\thinspace V$ at $t \approx 3.33\thinspace ms$, crosses zero going down at $t \approx 8.33\thinspace ms$, reaches its minimum $-325\thinspace V$ at $t \approx 13.33\thinspace ms$, crosses zero going up at $t \approx 18.33\thinspace ms$ and is back at $162.5\thinspace V$ when $t = 20\thinspace ms$.

**Answer:** a) Amplitude $325\thinspace V$, RMS value about $230\thinspace V$, frequency $50\thinspace Hz$, period $20\thinspace ms$ and phase $30°$.

---

### Question 6 (2.0 points)
The current through an inductor varies during a measurement as

```math
i(t) = t^3 - 9t^2 + 24t\,mA,
```

where $t$ is the time in seconds and $0 \leq t \leq 5$.

**a)** Differentiate the function $i(t)$ and find the expression for $i'(t)$.

**b)** Find the times at which the function is stationary, i.e. solve $i'(t) = 0$.

**c)** Use the second derivative to decide whether each point is a maximum or a minimum.

**d)** Calculate the current at the stationary points.

**e)** Draw the graph of $i(t)$ for the interval $0 \leq t \leq 5\thinspace s$. Mark the turning points.

**f)** The voltage across the inductor is $u(t) = L \cdot i'(t)$. Calculate the voltage at time $t = 1\thinspace s$ if the inductance is $L = 0.5\thinspace H$.

---

### Solution
**a)** We differentiate term by term:

```math
i'(t) = 3t^2 - 18t + 24
```

**b)** We solve $i'(t) = 0$ and divide by 3:

```math
3t^2 - 18t + 24 = 0 \quad \Rightarrow \quad t^2 - 6t + 8 = 0
```

With the PQ-formula ($p = -6$, $q = 8$):

```math
t = 3 \pm \sqrt{3^2 - 8} = 3 \pm 1
```

The function is therefore stationary at $t = 2\thinspace s$ and $t = 4\thinspace s$.

**c)** The second derivative is

```math
i''(t) = 6t - 18
```

```math
i''(2) = -6 < 0 \quad \Rightarrow \quad \text{maximum}, \qquad i''(4) = 6 > 0 \quad \Rightarrow \quad \text{minimum}
```

**d)** We substitute the stationary points into the function:

```math
i(2) = 8 - 36 + 48 = 20\,mA, \qquad i(4) = 64 - 144 + 96 = 16\,mA
```

**e)** In addition, $i(0) = 0\thinspace mA$, $i(3) = 27 - 81 + 72 = 18\thinspace mA$ and $i(5) = 125 - 225 + 120 = 20\thinspace mA$. The graph starts at the origin, rises to the maximum $(2, 20)$, falls to the minimum $(4, 16)$ and then rises again to $(5, 20)$.

**f)** We calculate the derivative at $t = 1$:

```math
i'(1) = 3 - 18 + 24 = 9\,mA/s = 0.009\,A/s
```

The voltage is therefore

```math
u(1) = L \cdot i'(1) = 0.5 \cdot 0.009 = 0.0045\,V = 4.5\,mV
```

**Answer:** Maximum $i(2) = 20\thinspace mA$, minimum $i(4) = 16\thinspace mA$ and $u(1) = 4.5\thinspace mV$.

---

### Question 7 (1.5 points)
The charge $q(t)$ that passes through a conductor during the time interval $(0, t)$ can be calculated with the following function:

```math
q(t) = \int_0^t i(t)\,dt = \big[I(t)\big]_0^t,
```

where

* $q(t)$ is the charge through the conductor in $C$ (coulombs),
* $i(t)$ is the current through the conductor in $A$ (amperes),
* $I(t)$ is the antiderivative (indefinite integral) of $i(t)$.

The current $i(t)$ into a battery that is being charged is given by the following function:

```math
i(t) = 0.06t^2 + 0.4t + 1
```

where $t$ is the time in seconds.

**a)** Find an expression for the antiderivative $I(t) = \int i(t)\thinspace dt$, i.e. integrate without any limits.

**b)** Find an expression for the charge $q(t)$ by integrating over the interval $[0, t]$.

**c)** Calculate the charge that flows into the battery between $t = 2\thinspace s$ and $t = 5\thinspace s$.

**d)** Calculate the average current over the same interval, i.e. the charge divided by the length of the interval.

---

### Solution
**a)** We integrate term by term:

```math
I(t) = \int \left(0.06t^2 + 0.4t + 1\right)dt = 0.06 \cdot \frac{t^3}{3} + 0.4 \cdot \frac{t^2}{2} + t + C = 0.02t^3 + 0.2t^2 + t + C
```

**Check:** Differentiating $I(t)$ gives $0.06t^2 + 0.4t + 1 = i(t)$.

**b)** All terms become zero at the lower limit $t = 0$, so only $C$ remains there and cancels the constant at the upper limit:

```math
q(t) = \big[0.02t^3 + 0.2t^2 + t + C\big]_0^t = 0.02t^3 + 0.2t^2 + t
```

**c)** The charge between $t = 2$ and $t = 5$ is the definite integral over that interval:

```math
\int_2^5 i(t)\,dt = \big[0.02t^3 + 0.2t^2 + t\big]_2^5 = (2.5 + 5 + 5) - (0.16 + 0.8 + 2) = 12.5 - 2.96 = 9.54\,C
```

**d)** The interval is $5 - 2 = 3$ seconds long, so the average current is

```math
i_{avg} = \frac{9.54}{3} = 3.18\,A
```

**Answer:** a) $I(t) = 0.02t^3 + 0.2t^2 + t + C$. b) $q(t) = 0.02t^3 + 0.2t^2 + t$. c) $9.54\thinspace C$. d) $3.18\thinspace A$.

---

### Question 8 (2.0 points)
A resistor $R = 30\thinspace\Omega$ and an inductor with the reactance $X_L = 40\thinspace\Omega$ are connected in series and supplied with the voltage $U = 100\angle 0°\thinspace V$. The current $I$ through the circuit can be calculated with "Ohm's law", that is, Ohm's law adapted to complex numbers:

```math
I = \frac{U}{Z}
```

**a)** Find the impedance $Z = R + jX_L$ of the circuit and give it in both rectangular and polar form.

**b)** Calculate the current $I$ and give it in both polar and rectangular form.

**c)** The frequency is $f = 50\thinspace Hz$. Calculate the inductance $L$ of the inductor, where $X_L = \omega L$.

---

### Solution
**a)** The impedance in rectangular form is

```math
Z = R + jX_L = 30 + j40\,\Omega
```

The magnitude and the phase angle are

```math
|Z| = \sqrt{30^2 + 40^2} = \sqrt{2500} = 50\,\Omega, \qquad \delta_z = \tan^{-1}\left(\frac{40}{30}\right) \approx 53.1° \approx 0.93\,\text{rad}
```

$Z$ lies in the first quadrant, so the angle needs no correction: $Z \approx 50\angle 53.1°\thinspace\Omega$.

**b)** In division in polar form, the magnitudes are divided and the angles subtracted:

```math
I = \frac{U}{Z} \approx \frac{100\angle 0°}{50\angle 53.1°} = 2\angle{-53.1°}\,A
```

In rectangular form the current is

```math
I \approx 2\cos(-53.1°) + j2\sin(-53.1°) \approx 1.2 - j1.6\,A
```

**Check:** With the conjugate of the denominator, $I = \frac{100(30 - j40)}{30^2 + 40^2} = \frac{3000 - j4000}{2500} = 1.2 - j1.6\thinspace A$.

**c)** The angular frequency is $\omega = 2\pi f = 100\pi\thinspace\text{rad/s}$. We solve $X_L = \omega L$ for $L$:

```math
L = \frac{X_L}{\omega} = \frac{40}{100\pi} = \frac{2}{5\pi} \approx 0.127\,H = 127\,mH
```

**Answer:** a) $Z = 30 + j40 \approx 50\angle 53.1°\thinspace\Omega$. b) $I \approx 2\angle{-53.1°}\thinspace A = 1.2 - j1.6\thinspace A$. c) $L \approx 127\thinspace mH$.

---

### Question 9 (1.5 points)
A current $i(t)$ in an AC circuit can be represented by a phasor $I$, which in rectangular form is written as below:

```math
I = -8 - j6\,mA
```

**a)** Draw the phasor $I$ in the complex plane (x-axis = real part, y-axis = imaginary part).

**b)** Express the phasor $I$ in Euler form, i.e. find the magnitude $|I|$ and the phase angle $\delta$ such that $I = |I|e^{j\delta}$.

**c)** Assume that the frequency of the current is $f = 50\thinspace Hz$. Find the angular frequency $\omega$.

**d)** Write the current as a sinusoidal function of time, $i(t) = |I|\sin(\omega t + \delta)$.

---

### Solution
**a)** The phasor $I = -8 - j6\thinspace mA$ lies in the third quadrant of the complex plane (negative real part, negative imaginary part).

**b)** We first find the magnitude with Pythagoras' theorem:

```math
|I| = \sqrt{(-8)^2 + (-6)^2} = \sqrt{100} = 10\,mA
```

We then find the phase angle with $\tan^{-1}$:

```math
\delta = \tan^{-1}\left(\frac{-6}{-8}\right) \pm k\pi \approx 0.64 \pm k\pi\,\text{rad} \approx 36.9° \pm k \cdot 180°
```

$36.9°$ points into the first quadrant, but $I$ lies in the third. We therefore subtract $180°$:

```math
\delta \approx 36.9° - 180° = -143.1° \approx -2.50\,\text{rad}
```

This means that

```math
I \approx 10e^{-j2.50}\,mA
```

**c)** The angular frequency is

```math
\omega = 2\pi f = 2\pi \cdot 50 = 100\pi\,\text{rad/s}
```

**d)** With the amplitude $|I| = 10\thinspace mA$ and the phase $\delta \approx -2.50\thinspace\text{rad}$,

```math
i(t) \approx 10\sin(100\pi t - 2.50)\,mA
```

**Answer:** b) $I \approx 10e^{-j2.50}\thinspace mA$ ($\delta \approx -143.1°$). c) $\omega = 100\pi\thinspace\text{rad/s}$. d) $i(t) \approx 10\sin(100\pi t - 2.50)\thinspace mA$.

---

### Question 10 (2.0 points)
In a series connection of three components, the AC voltage across each component is measured as:

```math
u_1(t) = 4\sin(wt + 60°)\,V
```

```math
u_2(t) = 3\sin(wt - 30°)\,V
```

```math
u_3(t) = 2\sin(wt + 150°)\,V
```

The total voltage in the circuit $u_{tot}(t)$ is calculated as below:

```math
u_{tot}(t) = u_1(t) + u_2(t) + u_3(t)
```

**a)** Rewrite the voltages $u_1(t)$, $u_2(t)$ and $u_3(t)$ as phasors $U_1$, $U_2$ and $U_3$ in complex rectangular form.

**b)** Calculate the phasor sum $U_{tot} = U_1 + U_2 + U_3$.

**c)** Draw the phasors in the complex plane (x-axis = real part, y-axis = imaginary part).

**d)** Convert the result back to a sinusoidal voltage in the time domain, in the form $u_{tot}(t) = |U_{tot}|\sin(wt + \delta_{tot})$.

---

### Solution
**a)** We convert the sinusoidal voltages to phasors one at a time:

```math
U_1 = 4\cos(60°) + j4\sin(60°) \approx 2.000 + j3.464\,V
```

```math
U_2 = 3\cos(-30°) + j3\sin(-30°) \approx 2.598 - j1.500\,V
```

```math
U_3 = 2\cos(150°) + j2\sin(150°) \approx -1.732 + j1.000\,V
```

**b)** We add the real parts and the imaginary parts separately:

```math
U_{tot} \approx (2.000 + 2.598 - 1.732) + j(3.464 - 1.500 + 1.000) = 2.866 + j2.964\,V
```

**c)** $U_1$ lies in the first quadrant, $U_2$ in the fourth and $U_3$ in the second. The sum $U_{tot}$ lies in the first quadrant, roughly on the diagonal.

**d)** The magnitude and the phase angle are

```math
|U_{tot}| \approx \sqrt{2.866^2 + 2.964^2} \approx 4.12\,V
```

```math
\delta_{tot} = \tan^{-1}\left(\frac{2.964}{2.866}\right) \approx 46.0°
```

$U_{tot}$ lies in the first quadrant, so the angle needs no correction.

**Answer:**

```math
u_{tot}(t) \approx 4.12\sin(wt + 46.0°)\,V
```

---
