### Expectation and variance

- Expectation and variance are two important concepts in probability and statistics that measure the average and the spread of a random variable respectively.
- A random variable is a variable whose value is determined by the outcome of a random experiment, such as tossing a coin, rolling a die, or drawing a card from a deck.
- The expectation of a random variable, denoted by E(X), is the weighted average of all possible values that X can take, where the weights are the probabilities of each value. For example, if X is the number of heads obtained when tossing a fair coin twice, then X can take the values 0, 1, or 2, with probabilities 1/4, 1/2, and 1/4 respectively. The expectation of X is then E(X) = 0 * (1/4) + 1 * (1/2) + 2 * (1/4) = 1.
- The variance of a random variable, denoted by Var(X), is the measure of how much the values of X deviate from the expectation. It is calculated by taking the average of the squared differences between each value and the expectation. For example, if X is the same random variable as above, then the variance of X is Var(X) = (0 - 1)^2 * (1/4) + (1 - 1)^2 * (1/2) + (2 - 1)^2 * (1/4) = 1/2.
- The standard deviation of a random variable, denoted by SD(X), is the square root of the variance. It is a more intuitive measure of the spread of X, as it has the same units as X. For example, if X is the same random variable as above, then the standard deviation of X is SD(X) = sqrt(1/2) = 0.707.
- Expectation and variance have some useful properties that make them easier to calculate and manipulate. Some of these properties are:

  - E(a) = a, where a is a constant.
  - E(aX + b) = aE(X) + b, where a and b are constants.
  - Var(a) = 0, where a is a constant.
  - Var(aX + b) = a^2 Var(X), where a and b are constants.
  - SD(aX + b) = |a| SD(X), where a and b are constants.
  - E(X + Y) = E(X) + E(Y), where X and Y are any two random variables.
  - Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y), where X and Y are any two random variables, and Cov(X, Y) is the covariance between X and Y, which measures how much X and Y vary together.
  - SD(X + Y) = sqrt(Var(X + Y)), where X and Y are any two random variables.

- Expectation and variance are useful for describing the behavior and the uncertainty of random variables, and for making inferences and predictions based on data. For example, expectation and variance can be used to calculate the mean and the standard error of a sample mean, which are important statistics for estimating the population mean and its confidence interval.

Some possible mnemonics and learning tricks for the topic are:

- To remember the formula for expectation, think of E(X) as the Expected value of X, and multiply each value by its probability.
- To remember the formula for variance, think of Var(X) as the Variation of X, and square the difference between each value and the expectation, then multiply by its probability.
- To remember the formula for standard deviation, think of SD(X) as the Standard Distance of X, and take the square root of the variance.
- To remember the properties of expectation and variance, think of the following acronyms:

  - LIE: Linearity of Expectation. E(aX + b) = aE(X) + b.
  - VAC: Variance of a Constant. Var(a) = 0.
  - VAS: Variance of a Scaled variable. Var(aX + b) = a^2 Var(X).
  - SAS: Standard deviation of a Scaled variable. SD(aX + b) = |a| SD(X).
  - ADE: Addition of Expectations. E(X + Y) = E(X) + E(Y).
  - VAC: Variance of a Combination. Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y).
  - SAV: Standard deviation of a Combination. SD(X + Y) = sqrt(Var(X + Y)).