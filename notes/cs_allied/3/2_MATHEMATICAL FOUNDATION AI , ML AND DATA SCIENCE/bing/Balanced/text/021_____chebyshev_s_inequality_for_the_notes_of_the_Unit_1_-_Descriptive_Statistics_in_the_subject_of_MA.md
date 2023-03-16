### Chebyshev’s Inequality

- Chebyshev’s inequality is a theorem in probability theory that guarantees that, for any probability distribution, no more than a certain fraction of values can be more than a certain distance from the mean .
- The fraction is given by 1/k^2, where k is the number of standard deviations from the mean. The distance is given by k times the standard deviation of the distribution .
- Chebyshev’s inequality can be written as:

P(|X - μ| ≥ kσ) ≤ 1/k^2

where X is a random variable, μ is the mean, σ is the standard deviation, and k is any positive number .

- Chebyshev’s inequality is useful because it applies to any probability distribution, regardless of its shape or parameters . It provides a lower bound for the probability that a value will be within a certain number of standard deviations from the mean .
- For example, Chebyshev’s inequality states that at most 25% of the values will be more than two standard deviations from the mean (k = 2), and at most 11.11% of the values will be more than three standard deviations from the mean (k = 3)  . These bounds are valid for any distribution, but they may not be tight for some distributions, such as the normal distribution, which has smaller probabilities of extreme values .
- Chebyshev’s inequality can be used to analyze the variability of data, to estimate confidence intervals, and to test hypotheses . It can also be generalized to higher moments, such as the variance and the skewness, and to multivariate distributions .