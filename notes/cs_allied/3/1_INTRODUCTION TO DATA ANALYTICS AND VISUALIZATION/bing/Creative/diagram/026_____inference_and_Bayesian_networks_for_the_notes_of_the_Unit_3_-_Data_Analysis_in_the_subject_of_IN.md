### Inference and Bayesian Networks

- Bayesian networks are a type of probabilistic graphical model that uses Bayesian inference for probability computations .
- Bayesian networks aim to model conditional dependence, and therefore causation, by representing conditional dependence by edges in a directed graph .
- Through these relationships, one can efficiently conduct inference on the random variables in the graph through the use of factors .
- Factors are functions that map a set of variables to a real number, representing the strength of their association.
- Inference is one key objective in a Bayesian network, and it aims to estimate the posterior distributions of state variables based on evidence (observations).
- Inference over a Bayesian network can come in two forms: exact and approximate.
- Exact inference methods compute the exact posterior distributions by using algorithms such as enumeration or variable elimination .
- Enumeration is a brute-force method that sums out all the irrelevant variables from the joint distribution.
- Variable elimination is a more efficient method that exploits the conditional independence structure of the network and eliminates variables one by one.
- Approximate inference methods use sampling techniques to generate approximate posterior distributions by using algorithms such as stochastic simulation or Markov chain Monte Carlo (MCMC)  .
- Stochastic simulation is a method that generates samples from the prior distribution and then weights them by the likelihood of the evidence.
- MCMC is a method that generates samples from the posterior distribution by using a Markov chain that converges to the desired distribution .