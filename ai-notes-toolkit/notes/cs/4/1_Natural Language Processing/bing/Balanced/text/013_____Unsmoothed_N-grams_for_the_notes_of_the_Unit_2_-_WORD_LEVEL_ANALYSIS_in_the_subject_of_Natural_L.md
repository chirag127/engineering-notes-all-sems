### Unsmoothed N-grams

- An n-gram is a sequence of n words or tokens in a text. For example, "natural language processing" is a trigram (n = 3).
- N-grams are used to model the probability of a word given its previous words or context. For example, P(processing | natural language) is the probability of the word "processing" given the previous words "natural language".
- An unsmoothed n-gram model estimates the probability of a word by counting the frequency of the n-gram in the text and dividing it by the frequency of the (n-1)-gram. For example, P(processing | natural language) = C(natural language processing) / C(natural language), where C is the count function.
- Unsmoothed n-gram models have some advantages and disadvantages:
  - Advantages:
    - They are simple and easy to implement.
    - They can capture local dependencies and patterns in the text.
    - They can be used for various tasks in natural language processing, such as text generation, speech recognition, language identification, etc.
  - Disadvantages:
    - They suffer from data sparsity, which means that many n-grams may not occur in the text or have zero counts, leading to zero probabilities and unreliable estimates.
    - They have a high dimensionality, which means that the number of possible n-grams grows exponentially with n and the vocabulary size, making them computationally expensive and memory intensive.
    - They make a strong independence assumption, which means that they only consider the previous n-1 words as the context and ignore the rest of the history, which may not be realistic or sufficient for some tasks.