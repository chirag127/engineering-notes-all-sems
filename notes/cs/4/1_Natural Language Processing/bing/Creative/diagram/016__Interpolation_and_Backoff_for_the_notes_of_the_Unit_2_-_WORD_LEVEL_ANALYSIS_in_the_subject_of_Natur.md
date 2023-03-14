Interpolation and backoff are two techniques for smoothing n-gram probabilities in natural language processing. They are used to deal with the problem of data sparsity, which occurs when some n-grams are not observed in the training data and thus have zero probability.

Interpolation is a method that combines the probabilities of n-grams of different orders, weighted by some coefficients. For example, the probability of a trigram can be interpolated as:

P(w3|w1,w2) = lambda1 * P(w3|w1,w2) + lambda2 * P(w3|w2) + lambda3 * P(w3)

where lambda1, lambda2 and lambda3 are the interpolation coefficients that sum to one. The coefficients can be estimated using various methods, such as expectation-maximization (EM) or deleted interpolation.

Backoff is a method that uses a lower-order n-gram probability when the higher-order n-gram probability is zero or unreliable. For example, the probability of a trigram can be backed off as:

P(w3|w1,w2) = P(w3|w1,w2) if c(w1,w2,w3) > 0
            = alpha(w1,w2) * P(w3|w2) if c(w1,w2,w3) = 0 and c(w2,w3) > 0
            = alpha(w1,w2) * beta(w2) * P(w3) if c(w1,w2,w3) = 0 and c(w2,w3) = 0

where alpha and beta are the backoff coefficients that adjust the lower-order probabilities. The coefficients can be estimated using various methods, such as absolute discounting or Good-Turing estimation.

The following diagram illustrates the basic architecture of interpolation and backoff for n-gram models:

```
+-----------------+     +-----------------+     +-----------------+
| Unigram Model   |     | Bigram Model    |     | Trigram Model   |
| P(w)            |     | P(w|w-1)        |     | P(w|w-1,w-2)    |
+-----------------+     +-----------------+     +-----------------+
        |                      |                      |
        |                      |                      |
        +----------------------+----------------------+
                               |
                               v
                      +-----------------+
                      | Interpolation   |
                      | P(w|w-1,w-2) =  |
                      | lambda1 * P(w|w-1,w-2) + |
                      | lambda2 * P(w|w-1) +    |
                      | lambda3 * P(w)          |
                      +-----------------+
                               |
                               v
                      +-----------------+
                      | Backoff         |
                      | P(w|w-1,w-2) =  |
                      | P(w|w-1,w-2) if c(w-2,w-1,w) > 0 |
                      | alpha(w-2,w-1) * P(w|w-1) if c(w-2,w-1,w) = 0 and c(w-1,w) > 0 |
                      | alpha(w-2,w-1) * beta(w-1) * P(w) if c(w-2,w-1,w) = 0 and c(w-1,w) = 0 |
                      +-----------------+
                               |
                               v
                      +-----------------+
                      | Smoothed        |
                      | Probability     |
                      | P(w|w-1,w-2)    |
                      +-----------------+
```