### Unit 3 - Pseudo-Random Numbers: Gibbs Sampling

Gibbs sampling is a Markov chain Monte Carlo (MCMC) algorithm for obtaining a sequence of observations which are approximated from a specified multivariate probability distribution, when direct sampling is difficult . It is commonly used as a means of statistical inference, especially Bayesian inference .

In its basic incarnation, Gibbs sampling is a special case of the Metropolis–Hastings algorithm. The point of Gibbs sampling is that given a multivariate distribution, it is simpler to sample from a conditional distribution than to marginalize by integrating over a joint distribution .

Gibbs sampling is a randomized algorithm (i.e. an algorithm that makes use of random numbers), and is an alternative to deterministic algorithms for statistical inference such as the expectation-maximization algorithm (EM) .