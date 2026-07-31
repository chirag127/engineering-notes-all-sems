### Unsmoothed N-grams

- N-grams are a sequence of N words or tokens, used to model language and predict the next word in a sequence.
- Unsmoothed N-grams are a basic form of N-grams, where the probability of a word is calculated based on the frequency of its occurrence in the training data.
- The probability of a word given the previous N-1 words is calculated as the count of the N-gram divided by the count of the (N-1)-gram.
- Unsmoothed N-grams suffer from the problem of data sparsity, where N-grams that have not been seen in the training data are assigned a probability of zero.
- This can lead to poor performance when dealing with unseen data, as the model is unable to assign a non-zero probability to unseen N-grams.
- Smoothing techniques are used to address this issue by assigning non-zero probabilities to unseen N-grams.
