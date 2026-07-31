# Correlation and Rank Correlation

- Correlation is a statistical technique that measures the degree and direction of the linear relationship between two variables. It is denoted by the symbol r and ranges from -1 to 1. A correlation of -1 indicates a perfect negative linear relationship, a correlation of 1 indicates a perfect positive linear relationship, and a correlation of 0 indicates no linear relationship.   
- The most common method of calculating correlation is the Pearson correlation coefficient, which is based on the actual values of the variables. The formula for Pearson correlation coefficient is:

r = (nΣxy - ΣxΣy) / √[(nΣx^2 - (Σx)^2)(nΣy^2 - (Σy)^2)]

where n is the number of observations, x and y are the values of the two variables, and Σ means the sum of.  

- However, sometimes the actual values of the variables are not available or meaningful, and we only have the ranks of the observations. For example, if we want to study the preference or satisfaction of customers, we may use a rating scale or a questionnaire that assigns ranks to the responses. In such cases, we can use rank correlation to measure the relationship between the ranks of the two variables.  
- The most common method of calculating rank correlation is the Spearman's rank correlation coefficient, which is based on the difference between the ranks of the two variables. The formula for Spearman's rank correlation coefficient is:

ρ = 1 - (6Σd^2) / (n(n^2 - 1))

where ρ is the rank correlation coefficient, d is the difference between the ranks of the two variables for each observation, and n is the number of observations.   

- Rank correlation is useful when the variables are not normally distributed, have outliers, or are measured on an ordinal scale. Rank correlation is also more robust to non-linear relationships than Pearson correlation. However, rank correlation does not capture the magnitude of the relationship, only the direction and monotonicity.