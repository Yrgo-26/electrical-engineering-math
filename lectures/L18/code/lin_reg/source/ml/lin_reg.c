/**
 * @file Linear regression model implementation details.
 */
#include <stdbool.h>
#include <stddef.h>

#include "ml/lin_reg.h"

#define LR_THRES_LOW 0.0  // Lower learning rate threshold.
#define LR_THRES_HIGH 1.0 // Upper learning rate threshold.

// -----------------------------------------------------------------------------
static inline bool lr_valid(const double lr) { return (LR_THRES_LOW < lr) && (LR_THRES_HIGH > lr); }

// -----------------------------------------------------------------------------
static inline bool train_data_valid(const train_data_t* self)
{
    return (NULL != self->inputs) && (NULL != self->outputs) && (0U != self->sets);
}

// -----------------------------------------------------------------------------
static inline bool train_param_valid(const train_param_t* self)
{
    return (0U != self->epochs) && lr_valid(self->lr);
}

// -----------------------------------------------------------------------------
static void lin_reg_optimize(lin_reg_t* self, const double input, const double reference,
                             const double lr)
{
    // Compute the predicted value yp: yp = kx + m.
    // Compute the error delta: delta = yref - yp.
    // Compute the change delta_e: delta_e = delta * LR.
    // Update the bias value m: m = m + delta_e.
    // Update the weight value k: k = k + delta_e * x.
}

// -----------------------------------------------------------------------------
bool lin_reg_train(lin_reg_t* self, const train_data_t* data, const train_param_t* param)
{
    // Check the input arguments, return false if invalid.
    if (NULL == self) { return false; }
    if (!train_data_valid(data)) { return false; }
    if (!train_param_valid(param)) { return false; }

    // Train the model for the specified number of epochs.
    for (size_t i = 0U; i < param->epochs; ++i)
    {
        // Iterate through all training sets during each epoch.
        for (size_t j = 0U; j < data->sets; ++j)
        {
            // Let the model predict based on the current set, update the trainable parameters
            // based on the result.
            const double input     = data->inputs[j];
            const double reference = data->outputs[j];
            lin_reg_optimize(self, input, reference, param->lr);
        }
    }
    return true;
}

// -----------------------------------------------------------------------------
double lin_reg_predict(const lin_reg_t* self, const double input)
{
    // Predict based on the pattern y = kx + m.
    return (NULL != self) ? self->weight * input + self->bias : 0.0;
}
