An unsmoothed n-gram model is a probabilistic model that estimates the probability of a word given its previous n-1 words, based on the frequency counts of n-grams in a corpus. An n-gram is a sequence of n words, such as a unigram (one word), a bigram (two words), a trigram (three words), etc. For example, the sentence "I love natural language processing" contains five unigrams, four bigrams, three trigrams, two four-grams, and one five-gram.

The following diagram illustrates the basic architecture of an unsmoothed n-gram model:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Corpus        |     |   N-gram        |     |   Probability   |
|                 |     |   counts        |     |   estimation    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   A collection  |     |   The number of |     |   The frequency |
|   of text       |---->|   times each    |---->|   of each n-gram|
|   documents     |     |   n-gram occurs |     |   divided by the|
|                 |     |   in the corpus |     |   frequency of  |
|                 |     |                 |     |   its prefix    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

An example of unsmoothed n-gram probability estimation is:

- Given the corpus: "I love natural language processing. I love machine learning. I love data science."
- The unigram counts are: {"I": 3, "love": 3, "natural": 1, "language": 1, "processing": 1, "machine": 1, "learning": 1, "data": 1, "science": 1, ".": 3}
- The bigram counts are: {"I love": 3, "love natural": 1, "natural language": 1, "language processing": 1, "processing .": 1, "love machine": 1, "machine learning": 1, "learning .": 1, "love data": 1, "data science": 1, "science .": 1}
- The trigram counts are: {"I love natural": 1, "love natural language": 1, "natural language processing": 1, "language processing .": 1, "I love machine": 1, "love machine learning": 1, "machine learning .": 1, "I love data": 1, "love data science": 1, "data science .": 1}
- The unsmoothed unigram probabilities are: P(I) = 3/15, P(love) = 3/15, P(natural) = 1/15, P(language) = 1/15, P(processing) = 1/15, P(machine) = 1/15, P(learning) = 1/15, P(data) = 1/15, P(science) = 1/15, P(.) = 3/15
- The unsmoothed bigram probabilities are: P(love|I) = 3/3, P(natural|love) = 1/3, P(language|natural) = 1/1, P(processing|language) = 1/1, P(.|processing) = 1/1, P(machine|love) = 1/3, P(learning|machine) = 1/1, P(.|learning) = 1/1, P(data|love) = 1/3, P(science|data) = 1/1, P(.|science) = 1/1
- The unsmoothed trigram probabilities are: P(natural|I love) = 1/3, P(language|love natural) = 1/1, P(processing|natural language) = 1/1, P(.|language processing) = 1/1, P(machine|I love) = 1/3, P(learning|love machine) = 1/1, P(.|machine