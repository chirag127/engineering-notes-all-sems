### WSD using Supervised

- Word Sense Disambiguation (WSD) is the task of identifying the correct meaning of a word in a given context, when the word has multiple possible meanings.
- Supervised WSD methods use sense-annotated corpora to train machine learning models that can predict the word sense based on features extracted from the context  .
- The most widely used training corpus for supervised WSD is SemCor, which contains 226,036 sense annotations from 352 documents manually annotated with WordNet senses .
- Some of the common features used for supervised WSD are: 
  - Bag-of-words: The words in the surrounding context of the target word.
  - Part-of-speech tags: The grammatical categories of the words in the context.
  - Collocations: The co-occurrence patterns of the words in the context.
  - Local syntactic dependencies: The syntactic relations between the target word and its neighbors.
  - Semantic features: The semantic categories or concepts associated with the words in the context .
- Some of the common machine learning algorithms used for supervised WSD are: 
  - Decision trees: These are tree-like structures that split the feature space into regions based on rules derived from the training data.
  - Naive Bayes: These are probabilistic models that compute the likelihood of a word sense given the features, based on the assumption of conditional independence among the features.
  - Support vector machines: These are linear models that find the optimal hyperplane that separates the feature vectors of different word senses in a high-dimensional space.
  - Neural networks: These are non-linear models that learn complex mappings between the features and the word senses, using multiple layers of neurons and activation functions  .
- Supervised WSD methods have the advantage of being able to learn from large amounts of labeled data and achieve high accuracy on the same domain and sense inventory as the training data.
- Supervised WSD methods have the disadvantage of being dependent on the availability and quality of sense-annotated corpora, which are costly and time-consuming to create, and may not cover all the possible word senses, domains, and languages .