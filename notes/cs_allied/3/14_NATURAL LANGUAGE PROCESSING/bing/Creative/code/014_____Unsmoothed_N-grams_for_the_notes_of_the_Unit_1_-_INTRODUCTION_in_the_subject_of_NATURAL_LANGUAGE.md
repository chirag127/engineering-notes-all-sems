### Unsmoothed N-grams

- An n-gram is a sequence of n words or tokens in a text. For example, "natural language processing" is a trigram (n = 3).
- N-grams are used to model the probability of a word given its previous words or context. For example, P(processing | natural language) is the probability of the word "processing" given the previous words "natural language".
- An unsmoothed n-gram model estimates the probability of a word by counting the frequency of the n-gram in the text and dividing it by the frequency of the (n-1)-gram. For example, P(processing | natural language) = C(natural language processing) / C(natural language), where C is the count function.
- Unsmoothed n-gram models have some limitations, such as:
  - They are sensitive to data sparsity, meaning that they assign zero probability to unseen n-grams, which may not reflect the true probability.
  - They suffer from overfitting, meaning that they memorize the training data and do not generalize well to new data.
  - They do not account for the variability of natural language, meaning that they assume that the probability of a word depends only on a fixed number of previous words, which may not capture the long-range dependencies or the semantic and syntactic relations in the text.
- To overcome these limitations, smoothed n-gram models are used, which apply various techniques to adjust the probabilities of n-grams based on their frequency, length, and context. Some examples of smoothing techniques are Laplace smoothing, Good-Turing smoothing, Kneser-Ney smoothing, etc.