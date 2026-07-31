 Here are the notes on Goodness of fit for the Unit 2 - Inferential Statistics in the subject of MATHEMATICAL FOUNDATION AI , ML AND DATA SCIENCE:

### Goodness of fit

- Goodness of fit tests are used to assess whether a sample comes from a population with a specific distribution.
- They are used to compare the observed frequencies with expected frequencies.
- The null hypothesis is that the data comes from the assumed distribution. The alternative hypothesis is that the data does not come from the assumed distribution.
- If the p-value from the goodness of fit test is less than the significance level, we reject the null hypothesis and conclude that the data does not come from the assumed distribution. Otherwise, we fail to reject the null hypothesis.
- Some common goodness of fit tests are:
    - Chi-square test: Used for categorical data
    - Kolmogorov-Smirnov test: Used for continuous data
    - Anderson-Darling test: Also used for continuous data

- The tests are applied as follows:
    - State the null and alternative hypotheses
    - Compute the test statistic (chi-square value, KS statistic, AD statistic, etc.)
    - Determine the p-value
    - Compare the p-value to the significance level and draw conclusions

- Some key points:
    - The sample size should be large for the goodness of fit tests to be reliable
    - The expected frequencies must be greater than 5 for the chi-square test to be reliable
    - The distributions being tested should be continuous for KS and AD tests

- The goodness of fit tests are useful to determine if a model is appropriate for a set of data or if a distribution fits the data. They help in statistical modeling and inference.