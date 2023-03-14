 Here is the content in markdown format for the given topic:

### Stochastic for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

- Stochastic basically refers to a random probability distribution or process.
- In NLP, stochastic models are used to assign probabilities to the occurrence of words.
- These models consider the probability of a word appearing based on the previous words.
- Some of the commonly used stochastic models are:
    - N-gram models: These models compute the probability of a word appearing based on the previous n-1 words. For e. g. a trigram model considers the previous 2 words to compute the probability of the next word. These models are easy to build but do not consider long-range dependencies.
    - Hidden Markov Models (HMMs): These are a class of stochastic models which assume that the system being modeled is a Markov process with hidden states. They are commonly used for Part-of-Speech tagging, speech recognition, etc.
    - Probabilistic Context-Free Grammars (PCFGs): These are stochastic models that are based on context-free grammars. They assign probabilities to the production rules of a context-free grammar. These are used to model the syntax of sentences.
- Some advantages of stochastic models are:
    - They can handle unseen data/words.
    - They are relatively simple to build and train.
- Some disadvantages are:
    - They do not capture longer range dependencies.
    - They require large amounts of training data to build accurate models.
- Overall, stochastic models are useful as they provide a way to compute probabilities in NLP which can then be used for tasks like predicting the next word, Part-of-Speech tagging, etc.