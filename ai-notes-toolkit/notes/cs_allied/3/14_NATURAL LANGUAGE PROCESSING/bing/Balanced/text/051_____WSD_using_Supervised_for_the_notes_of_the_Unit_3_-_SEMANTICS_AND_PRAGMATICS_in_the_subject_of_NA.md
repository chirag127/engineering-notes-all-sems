### WSD using Supervised

- Word Sense Disambiguation (WSD) is the task of identifying the correct meaning of a word in a given context, when the word has multiple possible meanings.
- Supervised WSD methods use sense-annotated corpora to train machine learning models that can predict the sense of a word based on its features, such as surrounding words, part-of-speech tags, syntactic dependencies, etc  .
- The most widely used training corpus for supervised WSD is SemCor, which contains 226,036 sense annotations from 352 documents manually annotated with WordNet senses .
- Some of the common supervised WSD algorithms are:
  - Naive Bayes: This is a probabilistic classifier that assigns the most likely sense to a word based on the frequencies of its features in the training data.
  - Decision Trees: This is a rule-based classifier that splits the feature space into regions based on a series of binary decisions, and assigns the most frequent sense in each region.
  - Support Vector Machines: This is a linear classifier that finds the optimal hyperplane that separates the feature vectors of different senses with the maximum margin.
  - Neural Networks: This is a non-linear classifier that learns a complex function that maps the input features to the output senses, using hidden layers of neurons and activation functions.
- Supervised WSD methods have the advantage of being able to learn from large amounts of data and achieve high accuracy, but they also have some limitations, such as:
  - Data sparsity: The sense-annotated corpora are often incomplete, noisy, and inconsistent, and may not cover all the possible senses and contexts of a word .
  - Domain adaptation: The trained models may not generalize well to new domains or genres that have different distributions of words and senses .
  - Sense granularity: The sense inventory used for annotation may not match the level of detail required for a specific application or task .