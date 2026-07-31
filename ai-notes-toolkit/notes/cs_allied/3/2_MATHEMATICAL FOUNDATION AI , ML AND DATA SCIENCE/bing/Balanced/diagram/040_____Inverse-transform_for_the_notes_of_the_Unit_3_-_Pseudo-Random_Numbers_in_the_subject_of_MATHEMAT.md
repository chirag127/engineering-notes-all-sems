### Inverse-transform method for pseudo-random numbers

- The inverse-transform method is a basic technique for generating sample numbers from any probability distribution given its cumulative distribution function (CDF).
- The CDF of a random variable X is defined as F_X(x) = P(X <= x), which gives the probability that X is less than or equal to a given value x.
- The inverse-transform method works as follows:
  - Generate a random number u from the standard uniform distribution in the interval [0, 1].
  - Find the inverse of the desired CDF, i.e. F_X^(-1)(u), which gives the value of x such that F_X(x) = u.
  - Compute X' = F_X^(-1)(u), which is a sample from the distribution of X.
- The inverse-transform method is based on the fact that the CDF of a random variable has a uniform distribution on [0, 1], i.e. F_X(X) ~ U[0, 1].
- The inverse-transform method can be applied to any distribution that has a continuous and strictly increasing CDF with a known inverse.
- Some examples of distributions that can be sampled using the inverse-transform method are:
  - Exponential distribution: F_X^(-1)(u) = -ln(1 - u) / lambda, where lambda is the rate parameter.
  - Normal distribution: F_X^(-1)(u) = mu + sigma * Z, where mu is the mean, sigma is the standard deviation, and Z is the standard normal quantile function.
  - Poisson distribution: F_X^(-1)(u) = the smallest integer k such that F_X(k) >= u, where F_X(k) = e^(-lambda) * sum_{i = 0}^k (lambda^i / i!), and lambda is the mean.