### Central Limit Theorem

The central limit theorem (CLT) is one of the most fundamental and important theorems in probability and statistics. It states that, under certain conditions, the distribution of the sample mean of a random variable approaches a normal distribution as the sample size increases, regardless of the shape of the original distribution.

The CLT has many applications and implications in statistics, such as:

- It allows us to use the normal distribution to approximate the sampling distribution of many statistics, such as the sample mean, the sample proportion, the difference between two sample means, etc.
- It provides a theoretical basis for hypothesis testing and confidence intervals, which are widely used in inferential statistics.
- It enables us to use the standard normal distribution (Z-distribution) to calculate probabilities and critical values for many statistics, by standardizing them using the sample mean and the standard error.

The CLT also has some key characteristics and assumptions that need to be satisfied for it to be valid, such as:

- The samples must be independent and identically distributed (i.i.d.), meaning that they are drawn randomly from the same population and do not affect each other.
- The sample size must be large enough for the CLT to hold. A common rule of thumb is that the sample size should be at least 30, but this may vary depending on the shape of the population distribution. The more skewed or non-normal the population distribution is, the larger the sample size needed for the CLT to apply.
- The population distribution must have a finite mean and variance, meaning that it is not too extreme or irregular.

The CLT can be mathematically expressed as follows:

Let X1, X2, ..., Xn be a random sample of size n from a population with mean μ and variance σ2. Then, as n approaches infinity, the distribution of the sample mean X̄ converges to a normal distribution with mean μ and variance σ2/n, or equivalently, the standardized sample mean (X̄ - μ) / (σ / √n) converges to a standard normal distribution with mean 0 and variance 1.

This can be written as:

X̄ ~ N(μ, σ2/n) as n → ∞

or

(X̄ - μ) / (σ / √n) ~ N(0, 1) as n → ∞

where ~ means "is approximately distributed as" and N(μ, σ2) denotes a normal distribution with mean μ and variance σ2.

The following diagram illustrates the CLT for a population distribution that is not normal, but becomes more normal as the sample size increases.

![CLT diagram](https://www.statology.org/wp-content/uploads/2019/03/central-limit-theorem.png)

Source: [Statology](https://www.statology.org/central-limit-theorem/)