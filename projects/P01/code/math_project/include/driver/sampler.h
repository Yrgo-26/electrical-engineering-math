/**
 * @file Sampler driver for AVR32DB28.
 */
#ifndef SAMPLER_H_
#define SAMPLER_H_

#include <stdbool.h>
#include <stdint.h>

/**
 * @brief Initialize sampler.
 *
 * @param[in] samples Samples to write.
 * @param[in] sample_count Number of samples to write. Must be greater than 0.
 * @param[in] freq_hz Sample frequency in Hz. Must be in range [65, 10000].
 *
 * @return True on successful initialization, false on failure.
 */
bool sampler_init(const uint16_t* samples, uint16_t sample_count, uint16_t freq_hz);

#endif /* SAMPLER_H_ */