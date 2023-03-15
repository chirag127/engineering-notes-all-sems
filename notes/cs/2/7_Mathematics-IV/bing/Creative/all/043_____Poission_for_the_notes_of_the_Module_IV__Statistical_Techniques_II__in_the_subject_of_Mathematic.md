# Poisson Distribution

- A Poisson distribution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space if these events occur with a known constant mean rate and independently of the time since the last event .
- The Poisson distribution has only one parameter, λ (lambda), which is the mean number of events per interval.
- The Poisson distribution can be used to model various phenomena such as the number of phone calls received by a call center, the number of customers arriving at a bank, the number of radioactive decays in a sample of material, etc .
- The probability mass function (PMF) of a Poisson distribution is given by:

$$
P(X=k) = \frac{e^{-\lambda}\lambda^k}{k!}
$$

where X is the random variable that counts the number of events in an interval, k is a non-negative integer, e is the base of the natural logarithm, and k! is the factorial of k .

- The PMF of a Poisson distribution can be represented by a table or a graph. The table shows the probability of each possible value of k for a given value of λ. The graph shows the shape of the PMF as a series of vertical bars.

- Some properties of a Poisson distribution are:

  - The mean and the variance of a Poisson distribution are both equal to λ .
  - The mode of a Poisson distribution is either ⌊λ⌋ or ⌊λ⌋ + 1, where ⌊λ⌋ is the largest integer less than or equal to λ.
  - The skewness of a Poisson distribution is 1/√λ, which means that the distribution is positively skewed for λ < 10 and becomes more symmetric as λ increases.
  - The kurtosis of a Poisson distribution is 1/λ, which means that the distribution is platykurtic (flatter than a normal distribution) for λ > 3 and becomes more leptokurtic (peaked than a normal distribution) as λ decreases.
  - The Poisson distribution is a special case of the binomial distribution when the number of trials n is large and the probability of success p is small, such that np = λ .
  - The Poisson distribution is also a special case of the negative binomial distribution when the number of failures r is 1.
  - The Poisson distribution is related to the exponential distribution, which models the time between events in a Poisson process .