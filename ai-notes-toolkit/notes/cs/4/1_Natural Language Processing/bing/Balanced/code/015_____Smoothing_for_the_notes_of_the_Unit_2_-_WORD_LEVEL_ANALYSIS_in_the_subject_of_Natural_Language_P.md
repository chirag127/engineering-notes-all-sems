### Smoothing

- Smoothing is the process of flattening a probability distribution implied by a language model so that all reasonable word sequences can occur with some probability .
- Smoothing often involves broadening the distribution by redistributing weight from high probability regions to zero probability regions .
- Smoothing is very important in natural language processing, as some words may have zero or close to zero probabilities such as the out-of-vocabulary words (words that do not exist in the vocabulary), but the same rare words may not have the same values in test data.
- Smoothing techniques in NLP are used to address scenarios related to determining probability / likelihood estimate of a sequence of words (say, a sentence) occurring together when one or more words individually (unigram) or N-grams such as bigram or trigram in the given set have never occurred in the past.
- Smoothing can help performance whenever data sparsity is an issue, and data sparsity is almost always an issue in statistical modeling.
- Some common smoothing techniques are:
  - Additive smoothing: adding a small constant to all N-gram counts.
  - Backoff smoothing: using lower order N-grams when higher order N-grams have zero counts.
  - Interpolation smoothing: combining N-gram probabilities with different weights.
  - Kneser-Ney smoothing: using a modified count that discounts the probability of seen N-grams and assigns some probability mass to unseen N-grams.