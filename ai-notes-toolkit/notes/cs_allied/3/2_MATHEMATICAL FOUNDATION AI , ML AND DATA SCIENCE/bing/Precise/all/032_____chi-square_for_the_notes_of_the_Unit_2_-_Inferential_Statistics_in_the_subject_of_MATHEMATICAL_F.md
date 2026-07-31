# Chi-Square

Chi-square is a statistical test commonly used to determine if there is a significant association between two categorical variables. It is a non-parametric test, meaning that it does not assume any particular distribution for the data.

The chi-square test is based on a contingency table, which displays the frequency distribution of the data across the different categories of the two variables. The test calculates the expected frequencies for each cell of the table, based on the assumption of independence between the two variables. The chi-square statistic is then calculated as the sum of the squared differences between the observed and expected frequencies, divided by the expected frequencies.

The resulting chi-square statistic follows a chi-square distribution with degrees of freedom equal to (number of rows - 1) * (number of columns - 1). The p-value for the test is calculated by comparing the chi-square statistic to the chi-square distribution. A small p-value indicates that the observed data is unlikely to have occurred by chance, and therefore suggests that there is a significant association between the two variables.

In summary, the steps for conducting a chi-square test are as follows:
1. Create a contingency table displaying the frequency distribution of the data across the different categories of the two variables.
2. Calculate the expected frequencies for each cell of the table, based on the assumption of independence between the two variables.
3. Calculate the chi-square statistic as the sum of the squared differences between the observed and expected frequencies, divided by the expected frequencies.
4. Determine the degrees of freedom for the test as (number of rows - 1) * (number of columns - 1).
5. Calculate the p-value by comparing the chi-square statistic to the chi-square distribution with the appropriate degrees of freedom.
6. Interpret the p-value to determine if there is a significant association between the two variables.
