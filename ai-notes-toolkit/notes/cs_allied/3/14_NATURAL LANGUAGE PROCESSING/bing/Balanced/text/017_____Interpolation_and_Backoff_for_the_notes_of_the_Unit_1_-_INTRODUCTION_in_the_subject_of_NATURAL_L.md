### Interpolation and Backoff

- Interpolation and backoff are two methods for smoothing n-gram language models, which are used to estimate the probability of a word given its previous n-1 words in a sequence.
- Smoothing is necessary to deal with the problem of data sparsity, which occurs when some n-grams are not observed in the training data, resulting in zero probabilities that can affect the performance of language models.
- Interpolation is a method that combines the probabilities of n-grams of different orders, such as unigrams, bigrams, and trigrams, using some weights that sum to one. For example, the interpolated trigram probability can be written as:

    P(w_i|w_{i-2},w_{i-1}) = \lambda_1 P(w_i|w_{i-2},w_{i-1}) + \lambda_2 P(w_i|w_{i-1}) + \lambda_3 P(w_i)

- The weights \lambda_1, \lambda_2, and \lambda_3 can be estimated using various methods, such as maximum likelihood estimation, expectation-maximization, or cross-validation. Interpolation can capture both long-range and short-range dependencies between words, and can assign non-zero probabilities to unseen n-grams by using lower-order n-grams.
- Backoff is a method that uses a lower-order n-gram probability only when the higher-order n-gram probability is zero or unreliable. For example, the backoff trigram probability can be written as:

    P(w_i|w_{i-2},w_{i-1}) = \begin{cases} P(w_i|w_{i-2},w_{i-1}), & \text{if } C(w_{i-2},w_{i-1},w_i) > 0 \\ \alpha(w_{i-2},w_{i-1}) P(w_i|w_{i-1}), & \text{otherwise} \end{cases}

- The function \alpha(w_{i-2},w_{i-1}) is a discounting factor that adjusts the lower-order probability to preserve the total probability mass. Backoff can avoid relying on unreliable estimates based on sparse data, and can also assign non-zero probabilities to unseen n-grams by using lower-order n-grams.
- In general, interpolation works better than backoff, as it can use more information from different n-gram orders. However, backoff is simpler and faster to implement, and can also achieve good results in combination with smoothing techniques.