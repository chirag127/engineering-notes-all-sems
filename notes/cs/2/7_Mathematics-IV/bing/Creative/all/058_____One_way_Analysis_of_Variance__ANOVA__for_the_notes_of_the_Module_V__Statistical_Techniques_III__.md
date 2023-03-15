# One way Analysis of Variance (ANOVA)

- One way ANOVA is a statistical technique that can be used to compare whether two or more sample means are significantly different or not (using the F distribution) .
- One way ANOVA is a parametric test that assumes that the data are normally distributed and have equal variances .
- One way ANOVA is also known as single factor ANOVA or one factor ANOVA .
- One way ANOVA has one independent variable (also called factor or treatment) that has two or more levels (also called groups or categories)  .
- One way ANOVA has one dependent variable (also called response or outcome) that is continuous and numerical  .
- One way ANOVA tests the null hypothesis that the population means of all groups are equal against the alternative hypothesis that at least one population mean is different   .
- One way ANOVA calculates the F statistic, which is the ratio of the between-group variance to the within-group variance   .
- One way ANOVA compares the F statistic to the critical value from the F distribution with appropriate degrees of freedom to determine the p-value   .
- One way ANOVA rejects the null hypothesis if the p-value is less than the significance level (usually 0.05), which means that there is a statistically significant difference between the group means   .
- One way ANOVA can be performed using various software tools, such as SPSS, Excel, R, etc.   .
- One way ANOVA can be followed by post-hoc tests, such as Tukey's HSD, to identify which pairs of groups have significant mean differences   .

## Example of One way ANOVA

Suppose we want to compare the mean scores of three groups of students who received different teaching methods: A, B, and C. The data are shown below:

| Group | Score |
|-------|-------|
| A     | 75    |
| A     | 80    |
| A     | 85    |
| A     | 90    |
| A     | 95    |
| B     | 70    |
| B     | 75    |
| B     | 80    |
| B     | 85    |
| B     | 90    |
| C     | 65    |
| C     | 70    |
| C     | 75    |
| C     | 80    |
| C     | 85    |

The steps to perform a one way ANOVA are:

1. State the null and alternative hypotheses:

   H0: μA = μB = μC (the population means of all groups are equal)

   HA: not H0 (at least one population mean is different)

2. Calculate the degrees of freedom:

   df1 = k - 1 = 3 - 1 = 2 (between-group degrees of freedom)

   df2 = N - k = 15 - 3 = 12 (within-group degrees of freedom)

   where k is the number of groups and N is the total number of observations.

3. Calculate the sum of squares:

   SST = SSB + SSW (total sum of squares)

   SSB = Σnᵢ(ȳᵢ - ȳ)² (between-group sum of squares)

   SSW = ΣΣ(yᵢⱼ - ȳᵢ)² (within-group sum of squares)

   where nᵢ is the sample size of group i, ȳᵢ is the sample mean of group i, ȳ is the grand mean of all observations, and yᵢⱼ is the jth observation in group i.

   Using the data, we can calculate:

   SST = 750