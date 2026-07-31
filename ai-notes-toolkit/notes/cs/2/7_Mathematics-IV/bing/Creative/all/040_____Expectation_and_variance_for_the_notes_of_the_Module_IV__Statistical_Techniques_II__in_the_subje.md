# Expectation and Variance

- Expectation and variance are two important summary statistics of a random variable, which describe its average value and spread around the average, respectively .
- The expectation of a random variable X is denoted by E(X) or μ, and it is the weighted average of the possible values that X can take, each value being weighted by its probability.
- The variance of a random variable X is denoted by Var(X) or σ^2^, and it is the expectation of the squared deviation of X from its mean. It measures how far the values of X are spread out from their average value.
- The standard deviation of a random variable X is denoted by SD(X) or σ, and it is the positive square root of the variance. It has the same units as X, unlike the variance, which has the units of X squared.
- The expectation and variance of a random variable can be computed using different formulas, depending on whether the random variable is discrete or continuous, and whether it has a known probability distribution or not.
- For a discrete random variable X with a finite number of possible values x_1, x_2, ..., x_n and corresponding probabilities p_1, p_2, ..., p_n, the expectation and variance are given by:

E(X) = ∑_i=1^n p_i x_i

Var(X) = E(X^2^) - E(X)^2^ = ∑_i=1^n p_i x_i^2^ - (∑_i=1^n p_i x_i)^2^

- For a continuous random variable X with a probability density function f(x), the expectation and variance are given by:

E(X) = ∫_(-∞)^∞ x f(x) dx

Var(X) = E(X^2^) - E(X)^2^ = ∫_(-∞)^∞ x^2^ f(x) dx - (∫_(-∞)^∞ x f(x) dx)^2^

- For a random variable X with a known probability distribution, such as the binomial, Poisson, normal, exponential, etc., the expectation and variance can be computed using the formulas or properties of that distribution. For example, if X follows a binomial distribution with parameters n and p, then:

E(X) = np

Var(X) = np(1-p)

- The expectation and variance have some useful properties that can be used to simplify calculations or derive new results. For example, if X and Y are two random variables, and a and b are two constants, then:

E(aX + bY) = aE(X) + bE(Y)

Var(aX + bY) = a^2^Var(X) + b^2^Var(Y) + 2abCov(X,Y)

where Cov(X,Y) is the covariance of X and Y, which measures the linear relationship between them.

- The expectation and variance are also related to other concepts in statistics, such as moments, moment generating functions, cumulants, skewness, kurtosis, etc. These concepts can be used to describe the shape, symmetry, and tail behavior of a probability distribution.