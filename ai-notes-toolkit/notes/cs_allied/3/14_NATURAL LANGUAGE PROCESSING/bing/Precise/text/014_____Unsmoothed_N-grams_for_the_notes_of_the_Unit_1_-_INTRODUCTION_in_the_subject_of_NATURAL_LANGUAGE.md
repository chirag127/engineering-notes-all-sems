### Unsmoothed N-grams

- N-grams are a sequence of N words or tokens.
- Unsmoothed N-grams are a type of N-gram model where the probabilities of the N-grams are calculated directly from the counts in the training data.
- The probability of a word given the previous N-1 words is calculated as the count of the N-gram divided by the count of the N-1 gram.
- Unsmoothed N-grams can suffer from the problem of data sparsity, where N-grams that do not appear in the training data are assigned a probability of zero.
- This can lead to problems when trying to use the model to generate or recognize text, as unseen N-grams will be considered impossible.
- Smoothing techniques can be used to address this issue by assigning non-zero probabilities to unseen N-grams.
