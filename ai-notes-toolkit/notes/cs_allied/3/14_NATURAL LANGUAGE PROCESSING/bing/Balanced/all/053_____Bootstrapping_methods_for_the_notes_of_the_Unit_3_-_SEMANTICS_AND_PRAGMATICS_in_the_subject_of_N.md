# Bootstrapping methods for the notes of the Unit 3 - SEMANTICS AND PRAGMATICS in the subject of NATURAL LANGUAGE PROCESSING

- Bootstrapping methods are a type of semi-supervised learning techniques that use a small set of labeled data and a large set of unlabeled data to learn a model or a task.
- Bootstrapping methods can be applied to various natural language processing (NLP) tasks, such as part-of-speech tagging, named entity recognition, relation extraction, sentiment analysis, etc.
- Bootstrapping methods generally follow the same format:
  - Start with an empty list of things (e.g., words, phrases, entities, relations, etc.).
  - Initialize the list with carefully chosen seeds (e.g., manually annotated examples, rules, patterns, etc.).
  - Leverage the things in the list to find more things from the unlabeled data (e.g., using similarity measures, classifiers, parsers, etc.).
  - Repeat the previous step until a stopping criterion is met (e.g., no more things are found, a predefined number of iterations is reached, etc.).
- Bootstrapping methods can be classified into two main categories:
  - Self-training: The model learns from its own predictions on the unlabeled data and adds the most confident ones to the labeled data.
  - Co-training: The model consists of two or more learners that use different views or features of the data and teach each other from their predictions on the unlabeled data.
- Bootstrapping methods can also be combined with other learning techniques, such as rule-based methods, active learning, ensemble methods, etc.
- Bootstrapping methods have some advantages and disadvantages :
  - Advantages: They can reduce the need for manual annotation, they can exploit large amounts of unlabeled data, they can adapt to new domains or tasks, they can improve the performance of the model over time.
  - Disadvantages: They can suffer from semantic drift, which is the loss of accuracy or consistency of the model due to the propagation of errors or noise in the unlabeled data, they can be sensitive to the choice of seeds, they can be computationally expensive or complex.