# Central Limit Theorem

The central limit theorem (CLT) is one of the most fundamental and important theorems in statistics. It states that:

- For any population with mean μ and standard deviation σ, the distribution of sample means of size n will approach a normal distribution with mean μ and standard deviation σ/√n as n increases.
- This means that the sampling distribution of the mean will be approximately normal, regardless of the shape of the population distribution, as long as the sample size is large enough (usually n ≥ 30).
- The CLT also implies that the sample mean is an unbiased and consistent estimator of the population mean, meaning that it is accurate and reliable as n increases.

The CLT has many applications and implications in statistics, such as:

- It allows us to use the normal distribution to calculate confidence intervals and perform hypothesis tests for the population mean, even if the population is not normal.
- It enables us to use the t-distribution to perform the same tasks when the population standard deviation is unknown, as long as the sample size is large enough or the population is normal.
- It provides the theoretical basis for the law of large numbers, which states that the sample mean converges to the population mean as n increases.
- It explains why many natural and social phenomena tend to follow the normal distribution, such as heights, weights, IQ scores, test scores, errors, etc.

The CLT can be illustrated by the following example:

- Suppose we have a population of dice rolls, which has a uniform distribution with mean 3.5 and standard deviation 1.71.
- If we take a random sample of size 1 from this population and calculate the sample mean, we will get a value between 1 and 6, with equal probability.
- If we take a random sample of size 2 from this population and calculate the sample mean, we will get a value between 1 and 6, but with different probabilities. For example, the probability of getting a sample mean of 1 is 1/36, while the probability of getting a sample mean of 3.5 is 6/36.
- If we take a random sample of size 10 from this population and calculate the sample mean, we will get a value between 1 and 6, but with even more different probabilities. For example, the probability of getting a sample mean of 1 is 1/60,467,200, while the probability of getting a sample mean of 3.5 is 0.12.
- If we take a random sample of size 30 from this population and calculate the sample mean, we will get a value that is very close to 3.5, with a very high probability. The distribution of the sample means will look like a normal distribution with mean 3.5 and standard deviation 1.71/√30 = 0.31.

The following graph shows the histograms of the sample means for different sample sizes, along with the normal curve that approximates the sampling distribution.

![Histograms of sample means for different sample sizes](https://www.statology.org/wp-content/uploads/2019/04/clt.png)

Source: [Statology](https://www.statology.org/central-limit-theorem/)

The CLT can be mathematically proven using various methods, such as the characteristic function, the moment-generating function, or the Taylor series expansion. However, these methods are beyond the scope of this note. For more details, please refer to the following sources:

- [Investopedia](https://www.investopedia.com/terms/c/central_limit_theorem.asp)
- [Wikipedia](https://en.wikipedia.org/wiki/Central_limit_theorem)
- [Scribbr](https://www.scribbr.com/statistics/central-limit-theorem/)