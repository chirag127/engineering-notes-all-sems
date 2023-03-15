# Chi-square test

- A chi-square test is a statistical hypothesis test used to analyze the relationship between two categorical variables.
- A categorical variable is one that can take only a limited number of values, such as gender, blood type, or eye color.
- A chi-square test compares the observed frequencies of the values of the categorical variables with the expected frequencies under the null hypothesis of independence.
- The null hypothesis of independence states that there is no association between the two categorical variables, and that the observed frequencies are due to chance.
- The alternative hypothesis states that there is some association between the two categorical variables, and that the observed frequencies are not due to chance.
- The test statistic for a chi-square test is calculated as:

$$\chi^2 = \sum_{i=1}^{r} \sum_{j=1}^{c} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$

- Where $O_{ij}$ is the observed frequency of the $i$th row and $j$th column of the contingency table, $E_{ij}$ is the expected frequency of the $i$th row and $j$th column of the contingency table, $r$ is the number of rows, and $c$ is the number of columns.
- The expected frequency of each cell is calculated as:

$$E_{ij} = \frac{R_i C_j}{N}$$

- Where $R_i$ is the total frequency of the $i$th row, $C_j$ is the total frequency of the $j$th column, and $N$ is the total frequency of the entire table.
- The test statistic follows a chi-square distribution with $(r-1)(c-1)$ degrees of freedom, where $r$ and $c$ are the number of rows and columns of the contingency table, respectively.
- The p-value of the test is the probability of obtaining a test statistic as extreme or more extreme than the observed one, under the null hypothesis of independence.
- The p-value can be obtained from a chi-square distribution table or a calculator.
- The test is usually performed at a significance level of 0.05, which means that the null hypothesis is rejected if the p-value is less than 0.05, and accepted otherwise.
- A chi-square test can be used to test various hypotheses, such as:

  - Whether two variables are independent or dependent
  - Whether the distribution of a variable is uniform or not
  - Whether the observed frequencies of a variable match the expected frequencies of a theoretical model
  - Whether there is a difference between the proportions of two or more groups