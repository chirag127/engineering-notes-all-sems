# Interpolation and Backoff

- Interpolation and backoff are two methods for smoothing n-gram language models in natural language processing.
- N-gram language models assign probabilities to sequences of words based on their frequency in a corpus of text.
- Smoothing is a technique to deal with the problem of data sparseness, which occurs when some n-grams are not observed in the training data, but may appear in the test data.
- Interpolation and backoff are both based on the idea of using lower-order n-grams to estimate the probabilities of higher-order n-grams when there is insufficient evidence for the latter.

## Interpolation

- Interpolation is a method that combines the probabilities of n-grams of different orders using weighted coefficients that sum to one.
- For example, a trigram interpolation model can be written as:

$$P(w_i|w_{i-2}w_{i-1}) = \lambda_1 P(w_i|w_{i-2}w_{i-1}) + \lambda_2 P(w_i|w_{i-1}) + \lambda_3 P(w_i)$$

- Where $\lambda_1$, $\lambda_2$, and $\lambda_3$ are the interpolation coefficients that satisfy $\lambda_1 + \lambda_2 + \lambda_3 = 1$.
- The coefficients can be learned from a held-out corpus using various methods, such as maximum likelihood estimation or expectation-maximization algorithm.
- Interpolation has the advantage of using all the available information from different n-gram orders, but it also requires more computation and storage.

## Backoff

- Backoff is a method that uses a lower-order n-gram model when the higher-order n-gram model has zero probability or low confidence.
- For example, a trigram backoff model can be written as:

$$P(w_i|w_{i-2}w_{i-1}) = \begin{cases} P(w_i|w_{i-2}w_{i-1}), & \text{if } C(w_{i-2}w_{i-1}w_i) > 0 \\ \alpha(w_{i-2}w_{i-1})P(w_i|w_{i-1}), & \text{otherwise} \end{cases}$$

- Where $C(w_{i-2}w_{i-1}w_i)$ is the count of the trigram $w_{i-2}w_{i-1}w_i$ in the training data, and $\alpha(w_{i-2}w_{i-1})$ is a discounting factor that ensures the probabilities sum to one.
- The discounting factor can be computed using various methods, such as Good-Turing estimation or Kneser-Ney smoothing.
- Backoff has the advantage of being simpler and faster than interpolation, but it also discards some information from higher-order n-grams.