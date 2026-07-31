# Interpolation and Backoff

- Interpolation and backoff are two methods of smoothing n-gram language models to deal with data sparsity and generalization problems.
- Interpolation: a linear combination of n-gram probabilities with different orders, weighted by coefficients that sum to one.
- Backoff: a conditional probability that falls back to a lower-order n-gram if the higher-order n-gram has zero count or low confidence.
- In general, interpolation works better than backoff, but requires more computation and parameter tuning.
- There are different ways of estimating the interpolation coefficients, such as held-out interpolation, deleted interpolation, or expectation-maximization (EM) algorithm.
- There are different ways of implementing the backoff strategy, such as Katz backoff, Witten-Bell backoff, or Kneser-Ney smoothing.