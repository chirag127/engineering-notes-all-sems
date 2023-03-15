### Bayesian modeling

- Bayesian modeling is a statistical model where you use probability to represent all uncertainty within the model, both the uncertainty regarding the output but also the uncertainty regarding the input (aka parameters) to the model.
- A Bayesian model is based on Bayes' theorem, which describes the conditional probability of an event based on data as well as prior information or beliefs about the event or conditions related to the event.
- A Bayesian model consists of three main components: a likelihood function, a prior distribution, and a posterior distribution.
  - The likelihood function is the probability of the data given the parameters of the model.
  - The prior distribution is the probability of the parameters before observing the data, based on some assumptions or knowledge.
  - The posterior distribution is the probability of the parameters after observing the data, obtained by multiplying the likelihood and the prior and normalizing by the evidence (the probability of the data).
- A Bayesian model can be written in multiple levels (hierarchical form) to account for different sources of variation and uncertainty in the data.
- A Bayesian model can be used to perform inference, prediction, and decision-making based on the posterior distribution and its properties, such as the mean, the variance, the credible intervals, the posterior predictive distribution, etc.
- A Bayesian model can be updated with new data by using the posterior distribution as the new prior distribution and repeating the process of applying Bayes' theorem.
- A Bayesian model can be applied to various domains and problems, such as regression, classification, clustering, hypothesis testing, causal inference, etc.
- A Bayesian model can be implemented using various computational methods, such as Markov chain Monte Carlo (MCMC), variational inference, expectation propagation, etc.