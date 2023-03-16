Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of evaluating n-grams for the notes of the unit 2 - word level analysis in the subject of natural language processing.

### Evaluating N-grams

- N-grams are sequences of n words that are used to model the probability of a word given its previous words in a text.
- N-grams are useful for various natural language processing tasks, such as speech recognition, machine translation, text summarization, etc.
- However, n-grams have some limitations and challenges that need to be evaluated and addressed, such as data sparsity, smoothing, perplexity, etc.

#### Data sparsity

- Data sparsity refers to the problem of having insufficient data to estimate the probabilities of n-grams accurately.
- Data sparsity occurs when some n-grams are rare or unseen in the training data, but may appear in the test data, leading to zero or low probabilities and poor performance.
- Data sparsity can be mitigated by using various techniques, such as:

  - Back-off: using lower-order n-grams when higher-order n-grams are not available.
  - Interpolation: combining the probabilities of different n-grams with different weights.
  - Discounting: reducing the probabilities of observed n-grams to allocate some probability mass to unseen n-grams.

#### Smoothing

- Smoothing is a general term for any technique that modifies the probabilities of n-grams to avoid zero or low probabilities and improve the generalization ability of the model.
- Smoothing can be seen as a form of regularization that prevents overfitting to the training data and improves the performance on the test data.
- Smoothing can be done by using various methods, such as:

  - Additive smoothing: adding a small constant to the counts of n-grams before computing the probabilities.
  - Good-Turing smoothing: adjusting the counts of n-grams based on their frequency in the training data.
  - Kneser-Ney smoothing: using the relative frequency of n-grams as a measure of their informativeness and discounting the probabilities accordingly.

#### Perplexity

- Perplexity is a measure of how well a probabilistic model predicts a sample of text.
- Perplexity is defined as the inverse of the average probability of each word in the text, raised to the power of the number of words.
- Perplexity can be used to compare and evaluate different n-gram models, with lower perplexity indicating a better fit to the data.
- Perplexity can be computed by using the following formula:

  - Perplexity(W) = P(w1, w2, ..., wn)^(-1/n) = (product of P(wi|wi-1, ..., wi-n+1))^(-1/n) for i = 1 to n
  - where W is the sequence of words, P is the probability function, and n is the order of the n-gram model.