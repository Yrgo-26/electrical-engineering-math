/**
 * @file Digital-to-Analog Converter (DAC) driver implementation details for AVR32DB28.
 */
#include <stdbool.h>
#include <stdint.h>

#include <avr/io.h>

#include "driver/dac.h"

/** Port pin connected to the DAC. */
#define DAC_PIN_CTRL PORTD.PIN6CTRL

/** Shift required to align a 10-bit sample with the 16-bit DAC register. */
#define SAMPLE_SHIFT 6U

/** Maximum 10-bit sample value. */
#define SAMPLE_MAX 1023U

// -----------------------------------------------------------------------------
static inline bool is_sample_valid(const uint16_t sample) { return SAMPLE_MAX >= sample; }

// -----------------------------------------------------------------------------
void dac_init(void)
{
    // Set voltage reference for the DAC.
    VREF.DAC0REF = VREF_REFSEL_2V048_gc | VREF_ALWAYSON_bm;

    // Disable the digital input buffer on the DAC pin.
    DAC_PIN_CTRL &= ~PORT_ISC_gm;
    DAC_PIN_CTRL |= PORT_ISC_INPUT_DISABLE_gc;

    // Enable DAC.
    DAC0.CTRLA = DAC_ENABLE_bm | DAC_OUTEN_bm;
}

// -----------------------------------------------------------------------------
bool dac_write(const uint16_t sample)
{
    // Check sample value, return false if invalid.
    if (!is_sample_valid(sample)) { return false; }

    // Write sample value, then return true to indicate success.
    DAC0.DATA = sample << SAMPLE_SHIFT;
    return true;
}

// -----------------------------------------------------------------------------
uint16_t dac_read(void)
{
    // Convert the 16-bit register value back to a 10-bit sample.
    return (uint16_t)(DAC0.DATA >> SAMPLE_SHIFT);
}
