### WSD using Supervised

- Word Sense Disambiguation (WSD) is the task of identifying the correct meaning of a word in a given context, when the word has multiple possible meanings.
- Supervised WSD methods use sense-annotated corpora to train machine learning models that can predict the sense of a word based on its features, such as surrounding words, part-of-speech tags, syntactic dependencies, etc  .
- The most widely used training corpus for supervised WSD is SemCor, which contains 226,036 sense annotations from 352 documents manually annotated with WordNet senses .
- Some of the common supervised WSD algorithms are:
  - Naive Bayes: This is a probabilistic classifier that assumes that the features are independent given the sense. It calculates the posterior probability of each sense given the features, and chooses the sense with the highest probability.
  - Decision Trees: This is a hierarchical classifier that splits the feature space into regions based on a series of rules. Each leaf node of the tree represents a sense, and each internal node represents a feature test. The classifier follows the path from the root to the leaf that matches the features of the input word.
  - Support Vector Machines: This is a linear classifier that finds the optimal hyperplane that separates the feature vectors of different senses. The classifier assigns the sense that corresponds to the side of the hyperplane where the input word lies.
  - Neural Networks: This is a non-linear classifier that consists of multiple layers of nodes that perform weighted sums and activation functions. The classifier learns the weights of the connections between the nodes from the training data, and outputs the sense with the highest activation value.
- The advantages of supervised WSD methods are:
  - They can achieve high accuracy and precision, especially for fine-grained senses.
  - They can leverage rich and complex features that capture the semantic and syntactic context of the word.
  - They can benefit from the advances in machine learning techniques and architectures.
- The disadvantages of supervised WSD methods are:
  - They require a large amount of sense-annotated data, which is costly and time-consuming to obtain .
  - They suffer from the data sparsity problem, which means that some senses may not have enough examples in the training data to learn from .
  - They are domain-dependent, which means that they may not generalize well to new domains or genres that have different word usage patterns .