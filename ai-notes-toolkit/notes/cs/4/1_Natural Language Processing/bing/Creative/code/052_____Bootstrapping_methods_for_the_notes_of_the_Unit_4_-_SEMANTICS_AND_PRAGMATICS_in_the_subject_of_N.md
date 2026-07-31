# Bootstrapping methods for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

- Bootstrapping methods are a type of semi-supervised learning techniques that use a small set of labeled data and a large set of unlabeled data to learn a mapping from input to output.
- Bootstrapping methods can be applied to various natural language processing tasks, such as part-of-speech tagging, named entity recognition, relation extraction, semantic role labeling, etc.
- Bootstrapping methods generally follow the same format:
  - Start with an empty list of things (e.g., tags, entities, relations, roles, etc.).
  - Initialize the list with carefully chosen seeds (e.g., rules, patterns, examples, etc.).
  - Leverage the things in the list to find more things from the training corpus (e.g., using pattern matching, classification, clustering, etc.).
  - Repeat the previous step until a stopping criterion is met (e.g., no more things are found, a predefined number of iterations is reached, etc.).
- Bootstrapping methods can be classified into two main categories:
  - Generative bootstrapping: the list of things is used to generate new patterns or rules that can extract more things from the corpus (e.g., DIPRE, Snowball, etc.).
  - Discriminative bootstrapping: the list of things is used to train a classifier or a model that can assign labels to more things from the corpus (e.g., Yarowsky, Co-training, etc.).
- Bootstrapping methods have some advantages and disadvantages:
  - Advantages: they can reduce the need for manual annotation, they can exploit the redundancy and regularity of natural language, they can adapt to different domains and languages, etc.
  - Disadvantages: they can suffer from semantic drift, they can be sensitive to noise and errors, they can be biased by the initial seeds, they can have difficulty with rare or ambiguous things, etc.