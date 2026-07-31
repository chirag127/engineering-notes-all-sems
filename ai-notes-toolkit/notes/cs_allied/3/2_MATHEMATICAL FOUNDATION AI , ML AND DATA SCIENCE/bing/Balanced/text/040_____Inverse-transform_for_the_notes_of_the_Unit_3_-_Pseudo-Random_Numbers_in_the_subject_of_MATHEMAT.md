### Inverse-transform method for pseudo-random number generation

- The inverse-transform method is a basic technique for generating pseudo-random numbers from any probability distribution given its cumulative distribution function (CDF) .
- The CDF of a random variable X is the function that gives the probability that X is less than or equal to a given value x, i.e., F_X(x) = P(X <= x) .
- The inverse-transform method works as follows  :
  - Generate a uniform random number U between 0 and 1.
  - Find the inverse of the CDF, F_X^{-1}(u), such that F_X^{-1}(u) = x if and only if F_X(x) = u.
  - Return F_X^{-1}(U) as the pseudo-random number from the distribution of X.
- The inverse-transform method is based on the fact that if U is a uniform random variable on [0, 1], then F_X^{-1}(U) has the same distribution as X  .
- The inverse-transform method can be used to generate pseudo-random numbers from any distribution that has a known and invertible CDF  .
- Some examples of distributions that have known and invertible CDFs are the exponential, normal, Poisson, binomial, and geometric distributions  .
- The inverse-transform method has some advantages and disadvantages  :
  - Advantages:
    - It is simple and intuitive to implement.
    - It can be applied to any distribution that has a known and invertible CDF.
    - It can be easily extended to generate multivariate random variables by using the inverse of the joint CDF.
  - Disadvantages:
    - It may be computationally expensive or difficult to find the inverse of the CDF, especially for complex or continuous distributions.
    - It may suffer from numerical errors or instability due to rounding or truncation of the CDF or its inverse.
    - It may not be efficient or accurate for generating random variables from distributions that have heavy tails or high variance.