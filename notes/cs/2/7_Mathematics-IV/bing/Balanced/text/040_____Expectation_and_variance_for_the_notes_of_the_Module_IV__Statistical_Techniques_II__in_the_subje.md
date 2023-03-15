### Expectation and Variance

- Expectation and variance are two important summary statistics of a random variable, which is a variable whose value depends on the outcome of a random experiment.
- The expectation of a random variable X, denoted by E(X) or μ, is the weighted average of the possible values that X can take, each value being weighted by its probability. It represents the average or mean value of X in the long run.
- The variance of a random variable X, denoted by Var(X) or σ^2, is the expectation of the squared deviation of X from its mean. It measures the spread or variability of X around its mean. The standard deviation of X, denoted by SD(X) or σ, is the positive square root of the variance. It has the same units as X and is easier to interpret than the variance.
- The formulas for computing the expectation and variance of a discrete random variable X are:

  - E(X) = ΣxP(X=x), where the summation is over all possible values of X and P(X=x) is the probability mass function of X.
  - Var(X) = E(X^2) - E(X)^2 = Σx^2P(X=x) - E(X)^2, where E(X^2) is the expectation of X squared.
  - SD(X) = √Var(X) = √[E(X^2) - E(X)^2]

- The formulas for computing the expectation and variance of a continuous random variable X are:

  - E(X) = ∫xf(x)dx, where the integral is over the domain of X and f(x) is the probability density function of X.
  - Var(X) = E(X^2) - E(X)^2 = ∫x^2f(x)dx - E(X)^2, where E(X^2) is the expectation of X squared.
  - SD(X) = √Var(X) = √[E(X^2) - E(X)^2]

- Some properties of expectation and variance are:

  - E(a) = a, where a is a constant.
  - E(aX+b) = aE(X) + b, where a and b are constants.
  - Var(a) = 0, where a is a constant.
  - Var(aX+b) = a^2Var(X), where a and b are constants.
  - SD(aX+b) = |a|SD(X), where a and b are constants.
  - If X and Y are independent random variables, then E(X+Y) = E(X) + E(Y) and Var(X+Y) = Var(X) + Var(Y).