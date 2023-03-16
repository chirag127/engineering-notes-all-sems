Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of Test of Independence for the Unit 2 - Inferential Statistics in the subject of Mathematical Foundation AI, ML and Data Science.

### Test of Independence

- A test of independence is a statistical procedure that determines whether two categorical variables are independent of each other or not.
- Independence means that the occurrence of one event does not affect the probability of another event.
- For example, if we want to test whether gender and political preference are independent, we can use a test of independence to see if the proportion of males and females who prefer a certain party is the same or not.
- A test of independence is based on a contingency table, which is a table that shows the frequency distribution of the two variables across all possible categories.
- For example, the following table shows the gender and political preference of 100 randomly selected voters.

| Gender | Democrat | Republican | Independent | Total |
|--------|----------|------------|-------------|-------|
| Male   | 15       | 25         | 10          | 50    |
| Female | 20       | 15         | 15          | 50    |
| Total  | 35       | 40         | 25          | 100   |

- A test of independence uses the chi-square statistic, which measures the discrepancy between the observed frequencies and the expected frequencies under the assumption of independence.
- The expected frequency for each cell is calculated by multiplying the row total and the column total and dividing by the grand total.
- For example, the expected frequency for the cell (Male, Democrat) is (50 x 35) / 100 = 17.5
- The chi-square statistic is then computed by summing up the squared differences between the observed and expected frequencies, divided by the expected frequencies, for all cells.
- For example, the chi-square statistic for the above table is

![chi-square formula](https://latex.codecogs.com/png.latex?%5Cchi%5E2%20%3D%20%5Csum_%7Bi%2Cj%7D%20%5Cfrac%7B%28O_%7Bi%2Cj%7D%20-%20E_%7Bi%2Cj%7D%29%5E2%7D%7BE_%7Bi%2Cj%7D%7D%20%3D%20%5Cfrac%7B%2815%20-%2017.5%29%5E2%7D%7B17.5%7D%20&plus;%20%5Cfrac%7B%2825%20-%2020%29%5E2%7D%7B20%7D%20&plus;%20%5Cfrac%7B%2810%20-%2012.5%29%5E2%7D%7B12.5%7D%20&plus;%20%5Cfrac%7B%2820%20-%2017.5%29%5E2%7D%7B17.5%7D%20&plus;%20%5Cfrac%7B%2815%20-%2020%29%5E2%7D%7B20%7D%20&plus;%20%5Cfrac%7B%2815%20-%2012.5%29%5E2%7D%7B12.5%7D%20%3D%203.6)

- The chi-square statistic follows a chi-square distribution with a certain degree of freedom, which depends on the number of rows and columns in the contingency table.
- The degree of freedom is calculated by multiplying the number of rows minus one and the number of columns minus one.
- For example, the degree of freedom for the above table is (2 - 1) x (3 - 1) = 2
- The p-value of the test is the probability of obtaining a chi-square statistic as large as or larger than the observed one, under the null hypothesis of independence.
- The p-value can be obtained by using a chi-square table or a calculator.
- For example, the p-value for the above table is 0.166, which means that there is a 16.6% chance of getting a chi-square statistic of 3.6 or more, if gender and political preference are independent.
- The test of independence is a two-tailed test, which means that we reject the null hypothesis of independence if the p-value is less than or equal to the