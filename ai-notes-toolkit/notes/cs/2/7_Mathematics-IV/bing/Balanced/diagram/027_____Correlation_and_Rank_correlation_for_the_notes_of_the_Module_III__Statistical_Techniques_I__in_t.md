### Correlation and Rank Correlation

- Correlation is a statistical technique that measures the degree and direction of the linear relationship between two variables. It is denoted by the symbol r and ranges from -1 to 1. A correlation of -1 indicates a perfect negative linear relationship, a correlation of 0 indicates no linear relationship, and a correlation of 1 indicates a perfect positive linear relationship.   
- The most common method of calculating correlation is the Pearson correlation coefficient, which is based on the actual values of the variables. However, sometimes the variables are not measured on an interval or ratio scale, but on an ordinal scale, where the values are ranked according to some criterion. In such cases, the Pearson correlation coefficient is not appropriate, and we need to use a rank correlation coefficient.  
- Rank correlation is a measure of the relationship between the rankings of two variables or two rankings of the same variable. It assesses the degree of monotonicity of the relationship, that is, whether the rankings tend to increase or decrease together. Rank correlation is also less sensitive to outliers and non-normal distributions than Pearson correlation.  
- The most common method of calculating rank correlation is the Spearman's rank correlation coefficient, denoted by the symbol rho. It is based on the differences between the ranks of the two variables for each observation. The formula for Spearman's rho is:

![Spearman's rho formula](https://www.embibe.com/exams/wp-content/uploads/sites/2/2021/01/Spearmans-Rank-Correlation-Coefficient-Formula.png)

where d is the difference between the two ranks for each observation and N is the total number of observations.  
- Spearman's rho also ranges from -1 to 1, with the same interpretation as Pearson's r. A rho of -1 indicates a perfect negative monotonic relationship, a rho of 0 indicates no monotonic relationship, and a rho of 1 indicates a perfect positive monotonic relationship. 
- To calculate Spearman's rho, we need to follow these steps:

  - Assign ranks to each value of the two variables, with the lowest value getting rank 1 and the highest value getting rank N. If there are ties, assign the average rank to the tied values.
  - Calculate the difference between the ranks of each observation, and square the differences.
  - Sum up the squared differences, and plug the values into the formula.
  - Interpret the result based on the magnitude and sign of rho.  

- Here is an example of calculating Spearman's rho for a dataset of 10 students' scores on two tests:

| Student | Test 1 | Test 2 |
| ------- | ------ | ------ |
| A       | 75     | 85     |
| B       | 60     | 70     |
| C       | 90     | 95     |
| D       | 80     | 75     |
| E       | 70     | 80     |
| F       | 65     | 60     |
| G       | 85     | 90     |
| H       | 55     | 65     |
| I       | 95     | 100    |
| J       | 50     | 55     |

- The ranks for each variable are:

| Student | Test 1 | Rank 1 | Test 2 | Rank 2 | d    | d^2   |
| ------- | ------ | ------ | ------ | ------ | ---- | ----- |
| A       | 75     | 6      | 85     | 6      | 0    | 0     |
| B       | 60     | 4      | 70     | 4      | 0    | 0     |
| C       | 90     | 9      | 95     | 9      | 0    | 0     |
| D       | 80     | 7      | 75     | 5      | 2    | 4     |
| E       | 70     | 5      | 80     | 7      | -2   | 4     |
| F       | 65     | 3      | 60     | 3      | 0    | 0     |
| G