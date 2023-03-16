# Metropolis-Hastings algorithm

The Metropolis-Hastings algorithm is a Markov chain Monte Carlo (MCMC) method for obtaining a sequence of random samples from a probability distribution from which direct sampling is difficult. It is useful for drawing samples from Bayesian posterior distributions.

The main steps of the algorithm are:

- Choose an initial value for the parameter of interest, denoted by x0.
- For each iteration t = 1, 2, ..., do the following:
  - Generate a candidate value x* from a proposal distribution q(x* | xt-1), which depends on the current value of the parameter.
  - Compute the acceptance ratio r = p(x*)q(xt-1 | x*) / (p(xt-1)q(x* | xt-1)), where p(x) is the target distribution.
  - Generate a uniform random number u from [0, 1].
  - If u < r, accept the candidate value and set xt = x*. Otherwise, reject the candidate value and set xt = xt-1.
- Return the sequence of accepted values as a sample from the target distribution.

The proposal distribution q(x* | xt-1) can be chosen in different ways, such as:

- Independent: q(x* | xt-1) = q(x*), which does not depend on the current value of the parameter. This simplifies the acceptance ratio to r = p(x*) / p(xt-1).
- Random-walk: q(x* | xt-1) = q(x* - xt-1), which depends on the difference between the candidate and the current value of the parameter. This allows the chain to explore the parameter space more efficiently.

The Metropolis-Hastings algorithm works by generating a sequence of sample values in such a way that, as more and more sample values are produced, the distribution of values more closely approximates the desired distribution. The algorithm satisfies two conditions:

- Ergodicity: the chain can reach any state from any other state in a finite number of steps.
- Detailed balance: the chain is in equilibrium, meaning that the probability of moving from one state to another is equal to the probability of moving in the opposite direction.

The Metropolis-Hastings algorithm is widely used in statistics and computational physics for solving problems such as Bayesian inference, optimization, and simulation. It is also the basis for other MCMC methods, such as the Gibbs sampler.