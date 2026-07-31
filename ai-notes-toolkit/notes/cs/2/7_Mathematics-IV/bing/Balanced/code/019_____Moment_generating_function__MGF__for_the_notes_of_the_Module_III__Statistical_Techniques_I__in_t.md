### Moment generating function (MGF)

- A moment generating function (MGF) is a function that can be used to characterize the distribution of a random variable  .
- The MGF of a random variable X is defined as M_X(t) = E[e^(tX)], where t is a real parameter and E is the expectation operator  .
- The MGF has the following properties  :
  - The MGF is unique for a given distribution, i.e., if two random variables have the same MGF, they have the same distribution.
  - The MGF can be used to easily derive the moments of a random variable, i.e., the nth moment of X is equal to the nth derivative of M_X(t) evaluated at t = 0.
  - The MGF can be used to find the distribution of a linear transformation of a random variable, i.e., if Y = aX + b, then M_Y(t) = e^(bt)M_X(at).
  - The MGF can be used to find the distribution of a sum of independent random variables, i.e., if X_1, X_2, ..., X_n are independent, then M_(X_1 + X_2 + ... + X_n)(t) = M_X1(t)M_X2(t)...M_Xn(t).
- The MGF does not always exist for a given distribution, unlike the characteristic function. The MGF exists if there is a positive constant c such that E[e^(tX)] < infinity for all |t| < c .
- Some examples of MGFs for common distributions are  :
  - Normal distribution: M_X(t) = e^(mu t + sigma^2 t^2 / 2), where mu is the mean and sigma is the standard deviation.
  - Exponential distribution: M_X(t) = lambda / (lambda - t), where lambda is the rate parameter and t < lambda.
  - Poisson distribution: M_X(t) = e^(lambda (e^t - 1)), where lambda is the mean and variance.
  - Binomial distribution: M_X(t) = (p e^t + 1 - p)^n, where p is the probability of success and n is the number of trials.