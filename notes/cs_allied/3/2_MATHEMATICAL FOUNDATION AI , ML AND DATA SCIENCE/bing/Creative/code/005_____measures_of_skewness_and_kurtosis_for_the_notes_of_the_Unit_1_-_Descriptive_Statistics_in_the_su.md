Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of measures of skewness and kurtosis for the notes of the Unit 1 - Descriptive Statistics in the subject of MATHEMATICAL FOUNDATION AI , ML AND DATA SCIENCE.

```markdown
# Measures of Skewness and Kurtosis

## Skewness
- Skewness is a measure of the asymmetry of a probability distribution.
- A distribution is symmetric if it looks the same to the left and right of the center point.
- A distribution is skewed if one of its tails is longer than the other.
- The skewness of a distribution is defined as the third standardized moment, which is the ratio of the third central moment and the cube of the standard deviation.
- The skewness of a distribution can be positive, negative, or zero.
- A positive skewness means that the distribution has a longer right tail, and the mean is greater than the median.
- A negative skewness means that the distribution has a longer left tail, and the mean is less than the median.
- A zero skewness means that the distribution is symmetric, and the mean is equal to the median.
- Skewness can be calculated using the formula:

    `skewness = E[(X - μ)^3] / σ^3`

    where X is a random variable, μ is the mean, σ is the standard deviation, and E is the expectation operator.

- Skewness can also be estimated from a sample using the formula:

    `skewness = (n / ((n - 1) (n - 2))) * Σ((x_i - x_bar)^3 / s^3)`

    where n is the sample size, x_i is the i-th observation, x_bar is the sample mean, s is the sample standard deviation, and Σ is the summation operator.

- Some examples of skewed distributions are:

    - The exponential distribution, which has a positive skewness of 2.
    - The lognormal distribution, which has a positive skewness that depends on the parameters.
    - The beta distribution, which can have positive or negative skewness depending on the parameters.
    - The normal distribution, which has a zero skewness.

## Kurtosis
- Kurtosis is a measure of the peakedness or flatness of a probability distribution.
- A distribution is peaked if it has a higher probability of values near the mean, and a lower probability of values far from the mean.
- A distribution is flat if it has a lower probability of values near the mean, and a higher probability of values far from the mean.
- The kurtosis of a distribution is defined as the fourth standardized moment, which is the ratio of the fourth central moment and the fourth power of the standard deviation.
- The kurtosis of a distribution can be any non-negative number.
- A common reference point for kurtosis is the normal distribution, which has a kurtosis of 3.
- A distribution with a kurtosis greater than 3 is called leptokurtic, which means it is more peaked than the normal distribution.
- A distribution with a kurtosis less than 3 is called platykurtic, which means it is more flat than the normal distribution.
- A distribution with a kurtosis equal to 3 is called mesokurtic, which means it has the same peakedness as the normal distribution.
- Kurtosis can be calculated using the formula:

    `kurtosis = E[(X - μ)^4] / σ^4`

    where X is a random variable, μ is the mean, σ is the standard deviation, and E is the expectation operator.

- Kurtosis can also be estimated from a sample using the formula:

    `kurtosis = ((n (n + 1)) / ((n - 1) (n - 2) (n - 3))) * Σ((x_i - x_bar)^4 / s^4) - (3 (n - 1)^2 / ((n - 2) (n - 3)))`

    where n is the sample size, x_i is the i-th observation, x_bar is the sample mean, s is the sample standard deviation, and Σ is the summation operator.

- Some examples of distributions with different kurtosis are:

    - The uniform distribution, which has a kurtosis of 1.8, and is platykurtic.
    - The binomial distribution, which has a kurtosis that depends on the parameters, and can be platykurtic or leptokurtic.
    - The t-distribution, which has