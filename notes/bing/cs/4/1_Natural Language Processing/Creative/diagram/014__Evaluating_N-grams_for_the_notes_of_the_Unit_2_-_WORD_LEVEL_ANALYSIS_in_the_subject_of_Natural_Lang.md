An N-gram is a sequence of N words or letters from a given text or speech. An N-gram model is a probabilistic model that predicts the next word or letter based on the previous N-1 words or letters. N-gram models are widely used in natural language processing for tasks such as speech recognition, machine translation and sentiment analysis.

The following diagram illustrates the basic architecture of an N-gram model:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   N-1 words     |---->|  N-gram model   |---->|  Next word      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The N-gram model takes as input a sequence of N-1 words and outputs the most probable word that might follow this sequence. The N-gram model is trained on a large corpus of text, where it counts the frequency of each N-gram and estimates the probability of each word given the previous N-1 words. For example, given the sequence "the quick brown", a trigram model (N=3) might predict the next word as "fox" with a high probability, based on how often this N-gram occurs in the training corpus.

There are different types of N-gram models, depending on the value of N. A unigram model (N=1) considers only the frequency of each word, without looking at the previous words. A bigram model (N=2) considers the previous word to predict the current word. A trigram model (N=3) considers the previous two words to predict the current word. And so on. Generally, higher values of N capture more context and produce more accurate predictions, but they also require more data and computational resources.