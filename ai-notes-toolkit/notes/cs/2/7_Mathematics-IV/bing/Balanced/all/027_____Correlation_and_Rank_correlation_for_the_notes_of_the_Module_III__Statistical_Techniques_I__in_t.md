# Correlation and Rank Correlation

- Correlation is a statistical technique that measures the degree and direction of the linear relationship between two variables. It is denoted by the symbol r and ranges from -1 to 1. A correlation of -1 indicates a perfect negative linear relationship, a correlation of 1 indicates a perfect positive linear relationship, and a correlation of 0 indicates no linear relationship.   
- The most common method of calculating correlation is the Pearson correlation coefficient, which is given by the formula:

r = (nΣxy - ΣxΣy) / √[(nΣx^2 - (Σx)^2)(nΣy^2 - (Σy)^2)]

where n is the number of observations, x and y are the values of the two variables, and Σ means the sum of.  

- Rank correlation is a special type of correlation that measures the ordinal association between two ranked variables. It is useful when the data are not continuous or not normally distributed. It is denoted by the symbol ρ (rho) and also ranges from -1 to 1. A rank correlation of -1 indicates a perfect negative monotonic relationship, a rank correlation of 1 indicates a perfect positive monotonic relationship, and a rank correlation of 0 indicates no monotonic relationship.  
- The most common method of calculating rank correlation is the Spearman's rank correlation coefficient, which is given by the formula:

ρ = 1 - (6Σd^2) / (n(n^2 - 1))

where n is the number of observations, d is the difference between the ranks of the two variables, and Σ means the sum of.   

- Correlation and rank correlation are both useful tools for exploring the relationship between two variables, but they have different assumptions and interpretations. Correlation assumes that the variables are linearly related and have a normal distribution, while rank correlation does not. Correlation measures the strength and direction of the linear relationship, while rank correlation measures the strength and direction of the monotonic relationship.