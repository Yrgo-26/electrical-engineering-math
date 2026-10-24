/**
 * @file Machine learning utility functions.
 */
#ifndef ML_UTILS_H_
#define ML_UTILS_H_

/**
 * @brief Get the size of the given array.
 *
 * @param[in] array Array in question.
 *
 * @return Size of the array measured in the number of elements it can hold.
 */
#define ARRAY_SIZE(array) (sizeof(array) / sizeof((array)[0U]))

/**
 * @brief Get the smallest of two numbers.
 *
 * @param[in] x First number.
 * @param[in] y Second number.
 *
 * @return The smallest of the two numbers.
 */
#define MIN(x, y) ((x) <= (y) ? (x) : (y))

/**
 * @brief Compute the number of complete training sets.
 *
 * @param[in] inputs Training inputs.
 * @param[in] outputs Training outputs.
 *
 * @return Number of complete training sets.
 */
#define COMPUTE_SETS(inputs, outputs) (MIN(ARRAY_SIZE(inputs), ARRAY_SIZE(outputs)))

#endif /** ML_UTILS_H_ */
