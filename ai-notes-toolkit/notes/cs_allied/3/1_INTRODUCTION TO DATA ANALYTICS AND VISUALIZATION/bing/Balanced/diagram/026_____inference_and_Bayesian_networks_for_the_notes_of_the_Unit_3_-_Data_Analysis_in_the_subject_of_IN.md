### Inference and Bayesian Networks

- Bayesian networks are a type of probabilistic graphical model that uses Bayesian inference for probability computations .
- Bayesian networks aim to model conditional dependence, and therefore causation, by representing conditional dependence by edges in a directed graph .
- Through these relationships, one can efficiently conduct inference on the random variables in the graph through the use of factors .
- Factors are functions that map a set of variables to a real number, representing the strength of their association.
- Inference is one key objective in a Bayesian network, and it aims to estimate the posterior distributions of state variables based on evidence (observations).
- Inference over a Bayesian network can come in two forms: exact and approximate.
- Exact inference methods compute the exact posterior distributions by using algorithms such as enumeration or variable elimination .
- Enumeration is a brute-force method that sums over all possible assignments of the variables in the network.
- Variable elimination is a more efficient method that exploits the conditional independence properties of the network and eliminates irrelevant variables.
- Approximate inference methods use sampling techniques to generate approximate posterior distributions by using algorithms such as stochastic simulation or Markov chain Monte Carlo (MCMC)  .
- Stochastic simulation is a method that generates samples from the joint distribution of the network and then uses them to estimate the posterior distributions.
- MCMC is a method that generates samples from a Markov chain that converges to the posterior distribution of the network .
- Approximate inference methods are useful when exact inference is intractable or computationally expensive, such as in multiply connected networks .
- Multiply connected networks are networks that have more than one (undirected) path between any two nodes, and they are NP-hard and #P-complete to perform exact inference on.
- Singly connected networks are networks that have at most one (undirected) path between any two nodes, and they are polynomial-time solvable for exact inference .