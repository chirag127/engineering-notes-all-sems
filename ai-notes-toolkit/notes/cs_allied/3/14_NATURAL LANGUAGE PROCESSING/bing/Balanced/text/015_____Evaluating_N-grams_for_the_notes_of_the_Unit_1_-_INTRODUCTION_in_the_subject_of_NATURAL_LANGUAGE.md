### Evaluating N-grams for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- N-grams are sequences of N words that are used to model natural language .
- N-grams can be used to capture the local context and dependencies of words in a text .
- N-grams can be extracted from a text by sliding a window of size N over the words and counting the frequency of each sequence .
- N-grams can be used to estimate the probability of a word given its previous N-1 words, using the formula:

P(w<sub>N</sub>|w<sub>1</sub>,...,w<sub>N-1</sub>) = C(w<sub>1</sub>,...,w<sub>N</sub>)/C(w<sub>1</sub>,...,w<sub>N-1</sub>)

where C is the count function and P is the probability function .

- N-grams can be used to generate text by sampling words from the probability distribution given by the N-gram model .
- N-grams have some limitations, such as data sparsity, curse of dimensionality, and lack of long-term dependencies .
- N-grams can be evaluated using various metrics, such as perplexity, log-likelihood, cross-entropy, and accuracy .
- Perplexity measures how well the N-gram model predicts the test data, and is defined as the inverse of the geometric mean of the probabilities of each word in the test data .
- Log-likelihood measures how likely the N-gram model is to generate the test data, and is defined as the sum of the logarithms of the probabilities of each word in the test data .
- Cross-entropy measures the average number of bits needed to encode the test data using the N-gram model, and is defined as the negative of the log-likelihood divided by the number of words in the test data .
- Accuracy measures how often the N-gram model predicts the correct word, and is defined as the ratio of the number of correct predictions to the total number of predictions .