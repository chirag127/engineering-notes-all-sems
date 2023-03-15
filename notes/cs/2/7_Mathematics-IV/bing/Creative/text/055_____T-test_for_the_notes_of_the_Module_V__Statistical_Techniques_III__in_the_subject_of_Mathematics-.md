### T-test

A t-test is a statistical test that is used to compare the means of one or more groups of samples. It is based on the assumption that the samples are drawn from normal distributions with unknown but equal variances. A t-test can be used to test hypotheses about the difference between the population means or the difference between a sample mean and a known or hypothetical value.

There are three main types of t-test:

- **One-sample t-test**: This type of t-test is used to compare the mean of a single sample to a known or hypothetical value. For example, a one-sample t-test can be used to test whether the average height of students in a class is different from 170 cm.
- **Independent samples t-test**: This type of t-test is used to compare the means of two independent groups of samples. For example, an independent samples t-test can be used to test whether the average weight of males and females in a population is different.
- **Paired samples t-test**: This type of t-test is used to compare the means of two related groups of samples. For example, a paired samples t-test can be used to test whether the average blood pressure of patients before and after a treatment is different.

The general formula for a t-test is:

$$t = \frac{\bar{x} - \mu}{s/\sqrt{n}}$$

where:

- $\bar{x}$ is the sample mean
- $\mu$ is the population mean or the known or hypothetical value
- $s$ is the sample standard deviation
- $n$ is the sample size

The t-test statistic follows a t-distribution with $n-1$ degrees of freedom under the null hypothesis. The null hypothesis is usually that there is no difference between the means of the groups or samples. The alternative hypothesis is usually that there is a difference between the means of the groups or samples.

To perform a t-test, we need to calculate the t-statistic and compare it with a critical value from the t-distribution table for a given level of significance (usually 0.05 or 0.01) and degrees of freedom. If the absolute value of the t-statistic is greater than the critical value, we reject the null hypothesis and conclude that there is a significant difference between the means. If the absolute value of the t-statistic is less than or equal to the critical value, we fail to reject the null hypothesis and conclude that there is no significant difference between the means.

The t-test can also be performed using a p-value, which is the probability of obtaining a t-statistic as extreme or more extreme than the observed one, assuming the null hypothesis is true. If the p-value is less than the level of significance, we reject the null hypothesis and conclude that there is a significant difference between the means. If the p-value is greater than or equal to the level of significance, we fail to reject the null hypothesis and conclude that there is no significant difference between the means.