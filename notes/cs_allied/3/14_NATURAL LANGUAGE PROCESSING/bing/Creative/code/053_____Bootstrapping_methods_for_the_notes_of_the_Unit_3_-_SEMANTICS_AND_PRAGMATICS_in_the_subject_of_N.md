### Bootstrapping methods for the notes of the Unit 3 - SEMANTICS AND PRAGMATICS in the subject of NATURAL LANGUAGE PROCESSING

- Bootstrapping methods are a type of semi-supervised learning techniques that use a small set of labeled data and a large set of unlabeled data to learn a model or a task.
- Bootstrapping methods can be applied to various natural language processing (NLP) tasks, such as part-of-speech tagging, named entity recognition, relation extraction, semantic parsing, etc.
- Bootstrapping methods generally follow the same format:
  - Start with an empty list of things (e.g., tags, entities, relations, etc.).
  - Initialize the list with carefully chosen seeds (e.g., rules, patterns, examples, etc.).
  - Leverage the things in the list to find more things from the unlabeled data (e.g., by matching, expanding, scoring, etc.).
  - Repeat the previous step until a stopping criterion is met (e.g., no more things are found, a threshold is reached, etc.).
- Bootstrapping methods can be classified into two main categories:
  - Generative bootstrapping: the model learns a probabilistic distribution over the data and uses it to generate new labels for the unlabeled data (e.g., EM algorithm, Naive Bayes, etc.).
  - Discriminative bootstrapping: the model learns a classifier or a function that discriminates between different labels and uses it to assign new labels to the unlabeled data (e.g., SVM, logistic regression, etc.).
- Bootstrapping methods can also be distinguished by the type of seeds they use:
  - Rule-based bootstrapping: the seeds are manually crafted rules or patterns that capture the linguistic features of the target task (e.g., regular expressions, syntactic rules, etc.).
  - Example-based bootstrapping: the seeds are manually annotated examples that represent the target task (e.g., word pairs, entity pairs, etc.).
- Bootstrapping methods have some advantages and disadvantages:
  - Advantages: they can reduce the need for human annotation, they can exploit large amounts of unlabeled data, they can adapt to new domains or languages, etc.
  - Disadvantages: they can suffer from semantic drift, they can be sensitive to noise or errors, they can be biased by the initial seeds, etc.