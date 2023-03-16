### Metropolis-Hastings algorithm

- The Metropolis-Hastings algorithm is a Markov chain Monte Carlo (MCMC) method for obtaining a sequence of random samples from a probability distribution from which direct sampling is difficult  .
- The Metropolis-Hastings algorithm works by generating a sequence of sample values in such a way that, as more and more sample values are produced, the distribution of values more closely approximates the desired distribution.
- The Metropolis-Hastings algorithm involves designing a Markov process (by constructing transition probabilities) that fulfills the two conditions of irreducibility and aperiodicity, such that its stationary distribution () is chosen to be () . The derivation of the algorithm starts with the condition of detailed balance:
  - () = () for all , 
  - where () is the transition probability from state to state , and () is the desired distribution.
- The Metropolis-Hastings algorithm consists of the following steps   :
  - Choose an initial state  and set  = 0.
  - Generate a candidate state  from a proposal distribution () that depends only on the current state .
  - Calculate the acceptance ratio  = ()()/()(), where () is the desired distribution.
  - Generate a uniform random number  from [0, 1].
  - If  ≤ , accept the candidate state and set  = , otherwise reject the candidate state and set  = .
  - Increment  by 1 and repeat from step 2 until a sufficient number of samples are obtained.
- The proposal distribution () can be chosen in different ways, such as independent or random-walk proposals. The choice of () affects the efficiency and convergence of the algorithm.
- The Metropolis-Hastings algorithm is a general term for a family of Markov chain simulation methods that are useful for drawing samples from Bayesian posterior distributions. The Gibbs sampler can be viewed as a special case of Metropolis-Hastings (as well will soon see).