### Gibbs sampling

- Gibbs sampling is a Markov chain Monte Carlo (MCMC) algorithm for obtaining a sequence of observations which are approximated from a specified multivariate probability distribution, when direct sampling is difficult.
- Gibbs sampling is based on the idea of sampling from the conditional distributions of each variable given the current values of the other variables.
- Gibbs sampling can be used as a means of statistical inference, especially Bayesian inference, when the posterior distribution is too complex to sample from directly or to compute analytically .
- Gibbs sampling consists of the following steps :
  - Choose initial values for each variable in the multivariate distribution.
  - For each iteration, do the following for each variable:
    - Sample a new value for the variable from its conditional distribution given the current values of the other variables.
    - Update the value of the variable with the sampled value.
  - Repeat the iterations until the samples converge to the target distribution or a desired level of accuracy is achieved.
- Gibbs sampling has some advantages and disadvantages as a MCMC method :
  - Advantages:
    - It is easy to implement and does not require tuning parameters such as step sizes or proposal distributions.
    - It can handle high-dimensional problems and complex dependencies among variables.
    - It can exploit the structure and sparsity of the conditional distributions to speed up the sampling process.
  - Disadvantages:
    - It can suffer from slow mixing and poor convergence if the conditional distributions are highly correlated or multimodal.
    - It can be inefficient if the conditional distributions are hard to sample from or have high variance.
    - It can be sensitive to the choice of initial values and the order of updating the variables.