### Antithetic variables/control variates

- Antithetic variables and control variates are two variance reduction techniques used in Monte Carlo methods.
- Monte Carlo methods are a class of algorithms that use random numbers to approximate a function or a distribution.
- The error in the Monte Carlo estimate has a one-over square root convergence, which means that a large number of samples is needed to achieve a high accuracy.
- Variance reduction techniques aim to reduce the number of samples needed by exploiting some properties of the function or the distribution.

#### Antithetic variables

- The antithetic variables technique is based on the idea of using symmetric or complementary samples to cancel out some of the variability in the estimate.
- For example, if the function is monotonic, then using the samples x and 1-x will reduce the variance of the estimate of the mean, since they will have opposite deviations from the mean.
- The antithetic variables technique consists of generating N/2 pairs of antithetic samples, and taking the average of the function values over all N samples as the estimate.
- The advantage of this technique is that it reduces the number of random samples needed by half, and it reduces the variance of the estimate if the function is negatively correlated with its antithetic counterpart.
- The disadvantage of this technique is that it requires some knowledge of the symmetry or the inverse of the function or the distribution, and it may increase the variance if the function is positively correlated with its antithetic counterpart.

#### Control variates

- The control variates technique is based on the idea of using a known function or distribution that is correlated with the function or distribution of interest, and adjusting the estimate by the difference between the expected and the observed values of the control variate.
- For example, if the function is linearly related to another function with a known mean, then using the difference between the observed and the expected values of the other function as a control variate will reduce the variance of the estimate of the mean, since it will account for some of the variability in the function of interest.
- The control variates technique consists of generating N samples of the function of interest and the control variate, and taking the weighted average of the function values and the control variate values as the estimate, where the weight is chosen to minimize the variance of the estimate.
- The advantage of this technique is that it reduces the variance of the estimate if the function and the control variate are strongly correlated, and it does not require any symmetry or inverse properties of the function or the distribution.
- The disadvantage of this technique is that it requires some knowledge of the mean and the variance of the control variate, and it may increase the variance if the function and the control variate are weakly correlated or have opposite signs.