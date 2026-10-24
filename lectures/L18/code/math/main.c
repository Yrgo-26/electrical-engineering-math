/**
 * @file Math lab example program.
 */
#include <stdio.h>

/**
 * @brief Divide two numbers.
 *
 * @param[in] x Dividend.
 * @param[in] y Divisor.
 *
 * @return The quotient x / y, or 0 if the divisor is 0.
 */
static inline double divide(const double x, const double y) { return 0.0 != y ? x / y : 0.0; }

/**
 * @brief Application entry point.
 *
 * @return 0 on termination of the program.
 */
int main(void)
{
    const double x = 3.4;
    const double y = 2.0;
    const double q = divide(x, y);
    printf("%g / %g = %g\n", x, y, q);
    return 0;
}
