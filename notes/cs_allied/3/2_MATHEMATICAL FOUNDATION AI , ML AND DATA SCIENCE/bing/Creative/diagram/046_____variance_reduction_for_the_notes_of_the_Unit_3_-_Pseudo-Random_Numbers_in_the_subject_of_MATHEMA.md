### Variance Reduction

Variance reduction is a set of techniques that aim to improve the accuracy and efficiency of Monte Carlo simulations by reducing the variance of the estimator without changing its expected value. Variance reduction can help to achieve a desired level of precision with fewer simulations, or to increase the precision with the same number of simulations.

Some of the common variance reduction techniques are:

- **Common random numbers (CRN)**: This technique applies when comparing two or more alternative configurations of a system, such as different policies or strategies. CRN uses the same random numbers to generate the inputs for each configuration, so that the outputs are correlated and the difference between them has less variance. CRN can also be used to estimate the sensitivity of the output to changes in the input parameters.

- **Control variates (CV)**: This technique uses a known function of the random inputs that is correlated with the output of interest and has a known expected value. CV subtracts a multiple of this function from the output and adds back the multiple of its expected value. This reduces the variance of the estimator if the function and the output are negatively correlated, or increases it if they are positively correlated. The optimal multiple is the negative of the covariance between the function and the output divided by the variance of the function.

- **Partial integration (PI)**: This technique replaces some of the random variables or some of the integration domains by their expected values, which reduces the dimensionality and complexity of the simulation. PI can also be seen as a special case of CV, where the control variate is the output itself integrated over some variables or domains.

- **Systematic sampling (SS)**: This technique uses a deterministic or quasi-random sequence of numbers instead of a purely random one to generate the inputs for the simulation. SS can reduce the variance of the estimator by increasing the uniformity and coverage of the sampling points, and avoiding clustering or gaps. SS includes methods such as antithetic variates, stratified sampling, and quasi-Monte Carlo integration.

- **Importance sampling (IS)**: This technique changes the probability distribution of the random inputs to make the output more likely to occur or to have a larger magnitude. IS assigns a weight to each simulation that is proportional to the ratio of the original distribution and the new distribution. IS can reduce the variance of the estimator by increasing the frequency or the impact of the output, especially for rare events or tail probabilities. IS requires choosing a suitable distribution that is close to the output and easy to sample from .