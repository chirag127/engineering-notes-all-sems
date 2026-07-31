# Inference and Bayesian Networks

## Introduction

- Bayesian networks are a type of probabilistic graphical model that uses Bayesian inference for probability computations .
- Bayesian networks aim to model conditional dependence, and therefore causation, by representing conditional dependence by edges in a directed graph .
- Through these relationships, one can efficiently conduct inference on the random variables in the graph through the use of factors .
- Bayesian inference is a method of updating beliefs based on evidence using Bayes' theorem .
- Bayes' theorem states that the posterior probability of a hypothesis given some evidence is proportional to the prior probability of the hypothesis and the likelihood of the evidence given the hypothesis .
- Bayesian inference can be used to answer queries about the network, such as the marginal probability of a node, the conditional probability of a node given some evidence, or the most probable explanation for some evidence .

## Exact Inference

- Exact inference is the process of computing the exact posterior probabilities of the nodes in the network given some evidence .
- Exact inference can be done by two main methods: enumeration and variable elimination .
- Enumeration is a brute-force method that sums over all possible assignments of the variables in the network and uses the chain rule to compute the joint probabilities .
- Enumeration is exponential in the number of variables and the size of the largest factor .
- Variable elimination is a more efficient method that exploits the conditional independence properties of the network and eliminates irrelevant variables by summing them out .
- Variable elimination is polynomial in the number of variables and exponential in the size of the largest factor .
- Variable elimination can be improved by choosing a good elimination order and using caching and dynamic programming techniques .

## Approximate Inference

- Approximate inference is the process of computing approximate posterior probabilities of the nodes in the network given some evidence .
- Approximate inference can be done by two main methods: stochastic simulation and Markov chain Monte Carlo (MCMC) .
- Stochastic simulation is a method that generates samples from the network and uses them to estimate the posterior probabilities .
- Stochastic simulation can be done by two main techniques: prior sampling and likelihood weighting .
- Prior sampling is a technique that generates samples from the network by sampling each node according to its prior distribution .
- Prior sampling is simple and fast, but it can be inefficient and inaccurate when the evidence is rare or unlikely .
- Likelihood weighting is a technique that generates samples from the network by sampling each node according to its likelihood given the evidence .
- Likelihood weighting is more efficient and accurate than prior sampling, but it can suffer from sample impoverishment and variance problems when the evidence is complex or contradictory .
- Markov chain Monte Carlo (MCMC) is a method that generates samples from the network by constructing a Markov chain that converges to the posterior distribution .
- MCMC can be done by two main techniques: Gibbs sampling and Metropolis-Hastings sampling .
- Gibbs sampling is a technique that generates samples from the network by sampling each node according to its conditional distribution given the current values of the other nodes .
- Gibbs sampling is simple and easy to implement, but it can be slow to converge and sensitive to initial values .
- Metropolis-Hastings sampling is a technique that generates samples from the network by sampling each node according to a proposal distribution and accepting or rejecting the sample based on a ratio of probabilities .
- Metropolis-Hastings sampling is more flexible and general than Gibbs sampling, but it can be difficult to choose a good proposal distribution and to ensure the chain is ergodic .

## References

: https://nikhil-st8.medium.com/approximate-exact-inference-in-b