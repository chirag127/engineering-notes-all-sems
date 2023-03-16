### Unsmoothed N-grams

- N-grams are a sequence of N words or tokens, where N is a positive integer.
- Unsmoothed N-grams are a type of N-gram model where the probability of a word or token is calculated based on its frequency in the training data.
- The probability of a word or token is calculated by dividing the number of times it appears in the training data by the total number of N-grams in the training data.
- Unsmoothed N-grams do not account for unseen or rare words or tokens, which can result in zero probabilities.
- This can cause problems when using the model to generate text or make predictions, as zero probabilities can cause the model to assign zero probability to valid sequences of words or tokens.
- To address this issue, smoothing techniques can be applied to the N-gram model to assign non-zero probabilities to unseen or rare words or tokens.
- Common smoothing techniques include Laplace smoothing, Good-Turing smoothing, and Kneser-Ney smoothing.
- Unsmoothed N-grams can be useful for certain tasks, such as language identification or text classification, where the presence or absence of specific words or tokens is more important than their probabilities.
- However, for tasks such as language generation or machine translation, smoothed N-grams are generally preferred as they can better handle unseen or rare words or tokens.