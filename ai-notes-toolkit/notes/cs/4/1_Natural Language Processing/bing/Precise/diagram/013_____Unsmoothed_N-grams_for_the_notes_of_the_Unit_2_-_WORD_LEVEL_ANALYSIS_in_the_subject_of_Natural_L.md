### Unsmoothed N-grams

- N-grams are a sequence of N words or tokens, where N is a positive integer.
- Unsmoothed N-grams are a type of N-gram model where the probability of a word or token is calculated based on its frequency in the training data.
- Unsmoothed N-grams do not account for unseen or rare words or tokens, which can result in zero probabilities and affect the performance of the model.
- To address this issue, smoothing techniques can be applied to N-gram models to assign non-zero probabilities to unseen or rare words or tokens.
- Common smoothing techniques include Laplace smoothing, Good-Turing smoothing, and Kneser-Ney smoothing.
- Unsmoothed N-grams can be useful for certain applications, such as language identification or text classification, where the presence or absence of specific words or tokens is important.
- However, for tasks such as language generation or machine translation, smoothed N-grams are generally preferred due to their ability to handle unseen or rare words or tokens.
