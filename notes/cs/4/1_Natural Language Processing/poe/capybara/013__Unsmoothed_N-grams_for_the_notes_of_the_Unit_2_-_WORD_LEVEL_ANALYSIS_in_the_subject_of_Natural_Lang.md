### Unsmoothed N-grams for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

In natural language processing, Unsmoothed N-grams is an important technique used in word level analysis. Here are some key points to understand this technique:

- Unsmoothed N-grams is a statistical language modeling technique used to predict the probability of a word based on its previous N-1 words.
- It is called "Unsmoothed" because it does not account for unseen words in the training data. This means that if a word appears in the test data that was not seen in the training data, the model will assign a probability of zero to it.
- Unsmoothed N-grams can be used for both language modeling and text classification tasks.
- The most commonly used value of N is 2 or 3, which means that the model predicts the probability of a word based on the previous one or two words.
- The probability of a word given its context can be calculated using the formula P(w_n|w_1,w_2,...,w_n-1) = C(w_1,w_2,...,w_n)/C(w_1,w_2,...,w_n-1), where C(w_1,w_2,...,w_n) is the count of the n-gram in the training data.
- Unsmoothed N-grams suffer from the problem of sparsity, which means that the probability of an n-gram with zero count in the training data will be zero. This can be addressed by smoothing techniques such as Laplace smoothing or Good-Turing smoothing.
- Unsmoothed N-grams are widely used in applications such as speech recognition, machine translation, and text generation.

In conclusion, Unsmoothed N-grams is an important technique in natural language processing for word level analysis. It is a simple yet effective way to predict the probability of a word given its context. However, it suffers from the problem of sparsity, which can be addressed by smoothing techniques.