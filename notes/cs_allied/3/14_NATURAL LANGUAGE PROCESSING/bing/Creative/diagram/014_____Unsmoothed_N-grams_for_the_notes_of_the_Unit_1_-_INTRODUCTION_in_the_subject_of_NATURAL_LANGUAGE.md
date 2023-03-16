### Unsmoothed N-grams

- An n-gram is a sequence of n words or symbols in a text. For example, "natural language processing" is a trigram (n = 3).
- N-grams are used to model the probability of a word given its previous words in a text. For example, P(processing | natural language) is the probability of the word "processing" following the words "natural language".
- An unsmoothed n-gram model estimates the probability of an n-gram by counting its frequency in a corpus and dividing it by the frequency of its prefix (n-1)-gram. For example, P(processing | natural language) = count(natural language processing) / count(natural language).
- Unsmoothed n-gram models have some drawbacks, such as:
  - They assign zero probability to unseen n-grams, which may occur in new texts.
  - They overestimate the probability of frequent n-grams, which may not reflect the true language distribution.
  - They suffer from data sparsity, which means that there are not enough examples of n-grams in the corpus to estimate their probabilities accurately.
- To overcome these drawbacks, smoothed n-gram models are used, which add some probability mass to unseen n-grams and subtract some from seen n-grams. There are different smoothing techniques, such as Laplace smoothing, Good-Turing smoothing, Kneser-Ney smoothing, etc.