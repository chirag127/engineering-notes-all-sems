### Moment generating function (MGF)

- A moment generating function (MGF) is a function that characterizes the probability distribution of a random variable .
- The MGF of a random variable X is defined as M_X(t) = E[e^{tX}], where E is the expectation operator and e is the base of the natural logarithm   .
- The MGF is called so because its derivatives at t = 0 are equal to the moments of X, that is, M_X^{(n)}(0) = E[X^n], where n is a positive integer  .
- The MGF can be used to easily derive moments, as well as other properties of the distribution, such as the mean, variance, skewness, kurtosis, etc .
- The MGF also provides a way to identify the distribution of X, as different distributions have different MGFs. If two random variables have the same MGF, then they have the same distribution .
- The MGF does not always exist for every random variable, unlike the characteristic function. The MGF exists if there is a positive constant c such that E[e^{tX}] is finite for all |t| < c .
- Some examples of MGFs for common distributions are:

  - Uniform distribution: M_X(t) = \frac{e^{tb} - e^{ta}}{t(b-a)}, where a and b are the lower and upper bounds of the distribution.
  - Normal distribution: M_X(t) = e^{\mu t + \frac{1}{2}\sigma^2 t^2}, where \mu and \sigma are the mean and standard deviation of the distribution.
  - Exponential distribution: M_X(t) = \frac{\lambda}{\lambda - t}, where \lambda is the rate parameter of the distribution.
  - Binomial distribution: M_X(t) = (pe^t + q)^n, where p and q are the probabilities of success and failure, and n is the number of trials.
  - Poisson distribution: M_X(t) = e^{\lambda (e^t - 1)}, where \lambda is the mean and variance of the distribution.