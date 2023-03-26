 Here is the content in markdown format without any emojis or external links:

### Smoothing for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing.

1.  Smoothing is a technique used to avoid zero probabilities. When we calculate probability of a word, it may happen that the word has never occurred in the training data, then its probability would be zero according to Maximum Likelihood Estimation. To avoid this, we use Smoothing technique.
2.  Adding a fixed quantity to all counts: In this technique, we add a fixed quantity `c` to all counts. For example, if we add 1 to all counts, then the smoothed probability would be:

P(w|c) = (Count(w) + 1) / (Total Count + Vocabulary Size)

Here, vocabulary size is the total number of unique words in the corpus.
3.  Interpolation: In interpolation, we take a weighted average of the maximum likelihood probability and a fixed probability distribution (typically a uniform distribution). The basic formula is:

P(w) = λPML(w) + (1-λ)P(w)

Here, λ is the interpolation parameter whose value is between 0 and 1. PML(w) is the maximum likelihood probability and P(w) is the fixed distribution probability.
4.  Good-Turing Smoothing: This technique assumes that the probability of a word with count c occurring `n+1` times is the same as the probability of a word with count `c-1` occurring `n` times. The formula is:

P(*|w, c) = (c + 1) / (N + C(c))

Here, C(c) is the number of words with count c in the training data and N is the total number of words in the training data.