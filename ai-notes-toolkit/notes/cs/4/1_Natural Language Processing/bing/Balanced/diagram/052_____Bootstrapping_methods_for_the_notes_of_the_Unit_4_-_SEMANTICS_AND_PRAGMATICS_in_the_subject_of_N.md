### Bootstrapping methods

- Bootstrapping methods are a class of semi-supervised learning techniques that use a small set of labeled data and a large set of unlabeled data to learn a model or a task.
- Bootstrapping methods are useful for natural language processing (NLP) tasks that require large amounts of annotated data, such as named entity recognition, relation extraction, sentiment analysis, etc.
- Bootstrapping methods generally follow the same format:
  - Start with an empty list of things (e.g., entities, relations, sentiments, etc.).
  - Initialize the list with carefully chosen seeds (e.g., seed words, seed patterns, seed rules, etc.).
  - Leverage the things in the list to find more things from the unlabeled data (e.g., using pattern matching, rule induction, classifier learning, etc.).
  - Repeat the previous step until a stopping criterion is met (e.g., no more things can be found, a predefined number of iterations is reached, a desired accuracy is achieved, etc.).
- Bootstrapping methods can be divided into two main types:
  - Pattern-based bootstrapping: This type of bootstrapping uses linguistic patterns (e.g., regular expressions, syntactic dependencies, semantic roles, etc.) to extract things from the unlabeled data. For example, a pattern-based bootstrapping method for named entity recognition could use the pattern "X, the Y of Z" to extract person names (X), titles (Y), and organizations (Z) from the text.
  - Classifier-based bootstrapping: This type of bootstrapping uses a classifier (e.g., a decision tree, a neural network, a support vector machine, etc.) to assign labels to the unlabeled data. For example, a classifier-based bootstrapping method for sentiment analysis could use a classifier trained on the seed words to predict the polarity of the unlabeled words.
- Bootstrapping methods have some advantages and disadvantages:
  - Advantages: Bootstrapping methods can reduce the cost and effort of manual annotation, can exploit the diversity and richness of the unlabeled data, and can adapt to different domains and tasks.
  - Disadvantages: Bootstrapping methods can suffer from semantic drift, which is the phenomenon of accumulating errors and noise in the list of things as the bootstrapping process progresses. Bootstrapping methods can also be sensitive to the choice of seeds, patterns, and classifiers, which can affect the quality and coverage of the results.