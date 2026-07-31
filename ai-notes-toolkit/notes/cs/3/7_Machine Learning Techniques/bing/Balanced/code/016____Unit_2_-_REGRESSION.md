## Unit 2 - REGRESSION

Regression is a statistical method that allows us to examine the relationship between one or more explanatory variables (also called independent variables or predictors) and a response variable (also called dependent variable or outcome).

Some examples of regression problems are:

- Predicting the price of a house based on its size, location, and features.
- Estimating the effect of advertising expenditure on sales revenue.
- Analyzing the impact of air pollution on life expectancy.

There are different types of regression models depending on the nature and number of explanatory variables and the distribution of the response variable. Some of the most common regression models are:

- Linear regression: A linear regression model assumes that the relationship between the explanatory variables and the response variable is linear, that is, the response variable can be expressed as a weighted sum of the explanatory variables plus an error term. The error term represents the random variation that is not explained by the model. Linear regression can be used for continuous or categorical response variables, but the latter requires some transformation or encoding of the response variable.
- Logistic regression: A logistic regression model is used when the response variable is binary, that is, it can only take two possible values, such as 0 or 1, yes or no, success or failure, etc. A logistic regression model estimates the probability of the response variable being 1 given the values of the explanatory variables. It does so by applying a logistic function (also called a sigmoid function) to the linear combination of the explanatory variables. The logistic function maps any real number to a value between 0 and 1, which can be interpreted as a probability.
- Multiple regression: A multiple regression model is a generalization of the linear or logistic regression model that allows for more than one explanatory variable. The model can be written as:

  - For linear regression: y = b0 + b1x1 + b2x2 + ... + bnxn + e
  - For logistic regression: p(y=1) = 1 / (1 + exp(-(b0 + b1x1 + b2x2 + ... + bnxn)))

  where y is the response variable, x1, x2, ..., xn are the explanatory variables, b0, b1, b2, ..., bn are the coefficients or parameters of the model, e is the error term, and p(y=1) is the probability of the response variable being 1.

- Polynomial regression: A polynomial regression model is a special case of multiple regression that allows for nonlinear relationships between the explanatory variables and the response variable. It does so by adding higher-order terms of the explanatory variables to the model, such as x^2, x^3, x^4, etc. For example, a quadratic polynomial regression model can be written as:

  - For linear regression: y = b0 + b1x + b2x^2 + e
  - For logistic regression: p(y=1) = 1 / (1 + exp(-(b0 + b1x + b2x^2)))

  where x is the explanatory variable, y is the response variable, and the other terms are as defined before.

- Ridge regression: A ridge regression model is a modification of the linear or logistic regression model that introduces a regularization term to the model. Regularization is a technique that helps to prevent overfitting, which is a situation where the model performs well on the training data but poorly on new or unseen data. Overfitting can occur when the model is too complex or has too many parameters compared to the amount of data available. Regularization reduces the complexity or the magnitude of the parameters by adding a penalty term to the model. The penalty term is proportional to the sum of the squared values of the parameters, hence the name ridge regression. The model can be written as:

  - For linear regression: y = b0 + b1x1 + b2x2 + ... + bnxn + e + lambda * (b1^2 + b2^2 + ... + bn^2)
  - For logistic regression: p(y=1) = 1 / (1 + exp(-(b0 + b1x1 + b2x2 + ... + bnxn + lambda * (b1^2 + b2^2 + ... + bn^2))))

  where lambda is a hyperparameter that controls the amount of regularization. A higher lambda means more regularization and less overfitting, but also more bias and less variance. A lower lambda means less regularization and more overfitting, but also less bias and more variance. Bias is the difference between the expected or true value of the response variable and the predicted value by the model. Variance is the variability of the predicted value by the