### Metropolis-Hastings algorithm

The Metropolis-Hastings algorithm is a Markov chain Monte Carlo (MCMC) method for obtaining a sequence of random samples from a probability distribution from which direct sampling is difficult. It is useful for drawing samples from Bayesian posterior distributions. The algorithm works by generating a sequence of sample values in such a way that, as more and more sample values are produced, the distribution of values more closely approximates the desired distribution.

The Metropolis-Hastings algorithm involves designing a Markov process that fulfills the following two conditions:

- The Markov process is irreducible, meaning that any state can be reached from any other state in a finite number of steps.
- The Markov process is aperiodic, meaning that the states are not visited in a regular pattern.

The stationary distribution of the Markov process is chosen to be the desired distribution. The derivation of the algorithm starts with the condition of detailed balance, which states that the probability of transitioning from state x to state y is equal to the probability of transitioning from state y to state x, multiplied by the ratio of the stationary probabilities of x and y.

The algorithm can be summarized as follows:

- Choose an initial state x0 and a proposal distribution q(x|y), which gives the probability of proposing state x given the current state y.
- For each iteration t = 1, 2, ..., do the following:
  - Generate a candidate state x* from q(x|x(t-1)).
  - Calculate the acceptance probability a(x*, x(t-1)) = min(1, p(x*)q(x(t-1)|x*) / (p(x(t-1))q(x*|x(t-1)))), where p(x) is the desired distribution.
  - Generate a uniform random number u from [0, 1].
  - If u < a(x*, x(t-1)), then accept the candidate state and set x(t) = x*; otherwise, reject the candidate state and set x(t) = x(t-1).
- Return the sequence of states x0, x1, x2, ... as the samples from the desired distribution.

There are different choices of the proposal distribution q(x|y), such as:

- Independent proposal: q(x|y) does not depend on y, and is usually chosen to be similar to p(x).
- Random-walk proposal: q(x|y) = q(x - y), meaning that the candidate state is obtained by adding a random perturbation to the current state.
- Gibbs sampling: q(x|y) = p(x|y), meaning that the candidate state is obtained by sampling from the conditional distribution of one variable given the others. This is a special case of Metropolis-Hastings with acceptance probability always equal to 1.