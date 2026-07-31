### Chi-square test

- A chi-square test is a statistical method that compares the observed frequencies of categorical data with the expected frequencies under a null hypothesis.
- A chi-square test can be used to test various hypotheses, such as the independence of two variables, the goodness of fit of a model, or the homogeneity of a population.
- A chi-square test statistic is calculated by summing the squared differences between the observed and expected frequencies, divided by the expected frequencies .
- The formula for the chi-square test statistic is:

$$\chi^2 = \sum \frac{(O - E)^2}{E}$$

where O is the observed frequency, E is the expected frequency, and the sum is over all categories.

- The chi-square test statistic follows a chi-square distribution with a certain number of degrees of freedom, which depends on the type of test and the number of categories .
- The chi-square distribution is a family of distributions that are skewed to the right and have a minimum value of zero.
- The degrees of freedom of a chi-square distribution are equal to the number of categories minus the number of parameters estimated under the null hypothesis.
- The p-value of a chi-square test is the probability of obtaining a chi-square test statistic as extreme or more extreme than the observed one, assuming the null hypothesis is true .
- The p-value can be calculated using a chi-square distribution table or a statistical software .
- The p-value is compared with a significance level, usually 0.05, to decide whether to reject or fail to reject the null hypothesis .
- A small p-value (less than the significance level) indicates that the observed frequencies are unlikely to occur under the null hypothesis, and thus there is evidence to reject the null hypothesis .
- A large p-value (greater than or equal to the significance level) indicates that the observed frequencies are compatible with the null hypothesis, and thus there is no evidence to reject the null hypothesis .

- Examples of chi-square tests are:

  - Pearson's chi-square test of independence: This test examines whether two categorical variables are independent or associated . For example, this test can be used to test whether the proportion of people who are left-handed is the same for Americans and Canadians.
  - Chi-square goodness of fit test: This test examines whether the observed frequencies of a categorical variable follow a specified distribution or model . For example, this test can be used to test whether the results of tossing a fair coin follow a binomial distribution with equal probabilities of heads and tails.
  - Chi-square test of homogeneity: This test examines whether the proportions of a categorical variable are the same across different populations or groups . For example, this test can be used to test whether the blood types of people from different regions are homogeneous.
  - Chi-square test of variance: This test examines whether the variance of a normally distributed population has a given value based on a sample variance. For example, this test can be used to test whether the variance of the heights of students in a class is equal to 10 cm^2^.