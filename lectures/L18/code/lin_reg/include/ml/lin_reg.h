/**
 * @file Linear regression model API.
 */
#ifndef LIN_REG_H_
#define LIN_REG_H_

#include <stdbool.h>
#include <stddef.h>

// clang-format off
/**
 * @brief Create a new linear regression model instance.
 * 
 * @return Linear regression model instance with initialized parameters.
 */
#define LIN_REG_NEW() {0.0, 0.0}
// clang-format off

/**
 * @brief Linear regression model structure.
 *
 *        The model predicts in accordance with the formula y = kx + m, where
 *        y is the output, k is the weight, x is the input, and m is the bias.
 */
typedef struct
{
    double bias;   /** Bias value (m-value). */
    double weight; /** Weight value (k-value). */
} lin_reg_t;

/**
 * @brief Training data structure.
 */
typedef struct
{
    const double* inputs;  /** Input values. */
    const double* outputs; /** Output values. */
    const size_t sets;     /** Number of training sets. */
} train_data_t;

/**
 * @brief Training parameter structure.
 */
typedef struct
{
    const size_t epochs; /** Number of epochs to train the model. Must be greater than 0. */
    const double lr;     /** Learning rate to use. Must be in range (0.0, 1.0). */
} train_param_t;

/**
 * @brief Train the linear regression model.
 *
 * @param[in,out] self Linear regression model instance.
 * @param[in] data Training data. Must contain at least one complete set.
 * @param[in] param Training parameters. All must be valid.
 *
 * @return True after training, or false on invalid input argument(s).
 */
bool lin_reg_train(lin_reg_t* self, const train_data_t* data, const train_param_t* param);

/**
 * @brief Perform prediction based on the given input.
 *
 * @param[in] self Linear regression model instance.
 * @param[in] input Input value.
 *
 * @return Predicted output value.
 */
double lin_reg_predict(const lin_reg_t* self, double input);

#endif /** LIN_REG_H_ */
