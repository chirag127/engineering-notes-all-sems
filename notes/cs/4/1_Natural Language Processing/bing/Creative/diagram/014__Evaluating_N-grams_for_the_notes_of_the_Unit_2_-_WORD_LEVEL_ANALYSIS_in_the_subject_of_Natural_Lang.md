An n-gram is a sequence of n words or characters from a given text or speech. N-gram models are used to estimate the probability of a word given its previous words or characters. They are useful for many natural language processing tasks such as speech recognition, machine translation, spelling correction, and text generation.

To evaluate an n-gram model, we need to measure how well it predicts unseen data. One way to do this is to use perplexity, which is the inverse of the average probability assigned to each word or character by the model. A lower perplexity means a better model.

To calculate the perplexity of an n-gram model, we need to split the data into two sets: a training set and a test set. The training set is used to build the model by counting the frequencies of n-grams in the data. The test set is used to evaluate the model by computing the probability of each word or character in the test set using the model.

The following diagram illustrates the basic steps of evaluating an n-gram model:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Training set  |     |  N-gram model  |     |  Test set      |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Count n-grams | --> |  Estimate      | --> |  Compute       |
|                |     |  probabilities |     |  perplexity    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```