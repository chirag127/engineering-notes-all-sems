### Interpolation and Backoff

- Interpolation and backoff are two methods for smoothing n-gram probabilities in natural language processing.
- Smoothing is the process of assigning non-zero probabilities to unseen n-grams, and adjusting the probabilities of seen n-grams, to avoid overfitting and sparsity issues.
- Interpolation and backoff are based on the idea of using lower-order n-grams as a backup when higher-order n-grams are unreliable or unavailable.

#### Backoff

- Backoff is a method that uses a higher-order n-gram if it has enough evidence, otherwise it falls back to a lower-order n-gram.
- For example, if we want to estimate the probability of a word w given the previous two words u and v, we can use a trigram model p(w|uv) if it is well-estimated, otherwise we can use a bigram model p(w|v), otherwise we can use a unigram model p(w).
- Backoff requires a discounting factor to reduce the probabilities of seen n-grams, and a weighting factor to distribute the remaining probability mass to unseen n-grams.
- One common backoff method is Katz backoff, which uses a discounting factor based on the frequency of the n-gram, and a weighting factor based on the number of n-grams that share the same context.

#### Interpolation

- Interpolation is a method that combines the probabilities of n-grams of different orders, weighted by some coefficients that sum to one.
- For example, if we want to estimate the probability of a word w given the previous two words u and v, we can use a linear interpolation of the trigram, bigram, and unigram models: p(w|uv) = λ1 p(w|uv) + λ2 p(w|v) + λ3 p(w), where λ1 + λ2 + λ3 = 1.
- Interpolation requires estimating the coefficients λi, which can be done by using a held-out corpus, or by using an expectation-maximization algorithm.
- One common interpolation method is Jelinek-Mercer smoothing, which uses a fixed coefficient for each order of n-gram, and adjusts it based on the domain or genre of the text.

#### Comparison

- In general, interpolation works better than backoff, as it can capture more information from lower-order n-grams, and does not require a threshold for falling back.
- However, interpolation is more computationally expensive, as it requires estimating and storing more parameters, and summing over more n-grams.
- Backoff is simpler and faster, and can be effective for sparse data, especially with a good discounting and weighting scheme.