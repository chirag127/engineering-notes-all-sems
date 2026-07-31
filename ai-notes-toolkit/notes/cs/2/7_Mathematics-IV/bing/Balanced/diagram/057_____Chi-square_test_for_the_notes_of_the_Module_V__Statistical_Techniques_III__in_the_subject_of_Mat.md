### Chi-square test

A chi-square test is a statistical method that compares the observed frequencies of categorical data with the expected frequencies under a null hypothesis. The null hypothesis is usually that the observed frequencies are equal to the expected frequencies, or that the observed frequencies are independent of each other. The chi-square test can be used to test various hypotheses, such as:

- Whether a coin is fair or biased
- Whether a die is loaded or fair
- Whether a genetic trait follows a Mendelian ratio
- Whether two variables are associated or independent

The chi-square test statistic is calculated as:

$$\chi^2 = \sum \frac{(O - E)^2}{E}$$

where O is the observed frequency, E is the expected frequency, and the sum is over all the categories of data.

The chi-square test statistic follows a chi-square distribution with k - 1 degrees of freedom, where k is the number of categories of data. The chi-square distribution is a family of distributions that depends on the degrees of freedom parameter. It is a right-skewed distribution that ranges from 0 to infinity. The shape of the chi-square distribution changes as the degrees of freedom increases. Here is an example of chi-square distributions with different degrees of freedom:

![Chi-square distributions](https://www.scribbr.com/wp-content/uploads/2020/10/chi-square-distributions.png)

To perform a chi-square test, we need to compare the chi-square test statistic with a critical value from the chi-square distribution. The critical value depends on the significance level (α) and the degrees of freedom (k - 1) of the test. The significance level is the probability of rejecting the null hypothesis when it is true. A common choice for the significance level is 0.05, which means that there is a 5% chance of making a type I error (rejecting the null hypothesis when it is true).

The critical value can be found from a chi-square table or a calculator. The critical value is the value of the chi-square distribution that corresponds to the upper tail area of α. For example, if α = 0.05 and k - 1 = 3, the critical value is 7.815, which means that 5% of the area under the chi-square distribution with 3 degrees of freedom is above 7.815.

The chi-square test can be performed as follows:

- State the null and alternative hypotheses
- Calculate the expected frequencies under the null hypothesis
- Calculate the chi-square test statistic using the formula
- Find the critical value from the chi-square table or calculator
- Compare the test statistic with the critical value and make a decision

If the test statistic is greater than the critical value, we reject the null hypothesis and conclude that there is a significant difference or association between the observed and expected frequencies. If the test statistic is less than or equal to the critical value, we fail to reject the null hypothesis and conclude that there is no significant difference or association between the observed and expected frequencies.

Here is an example of a chi-square test:

Suppose we want to test whether a die is fair or loaded. We roll the die 60 times and record the number of times each face appears. The observed frequencies are:

| Face | 1 | 2 | 3 | 4 | 5 | 6 |
|------|---|---|---|---|---|---|
| Frequency | 8 | 9 | 11 | 12 | 10 | 10 |

The null hypothesis is that the die is fair, which means that the probability of each face is 1/6. The alternative hypothesis is that the die is loaded, which means that the probability of each face is not 1/6. The expected frequencies under the null hypothesis are:

| Face | 1 | 2 | 3 | 4 | 5 | 6 |
|------|---|---|---|---|---|---|
| Frequency | 10 | 10 | 10 | 10 | 10 | 10 |

The chi-square test statistic is:

$$\chi^2 = \sum \frac{(O - E)^2}{E} = \frac{(8 - 10)^2}{10} + \frac{(9 - 10)^2}{10} + \frac{(11 - 10)^2}{10} + \frac{(12 - 10)^2}{10} + \frac{(10 - 10)^2}{10} + \frac{(10 - 10)^2}{10} = 1.6$$