### Antithetic Variables/Control Variates

- Antithetic variables and control variates are two variance reduction techniques used in Monte Carlo methods.
- Monte Carlo methods are a class of algorithms that use random sampling to approximate numerical integrals or expectations of functions.
- Variance reduction techniques aim to improve the accuracy and efficiency of Monte Carlo methods by reducing the variance of the estimator.

#### Antithetic Variables

- The antithetic variables method is based on the idea of using the opposite or complementary values of the random variables to cancel out some of the variation in the function.
- For example, if X is a uniformly distributed random variable on [a,b], then its antithetic variable is Y = a + b - X, which is also uniformly distributed on [a,b].
- The antithetic variables method works best when the function is monotonic, i.e., either increasing or decreasing, in the random variables.
- The antithetic variables method reduces the variance of the estimator by exploiting the negative covariance between the function values at X and Y.
- The antithetic variables method can be implemented as follows:

  - Generate n/2 pairs of independent random variables (X_i, Y_i), where Y_i is the antithetic variable of X_i.
  - Evaluate the function at each pair of random variables, i.e., compute f(X_i) and f(Y_i) for i = 1, ..., n/2.
  - Compute the average of the function values, i.e., (f(X_i) + f(Y_i))/2 for i = 1, ..., n/2.
  - Use the average of the averages as the estimator, i.e., (1/n) * sum_{i=1}^{n/2} (f(X_i) + f(Y_i))/2.

#### Control Variates

- The control variates method is based on the idea of using a known function that is correlated with the unknown function to reduce the variance of the estimator.
- For example, if X is a normally distributed random variable and f(X) is the unknown function, then a possible control variate is g(X) = X, which has a known expectation of zero.
- The control variates method works best when the function and the control variate have a high correlation, either positive or negative.
- The control variates method reduces the variance of the estimator by adjusting the function values by a weighted difference of the control variate values and their known expectation.
- The control variates method can be implemented as follows:

  - Generate n independent random variables X_i and evaluate the function and the control variate at each random variable, i.e., compute f(X_i) and g(X_i) for i = 1, ..., n.
  - Compute the sample mean and variance of the function values and the control variate values, i.e., f_bar, g_bar, s_f^2, and s_g^2.
  - Compute the sample covariance between the function values and the control variate values, i.e., s_fg.
  - Compute the optimal weight for the control variate, i.e., b = s_fg / s_g^2.
  - Compute the adjusted function values, i.e., f_hat(X_i) = f(X_i) - b * (g(X_i) - E[g(X)]), where E[g(X)] is the known expectation of the control variate.
  - Use the average of the adjusted function values as the estimator, i.e., (1/n) * sum_{i=1}^n f_hat(X_i).