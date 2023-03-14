Natural Language Processing Word2Vec is a technique for learning word embeddings from a large corpus of text using a neural network model. Word embeddings are vector representations of words that capture their semantic and syntactic qualities. Word2Vec consists of two main models: Skip-gram and Continuous Bag of Words (CBOW). Skip-gram predicts the context words given a target word, while CBOW predicts the target word given the context words. Both models use a hidden layer to learn the word embeddings.

The following diagram illustrates the basic architecture of a Skip-gram model:

```
    Input layer: one-hot encoded vector for target word
    Hidden layer: linear projection of input vector
    Output layer: softmax layer to predict probabilities of context words

    +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |
    |   Input layer   |---->|  Hidden layer   |---->|  Output layer   |
    |                 |     |                 |     |                 |
    +-----------------+     +-----------------+     +-----------------+
    | 0 | 0 | 1 | 0 | |     | 0.2 | -0.1 | ...|     | 0.01 | 0.05 | ...|
    +-----------------+     +-----------------+     +-----------------+
      ^                       ^                       ^
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
    Target word: "cat"    Word embedding: w      Context words: "the", "black", ...
```

The following diagram illustrates the basic architecture of a CBOW model:

```
    Input layer: one-hot encoded vectors for context words
    Hidden layer: average of input vectors
    Output layer: softmax layer to predict probability of target word

    +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |
    |   Input layer   |---->|  Hidden layer   |---->|  Output layer   |
    |                 |     |                 |     |                 |
    +-----------------+     +-----------------+     +-----------------+
    | 0 | 1 | 0 | 0 | |     | 0.1 | 0.05 | ...|     | 0.02 | 0.03 | ...|
    | 1 | 0 | 0 | 0 | |     +-----------------+     +-----------------+
    | 0 | 0 | 0 | 1 | |       ^                       ^
    +-----------------+       |                       |
      ^ ^             ^       |                       |
      | |             |       |                       |
      | |             |       |                       |
      | |             |       |                       |
      | |             |       |                       |
      | |             |       |                       |
      | |             |       |                       |
      | |             |       |                       |
      | |             |       |                       |
      | |             |       |                       |
      | |             |       |                       |
      | |             |       |                       |
      | |             |       |                       |
    Context words:     Word embedding: v      Target word: "cat"
    "the", "black", ...
```