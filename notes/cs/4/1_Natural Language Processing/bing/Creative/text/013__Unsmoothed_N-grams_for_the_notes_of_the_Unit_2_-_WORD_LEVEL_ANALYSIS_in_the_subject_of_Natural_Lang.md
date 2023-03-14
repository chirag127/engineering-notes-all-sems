### Unsmoothed N-grams

- An n-gram is a sequence of n words from a given text or speech.
- N-grams are used to model the probability of a word given its previous words, based on the frequency of occurrence of the n-gram in a large corpus.
- The probability of an n-gram is estimated by counting the number of times it appears in the corpus and dividing it by the number of times the (n-1)-gram prefix appears.
- For example, the probability of the bigram "the cat" is estimated by counting the number of times "the cat" appears in the corpus and dividing it by the number of times "the" appears.
- Unsmoothed n-grams are n-grams that do not use any smoothing technique to deal with the problem of data sparsity.
- Data sparsity is the situation where some n-grams may not appear in the corpus at all, or may appear very rarely, resulting in zero or very low probabilities.
- Unsmoothed n-grams suffer from the following drawbacks:
  - They assign zero probability to unseen n-grams, which may not reflect the true probability of the n-gram in the language.
  - They overestimate the probability of frequent n-grams, which may not generalize well to new texts or domains.
  - They are sensitive to the size and quality of the corpus, which may not be representative of the language as a whole.
- Unsmoothed n-grams are therefore not suitable for language modeling, as they do not capture the variability and uncertainty of natural language. 
- Smoothing techniques are methods that modify the n-gram probabilities to avoid zero probabilities and reduce the impact of data sparsity. Some examples of smoothing techniques are add-one smoothing, Good-Turing smoothing, Kneser-Ney smoothing, etc.