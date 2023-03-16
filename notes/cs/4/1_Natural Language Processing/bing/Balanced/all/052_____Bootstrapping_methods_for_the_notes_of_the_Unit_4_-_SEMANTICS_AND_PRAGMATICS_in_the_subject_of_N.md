# Bootstrapping methods for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

- Bootstrapping methods are a type of semi-supervised learning techniques that use a small set of labeled data and a large set of unlabeled data to learn a model or a task.
- Bootstrapping methods are useful for natural language processing (NLP) tasks that require semantic or pragmatic knowledge, such as word sense disambiguation, relation extraction, named entity recognition, etc.
- Bootstrapping methods in NLP generally follow the same format:
  - Start with an empty list of things (e.g., words, phrases, entities, relations, etc.).
  - Initialize the list with carefully chosen seeds (e.g., manually annotated examples, heuristics, dictionaries, etc.).
  - Leverage the things in the list to find more things from the unlabeled data (e.g., using pattern matching, similarity measures, clustering, etc.).
  - Repeat the previous step until a stopping criterion is met (e.g., no more new things are found, a predefined number of iterations is reached, etc.).
- Bootstrapping methods can be classified into two types:
  - Self-training: The model learns from its own predictions on the unlabeled data and adds the most confident ones to the labeled data.
  - Co-training: The model consists of two or more classifiers that learn from different views or features of the data and mutually reinforce each other by adding the most confident predictions to the labeled data.
- Bootstrapping methods can also be combined with other learning techniques, such as rule-based methods, active learning, ensemble methods, etc.
- Bootstrapping methods have some advantages and disadvantages:
  - Advantages: They can reduce the need for manual annotation, exploit the large amount of unlabeled data, and improve the performance of the model.
  - Disadvantages: They can suffer from semantic drift, noise propagation, and data sparsity. Semantic drift refers to the deviation of the learned concepts from the original seeds due to errors or ambiguities. Noise propagation refers to the accumulation of errors or inconsistencies in the labeled data due to the model's predictions. Data sparsity refers to the lack of sufficient or diverse examples for some concepts or categories.