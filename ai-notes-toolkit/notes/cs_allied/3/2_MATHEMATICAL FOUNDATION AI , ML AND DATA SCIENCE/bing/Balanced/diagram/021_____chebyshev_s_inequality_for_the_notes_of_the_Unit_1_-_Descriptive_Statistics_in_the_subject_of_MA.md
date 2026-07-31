### Chebyshev's inequality

- Chebyshev's inequality is a theorem in probability theory that states that for any probability distribution, the proportion of values that are at least k standard deviations away from the mean is at most 1/k^2.
- Mathematically, Chebyshev's inequality can be written as:

  P(|X - μ| ≥ kσ) ≤ 1/k^2

  where X is a random variable, μ is the mean, σ is the standard deviation, and k is any positive number.
- Chebyshev's inequality is useful because it applies to any probability distribution, regardless of its shape or parameters. It provides a lower bound on how much of the distribution is concentrated near the mean.
- Chebyshev's inequality can be used to estimate confidence intervals for the mean of a population based on a sample. For example, if we have a sample of size n with mean x̄ and standard deviation s, then we can say that with probability at least 1 - 1/k^2, the population mean μ is within k(s/√n) of x̄. This is called the Chebyshev confidence interval.
- Chebyshev's inequality can also be used to compare different probability distributions and measure how spread out they are. For example, if we have two distributions with the same mean and standard deviation, then the one that has a smaller proportion of values more than k standard deviations away from the mean is more concentrated and less variable. This is called the Chebyshev inequality ratio.
- Chebyshev's inequality is a general result that does not depend on any specific assumptions about the distribution. However, it is often not very tight and can be improved by using more information about the distribution. For example, for the normal distribution, the proportion of values that are more than k standard deviations away from the mean is much smaller than 1/k^2 and can be calculated using the standard normal table or the error function.