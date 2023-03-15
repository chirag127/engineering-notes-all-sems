### BAYESIAN LEARNING for the notes of the Unit 2 - REGRESSION in the subject of Machine Learning Techniques

- Bayesian learning is a framework for reasoning about uncertainty and updating beliefs based on evidence.
- Bayesian learning is based on the Bayes theorem, which states that the posterior probability of a hypothesis given some data is proportional to the prior probability of the hypothesis and the likelihood of the data given the hypothesis.
- Bayesian learning can be applied to various machine learning models, such as regression, classification, clustering, etc.
- In this note, we will focus on Bayesian learning for linear regression, which is a simple and widely used model for predicting a continuous output variable from one or more input variables.

#### Bayesian Linear Regression

- Linear regression assumes that the output variable y is a linear function of the input variables x, plus some noise term e:

y = w^T x + e

- where w is a vector of weights, x is a vector of inputs, and e is a random variable with zero mean and variance sigma^2.
- The goal of linear regression is to estimate the unknown weight vector w from a set of training data (x_i, y_i) for i = 1, ..., N.
- In the frequentist approach, w is treated as a fixed but unknown parameter, and the estimation is done by minimizing the sum of squared errors (SSE) between the predicted and actual outputs:

w_hat = argmin_w sum_i=1^N (y_i - w^T x_i)^2

- In the Bayesian approach, w is treated as a random variable with some prior distribution p(w), which encodes our initial beliefs about the possible values of w before seeing any data.
- The prior distribution can be chosen based on some domain knowledge or assumptions, such as smoothness, sparsity, etc.
- The Bayesian approach updates the prior distribution with the observed data using the Bayes theorem, and obtains the posterior distribution p(w|D), where D is the set of training data:

p(w|D) = p(D|w) p(w) / p(D)

- The posterior distribution represents our updated beliefs about the possible values of w after seeing the data.
- The posterior distribution can be used to make predictions for new inputs x* by computing the predictive distribution p(y*|x*, D), which is the average of the outputs over all possible values of w weighted by their posterior probabilities:

p(y*|x*, D) = integral p(y*|x*, w) p(w|D) dw

- The predictive distribution captures the uncertainty in both the model parameters w and the output variable y*.
- The Bayesian approach has several advantages over the frequentist approach, such as:
  - It avoids overfitting by regularizing the model parameters with the prior distribution.
  - It provides a principled way of selecting the model complexity by comparing the marginal likelihoods of different models.
  - It can handle missing data and outliers by incorporating them into the likelihood function.
  - It can incorporate prior knowledge and domain expertise into the model by choosing appropriate prior distributions.