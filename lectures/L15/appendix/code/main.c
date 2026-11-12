/**
 * @file Complex numbers on rectangular and polar form, implementation of exercise 4.1.
 */
#include <math.h>
#include <stdio.h>

/** Half a turn: pi radians correspond to 180 degrees. */
#define PI_DEG 180.0

/** Exponent used with pow() to square a number. */
#define SQUARE 2.0

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
    // z1 = 3 + j4 and z2 = -2 - j3 are created on rectangular form, z3 = 10 < 45 on polar form.
    const complex_t z1 = {3.0, 4.0};
    const complex_t z2 = {-2.0, -3.0};
    const complex_t z3 = complex_from_polar(10.0, 45.0);

    // Print each number on both rectangular and polar form.
    complex_print(&z1);
    complex_print(&z2);
    complex_print(&z3);
    return 0;
}
