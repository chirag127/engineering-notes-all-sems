### Unsmoothed N-grams

- N-grams are a type of probabilistic language model used in natural language processing.
- An N-gram model predicts the probability of the next word in a sequence based on the previous N-1 words.
- Unsmoothed N-grams do not use any smoothing techniques to adjust the probabilities of unseen N-grams.
- This can result in zero probabilities for unseen N-grams, which can cause problems when trying to calculate the probability of a sentence or document.
- One solution to this problem is to use smoothing techniques, such as Laplace smoothing or Good-Turing smoothing, to adjust the probabilities of unseen N-grams.
- However, unsmoothed N-grams can still be useful in certain situations, such as when working with small amounts of data or when the data is highly predictable.
- Unsmoothed N-grams can also be used as a baseline for comparison with smoothed N-gram models.
