# Inference and Bayesian Networks

## Introduction

- Bayesian networks are a type of probabilistic graphical model that uses Bayesian inference for probability computations .
- Bayesian networks aim to model conditional dependence, and therefore causation, by representing conditional dependence by edges in a directed graph .
- Through these relationships, one can efficiently conduct inference on the random variables in the graph through the use of factors .
- Factors are functions that map a set of variables to a real number, representing the strength of their association.
- Bayesian networks can be used for various tasks such as reasoning, prediction, diagnosis, decision making, and learning.

## Inference

- Inference is one key objective in a Bayesian network (BN), and it aims to estimate the posterior distributions of state variables based on evidence (observations).
- Inference can be classified into two types: exact and approximate.
- Exact inference methods compute the exact posterior distributions by exploiting the structure of the BN and applying the rules of probability theory .
- Exact inference methods include enumeration, variable elimination, and junction tree algorithms .
- Approximate inference methods use sampling or optimization techniques to generate approximate posterior distributions when exact methods are intractable or inefficient .
- Approximate inference methods include stochastic simulation, Markov chain Monte Carlo (MCMC), belief propagation, and variational methods  .

## Example

- Consider the following BN that models the relationship between the weather (W), the sprinkler (S), the grass (G), and the dog (D):

![BN example](https://miro.medium.com/max/1400/1*Q2Z1fL6n5R4w0y4wQy1x1w.png)

- The BN encodes the following conditional probabilities:

P(W) = 0.6 (sunny), 0.4 (rainy)

P(S|W) = 0.8 (on), 0.2 (off) if W = sunny

P(S|W) = 0.1 (on), 0.9 (off) if W = rainy

P(G|W,S) = 0.95 (wet), 0.05 (dry) if W = rainy or S = on

P(G|W,S) = 0.1 (wet), 0.9 (dry) if W = sunny and S = off

P(D|G) = 0.9 (happy), 0.1 (sad) if G = wet

P(D|G) = 0.4 (happy), 0.6 (sad) if G = dry

- Suppose we want to infer the probability of the dog being happy given that the grass is wet, i.e., P(D = happy | G = wet).
- Using the enumeration method, we can compute this probability by summing over all possible values of W and S:

P(D = happy | G = wet) = P(D = happy, G = wet) / P(G = wet)

P(D = happy, G = wet) = P(D = happy | G = wet) * P(G = wet)

P(G = wet) = P(G = wet | W = sunny, S = on) * P(W = sunny) * P(S = on | W = sunny) + P(G = wet | W = sunny, S = off) * P(W = sunny) * P(S = off | W = sunny) + P(G = wet | W = rainy, S = on) * P(W = rainy) * P(S = on | W = rainy) + P(G = wet | W = rainy, S = off) * P(W = rainy) * P(S = off | W = rainy)

P(D = happy, G = wet) = P(D = happy | G = wet) * (P(G = wet | W = sunny, S = on) * P(W = sunny) * P(S = on | W = sunny) + P(G = wet | W = sunny, S = off) * P(W = sunny) * P(S = off | W = sunny) + P(G = wet | W = rainy, S = on) * P(W = rainy) * P(S = on | W = rainy