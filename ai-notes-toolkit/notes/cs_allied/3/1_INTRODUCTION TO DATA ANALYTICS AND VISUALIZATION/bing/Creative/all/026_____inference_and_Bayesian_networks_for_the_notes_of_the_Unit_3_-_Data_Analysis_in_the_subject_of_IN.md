# Inference and Bayesian Networks

## Introduction

- Bayesian networks are a type of probabilistic graphical model that uses Bayesian inference for probability computations .
- Bayesian networks aim to model conditional dependence, and therefore causation, by representing conditional dependence by edges in a directed graph .
- Through these relationships, one can efficiently conduct inference on the random variables in the graph through the use of factors .
- Factors are functions that map a set of variables to a real number, representing the strength of their association.
- Bayesian networks can be used for various tasks, such as classification, diagnosis, prediction, decision making, and learning .

## Inference

- Inference is one key objective in a Bayesian network (BN), and it aims to estimate the posterior distributions of state variables based on evidence (observations).
- Inference can be divided into two types: exact and approximate.
- Exact inference methods compute the exact posterior distributions by exploiting the structure of the BN and applying the rules of probability .
- Exact inference methods include enumeration, variable elimination, and junction tree algorithms .
- Approximate inference methods use sampling or optimization techniques to generate approximate posterior distributions when exact methods are intractable or inefficient .
- Approximate inference methods include stochastic simulation, Markov chain Monte Carlo (MCMC), belief propagation, and variational methods  .

## Bayesian Networks

- A Bayesian network is a directed acyclic graph (DAG) where each node represents a random variable and each edge represents a conditional dependence .
- A Bayesian network encodes a joint probability distribution over the variables in the graph, which can be factorized as follows :

$$
P(X_1, X_2, ..., X_n) = \prod_{i=1}^n P(X_i | Pa(X_i))
$$

- where $Pa(X_i)$ denotes the set of parents of $X_i$ in the graph.
- A Bayesian network also requires a set of conditional probability tables (CPTs) that specify the conditional probabilities of each variable given its parents .
- A Bayesian network can be constructed from data using various methods, such as score-based, constraint-based, or hybrid approaches .
- A Bayesian network can also be updated with new data using Bayesian learning, which applies Bayes' rule to update the parameters of the CPTs .

## References

: https://nikhil-st8.medium.com/approximate-exact-inference-in-bayesian-networks-b682ed19fbbf
: https://towardsdatascience.com/introduction-to-bayesian-networks-81031eeed94e
: https://cs.gmu.edu/~ashehu/sites/default/files/cs580_Spring2018/LecBayesNetsAndInference.pdf
: https://courses.csail.mit.edu/6.034s/handouts/spring12/chapter14_mod_b.pdf