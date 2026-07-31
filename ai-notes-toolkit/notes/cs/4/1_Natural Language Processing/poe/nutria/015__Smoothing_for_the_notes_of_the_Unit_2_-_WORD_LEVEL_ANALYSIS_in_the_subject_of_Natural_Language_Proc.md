
### Smoothing for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

* Smoothing is a technique used in Natural Language Processing to reduce the impact of data sparsity.
* It is used to estimate the probability of a word given a context, even when the word is not seen in the training data.
* Smoothing techniques include Laplace Smoothing, Good-Turing Smoothing, and Kneser-Ney Smoothing.
* Laplace Smoothing assigns a probability of 1/(n+1) to all unseen words, where n is the size of the vocabulary.
* Good-Turing Smoothing assigns a probability of (c+1)/(N+1) to all unseen words, where c is the count of the word in the training data and N is the total number of words in the training data.
* Kneser-Ney Smoothing assigns a probability to unseen words based on the probability of the words that come before it in the training data.