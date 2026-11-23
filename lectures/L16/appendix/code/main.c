/**
 * @file Rotation of a complex number by multiplication with j, implementation of exercise 4.1.
 */
#include <math.h>
#include <stdint.h>
#include <stdio.h>

/** Half a turn: pi radians correspond to 180 degrees. */
#define PI_DEG 180.0

/** Exponent used with pow() to square a number. */
#define SQUARE 2.0

/** Number of multiplications with j. Four quarter turns make a whole turn. */
#define ROTATIONS 4U

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
 * @brief Multiply a complex number with j, which rotates it a quarter turn anticlockwise.
 *
 *        Since j^2 = -1, j(a + jb) = ja + j^2 b = -b + ja: the new real part is the old imaginary
 *        part with the opposite sign, and the new imaginary part is the old real part.
 *
 * @param[in] z The complex number to rotate.
 *
 * @return The rotated number jz. The number z itself is not changed.
 */
static complex_t complex_rotate_j(const complex_t* z)
{
    const double im   = z->re;
    const double re   = -z->im;
    complex_t rotated = {re, im};
    return rotated;
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
    // Start with z = 3 + j4 and print it before the first multiplication.
    complex_t z = {3.0, 4.0};
    complex_print(&z);

    // Multiply z with j four times and print the number after each multiplication. The result
    // is assigned back to z, since complex_rotate_j() returns a new number.
    for (uint8_t i = 0U; i < ROTATIONS; ++i)
    {
        z = complex_rotate_j(&z);
        complex_print(&z);
    }
    return 0;
}
