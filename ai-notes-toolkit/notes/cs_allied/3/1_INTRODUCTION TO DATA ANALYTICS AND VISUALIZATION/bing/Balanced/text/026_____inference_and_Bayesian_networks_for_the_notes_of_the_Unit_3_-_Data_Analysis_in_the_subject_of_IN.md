### Inference and Bayesian Networks

- Bayesian networks are a type of probabilistic graphical model that uses Bayesian inference for probability computations .
- Bayesian networks aim to model conditional dependence, and therefore causation, by representing conditional dependence by edges in a directed graph .
- Through these relationships, one can efficiently conduct inference on the random variables in the graph through the use of factors.
- Factors are functions that map a set of variables to a real number, representing the strength of their association.
- Inference is one key objective in a Bayesian network, and it aims to estimate the posterior distributions of state variables based on evidence (observations).
- Inference over a Bayesian network can come in two forms: exact inference and approximate inference.
- Exact inference is the process of computing the exact posterior distributions of the variables of interest, given the evidence.
- Exact inference can be done by enumeration, which involves summing out all the irrelevant variables from the joint distribution, or by variable elimination, which involves applying the distributive law to factorize the joint distribution and eliminate variables one by one .
- Exact inference is computationally expensive and intractable for large and complex networks, especially if they are multiply connected (have more than one undirected path between any two nodes) .
- Approximate inference is the process of computing an approximation of the posterior distributions of the variables of interest, given the evidence.
- Approximate inference can be done by stochastic simulation, which involves sampling from the joint distribution and counting the frequency of the samples that match the evidence, or by Markov chain Monte Carlo (MCMC), which involves constructing a Markov chain that converges to the desired posterior distribution and sampling from it  .
- Approximate inference is computationally efficient and scalable for large and complex networks, but it introduces some error and uncertainty in the results.