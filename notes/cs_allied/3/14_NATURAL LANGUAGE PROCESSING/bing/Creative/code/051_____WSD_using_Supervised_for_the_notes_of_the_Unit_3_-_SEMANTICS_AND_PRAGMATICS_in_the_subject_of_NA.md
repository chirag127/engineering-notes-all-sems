### WSD using Supervised

- Word Sense Disambiguation (WSD) is the task of identifying the correct meaning of a word in a given context, when the word has multiple possible meanings.
- Supervised WSD methods use sense-annotated corpora to train machine learning models that can predict the sense of a word based on its features, such as surrounding words, part-of-speech tags, syntactic dependencies, etc  .
- The most widely used training corpus for supervised WSD is SemCor, which contains 226,036 sense annotations from 352 documents manually annotated with WordNet senses .
- Some of the common supervised WSD algorithms are:
  - Naive Bayes: This is a probabilistic classifier that assumes that the features are conditionally independent given the sense. It estimates the posterior probability of a sense given the features using the Bayes' rule and chooses the sense with the highest probability .
  - Decision Trees: This is a non-parametric classifier that builds a tree-like structure where each node represents a feature test and each leaf represents a sense. It recursively splits the data into subsets based on the feature that best separates the senses, until a stopping criterion is met .
  - Support Vector Machines (SVM): This is a linear classifier that finds a hyperplane that maximizes the margin between the senses. It can also use kernel functions to map the features into a higher-dimensional space where the senses are more separable .
  - Neural Networks: This is a non-linear classifier that consists of multiple layers of neurons that can learn complex patterns from the data. It can use various architectures, such as feed-forward, recurrent, convolutional, or attention-based networks, to capture the semantic and syntactic features of the context .
- The advantages of supervised WSD methods are:
  - They can achieve high accuracy and precision on the test data, especially when the training data is large and representative of the domain .
  - They can leverage various types of features and information sources, such as word embeddings, syntactic parsers, or external knowledge bases, to improve the performance .
- The disadvantages of supervised WSD methods are:
  - They require a lot of manually sense-tagged data, which is costly and time-consuming to obtain. Moreover, the sense annotations may be inconsistent, noisy, or incomplete .
  - They suffer from the problem of data sparsity, which means that some senses may have very few or no examples in the training data, leading to poor generalization .
  - They are domain-dependent, which means that they may not perform well on new or different domains that have different sense distributions or vocabulary .