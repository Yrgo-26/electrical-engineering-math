/**
 * @file Digital-to-Analog Converter (DAC) driver for AVR32DB28.
 */
#ifndef DAC_H_
#define DAC_H_

#include <stdbool.h>
#include <stdint.h>

/**
 * @brief Initialize DAC.
 */
void dac_init(void);

/**
 * @brief Write sample value to DAC.
 *
 * @param[in] sample 10-bit sample value.
 *
 * @return True on success, false if the sample value is invalid.
 */
bool dac_write(uint16_t sample);

/**
 * @brief Read the current DAC sample value.
 *
 * @return Current 10-bit DAC value.
 */
uint16_t dac_read(void);

#endif /* DAC_H_ */
