# Central Limit Theorem

- The central limit theorem (CLT) is one of the most fundamental and important theorems in probability and statistics. It states that the distribution of sample means approximates a normal distribution as the sample size gets larger, regardless of the population's distribution .
- The CLT is useful because it allows us to make inferences about the population mean and other parameters based on the sample mean and other statistics. It also enables us to perform parametric tests, such as t tests, ANOVAs, and linear regression, that have more statistical power than most non-parametric tests.
- The CLT also states that the sampling distribution will have the following properties:
  - The mean of the sampling distribution will be equal to the mean of the population distribution: x = μ
  - The variance of the sampling distribution will be equal to the variance of the population distribution divided by the sample size: s^2 = σ^2 / n
  - The standard deviation of the sampling distribution will be equal to the standard deviation of the population distribution divided by the square root of the sample size: s = σ / √n
  - The shape of the sampling distribution will approach a normal distribution as the sample size increases, regardless of the shape of the population distribution.
- The CLT can be illustrated by an example. Suppose we have a population of dice rolls, which has a uniform distribution with a mean of 3.5 and a standard deviation of 1.71. If we take a random sample of size 1 from this population and calculate the sample mean, we will get a value between 1 and 6, with equal probability. The distribution of sample means for n = 1 will look like this:

![Distribution of sample means for n = 1](https://www.statology.org/wp-content/uploads/2019/10/CLT1.png)

- If we increase the sample size to 2, the distribution of sample means will change. The possible values of the sample mean will range from 1 to 6, but with different probabilities. The distribution of sample means for n = 2 will look like this:

![Distribution of sample means for n = 2](https://www.statology.org/wp-content/uploads/2019/10/CLT2.png)

- As we can see, the distribution of sample means for n = 2 is more symmetric and less spread out than the distribution for n = 1. The mean of the sampling distribution is still 3.5, but the variance and standard deviation are smaller. The variance is 1.71^2 / 2 = 1.46, and the standard deviation is 1.71 / √2 = 1.21.
- If we continue to increase the sample size, the distribution of sample means will become more and more normal, with a mean of 3.5 and a standard deviation that decreases as the sample size increases. The distribution of sample means for n = 10 will look like this:

![Distribution of sample means for n = 10](https://www.statology.org/wp-content/uploads/2019/10/CLT10.png)

- The distribution of sample means for n = 10 is very close to a normal distribution, with a mean of 3.5 and a standard deviation of 1.71 / √10 = 0.54. The CLT tells us that as the sample size approaches infinity, the distribution of sample means will converge to a normal distribution with a mean of 3.5 and a standard deviation of 0.
- The CLT is a powerful and useful theorem that allows us to make inferences about the population mean and other parameters based on the sample mean and other statistics. It also enables us to perform parametric tests that have more statistical power than most non-parametric tests. The CLT applies to any population distribution, as long as the sample size is large enough and the samples are independent and identically distributed.