### Interpolation and Backoff

- Interpolation and backoff are two methods of smoothing n-gram models in natural language processing (NLP).
- Smoothing is the process of assigning non-zero probabilities to unseen n-grams, and adjusting the probabilities of seen n-grams, to avoid overfitting and improve generalization.
- Interpolation is a method of smoothing that combines the probabilities of different n-gram models, such as unigram, bigram, and trigram, using some weights that sum to one.
- Backoff is a method of smoothing that uses a lower-order n-gram model when a higher-order n-gram model is not available or reliable, such as using a bigram model when a trigram model is zero or sparse.
- Both interpolation and backoff can be applied recursively, such as using a linear combination of trigram, bigram, and unigram models for interpolation, or using a unigram model when both trigram and bigram models are zero or sparse for backoff.
- The weights for interpolation and the thresholds for backoff can be learned from a held-out corpus, or estimated using some heuristics, such as the Good-Turing estimate or the Kneser-Ney estimate.