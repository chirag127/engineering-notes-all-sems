### Unsmoothed N-grams

- An n-gram is a sequence of n words or tokens in a text. For example, "natural language processing" is a trigram (n = 3).
- An n-gram model is a probabilistic model that estimates the probability of a word or token given the previous n-1 words or tokens. For example, P(processing | natural language) is the probability of the word "processing" given the previous bigram "natural language".
- An unsmoothed n-gram model is a simple n-gram model that uses the maximum likelihood estimation (MLE) to calculate the probabilities. For example, P(processing | natural language) = C(natural language processing) / C(natural language), where C is the count of the n-gram in the text.
- Unsmoothed n-gram models have some advantages and disadvantages:
  - Advantages:
    - They are easy to implement and understand.
    - They can capture local dependencies and patterns in the text.
    - They can be used for various natural language processing tasks, such as language modeling, text generation, speech recognition, etc.
  - Disadvantages:
    - They suffer from data sparsity, which means that many n-grams may have zero counts or very low frequencies in the text, leading to unreliable or zero probabilities.
    - They suffer from overfitting, which means that they may memorize the n-grams in the training text and fail to generalize to unseen or new texts.
    - They suffer from the curse of dimensionality, which means that the number of possible n-grams grows exponentially with the length of n and the size of the vocabulary, making the model computationally expensive and inefficient.