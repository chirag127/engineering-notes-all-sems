
### Logistic Regression
Logistic regression is a type of supervised learning algorithm used in machine learning. It is used to predict the probability of an event occurring, based on previous data. Logistic regression is a type of regression analysis where the dependent variable is categorical.

Logistic regression is used in a variety of applications, such as predicting whether a customer will default on a loan, whether a patient has a certain disease, or whether an email is spam.

The goal of logistic regression is to find the best fitting model to describe the relationship between the dependent variable (the one we are trying to predict) and the independent variables (the factors that may influence the dependent variable).

The logistic regression model is a linear model, meaning that the relationship between the independent and dependent variables is assumed to be linear. The model is represented by a linear equation of the form:

$$\hat{y} = \beta_0 + \beta_1x_1 + \beta_2x_2 + ... + \beta_nx_n$$

where $\hat{y}$ is the predicted probability of the dependent variable, and $\beta_i$ are the model coefficients for each independent variable.

The coefficients of the logistic regression model can be estimated using maximum likelihood estimation. This involves finding the parameters that maximize the likelihood of the data given the model.

Once the model is estimated, it can be used to make predictions on new data. The predicted probability of the dependent variable can be used to assign a class label to each observation. For example, if the predicted probability is greater than 0.5, the observation is assigned to the “positive” class, and if the predicted probability is less than 0.5, the observation is assigned to the “negative” class.