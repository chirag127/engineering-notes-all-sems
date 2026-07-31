### Bootstrapping methods for the notes of the Unit 3 - SEMANTICS AND PRAGMATICS in the subject of NATURAL LANGUAGE PROCESSING

- Bootstrapping methods are a type of semi-supervised learning techniques that use a small set of labeled data and a large set of unlabeled data to learn a mapping from input to output.
- Bootstrapping methods can be applied to various natural language processing tasks, such as part-of-speech tagging, named entity recognition, relation extraction, semantic parsing, etc .
- Bootstrapping methods generally follow the same format:
  - Start with an empty list of things (e.g., tags, entities, relations, etc.).
  - Initialize the list with carefully chosen seeds (e.g., rules, patterns, examples, etc.).
  - Leverage the things in the list to find more things from the unlabeled data (e.g., using pattern matching, classification, clustering, etc.).
  - Repeat the previous step until a stopping criterion is met (e.g., no more new things are found, a predefined number of iterations is reached, etc.).
- Bootstrapping methods can benefit from a broad-coverage, rule-based parser that can compute probabilities while parsing an untagged corpus of natural language text, and then incorporate those probabilities into the processing of the same parser as it analyzes new text.
- Bootstrapping methods can face some challenges, such as data sparsity, noise propagation, semantic drift, etc . Various techniques have been proposed to address these challenges, such as using multiple seed sets, filtering unreliable patterns, incorporating external knowledge, etc .