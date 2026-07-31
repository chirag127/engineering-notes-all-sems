### Expectation and Variance

- Expectation and variance are two important summary statistics of a random variable.
- A random variable is a variable whose value is determined by the outcome of a random experiment.
- The expectation of a random variable is the weighted average of the possible values that it can take, where the weights are the probabilities of those values.
- The expectation of a random variable X is usually written as E(X) or μ.
- The variance of a random variable is the measure of how far the values are spread out from the expectation.
- The variance of a random variable X is usually written as Var(X) or σ^2.
- The variance of a random variable X is the expectation of the squared deviation of X from its mean, that is, Var(X) = E[(X - μ)^2].
- The standard deviation of a random variable X is the positive square root of the variance, that is, SD(X) = σ = √Var(X).
- The standard deviation is a measure of how much the values deviate from the mean on average.
- The expectation and variance of a random variable depend on its probability distribution, which describes the possible values and their probabilities.
- There are different formulas for calculating the expectation and variance of a random variable depending on whether it is discrete or continuous.
- A discrete random variable is one that can take only a finite or countable number of values, such as the number of heads in a coin toss or the number of students in a class.
- A continuous random variable is one that can take any value in a given interval, such as the height of a person or the time of arrival of a bus.
- The expectation and variance of a discrete random variable X are given by:

  - E(X) = ∑xP(X = x), where the sum is over all possible values of X and P(X = x) is the probability of X taking the value x.
  - Var(X) = E(X^2) - [E(X)]^2 = ∑x^2P(X = x) - [∑xP(X = x)]^2, where the sums are over all possible values of X.

- The expectation and variance of a continuous random variable X are given by:

  - E(X) = ∫xf(x)dx, where the integral is over the domain of X and f(x) is the probability density function of X, which gives the relative likelihood of X taking the value x.
  - Var(X) = E(X^2) - [E(X)]^2 = ∫x^2f(x)dx - [∫xf(x)dx]^2, where the integrals are over the domain of X.

- Some properties of expectation and variance are:

  - E(a) = a, where a is a constant.
  - E(aX + b) = aE(X) + b, where a and b are constants.
  - Var(a) = 0, where a is a constant.
  - Var(aX + b) = a^2Var(X), where a and b are constants.
  - E(X + Y) = E(X) + E(Y), where X and Y are any two random variables.
  - Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y), where X and Y are any two random variables and Cov(X, Y) is the covariance of X and Y, which measures the linear relationship between them.
  - If X and Y are independent, then Cov(X, Y) = 0 and Var(X + Y) = Var(X) + Var(Y).

- Expectation and variance are useful for describing the behavior and characteristics of a random variable, such as its center, spread, and shape.
- Expectation and variance are also useful for calculating other statistics, such as the mean, median, mode, skewness, kurtosis, and moments of a random variable.