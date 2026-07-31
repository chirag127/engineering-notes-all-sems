### Test of Independence

- A test of independence is a statistical procedure that determines whether two categorical variables are independent or related.
- The null hypothesis of the test is that the variables are independent, meaning that there is no association between them.
- The alternative hypothesis is that the variables are dependent, meaning that there is some association between them.
- The test of independence is based on the chi-square statistic, which measures the discrepancy between the observed frequencies and the expected frequencies under the null hypothesis.
- The expected frequency for each cell of a contingency table is calculated as:

$$E_{ij} = \frac{R_i C_j}{n}$$

where $E_{ij}$ is the expected frequency for the $i$th row and $j$th column, $R_i$ is the total frequency for the $i$th row, $C_j$ is the total frequency for the $j$th column, and $n$ is the total sample size.

- The chi-square statistic is then calculated as:

$$\chi^2 = \sum_{i=1}^r \sum_{j=1}^c \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$

where $O_{ij}$ is the observed frequency for the $i$th row and $j$th column, $r$ is the number of rows, and $c$ is the number of columns.

- The chi-square statistic follows a chi-square distribution with $(r-1)(c-1)$ degrees of freedom under the null hypothesis.
- The p-value of the test is the probability of obtaining a chi-square statistic as large or larger than the observed one, assuming that the null hypothesis is true.
- The test of independence is also known as the chi-square test of independence or the chi-square test of association.