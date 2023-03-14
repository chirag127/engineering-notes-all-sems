### Interpolation and Backoff for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

- Interpolation and backoff are two methods of smoothing probability estimates for n-gram language models.
- Smoothing is needed to deal with data sparsity, which is the problem of having zero counts for some n-grams in the training data, but not in the test data.
- Interpolation is a method of combining probability estimates from different orders of n-grams, such as unigrams, bigrams, and trigrams, with some weights.
- Backoff is a method of using lower-order n-grams when higher-order n-grams have zero counts, with some discounts.
- Both methods aim to improve the accuracy and generalization of the language model.

#### Interpolation

- Interpolation is based on the idea that a higher-order n-gram probability can be estimated by a linear combination of lower-order n-gram probabilities.
- For example, a trigram probability p(w3|w1w2) can be interpolated as:

  p(w3|w1w2) = λ1p(w3|w1w2) + λ2p(w3|w2) + λ3p(w3)

- Where λ1, λ2, and λ3 are the interpolation weights that sum to one.
- The interpolation weights can be estimated by maximizing the likelihood of a held-out set of data, or by using some heuristics, such as the deleted interpolation method.
- Interpolation can also be applied recursively, such as:

  p(w3|w1w2) = λ1p(w3|w1w2) + (1 - λ1)p(w3|w2)
  p(w3|w2) = λ2p(w3|w2) + (1 - λ2)p(w3)

- Interpolation has the advantage of always using all the available information from different n-gram orders, and avoiding zero probabilities.
- Interpolation has the disadvantage of requiring more computation and storage, and being sensitive to the choice of interpolation weights.

#### Backoff

- Backoff is based on the idea that a higher-order n-gram probability can be approximated by a lower-order n-gram probability when the higher-order n-gram has zero count in the training data.
- For example, a trigram probability p(w3|w1w2) can be backed off to a bigram probability p(w3|w2) when c(w1w2w3) = 0, where c is the count function.
- However, simply backing off to a lower-order n-gram probability can introduce bias and inconsistency, since the lower-order n-gram probabilities may not sum to one when conditioned on the higher-order n-gram context.
- Therefore, backoff methods usually apply some discounts to the higher-order n-gram probabilities, and some normalization factors to the lower-order n-gram probabilities, to ensure that the resulting probabilities are well-defined and consistent.
- For example, a discounted trigram probability can be defined as:

  p*(w3|w1w2) = (c(w1w2w3) - d) / c(w1w2)

- Where d is a discount factor that reduces the probability mass of the observed n-grams.
- A normalized bigram probability can be defined as:

  p*(w3|w2) = α(w1w2)p(w3|w2)

- Where α(w1w2) is a normalization factor that increases the probability mass of the unobserved n-grams, and is computed as:

  α(w1w2) = d / c(w1w2) * N1+(w1w2.)

- Where N1+(w1w2.) is the number of unique words that follow the bigram context w1w2 in the training data.
- A backoff trigram probability can be defined as:

  pBO(w3|w1w2) = p*(w3|w1w2) if c(w1w2w3) > 0
  pBO(w3|w1w2) = β(w1w2)p*(w3|w2) if c(w1w2w3) = 0

- Where β(w1w2) is a backoff weight that ensures that the backoff probabilities sum to one, and is computed as:

  β(w1w2) = (1 - Σw3p*(w3|w1w2)) / (