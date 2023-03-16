# Interpolation and Backoff

- Interpolation and backoff are two methods for smoothing n-gram language models, which are used to estimate the probability of a word given its previous context.
- Smoothing is necessary because n-gram models often encounter unseen or rare events, which can lead to zero or unreliable probabilities.
- Interpolation and backoff are based on the idea of using lower-order n-grams (e.g., bigrams or unigrams) to estimate the probability of higher-order n-grams (e.g., trigrams or quadrigrams) when there is insufficient data.

## Interpolation

- Interpolation is a method that combines the probabilities of n-grams of different orders using weighted coefficients.
- For example, the interpolated probability of a trigram w<sub>i-2</sub>w<sub>i-1</sub>w<sub>i</sub> can be computed as:

  P<sub>interp</sub>(w<sub>i</sub>|w<sub>i-2</sub>w<sub>i-1</sub>) = λ<sub>1</sub>P(w<sub>i</sub>|w<sub>i-2</sub>w<sub>i-1</sub>) + λ<sub>2</sub>P(w<sub>i</sub>|w<sub>i-1</sub>) + λ<sub>3</sub>P(w<sub>i</sub>)

- where λ<sub>1</sub>, λ<sub>2</sub>, and λ<sub>3</sub> are the interpolation coefficients that sum to one.
- The interpolation coefficients can be estimated using various methods, such as maximum likelihood estimation, expectation-maximization, or cross-validation.
- Interpolation has the advantage of using all available information from different n-gram orders, but it also requires more computation and storage.

## Backoff

- Backoff is a method that uses a lower-order n-gram probability only when the higher-order n-gram probability is zero or below a threshold.
- For example, the backoff probability of a trigram w<sub>i-2</sub>w<sub>i-1</sub>w<sub>i</sub> can be computed as:

  P<sub>backoff</sub>(w<sub>i</sub>|w<sub>i-2</sub>w<sub>i-1</sub>) = 
  \begin{cases}
    P(w<sub>i</sub>|w<sub>i-2</sub>w<sub>i-1</sub>), & \text{if } C(w<sub>i-2</sub>w<sub>i-1</sub>w<sub>i</sub>) > 0 \\
    α(w<sub>i-2</sub>w<sub>i-1</sub>)P(w<sub>i</sub>|w<sub>i-1</sub>), & \text{otherwise}
  \end{cases}

- where C(w<sub>i-2</sub>w<sub>i-1</sub>w<sub>i</sub>) is the count of the trigram, and α(w<sub>i-2</sub>w<sub>i-1</sub>) is a discounting factor that ensures the probabilities sum to one.
- The discounting factor can be computed using various methods, such as absolute discounting, Good-Turing, or Kneser-Ney.
- Backoff has the advantage of being simpler and faster than interpolation, but it also discards some information from higher-order n-grams.