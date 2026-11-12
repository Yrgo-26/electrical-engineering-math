# Practice exam 2

## Permitted aids
* Writing materials and a calculator of any kind.
* One A4 sheet (both sides), handwritten or typed, with formulas, examples and notes of your own choice.

> **NOTE!** Mobile phones may not be used while the exam is in progress and must be left in the place indicated.

## Points
16 points in total. On top of that, up to 1.0 bonus point can be earned from tests 1–2.

## Grade thresholds
* IG < 6.5 points
* G >= 6.5 points
* VG >= 11 points

## Other
Every question requires a solution and a justification with a stated answer (including the unit where relevant). In other words, you must explain how you arrived at your results! Good luck!

---

### Question 1 (1.0 points)
Solve the system of equations below to calculate the currents $I_1$ and $I_2$, in $mA$:

```math
\begin{cases}
2I_1 + 3I_2 = 16 \\
4I_1 = I_2 + 4
\end{cases}
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

### Question 3 (1.5 points)
The voltage $U$ in volts across a component depends on the current $I$ in amperes as

```math
U(I) = \frac{3I^2 - 3I - 18}{I^2 - 9}
```

**a)** Simplify the expression and state which values of $I$ it is not defined for.

**b)** Find the current $I$ when the voltage is $U = 2.7\thinspace V$.

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

### Question 5 (1.0 points)
An AC voltage is described by the following function:

```math
u(t) = 325 \sin\left(100\pi t + \frac{\pi}{6}\right)\,V
```

**a)** State the voltage's amplitude, RMS value, frequency, period and phase. The RMS value is given by $U_{RMS} = \frac{|U|}{\sqrt{2}}$. Give the phase in degrees.

**b)** Draw the sine wave of the AC voltage over one period $T$.

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

### Question 8 (2.0 points)
A resistor $R = 30\thinspace\Omega$ and an inductor with the reactance $X_L = 40\thinspace\Omega$ are connected in series and supplied with the voltage $U = 100\angle 0°\thinspace V$. The current $I$ through the circuit can be calculated with "Ohm's law", that is, Ohm's law adapted to complex numbers:

```math
I = \frac{U}{Z}
```

**a)** Find the impedance $Z = R + jX_L$ of the circuit and give it in both rectangular and polar form.

**b)** Calculate the current $I$ and give it in both polar and rectangular form.

**c)** The frequency is $f = 50\thinspace Hz$. Calculate the inductance $L$ of the inductor, where $X_L = \omega L$.

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
