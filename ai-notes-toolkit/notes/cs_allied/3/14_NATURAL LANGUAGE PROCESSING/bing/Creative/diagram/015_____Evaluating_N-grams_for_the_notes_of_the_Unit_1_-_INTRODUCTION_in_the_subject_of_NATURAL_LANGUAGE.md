### Evaluating N-grams

- N-grams are sequences of n words or tokens that are used to model language and capture the probability of a word given its previous n-1 words.
- N-grams are often used to estimate the likelihood of a sentence or a document by multiplying the probabilities of each n-gram in the sequence.
- N-grams can be evaluated based on different criteria, such as:
  - Coverage: how well the n-grams represent the language or the domain of interest. This can be measured by the percentage of n-grams in a test set that are also present in a training set.
  - Perplexity: how well the n-grams predict the next word in a sequence. This can be measured by the inverse of the average probability of each word in a test set given its previous n-1 words.
  - Smoothness: how well the n-grams handle unseen or rare words. This can be achieved by adding a small constant to the counts of each n-gram or by interpolating the probabilities of different n-grams.
  - Coherence: how well the n-grams capture the meaning and the structure of the language. This can be measured by the semantic and syntactic similarity of the n-grams to the human-generated texts.