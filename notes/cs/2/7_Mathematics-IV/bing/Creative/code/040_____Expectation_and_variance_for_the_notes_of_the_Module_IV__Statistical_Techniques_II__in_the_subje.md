### Expectation and variance

- Expectation and variance are two important summary statistics of a random variable, which is a variable whose value depends on the outcome of a random experiment.
- The expectation of a random variable X, denoted by E(X) or μ, is the weighted average of the possible values that X can take, each value being weighted by its probability. It represents the average or mean value of X in the long run.
- The variance of a random variable X, denoted by Var(X) or σ^2, is the expectation of the squared deviation of X from its mean. It measures the spread or variability of X around its mean. The standard deviation of X, denoted by SD(X) or σ, is the positive square root of the variance. It has the same units as X and is easier to interpret than the variance.
- The formulas for computing the expectation and variance of a random variable depend on whether the random variable is discrete or continuous. A discrete random variable can take only a finite or countable number of values, while a continuous random variable can take any value in an interval.
- For a discrete random variable X with probability mass function p(x), the expectation and variance are given by:

E(X) = Σx p(x)

Var(X) = E(X^2) - E(X)^2 = Σx^2 p(x) - (Σx p(x))^2

- For a continuous random variable X with probability density function f(x), the expectation and variance are given by:

E(X) = ∫x f(x) dx

Var(X) = E(X^2) - E(X)^2 = ∫x^2 f(x) dx - (∫x f(x) dx)^2

- Some properties of expectation and variance are:

E(aX + b) = aE(X) + b

Var(aX + b) = a^2 Var(X)

E(X + Y) = E(X) + E(Y)

Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y)

where a and b are constants and Cov(X, Y) is the covariance of X and Y, which measures the linear relationship between them.

- Some examples of random variables and their expectations and variances are:

X: the number of heads in 10 tosses of a fair coin

E(X) = 10 * 0.5 = 5

Var(X) = 10 * 0.5 * 0.5 = 2.5

X: the number of dots on a single roll of a fair die

E(X) = (1 + 2 + 3 + 4 + 5 + 6) / 6 = 3.5

Var(X) = (1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2) / 6 - 3.5^2 = 2.9167

X: the time (in minutes) until the next bus arrives at a bus stop, assuming it follows an exponential distribution with mean 10

E(X) = 10

Var(X) = 10^2 = 100