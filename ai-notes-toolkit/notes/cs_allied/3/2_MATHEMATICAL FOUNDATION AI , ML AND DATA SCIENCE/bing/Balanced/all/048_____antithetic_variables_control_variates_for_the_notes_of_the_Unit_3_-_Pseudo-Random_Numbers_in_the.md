# Antithetic Variables/Control Variates

- Antithetic variables and control variates are two variance reduction techniques used in Monte Carlo methods.
- Monte Carlo methods are a class of algorithms that use random sampling to approximate numerical integrals, expectations, or other functions of interest.
- Variance reduction techniques aim to improve the accuracy and efficiency of Monte Carlo methods by reducing the variance of the estimator without changing its expected value.

## Antithetic Variables

- The antithetic variables method is based on the idea of using the opposite or complementary values of the random variables to cancel out some of the variation in the estimator.
- For example, if X is a random variable with a uniform distribution on [a,b], then its antithetic variable is Y = a + b - X, which has the same distribution as X but is negatively correlated with X.
- The antithetic variables method works as follows:

  - Generate n/2 pairs of random variables (X_i, Y_i) such that Y_i is the antithetic variable of X_i.
  - Evaluate the function of interest g(X_i) and g(Y_i) for each pair.
  - Compute the average of g(X_i) and g(Y_i) for each pair, and then take the average of these averages as the estimator.

- The antithetic variables method reduces the variance of the estimator if the function g is monotonic and the random variables X and Y are negatively correlated.
- The antithetic variables method is simple to implement and does not require any additional information about the function g or the distribution of X.

## Control Variates

- The control variates method is based on the idea of using a known function h that is correlated with the function of interest g to adjust the estimator and reduce its variance.
- For example, if X is a random variable with a normal distribution and g(X) is the function of interest, then h(X) = X could be a possible control variate, since it is linearly correlated with g(X) and its expected value is known.
- The control variates method works as follows:

  - Generate n random variables X_i and evaluate the function of interest g(X_i) and the control variate h(X_i) for each sample.
  - Compute the sample mean and variance of g(X_i) and h(X_i), and the sample covariance of g(X_i) and h(X_i).
  - Choose a constant c that minimizes the variance of the estimator, which is given by c = - Cov(g(X), h(X)) / Var(h(X)).
  - Compute the estimator as the average of g(X_i) + c (h(X_i) - E[h(X)]) for each sample.

- The control variates method reduces the variance of the estimator if the function h is correlated with the function g and its expected value is known or can be easily computed.
- The control variates method requires some additional information about the function g and the distribution of X, and some computation to find the optimal constant c.