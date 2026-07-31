### Unsmoothed N-grams for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing.

In natural language processing, N-gram models are widely used to predict the probability of a word appearing in a sentence given the previous words. Unsmoothed N-grams are a type of N-gram model that does not use any smoothing techniques to account for unseen words or sequences. Here are some important points to understand about Unsmoothed N-grams:

- Unsmoothed N-grams are a type of probabilistic language model used to predict the probability of a word given its previous context in a sentence.
- They are called "unsmoothed" because they do not use any smoothing techniques to account for words or sequences that are not present in the training data.
- The probability of a word given its context is calculated as the frequency of the word in that context divided by the frequency of the context in the training data.
- Unsmoothed N-grams suffer from the problem of zero probabilities, where the probability of a word given a context is zero if that word or context is not present in the training data.
- This can lead to poor performance on unseen data or data with rare words or sequences.
- Unsmoothed N-grams are easy to implement and computationally efficient, making them a good starting point for language modeling tasks.
- They are commonly used in applications such as speech recognition, machine translation, and text generation.
- To overcome the problem of zero probabilities, smoothing techniques such as Laplace smoothing or Good-Turing smoothing can be used to adjust the probabilities of unseen words and contexts.
- Overall, Unsmoothed N-grams provide a simple and effective way to model language, but they are limited by their inability to handle unseen words and sequences.