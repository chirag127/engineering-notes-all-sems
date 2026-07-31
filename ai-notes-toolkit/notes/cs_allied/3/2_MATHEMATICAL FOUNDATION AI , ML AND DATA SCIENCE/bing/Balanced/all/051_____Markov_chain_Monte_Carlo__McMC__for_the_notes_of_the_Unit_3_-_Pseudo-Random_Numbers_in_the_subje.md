# Markov chain Monte Carlo (MCMC)

- Markov chain Monte Carlo (MCMC) is a class of algorithms for sampling from a probability distribution that is difficult to sample from directly.
- MCMC works by constructing a Markov chain that has the desired distribution as its equilibrium or stationary distribution, and then running the chain for a long enough time to reach the equilibrium.
- The states of the chain are then used as samples from the desired distribution, and can be used to estimate various quantities of interest, such as means, variances, expected values, or posterior distributions in Bayesian models.
- The main advantage of MCMC is that it can sample from complex and high-dimensional distributions that are intractable by other methods, such as analytical integration or rejection sampling.
- The main challenge of MCMC is to ensure that the chain converges to the equilibrium distribution, and to diagnose and monitor the convergence.
- There are different types of MCMC algorithms, such as Gibbs sampling, Metropolis-Hastings, Hamiltonian Monte Carlo, and slice sampling, that differ in how they propose and accept new states for the chain.
- MCMC is widely used in statistics, machine learning, physics, chemistry, biology, and other fields that involve modeling uncertainty and complexity.