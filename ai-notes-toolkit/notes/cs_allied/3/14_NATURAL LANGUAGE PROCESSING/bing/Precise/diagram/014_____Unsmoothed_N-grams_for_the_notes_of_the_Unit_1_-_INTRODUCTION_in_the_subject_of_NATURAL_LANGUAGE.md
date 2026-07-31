### Unit 1 - INTRODUCTION: Unsmoothed N-grams

- N-grams are a type of probabilistic language model used in natural language processing.
- An N-gram model predicts the probability of the next word in a sequence based on the previous N-1 words.
- Unsmoothed N-grams do not apply any smoothing techniques to the probabilities.
- This means that if an N-gram has not been seen in the training data, its probability is estimated to be zero.
- This can lead to problems when dealing with unseen N-grams in new data.
- Smoothing techniques can be applied to N-gram models to address this issue.
- Common smoothing techniques include Laplace smoothing, Good-Turing smoothing, and Kneser-Ney smoothing.
- Unsmoothed N-grams can still be useful in certain applications, but smoothed N-grams are generally preferred for their improved performance.
