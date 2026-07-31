 Here is the content in Markdown format without any emojis or external links:

### Statistical LM for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

1. Statistical language models estimate the probability of a sequence of words. They are used to predict the next word in a sequence.
2. The probability of a sentence is estimated as the product of probabilities of each word in the sentence.
3. The main types of Statistical LMs are:
- Unigram: Probability of a word depends only on the previous word.
- Bigram: Probability of a word depends on the previous two words.
- Trigram: Probability of a word depends on the previous three words.
4. As we increase the 'gram', the LM captures more context but suffers from data sparsity.
5. To handle data sparsity, smoothing techniques are used like:
- Add-one smoothing: Replace zero probabilities with a small non-zero value.
- Good-Turing smoothing: Use probabilities of less frequent events to estimate probabilities of more infrequent events.
6. Cross-entropy is used as a metric to evaluate the performance of a language model. The language model with lower cross-entropy is preferred.

The content is written in a formal tone with points and without any emojis or external links as per the instructions. Please let me know if you would like me to modify or expand the content in any way.