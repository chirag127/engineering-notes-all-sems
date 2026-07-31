### Expectation and Variance

- The **expectation** of a random variable is the weighted average of its possible values, where the weights are the probabilities of each value. It is also called the **mean** or the **expected value** of the random variable. It is denoted by E(X) or µX.
- The **variance** of a random variable is the measure of how much the values of the random variable deviate from the mean. It is the average of the squared differences from the mean. It is denoted by Var(X) or σX^2.
- The **standard deviation** of a random variable is the positive square root of the variance. It is denoted by SD(X) or σX.
- The **covariance** of two random variables is the measure of how much they vary together. It is the expected value of the product of the deviations from the mean. It is denoted by Cov(X, Y) or σXY.

#### Formulas

- For a discrete random variable X with probability mass function p(x), the expectation is given by:

  E(X) = ∑x p(x) x

- For a continuous random variable X with probability density function f(x), the expectation is given by:

  E(X) = ∫x f(x) x dx

- For any random variable X and constants a and b, the expectation has the following properties:

  E(aX + b) = aE(X) + b

  E(X + Y) = E(X) + E(Y)

- For a discrete random variable X with probability mass function p(x) and mean µX, the variance is given by:

  Var(X) = ∑x p(x) (x - µX)^2

- For a continuous random variable X with probability density function f(x) and mean µX, the variance is given by:

  Var(X) = ∫x f(x) (x - µX)^2 dx

- For any random variable X and constants a and b, the variance has the following properties:

  Var(aX + b) = a^2 Var(X)

  Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y)

- The standard deviation is given by:

  SD(X) = √Var(X)

- For two random variables X and Y with means µX and µY, the covariance is given by:

  Cov(X, Y) = E[(X - µX)(Y - µY)]

- For discrete random variables X and Y with probability mass function p(x, y), the covariance is given by:

  Cov(X, Y) = ∑x ∑y p(x, y) (x - µX)(y - µY)

- For continuous random variables X and Y with probability density function f(x, y), the covariance is given by:

  Cov(X, Y) = ∫x ∫y f(x, y) (x - µX)(y - µY) dx dy

- For any random variables X and Y and constants a and b, the covariance has the following properties:

  Cov(aX + b, Y) = aCov(X, Y)

  Cov(X + Y, Z) = Cov(X, Z) + Cov(Y, Z)

  Cov(X, X) = Var(X)

  Cov(X, Y) = Cov(Y, X)