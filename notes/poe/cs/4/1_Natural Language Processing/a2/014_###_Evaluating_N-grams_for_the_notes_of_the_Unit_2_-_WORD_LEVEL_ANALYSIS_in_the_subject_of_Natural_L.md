 Here is the content in markdown format:

### Evaluating N-grams for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

N-grams are sequences of n words from a given text. They are widely used in Natural Language Processing for various tasks like:

- Language Modelling: Predicting the next word in a sentence based on the previous words.
- Text Classification: Identifying the topic or sentiment of a document.
- Plagiarism Detection: Finding similarities between documents.

Following are some ways to evaluate N-grams:

1. Frequency: The frequency of an N-gram can indicate its significance. Common word combinations occuring more frequently can be good indicators of context.
However, very high frequency N-grams like "the", "a", "is", etc. may not carry much meaning. Hence, frequency should be used along with other metrics.

2. Pointwise Mutual Information (PMI): It measures how much more or less likely it is to observe two words together than separately. A high PMI indicates a strong association between the words.
PMI(w1, w2) = log[(P(w1,w2)/P(w1)P(w2))](w1, w2 are words)

3. Log Likelihood Ratio (LLR): It is similar to PMI but uses log likelihood instead of mutual information.
LLR(w1, w2) = log[P(w1,w2)/P(w1)P(w2)]

4. Perplexity: It evaluates how well a language model predicts the next word. A lower perplexity indicates the model is better at predicting the next word.
Perplexity = exp(-1/N ∑logP(wi|w1...wi-1)) (where N is number of words and P is predicted probability of each word)

These are some common ways to evaluate N-grams. Based on the use case, a suitable metric can be chosen and optimized to get the best N-grams.