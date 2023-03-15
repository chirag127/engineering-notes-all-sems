### Poisson Distribution

- A Poisson distribution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space if these events occur with a known constant mean rate and independently of the time since the last event.
- The Poisson distribution has only one parameter, λ (lambda), which is the mean number of events per interval.
- The Poisson distribution can be used to model various phenomena such as the number of phone calls received by a call center, the number of radioactive decays in a sample, the number of customers arriving at a shop, etc.
- The probability mass function (PMF) of the Poisson distribution is given by:

![Poisson PMF](https://latex.codecogs.com/png.latex?P%28X%3Dk%29%3D%5Cfrac%7B%5Clambda%5Eke%5E%7B-%5Clambda%7D%7D%7Bk%21%7D)

where k is the number of events, λ is the mean number of events per interval, and e is the base of the natural logarithm.

- The Poisson distribution has the following properties:

  - The mean of the Poisson distribution is equal to λ, i.e., E(X) = λ.
  - The variance of the Poisson distribution is also equal to λ, i.e., Var(X) = λ.
  - The standard deviation of the Poisson distribution is equal to the square root of λ, i.e., SD(X) = √λ.
  - The mode of the Poisson distribution is equal to the largest integer less than or equal to λ, i.e., Mode(X) = ⌊λ⌋.
  - The skewness of the Poisson distribution is equal to 1/√λ, i.e., Skew(X) = 1/√λ.
  - The kurtosis of the Poisson distribution is equal to 1/λ, i.e., Kurt(X) = 1/λ.
  - The Poisson distribution is a special case of the binomial distribution when the number of trials is large and the probability of success is small, i.e., n → ∞ and p → 0 such that np = λ.
  - The Poisson distribution is also a special case of the negative binomial distribution when the number of failures is fixed at zero, i.e., r = 0.
  - The Poisson distribution is related to the exponential distribution by the following formula: If X ~ Poisson(λ), then the time between two successive events, T, follows an exponential distribution with parameter λ, i.e., T ~ Exp(λ).