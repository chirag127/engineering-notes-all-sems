## Unit 2 - REGRESSION

Regression is a statistical method used in data analysis to establish a relationship between a dependent variable and one or more independent variables. This method is used to predict the value of the dependent variable based on the values of the independent variables.

Regression can be broadly classified into two types: 

1. Simple regression: This is a type of regression where there is only one independent variable that is used to predict the dependent variable. 

2. Multiple regression: This is a type of regression where there are two or more independent variables that are used to predict the dependent variable.

### Simple Linear Regression

Simple linear regression is a statistical method used to establish a linear relationship between a dependent variable and one independent variable. In this method, a straight line is fitted to the data points to predict the value of the dependent variable.

The equation for simple linear regression is given by:

`y = mx + c`

where y is the dependent variable, x is the independent variable, m is the slope of the line, and c is the y-intercept.

### Multiple Linear Regression

Multiple linear regression is a statistical method used to establish a linear relationship between a dependent variable and two or more independent variables. In this method, a plane is fitted to the data points to predict the value of the dependent variable.

The equation for multiple linear regression is given by:

`y = b0 + b1x1 + b2x2 + ... + bnxn`

where y is the dependent variable, x1, x2, ..., xn are the independent variables, and b0, b1, b2, ..., bn are the coefficients of the independent variables.

### Logistic Regression

Logistic regression is a statistical method used to establish a relationship between a dependent variable and one or more independent variables. This method is used when the dependent variable is binary (0 or 1). The logistic regression model is used to predict the probability of the occurrence of an event.

The equation for logistic regression is given by:

`p = 1 / (1 + exp(-z))`

where p is the probability of the occurrence of an event, exp is the exponential function, and z is the linear combination of the independent variables.

### Polynomial Regression

Polynomial regression is a statistical method used to establish a relationship between a dependent variable and one independent variable where the relationship is not linear. In this method, a polynomial function is fitted to the data points to predict the value of the dependent variable.

The equation for polynomial regression is given by:

`y = b0 + b1x + b2x^2 + ... + bnx^n`

where y is the dependent variable, x is the independent variable, and b0, b1, b2, ..., bn are the coefficients of the independent variables.

### Ridge Regression

Ridge regression is a statistical method used to prevent overfitting in the regression model. In this method, a penalty term is added to the cost function to reduce the magnitude of the coefficients of the independent variables.

The equation for ridge regression is given by:

`Cost function = RSS + λΣ(bi^2)`

where RSS is the residual sum of squares, λ is the regularization parameter, and bi is the coefficient of the independent variable.

### Lasso Regression

Lasso regression is a statistical method used to prevent overfitting in the regression model. In this method, a penalty term is added to the cost function to reduce the magnitude of the coefficients of the independent variables. Lasso regression is similar to ridge regression, but it uses the L1 norm instead of the L2 norm.

The equation for lasso regression is given by:

`Cost function = RSS + λΣ|bi|`

where RSS is the residual sum of squares, λ is the regularization parameter, and bi is the coefficient of the independent variable.