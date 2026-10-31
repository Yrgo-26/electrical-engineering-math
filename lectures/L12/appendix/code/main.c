/**
 * @file Implementation of exercise 3.
 */
#include <stdio.h>

#define H_MIN 1e-6  // Minimum h value for the derivative.
#define H_MAX 1.0   // Maximum h value for the derivative.
#define H_STEP 10.0 // h divisor.

/**
 * @brief Compute the output of the function f, where f(x) = x^2.
 *
 * @param[in] x Input number.
 *
 * @return The corresponding output.
 */
static inline double f(const double x) { return x * x; }

/**
 * @brief Approximate f'(x) with the step h.
 *
 * @param[in] x The x coordinate.
 * @param[in] h Step size, must not be 0.
 *
 * @return Approximate f'(x).
 */
static inline double derive(const double x, const double h) { return (f(x + h) - f(x)) / h; }

/**
 * @brief Application entry point.
 *
 * @return 0 on termination of the program.
 */
int main(void)
{
    const double x = 3.0;

    for (double h = H_MAX; h >= H_MIN; h /= H_STEP)
    {
        const double slope = derive(x, h);
        printf("x = %g, f'(%g) = %g when h = %g\n", x, x, slope, h);
    }
    return 0;
}
