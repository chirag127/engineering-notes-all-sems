Natural Language Processing (NLP) is the field of computer science that deals with analyzing, understanding and generating natural language. Word2Vec is a technique for NLP that learns word embeddings from a large corpus of text. Word embeddings are numerical representations of words that capture their semantic and syntactic features. Word2Vec uses a neural network model to learn word embeddings in an unsupervised way.

The following diagram illustrates the basic architecture of a Word2Vec model:

```
+-----------------+     +-----------------+     +-----------------+
| Input Layer     |     | Hidden Layer    |     | Output Layer    |
| One-hot vectors | --> | Linear layer    | --> | Softmax layer   |
| of words        |     | of neurons      |     | of probabilities|
+-----------------+     +-----------------+     +-----------------+
```

The input layer consists of one-hot vectors of words in the corpus. A one-hot vector is a vector that has only one element as 1 and the rest as 0. For example, if the vocabulary size is 10,000, then the word "cat" might be represented as [0, 0, 0, ..., 0, 1, 0, ..., 0] where the 1 is in the position corresponding to the word "cat" in the vocabulary.

The hidden layer is a linear layer of neurons that projects the input vectors into a lower-dimensional space. The number of neurons in the hidden layer determines the size of the word embeddings. For example, if the hidden layer has 300 neurons, then each word will be represented by a 300-dimensional vector.

The output layer is a softmax layer that computes the probabilities of each word in the vocabulary given the input word. The softmax layer is a nonlinear layer that normalizes the output of the hidden layer to sum to 1. The softmax layer is used to train the model using the cross-entropy loss function.

There are two variants of Word2Vec: skip-gram and continuous bag-of-words (CBOW). The skip-gram model predicts the context words given the target word, while the CBOW model predicts the target word given the context words. The context words are the words that appear within a fixed window around the target word in the corpus. For example, if the window size is 2, then the context words for the word "dog" in the sentence "The cat chased the dog away" are "cat", "chased", "away".

The following diagram illustrates the skip-gram model:

```
+-----------------+     +-----------------+     +-----------------+
| Input Layer     |     | Hidden Layer    |     | Output Layer    |
| One-hot vector  | --> | Linear layer    | --> | Softmax layer   |
| of target word  |     | of neurons      |     | of probabilities|
+-----------------+     +-----------------+     +-----------------+
  |                                                    ^
  |                                                    |
  +------------------------> Predict context words <---+
```

The following diagram illustrates the CBOW model:

```
+-----------------+     +-----------------+     +-----------------+
| Input Layer     |     | Hidden Layer    |     | Output Layer    |
| One-hot vectors | --> | Linear layer    | --> | Softmax layer   |
| of context words|     | of neurons      |     | of probabilities|
+-----------------+     +-----------------+     +-----------------+
  |                                                    ^
  |                                                    |
  +------------------------> Predict target word <-----+
```

Word2Vec models can be trained using stochastic gradient descent (SGD) or other optimization algorithms. The models can also be improved by using negative sampling or hierarchical softmax to reduce the computational cost of the softmax layer. Word2Vec models can be used for various NLP tasks, such as word similarity, word analogy, text classification, sentiment analysis, etc.