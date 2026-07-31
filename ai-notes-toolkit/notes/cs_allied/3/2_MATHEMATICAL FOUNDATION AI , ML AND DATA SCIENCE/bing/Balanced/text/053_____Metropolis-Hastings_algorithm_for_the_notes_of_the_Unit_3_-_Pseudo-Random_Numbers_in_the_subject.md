### Metropolis-Hastings algorithm

- The Metropolis-Hastings algorithm is a Markov chain Monte Carlo (MCMC) method for obtaining a sequence of random samples from a probability distribution from which direct sampling is difficult .
- The algorithm works by generating a sequence of sample values in such a way that, as more and more sample values are produced, the distribution of values more closely approximates the desired distribution.
- The algorithm involves designing a Markov process that fulfills two conditions: 
  - The Markov process is irreducible, meaning that any state can be reached from any other state in a finite number of steps.
  - The Markov process is aperiodic, meaning that the states are not visited in a regular pattern.
- The stationary distribution of the Markov process is chosen to be the desired distribution .
- The algorithm consists of the following steps:
  - Choose an initial value for the state variable x.
  - Repeat the following steps until a sufficient number of samples are obtained:
    - Generate a candidate value x' from a proposal distribution q(x'|x), which depends on the current value of x.
    - Compute the acceptance ratio r = p(x')q(x|x') / (p(x)q(x'|x)), where p(x) is the desired distribution.
    - Generate a uniform random number u from [0,1].
    - If u < r, accept the candidate value and set x = x'. Otherwise, reject the candidate value and keep x unchanged.
    - Record the value of x as a sample from the desired distribution.