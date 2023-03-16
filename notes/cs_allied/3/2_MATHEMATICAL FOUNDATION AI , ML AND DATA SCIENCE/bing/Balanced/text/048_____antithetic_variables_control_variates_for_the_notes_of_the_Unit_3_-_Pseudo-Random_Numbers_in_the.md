### Antithetic Variables/Control Variates

- Antithetic variables and control variates are two variance reduction techniques used in Monte Carlo methods.
- Monte Carlo methods are a class of algorithms that use random sampling to approximate numerical integrals or expectations of functions.
- Variance reduction techniques aim to improve the accuracy and efficiency of Monte Carlo methods by reducing the variance of the estimator.

#### Antithetic Variables

- The antithetic variables method is based on the idea of using the opposite or complementary values of the random variables to cancel out some of the randomness.
- For example, if X is a random variable with a uniform distribution on [a,b], then its antithetic variable is Y = a + b - X, which has the same distribution as X but is negatively correlated with X.
- The antithetic variables method works as follows:

  - Generate n pairs of random variables (X1, Y1), ..., (Xn, Yn) such that Xi and Yi are antithetic variables for i = 1, ..., n.
  - Evaluate the function of interest g at each pair of random variables and take the average of the two values: Zi = (g(Xi) + g(Yi))/2 for i = 1, ..., n.
  - Use the sample mean of Zi as the estimator of the expectation of g: Z = (1/n) * sum(Zi) for i = 1, ..., n.

- The antithetic variables method reduces the variance of the estimator Z if the function g is monotonic and the random variables X and Y are negatively correlated.
- The antithetic variables method is simple to implement and does not require any additional information about the function g or the distribution of X.

#### Control Variates

- The control variates method is based on the idea of using a known function h that is correlated with the function of interest g to adjust the estimator of the expectation of g.
- For example, if X is a random variable with a normal distribution and g(X) is the payoff of a European call option, then h(X) could be the payoff of a European put option with the same strike price and maturity, which has a known analytical formula.
- The control variates method works as follows:

  - Generate n random variables X1, ..., Xn from the distribution of X.
  - Evaluate the functions g and h at each random variable: gi = g(Xi) and hi = h(Xi) for i = 1, ..., n.
  - Use the sample mean of gi as the naive estimator of the expectation of g: G = (1/n) * sum(gi) for i = 1, ..., n.
  - Use the sample mean of hi as the estimator of the expectation of h: H = (1/n) * sum(hi) for i = 1, ..., n.
  - Choose a constant c that minimizes the variance of the estimator Z = G + c * (H - E[h(X)]), where E[h(X)] is the known expectation of h.
  - Use Z as the estimator of the expectation of g.

- The control variates method reduces the variance of the estimator Z if the function h is correlated with the function g and the constant c is chosen appropriately.
- The control variates method requires some additional information about the function h and its expectation, which may not be easy to obtain or compute.