 Here is the content in markdown format for the topic ## Unit 2 - REGRESSION:

## Unit 2 - REGRESSION

### Linear Regression
- Linear regression is a basic and commonly used type of predictive analysis.
- It is used to predict a quantitative outcome variable (y) based on the value of a predictor variable (x).
- The relationship between the variables is represented by a straight line (y=mx+c) known as the regression line.
- The goal is to minimize the distance between the observed data points and the regression line (residual sum of squares).
- Steps involved:
	1. Plot the data and observe the pattern (if linear)
	2. Calculate the regression line:
	- Mean of x and y
	- Calculate m (slope):covariance(x,y)/variance(x)
	- Calculate c (intercept): mean(y)-m*mean(x)
	3. Evaluate the model:
	- R-squared: Proportion of variance explained by the model
	- p-value: Statistical significance of the model
	- Standard error: Error in the slope estimate

**Advantages:** Simple to understand and implement. Can handle linear relationships.
**Disadvantages:** Cannot handle non-linear relationships. Sensitive to outliers.
**Applications:** Predicting housing prices, stock prices, etc.

[Detailed diagrams and codes can be included here if required]