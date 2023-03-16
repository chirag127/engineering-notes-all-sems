# Metropolis-Hastings algorithm

The Metropolis-Hastings algorithm is a Markov chain Monte Carlo (MCMC) method for obtaining a sequence of random samples from a probability distribution from which direct sampling is difficult. It is useful for drawing samples from Bayesian posterior distributions.

The main idea of the algorithm is to construct a Markov chain that has the desired distribution as its stationary distribution. The algorithm works by generating a sequence of sample values in such a way that, as more and more sample values are produced, the distribution of values more closely approximates the desired distribution.

The algorithm consists of the following steps  :

- Choose an initial value for the state of the Markov chain, denoted by x0.
- For each iteration t = 1, 2, ..., do the following:
  - Generate a candidate value for the next state, denoted by x*, from a proposal distribution q(x*|xt-1). This distribution can be chosen arbitrarily, as long as it is easy to sample from and has a nonzero probability for any possible value of x*.
  - Compute the acceptance ratio, denoted by r, which is given by:

    r = min(1, p(x*)q(xt-1|x*) / p(xt-1)q(x*|xt-1))

    where p(x) is the target distribution that we want to sample from.

  - Generate a uniform random number u from the interval [0, 1].
  - If u <= r, then accept the candidate value and set xt = x*. Otherwise, reject the candidate value and set xt = xt-1.
- Return the sequence of sample values x0, x1, ..., xn as an approximation of the target distribution.

The algorithm satisfies the detailed balance condition, which ensures that the stationary distribution of the Markov chain is the target distribution. The proposal distribution q(x*|xt-1) can be chosen to be symmetric, such as a normal distribution centered at xt-1, or asymmetric, such as a random-walk distribution that adds a random increment to xt-1. The choice of the proposal distribution affects the efficiency and convergence of the algorithm.

The Metropolis-Hastings algorithm is a generalization of the Metropolis algorithm, which was proposed by Metropolis et al. (1953) for simulating the distribution of states in a physical system. The Metropolis algorithm assumes that the proposal distribution is symmetric, so that q(x*|xt-1) = q(xt-1|x*). The Metropolis-Hastings algorithm relaxes this assumption and allows for asymmetric proposal distributions, which was suggested by Hastings (1970).

The Gibbs sampler can be viewed as a special case of the Metropolis-Hastings algorithm, where the proposal distribution is chosen to be the conditional distribution of one variable given the others. In this case, the acceptance ratio is always equal to one, so the candidate value is always accepted. The Gibbs sampler is useful when the full conditional distributions are easy to sample from, but the joint distribution is not.