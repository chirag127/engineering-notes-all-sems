### ANOVA

- ANOVA stands for **Analysis of Variance**. It is a statistical test that compares the means of different groups on a certain variable .
- ANOVA can be used to test if there is a significant difference between the means of two or more groups, or if the means are equal  .
- ANOVA can be classified into different types based on the number and nature of the independent variables. The most common types are:
  - **One-way ANOVA**: This type of ANOVA has one independent variable with two or more levels (groups). For example, testing the effect of social media use (low, medium, high) on sleep hours.
  - **Two-way ANOVA**: This type of ANOVA has two independent variables, each with two or more levels. For example, testing the effect of seed type and fertilizer type on crop yield.
  - **Repeated measures ANOVA**: This type of ANOVA has one independent variable with two or more levels, but the same subjects are measured in each level. For example, testing the effect of time (before, during, after) on stress level of students.
- ANOVA uses the **F-test** to compare the variance between groups and the variance within groups. The F-test is based on the ratio of two estimates of variance: the **mean square between groups (MSB)** and the **mean square within groups (MSW)**  .
- The formula for the F-test is:

  ```
  F = MSB / MSW
  ```

- The null hypothesis of ANOVA is that the means of all groups are equal, or there is no effect of the independent variable(s) on the dependent variable. The alternative hypothesis is that at least one group mean is different from the others, or there is an effect of the independent variable(s) on the dependent variable  .
- To perform an ANOVA, the following steps are required:
  - Calculate the **sum of squares between groups (SSB)**, which measures the variation due to the differences between group means.
  - Calculate the **sum of squares within groups (SSW)**, which measures the variation due to the differences within each group.
  - Calculate the **degrees of freedom between groups (dfB)**, which is the number of groups minus one.
  - Calculate the **degrees of freedom within groups (dfW)**, which is the total number of observations minus the number of groups.
  - Calculate the **mean square between groups (MSB)**, which is the SSB divided by the dfB.
  - Calculate the **mean square within groups (MSW)**, which is the SSW divided by the dfW.
  - Calculate the **F-statistic**, which is the MSB divided by the MSW.
  - Compare the **F-statistic** with the **critical value** from the F-distribution table, based on the dfB and dfW, and the chosen level of significance (usually 0.05).
  - If the F-statistic is greater than the critical value, reject the null hypothesis and conclude that there is a significant difference between the group means. If the F-statistic is less than or equal to the critical value, fail to reject the null hypothesis and conclude that there is no significant difference between the group means  .
- ANOVA can be performed using various software tools, such as SPSS, Excel, R, etc. The output of ANOVA usually includes a table that summarizes the sources of variation, the degrees of freedom, the sum of squares, the mean squares, the F-statistic, and the p-value  .
- ANOVA has some assumptions that need to be checked before applying the test, such as:
  - The dependent variable is continuous and normally distributed in each group.
  - The independent variable(s) are categorical and independent of each other.
  - The groups have equal variances, or homogeneity of variance.
  - The observations are independent and randomly sampled from the population  .
- ANOVA can be extended or modified to suit different situations, such as:
  - **Post-hoc tests**: