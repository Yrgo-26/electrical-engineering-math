# Practice exam 1

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
3I_1 - I_2 = 7 \\
3I_2 = I_1 + 3
\end{cases}
```

---

### Question 2 (2.0 points)
A battery with the open-circuit voltage $E = 24\thinspace V$ and the internal resistance $R_i = 6\thinspace\Omega$ is connected to a load with the resistance $R$. The power $P$ developed in the load is given by

```math
P = \frac{E^2 R}{(R + R_i)^2}
```

**a)** Find the load resistance $R$ such that the power in the load is $P = 18\thinspace W$. The equation has two solutions.

**b)** Calculate the current $I = \frac{E}{R + R_i}$ for each solution. Which solution is preferable if the battery is to last as long as possible? Justify your answer.

---

### Question 3 (1.5 points)
The voltage $U$ in volts across a component depends on the current $I$ in amperes as

```math
U(I) = \frac{4I^2 - 36}{I^2 - I - 6}
```

**a)** Simplify the expression and state which values of $I$ it is not defined for.

**b)** Calculate the voltage $U$ when the current is $I = 2\thinspace A$.

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

A capacitor with the capacitance $680\thinspace\mu F$ is connected to a $10\thinspace\text{k}\Omega$ resistor. It is initially charged to $10\thinspace V$ and starts to discharge at time $t = 0$.

**a)** Calculate the voltage after three seconds.

**b)** Find the function's domain and range for the time interval $0 - 10$ seconds.

**c)** Calculate how long it takes for the voltage to fall to 40 % of its original value.

---

### Question 5 (1.0 points)
An AC voltage has the amplitude $5\thinspace V$, the frequency $100\thinspace Hz$ and the phase 90°.

**a)** Find the equation $u(t)$ of the AC voltage. Give the phase in radians.

**b)** Draw the sine wave of the AC voltage over one period $T$.

---

### Question 6 (2.0 points)
The battery in Question 2, with the open-circuit voltage $E = 24\thinspace V$ and the internal resistance $R_i = 6\thinspace\Omega$, delivers the current $I$ to a load. The terminal voltage is $U = E - R_i I$, so the power in the load as a function of the current is

```math
P(I) = U \cdot I = (24 - 6I) \cdot I = 24I - 6I^2
```

**a)** Differentiate the function $P(I)$ and find the expression for $P'(I)$.

**b)** Find where the function is stationary, i.e. solve $P'(I) = 0$.

**c)** Use the second derivative to decide whether the point is a maximum or a minimum.

**d)** Calculate the largest or smallest value of the function, i.e. find $P(I)$ at the point where the function is stationary.

**e)** Draw the graph of $P(I)$ for the interval $0 \leq I \leq 4\thinspace A$. Mark the turning point and the points where the graph crosses the axes.

**f)** Calculate the load resistance $R = \frac{U}{I}$ at the stationary point and compare it with $R_i$.

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

The current $i(t)$ in a capacitor is given by the following function:

```math
i(t) = 0.03t^2 + 0.1t + 0.5
```

where $t$ is the time in seconds. The capacitor already has the charge $q_0 = 1\thinspace C$ at the start.

**a)** Find an expression for the antiderivative $I(t) = \int i(t)\thinspace dt$, i.e. integrate without any limits.

**b)** Find an expression for the charge $q(t)$ of the capacitor by integrating over the interval $[0, t]$.

**c)** Find a formula for the total charge $q_{tot}(t)$ in the capacitor, including the initial charge $q_0$.

**d)** How much total charge (including the initial charge) has flowed into the capacitor after 4 seconds?

---

### Question 8 (2.0 points)
A circuit is supplied with the voltage $U = 3 - j4\thinspace V$. The circuit has the impedance $Z = 2 + j2\thinspace\Omega$. The current $I$ through the circuit can be calculated with "Ohm's law", that is, Ohm's law adapted to complex numbers:

```math
I = \frac{U}{Z}
```

**a)** Calculate the current $I$ and give it in both rectangular and polar form.

**b)** The impedance can be written $Z = R + jX$. State the resistance $R$ and the reactance $X$, and decide whether the circuit is inductive or capacitive.

**c)** The frequency is $f = 50\thinspace Hz$. Calculate the inductance or capacitance that gives the circuit's reactance.

---

### Question 9 (1.5 points)
A current $i(t)$ in an AC circuit can be represented by a phasor $I$, which in rectangular form is written as below:

```math
I = 10 - j5\,mA
```

**a)** Draw the phasor $I$ in the complex plane (x-axis = real part, y-axis = imaginary part).

**b)** Express the phasor $I$ in Euler form, i.e. find the magnitude $|I|$ and the phase angle $\delta$ such that $I = |I|e^{j\delta}$.

**c)** Assume that the frequency of the current is $f = 10\thinspace Hz$. Find the angular frequency $w$.

**d)** Write $i(t)$ as a function of time $i(t) = |I| \cdot e^{j(wt+\delta)}$.

---

### Question 10 (2.0 points)
In a series connection of three components, the AC voltage across each component is measured as:

```math
u_1(t) = 2\sin(wt + 25°)\,V
```

```math
u_2(t) = 5\sin(wt - 45°)\,V
```

```math
u_3(t) = 1.5\sin(wt + 36°)\,V
```

The total voltage in the circuit $u_{tot}(t)$ is calculated as below:

```math
u_{tot}(t) = u_1(t) + u_2(t) + u_3(t)
```

**a)** Rewrite the voltages $u_1(t)$, $u_2(t)$ and $u_3(t)$ as phasors $U_1$, $U_2$ and $U_3$ in complex rectangular form.

**b)** Calculate the phasor sum $U_{tot} = U_1 + U_2 + U_3$.

**c)** Draw the phasors in the complex plane (x-axis = real part, y-axis = imaginary part).

**d)** Convert the result back to a sinusoidal voltage in the time domain, in the following form:

```math
u_{tot}(t) = |U_{tot}| \sin(wt + \delta_{tot})
```

---
