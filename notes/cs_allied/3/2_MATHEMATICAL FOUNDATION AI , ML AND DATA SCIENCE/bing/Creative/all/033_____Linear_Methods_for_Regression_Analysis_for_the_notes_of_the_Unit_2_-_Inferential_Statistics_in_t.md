# Linear Methods for Regression Analysis

## Introduction

Regression analysis is a statistical technique that aims to explore the relationship between a dependent variable (also known as the response or outcome variable) and one or more independent variables (also known as the predictors or explanatory variables). Regression analysis can be used for various purposes, such as:

- Describing how the dependent variable changes as the independent variables change.
- Testing hypotheses about the effects of the independent variables on the dependent variable.
- Estimating the value of the dependent variable for a given set of values of the independent variables.
- Predicting the value of the dependent variable for new or unseen values of the independent variables.

There are different types of regression models, depending on the nature and number of the independent and dependent variables, the functional form of the relationship, and the assumptions about the error term. In this note, we will focus on linear methods for regression analysis, which are widely used and have many applications in various fields.

## Simple Linear Regression

Simple linear regression is the simplest form of linear regression, where there is only one independent variable and one dependent variable. The goal of simple linear regression is to find a straight line that best fits the observed data, such that the sum of the squared errors (or residuals) is minimized. The equation of the simple linear regression model is:

$$
Y = \beta_0 + \beta_1 X + \epsilon
$$

where:

- $Y$ is the dependent variable.
- $X$ is the independent variable.
- $\beta_0$ is the intercept, or the value of $Y$ when $X$ is zero.
- $\beta_1$ is the slope, or the change in $Y$ for a unit change in $X$.
- $\epsilon$ is the error term, or the difference between the observed and predicted values of $Y$.

The parameters $\beta_0$ and $\beta_1$ are estimated from the data using the method of least squares, which minimizes the sum of the squared errors:

$$
\min_{\beta_0, \beta_1} \sum_{i=1}^n (Y_i - \beta_0 - \beta_1 X_i)^2
$$

where $n$ is the number of observations in the data. The solution to this optimization problem is given by:

$$
\hat{\beta}_1 = \frac{\sum_{i=1}^n (X_i - \bar{X})(Y_i - \bar{Y})}{\sum_{i=1}^n (X_i - \bar{X})^2}
$$

$$
\hat{\beta}_0 = \bar{Y} - \hat{\beta}_1 \bar{X}
$$

where $\bar{X}$ and $\bar{Y}$ are the sample means of $X$ and $Y$, respectively. The estimated regression line is then:

$$
\hat{Y} = \hat{\beta}_0 + \hat{\beta}_1 X
$$

where $\hat{Y}$ is the predicted value of $Y$ for a given value of $X$.

## Multiple Linear Regression

Multiple linear regression is a generalization of simple linear regression, where there are more than one independent variables and one dependent variable. The goal of multiple linear regression is to find a hyperplane that best fits the observed data, such that the sum of the squared errors (or residuals) is minimized. The equation of the multiple linear regression model is:

$$
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_p X_p + \epsilon
$$

where:

- $Y$ is the dependent variable.
- $X_1, X_2, \ldots, X_p$ are the independent variables.
- $\beta_0$ is the intercept, or the value of $Y$ when all the $X$'s are zero.
- $\beta_1, \beta_2, \ldots, \beta_p$ are the slopes, or the changes in $Y$ for unit changes in the corresponding $X$'s.
- $\epsilon$ is the error term, or the difference between the observed and predicted values of $Y$.

The parameters $\beta_0, \beta_1, \ldots, \beta_p$ are estimated from the data using the method of least squares, which minimizes the sum of the squared errors:

$$
\min_{\beta_0, \beta_1