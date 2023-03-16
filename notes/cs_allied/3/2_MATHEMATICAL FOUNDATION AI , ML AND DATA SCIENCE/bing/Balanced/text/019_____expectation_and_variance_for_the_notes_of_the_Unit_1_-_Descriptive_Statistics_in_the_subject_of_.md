### Expectation and Variance

- The **expectation** of a random variable is the weighted average of its possible values, where the weights are the probabilities of each value. It is also called the **mean** or the **expected value** of the random variable. It is denoted by E(X) or µX.
- The **variance** of a random variable is the measure of how much the values of the random variable deviate from the mean. It is also called the **mean squared deviation** or the **second central moment** of the random variable. It is denoted by Var(X) or σX^2.
- The **standard deviation** of a random variable is the positive square root of the variance. It is also a measure of dispersion or spread of the random variable. It is denoted by SD(X) or σX.

- The formulas for expectation and variance depend on whether the random variable is discrete or continuous. For a discrete random variable X with probability mass function p(x), the formulas are:

  - E(X) = ∑xp(x) for all possible values of x
  - Var(X) = E(X^2) - E(X)^2 = ∑x^2p(x) - E(X)^2 for all possible values of x
  - SD(X) = √Var(X)

- For a continuous random variable X with probability density function f(x), the formulas are:

  - E(X) = ∫xf(x)dx over the domain of x
  - Var(X) = E(X^2) - E(X)^2 = ∫x^2f(x)dx - E(X)^2 over the domain of x
  - SD(X) = √Var(X)

- Some properties of expectation and variance are:

  - E(aX + b) = aE(X) + b for any constants a and b
  - Var(aX + b) = a^2Var(X) for any constants a and b
  - SD(aX + b) = |a|SD(X) for any constant a
  - Cov(X, Y) = E(XY) - E(X)E(Y) is the **covariance** of two random variables X and Y, which measures the linear relationship between them
  - Corr(X, Y) = Cov(X, Y) / (SD(X)SD(Y)) is the **correlation** of two random variables X and Y, which measures the strength and direction of the linear relationship between them
  - Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y) for any two random variables X and Y
  - Var(X - Y) = Var(X) + Var(Y) - 2Cov(X, Y) for any two random variables X and Y
  - If X and Y are **independent**, then Cov(X, Y) = 0 and Corr(X, Y) = 0
  - If X and Y are independent, then E(XY) = E(X)E(Y) and Var(X + Y) = Var(X) + Var(Y) and Var(X - Y) = Var(X) + Var(Y)