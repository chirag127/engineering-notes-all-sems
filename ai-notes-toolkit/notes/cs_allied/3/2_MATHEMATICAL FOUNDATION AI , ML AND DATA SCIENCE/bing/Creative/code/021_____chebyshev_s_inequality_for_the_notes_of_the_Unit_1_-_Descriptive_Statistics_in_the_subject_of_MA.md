### Chebyshev’s inequality

- Chebyshev’s inequality is a theorem in probability theory that describes how far the values of a distribution can deviate from its mean  .
- The inequality states that for any distribution with a finite mean and variance, the probability that a value is more than k standard deviations away from the mean is at most 1/k^2  .
- Mathematically, the inequality can be written as:

```
P(|X - μ| ≥ kσ) ≤ 1/k^2
```

where X is a random variable, μ is the mean, σ is the standard deviation, and k is any positive number  .

- The inequality can be used to bound the probability of extreme events, such as outliers or rare occurrences, in any distribution, regardless of its shape  .
- The inequality also implies that the fraction of values that lie within k standard deviations of the mean is at least 1 - 1/k^2  .
- For example, Chebyshev’s inequality guarantees that at least 75% of the values are within two standard deviations of the mean, and at least 88.9% of the values are within three standard deviations of the mean  .
- These bounds are valid for any distribution, but they may not be tight or optimal. For some distributions, such as the normal distribution, the actual probabilities of being within k standard deviations of the mean are much higher than the bounds given by Chebyshev’s inequality .
- Chebyshev’s inequality is named after the Russian mathematician Pafnuty Chebyshev, who proved it in the 19th century. It is also sometimes called the Bienaymé-Chebyshev inequality, after the French mathematician Irénée-Jules Bienaymé, who independently discovered it .