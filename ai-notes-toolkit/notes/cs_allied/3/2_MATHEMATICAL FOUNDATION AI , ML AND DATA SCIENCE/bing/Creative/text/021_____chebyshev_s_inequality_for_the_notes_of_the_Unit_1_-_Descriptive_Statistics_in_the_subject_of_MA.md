### Chebyshev’s inequality

- Chebyshev’s inequality is a theorem in probability theory that describes how far the values of a distribution can deviate from its mean  .
- The inequality states that for any real number k > 0, the probability that a value is at least k standard deviations away from the mean is at most 1/k^2  .
- Mathematically, the inequality can be written as:

P(|X - μ| ≥ kσ) ≤ 1/k^2

where X is a random variable, μ is the mean, σ is the standard deviation, and k is any positive number  .

- The inequality can also be expressed in terms of the variance, which is the square of the standard deviation:

P(|X - μ| ≥ k√V) ≤ V/k^2

where V is the variance  .

- The inequality is useful because it applies to any distribution, regardless of its shape or parameters  . It provides a lower bound on how much of the distribution is concentrated near the mean.
- The inequality can be used to estimate the range of values that contain a certain percentage of the distribution. For example, if we want to find the range that contains 75% of the distribution, we can set 1/k^2 = 0.25 and solve for k. We get k = 2, which means that the range is within two standard deviations from the mean .
- Similarly, if we want to find the range that contains 89% of the distribution, we can set 1/k^2 = 0.11 and solve for k. We get k = 3, which means that the range is within three standard deviations from the mean .
- The inequality gives a conservative estimate of the range, meaning that it may be wider than the actual range for some distributions. For example, for the normal distribution, about 95% of the values are within two standard deviations from the mean, and about 99.7% are within three standard deviations from the mean. Chebyshev’s inequality gives lower bounds of 75% and 89%, respectively .
- Chebyshev’s inequality can be generalized to higher moments, such as the skewness and kurtosis, which measure the asymmetry and peakedness of a distribution, respectively. It can also be extended to multivariate distributions, which involve more than one random variable.