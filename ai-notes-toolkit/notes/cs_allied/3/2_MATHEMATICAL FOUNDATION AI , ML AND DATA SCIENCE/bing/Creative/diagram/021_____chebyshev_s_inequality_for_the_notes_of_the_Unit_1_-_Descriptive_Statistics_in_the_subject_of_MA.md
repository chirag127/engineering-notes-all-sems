### Chebyshev’s inequality

- Chebyshev’s inequality is a theorem in probability theory that describes how far the values of a distribution can deviate from its mean  .
- The inequality states that for any distribution with a finite mean and variance, the probability that a value is more than k standard deviations away from the mean is at most 1/k^2  .
- Mathematically, the inequality can be written as:

```math
P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}
```

where X is a random variable, \mu is the mean, \sigma is the standard deviation, and k is any positive number  .

- The inequality can also be expressed in terms of the absolute deviation from the mean, as:

```math
P(|X - \mu| \geq c) \leq \frac{\sigma^2}{c^2}
```

where c is any positive number  .

- The inequality is useful because it applies to any distribution, regardless of its shape or parameters  . It provides a lower bound on how much of the distribution is concentrated near the mean  .
- For example, Chebyshev’s inequality guarantees that at least 75% of the values are within two standard deviations of the mean, and at least 88.9% of the values are within three standard deviations of the mean  . These bounds are valid for any distribution, but they may not be tight for some distributions  .
- Chebyshev’s inequality can be used to estimate the probability of rare events, to construct confidence intervals, and to compare different distributions  .

: Chebyshev's inequality - Wikipedia
: Chebyshev’s Inequality - Overview, Statement, Example
: Chebyshev’s inequality | mathematics | Britannica