### Smoothing for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing
Smoothing is a technique used in NLP to address the issue of unseen words or events in language modeling. It adjusts the probabilities assigned to words or events to account for the fact that some words or events may not have been seen in the training data. Smoothing methods include:

1. Add-k smoothing: Adds a constant k to the count of each word, effectively giving all words a minimum count.
2. Laplace smoothing (Add-1 smoothing): Adds 1 to the count of each word. 
3. Good-Turing smoothing: Replaces the count of each word with a modified count based on the frequency of the word in the training data.
4. Interpolation smoothing: Combines the probabilities of different models (e.g. unigram, bigram) by weighting them.
5. Backoff smoothing: Falls back to a lower-order model (e.g. unigram) when the higher-order model (e.g. bigram) has insufficient data.
