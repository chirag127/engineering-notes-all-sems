### Bootstrapping methods for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

- Bootstrapping methods are a type of semi-supervised learning techniques that use a small set of labeled data and a large set of unlabeled data to learn a mapping from input to output.
- Bootstrapping methods can be applied to various natural language processing tasks, such as part-of-speech tagging, named entity recognition, relation extraction, semantic parsing, etc .
- Bootstrapping methods generally follow the same format:
  - Start with an empty list of things (e.g., words, phrases, entities, relations, etc.).
  - Initialize the list with carefully chosen seeds (e.g., manually annotated examples, heuristics, rules, etc.).
  - Leverage the things in the list to find more things from the unlabeled data (e.g., using pattern matching, similarity measures, classifiers, etc.).
  - Repeat the previous step until a stopping criterion is met (e.g., no more things can be found, a predefined number of iterations is reached, etc.).
- Bootstrapping methods can be classified into two main categories:
  - Self-training: The learner uses its own predictions on the unlabeled data to augment the labeled data and retrain itself.
  - Co-training: The learner consists of two or more classifiers that use different views or features of the input data and mutually teach each other by labeling the unlabeled data.
- Bootstrapping methods can benefit from the following advantages :
  - They can reduce the cost and effort of manual annotation.
  - They can exploit the large amount of available unlabeled data.
  - They can adapt to new domains or tasks with minimal supervision.
- Bootstrapping methods can also face the following challenges :
  - They can suffer from semantic drift, which is the gradual loss of accuracy and precision due to the propagation of errors and noise in the unlabeled data.
  - They can be sensitive to the choice of seeds, which can affect the coverage and diversity of the learned things.
  - They can be limited by the quality and quantity of the unlabeled data, which can affect the scalability and robustness of the learner.