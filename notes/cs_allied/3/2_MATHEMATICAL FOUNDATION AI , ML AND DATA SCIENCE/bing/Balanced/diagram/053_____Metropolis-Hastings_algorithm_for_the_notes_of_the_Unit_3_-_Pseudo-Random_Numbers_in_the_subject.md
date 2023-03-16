### Metropolis-Hastings algorithm

- The Metropolis-Hastings algorithm is a Markov chain Monte Carlo (MCMC) method for obtaining a sequence of random samples from a probability distribution from which direct sampling is difficult  .
- The algorithm works by generating a sequence of sample values in such a way that, as more and more sample values are produced, the distribution of values more closely approximates the desired distribution .
- The algorithm involves designing a Markov process (by constructing transition probabilities) that fulfills two conditions: 
  - The Markov process is irreducible, meaning that any state can be reached from any other state in a finite number of steps.
  - The Markov process is aperiodic, meaning that the states are not visited in a regular pattern.
- The stationary distribution of the Markov process is chosen to be the desired distribution  .
- The algorithm starts with the condition of detailed balance, which states that the probability of moving from state x to state y is equal to the probability of moving from state y to state x in the stationary distribution .
- The algorithm consists of the following steps:
  - Choose an initial state x0 and a proposal distribution q(x|y) that is easy to sample from and has a nonzero probability for any x and y.
  - For each iteration t = 1, 2, ..., do the following:
    - Generate a candidate state y from the proposal distribution q(y|x(t-1)).
    - Compute the acceptance ratio a = min(1, p(y)q(x(t-1)|y) / p(x(t-1))q(y|x(t-1))), where p(x) is the desired distribution.
    - Generate a uniform random number u from [0, 1].
    - If u < a, accept the candidate state and set x(t) = y. Otherwise, reject the candidate state and set x(t) = x(t-1).
- The output of the algorithm is the sequence of states x0, x1, x2, ..., which converges to the desired distribution p(x) as t increases   .
- The algorithm can be modified by using different proposal distributions, such as a random-walk proposal that adds a random perturbation to the current state, or an independent proposal that does not depend on the current state .
- The algorithm can also be extended to handle multivariate distributions, by using vector-valued states and proposal distributions .
- The algorithm can be used for various applications, such as Bayesian inference, optimization, simulation, and statistical physics  .