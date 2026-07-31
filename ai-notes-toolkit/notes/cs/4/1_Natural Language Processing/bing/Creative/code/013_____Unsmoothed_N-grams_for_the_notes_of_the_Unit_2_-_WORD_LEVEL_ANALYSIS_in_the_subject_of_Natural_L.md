# Unsmoothed N-grams

- An n-gram is a sequence of n words or tokens in a text. For example, "natural language processing" is a trigram (n = 3).
- An n-gram model is a probabilistic model that estimates the probability of a word given the previous n-1 words. For example, P(processing | natural language) is the probability of the word "processing" given the previous bigram "natural language".
- An unsmoothed n-gram model is a simple way of estimating the n-gram probabilities by counting the frequencies of n-grams in a corpus and dividing by the frequencies of (n-1)-grams. For example, P(processing | natural language) = C(natural language processing) / C(natural language), where C() is the count function.
- Unsmoothed n-gram models have some advantages and disadvantages:
  - Advantages:
    - They are easy to implement and understand.
    - They can capture local dependencies and patterns in the text.
    - They can be used for various tasks in natural language processing, such as language modeling, text generation, speech recognition, etc.
  - Disadvantages:
    - They suffer from data sparsity, meaning that many n-grams may have zero counts in the corpus, leading to zero probabilities and poor generalization.
    - They are sensitive to the choice of n, meaning that different values of n may result in different performance and complexity.
    - They make the Markov assumption, meaning that they ignore the long-range dependencies and context beyond the previous n-1 words.