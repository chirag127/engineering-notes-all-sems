### Unit 1 - INTRODUCTION: Smoothing

- Smoothing is a technique used in natural language processing to address the problem of zero probabilities.
- When building language models, it is common to encounter words or sequences of words that have not been seen before in the training data. This can result in a zero probability estimate, which can cause problems when calculating the probability of a sentence or document.
- Smoothing methods adjust the probability estimates to avoid zero probabilities and improve the performance of the language model.
- There are several smoothing techniques, including Laplace smoothing, Good-Turing smoothing, and Kneser-Ney smoothing.
- Laplace smoothing, also known as additive smoothing, involves adding a small constant to the count of each word or sequence of words. This has the effect of increasing the probability of unseen words or sequences.
- Good-Turing smoothing adjusts the probability estimates based on the frequency of words or sequences of words that have been seen once, twice, etc. in the training data.
- Kneser-Ney smoothing is a more advanced technique that takes into account the context in which words appear. It adjusts the probability estimates based on the number of different contexts in which a word or sequence of words has been seen.
- Smoothing is an important concept in natural language processing and is essential for building effective language models.