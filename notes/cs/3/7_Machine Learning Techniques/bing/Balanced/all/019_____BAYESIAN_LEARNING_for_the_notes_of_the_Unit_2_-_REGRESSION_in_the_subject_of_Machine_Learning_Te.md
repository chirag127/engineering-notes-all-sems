# Bayesian Learning for Machine Learning: Part II - Linear Regression

- Bayesian learning is a probabilistic approach to machine learning that incorporates prior knowledge and uncertainty into the learning process.
- Bayesian learning can be applied to various machine learning models, such as regression, classification, clustering, etc.
- In this note, we will focus on Bayesian learning for linear regression, which is a simple and widely used machine learning model for predicting continuous values.

## Linear Regression

- Linear regression is a machine learning model that assumes a linear relationship between a dependent variable $Y$ and one or more independent variables $X$.
- The goal of linear regression is to find the optimal values of the coefficients $\beta$ that minimize the sum of squared errors (SSE) between the observed values of $Y$ and the predicted values of $Y$ using the linear equation:

$$
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_p X_p + \epsilon
$$

- where $\epsilon$ is the error term that captures the random noise in the data.
- The coefficients $\beta$ can be estimated using various methods, such as ordinary least squares (OLS), gradient descent, etc.

## Bayesian Learning for Linear Regression

- Bayesian learning for linear regression is based on the Bayes' theorem, which is a formula for calculating conditional probabilities:

$$
P(A|B) = \frac{P(B|A)P(A)}{P(B)}
$$

- where $P(A|B)$ is the posterior probability of $A$ given $B$, $P(B|A)$ is the likelihood of $B$ given $A$, $P(A)$ is the prior probability of $A$, and $P(B)$ is the marginal probability of $B$.
- In the context of linear regression, we can use the Bayes' theorem to update our beliefs about the coefficients $\beta$ given the data $D$:

$$
P(\beta|D) = \frac{P(D|\beta)P(\beta)}{P(D)}
$$

- where $P(\beta|D)$ is the posterior distribution of $\beta$ given $D$, $P(D|\beta)$ is the likelihood of $D$ given $\beta$, $P(\beta)$ is the prior distribution of $\beta$, and $P(D)$ is the marginal likelihood of $D$.
- The posterior distribution represents our updated beliefs about the coefficients after observing the data, and it incorporates both the prior information and the data evidence.
- The likelihood function measures how well the linear model fits the data, and it is usually assumed to follow a normal distribution with mean $Y$ and variance $\sigma^2$:

$$
P(D|\beta) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(y_i - \beta_0 - \beta_1 x_{i1} - ... - \beta_p x_{ip})^2}{2\sigma^2}\right)
$$

- The prior distribution reflects our initial beliefs about the coefficients before observing the data, and it can be chosen based on domain knowledge or assumptions. A common choice is to use a normal distribution with mean $0$ and variance $\tau^2$:

$$
P(\beta) = \prod_{j=0}^p \frac{1}{\sqrt{2\pi\tau^2}} \exp\left(-\frac{\beta_j^2}{2\tau^2}\right)
$$

- The marginal likelihood is the probability of the data under any possible values of the coefficients, and it can be obtained by integrating out the coefficients from the joint distribution:

$$
P(D) = \int P(D|\beta)P(\beta) d\beta
$$

- The marginal likelihood is often difficult to compute analytically, but it can be approximated using numerical methods, such as Monte Carlo sampling, Laplace approximation, etc.
- The posterior distribution can be used to make predictions for new data points $X^*$ by computing the predictive distribution of $Y^*$:

$$
P(Y^*|X^*,D) = \int P(Y^*|X^*,\beta)P(\beta|D) d\beta
$$

- where $P(Y^*|X^*,\beta)$ is the conditional distribution of $Y^*$ given $X^*$ and $\beta$, and it is usually assumed to follow a normal