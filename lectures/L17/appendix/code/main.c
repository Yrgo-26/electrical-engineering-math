/**
 * @file Phasor addition with complex numbers, implementation of exercise 4.1.
 */
#include <math.h>
#include <stdio.h>

/** Half a turn: pi radians correspond to 180 degrees. */
#define PI_DEG 180.0

/** Exponent used with pow() to square a number. */
#define SQUARE 2.0

/** Angular frequency 2 * pi * 50 Hz in rad/s. Any value works at t = 0, since then wt = 0. */
#define OMEGA (2.0 * M_PI * 50.0)

/**
 * @brief Complex number structure.
 */
typedef struct
{
    /** Real part (3 in z = 3 + j4). */
    double re;

    /** Imaginary part (4 in z = 3 + j4). */
    double im;
} complex_t;

/**
 * @brief Sinusoidal signal u(t) = |U|sin(wt + d).
 */
typedef struct
{
    /** Amplitude |U| (2 in u1(t) = 2sin(wt + 45)). */
    double amplitude;

    /** Angular frequency w in rad/s. */
    double omega;

    /** Phase d in degrees (45 in u1(t) = 2sin(wt + 45)). */
    double deg;
} sine_t;

/**
 * @brief Convert an angle from radians to degrees.
 *
 * @param[in] rad The angle in radians.
 *
 * @return The angle in degrees.
 */
static inline double to_deg(const double rad) { return rad * PI_DEG / M_PI; }

/**
 * @brief Convert an angle from degrees to radians.
 *
 * @param[in] deg The angle in degrees.
 *
 * @return The angle in radians.
 */
static inline double to_rad(const double deg) { return deg * M_PI / PI_DEG; }

/**
 * @brief Compute the magnitude |z| of a complex number with Pythagoras' theorem.
 *
 * @param[in] z The complex number.
 *
 * @return The magnitude of the number.
 */
static inline double complex_magnitude(const complex_t* z)
{
    const double re = pow(z->re, SQUARE);
    const double im = pow(z->im, SQUARE);
    return sqrt(re + im);
}

/**
 * @brief Compute the argument of a complex number in degrees.
 *
 * @param[in] z The complex number.
 *
 * @return The argument in degrees, between -180 and 180.
 */
static inline double complex_angle_deg(const complex_t* z)
{
    // atan2() takes the imaginary and the real part separately and sees the sign of both, so
    // the angle ends up in the right quadrant.
    const double rad = atan2(z->im, z->re);
    return to_deg(rad);
}

/**
 * @brief Create a complex number on rectangular form from polar form.
 *
 * @param[in] r The magnitude of the number.
 * @param[in] deg The argument in degrees.
 *
 * @return The complex number on rectangular form.
 */
static complex_t complex_from_polar(const double r, const double deg)
{
    const double rad = to_rad(deg);
    complex_t z;
    z.re = r * cos(rad);
    z.im = r * sin(rad);
    return z;
}

/**
 * @brief Add two complex numbers by adding the real parts and the imaginary parts separately.
 *
 * @param[in] a The first complex number.
 * @param[in] b The second complex number.
 *
 * @return The sum of the complex numbers.
 */
static complex_t complex_add(const complex_t* a, const complex_t* b)
{
    const double re   = a->re + b->re;
    const double im   = a->im + b->im;
    const complex_t z = {re, im};
    return z;
}

/**
 * @brief Compute the value |U|sin(wt + d) of a sinusoidal signal at a given time.
 *
 * @param[in] s The sinusoidal signal.
 * @param[in] t The time in seconds.
 *
 * @return The value of the signal at time t.
 */
static double sine_value(const sine_t* s, const double t)
{
    const double rad = to_rad(s->deg);
    return s->amplitude * sin(s->omega * t + rad);
}

/**
 * @brief Print a complex number on both rectangular and polar form, with the argument in degrees.
 *
 * @param[in] z The complex number to print.
 */
static void complex_print(const complex_t* z)
{
    // Print the sign of the imaginary part separately, followed by its absolute value, so that
    // the number is printed as -2 - j3 rather than -2 + j-3.
    const char ch     = 0.0 <= z->im ? '+' : '-';
    const double im   = fabs(z->im);
    const double magn = complex_magnitude(z);
    const double deg  = complex_angle_deg(z);

    printf("--------------------------------------------------------------------------------\n");
    printf("Rectangular form:\tZ = %g %c j%g\n", z->re, ch, im);
    printf("Polar form:\t\tZ = %g < %g\n", magn, deg);
    printf("--------------------------------------------------------------------------------\n\n");
}

/**
 * @brief Application entry point.
 *
 * @return 0 on termination of the program.
 */
int main(void)
{
    // The sine voltages u1(t) = 2sin(wt + 45) and u2(t) = 3sin(wt - 60).
    const sine_t u1 = {2.0, OMEGA, 45.0};
    const sine_t u2 = {3.0, OMEGA, -60.0};

    // The phasors U1 = 2 < 45 and U2 = 3 < -60, created from the amplitude and the phase of each
    // sine voltage.
    const complex_t a = complex_from_polar(u1.amplitude, u1.deg);
    const complex_t b = complex_from_polar(u2.amplitude, u2.deg);

    // Add the phasors on rectangular form and print the sum Utot on both rectangular and polar
    // form.
    const complex_t z = complex_add(&a, &b);
    complex_print(&z);

    // Exercise c): compute the sum of the sine voltages at t = 0, where sin(wt + d) = sin(d), and
    // compare it with the imaginary part of Utot.
    const double u0 = sine_value(&u1, 0.0) + sine_value(&u2, 0.0);
    printf("u1(0) + u2(0) = %g\n", u0);
    printf("Im(Utot)      = %g\n", z.im);
    return 0;
}
