### Bootstrapping methods for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

Bootstrapping methods in Natural Language Processing (NLP) are used to learn a mapping from input to output given a training set of few examples annotated with target labels and many unannotated examples. The goal is to enlarge the annotated examples from the unannotated ones with the most appropriate examples.

One bootstrapping method uses a broad-coverage, rule-based parser to compute probabilities while parsing an untagged corpus of natural language text. These probabilities are then incorporated into the processing of the same parser as it analyzes new text.

Bootstrapping approaches in NLP generally follow the same format:
1. Start with an empty list of things.
2. Initialize this list with carefully chosen seeds.
3. Leverage the things in the list to find more things from a training corpus.
