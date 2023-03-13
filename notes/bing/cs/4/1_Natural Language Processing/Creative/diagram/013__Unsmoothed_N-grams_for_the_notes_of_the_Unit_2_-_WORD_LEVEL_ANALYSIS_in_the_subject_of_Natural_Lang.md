An N-gram is a sequence of N words. For example, "natural language processing" is a trigram (N = 3). An N-gram model is a probabilistic model that predicts the next word in a sequence based on the previous N - 1 words. An unsmoothed N-gram model assigns zero probability to any unseen N-gram, which is a problem for natural language processing tasks. A smoothed N-gram model assigns some non-zero probability to unseen N-grams by adjusting the counts of seen N-grams.

The following diagram illustrates the basic architecture of an unsmoothed N-gram model:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Vocabulary    |     |   Vocabulary    |     |   Vocabulary    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       V                      V                      V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   N-gram        |     |   N-gram        |     |   N-gram        |
|   Counts        |     |   Counts        |     |   Counts        |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       V                      V                      V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   N-gram        |     |   N-gram        |     |   N-gram        |
|   Probabilities |     |   Probabilities |     |   Probabilities |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       V                      V                      V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Next Word     |     |   Next Word     |     |   Next Word     |
|   Prediction    |     |   Prediction    |     |   Prediction    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The diagram shows three N-gram models with different values of N. Each model takes a vocabulary of words as input and outputs a prediction for the next word in a sequence. The model first counts the frequency of each N-gram in a corpus of text and stores them in a table. Then, it calculates the probability of each N-gram by dividing the count by the total number of N-grams. Finally, it uses the probability to predict the next word given the previous N - 1 words. For example, if N = 2, the model predicts the next word given the previous word. If the previous word is "natural", the model looks up the probability of all bigrams that start with "natural" and chooses the one with the highest probability as the prediction. If the model has never seen a bigram that starts with "natural", it assigns zero probability to all possible next words and cannot make a prediction. This is the problem of unsmoothed N-gram models.