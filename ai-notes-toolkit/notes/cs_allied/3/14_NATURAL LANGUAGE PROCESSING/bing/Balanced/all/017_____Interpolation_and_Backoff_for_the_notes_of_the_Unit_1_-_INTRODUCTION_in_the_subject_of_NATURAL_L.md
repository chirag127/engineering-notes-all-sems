# Interpolation and Backoff

- Interpolation and backoff are two methods of smoothing language models in natural language processing (NLP).
- Smoothing is a technique to assign non-zero probabilities to unseen events or n-grams, by redistributing some probability mass from seen events or n-grams.
- Interpolation is a method that combines multiple n-gram models, such as unigram, bigram, and trigram, by weighting each contribution so that the result is another probability function.
- Backoff is a method that uses a lower-order n-gram model when the higher-order n-gram model has zero count or probability, by applying a discount factor to the lower-order model.
- Both methods aim to improve the accuracy and generalization of language models, by reducing the data sparsity and overfitting problems.

## Interpolation

- Interpolation can be formulated as follows:

  - Given a word sequence w1, w2, ..., wn, the probability of the next word wn+1 can be estimated by a linear combination of different n-gram models:

    - p(w<sub>n+1</sub>|w<sub>1</sub>, ..., w<sub>n</sub>) = λ<sub>1</sub>p(w<sub>n+1</sub>|w<sub>1</sub>, ..., w<sub>n</sub>) + λ<sub>2</sub>p(w<sub>n+1</sub>|w<sub>2</sub>, ..., w<sub>n</sub>) + ... + λ<sub>n</sub>p(w<sub>n+1</sub>|w<sub>n</sub>) + λ<sub>n+1</sub>p(w<sub>n+1</sub>)

  - Where λ<sub>i</sub> are the interpolation weights that satisfy the following constraints:

    - λ<sub>i</sub> ≥ 0 for all i
    - Σ<sub>i</sub>λ<sub>i</sub> = 1

  - The interpolation weights can be learned from a held-out corpus, which is a separate training corpus that is used to set hyperparameters, by choosing the λ values that maximize the likelihood of the held-out corpus.

- Interpolation can be seen as a way of mixing different sources of information, such as the context and the history, to estimate the probability of the next word.

- Interpolation can also be applied conditionally, by using different weights for different contexts. For example, the weights can depend on the previous word or the part-of-speech tag of the previous word.

- Interpolation can be generalized to any number of n-gram models, such as 4-gram, 5-gram, etc.

## Backoff

- Backoff can be formulated as follows:

  - Given a word sequence w1, w2, ..., wn, the probability of the next word wn+1 can be estimated by using the highest-order n-gram model that has a non-zero count or probability, and applying a discount factor to the lower-order models:

    - p(w<sub>n+1</sub>|w<sub>1</sub>, ..., w<sub>n</sub>) = p(w<sub>n+1</sub>|w<sub>1</sub>, ..., w<sub>n</sub>) if c(w<sub>1</sub>, ..., w<sub>n+1</sub>) > 0
    - p(w<sub>n+1</sub>|w<sub>1</sub>, ..., w<sub>n</sub>) = α<sub>1</sub>p(w<sub>n+1</sub>|w<sub>2</sub>, ..., w<sub>n</sub>) if c(w<sub>1</sub>, ..., w<sub>n+1</sub>) = 0 and c(w<sub>2</sub>, ..., w<sub>n+1</sub>) > 0
    - p(w<sub>n+1</sub>|w<sub>1</sub>, ..., w<sub>n</sub>) = α<sub>1</sub>α<sub>2</sub>p(w<sub>n+1</sub>|w<sub>3</sub>, ..., w<sub>n</sub>) if c(w<sub>1</sub>, ..., w<sub>n+1</sub>) = 0 and c(w<sub>2</sub>, ..., w<sub>n+1</sub>) = 0 and c(w<sub>3</sub>, ...,