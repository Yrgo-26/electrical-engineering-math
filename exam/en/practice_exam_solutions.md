# Worked solutions to the practice exam

### Question 1 (1.0 points)
Solve the system of equations below to calculate the currents $I_1$ and $I_2$, in $mA$:

```math
\begin{cases}
3I_1 - I_2 = 7 \\
3I_2 = I_1 + 3
\end{cases}
```

---

### Solution
We start by solving the first equation for $I_2$:

```math
3I_1 - I_2 = 7 \quad \Rightarrow \quad I_2 = 3I_1 - 7
```

We substitute the expression for $I_2$ into the second equation:

```math
3(3I_1 - 7) = I_1 + 3,
```

which can be simplified to

```math
9I_1 - 21 = I_1 + 3 \quad \Rightarrow \quad 8I_1 = 24 \quad \Rightarrow \quad I_1 = 3
```

We substitute $I_1 = 3$ into the expression for $I_2$:

```math
I_2 = 3 \cdot 3 - 7 = 2
```

**Check:** In the first equation the left-hand side is $3 \cdot 3 - 2 = 7$, which matches the right-hand side. In the second equation the left-hand side is $3 \cdot 2 = 6$ and the right-hand side is $3 + 3 = 6$.

**Answer:**

```math
I_1 = 3\,mA, \quad I_2 = 2\,mA
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

### Solution
**a)** We substitute the given values:

```math
18 = \frac{24^2 \cdot R}{(R + 6)^2} = \frac{576R}{(R + 6)^2}
```

We multiply both sides by $(R + 6)^2$, which is allowed since $R > 0$, so the denominator is never zero:

```math
18(R + 6)^2 = 576R
```

Dividing both sides by 18 gives

```math
(R + 6)^2 = 32R
```

We expand the square on the left-hand side:

```math
R^2 + 12R + 36 = 32R \quad \Rightarrow \quad R^2 - 20R + 36 = 0
```

We solve the equation with the PQ-formula ($p = -20$, $q = 36$):

```math
R = 10 \pm \sqrt{10^2 - 36} = 10 \pm \sqrt{64} = 10 \pm 8
```

This means that

```math
\begin{cases}
R_1 = 10 + 8 = 18\,\Omega \\
R_2 = 10 - 8 = 2\,\Omega
\end{cases}
```

**Check:** For $R = 18\thinspace\Omega$ we get $P = \frac{576 \cdot 18}{24^2} = 18\thinspace W$, and for $R = 2\thinspace\Omega$ we get $P = \frac{576 \cdot 2}{8^2} = 18\thinspace W$.

**b)** For $R = 18\thinspace\Omega$ the current is

```math
I = \frac{24}{18 + 6} = 1\,A
```

and for $R = 2\thinspace\Omega$

```math
I = \frac{24}{2 + 6} = 3\,A
```

The load gets the same power in both cases, but with $R = 18\thinspace\Omega$ it draws only a third of the current. The internal resistance then dissipates $R_i I^2 = 6 \cdot 1^2 = 6\thinspace W$ instead of $6 \cdot 3^2 = 54\thinspace W$, so far less energy is lost as heat in the battery.

**Answer:** a) $R = 2\thinspace\Omega$ or $R = 18\thinspace\Omega$. b) $I = 3\thinspace A$ and $1\thinspace A$ respectively. $R = 18\thinspace\Omega$ is preferable, since it gives the same power with a third of the current.

---

### Question 3 (1.5 points)
The voltage $U$ in volts across a component depends on the current $I$ in amperes as

```math
U(I) = \frac{4I^2 - 36}{I^2 - I - 6}
```

**a)** Simplify the expression and state which values of $I$ it is not defined for.

**b)** Calculate the voltage $U$ when the current is $I = 2\thinspace A$.

---

### Solution
**a)** We factorise the numerator by taking out 4 and using the difference of two squares:

```math
4I^2 - 36 = 4(I^2 - 9) = 4(I + 3)(I - 3)
```

To find which values $I$ cannot take, we look at when the denominator becomes zero:

```math
I^2 - I - 6 = 0
```

We solve the equation with the PQ-formula ($p = -1$, $q = -6$):

```math
I = \frac{1}{2} \pm \sqrt{\left(\frac{1}{2}\right)^2 + 6} = 0.5 \pm \sqrt{6.25} = 0.5 \pm 2.5
```

The denominator is therefore zero for $I = 3$ and $I = -2$, which means that

```math
I \neq 3, \quad I \neq -2
```

With these zeros, the denominator can be factorised as $I^2 - I - 6 = (I - 3)(I + 2)$. We substitute the factorised numerator and denominator:

```math
U(I) = \frac{4(I + 3)(I - 3)}{(I - 3)(I + 2)}
```

For $I \neq 3$ we can cancel the factor $(I - 3)$, which appears in both the numerator and the denominator:

```math
U(I) = \frac{4(I + 3)}{I + 2}
```

**b)** We substitute $I = 2$ into the simplified expression:

```math
U(2) = \frac{4(2 + 3)}{2 + 2} = \frac{20}{4} = 5\,V
```

**Check:** With the original expression, $U(2) = \frac{4 \cdot 4 - 36}{4 - 2 - 6} = \frac{-20}{-4} = 5\thinspace V$.

**Answer:** a) $U(I) = \frac{4(I + 3)}{I + 2}$, where $I \neq -2$ and $I \neq 3$. b) $U(2) = 5\thinspace V$.

---

### Question 4 (1.5 points)
When a capacitor discharges through a resistor, the voltage across the capacitor decreases exponentially with time. The voltage $u(t)$ can be described by the following function:

```math
u(t) = U_0 e^{-t/(RC)}
```

A capacitor with the capacitance $680\thinspace\mu F$ is connected to a $10\thinspace\text{k}\Omega$ resistor. It is initially charged to $10\thinspace V$ and starts to discharge at time $t = 0$.

**a)** Calculate the voltage after three seconds.

**b)** Find the function's domain and range for the time interval $0 - 10$ seconds.

**c)** Calculate how long it takes for the voltage to fall to 40 % of its original value.

---

### Solution
**a)** With the given values, the formula above can be rewritten as below:

```math
u(t) = 10 e^{-t/(680\mu \cdot 10\text{k})} = 10 e^{-t/6.8}\,V
```

We calculate $u(3)$ to find the voltage after three seconds:

```math
u(3) = 10 e^{-3/6.8} \approx 6.43\,V
```

**b)** The domain is given in the question:

```math
0 \leq t \leq 10\,s
```

The range is found by calculating $u(0)$ and $u(10)$:

```math
u(0) = 10 e^{-0/6.8} = 10 \cdot e^0 = 10\,V
```

```math
u(10) = 10 e^{-10/6.8} \approx 2.30\,V
```

This means that

```math
2.30\,V \leq u(t) \leq 10\,V
```

**c)** To find the time $t$ at which the voltage has fallen to 40 % of the original value $10\thinspace V$, we set $u(t) = 10 \cdot 0.4 = 4\thinspace V$:

```math
u(t) = 10 e^{-t/6.8} = 4
```

Dividing both sides by 10 turns the expression above into

```math
e^{-t/6.8} = 0.4
```

To solve for $t$, we take the natural logarithm $\ln$ of both sides:

```math
-\frac{t}{6.8} = \ln 0.4
```

Multiplying both sides by $-6.8$ gives $t$:

```math
t = -6.8 \cdot \ln 0.4 \approx 6.23\,s
```

**Answer:** After about 6.23 seconds the voltage has fallen to 40 % of the original value.

---

### Question 5 (1.0 points)
An AC voltage has the amplitude $5\thinspace V$, the frequency $100\thinspace Hz$ and the phase 90°.

**a)** Find the equation $u(t)$ of the AC voltage. Give the phase in radians.

**b)** Draw the sine wave of the AC voltage over one period $T$.

---

### Solution
**a)** The formula for an AC voltage $u(t)$ is the following:

```math
u(t) = |U| \sin(wt + \delta),
```

where $|U|$ is the amplitude (peak value), $w$ is the angular frequency, $t$ is the time and $\delta$ is the phase.

According to the question, the amplitude (peak value) $|U|$ of the sine wave is $5\thinspace V$:

```math
|U| = 5\,V
```

According to the question, the frequency $f$ of the sine wave is $100\thinspace Hz$. The corresponding angular frequency $w$ is therefore $200\pi\thinspace\text{rad/s}$:

```math
w = 2\pi f = 2\pi \cdot 100 = 200\pi\,\text{rad/s}
```

According to the question, the phase $\delta$ is 90°, which corresponds to $\pi/2\thinspace\text{rad}$, since

```math
\delta_{rad} = \delta_{deg} \cdot \frac{\pi}{180°} = 90 \cdot \frac{\pi}{180} = \frac{90\pi}{180} = \frac{\pi}{2}\,\text{rad}
```

The AC voltage $u(t)$ is therefore given by the following:

```math
u(t) = 5 \sin\left(200\pi t + \frac{\pi}{2}\right)\,V
```

**b)** We start from the properties of the sine wave. Since the frequency $f$ is $100\thinspace Hz$, the period $T$ is $10\thinspace ms$:

```math
T = \frac{1}{f} = \frac{1}{100} = 0.01\,s = 10\,ms
```

We are therefore drawing a sine wave that repeats every 10 milliseconds. For a sine wave, the following holds:
* The voltage is 0 at the start of each cycle and after half a cycle.
* The maximum voltage $|U| = 5\thinspace V$ is reached after a quarter of a cycle.
* The minimum voltage $-|U| = -5\thinspace V$ is reached after three quarters of a cycle.

The phase $\delta$ is 90°, which means that the curve is $90°/360° = 1/4$, that is, a quarter of a cycle "ahead" along the x-axis. This corresponds to $2.5\thinspace ms$, since

```math
\frac{T}{4} = \frac{10\text{m}}{4} = 2.5\,ms
```

The sine wave therefore has the period $T = 10\thinspace ms$, starts at $u(0) = 5\sin(\pi/2) = 5\thinspace V$ (already at its maximum, since the phase is 90°), crosses zero at $t = 2.5\thinspace ms$ and $t = 7.5\thinspace ms$, and reaches its minimum $-5\thinspace V$ at $t = 5\thinspace ms$.

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

### Solution
**a)** We differentiate term by term:

```math
P'(I) = 24 - 12I
```

**b)** We solve $P'(I) = 0$:

```math
24 - 12I = 0 \quad \Rightarrow \quad 12I = 24 \quad \Rightarrow \quad I = \frac{24}{12} = 2\,A
```

**c)** We calculate the second derivative, that is, the derivative of $P'(I)$:

```math
P''(I) = -12
```

Since the second derivative is negative for all $I$, including $I = 2\thinspace A$, the point is a maximum:

```math
P''(2) = -12 < 0 \quad \Rightarrow \quad \text{maximum}
```

**d)** We calculate the maximum power by substituting $I = 2$ into the function:

```math
P(2) = 24 \cdot 2 - 6 \cdot 2^2 = 48 - 24 = 24\,W
```

The load can therefore get at most $24\thinspace W$ from the battery.

**e)** The zeros are given by $P(I) = 6I(4 - I) = 0$, that is, $I = 0$ and $I = 4\thinspace A$. In addition, $P(1) = 18\thinspace W$ and $P(3) = 18\thinspace W$. The graph is a downward-opening parabola with its maximum at $(2, 24)$, which crosses the $I$-axis at $(0, 0)$ and $(4, 0)$. At $I = 4\thinspace A$ the battery is short-circuited: the terminal voltage is zero, so no power is developed in the load.

The graph also shows why Question 2 has two solutions: the power $18\thinspace W$ is less than the maximum power $24\thinspace W$ and is reached at two currents, $I = 1\thinspace A$ and $I = 3\thinspace A$.

**f)** At the stationary point the terminal voltage is

```math
U = 24 - 6 \cdot 2 = 12\,V
```

and the load resistance is

```math
R = \frac{U}{I} = \frac{12}{2} = 6\,\Omega
```

The load resistance is therefore equal to the internal resistance $R_i = 6\thinspace\Omega$. The load gets the most power when $R = R_i$, which is called maximum power transfer.

**Answer:** The maximum power is $P(2) = 24\thinspace W$, reached at $I = 2\thinspace A$, that is, when $R = R_i = 6\thinspace\Omega$.

---

### Question 7 (1.5 points)
The charge $q(t)$ that passes through a conductor during the time interval $(0, t)$ can be calculated with the following function:

```math
q(t) = \int_0^t i(t)\,dt = \big[I(t)\big]_0^t,
```

where $I(t)$ is the antiderivative (indefinite integral) of $i(t)$. The current $i(t)$ in a capacitor is given by:

```math
i(t) = 0.03t^2 + 0.1t + 0.5
```

where $t$ is the time in seconds. The capacitor already has the charge $q_0 = 1\thinspace C$ at the start.

**a)** Find an expression for the antiderivative $I(t) = \int i(t)\thinspace dt$.

**b)** Find an expression for the charge $q(t)$ of the capacitor by integrating over the interval $[0, t]$.

**c)** Find a formula for the total charge $q_{tot}(t)$ in the capacitor, including the initial charge $q_0$.

**d)** How much total charge (including the initial charge) has flowed into the capacitor after 4 seconds?

---

### Solution
**a)** We find the antiderivative $I(t)$ by integrating $i(t)$ term by term, without any limits. The exponent of each term increases by one, and the term is divided by the new exponent:

```math
I(t) = \int \left(0.03t^2 + 0.1t + 0.5\right)dt = 0.03 \cdot \frac{t^3}{3} + 0.1 \cdot \frac{t^2}{2} + 0.5t + C,
```

which can be rewritten as

```math
I(t) = 0.01t^3 + 0.05t^2 + 0.5t + C
```

**Check:** Differentiating $I(t)$ gives $0.03t^2 + 0.1t + 0.5 = i(t)$.

**b)** We integrate the current $i(t)$ over the interval $(0, t)$:

```math
q(t) = \int_0^t i(t)\,dt = \big[I(t)\big]_0^t = \big[0.01t^3 + 0.05t^2 + 0.5t + C\big]_0^t
```

We expand $q(t)$. All terms at the lower limit become zero when $t = 0$, so only $C$ remains there:

```math
q(t) = \left(0.01t^3 + 0.05t^2 + 0.5t + C\right) - \left(0 + 0 + 0 + C\right) = 0.01t^3 + 0.05t^2 + 0.5t
```

**c)** To find a formula for the charge $q_{tot}(t)$, we must find the constant of integration $C$. We interpret the constant as the $C$ in the antiderivative $I(t)$, where $q_{tot}(t) = I(t) = 0.01t^3 + 0.05t^2 + 0.5t + C$, and find $q_{tot}(0) = I(0)$:

```math
q_{tot}(0) = I(0) = 0.01 \cdot 0^3 + 0.05 \cdot 0^2 + 0.5 \cdot 0 + C = C
```

According to the question, the initial charge is $q_{tot}(0) = q_0 = 1\thinspace C$. The constant of integration is therefore $C = 1$, and the total charge $q_{tot}(t)$ after a given time $t$ can be calculated with the following formula:

```math
q_{tot}(t) = 0.01t^3 + 0.05t^2 + 0.5t + 1
```

The same result is obtained by adding the initial charge $q_0 = 1\thinspace C$ to the charge $q(t)$ from b), which is counted from zero:

```math
q_{tot}(t) = q(t) + q_0 = 0.01t^3 + 0.05t^2 + 0.5t + 1
```

**d)** The total charge after 4 seconds is found by calculating $q_{tot}(4)$:

```math
q_{tot}(4) = 0.01 \cdot 4^3 + 0.05 \cdot 4^2 + 0.5 \cdot 4 + 1 = 0.64 + 0.8 + 2 + 1 = 4.44\,C
```

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

### Solution
**a)** To calculate the current $I$, the voltage $U$ and the impedance $Z$ must be converted to polar form.

We start by converting the voltage $U$, whose magnitude $|U|$ is calculated with Pythagoras' theorem:

```math
|U| = \sqrt{3^2 + (-4)^2} = \sqrt{9 + 16} = \sqrt{25} = 5\,V
```

We then calculate the phase angle $\delta_u$ of the voltage with $\tan^{-1}$:

```math
\delta_u = \tan^{-1}\left(\frac{-4}{3}\right) \pm k\pi \approx -0.9 \pm k\pi\,\text{rad} \approx -53.1° \pm k \cdot 180°
```

Since $U$ lies in the fourth quadrant ($270° \leq \delta_u \leq 360°$) and $-53.1° = 360° - 53.1° = 306.9°$, the calculated phase angle $\delta_u$ is correct. This means that

```math
U = 3 - j4 \approx 5\,\angle\,{-0.9}\,\text{rad}\,V
```

We then convert the impedance $Z$, whose magnitude $|Z|$ is calculated with Pythagoras' theorem:

```math
|Z| = \sqrt{2^2 + 2^2} = \sqrt{8} \approx 2.8\,\Omega
```

We then calculate the phase angle $\delta_z$ of the impedance with $\tan^{-1}$:

```math
\delta_z = \tan^{-1}\left(\frac{2}{2}\right) \pm k\pi \approx 0.8 \pm k\pi\,\text{rad} = 45° \pm k \cdot 180°
```

Since $Z$ lies in the first quadrant ($0° \leq \delta_z \leq 90°$), the calculated phase angle $\delta_z$ is correct. This means that

```math
Z = 2 + j2 \approx 2.8\,\angle\,0.8\,\text{rad}\,\Omega
```

We then calculate the current $I$ in polar form:

```math
I = \frac{U}{Z} \approx \frac{5\,\angle\,{-0.9}}{2.8\,\angle\,0.8} = \frac{5}{2.8}\,\angle\,(-0.9 - 0.8) \approx 1.8\,\angle\,{-1.7}\,\text{rad}\,A
```

The current can therefore be expressed in polar form as below:

```math
I \approx 1.8\,\angle\,{-1.7}\,\text{rad}\,A,
```

where the magnitude of the current is $|I| = 1.8\thinspace A$ and its phase angle is $\delta_i \approx -1.7\thinspace\text{rad} \approx -98.1°$.

We then convert the current to rectangular form, $I = I_{re} + jI_{im}$. We first calculate the real part $I_{re}$ with cosine:

```math
I_{re} = |I| \cdot \cos\delta_i \approx 1.8 \cdot \cos(-1.7) \approx -0.25\,A
```

We then calculate the imaginary part $I_{im}$ with sine:

```math
I_{im} = |I| \cdot \sin\delta_i \approx 1.8 \cdot \sin(-1.7) \approx -1.75\,A
```

**Answer:**

```math
I = -0.25 - j1.75\,A \approx 1.8\,\angle\,{-1.7}\,\text{rad}\,A
```

**b)** With $Z = 2 + j2$ the resistance is $R = 2\thinspace\Omega$ and the reactance is $X = 2\thinspace\Omega$. The reactance is positive, so the circuit is **inductive**.

**c)** For an inductor $X_L = \omega L$, where the angular frequency is

```math
\omega = 2\pi f = 2\pi \cdot 50 = 100\pi\,\text{rad/s}
```

We solve for the inductance:

```math
L = \frac{X_L}{\omega} = \frac{2}{100\pi} = \frac{1}{50\pi} \approx 6.37 \cdot 10^{-3}\,H = 6.37\,mH
```

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

### Solution
**a)** The phasor $I = 10 - j5\thinspace mA$ lies in the fourth quadrant of the complex plane (positive real part, negative imaginary part).

**b)** We first find the magnitude $|I|$ of the current with Pythagoras' theorem:

```math
|I| = \sqrt{10^2 + (-5)^2} = \sqrt{100 + 25} = \sqrt{125} \approx 11.2\,mA
```

We then find the phase angle $\delta$ with $\tan^{-1}$:

```math
\delta = \tan^{-1}\left(\frac{-5}{10}\right) \pm k\pi \approx -0.46 \pm k\pi\,\text{rad} \approx -26.6° \pm k \cdot 180°
```

Since $I$ lies in the fourth quadrant ($270° \leq \delta \leq 360°$) and $-26.6° = 360° - 26.6° = 333.4°$, the calculated phase angle $\delta$ is correct. We can then express the phasor $I$ in Euler form:

```math
I \approx 11.2 e^{-j0.46}\,mA
```

**c)** The angular frequency $w$ is calculated from the frequency $f = 10\thinspace Hz$:

```math
w = 2\pi f = 2\pi \cdot 10 = 20\pi\,\text{rad/s}
```

**d)** We insert the time component $wt$, where $w = 20\pi\thinspace\text{rad/s}$, into the expression for the phasor $I$ and get the following:

```math
i(t) \approx 11.2 e^{j(20\pi t - 0.46)}\,mA
```

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

**d)** Convert the result back to a sinusoidal voltage in the time domain, in the form $u_{tot}(t) = |U_{tot}| \sin(wt + \delta_{tot})$.

---

### Solution
**a)** We convert the sinusoidal voltages to the corresponding phasors one at a time:

```math
U_1 = 2\cos(25°) + j2\sin(25°) \approx 1.81 + j0.85\,V
```

```math
U_2 = 5\cos(-45°) + j5\sin(-45°) \approx 3.54 - j3.54\,V
```

```math
U_3 = 1.5\cos(36°) + j1.5\sin(36°) \approx 1.21 + j0.88\,V
```

**b)** We calculate the phasor sum $U_{tot}$ by adding the calculated phasors:

```math
U_{tot} \approx (1.81 + j0.85) + (3.54 - j3.54) + (1.21 + j0.88),
```

which can be rewritten as

```math
U_{tot} \approx 6.56 - j1.81\,V
```

**c)** The phasors $U_1$, $U_2$, $U_3$ and the sum $U_{tot}$ are drawn in the complex plane: $U_1$ and $U_3$ lie in the first quadrant, $U_2$ in the fourth quadrant, and the resultant $U_{tot}$ lies in the fourth quadrant just below the real axis.

**d)** We convert the phasor sum $U_{tot}$ to the corresponding sinusoidal voltage in the time domain:

```math
u_{tot}(t) = |U_{tot}| \sin(wt + \delta_{tot}),
```

where

```math
|U_{tot}| \approx \sqrt{6.56^2 + (-1.81)^2} \approx 6.81\,V
```

and

```math
\delta_{tot} = \tan^{-1}\left(\frac{-1.81}{6.56}\right) \pm k\pi \approx -0.27 \pm k\pi\,\text{rad} \approx -15.4° \pm k \cdot 180°
```

Since $U_{tot}$ lies in the fourth quadrant ($270° \leq \delta_{tot} \leq 360°$) and $-15.4° = 360° - 15.4° = 344.6°$, the calculated phase angle $\delta_{tot}$ is correct.

**Answer:**

```math
u_{tot}(t) \approx 6.81 \sin(wt - 15.4°)\,V
```

---
