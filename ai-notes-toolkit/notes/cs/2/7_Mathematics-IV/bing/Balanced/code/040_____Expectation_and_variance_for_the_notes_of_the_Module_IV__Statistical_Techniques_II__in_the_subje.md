### Expectation and variance

- Expectation and variance are two important summary statistics of a random variable, which describe its average value and spread around the average, respectively.
- The expectation of a random variable X is denoted by E(X) or μ, and it is the weighted average of the possible values that X can take, where the weights are the probabilities of those values.
- The variance of a random variable X is denoted by Var(X) or σ^2, and it is the expectation of the squared deviation of X from its mean, or equivalently, the average of the squared differences between the values of X and its mean.
- The standard deviation of a random variable X is denoted by SD(X) or σ, and it is the positive square root of the variance, or equivalently, the average distance between the values of X and its mean.
- The expectation and variance of a random variable can be computed using different formulas depending on whether the random variable is discrete or continuous, and whether it has a known probability distribution or not.
- Some properties of expectation and variance are:
  - E(aX + b) = aE(X) + b, where a and b are constants.
  - Var(aX + b) = a^2 Var(X), where a and b are constants.
  - E(X + Y) = E(X) + E(Y), where X and Y are any two random variables.
  - Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y), where X and Y are any two random variables, and Cov(X, Y) is the covariance between them, which measures the linear relationship between them.
  - If X and Y are independent, then E(XY) = E(X)E(Y), and Cov(X, Y) = 0, and Var(X + Y) = Var(X) + Var(Y).