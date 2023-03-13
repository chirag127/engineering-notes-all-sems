### WSD using Supervised for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

- Word Sense Disambiguation (WSD) is the task of identifying the correct meaning of a word in a given context, when the word has multiple possible meanings (polysemy).
- WSD is a part of computational lexical semantics, which deals with the representation and analysis of word meanings and their relations.
- WSD is an AI-complete problem, which means that it is as hard as the most difficult problems in AI, and requires human-like intelligence and common sense to solve.
- WSD has many applications in natural language processing, such as machine translation, information retrieval, text summarization, sentiment analysis, etc.
- WSD can be performed using supervised, unsupervised, or semi-supervised methods.
- Supervised WSD methods use labelled data, which means that each word in the training corpus is annotated with its correct sense, according to a predefined sense inventory (such as WordNet).
- Supervised WSD methods learn a classifier that can predict the correct sense of a word in a new context, based on the features extracted from the word and its surrounding words.
- Supervised WSD methods can be divided into two types: local and global.
- Local supervised WSD methods treat each word as an independent classification problem, and ignore the interdependencies among the senses of different words in the same context.
- Local supervised WSD methods can use various types of classifiers, such as decision trees, naive Bayes, support vector machines, neural networks, etc.
- Global supervised WSD methods take into account the coherence and consistency of the senses of different words in the same context, and try to find the optimal sense assignment for the whole context.
- Global supervised WSD methods can use various types of optimization techniques, such as integer linear programming, graph-based methods, Markov random fields, etc.
- Supervised WSD methods have the advantage of high accuracy and reliability, but they also have some limitations, such as:
  - They require a large amount of annotated data, which is costly and time-consuming to obtain.
  - They suffer from the data sparsity problem, which means that they may not encounter enough examples of a word sense in the training data to learn its features and patterns.
  - They are dependent on the sense inventory, which may not cover all the possible senses of a word, or may not match the granularity and domain of the application.
  - They are not robust to the domain adaptation problem, which means that they may not perform well on a different domain or genre than the one they were trained on.

- A possible mnemonic to remember the main points of supervised WSD methods is:

  - **S**upervised WSD methods use **S**ense-annotated data to learn a **S**ense classifier.
  - **S**upervised WSD methods can be **S**plit into local and global methods.
  - **S**upervised WSD methods have high accuracy but also some **S**hortcomings.