### Introduction for the notes of the Unit 2 - REGRESSION in the subject of Machine Learning Techniques

- Regression is a supervised learning technique that aims to model the relationship between a target variable (also called dependent variable or output) and one or more predictor variables (also called independent variables or inputs).
- Regression can be used for various purposes, such as prediction, inference, hypothesis testing, and data analysis.
- There are different types of regression techniques, depending on the nature and number of the predictor variables, the shape and form of the regression function, and the type and distribution of the target variable.
- Some of the common regression techniques are:
  - Linear regression: assumes a linear relationship between the target and predictor variables, and minimizes the sum of squared errors between the observed and predicted values.
  - Polynomial regression: extends linear regression by adding higher-order terms of the predictor variables, and can capture nonlinear relationships.
  - Logistic regression: models the probability of a binary target variable (such as yes/no, success/failure, etc.) as a function of the predictor variables, and uses a logistic function to map the probabilities to the range [0,1].
  - Multiple regression: involves more than one predictor variable, and can be linear or nonlinear, depending on the regression function.
  - Multivariate regression: involves more than one target variable, and can be linear or nonlinear, depending on the regression function.
  - Ridge regression: adds a regularization term to the linear regression objective function, and penalizes large values of the regression coefficients, to prevent overfitting and reduce multicollinearity.
  - Lasso regression: also adds a regularization term to the linear regression objective function, but uses the absolute value of the regression coefficients, and can perform feature selection by shrinking some coefficients to zero.
  - Elastic net regression: combines ridge and lasso regression, and uses a weighted sum of the squared and absolute values of the regression coefficients as the regularization term.
  - Support vector regression: uses the concept of support vectors and kernels to model nonlinear and high-dimensional relationships between the target and predictor variables, and minimizes the epsilon-insensitive loss function, which ignores errors within a certain margin.
  - Decision tree regression: uses a tree-like structure to split the predictor variables into regions, and assigns a constant value to the target variable for each region, based on the mean or median of the observed values.
  - Random forest regression: uses an ensemble of decision trees, each trained on a random subset of the data and/or the predictor variables, and averages their predictions to reduce the variance and improve the accuracy of the regression model.
  - Gradient boosting regression: also uses an ensemble of decision trees, but trains them sequentially, and each tree tries to correct the errors of the previous trees, by using a gradient descent algorithm to minimize a loss function.