### Importance sampling

- Importance sampling is a **variance reduction technique** that can be used in the **Monte Carlo method**.
- The idea behind importance sampling is that certain values of the input random variables in a simulation have more impact on the parameter being estimated than others.
- Importance sampling can be used to evaluate properties of a particular distribution, while only having samples generated from a different distribution than the distribution of interest.
- The basic idea of importance sampling is to sample the states from a different distribution to lower the variance of the estimation of E[X;P], or when sampling from P is difficult.
- This is accomplished by first choosing a random variable L such that E[L;P] = 1 and that L > 0 P-almost everywhere.
- Then, the expectation of X with respect to P can be written as E[X;P] = E[XL;P] = E[X/L;L].
- The last equality follows from the law of total expectation.
- Therefore, we can estimate E[X;P] by generating samples from L and computing the sample mean of X/L.
- The choice of L is crucial for the efficiency of importance sampling. A good choice of L should have the following properties:
  - L should be easy to sample from and compute the density or probability mass function.
  - L should have a similar shape as XP, so that the ratio X/L does not vary too much.
  - L should have a heavier tail than P, so that the rare events that contribute significantly to E[X;P] are not missed.
- The approximation error of importance sampling depends on the variance of X/L and the number of samples. The ideal case is when L = XP, which leads to zero variance and exact estimation. However, this is usually not possible or practical.
- An example of importance sampling is estimating the probability of a rare event, such as a coin landing on its edge. Suppose we toss a coin 100 times and we want to estimate the probability of getting at least one edge. The naive Monte Carlo method would require a very large number of simulations to observe such an event. However, we can use importance sampling by choosing L to be a distribution that assigns a higher probability to the edge outcome than the actual coin. For instance, we can use a triangular distribution that assigns 0.01 probability to the edge, 0.495 to the head, and 0.495 to the tail. Then, we can generate samples from L and compute the ratio X/L, where X is the indicator function of the event of interest. The sample mean of X/L will be an unbiased estimator of the probability of the event.