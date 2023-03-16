### Gibbs sampling

- Gibbs sampling is a Markov chain Monte Carlo (MCMC) algorithm for obtaining a sequence of observations which are approximated from a specified multivariate probability distribution, when direct sampling is difficult.
- Gibbs sampling is based on the idea of sampling from the conditional distributions of each variable given the current values of the other variables.
- Gibbs sampling can be used as a means of statistical inference, especially Bayesian inference, when the posterior distribution is too complex to sample from directly or to compute analytically .
- Gibbs sampling consists of the following steps:
  - Choose initial values for each variable in the multivariate distribution.
  - For each iteration, do the following for each variable:
    - Sample a new value for the variable from its conditional distribution given the current values of the other variables.
    - Update the value of the variable with the sampled value.
  - Repeat the iterations until the Markov chain converges to the stationary distribution, which is the target distribution .
- Gibbs sampling has some advantages and disadvantages compared to other MCMC methods, such as Metropolis-Hastings:
  - Advantages:
    - It does not require tuning parameters, such as proposal distributions or acceptance probabilities.
    - It can exploit the structure of the joint distribution, such as conditional independence or conjugacy, to simplify the sampling process.
    - It can handle high-dimensional problems and complex dependencies among variables.
  - Disadvantages:
    - It can be slow to converge, especially if the variables are strongly correlated or the conditional distributions are multimodal or skewed.
    - It can suffer from poor mixing, meaning that the Markov chain can get stuck in a local mode or region of the target distribution.
    - It can be difficult to assess the convergence and the quality of the samples .