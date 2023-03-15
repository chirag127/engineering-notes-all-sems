# Bayesian Learning for Machine Learning: Part II - Linear Regression

- Bayesian learning is a probabilistic approach to machine learning that incorporates prior knowledge and uncertainty into the learning process.
- Bayesian learning can be applied to various machine learning models, such as regression, classification, clustering, etc.
- In this note, we will focus on Bayesian learning for linear regression, which is a simple and widely used machine learning model for predicting continuous outcomes.

## Linear Regression

- Linear regression is a machine learning model that assumes a linear relationship between a dependent variable $Y$ and one or more independent variables $X$.
- The goal of linear regression is to find the optimal values of the coefficients $\beta$ that minimize the sum of squared errors (SSE) between the observed values of $Y$ and the predicted values of $Y$ using the linear equation:

$$
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_p X_p + \epsilon
$$

- where $\epsilon$ is the error term that captures the random variation in $Y$ that is not explained by the linear equation.
- The coefficients $\beta$ can be estimated using various methods, such as ordinary least squares (OLS), gradient descent, etc.

## Bayesian Learning for Linear Regression

- Bayesian learning for linear regression is a different way of estimating the coefficients $\beta$ that incorporates prior knowledge and uncertainty into the learning process.
- Bayesian learning treats the coefficients $\beta$ as random variables that follow a prior distribution $p(\beta)$ that reflects our initial beliefs about the possible values of $\beta$ before observing any data.
- Bayesian learning updates the prior distribution $p(\beta)$ using the observed data $D = \{(X_i, Y_i)\}_{i=1}^n$ to obtain the posterior distribution $p(\beta|D)$ that reflects our updated beliefs about the possible values of $\beta$ after observing the data.
- Bayesian learning uses the posterior distribution $p(\beta|D)$ to make predictions for new data $X_*$ by computing the predictive distribution $p(Y_*|X_*, D)$, which is the average of the linear equation over all possible values of $\beta$ weighted by their posterior probabilities:

$$
p(Y_*|X_*, D) = \int p(Y_*|X_*, \beta) p(\beta|D) d\beta
$$

- Bayesian learning for linear regression has several advantages over the traditional frequentist approach, such as:

  - It can incorporate prior knowledge and domain expertise into the learning process, which can improve the accuracy and robustness of the model.
  - It can quantify the uncertainty and variability of the coefficients $\beta$ and the predictions $Y_*$, which can provide useful information for decision making and risk assessment.
  - It can avoid overfitting and underfitting by automatically adjusting the complexity of the model according to the amount and quality of the data.

## Example of Bayesian Learning for Linear Regression

- To illustrate the Bayesian learning for linear regression, we will use a simple example of predicting the height of a person based on their weight.
- We will assume that the prior distribution of the coefficients $\beta$ is a normal distribution with mean zero and variance 100, which means that we have no strong prior beliefs about the values of $\beta$ and we allow for a wide range of possible values.
- We will use the following data set of 10 observations of weight and height:

| Weight (kg) | Height (cm) |
| ----------- | ----------- |
| 50          | 160         |
| 60          | 170         |
| 70          | 180         |
| 80          | 190         |
| 90          | 200         |
| 100         | 210         |
| 110         | 220         |
| 120         | 230         |
| 130         | 240         |
| 140         | 250         |

- We will use the Python library PyMC3 to perform the Bayesian learning for linear regression. The following code shows how to define the model, estimate the posterior distribution, and make predictions using PyMC3:

```python
# Import libraries
import numpy as np
import pandas as pd
import pymc3 as pm
import matplotlib.pyplot as plt

# Load data
data = pd.DataFrame({'weight': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],
                     'height': [160, 170,