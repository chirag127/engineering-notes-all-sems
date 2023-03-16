Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Test of Independence for the notes of the Unit 2 - Inferential Statistics in the subject of Mathematical Foundation AI, ML and Data Science.

### Test of Independence

- A test of independence is a statistical procedure that determines whether two categorical variables are independent of each other or not.
- Independence means that the occurrence of one variable does not affect the probability of occurrence of the other variable.
- A test of independence is based on a contingency table, which shows the frequency distribution of the variables across different categories.
- A test of independence uses the chi-square statistic to measure the discrepancy between the observed frequencies and the expected frequencies under the assumption of independence.
- The null hypothesis of a test of independence is that the two variables are independent, and the alternative hypothesis is that they are dependent or associated.
- The test of independence can be performed using the following steps:

  1. Construct a contingency table with the observed frequencies of the variables across the categories.
  2. Calculate the expected frequencies for each cell of the table using the formula: E = (row total * column total) / grand total
  3. Calculate the chi-square statistic using the formula: X^2 = sum of [(O - E)^2 / E] for all cells, where O is the observed frequency and E is the expected frequency.
  4. Find the degrees of freedom using the formula: df = (number of rows - 1) * (number of columns - 1)
  5. Find the p-value by comparing the chi-square statistic and the degrees of freedom with the chi-square distribution table or using a calculator or software.
  6. Draw a conclusion based on the p-value and a significance level. If the p-value is less than or equal to the significance level, reject the null hypothesis and conclude that the variables are dependent. If the p-value is greater than the significance level, fail to reject the null hypothesis and conclude that the variables are independent.

- An example of a test of independence is to determine whether gender and smoking status are independent or not based on the following contingency table:

| Gender | Smoker | Non-smoker | Total |
|--------|--------|------------|-------|
| Male   | 120    | 80         | 200   |
| Female | 90     | 110        | 200   |
| Total  | 210    | 190        | 400   |

- The expected frequencies for each cell are calculated as follows:

| Gender | Smoker | Non-smoker | Total |
|--------|--------|------------|-------|
| Male   | 105    | 95         | 200   |
| Female | 105    | 95         | 200   |
| Total  | 210    | 190        | 400   |

- The chi-square statistic is calculated as follows:

X^2 = [(120 - 105)^2 / 105] + [(80 - 95)^2 / 95] + [(90 - 105)^2 / 105] + [(110 - 95)^2 / 95]
X^2 = 3.81

- The degrees of freedom are calculated as follows:

df = (2 - 1) * (2 - 1)
df = 1

- The p-value can be found using a chi-square distribution table or a calculator or software. For example, using a calculator, the p-value is 0.051.
- Using a significance level of 0.05, the conclusion is that the p-value is greater than the significance level, so we fail to reject the null hypothesis and conclude that gender and smoking status are independent.