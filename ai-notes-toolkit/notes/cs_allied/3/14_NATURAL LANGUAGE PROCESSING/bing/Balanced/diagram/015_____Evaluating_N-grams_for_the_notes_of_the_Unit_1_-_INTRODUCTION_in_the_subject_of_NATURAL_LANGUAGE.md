### Evaluating N-grams for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- N-grams are sequences of N words that are used to model the probability of a word given its previous words in a text  .
- N-grams are also called unigrams (N=1), bigrams (N=2), trigrams (N=3), and so on .
- For example, the sentence "Natural language processing is fun" can be divided into the following n-grams:

  - Unigrams: "Natural", "language", "processing", "is", "fun"
  - Bigrams: "Natural language", "language processing", "processing is", "is fun"
  - Trigrams: "Natural language processing", "language processing is", "processing is fun"

- N-grams are widely used in statistical natural language processing for various tasks, such as speech recognition, parsing, machine translation, text summarization, etc .
- N-grams can be extracted from a text corpus using various methods, such as sliding window, skip-grams, or fixed-length n-grams .
- N-grams can be evaluated based on their frequency, likelihood, or information content in a text corpus .
- Some common metrics for evaluating n-grams are:

  - Count: The number of times an n-gram occurs in a text corpus.
  - Probability: The fraction of times an n-gram occurs in a text corpus, relative to the total number of n-grams of the same length.
  - Conditional probability: The fraction of times an n-gram occurs in a text corpus, given its previous (N-1) words.
  - Perplexity: The inverse of the average probability of an n-gram in a text corpus, which measures how well an n-gram model predicts the next word.
  - Mutual information: The amount of information an n-gram provides about its previous (N-1) words, which measures how much an n-gram reduces the uncertainty of the next word.
  - Log-likelihood ratio: The ratio of the probability of an n-gram under two different models, which measures how much an n-gram deviates from the expected frequency.
  - Chi-square test: A statistical test that compares the observed and expected frequencies of an n-gram, which measures how significant an n-gram is in a text corpus.

- N-grams have some advantages and disadvantages for natural language processing, such as:

  - Advantages:

    - N-grams are simple and easy to implement and compute.
    - N-grams can capture local and sequential patterns in a text corpus.
    - N-grams can be used to generate or complete sentences based on probabilities.

  - Disadvantages:

    - N-grams are sensitive to data sparsity and require large text corpora to estimate reliable probabilities.
    - N-grams are limited by the fixed window size and cannot capture long-range dependencies or semantic relations in a text corpus.
    - N-grams are prone to overfitting and require smoothing or pruning techniques to avoid zero probabilities or reduce noise.