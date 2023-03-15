# Inference and Bayesian Networks

- Bayesian networks are a type of probabilistic graphical model that uses Bayesian inference for probability computations .
- Bayesian networks aim to model conditional dependence, and therefore causation, by representing conditional dependence by edges in a directed graph .
- Through these relationships, one can efficiently conduct inference on the random variables in the graph through the use of factors.
- Factors are functions that map a set of variables to a real number, representing the strength of their association.
- Inference is one key objective in a Bayesian network, and it aims to estimate the posterior distributions of state variables based on evidence (observations).
- Inference over a Bayesian network can come in two forms: exact or approximate.
- Exact inference methods compute the exact posterior distributions by using algorithms such as enumeration or variable elimination .
- Enumeration is a brute-force method that sums over all possible assignments of the variables in the network.
- Variable elimination is a more efficient method that exploits the conditional independence properties of the network and eliminates irrelevant variables.
- Approximate inference methods use stochastic simulation or sampling techniques to generate approximate posterior distributions by using algorithms such as Monte Carlo methods or Markov chain Monte Carlo (MCMC) methods  .
- Monte Carlo methods are based on generating random samples from the network and using them to estimate the posterior distributions.
- Markov chain Monte Carlo methods are based on constructing a Markov chain that converges to the desired posterior distribution and sampling from it .
- Approximate inference methods are useful when exact inference is intractable or computationally expensive, such as in multiply connected networks .
- Multiply connected networks are networks that have more than one (undirected) path between any two nodes, and are NP-hard and #P-complete to perform exact inference on.