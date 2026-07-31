### Inverse-transform method for pseudo-random number sampling

- The inverse-transform method is a basic technique for generating sample numbers at random from any probability distribution given its cumulative distribution function (CDF) .
- The CDF of a random variable X is defined as F(x) = P(X ≤ x) for any x in the domain of X. It is a non-decreasing function that ranges from 0 to 1.
- The inverse-transform method works as follows :
  - Generate a uniform random number U between 0 and 1.
  - Find the inverse of the CDF, F<sup>-1</sup>, such that F<sup>-1</sup>(U) = x.
  - Return x as the sample from the desired distribution.
- The inverse-transform method is based on the fact that the CDF of a random variable X has a uniform distribution on [0, 1], i.e., F(X) ~ U(0, 1).
- The inverse-transform method can be applied to any distribution that has a continuous and strictly increasing CDF with a known inverse .
- Some examples of distributions that can be sampled using the inverse-transform method are the exponential, the normal, the lognormal, and the gamma distributions .
- The inverse-transform method has some advantages and disadvantages:
  - It is simple and easy to implement for many distributions.
  - It is exact and does not introduce any approximation error.
  - It is efficient and does not require rejection of any samples.
  - However, it may be difficult or impossible to find the inverse of the CDF for some distributions, such as the beta and the Weibull distributions.
  - It may also be computationally expensive or numerically unstable to evaluate the inverse of the CDF for some distributions, such as the normal and the lognormal distributions.