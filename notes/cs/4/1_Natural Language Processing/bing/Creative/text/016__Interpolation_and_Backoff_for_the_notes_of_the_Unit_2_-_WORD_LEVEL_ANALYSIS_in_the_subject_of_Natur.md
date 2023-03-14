### Interpolation and Backoff

- Interpolation and backoff are two methods for smoothing n-gram language models, which assign probabilities to sequences of words based on their frequency in a corpus.
- Smoothing is necessary because many n-grams, especially those with longer context, may not occur in the training data, leading to zero probabilities and poor generalization.
- Interpolation is a method that combines the probabilities of n-grams of different orders, such as unigrams, bigrams, and trigrams, using some weights that sum to one. For example, the probability of a trigram w1 w2 w3 can be interpolated as:

P(w3|w1 w2) = λ1 P(w3|w1 w2) + λ2 P(w3|w2) + λ3 P(w3)

where λ1, λ2, and λ3 are the interpolation weights that satisfy λ1 + λ2 + λ3 = 1.

- The interpolation weights can be estimated using various methods, such as maximum likelihood, expectation maximization, or held-out data.
- Interpolation has the advantage of using all the available information from different n-gram orders, but it also requires more computation and storage.
- Backoff is a method that uses a lower-order n-gram probability when the higher-order n-gram probability is zero or unreliable. For example, the probability of a trigram w1 w2 w3 can be backed off as:

P(w3|w1 w2) = 
  if C(w1 w2 w3) > 0: P(w3|w1 w2)
  elif C(w2 w3) > 0: α(w1 w2) P(w3|w2)
  else: α(w1 w2) α(w2) P(w3)

where C(w1 w2 w3) is the count of the trigram w1 w2 w3 in the corpus, and α(w1 w2) and α(w2) are the backoff weights that adjust the lower-order probabilities to sum to one.
- The backoff weights can be estimated using various methods, such as deleted interpolation, Good-Turing, or Katz smoothing.
- Backoff has the advantage of being simpler and faster than interpolation, but it also discards some information from the higher-order n-grams.