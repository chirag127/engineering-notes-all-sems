# Metropolis-Hastings algorithm

The Metropolis-Hastings algorithm is a Markov Chain Monte Carlo (MCMC) method used for generating samples from a probability distribution. It is particularly useful when the distribution is difficult to sample from directly. The algorithm works by generating a sequence of samples, where each sample is dependent on the previous one. The sequence of samples is known as a Markov chain.

The algorithm consists of the following steps:

1. Choose an initial value for the Markov chain.
2. Generate a candidate sample from a proposal distribution.
3. Calculate the acceptance probability, which is the ratio of the target distribution evaluated at the candidate sample to the target distribution evaluated at the current sample.
4. Accept or reject the candidate sample based on the acceptance probability.
5. If the candidate sample is accepted, set it as the new current sample. Otherwise, keep the current sample.
6. Repeat steps 2-5 until the desired number of samples is obtained.

The Metropolis-Hastings algorithm is widely used in various fields, including physics, chemistry, and statistics. It is a powerful tool for generating samples from complex distributions and can be used to estimate parameters, make predictions, and perform Bayesian inference.