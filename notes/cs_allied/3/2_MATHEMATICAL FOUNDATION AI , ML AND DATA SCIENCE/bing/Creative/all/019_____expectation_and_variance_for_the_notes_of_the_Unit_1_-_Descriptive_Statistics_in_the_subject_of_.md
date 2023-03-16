# Expectation and Variance

- The **expectation** of a random variable is the weighted average of its possible values, where the weights are the probabilities of each value. It is also called the **mean** or the **expected value** of the random variable. It is denoted by E(X) or µX.
- The **variance** of a random variable is the measure of how much the values of the random variable deviate from the mean. It is the average of the squared differences from the mean. It is denoted by Var(X) or σX^2.
- The **standard deviation** of a random variable is the positive square root of the variance. It is denoted by SD(X) or σX.

## Formulas

- For a discrete random variable X with probability mass function p(x), the expectation is given by:

E(X) = ∑x p(x) x

- For a continuous random variable X with probability density function f(x), the expectation is given by:

E(X) = ∫x f(x) x dx

- For any random variable X, the variance is given by:

Var(X) = E(X^2) - E(X)^2

- Alternatively, the variance can be computed by:

Var(X) = E[(X - µX)^2]

- The standard deviation is given by:

SD(X) = √Var(X)

## Properties

- The expectation and variance are **linear operators**, which means that for any random variables X and Y, and any constants a and b, the following properties hold:

E(aX + b) = aE(X) + b

Var(aX + b) = a^2 Var(X)

- The **covariance** of two random variables X and Y is a measure of how much they vary together. It is given by:

Cov(X, Y) = E[(X - µX)(Y - µY)]

- The covariance is related to the variance by the following formula:

Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y)

- If X and Y are **independent** random variables, then their covariance is zero, and their variance is additive:

Cov(X, Y) = 0

Var(X + Y) = Var(X) + Var(Y)

- The **correlation** of two random variables X and Y is a normalized measure of their linear relationship. It is given by:

Corr(X, Y) = Cov(X, Y) / (SD(X) SD(Y))

- The correlation is always between -1 and 1, and it is zero if and only if X and Y are **uncorrelated**, which means that their covariance is zero.