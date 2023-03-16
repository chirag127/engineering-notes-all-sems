### Interpolation and Backoff

- Interpolation and backoff are two methods of smoothing n-gram language models to deal with data sparsity and generalization issues    .
- Interpolation is a method of combining multiple n-gram models with different orders, such as unigram, bigram and trigram, by assigning weights to each model and taking a linear combination of their probabilities   .
- Backoff is a method of using a lower-order n-gram model when the higher-order model has insufficient evidence for a given context, such as using a bigram model when the trigram model has zero count for a word sequence  .
- In general, interpolation works better than backoff, as it can leverage information from all n-gram models, while backoff discards information from the higher-order models when backing off .
- The weights for interpolation can be estimated using various methods, such as maximum likelihood estimation, expectation-maximization, or cross-validation . The optimal weights depend on the frequency and context of the n-grams.
- The backoff method can be improved by using a discounting factor to reduce the probability mass of the higher-order model and redistribute it to the lower-order model, such as in the Kneser-Ney smoothing technique .