### Inference procedure for correlation coefficient

The correlation coefficient is a measure of the strength and direction of the linear relationship between two variables. It ranges from -1 to 1, where -1 indicates a perfect negative correlation, 0 indicates no correlation, and 1 indicates a perfect positive correlation.

To test the significance of the correlation coefficient, we can use the following steps:

1. State the null and alternative hypotheses. The null hypothesis is that the population correlation coefficient is zero, meaning that there is no linear relationship between the variables. The alternative hypothesis is that the population correlation coefficient is not zero, meaning that there is a linear relationship between the variables.
2. Calculate the t value using this formula: `t = r * sqrt((n - 2) / (1 - r^2))`, where `r` is the sample correlation coefficient and `n` is the sample size. This is the test statistic that follows a t distribution with `n - 2` degrees of freedom under the null hypothesis.
3. Find the critical value of t from a t table, using the significance level (usually 0.05) and the degrees of freedom. This is the value that marks the boundary of the rejection region, where we reject the null hypothesis if the test statistic falls in this region.
4. Compare the t value to the critical value and decide whether to reject or fail to reject the null hypothesis. If the absolute value of the t value is greater than or equal to the critical value, we reject the null hypothesis and conclude that there is a significant linear relationship between the variables. If the absolute value of the t value is less than the critical value, we fail to reject the null hypothesis and conclude that there is no significant linear relationship between the variables.
5. Report the results, including the t value, the degrees of freedom, the p value, and the confidence interval for the population correlation coefficient. The p value is the probability of obtaining a test statistic as extreme or more extreme than the observed one, assuming the null hypothesis is true. The confidence interval is a range of values that is likely to contain the true population correlation coefficient with a certain level of confidence (usually 95%). The confidence interval can be calculated using the Fisher transformation, which converts the correlation coefficient to a normally distributed variable. The steps are:

  - Compute the Fisher transform: `Z = 0.5 * log((1 + r) / (1 - r))`, where `r` is the sample correlation coefficient.
  - Compute the standard error of the Fisher transform: `SE = 1 / sqrt(n - 3)`, where `n` is the sample size.
  - Compute the confidence interval for the Fisher transform: `Z +/- t* * SE`, where `t*` is the critical value of t from the t table, using the significance level and the degrees of freedom `n - 3`.
  - Back-transform the confidence interval to the original scale: `r = (e^(2Z) - 1) / (e^(2Z) + 1)`, where `Z` is the lower and upper bounds of the confidence interval for the Fisher transform, and `e` is the base of the natural logarithm.

Example:

Suppose we want to test the significance of the correlation coefficient between the height and weight of 10 students. The sample correlation coefficient is 0.77. The null and alternative hypotheses are:

- H0: ρ = 0 (There is no linear relationship between height and weight.)
- Ha: ρ ≠ 0 (There is a linear relationship between height and weight.)

The steps are:

- Calculate the t value: `t = 0.77 * sqrt((10 - 2) / (1 - 0.77^2)) = 3.35`
- Find the critical value of t: Using a significance level of 0.05 and 8 degrees of freedom, the critical value of t is 2.306.
- Compare the t value to the critical value: Since the absolute value of the t value (3.35) is greater than the critical value (2.306), we reject the null hypothesis and conclude that there is a significant linear relationship between height and weight.
- Report the results: The t value is 3.35 with 8 degrees of freedom and a p value of 0.01. The 95% confidence interval for the population correlation coefficient is (0.29, 0.94). We can write the results as:

  - There is a significant positive correlation between height and weight (r = 0.