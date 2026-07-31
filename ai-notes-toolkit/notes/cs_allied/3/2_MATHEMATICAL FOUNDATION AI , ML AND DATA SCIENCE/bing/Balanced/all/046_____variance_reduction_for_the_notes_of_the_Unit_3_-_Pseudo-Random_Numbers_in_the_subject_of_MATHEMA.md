# Variance Reduction

Variance reduction is a set of techniques that aim to improve the accuracy and efficiency of Monte Carlo simulations by reducing the variance of the estimator without changing its expected value. Variance reduction can help to achieve a desired level of precision with fewer simulations, saving computational time and resources.

Some of the common variance reduction techniques are:

- **Common random numbers (CRN)**: This technique applies when comparing two or more alternative configurations of a system, such as different policies or strategies. CRN uses the same random numbers to generate the inputs for each configuration, so that the outputs are more correlated and the difference between them has less variance. CRN can also be used to estimate the sensitivity of the output to changes in the input parameters.

- **Control variates (CV)**: This technique uses a known function of the random inputs that is correlated with the output of interest and has a known expected value. CV subtracts a multiple of this function from the output and adds back the multiple of its expected value, so that the modified output has the same expected value as the original output but less variance. The optimal multiple is chosen to minimize the variance of the modified output.

- **Partial integration (PI)**: This technique reduces the variance by replacing some of the random variables or some parts of the integration domain by their expected values. PI can also be seen as a special case of CV, where the control variate is the conditional expectation of the output given some of the random variables.

- **Systematic sampling (SS)**: This technique uses a deterministic or quasi-random sequence of numbers instead of a purely random sequence to generate the inputs for the simulation. SS can reduce the variance by ensuring a more uniform coverage of the integration domain and avoiding clustering or gaps in the sample points. SS includes methods such as antithetic variates, stratified sampling, and quasi-Monte Carlo integration.

- **Importance sampling (IS)**: This technique changes the probability distribution of the random inputs to make the output more likely to occur or to have larger values. IS assigns different weights to the output values according to the ratio of the original and the modified probability distributions, so that the weighted average of the output has the same expected value as the unweighted average. IS can reduce the variance by focusing on the regions of the integration domain that contribute more to the output value. IS is especially useful for estimating rare events or tail probabilities .