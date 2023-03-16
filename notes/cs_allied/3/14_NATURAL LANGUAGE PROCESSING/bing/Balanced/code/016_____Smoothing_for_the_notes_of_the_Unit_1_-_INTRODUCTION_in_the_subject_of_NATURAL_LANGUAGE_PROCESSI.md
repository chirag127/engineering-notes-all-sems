### Smoothing

- Smoothing is the process of flattening a probability distribution implied by a language model so that all reasonable word sequences can occur with some probability .
- Smoothing often involves broadening the distribution by redistributing weight from high probability regions to zero probability regions .
- Smoothing is very important in natural language processing, as some words may have zero or close to zero probabilities such as the out-of-vocabulary words (words that do not exist in the vocabulary), but the same rare words may not have the same values in test data.
- Smoothing techniques in NLP are used to address scenarios related to determining probability / likelihood estimate of a sequence of words (say, a sentence) occurring together when one or more words individually (unigram) or N-grams such as bigram or trigram in the given set have never occurred in the past.
- Smoothing can help performance whenever data sparsity is an issue, and data sparsity is almost always an issue in statistical modeling.
- Smoothing can also allow expanding the model, such as by moving to a higher n-gram model, to improve the accuracy of the language model.
- Some common smoothing techniques are:
  - Additive smoothing (also known as Laplace smoothing): adding a small constant to all counts, usually 1.
  - Backoff smoothing: using lower order n-grams when higher order n-grams have zero counts.
  - Interpolation smoothing: combining different order n-grams with different weights.
  - Kneser-Ney smoothing: using a modified count that discounts the probability of n-grams that occur frequently and increases the probability of n-grams that occur rarely.
  - Good-Turing smoothing: using a formula to estimate the probability of unseen n-grams based on the frequency of n-grams that occur once.