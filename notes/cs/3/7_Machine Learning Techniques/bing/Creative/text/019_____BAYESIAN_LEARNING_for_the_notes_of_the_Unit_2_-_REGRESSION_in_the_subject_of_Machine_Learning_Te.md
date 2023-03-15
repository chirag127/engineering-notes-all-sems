### BAYESIAN LEARNING for the notes of the Unit 2 - REGRESSION in the subject of Machine Learning Techniques

- Bayesian learning is a framework for reasoning about uncertainty and learning from data using the Bayes' theorem.
- Bayes' theorem states that the posterior probability of a hypothesis given some data is proportional to the prior probability of the hypothesis and the likelihood of the data given the hypothesis.
- Mathematically, Bayes' theorem can be written as:

$$P(H|D) = \frac{P(D|H)P(H)}{P(D)}$$

where $H$ is the hypothesis, $D$ is the data, $P(H|D)$ is the posterior probability, $P(D|H)$ is the likelihood, $P(H)$ is the prior probability, and $P(D)$ is the marginal probability.

- In machine learning, Bayesian learning can be applied to various models, such as regression, classification, clustering, etc. In this note, we will focus on Bayesian learning for regression models.
- Regression is a machine learning task to predict continuous values (real numbers) based on some input features (predictors or independent variables).
- A simple regression model is the linear regression model, which assumes that the output variable (dependent variable) is a linear function of the input features plus some noise.
- Mathematically, the linear regression model can be written as:

$$y = \theta^T x + \epsilon$$

where $y$ is the output variable, $\theta$ is the vector of parameters, $x$ is the vector of input features, and $\epsilon$ is the noise term, usually assumed to follow a normal distribution with zero mean and some variance $\sigma^2$.

- In Bayesian learning, we do not assume that the parameters $\theta$ have a single, unique value, but rather that they have a certain distribution: the prior distribution.
- The prior distribution represents our initial belief or assumption about the parameters before seeing any data.
- A common choice of prior distribution for linear regression is the normal distribution, which has two parameters: the mean $\mu$ and the variance $\Sigma$.
- Mathematically, the prior distribution can be written as:

$$P(\theta) = \mathcal{N}(\theta|\mu,\Sigma)$$

where $\mathcal{N}(\theta|\mu,\Sigma)$ denotes the normal distribution with mean $\mu$ and variance $\Sigma$.

- After seeing some data, we can update our belief about the parameters using the Bayes' theorem and obtain the posterior distribution.
- The posterior distribution represents our updated belief or knowledge about the parameters after seeing some data.
- Mathematically, the posterior distribution can be written as:

$$P(\theta|D) = \frac{P(D|\theta)P(\theta)}{P(D)}$$

where $D$ is the data, $P(\theta|D)$ is the posterior distribution, $P(D|\theta)$ is the likelihood, $P(\theta)$ is the prior distribution, and $P(D)$ is the marginal distribution.

- The likelihood is the probability of the data given the parameters, which can be computed using the linear regression model and the noise distribution.
- Mathematically, the likelihood can be written as:

$$P(D|\theta) = \prod_{i=1}^n P(y_i|x_i,\theta) = \prod_{i=1}^n \mathcal{N}(y_i|\theta^T x_i, \sigma^2)$$

where $n$ is the number of data points, $y_i$ is the output variable for the $i$-th data point, $x_i$ is the input feature vector for the $i$-th data point, and $\mathcal{N}(y_i|\theta^T x_i, \sigma^2)$ denotes the normal distribution with mean $\theta^T x_i$ and variance $\sigma^2$.

- The marginal distribution is the probability of the data, which can be computed by integrating out the parameters from the joint distribution of the data and the parameters.
- Mathematically, the marginal distribution can be written as:

$$P(D) = \int P(D|\theta)P(\theta) d\theta$$

where the integral is over all possible values of $\theta