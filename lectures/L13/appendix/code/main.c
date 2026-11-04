/**
 * @file Implementation of exercise 4.
 */
#include <math.h>
#include <stdio.h>

#define H_STEP 1e-6 // h value for derivatives.

/** Math function alias. */
typedef double (*math_func_t)(double);

/**
 * @brief Derive with the given function and input.
 *
 * @param[in] f Function to use.
 * @param[in] x Function input.
 *
 * @return The slope of the function, i.e. f'(x).
 */
static inline double derive(math_func_t f, const double x)
{
    const double y1 = f(x);
    const double y2 = f(x + H_STEP);
    return (y2 - y1) / H_STEP;
}

/**
 * @brief Compute f(x) = e^x.
 *
 * @param[in] x Input value.
 *
 * @return Computed output value f(x) = e^x.
 */
static inline double e_x(const double x) { return pow(M_E, x); }

/**
 * @brief Compute f(x) = 2^x.
 *
 * @param[in] x Input value.
 *
 * @return Computed output value f(x) = 2^x.
 */
static inline double two_x(const double x) { return pow(2.0, x); }

/**
 * @brief Derive f(x) = e^x for inputs x = [0.0, 4.0].
 */
static void derive_e_x(void)
{
    printf("--------------------------------------------------------------------------------\n");
    printf("Test f(x) = e^x for x = [0, 4]:\n\n");

    for (double x = 0.0; x <= 4.0; ++x)
    {
        const double y     = e_x(x);
        const double slope = derive(e_x, x);
        printf("f(%g) = %g, f'(%g) = %g\n", x, y, x, slope);
    }
    printf("--------------------------------------------------------------------------------\n\n");
}

/**
 * @brief Derive f(v) = sin(v) for inputs v = [-1.0, 1.0].
 */
static void derive_sinv(void)
{
    printf("--------------------------------------------------------------------------------\n");
    printf("Test f(v) = sin(v) for v = [-1, 1], expect f'(v) = cos(v):\n\n");

    for (int i = -5; i <= 5; ++i)
    {
        const double v     = i * 0.2;
        const double sinv  = sin(v);
        const double cosv  = cos(v);
        const double slope = derive(sin, v);
        printf("sin(%g) = %g, cos(%g) = %g, f'(%g) = %g\n", v, sinv, v, cosv, v, slope);
    }
    printf("--------------------------------------------------------------------------------\n\n");
}

/**
 * @brief Derive f(x) = 2^x for inputs x = [0.0, 4.0].
 */
static void derive_2_x(void)
{
    printf("--------------------------------------------------------------------------------\n");
    printf("Test f(x) = 2^x for x = [0, 4], expect f'(x) = 2^x * ln(2)\n\n");
    for (double x = 0.0; x <= 4.0; ++x)
    {
        const double y     = two_x(x);
        const double slope = derive(two_x, x);
        printf("f(%g) = %g, f'(%g) = %g, 2^%g * ln(2) = %g\n", x, y, x, slope, x, y * log(2.0));
    }
    printf("--------------------------------------------------------------------------------\n\n");
}

/**
 * @brief Derive f(x) = log(x) for inputs x = [1.0, 5.0].
 */
static void derive_logx(void)
{
    printf("--------------------------------------------------------------------------------\n");
    printf("Test f(x) = log10(x) for x = [1, 5], expect f'(x) = 1 / (x * ln(10))\n\n");

    for (double x = 1.0; x <= 5.0; ++x)
    {
        const double y        = log10(x);
        const double slope    = derive(log10, x);
        const double expected = 1.0 / (x * log(10.0));
        printf("f(%g) = %g, f'(%g) = %g, 1 / (%g * ln(10)) = %g\n", x, y, x, slope, x, expected);
    }
    printf("--------------------------------------------------------------------------------\n\n");
}

/**
 * @brief Application entry point.
 *
 * @return 0 on termination of the program.
 */
int main(void)
{
    derive_e_x();
    derive_sinv();
    derive_2_x();
    derive_logx();
    return 0;
}
