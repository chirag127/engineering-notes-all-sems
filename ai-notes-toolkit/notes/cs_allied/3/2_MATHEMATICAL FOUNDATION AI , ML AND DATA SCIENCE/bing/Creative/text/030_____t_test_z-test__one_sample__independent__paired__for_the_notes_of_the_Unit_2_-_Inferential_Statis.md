### t-test/z-test (one sample, independent, paired)

- A t-test is a statistical test that is used to compare the means of two groups. It is often used in hypothesis testing to determine whether a process or treatment actually has an effect on the population of interest, or whether two groups are different from one another.
- A z-test is a statistical test that is used to compare the means of two groups when the population standard deviation is known and the sample size is large. It is based on the standard normal distribution.
- There are different types of t-tests and z-tests depending on the number and nature of the samples involved. Some of the common types are:
  - One sample t-test/z-test: This is used to compare the mean of a single sample to a known or hypothesized population mean. The null hypothesis is that the sample mean is equal to the population mean .
  - Independent samples t-test/z-test: This is used to compare the means of two independent samples from two different populations. The null hypothesis is that the population means are equal .
  - Paired samples t-test/z-test: This is used to compare the means of two dependent samples from the same population. The samples are paired based on some criteria, such as before and after measurements, matched pairs, or repeated measures. The null hypothesis is that the mean difference between the pairs is zero .
- The general formula for a t-test is:

  $$t = \frac{\bar{x} - \mu}{s/\sqrt{n}}$$

  where $\bar{x}$ is the sample mean, $\mu$ is the population mean, $s$ is the sample standard deviation, and $n$ is the sample size.

- The general formula for a z-test is:

  $$z = \frac{\bar{x} - \mu}{\sigma/\sqrt{n}}$$

  where $\bar{x}$ is the sample mean, $\mu$ is the population mean, $\sigma$ is the population standard deviation, and $n$ is the sample size.

- To perform a t-test or a z-test, the following steps are usually followed:
  - State the null and alternative hypotheses.
  - Choose the appropriate type of test and the significance level ($\alpha$).
  - Calculate the test statistic using the formula.
  - Compare the test statistic to the critical value or the p-value.
  - Draw a conclusion based on the comparison. Reject the null hypothesis if the test statistic is more extreme than the critical value or the p-value is less than the significance level. Fail to reject the null hypothesis otherwise .
- Some of the assumptions for a t-test or a z-test are:
  - The samples are randomly selected from the population.
  - The samples are independent of each other (except for paired samples).
  - The population is normally distributed or the sample size is large enough to approximate normality.
  - The population variance or standard deviation is known or can be estimated from the sample .