# Chi-square Test

- Chi-square test is a **non-parametric** test that does not assume any specific distribution of the data, but only that the data follows a **chi-square distribution**.
- Chi-square test is used to test **hypotheses** about the relationship between **categorical variables** (such as gender, race, occupation, etc.) in a **contingency table**.
- Chi-square test can be used for different purposes, such as:
  - **Goodness of fit test**: to check if the observed frequencies of a categorical variable match the expected frequencies based on a theoretical or empirical distribution.
  - **Test of independence**: to check if two categorical variables are independent of each other, or if there is an association between them.
  - **Test of homogeneity**: to check if the distribution of a categorical variable is the same across different groups or populations.
  - **Test of population variance**: to check if the variance of a numerical variable is equal to a given value.
- Chi-square test uses the following formula to calculate the **test statistic** :

  ![chi-square formula](https://latex.codecogs.com/png.latex?%5Cchi%5E2%20%3D%20%5Csum_%7Bi%3D1%7D%5E%7Bk%7D%20%5Cfrac%7B%28O_i%20-%20E_i%29%5E2%7D%7BE_i%7D)

  Where:
  - ![O_i](https://latex.codecogs.com/png.latex?O_i) is the **observed frequency** of the i-th category or cell
  - ![E_i](https://latex.codecogs.com/png.latex?E_i) is the **expected frequency** of the i-th category or cell, based on the null hypothesis
  - ![k](https://latex.codecogs.com/png.latex?k) is the **number of categories or cells** in the contingency table
- Chi-square test compares the **test statistic** with a **critical value** from the **chi-square distribution** with a given **degrees of freedom** and **significance level**.
- Chi-square test rejects the **null hypothesis** if the **test statistic** is greater than the **critical value**, meaning that there is a **significant difference** between the observed and expected frequencies, or that the variables are **not independent** or **not homogeneous**.
- Chi-square test has some **assumptions** and **limitations**, such as:
  - The data should be **randomly sampled** and **independent**.
  - The expected frequencies should be **large enough** (usually at least 5) to avoid errors in the approximation of the chi-square distribution.
  - The test is **sensitive** to the **sample size** and the **number of categories or cells**, which can affect the power and accuracy of the test.
  - The test does **not** provide information about the **direction** or the **strength** of the relationship between the variables.