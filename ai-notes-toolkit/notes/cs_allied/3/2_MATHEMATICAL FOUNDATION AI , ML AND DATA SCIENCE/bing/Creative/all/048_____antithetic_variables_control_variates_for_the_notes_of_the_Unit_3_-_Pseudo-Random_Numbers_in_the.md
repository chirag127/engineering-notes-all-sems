# Antithetic Variables/Control Variates

- Antithetic variables and control variates are two variance reduction techniques used in Monte Carlo methods.
- Monte Carlo methods are numerical methods that use random sampling to approximate complex integrals or expectations.
- Variance reduction techniques aim to improve the accuracy and efficiency of Monte Carlo methods by reducing the variance of the estimator.

## Antithetic Variables

- The antithetic variables method is based on the idea of using the opposite or complementary values of the random variables to cancel out some of the randomness.
- For example, if X is a random variable with a uniform distribution on [0,1], then 1-X is its antithetic variable, and they have the same mean but a negative covariance.
- The antithetic variables method works best when the function of interest is monotonic, so that the antithetic variables have opposite effects on the function value.
- The antithetic variables method can be implemented as follows:

  - Generate n/2 pairs of random variables (X1, 1-X1), (X2, 1-X2), ..., (Xn/2, 1-Xn/2) from the desired distribution.
  - Evaluate the function of interest at each pair of random variables, and compute the average of the function values within each pair.
  - Use the average of the averages as the estimator of the expectation or integral.

- The antithetic variables method can reduce the variance of the estimator by a factor of (1-ρ), where ρ is the correlation coefficient between the random variable and its antithetic variable.

## Control Variates

- The control variates method is based on the idea of using a known function that is correlated with the function of interest to adjust the estimator.
- For example, if X is a random variable with a known mean μ, and Y is a function of X that we want to estimate, then X can be used as a control variate for Y, and the estimator can be corrected by subtracting a multiple of (X-μ) from Y.
- The control variates method works best when the function of interest and the control variate have a high correlation, so that the adjustment can reduce the variance significantly.
- The control variates method can be implemented as follows:

  - Generate n random variables X1, X2, ..., Xn from the desired distribution.
  - Evaluate the function of interest and the control variate at each random variable, and compute the sample means and variances of Y and X, and the sample covariance of Y and X.
  - Use the formula b = -cov(Y,X)/var(X) to compute the optimal coefficient for the adjustment.
  - Use the formula Ybar + b(Xbar - μ) as the estimator of the expectation or integral, where Ybar and Xbar are the sample means of Y and X, and μ is the known mean of X.

- The control variates method can reduce the variance of the estimator by a factor of (1-ρ^2), where ρ is the correlation coefficient between the function of interest and the control variate.