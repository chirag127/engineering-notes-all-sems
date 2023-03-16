### Bootstrapping methods for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

- Bootstrapping methods are a type of semi-supervised learning techniques that use a small set of labeled data and a large set of unlabeled data to learn a model or a task.
- Bootstrapping methods can be applied to various natural language processing (NLP) tasks, such as part-of-speech tagging, named entity recognition, relation extraction, sentiment analysis, etc.
- Bootstrapping methods generally follow the same format:
  - Start with an empty list of things (e.g., words, phrases, entities, relations, etc.).
  - Initialize the list with carefully chosen seeds (e.g., manually annotated examples, rules, patterns, etc.).
  - Leverage the things in the list to find more things from the unlabeled data (e.g., using similarity measures, classifiers, parsers, etc.).
  - Repeat the previous step until a stopping criterion is met (e.g., no more things can be found, a predefined number of iterations is reached, etc.).
- Bootstrapping methods can be classified into two main categories:
  - Self-training: The model uses its own predictions on the unlabeled data to augment the labeled data and retrain itself.
  - Co-training: Two or more models use different views or features of the data to make predictions and exchange their confident predictions to augment the labeled data for each other.
- Bootstrapping methods can benefit from the following advantages :
  - They can reduce the cost and effort of manual annotation.
  - They can exploit the large amount of unlabeled data available for NLP tasks.
  - They can improve the performance and generalization of the model or the task.
- Bootstrapping methods can also face the following challenges :
  - They can suffer from semantic drift, which is the deviation of the learned things from the original seeds due to noise or ambiguity in the data.
  - They can be sensitive to the choice and quality of the seeds, which can affect the coverage and accuracy of the learned things.
  - They can be affected by the distribution and diversity of the unlabeled data, which can influence the reliability and confidence of the predictions.