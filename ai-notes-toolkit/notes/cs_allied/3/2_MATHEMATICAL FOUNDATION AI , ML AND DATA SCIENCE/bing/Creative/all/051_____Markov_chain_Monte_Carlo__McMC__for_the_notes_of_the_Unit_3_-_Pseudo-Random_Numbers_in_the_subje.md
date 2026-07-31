# Markov chain Monte Carlo (MCMC)

- Markov chain Monte Carlo (MCMC) is a class of algorithms for sampling from a probability distribution that is difficult to sample from directly.
- MCMC works by constructing a Markov chain that has the desired distribution as its equilibrium or stationary distribution, and then running the chain for a long enough time to reach equilibrium.
- A Markov chain is a stochastic process that moves from one state to another according to some transition probabilities that depend only on the current state and not on the past history of the process.
- The equilibrium or stationary distribution of a Markov chain is the probability distribution that remains unchanged as the chain evolves over time. It is also the limiting distribution of the chain as the number of steps goes to infinity.
- MCMC can be used to estimate various quantities of interest from the target distribution, such as means, variances, expected values, or posterior probabilities in Bayesian inference.
- MCMC can also be used to explore the shape and characteristics of the target distribution, such as its modes, tails, or correlations.
- The main challenge of MCMC is to design a Markov chain that converges quickly and reliably to the target distribution, and to diagnose and monitor the convergence of the chain.
- The two most common types of MCMC algorithms are Gibbs sampling and Metropolis-Hastings algorithm, which differ in how they generate the next state of the chain from the current state.
- Gibbs sampling is a special case of MCMC that updates one variable at a time, conditional on the values of the other variables. It is often used when the conditional distributions are easy to sample from, but the joint distribution is not.
- Metropolis-Hastings algorithm is a more general type of MCMC that proposes a new state from a proposal distribution, and then accepts or rejects it based on an acceptance ratio that ensures the detailed balance condition. It can be used when the proposal distribution is easy to sample from, but the target distribution is not.