## Unit 2 - REGRESSION

Regression is a statistical method that allows us to examine the relationship between one or more explanatory variables (also called independent variables or predictors) and a response variable (also called dependent variable or outcome).

The main goal of regression is to model the expected value of the response variable given the values of the explanatory variables. Regression can also be used to test hypotheses about the effects of the explanatory variables on the response variable, and to quantify the uncertainty of the estimates.

There are different types of regression models depending on the nature of the response variable and the explanatory variables. Some of the most common types are:

- Linear regression: The response variable is continuous and the relationship between the response and the explanatory variables is linear. The model can be written as:

  `y = β0 + β1x1 + β2x2 + ... + βkxk + ε`

  where y is the response variable, x1, x2, ..., xk are the explanatory variables, β0, β1, ..., βk are the coefficients, and ε is the error term.

- Logistic regression: The response variable is binary (0 or 1) and the relationship between the response and the explanatory variables is modeled by a logistic function. The model can be written as:

  `logit(p) = β0 + β1x1 + β2x2 + ... + βkxk`

  where p is the probability of the response being 1, x1, x2, ..., xk are the explanatory variables, β0, β1, ..., βk are the coefficients, and logit(p) is the log-odds of the response being 1.

- Poisson regression: The response variable is a count (non-negative integer) and the relationship between the response and the explanatory variables is modeled by a Poisson distribution. The model can be written as:

  `log(λ) = β0 + β1x1 + β2x2 + ... + βkxk`

  where λ is the expected value of the response variable, x1, x2, ..., xk are the explanatory variables, β0, β1, ..., βk are the coefficients, and log(λ) is the natural logarithm of the expected value of the response variable.

There are many other types of regression models, such as nonlinear regression, multilevel regression, survival analysis, etc. Each type of regression model has its own assumptions, methods of estimation, and interpretation. Regression models can also be extended to include interaction terms, polynomial terms, categorical variables, etc. to capture more complex relationships.

Some of the benefits of using regression models are:

- They can help us understand how the response variable changes with respect to the explanatory variables, and identify the most important predictors.
- They can help us make predictions or estimates of the response variable for new or unseen data, and quantify the uncertainty of the predictions or estimates.
- They can help us test hypotheses or answer research questions about the effects of the explanatory variables on the response variable, and provide evidence for causal inference.

Some of the challenges of using regression models are:

- They require careful selection of the appropriate type of model, the relevant explanatory variables, and the functional form of the relationship.
- They require checking and validating the assumptions of the model, such as linearity, independence, homoscedasticity, normality, etc. for linear regression, or link function, dispersion, etc. for other types of regression.
- They require proper interpretation and communication of the results, such as the meaning and significance of the coefficients, the goodness-of-fit of the model, the prediction intervals or confidence intervals, etc.