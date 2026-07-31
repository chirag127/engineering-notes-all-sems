Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes on antithetic variables and control variates for pseudo-random numbers.

### Antithetic variables

- Antithetic variables are a variance reduction technique used in Monte Carlo methods.
- The idea is to use the opposite or complementary values of the random numbers to generate a second sample that is negatively correlated with the first one .
- For example, if the random numbers are uniformly distributed in [0,1], the antithetic variables are 1-u, where u is the original random number.
- The average of the two samples is then used as an estimator of the expected value of the function of interest.
- The advantage of this method is that it reduces the variance of the estimator by exploiting the symmetry of the function.
- The disadvantage is that it requires the function to be monotonic or have a single mode, otherwise the correlation may not be negative.

### Control variates

- Control variates are another variance reduction technique used in Monte Carlo methods.
- The idea is to use a known function that is correlated with the function of interest to adjust the estimator.
- For example, if the function of interest is g(x) and the known function is h(x), the estimator is g(x) - b(h(x) - E[h(x)]), where b is a constant that minimizes the variance.
- The advantage of this method is that it can reduce the variance significantly if the correlation is high and the constant b is chosen optimally.
- The disadvantage is that it requires the knowledge of the expected value of the control variate, which may not be easy to obtain.