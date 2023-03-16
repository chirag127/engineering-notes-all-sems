# Central Limit Theorem

- The central limit theorem (CLT) is one of the most fundamental and important theorems in probability and statistics.
- The CLT states that, under certain conditions, the distribution of the sample means of a random variable approaches a normal distribution as the sample size increases, regardless of the shape of the population distribution.
- The CLT is useful because it allows us to make inferences about the population parameters, such as the mean and the standard deviation, based on the sample statistics, such as the sample mean and the sample standard deviation.
- The CLT also enables us to apply parametric tests, such as t-tests, ANOVAs, and linear regression, that assume normality of the data, even if the original data are not normally distributed.

## Key Characteristics of the CLT

- The CLT applies to any random variable that has a finite mean and variance, and that is independent and identically distributed (i.i.d.).
- The CLT requires that the sample size is sufficiently large, usually at least 30, for the approximation to be accurate.
- The CLT states that the mean of the sampling distribution of the sample mean is equal to the population mean, i.e., x = μ.
- The CLT states that the standard deviation of the sampling distribution of the sample mean is equal to the population standard deviation divided by the square root of the sample size, i.e., s = σ / √n.
- The CLT states that the shape of the sampling distribution of the sample mean becomes more normal as the sample size increases, regardless of the shape of the population distribution.

## Examples of the CLT

- Suppose we have a population of dice rolls, where each roll can take a value from 1 to 6 with equal probability. The population mean is 3.5 and the population standard deviation is 1.71.
- If we take a random sample of size 10 from this population and calculate the sample mean, we get a value that may or may not be close to 3.5, depending on the sample. The sampling distribution of the sample mean for n = 10 is not very normal, as shown in the following histogram:

![Histogram of sample means for n = 10](https://www.statology.org/wp-content/uploads/2019/06/sampling-distribution-n10.png)

- If we increase the sample size to 30, the sampling distribution of the sample mean becomes more normal, as shown in the following histogram:

![Histogram of sample means for n = 30](https://www.statology.org/wp-content/uploads/2019/06/sampling-distribution-n30.png)

- If we further increase the sample size to 100, the sampling distribution of the sample mean becomes even more normal, as shown in the following histogram:

![Histogram of sample means for n = 100](https://www.statology.org/wp-content/uploads/2019/06/sampling-distribution-n100.png)

- As we can see, the CLT allows us to approximate the sampling distribution of the sample mean by a normal distribution, with the same mean and standard deviation as given by the CLT, as the sample size increases. This approximation becomes more accurate as the sample size increases.