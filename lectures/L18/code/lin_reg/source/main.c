#include <stdio.h>

#include "ml/lin_reg.h"
#include "ml/utils.h"

#define EPOCHS 50U // Number of epochs to train the model.
#define LR 0.25    // Learning rate to use.

/**
 * @brief Test the model after training.
 *
 * @param[in] model Model to test.
 * @param[in] inputs Inputs to predict with.
 * @param[in] input_len Number of input values.
 */
static void test_model(const lin_reg_t* model, const double* inputs, const size_t input_len)
{
    printf("--------------------------------------------------------------------------------\n");

    for (size_t i = 0U; i < input_len; ++i)
    {
        const double input  = inputs[i];
        const double output = lin_reg_predict(model, input);
        printf("Input: %g, output: %g\n", input, output);
    }
    printf("--------------------------------------------------------------------------------\n\n");
}

/**
 * @brief Application entry point.
 *
 * @return 0 on success, -1 on failure.
 */
int main(void)
{
    // Define training data.
    const double inputs[]   = {0.0, 1.0, 2.0, 3.0, 4.0};
    const double outputs[]  = {2.0, 4.0, 6.0, 8.0, 10.0};
    const size_t sets       = COMPUTE_SETS(inputs, outputs);
    const train_data_t data = {inputs, outputs, sets};

    // Define training parameters.
    const train_param_t param = {EPOCHS, LR};

    // Create linear regression model.
    lin_reg_t model = LIN_REG_NEW();

    // Train the model, return -1 on failure.
    if (!lin_reg_train(&model, &data, &param)) { return -1; }

    // Test the model's performance, return 0 to indicate success.
    test_model(&model, inputs, ARRAY_SIZE(inputs));
    return 0;
}