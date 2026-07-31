### Interpolation and Backoff

- Interpolation and backoff are two methods of smoothing n-gram language models to deal with data sparsity and generalization problems.
- Interpolation: a linear combination of different order n-grams, weighted by coefficients that sum to one.
  - Example: P(w_i|w_{i-1},w_{i-2}) = \lambda_1 P(w_i|w_{i-1},w_{i-2}) + \lambda_2 P(w_i|w_{i-1}) + \lambda_3 P(w_i)
  - The coefficients can be estimated using held-out data or cross-validation.
  - Interpolation can capture more context from higher-order n-grams, but also use robust counts from lower-order n-grams.
- Backoff: a conditional probability that falls back to a lower order n-gram if the higher order n-gram has zero count.
  - Example: P(w_i|w_{i-1},w_{i-2}) = \begin{cases} P(w_i|w_{i-1},w_{i-2}) & \text{if } c(w_{i-2},w_{i-1},w_i) > 0 \\ \alpha(w_{i-1},w_{i-2}) P(w_i|w_{i-1}) & \text{otherwise} \end{cases}
  - The backoff weight \alpha(w_{i-1},w_{i-2}) can be computed using the probability mass reserved for unseen n-grams.
  - Backoff can avoid assigning zero probability to unseen n-grams, but also use less context for rare n-grams.