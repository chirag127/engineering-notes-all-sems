### Expectation and Variance

- Expectation and variance are two important summary statistics of a random variable, which is a variable whose value depends on the outcome of a random experiment.
- The expectation of a random variable X, denoted by E(X) or μ, is the weighted average of the possible values that X can take, each value being weighted by its probability. It represents the average or mean value of X in the long run.
- The variance of a random variable X, denoted by Var(X) or σ^2, is the expectation of the squared deviation of X from its mean. It measures the spread or variability of X around its mean. The standard deviation of X, denoted by SD(X) or σ, is the positive square root of the variance. It has the same units as X and is easier to interpret than the variance.
- The formulas for computing the expectation and variance depend on whether X is a discrete or a continuous random variable. A discrete random variable can take only a finite or countable number of values, while a continuous random variable can take any value in an interval.
- For a discrete random variable X with probability mass function p(x), the expectation and variance are given by:

E(X) = ∑x p(x) x

Var(X) = E(X^2) - E(X)^2 = ∑x p(x) x^2 - (∑x p(x) x)^2

- For a continuous random variable X with probability density function f(x), the expectation and variance are given by:

E(X) = ∫x f(x) dx

Var(X) = E(X^2) - E(X)^2 = ∫x f(x) x^2 dx - (∫x f(x) dx)^2

- Some properties of expectation and variance are:

E(aX + b) = aE(X) + b

Var(aX + b) = a^2 Var(X)

E(X + Y) = E(X) + E(Y)

Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y)

where a and b are constants, and Cov(X, Y) is the covariance of X and Y, which measures the linear relationship between them. If X and Y are independent, then Cov(X, Y) = 0 and Var(X + Y) = Var(X) + Var(Y).

- Some examples of random variables and their expectations and variances are:

X: the number of heads in 10 tosses of a fair coin

E(X) = 10 * 0.5 = 5

Var(X) = 10 * 0.5 * 0.5 = 2.5

Y: the time (in minutes) it takes to complete a task

E(Y) = 20

Var(Y) = 4

Z: the score (in points) of a student in a test

E(Z) = 75

Var(Z) = 100