
/**
 * @brief Math project application.
 */
#include <stdint.h>

#include "driver/dac.h"
#include "driver/sampler.h"

/** Sample frequency in Hz. */
#define SAMPLE_FREQ_HZ 1000U

/**
 * @brief Get the number of elements in the given array.
 *
 * @param[in] arr The array in question.
 *
 * @return Number of elements in the given array.
 */
#define ARR_SIZE(arr) (sizeof((arr)) / sizeof((arr)[0U]))

/**
 * @brief Application entry point.
 *
 * @return 0 on termination of the program (should never occur).
 */
int main(void)
{
    // Create example samples.
    const uint16_t samples[]    = {10U, 20U, 30U, 40U, 50U};
    const uint16_t sample_count = ARR_SIZE(samples);

    // Initialize the hardware.
    dac_init();
    sampler_init(samples, sample_count, SAMPLE_FREQ_HZ);

    // Keep program running as long as voltage is supplied.
    while (1)
        ;
    return 0;
}
