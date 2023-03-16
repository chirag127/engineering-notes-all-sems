### Bootstrapping methods for the notes of the Unit 3 - SEMANTICS AND PRAGMATICS in the subject of NATURAL LANGUAGE PROCESSING

- Bootstrapping methods are a type of semi-supervised learning techniques that use a small set of labeled data and a large set of unlabeled data to learn a model or a task.
- Bootstrapping methods can be applied to various natural language processing (NLP) tasks, such as part-of-speech tagging, named entity recognition, relation extraction, sentiment analysis, etc.
- Bootstrapping methods generally follow the same format:
  - Start with an empty list of things (e.g., words, phrases, entities, relations, etc.).
  - Initialize the list with carefully chosen seeds (e.g., manually annotated examples, heuristics, rules, etc.).
  - Leverage the things in the list to find more things from the unlabeled data (e.g., using pattern matching, classification, clustering, etc.).
  - Repeat the previous step until a stopping criterion is met (e.g., no more new things are found, a predefined number of iterations is reached, etc.).
- Bootstrapping methods can be classified into two main categories:
  - Self-training: The model learns from its own predictions on the unlabeled data and adds the most confident ones to the labeled data.
  - Co-training: The model consists of two or more classifiers that learn from different views or features of the data and mutually teach each other by adding the most confident predictions to the labeled data.
- Bootstrapping methods can also be combined with other techniques, such as rule-based parsing, active learning, or ensemble learning, to improve the performance and robustness of the model.
- Bootstrapping methods have some advantages and disadvantages:
  - Advantages: They can reduce the need for manual annotation, which is costly and time-consuming. They can also exploit the large amount of unlabeled data available on the web or other sources.
  - Disadvantages: They can suffer from semantic drift, which is the deviation of the model from the original task or domain due to the accumulation of errors or noise in the unlabeled data. They can also be sensitive to the choice of seeds, which can affect the quality and diversity of the learned things.