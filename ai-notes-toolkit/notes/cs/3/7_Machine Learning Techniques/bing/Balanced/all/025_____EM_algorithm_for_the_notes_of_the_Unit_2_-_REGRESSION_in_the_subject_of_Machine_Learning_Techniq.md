# EM algorithm for regression

The EM algorithm is a general method for finding maximum likelihood estimates of parameters in statistical models that involve latent or missing variables. It consists of two steps: the expectation step (E-step) and the maximization step (M-step).

- In the E-step, the latent or missing variables are estimated using the current values of the parameters and the observed data. This can be done by computing the conditional expectation of the latent variables given the observed data and the parameters, or by sampling from the conditional distribution of the latent variables.
- In the M-step, the parameters are updated by maximizing the expected log-likelihood of the observed and latent data, where the expectation is taken over the latent variables estimated in the E-step.

The EM algorithm iterates between the E-step and the M-step until convergence, which can be measured by the change in the log-likelihood or the parameters.

## EM algorithm for linear regression

Linear regression is a simple and widely used statistical model that assumes a linear relationship between a response variable and a set of predictor variables. The parameters of the linear regression model are the coefficients of the predictor variables and the intercept term.

The EM algorithm can be applied to linear regression in various scenarios, such as:

- When some of the response or predictor variables are missing or censored .
- When the response variable is binary or categorical, and the linear regression model is a probit or logistic regression model.
- When the response variable is subject to measurement error or heteroscedasticity.

In each scenario, the EM algorithm can be derived by specifying the latent or missing variables and their conditional distributions, and then applying the general E-step and M-step formulas.

For example, consider the case where some of the response variables are missing at random. Let $y_i$ be the response variable for the $i$-th observation, and let $x_i$ be the vector of predictor variables for the $i$-th observation. Let $\beta$ be the vector of parameters of the linear regression model, and let $\sigma^2$ be the variance of the error term. Assume that the error term follows a normal distribution with mean zero and variance $\sigma^2$.

The latent variable in this case is the missing response variable, denoted by $y_i^*$. The conditional distribution of $y_i^*$ given $x_i$ and $\beta$ is normal with mean $x_i^T\beta$ and variance $\sigma^2$.

The EM algorithm for this case is as follows:

- Initialize $\beta$ and $\sigma^2$ with some values, such as the estimates from the complete cases or the least squares method.
- Repeat until convergence:
  - E-step: For each observation with missing response variable, estimate $y_i^*$ by its conditional expectation, which is $x_i^T\beta$.
  - M-step: Update $\beta$ and $\sigma^2$ by maximizing the expected log-likelihood of the observed and latent data, which is
  $$
  \sum_{i=1}^n \log f(y_i^*|x_i,\beta,\sigma^2) = -\frac{n}{2}\log(2\pi\sigma^2) - \frac{1}{2\sigma^2}\sum_{i=1}^n (y_i^* - x_i^T\beta)^2
  $$
  where $f$ is the normal density function. The maximization can be done by setting the derivatives with respect to $\beta$ and $\sigma^2$ to zero and solving for them, which gives
  $$
  \beta = (X^TX)^{-1}X^TY^*
  $$
  and
  $$
  \sigma^2 = \frac{1}{n}\sum_{i=1}^n (y_i^* - x_i^T\beta)^2
  $$
  where $X$ is the matrix of predictor variables and $Y^*$ is the vector of observed and estimated response variables.

The EM algorithm can be modified or extended to handle other scenarios of linear regression with latent or missing variables, by changing the latent variables, their conditional distributions, and the expected log-likelihood function accordingly.