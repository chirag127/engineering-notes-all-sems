# Inverse-transform method for pseudo-random numbers

- The inverse-transform method is a basic technique for generating pseudo-random numbers from any probability distribution given its cumulative distribution function (CDF)   .
- The inverse-transform method works as follows :
  - Generate a random number u from the standard uniform distribution in the interval [0, 1].
  - Find the inverse of the desired CDF, i.e. F<sub>X</sub><sup>-1</sup>(u).
  - Compute X'(u) = F<sub>X</sub><sup>-1</sup>(u), which is a pseudo-random number from the desired distribution.
- The inverse-transform method is based on the fact that the CDF of a random variable has a uniform distribution on [0, 1].
- The inverse-transform method can be applied to any distribution that has a closed-form inverse CDF, such as the exponential, normal, gamma, beta, etc.
- The inverse-transform method can also be used to generate pseudo-random numbers from discrete distributions, such as the binomial, Poisson, geometric, etc., by using the inverse CDF of the corresponding probability mass function (PMF).
- The inverse-transform method has some advantages and disadvantages :
  - Advantages:
    - It is simple and easy to implement.
    - It can generate pseudo-random numbers from any distribution with a known inverse CDF.
    - It preserves the properties of the original distribution, such as the mean, variance, skewness, etc.
  - Disadvantages:
    - It can be computationally expensive or impossible to find the inverse CDF for some distributions, such as the Weibull, lognormal, etc.
    - It can introduce numerical errors or truncation errors due to the finite precision of the computer.
    - It can produce poor quality pseudo-random numbers if the inverse CDF is not a smooth function or has discontinuities.