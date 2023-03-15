# T-test

A t-test is a statistical test that is used to compare the means of one or two groups. It is often used in hypothesis testing to determine whether a process or treatment actually has an effect on the population of interest, or whether two groups are different from one another.

There are three main types of t-test :

- **One-sample t-test**: This test compares the mean of one sample to a known standard (or theoretical / hypothetical) mean. For example, you can use a one-sample t-test to test whether the average height of students in your class is equal to the national average.
- **Unpaired t-test**: This test compares the means of two independent groups. For example, you can use an unpaired t-test to test whether the average weight of men and women in your population is different.
- **Paired t-test**: This test compares the means of two related groups of samples. For example, you can use a paired t-test to test whether the average blood pressure of patients before and after a treatment is different.

All types of t-tests use a test statistic that follows a t-distribution under the null hypothesis. The t-distribution is a probability distribution that is similar to the normal distribution, but has heavier tails. The shape of the t-distribution depends on the degrees of freedom, which is a parameter that reflects the sample size or the number of groups being compared.

The general steps for performing a t-test are:

- Formulate a null hypothesis and an alternative hypothesis. The null hypothesis is usually a statement of no difference or no effect, while the alternative hypothesis is a statement of some difference or some effect.
- Choose an appropriate type of t-test based on the research question and the data available.
- Calculate the test statistic and the p-value using a formula or a software. The test statistic measures how far the sample mean is from the hypothesized mean (or the difference between the two sample means), while the p-value measures the probability of obtaining a test statistic as extreme or more extreme than the observed one, assuming the null hypothesis is true.
- Compare the p-value to a significance level, which is a threshold for rejecting the null hypothesis. The significance level is usually set at 0.05, which means that there is a 5% chance of rejecting the null hypothesis when it is true (a type I error). If the p-value is less than or equal to the significance level, then the null hypothesis is rejected and the alternative hypothesis is supported. If the p-value is greater than the significance level, then the null hypothesis is not rejected and the alternative hypothesis is not supported.
- Report the results and interpret them in the context of the research question. The results should include the test statistic, the p-value, the degrees of freedom, and the effect size (a measure of how large the difference or the effect is). The interpretation should explain what the results mean and what implications they have for the research problem.