### Unsmoothed N-grams

- N-grams are a sequence of N words or tokens.
- Unsmoothed N-grams are a type of N-gram model where the probability of a word is calculated based on the frequency of its occurrence in the training data.
- The probability of a word is calculated as the number of times the word appears in the training data divided by the total number of words in the training data.
- Unsmoothed N-grams do not account for words that do not appear in the training data.
- This can result in zero probabilities for unseen words, which can cause problems when calculating the probability of a sentence or document.
- One solution to this problem is to use smoothing techniques, which assign a small probability to unseen words.
- Unsmoothed N-grams are commonly used in language modeling and text classification tasks.
- They can be used to predict the next word in a sequence, or to classify a document into a particular category.
- Unsmoothed N-grams can be calculated for any value of N, with larger values of N capturing more context and resulting in more accurate predictions.
- However, as the value of N increases, the number of possible N-grams also increases, which can result in data sparsity and overfitting.
- Unsmoothed N-grams are a simple and effective method for language modeling and text classification, but they have limitations and should be used in conjunction with other techniques.