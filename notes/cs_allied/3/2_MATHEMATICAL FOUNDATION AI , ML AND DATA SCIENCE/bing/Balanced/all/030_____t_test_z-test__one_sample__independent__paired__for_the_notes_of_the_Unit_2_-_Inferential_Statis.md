# t-test/z-test (one sample, independent, paired)

- A t-test is a statistical test that is used to compare the means of two groups or the mean of one group against a known value. It is often used in hypothesis testing to determine whether a process or treatment actually has an effect on the population of interest, or whether two groups are different from one another.
- A z-test is a statistical test that is used to test the hypothesis that proportions from two independent samples differ greatly. It is also used to test the hypothesis that the mean of a population is equal to a specified value, when the population standard deviation is known.
- There are three main types of t-tests:
  - One sample t-test: A statistical test that compares the mean of a sample to a known value, such as the population mean. The null hypothesis is that the sample mean is equal to the known value. The alternative hypothesis is that the sample mean is not equal to the known value.
  - Independent sample t-test: A statistical test that compares the means of two independent groups. The null hypothesis is that the means of the two groups are equal. The alternative hypothesis is that the means of the two groups are not equal.
  - Paired sample t-test: A statistical test that compares the means of two dependent groups or repeated measures. The null hypothesis is that the mean difference between the paired observations is zero. The alternative hypothesis is that the mean difference between the paired observations is not zero.
- The main difference between t-test and z-test is that t-test is used when the population standard deviation is unknown or the sample size is small, while z-test is used when the population standard deviation is known or the sample size is large.
- The main similarity between t-test and z-test is that both tests assume that the samples are normally distributed and that the sampling is random.
- The formula for t-test is:

  - One sample t-test: t = (x̄ - μ) / (s / √n), where x̄ is the sample mean, μ is the known value, s is the sample standard deviation, and n is the sample size.
  - Independent sample t-test: t = (x̄1 - x̄2) / √((s1^2 / n1) + (s2^2 / n2)), where x̄1 and x̄2 are the sample means, s1 and s2 are the sample standard deviations, and n1 and n2 are the sample sizes of the two groups.
  - Paired sample t-test: t = (d̄ - μd) / (sd / √n), where d̄ is the mean difference between the paired observations, μd is the hypothesized mean difference, sd is the standard deviation of the differences, and n is the number of pairs.

- The formula for z-test is:

  - One sample z-test: z = (x̄ - μ) / (σ / √n), where x̄ is the sample mean, μ is the known value, σ is the population standard deviation, and n is the sample size.
  - Two sample z-test: z = (p1 - p2) / √((p(1 - p) / n1) + (p(1 - p) / n2)), where p1 and p2 are the sample proportions, p is the pooled proportion, and n1 and n2 are the sample sizes of the two groups.