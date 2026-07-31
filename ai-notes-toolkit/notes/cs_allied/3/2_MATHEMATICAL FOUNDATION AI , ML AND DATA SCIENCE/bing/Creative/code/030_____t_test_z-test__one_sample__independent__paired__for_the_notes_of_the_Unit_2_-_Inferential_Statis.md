### t-test/z-test (one sample, independent, paired)

- A t-test is a statistical test that is used to compare the means of two groups or the mean of one group against a known value. It is often used in hypothesis testing to determine whether a process or treatment actually has an effect on the population of interest, or whether two groups are different from one another.
- A z-test is a statistical test that is used to test the hypothesis that proportions from two independent samples differ greatly. It is also used to test the hypothesis that the mean of one group is equal to a specified value, when the population standard deviation is known.
- Both t-test and z-test are parametric tests, which means they assume that the samples are normally distributed. They also use the same formula to calculate the test statistic, but they differ in the way they estimate the standard error of the mean.
- The standard error of the mean is the standard deviation of the sampling distribution of the mean. It measures how much the sample mean varies from the population mean. The smaller the standard error, the more precise the sample mean is as an estimate of the population mean.
- The formula for the test statistic is:

$$
z = \frac{\bar{x} - \mu}{\frac{s}{\sqrt{n}}}
$$

where $\bar{x}$ is the sample mean, $\mu$ is the population mean or the known value, $s$ is the sample standard deviation or the population standard deviation, and $n$ is the sample size.

- The formula for the standard error of the mean depends on whether the sample standard deviation or the population standard deviation is used. If the population standard deviation is known, the standard error is:

$$
SE = \frac{s}{\sqrt{n}}
$$

where $s$ is the population standard deviation and $n$ is the sample size. This is the case for the z-test.

- If the population standard deviation is unknown, the standard error is:

$$
SE = \frac{s}{\sqrt{n}}
$$

where $s$ is the sample standard deviation and $n$ is the sample size. This is the case for the t-test.

- The main difference between the t-test and the z-test is that the t-test uses the sample standard deviation to estimate the standard error, while the z-test uses the population standard deviation. This means that the t-test is more appropriate when the sample size is small or the population standard deviation is unknown, while the z-test is more appropriate when the sample size is large or the population standard deviation is known .
- Another difference between the t-test and the z-test is that the t-test uses the t-distribution to determine the critical values and the p-values, while the z-test uses the standard normal distribution. The t-distribution is a family of distributions that depends on the degrees of freedom, which is the number of independent observations in the sample minus one. The t-distribution is similar to the standard normal distribution, but it has fatter tails and a lower peak. This means that the t-distribution is more conservative than the standard normal distribution, and it requires larger test statistics to reject the null hypothesis.
- There are three main types of t-test: one sample t-test, independent sample t-test, and paired sample t-test. Each type of t-test has a different purpose and a different way of calculating the test statistic and the degrees of freedom.

  - One sample t-test: A statistical test that is used to test the hypothesis that the mean of one group is equal to a specified value. The test statistic is calculated by:

  $$
  t = \frac{\bar{x} - \mu}{\frac{s}{\sqrt{n}}}
  $$

  where $\bar{x}$ is the sample mean, $\mu$ is the specified value, $s$ is the sample standard deviation, and $n$ is the sample size. The degrees of freedom are $n - 1$.

  - Independent sample t-test: A statistical test that is used to compare the means of two independent groups. The test statistic is calculated by:

  $$
  t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}
  $$

  where $\bar{x}_1$ and $\bar{x}_2$ are the sample means of the two groups, $s_1^2$