### Evaluating N-grams for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- N-grams are sequences of N words that are used to model natural language .
- N-grams can be used to capture the local context and dependencies of words in a text .
- N-grams can be extracted from a text by sliding a window of size N over the words and counting the frequency of each sequence .
- N-grams can be used to estimate the probability of a word given its previous N-1 words, using the formula:

P(w_n|w_1,...,w_n-1) = C(w_1,...,w_n) / C(w_1,...,w_n-1)

where C is the count of the n-gram in the text .

- N-grams can be used to generate text by sampling words according to their probabilities, given the previous words .
- N-grams have some limitations, such as data sparsity, overfitting, and lack of long-term dependencies .
- N-grams can be evaluated using various metrics, such as perplexity, accuracy, recall, precision, and F-measure .
- Perplexity measures how well an n-gram model predicts a test set. It is the inverse of the average probability of the test words, given by the model .
- Accuracy measures the percentage of correct predictions made by an n-gram model on a test set .
- Recall measures the proportion of relevant n-grams that are retrieved by an n-gram model from a test set .
- Precision measures the proportion of retrieved n-grams that are relevant to a test set .
- F-measure is the harmonic mean of precision and recall, and it balances the trade-off between them .