### Bootstrapping methods for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

- Bootstrapping methods are a class of semi-supervised learning techniques that aim to learn a mapping from input to output given a small set of labeled examples and a large set of unlabeled examples.
- Bootstrapping methods are useful for natural language processing tasks that require semantic knowledge, such as entity extraction, relation extraction, sentiment analysis, etc.
- Bootstrapping methods typically follow a general format :
  - Start with an empty list of things (e.g., entities, relations, sentiments, etc.).
  - Initialize the list with carefully chosen seeds (e.g., a few examples of the things to be learned).
  - Leverage the things in the list to find more things from the training corpus (e.g., by using extraction patterns, similarity measures, classifiers, etc.).
  - Add the new things to the list and repeat the process until a stopping criterion is met (e.g., no more new things are found, a predefined number of iterations is reached, etc.).
- Bootstrapping methods can be divided into two main types:
  - Pattern-based bootstrapping: This type of bootstrapping relies on extraction patterns that capture the syntactic and lexical contexts of the things to be learned. For example, to learn new entities of a certain type, one can use patterns like "X is a Y" or "X, a Y, ...", where X is a variable and Y is a seed entity. The patterns are either manually defined or automatically learned from the seeds and the corpus. The patterns are then applied to the corpus to extract new entities that match the patterns.
  - Classifier-based bootstrapping: This type of bootstrapping relies on classifiers that predict the labels of the things to be learned. For example, to learn new entities of a certain type, one can use a classifier that takes a word or a phrase as input and outputs a probability of being an entity of that type. The classifier is either pre-trained or trained on the seeds and the corpus. The classifier is then applied to the corpus to extract new entities that have high probabilities of being the desired type.
- Bootstrapping methods have some advantages and disadvantages:
  - Advantages:
    - They can reduce the need for manual annotation, which is costly and time-consuming.
    - They can leverage the large amount of unlabeled data, which is abundant and cheap.
    - They can adapt to different domains and tasks by changing the seeds and the extraction methods.
  - Disadvantages:
    - They can suffer from semantic drift, which is the phenomenon of gradually deviating from the original meaning of the things to be learned. This can happen because of noise, ambiguity, or diversity in the corpus and the extraction methods.
    - They can be sensitive to the quality and quantity of the seeds, which can affect the performance and the coverage of the bootstrapping process.
    - They can be hard to evaluate, as there is no ground truth for the unlabeled data and the bootstrapping results.

- Some examples of bootstrapping methods for natural language processing are  :
  - A bootstrapping method for learning semantic lexicons using extraction pattern contexts. This method learns semantic categories (e.g., animals, colors, emotions, etc.) and their members (e.g., dog, red, happy, etc.) from a corpus. It starts with a few seed members for each category and uses extraction patterns (e.g., "X and other Ys", "X or other Ys", etc.) to find new members from the corpus. It also uses the context of the extraction patterns to refine the categories and the members.
  - A bootstrapping method for learning to bootstrap for entity set expansion. This method learns new entities of a given type (e.g., cities, movies, products, etc.) from a corpus. It starts with a few seed entities and uses a classifier to find new entities from the corpus. It also uses a reinforcement learning framework to optimize the selection of the new entities and the update of the classifier.