# Expectation and Variance

- Expectation and variance are two important summary statistics of a random variable, which describe its average value and spread around the average, respectively .
- The expectation of a random variable X, denoted by E(X) or μ, is the weighted average of the possible values that X can take, each value being weighted by its probability.
- The variance of a random variable X, denoted by Var(X) or σ^2^, is the expectation of the squared deviation of X from its mean, or equivalently, the average of the squared differences between the values of X and its mean .
- The standard deviation of a random variable X, denoted by SD(X) or σ, is the positive square root of the variance, and it measures the typical distance of the values of X from the mean.
- The expectation and variance of a random variable can be calculated using different formulas depending on whether the random variable is discrete or continuous, and whether it has a known probability distribution or not .
- Some properties of expectation and variance are:
  - E(aX + b) = aE(X) + b, where a and b are constants
  - Var(aX + b) = a^2^Var(X), where a and b are constants
  - E(X + Y) = E(X) + E(Y), where X and Y are random variables
  - Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y), where X and Y are random variables and Cov(X, Y) is the covariance between them
  - If X and Y are independent, then E(XY) = E(X)E(Y) and Cov(X, Y) = 0, and the above formulas simplify to:
    - E(X + Y) = E(X) + E(Y)
    - Var(X + Y) = Var(X) + Var(Y)