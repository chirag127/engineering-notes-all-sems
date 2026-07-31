# Bayesian Learning for Machine Learning: Part II - Linear Regression

- Bayesian learning is a probabilistic approach to machine learning that incorporates prior knowledge and uncertainty into the learning process.
- Bayesian learning can be applied to various machine learning models, such as regression, classification, clustering, etc.
- In this note, we will focus on Bayesian learning for linear regression, which is a simple and widely used model for predicting a continuous output variable from one or more input variables.

## Linear Regression

- Linear regression assumes that the output variable $y$ is a linear function of the input variables $x_1, x_2, ..., x_n$, plus some random noise $\epsilon$:

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + ... + \beta_n x_n + \epsilon$$

- The coefficients $\beta_0, \beta_1, ..., \beta_n$ are called the regression parameters, and they determine the slope and intercept of the linear function.
- The noise term $\epsilon$ is assumed to follow a normal distribution with mean zero and variance $\sigma^2$, which is also a parameter of the model:

$$\epsilon \sim \mathcal{N}(0, \sigma^2)$$

- Given a set of training data $(x_i, y_i)$ for $i = 1, 2, ..., N$, the goal of linear regression is to estimate the parameters $\beta_0, \beta_1, ..., \beta_n$ and $\sigma^2$ that best fit the data.
- One common way to do this is by minimizing the sum of squared errors (SSE) between the observed outputs and the predicted outputs:

$$\text{SSE} = \sum_{i=1}^N (y_i - \hat{y}_i)^2$$

where $\hat{y}_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + ... + \beta_n x_{in}$ is the predicted output for the $i$-th input.

- This method is also known as ordinary least squares (OLS) or maximum likelihood estimation (MLE), and it results in point estimates for the parameters, meaning that they are fixed values with no uncertainty.

## Bayesian Linear Regression

- Bayesian linear regression is a different way of estimating the parameters of the linear model, based on the Bayes' theorem:

$$P(\theta | D) = \frac{P(D | \theta) P(\theta)}{P(D)}$$

where $\theta$ is the vector of parameters ($\beta_0, \beta_1, ..., \beta_n, \sigma^2$), $D$ is the data ($x_i, y_i$), $P(\theta | D)$ is the posterior distribution of the parameters given the data, $P(D | \theta)$ is the likelihood of the data given the parameters, $P(\theta)$ is the prior distribution of the parameters, and $P(D)$ is the marginal likelihood of the data.

- The posterior distribution represents our updated belief about the parameters after observing the data, and it incorporates both the likelihood and the prior information.
- The likelihood measures how well the parameters fit the data, and it is the same as the MLE method.
- The prior reflects our initial belief about the parameters before seeing the data, and it can be chosen based on some domain knowledge or assumptions.
- The marginal likelihood is a normalizing constant that ensures that the posterior is a valid probability distribution, and it can be computed by integrating over all possible values of the parameters.

- The advantage of Bayesian linear regression is that it provides a full distribution of the parameters, rather than a single point estimate, which allows us to quantify the uncertainty and variability of the parameters.
- The disadvantage is that it requires us to specify a prior distribution, which may be subjective or arbitrary, and it may be computationally expensive or intractable to calculate the posterior distribution, especially for high-dimensional or complex models.

## Example

- To illustrate the Bayesian linear regression, let us consider a simple example with one input variable $x$ and one output variable $y$, and assume that the true model is:

$$y = 3 + 2x + \epsilon$$

where $\epsilon \sim \mathcal{N}(0, 1)$.

- We generate 20 data points from this model and plot them below:

![data](https://i.imgur.com/0Z1wQZw.png)

- We want to