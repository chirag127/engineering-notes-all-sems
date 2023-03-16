### Unsmoothed N-grams

- N-grams are a sequence of N words or tokens, used to predict the next word in a sentence.
- Unsmoothed N-grams do not use any smoothing techniques to account for unseen N-grams.
- The probability of an N-gram is calculated by counting the number of times it appears in the training data and dividing it by the total number of N-grams.
- Unsmoothed N-grams can result in zero probabilities for unseen N-grams, which can cause problems when trying to predict the next word in a sentence.
- To avoid zero probabilities, smoothing techniques such as Laplace smoothing or Good-Turing smoothing can be used.
- Unsmoothed N-grams are a simple and effective way to model language, but they have limitations and can be improved with smoothing techniques.
