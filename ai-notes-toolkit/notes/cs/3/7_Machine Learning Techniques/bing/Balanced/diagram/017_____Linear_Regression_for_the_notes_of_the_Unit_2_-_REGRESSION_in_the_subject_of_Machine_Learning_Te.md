### Linear Regression for the notes of the Unit 2 - REGRESSION in the subject of Machine Learning Techniques

- Linear regression is a supervised machine learning algorithm that predicts a numeric target based on one or more independent variables.
- Linear regression assumes a linear relationship between the input and output variables, which can be represented by a straight line.
- Linear regression can be used for various purposes, such as finding the correlation between variables, testing hypotheses, estimating trends, and forecasting future values.
- Linear regression can be divided into two types: simple linear regression and multiple linear regression.
  - Simple linear regression involves one input variable and one output variable, and the equation of the line is y = a + bx, where y is the output, x is the input, a is the intercept, and b is the slope.
  - Multiple linear regression involves more than one input variable and one output variable, and the equation of the line is y = a + b1x1 + b2x2 + ... + bnxn, where y is the output, x1, x2, ..., xn are the inputs, a is the intercept, and b1, b2, ..., bn are the slopes.
- Linear regression learning the model involves finding the best values for the intercept and slope parameters that minimize the error between the predicted and actual outputs.
- Linear regression learning the model can be done by various methods, such as ordinary least squares, gradient descent, or regularized methods.
  - Ordinary least squares is a statistical method that calculates the intercept and slope parameters by minimizing the sum of squared errors between the predicted and actual outputs.
  - Gradient descent is an iterative method that updates the intercept and slope parameters by moving in the opposite direction of the gradient of the error function until it reaches a minimum.
  - Regularized methods are extensions of ordinary least squares that add a penalty term to the error function to reduce overfitting and improve generalization.
- Linear regression evaluating the model involves measuring the performance of the model on new data that was not used for training.
- Linear regression evaluating the model can be done by various metrics, such as mean squared error, root mean squared error, mean absolute error, coefficient of determination, or adjusted coefficient of determination.
  - Mean squared error is the average of the squared errors between the predicted and actual outputs.
  - Root mean squared error is the square root of the mean squared error, which gives the error in the same units as the output.
  - Mean absolute error is the average of the absolute errors between the predicted and actual outputs.
  - Coefficient of determination is a measure of how well the model explains the variation in the output, which ranges from 0 to 1, where 1 means perfect fit and 0 means no fit.
  - Adjusted coefficient of determination is a modified version of the coefficient of determination that takes into account the number of input variables and the sample size, which penalizes the model for adding unnecessary variables.