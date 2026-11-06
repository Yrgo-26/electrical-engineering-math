/**
 * @file Numerical integration, implementation of exercise 4.1.
 */
#include <math.h>
#include <stddef.h>
#include <stdio.h>

/** Exact values of the integrals, computed with antiderivatives. */
#define EXACT_2X 4.0                 // [x^2] from 0 to 2 = 4.
#define EXACT_SIN 2.0                // [-cos(x)] from 0 to pi = 2.
#define EXACT_E_2X 3.194528049465325 // [e^(2x) / 2] from 0 to 1 = (e^2 - 1) / 2.

/** Math function alias. */
typedef double (*math_func_t)(double);

/**
 * @brief Approximate the integral of f(x) from a to b with a sum of rectangles.
 *
 * @param[in] f Function to integrate.
 * @param[in] a Lower limit of integration.
 * @param[in] b Upper limit of integration.
 * @param[in] n Number of rectangles. Must be greater than 0.
 *
 * @return The approximate integral, or -1.0 if n is 0.
 */
static double integrate(math_func_t f, const double a, const double b, size_t n)
{
    // Check the number of samples, return -1.0 if invalid.
    if (0U == n)
    {
        printf("Cannot divide by 0!\n");
        return -1.0;
    }

    // Compute the step value to use.
    const double dx = (b - a) / n;
    double area     = 0.0;

    // Take 'n' samples, accumulate all f(x) values, iterate in steps of dx.
    for (size_t i = 0U; i < n; ++i)
    {
        area += f(a + i * dx);
    }
    return area * dx;
}

/**
 * @brief Compute f(x) = 2x.
 *
 * @param[in] x Function input.
 *
 * @return Function output f(x).
 */
static inline double two_x(const double x) { return 2.0 * x; }

/**
 * @brief Compute f(x) = e^(2x).
 *
 * @param[in] x Function input.
 *
 * @return Function output f(x).
 */
static inline double e_2x(const double x) { return pow(M_E, 2.0 * x); }

/**
 * @brief Integrate the given function once per number of rectangles and print the results.
 *
 * @param[in] func Function to integrate.
 * @param[in] samples Array holding the numbers of rectangles to test.
 * @param[in] sample_count Number of elements in the samples array.
 * @param[in] a Lower limit of integration.
 * @param[in] b Upper limit of integration.
 * @param[in] exact Exact value of the integral, used to compute the error.
 * @param[in] output The function as text for the printout, such as "sin(x)".
 */
static void test_integration(math_func_t func, const size_t* samples, const size_t sample_count,
                             const double a, const double b, const double exact, const char* output)
{
    printf("--------------------------------------------------------------------------------\n");
    printf("Integrating f(x) = %s:\n", output);

    // Integrate with each sample found in the samples array, print the approximated area and
    // the error, i.e. the distance to the exact value.
    for (size_t i = 0U; i < sample_count; ++i)
    {
        const size_t n    = samples[i];
        const double area = integrate(func, a, b, n);
        printf("Samples = %zu, area = %g, error = %g\n", n, area, fabs(area - exact));
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
    const size_t samples[]    = {4U, 10U, 100U, 1000U};
    const size_t sample_count = sizeof(samples) / sizeof(size_t);

    test_integration(two_x, samples, sample_count, 0.0, 2.0, EXACT_2X, "2x");
    test_integration(sin, samples, sample_count, 0.0, M_PI, EXACT_SIN, "sin(x)");
    test_integration(e_2x, samples, sample_count, 0.0, 1.0, EXACT_E_2X, "e^2x");
    return 0;
}
