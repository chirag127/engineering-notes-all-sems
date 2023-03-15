### Moment generating function (MGF)

- A moment generating function (MGF) is a function that can be used to characterize the distribution of a random variable.
- The MGF of a random variable X is defined as M_X(t) = E[e^(tX)], where t is a real number and E is the expectation operator.
- The MGF has the following properties:
  - M_X(0) = 1, since E[e^(0X)] = E[1] = 1.
  - M_X'(0) = E[X], since the derivative of e^(tX) with respect to t is Xe^(tX), and the derivative of M_X(t) at t = 0 is E[Xe^(0X)] = E[X].
  - M_X''(0) = E[X^2], since the second derivative of e^(tX) with respect to t is X^2e^(tX) + Xe^(tX), and the second derivative of M_X(t) at t = 0 is E[X^2e^(0X) + Xe^(0X)] = E[X^2] + E[X].
  - In general, M_X^(n)(0) = E[X^n], where M_X^(n)(t) is the nth derivative of M_X(t) with respect to t. This means that the moments of X can be easily derived from the MGF by taking derivatives and evaluating at t = 0.
  - If two random variables X and Y have the same MGF, then they have the same distribution. This is because the MGF uniquely determines the distribution of a random variable, as long as the MGF exists for some interval around t = 0.
  - The MGF of a linear transformation of X, such as aX + b, where a and b are constants, is M_(aX+b)(t) = e^(bt)M_X(at). This follows from the property of expectation that E[g(X)] = g(E[X]) for any function g that does not depend on X.
  - The MGF of a sum of independent random variables, such as X + Y, where X and Y are independent, is M_(X+Y)(t) = M_X(t)M_Y(t). This follows from the property of expectation that E[XY] = E[X]E[Y] for independent X and Y.