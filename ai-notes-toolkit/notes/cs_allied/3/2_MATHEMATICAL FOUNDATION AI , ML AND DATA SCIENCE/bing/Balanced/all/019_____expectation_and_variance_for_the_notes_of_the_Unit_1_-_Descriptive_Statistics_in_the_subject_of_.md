# Expectation and Variance

- The **expectation** of a random variable is the weighted average of its possible values, where the weights are the probabilities of each value. It is also called the **mean** or the **expected value** of the random variable. It is denoted by E(X) or µX.
- The **variance** of a random variable is the measure of how much the values of the random variable deviate from the mean. It is also called the **mean squared deviation** or the **second central moment** of the random variable. It is denoted by Var(X) or σX^2.
- The **standard deviation** of a random variable is the positive square root of the variance. It is also called the **root mean squared deviation** or the **second moment** of the random variable. It is denoted by SD(X) or σX.

## Formulas

- For a discrete random variable X with probability mass function p(x), the formulas for expectation and variance are:

  - E(X) = ∑x p(x) x
  - Var(X) = E(X^2) - E(X)^2 = ∑x p(x) x^2 - (∑x p(x) x)^2

- For a continuous random variable X with probability density function f(x), the formulas for expectation and variance are:

  - E(X) = ∫x f(x) dx
  - Var(X) = E(X^2) - E(X)^2 = ∫x f(x) x^2 dx - (∫x f(x) dx)^2

- For any random variable X and any constants a and b, the following properties hold:

  - E(aX + b) = aE(X) + b
  - Var(aX + b) = a^2 Var(X)
  - SD(aX + b) = |a| SD(X)