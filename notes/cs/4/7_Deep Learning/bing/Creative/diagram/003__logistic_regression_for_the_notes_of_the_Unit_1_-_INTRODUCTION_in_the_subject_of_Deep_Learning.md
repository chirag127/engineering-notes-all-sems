### Logistic regression

Logistic regression is a statistical model that predicts the probability of a binary outcome (such as yes or no, 1 or 0, success or failure) based on one or more input variables (also called features or predictors). The input variables can be either continuous (such as age, height, weight) or categorical (such as gender, color, type).

The logistic regression model uses a function called the logistic function or the sigmoid function to transform the linear combination of the input variables into a probability value between 0 and 1. The logistic function has an S-shaped curve that can be written as:

```
f(x) = 1 / (1 + e^(-x))
```

where x is the linear combination of the input variables and their coefficients, and e is the base of the natural logarithm. The coefficients are the parameters of the logistic regression model that need to be estimated from the data.

The following diagram illustrates the basic architecture of a logistic regression model:

```
  Input variables (x1, x2, ..., xn)    Linear combination    Logistic function    Output probability (y)
+-----------------+-----------------+ +-----------------+ +-----------------+ +-----------------+
|                 |                 | |                 | |                 | |                 |
|        x1       |        x2       | |        x        | |      f(x)       | |        y        |
|                 |                 | |                 | |                 | |                 |
+-----------------+-----------------+ +-----------------+ +-----------------+ +-----------------+
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       v                v                     v                   v                   v
+-----------------+-----------------+ +-----------------+ +-----------------+ +-----------------+
|                 |                 | |                 | |                 | |                 |
|       b1        |       b2        | |       b0        | |                 | |                 |
|                 |                 | |                 | |                 | |                 |
+-----------------+-----------------+ +-----------------+ +-----------------+ +-----------------+
       |                |                     |                   |
       |                |                     |                   |
       |                |                     |                   |
       |                |                     |                   |
       |                |                     |                   |
       |                |                     |                   |
       |                |                     |                   |
       |                |                     |                   |
       |                |                     |                   |
       |                |                     |                   |
       |                |                     |                   |
       |                |                     |                   |
       +----------------+---------------------+-------------------+
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  v
+-----------------+-----------------+ +-----------------+ +-----------------+ +-----------------+
|                 |                 | |                 | |                 | |                 |
|       x1*b1     |       x2*b2     | |       b0        | |      x*b        | |    f(x*b)       |
|                 |                 | |                 | |                 | |                 |
+-----------------+-----------------+ +-----------------+ +-----------------+ +-----------------+
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       |                |                     |                   |                   |
       +----------------+---------------------+-------------------+-------------------+
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                                  v
+-----------------+-----------------+ +-----------------+ +-----------------+ +-----------------+
|                 |                 | |                 | |                 | |