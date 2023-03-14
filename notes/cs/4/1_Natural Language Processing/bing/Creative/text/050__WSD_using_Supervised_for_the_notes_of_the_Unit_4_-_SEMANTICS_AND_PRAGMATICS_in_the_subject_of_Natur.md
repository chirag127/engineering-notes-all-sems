### WSD using Supervised

- Word Sense Disambiguation (WSD) is the task of identifying the correct meaning of an ambiguous word in a given context .
- Supervised WSD methods use sense-annotated corpora to train machine learning models that can predict the correct sense of a word based on its features   .
- The features used for supervised WSD can include lexical, syntactic, semantic, and collocational information of the word and its context .
- Supervised WSD methods can be classified into two types: local and global .
  - Local methods assign senses to each word independently, based on the local context of the word .
  - Global methods assign senses to all the words in a text jointly, based on the global coherence of the senses .
- Supervised WSD methods typically produce the best results, but they require labeled training data that may be difficult and expensive to obtain  .
- Supervised WSD methods are also limited by the coverage and quality of the sense inventory, which is usually a lexical resource such as WordNet  .
- Some examples of supervised WSD methods are decision trees, support vector machines, neural networks, and Bayesian classifiers  .