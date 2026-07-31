# Moment generating function (MGF)

- A moment generating function (MGF) is a function that can be used to characterize the distribution of a random variable .
- The MGF of a random variable X is defined as M_X(t) = E[e^{tX}], where E is the expectation operator and e is the base of the natural logarithm   .
- The MGF has the following properties  :
  - The MGF is unique for a given distribution, i.e., two random variables with the same MGF have the same distribution.
  - The MGF can be used to derive the moments of a random variable, i.e., the nth derivative of the MGF at t = 0 is equal to the nth moment of the random variable.
  - The MGF can be used to find the distribution of a linear transformation of a random variable, i.e., if Y = aX + b, then M_Y(t) = e^{bt}M_X(at).
  - The MGF can be used to find the distribution of a sum of independent random variables, i.e., if X_1, X_2, ..., X_n are independent, then M_{X_1 + X_2 + ... + X_n}(t) = M_{X_1}(t)M_{X_2}(t)...M_{X_n}(t).
- The MGF does not always exist for a given random variable, unlike the characteristic function. The MGF exists if there is a positive constant c such that E[e^{tX}] is finite for all |t| < c .
- Some examples of MGFs for common distributions are :
  - Uniform distribution: M_X(t) = \frac{e^{tb} - e^{ta}}{t(b - a)}, where a and b are the lower and upper bounds of the distribution.
  - Normal distribution: M_X(t) = e^{\mu t + \frac{1}{2}\sigma^2 t^2}, where \mu and \sigma^2 are the mean and variance of the distribution.
  - Exponential distribution: M_X(t) = \frac{\lambda}{\lambda - t}, where \lambda is the rate parameter of the distribution.
  - Poisson distribution: M_X(t) = e^{\lambda (e^t - 1)}, where \lambda is the mean and variance of the distribution.
  - Binomial distribution: M_X(t) = (pe^t + 1 - p)^n, where p is the probability of success and n is the number of trials of the distribution.