# Expectation and Variance

- The **expectation** of a random variable is the weighted average of its possible values, where the weights are the probabilities of each value. It is also called the **mean** or the **expected value** of the random variable. It is denoted by E(X) or µX.
- The **variance** of a random variable is the measure of how much the values of the random variable deviate from the mean. It is also called the **mean squared deviation** or the **second central moment** of the random variable. It is denoted by Var(X) or σX^2.
- The **standard deviation** of a random variable is the positive square root of the variance. It is also called the **root mean squared deviation** or the **second moment** of the random variable. It is denoted by SD(X) or σX.

## Formulas

- For a discrete random variable X with probability mass function p(x), the formulas for expectation, variance and standard deviation are:

  - E(X) = ∑x p(x) x
  - Var(X) = E(X^2) - E(X)^2 = ∑x p(x) x^2 - (∑x p(x) x)^2
  - SD(X) = √Var(X) = √(∑x p(x) x^2 - (∑x p(x) x)^2)

- For a continuous random variable X with probability density function f(x), the formulas for expectation, variance and standard deviation are:

  - E(X) = ∫x f(x) dx
  - Var(X) = E(X^2) - E(X)^2 = ∫x^2 f(x) dx - (∫x f(x) dx)^2
  - SD(X) = √Var(X) = √(∫x^2 f(x) dx - (∫x f(x) dx)^2)

## Properties

- Expectation is a **linear operator**, which means that for any random variables X and Y, and any constants a and b, E(aX + bY) = aE(X) + bE(Y).
- Variance is **not a linear operator**, but it has the following properties:

  - Var(X) ≥ 0 for any random variable X.
  - Var(aX + b) = a^2 Var(X) for any random variable X and any constants a and b.
  - Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y) for any random variables X and Y, where Cov(X, Y) is the **covariance** of X and Y, defined as Cov(X, Y) = E[(X - µX)(Y - µY)].
  - If X and Y are **independent**, then Cov(X, Y) = 0 and Var(X + Y) = Var(X) + Var(Y).

- Standard deviation has the same properties as variance, except that it is scaled by the factor √a for any constant a.