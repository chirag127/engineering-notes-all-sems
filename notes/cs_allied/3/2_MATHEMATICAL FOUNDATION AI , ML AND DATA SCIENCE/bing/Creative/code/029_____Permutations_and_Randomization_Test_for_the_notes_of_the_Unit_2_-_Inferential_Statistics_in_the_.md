Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes on permutations and randomization test for the unit 2 of inferential statistics.

### Permutations and Randomization Test

- Permutations and randomization tests are two types of nonparametric tests that can be used to compare two or more samples without making any assumptions about the underlying population distribution.
- Permutations and randomization tests are based on the idea of shuffling or rearranging the data in some way to create different possible scenarios under the null hypothesis, and then comparing the observed test statistic to the distribution of the test statistics from the shuffled data.
- Permutations and randomization tests are also called exact tests, because they do not rely on any approximation or asymptotic results, and they can provide the exact p-value for any sample size and any test statistic.
- Permutations and randomization tests have some advantages over parametric tests, such as being more robust to outliers, violations of normality, and heterogeneity of variances. They can also be applied to a wider range of data types and situations, such as ordinal, categorical, or non-independent data.
- Permutations and randomization tests have some disadvantages, such as being computationally intensive, especially for large sample sizes or complex test statistics. They may also be less powerful than parametric tests when the parametric assumptions are met or nearly met.

#### Permutation Test

- A permutation test is a type of randomization test that is based on random sampling from the data. It assumes that the data is sampled randomly from an underlying population distribution, and that the null hypothesis is that all samples come from the same population.
- A permutation test involves the following steps:
  - Compute the test statistic of interest using the original data, such as the difference in means, the correlation coefficient, or the chi-square statistic.
  - Shuffle or permute the data in all possible ways, or in a large number of random ways, keeping the sample sizes fixed. For each permutation, compute the same test statistic as in step 1.
  - Compare the observed test statistic to the distribution of the test statistics from the permutations. The p-value is the proportion of permutations that have a test statistic as extreme or more extreme than the observed one, in the direction of the alternative hypothesis.
  - If the p-value is less than or equal to the significance level, reject the null hypothesis. Otherwise, fail to reject the null hypothesis.

#### Randomization Test

- A randomization test is a type of permutation test that is based on random assignment of the data. It assumes that the data is obtained from an experiment or a quasi-experiment, where the treatment or group assignment is randomized or can be considered as random.
- A randomization test involves the following steps:
  - Compute the test statistic of interest using the original data, such as the difference in means, the correlation coefficient, or the chi-square statistic.
  - Shuffle or randomize the group labels or the treatment assignment, keeping the sample sizes fixed. For each randomization, compute the same test statistic as in step 1.
  - Compare the observed test statistic to the distribution of the test statistics from the randomizations. The p-value is the proportion of randomizations that have a test statistic as extreme or more extreme than the observed one, in the direction of the alternative hypothesis.
  - If the p-value is less than or equal to the significance level, reject the null hypothesis. Otherwise, fail to reject the null hypothesis.

#### Example

- Suppose we want to compare the mean scores of two groups of students on a math test, where group A received a new teaching method and group B received the standard method. The data is shown below:

| Group | Score |
|-------|-------|
| A     | 85    |
| A     | 90    |
| A     | 95    |
| A     | 80    |
| A     | 88    |
| B     | 75    |
| B     | 70    |
| B     | 82    |
| B     | 78    |
| B     | 76    |

- We can use a permutation test or a randomization test to test the null hypothesis that the mean scores of the two groups are equal, versus the alternative hypothesis that the mean score of group A is higher than that of group B.
- The test statistic of interest is the difference in means between the two groups. Using the original data, we can calculate the observed test statistic as:

```python
# Import numpy library
import numpy as np

# Define the data
group_A