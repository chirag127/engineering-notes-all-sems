### Markov chain Monte Carlo (MCMC) for the notes of the Unit 3 - Pseudo-Random Numbers in the subject of MATHEMATICAL FOUNDATION AI , ML AND DATA SCIENCE

- Markov chain Monte Carlo (MCMC) methods are a class of algorithms for sampling from a probability distribution.
- MCMC methods construct a Markov chain that has the desired distribution as its equilibrium or stationary distribution.
- A Markov chain is a sequence of random variables where the next state depends only on the current state and not on the previous states.
- The equilibrium or stationary distribution of a Markov chain is the probability distribution that remains unchanged in the long run as the chain is run.
- MCMC methods can be used to evaluate integrals, expected values, variances, and other quantities of interest over a continuous random variable, by generating samples from that variable .
- MCMC methods can also be used to explore the posterior distribution of Bayesian models, by generating samples from the posterior distribution given the data and the prior distribution .
- The main challenge of MCMC methods is to design a Markov chain that converges quickly and efficiently to the desired distribution, and to assess the quality and accuracy of the samples .
- The two most common approaches to MCMC sampling are Gibbs sampling and the Metropolis-Hastings algorithm .
- Gibbs sampling is a special case of the Metropolis-Hastings algorithm, where the acceptance probability of a new state is always one .
- Gibbs sampling works by updating one component of the state vector at a time, conditional on the rest of the components .
- The Metropolis-Hastings algorithm works by proposing a new state from a proposal distribution, and accepting or rejecting it based on a ratio of the target and proposal densities .
- The Metropolis-Hastings algorithm can handle more general proposal distributions than Gibbs sampling, but it may require more tuning and calibration .
- Both Gibbs sampling and the Metropolis-Hastings algorithm are examples of random-walk MCMC methods, where the next state is a perturbation of the current state.
- Other types of MCMC methods include Hamiltonian Monte Carlo, slice sampling, reversible jump MCMC, and sequential Monte Carlo .
- These methods aim to improve the efficiency, robustness, and scalability of MCMC sampling, by exploiting the structure, geometry, or dynamics of the target distribution .