Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of linear regression for the unit 2 - regression in the subject of machine learning techniques.

# Linear Regression

Linear regression is a supervised machine learning technique that models the relationship between one or more independent variables (also called predictors or features) and a dependent variable (also called response or outcome).

The goal of linear regression is to find the best-fitting line or hyperplane that minimizes the sum of squared errors (SSE) between the observed values and the predicted values of the dependent variable.

## Types of Linear Regression

There are two main types of linear regression: simple linear regression and multiple linear regression.

- Simple linear regression: This type of linear regression involves only one independent variable and one dependent variable. The equation of the best-fitting line is of the form:

  `y = b0 + b1 * x`

  where `y` is the dependent variable, `x` is the independent variable, `b0` is the intercept, and `b1` is the slope of the line.

- Multiple linear regression: This type of linear regression involves more than one independent variable and one dependent variable. The equation of the best-fitting hyperplane is of the form:

  `y = b0 + b1 * x1 + b2 * x2 + ... + bn * xn`

  where `y` is the dependent variable, `x1, x2, ..., xn` are the independent variables, `b0` is the intercept, and `b1, b2, ..., bn` are the coefficients of the independent variables.

## Assumptions of Linear Regression

Linear regression makes some assumptions about the data and the relationship between the variables. These assumptions are:

- Linearity: The relationship between the independent and dependent variables is linear, meaning that a change in one variable is associated with a proportional change in the other variable.

- Independence: The observations are independent of each other, meaning that the value of one observation does not affect the value of another observation.

- Homoscedasticity: The variance of the error terms is constant across all values of the independent variables, meaning that the errors are equally distributed.

- Normality: The error terms are normally distributed, meaning that they follow a bell-shaped curve.

## Methods of Estimating the Parameters

There are different methods of estimating the parameters of the linear regression model, such as the intercept and the coefficients. Some of the common methods are:

- Ordinary least squares (OLS): This method minimizes the sum of squared errors (SSE) between the observed and predicted values of the dependent variable. It is the most widely used method for linear regression.

- Gradient descent: This method iteratively updates the parameters by moving in the direction of the steepest descent of the cost function, which is usually the SSE. It is a popular method for large-scale data sets and complex models.

- Maximum likelihood estimation (MLE): This method maximizes the likelihood function, which is the probability of observing the data given the parameters. It is a more general method that can handle different types of error distributions and models.

## Evaluation Metrics for Linear Regression

There are different metrics to evaluate the performance and accuracy of the linear regression model, such as:

- R-squared: This metric measures the proportion of the variance in the dependent variable that is explained by the independent variables. It ranges from 0 to 1, with higher values indicating a better fit.

- Adjusted R-squared: This metric adjusts the R-squared value for the number of independent variables in the model. It penalizes the model for adding variables that do not improve the fit.

- Mean squared error (MSE): This metric measures the average of the squared errors between the observed and predicted values of the dependent variable. It is a measure of the overall error of the model.

- Root mean squared error (RMSE): This metric measures the square root of the MSE. It is a measure of the standard deviation of the errors.

- Mean absolute error (MAE): This metric measures the average of the absolute errors between the observed and predicted values of the dependent variable. It is a measure of the average error of the model.