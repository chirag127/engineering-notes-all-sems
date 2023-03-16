# WSD using Supervised

- Word Sense Disambiguation (WSD) is the task of identifying the correct meaning of a word in a given context, when the word has multiple possible meanings.
- Supervised WSD methods use sense-annotated corpora to train machine learning models that can predict the sense of a word based on its features, such as surrounding words, part-of-speech tags, syntactic dependencies, etc  .
- The most widely used training corpus for supervised WSD is SemCor, which contains 226,036 sense annotations from 352 documents manually annotated with WordNet senses .
- Some of the supervised learning algorithms that have been applied to WSD are decision trees, naive Bayes, support vector machines, neural networks, etc  .
- Supervised WSD methods have the advantage of being able to learn from large amounts of data and achieve high accuracy on the same domain and genre as the training data.
- However, supervised WSD methods also have some limitations, such as the scarcity of sense-annotated data, the domain and genre dependence of the models, and the lack of generalization to unseen words or senses  .
- To overcome these limitations, some semi-supervised and unsupervised WSD methods have been proposed, which use unlabelled data, lexical resources, or similarity measures to augment or replace the sense-annotated data  .