### Unsmoothed N-grams

- An n-gram is a sequence of n words in a text. For example, "natural language processing" is a trigram (n = 3).
- An n-gram language model is a probabilistic model that predicts the next word in a text based on the previous n-1 words. For example, a bigram model (n = 2) predicts the next word based on the previous word.
- An unsmoothed n-gram model is a simple n-gram model that estimates the probabilities of n-grams based on their frequencies in a training corpus. For example, an unsmoothed unigram model (n = 1) assigns the probability of a word as the number of times it occurs in the corpus divided by the total number of words in the corpus.
- An unsmoothed n-gram model has some limitations, such as:
  - It assigns zero probability to n-grams that do not occur in the training corpus, which leads to data sparsity and poor generalization.
  - It overestimates the probabilities of frequent n-grams and underestimates the probabilities of rare n-grams, which leads to poor performance on unseen data.
  - It does not account for unknown words that may appear in the test data, which leads to out-of-vocabulary errors.
- To overcome these limitations, various smoothing techniques are used to adjust the probabilities of n-grams based on some prior knowledge or assumptions. Some common smoothing techniques are:
  - Add-one (Laplacian) smoothing: This adds one to the count of every n-gram, regardless of whether it occurs in the training corpus or not. This ensures that no n-gram has zero probability, but it also introduces a lot of noise and distortion.
  - Good-Turing smoothing: This adjusts the counts of n-grams based on how many n-grams have the same frequency. This reduces the probability of frequent n-grams and increases the probability of rare n-grams, but it also requires a lot of computation and data.
  - Interpolation: This combines the probabilities of n-grams from different models, such as unigram, bigram, and trigram models, with some weights. This allows the model to use more information from different sources, but it also requires tuning the weights.
  - Backoff: This falls back to a lower-order n-gram model when the higher-order n-gram model does not have enough data. For example, a trigram model may use a bigram model when the trigram does not occur in the training corpus. This reduces the data sparsity problem, but it also introduces some bias.