# Unsmoothed N-grams

- An **n-gram** is a sequence of **n** words or tokens in a text. For example, "natural language processing" is a **trigram** (n = 3).
- An **n-gram model** is a probabilistic model that estimates the probability of a word given the previous **n - 1** words. For example, P(processing | natural language) is the probability of the word "processing" given the previous bigram "natural language".
- An **unsmoothed n-gram model** is a simple model that uses the **maximum likelihood estimation (MLE)** to calculate the n-gram probabilities based on the **relative frequency** of the n-grams in the training data. For example, P(processing | natural language) = C(natural language processing) / C(natural language), where C is the count function.
- Unsmoothed n-gram models have some advantages and disadvantages:
  - Advantages:
    - They are easy to implement and understand.
    - They can capture some local context and word order information.
    - They can be used for various natural language processing tasks, such as language identification, speech recognition, text generation, etc.
  - Disadvantages:
    - They suffer from **data sparsity** and **overfitting** problems, meaning that they assign zero probability to unseen n-grams and high probability to frequent n-grams, which may not reflect the true language distribution.
    - They require a large amount of training data and memory to store all the possible n-grams and their counts.
    - They make a **Markov assumption** that the current word only depends on the previous n - 1 words, which may not capture the long-range dependencies and semantic relations in natural language.