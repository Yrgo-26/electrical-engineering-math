/**
 * @file Sampler driver implementation details for AVR32DB28.
 */
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include <avr/interrupt.h>
#include <avr/io.h>

#include "driver/dac.h"
#include "driver/sampler.h"

/** CPU frequency in Hz. */
#define F_CPU 4000000UL

/** Minimum supported sample frequency in Hz. */
#define FREQ_MIN 65U

/** Maximum supported sample frequency in Hz. */
#define FREQ_MAX 10000U

/**
 * @brief Sample structure.
 */
typedef struct
{
    /** Sample entries. */
    const uint16_t* samples;

    /** Number of sample entries. */
    uint16_t count;

    /** Index of the next entry. */
    uint16_t next;
} sample_reg_t;

// -----------------------------------------------------------------------------
static inline void sample_reg_save(sample_reg_t* self, const uint16_t* samples,
                                   const uint16_t sample_count)
{
    self->samples = samples;
    self->count   = sample_count;
    self->next    = 0U;
}

// -----------------------------------------------------------------------------
static inline uint16_t sample_reg_get_next(sample_reg_t* self)
{
    // Retrieve the next sample, wrap around the next sample index.
    const uint16_t sample = self->samples[self->next++];
    self->next            = self->next % self->count;

    // Return the retrieved sample.
    return sample;
}

// -----------------------------------------------------------------------------
static inline bool is_freq_valid(const uint16_t freq_hz)
{
    return (FREQ_MIN <= freq_hz) && (FREQ_MAX >= freq_hz);
}

// -----------------------------------------------------------------------------
static inline uint16_t compute_period(const uint16_t freq_hz)
{
    return (uint16_t)(F_CPU / freq_hz - 1U);
}

/** Sample structure. */
static sample_reg_t sample_reg = {NULL, 0U, 0U};

// -----------------------------------------------------------------------------
bool sampler_init(const uint16_t* samples, const uint16_t sample_count, const uint16_t freq_hz)
{
    // Check the samples, return false on failure.
    if ((NULL == samples) || (0U == sample_count)) { return false; }

    // Check the sample frequency, return false if outside the supported range.
    if (!is_freq_valid(freq_hz)) { return false; }

    // Save samples.
    sample_reg_save(&sample_reg, samples, sample_count);

    // Initialize sample timer.
    TCA0.SINGLE.CTRLB   = TCA_SINGLE_WGMODE_NORMAL_gc;
    TCA0.SINGLE.PER     = compute_period(freq_hz);
    TCA0.SINGLE.INTCTRL = TCA_SINGLE_OVF_bm;
    TCA0.SINGLE.CTRLA   = TCA_SINGLE_CLKSEL_DIV1_gc | TCA_SINGLE_ENABLE_bm;

    // Enable interrupts globally, then return true to indicate success.
    sei();
    return true;
}

// -----------------------------------------------------------------------------
ISR(TCA0_OVF_vect)
{
    // Clear the overflow interrupt flag.
    TCA0.SINGLE.INTFLAGS = TCA_SINGLE_OVF_bm;

    // Write the next sample value.
    const uint16_t sample = sample_reg_get_next(&sample_reg);
    dac_write(sample);
}
