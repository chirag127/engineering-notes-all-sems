### Expectation and Variance

- The **expectation** of a random variable is the weighted average of its possible values, where the weights are the probabilities of each value. It is also called the **mean** or the **expected value** of the random variable. It is denoted by E(X) or µX.
- The **variance** of a random variable is the measure of how much the values of the random variable deviate from the mean. It is the average of the squared differences from the mean. It is denoted by Var(X) or σX^2.
- The **standard deviation** of a random variable is the positive square root of the variance. It is denoted by SD(X) or σX.

#### Formulas

- For a discrete random variable X with probability mass function p(x), the expectation is given by:

E(X) = ∑x p(x) x

- For a continuous random variable X with probability density function f(x), the expectation is given by:

E(X) = ∫x f(x) x dx

- For any random variable X, the variance is given by:

Var(X) = E[(X - E(X))^2] = E(X^2) - E(X)^2

- For any random variable X, the standard deviation is given by:

SD(X) = √Var(X)

#### Properties

- For any random variable X and any constants a and b, the following properties hold:

E(aX + b) = aE(X) + b

Var(aX + b) = a^2 Var(X)

SD(aX + b) = |a| SD(X)

- For any two random variables X and Y and any constants a and b, the following properties hold:

E(aX + bY) = aE(X) + bE(Y)

Var(aX + bY) = a^2 Var(X) + b^2 Var(Y) + 2ab Cov(X, Y)

SD(aX + bY) = √Var(aX + bY)

- The **covariance** of two random variables X and Y is a measure of how much they vary together. It is denoted by Cov(X, Y) and is given by:

Cov(X, Y) = E[(X - E(X))(Y - E(Y))] = E(XY) - E(X)E(Y)

- The **correlation** of two random variables X and Y is a measure of how linearly related they are. It is denoted by Corr(X, Y) or ρXY and is given by:

Corr(X, Y) = Cov(X, Y) / (SD(X) SD(Y))

- The correlation is always between -1 and 1, where -1 means perfect negative linear relationship, 0 means no linear relationship, and 1 means perfect positive linear relationship.