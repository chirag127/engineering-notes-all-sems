### Interpolation and Backoff

- Interpolation and backoff are two techniques to smooth the probabilities of n-grams in natural language processing (NLP).
- N-grams are sequences of n words that are used to model the language and predict the next word given some context.
- However, n-grams suffer from data sparsity, meaning that some n-grams may not occur in the training data, leading to zero probabilities and poor generalization.
- To overcome this problem, interpolation and backoff use lower-order n-grams to estimate the probabilities of higher-order n-grams that are unseen or rare in the data.

#### Interpolation

- Interpolation is a technique that combines the probabilities of n-grams of different orders using some weights that sum to one.
- For example, the probability of a trigram p(w3|w1,w2) can be interpolated as:

  p(w3|w1,w2) = λ1 p(w3|w1,w2) + λ2 p(w3|w2) + λ3 p(w3)

  where λ1, λ2, and λ3 are the interpolation weights that satisfy λ1 + λ2 + λ3 = 1.

- The weights can be learned from a held-out corpus or optimized using some criteria such as perplexity or likelihood.
- Interpolation can be applied recursively, such that the lower-order n-grams are also interpolated using their lower-order n-grams, and so on.
- Interpolation has the advantage of using all the available information from the n-grams of different orders, but it also has the disadvantage of requiring more parameters and computation.

#### Backoff

- Backoff is a technique that uses the probability of a lower-order n-gram only when the higher-order n-gram is not observed in the data.
- For example, the probability of a trigram p(w3|w1,w2) can be backed off as:

  p(w3|w1,w2) = { p(w3|w1,w2) if count(w1,w2,w3) > 0
                α(w1,w2) p(w3|w2) otherwise

  where α(w1,w2) is a backoff weight that ensures the probabilities sum to one.

- The backoff weight can be computed based on the frequency of the n-grams or estimated using some discounting methods such as Good-Turing or Kneser-Ney.
- Backoff can be applied recursively, such that the lower-order n-grams are also backed off using their lower-order n-grams, and so on.
- Backoff has the advantage of using fewer parameters and computation, but it also has the disadvantage of ignoring some information from the higher-order n-grams.