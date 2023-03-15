# Moment generating function (MGF)

- A moment generating function (MGF) is a function that can be used to characterize the distribution of a random variable  .
- The MGF of a random variable X is defined as M_X(t) = E[e^(tX)], where t is a real parameter and E is the expectation operator  .
- The MGF has the following properties :
  - It can be used to easily derive moments of X, such as the mean, variance, skewness, etc. by taking derivatives of M_X(t) and evaluating them at t = 0.
  - It can be used to identify the distribution of X, if the MGF of X is unique and matches the MGF of a known distribution.
  - It can be used to find the distribution of a linear transformation of X, such as aX + b, by using the property M_(aX+b)(t) = e^(bt)M_X(at).
  - It can be used to find the distribution of a sum of independent random variables, such as X + Y, by using the property M_(X+Y)(t) = M_X(t)M_Y(t).
- The MGF of a random variable does not always exist, unlike the characteristic function. The MGF of X exists if there is a positive constant c such that E[e^(tX)] is finite for all |t| < c.