### Markov chain Monte Carlo (MCMC) for the notes of the Unit 3 - Pseudo-Random Numbers in the subject of MATHEMATICAL FOUNDATION AI , ML AND DATA SCIENCE

- Markov chain Monte Carlo (MCMC) methods are a class of algorithms for sampling from a probability distribution.
- MCMC methods construct a Markov chain that has the desired distribution as its equilibrium or stationary distribution.
- A Markov chain is a sequence of random variables where the next state depends only on the current state and not on the previous states.
- The equilibrium or stationary distribution of a Markov chain is the probability distribution that remains unchanged in the long run as the chain is run.
- MCMC methods can be used to evaluate integrals, expected values, variances, and other quantities of interest over a continuous random variable, by generating samples from that variable .
- MCMC methods can also be used to explore the posterior distribution of Bayesian models, by generating samples from the posterior distribution given the data and the prior distribution .
- MCMC methods are useful when the probability distribution is complex, high-dimensional, or unknown, and when direct sampling is difficult or impossible .
- The two most common approaches to MCMC sampling are Gibbs sampling and the Metropolis-Hastings algorithm .
- Gibbs sampling is a special case of the Metropolis-Hastings algorithm, where the acceptance probability is always one .
- Gibbs sampling generates samples by updating one variable at a time, conditional on the current values of the other variables .
- The Metropolis-Hastings algorithm generates samples by proposing a new state based on the current state, and accepting or rejecting it based on a criterion that ensures the equilibrium distribution is preserved .
- The proposal distribution and the acceptance criterion are the two main components of the Metropolis-Hastings algorithm .
- MCMC methods are iterative and require a starting point or initial state  .
- MCMC methods may take some time to converge to the equilibrium distribution, depending on the properties of the Markov chain and the initial state  .
- MCMC methods may produce correlated samples, which can affect the accuracy and efficiency of the estimation  .
- MCMC methods require careful diagnostics and checks to ensure the validity and reliability of the results  .