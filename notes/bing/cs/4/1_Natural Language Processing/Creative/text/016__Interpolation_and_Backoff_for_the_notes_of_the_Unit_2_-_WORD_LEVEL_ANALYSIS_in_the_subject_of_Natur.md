### Interpolation and Backoff

- Interpolation and backoff are two methods for smoothing n-gram language models, which are used to estimate the probability of a word given its previous words in a sequence.
- Smoothing is necessary because n-gram models often encounter unseen or rare n-grams in new data, which would have zero or very low probability, leading to poor performance.
- Interpolation and backoff are both based on the idea of using lower-order n-grams (such as bigrams or unigrams) to estimate the probability of higher-order n-grams (such as trigrams or four-grams) when the latter are not observed or reliable enough in the training data.

#### Interpolation

- Interpolation is a method that combines the probabilities of n-grams of different orders using weighted coefficients that sum to one.
- For example, the interpolated probability of a trigram w1 w2 w3 can be computed as:

  P(w3 | w1 w2) = λ1 P(w3 | w1 w2) + λ2 P(w3 | w2) + λ3 P(w3)

  where λ1, λ2, and λ3 are the interpolation coefficients that satisfy λ1 + λ2 + λ3 = 1.

- The interpolation coefficients can be estimated using various methods, such as maximum likelihood estimation, expectation-maximization, or held-out data.
- Interpolation has the advantage of using all the available information from different n-gram orders, but it also has the disadvantage of requiring more parameters and computation.

#### Backoff

- Backoff is a method that uses lower-order n-grams only when higher-order n-grams are not observed or reliable enough in the training data.
- For example, the backoff probability of a trigram w1 w2 w3 can be computed as:

  P(w3 | w1 w2) = 
  - P(w3 | w1 w2) if C(w1 w2 w3) > 0
  - α(w1 w2) P(w3 | w2) if C(w1 w2 w3) = 0 and C(w2 w3) > 0
  - α(w1 w2) α(w2) P(w3) if C(w1 w2 w3) = 0 and C(w2 w3) = 0

  where C(w1 w2 w3) is the count of the trigram w1 w2 w3 in the training data, and α(w1 w2) and α(w2) are the backoff coefficients that discount the lower-order probabilities.

- The backoff coefficients can be estimated using various methods, such as absolute discounting, Kneser-Ney smoothing, or Good-Turing estimation.
- Backoff has the advantage of using fewer parameters and computation, but it also has the disadvantage of ignoring some information from higher-order n-grams.