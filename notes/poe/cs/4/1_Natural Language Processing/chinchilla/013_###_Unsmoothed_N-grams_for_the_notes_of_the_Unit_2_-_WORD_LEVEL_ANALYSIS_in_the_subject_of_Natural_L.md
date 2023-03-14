### Unsmoothed N-grams for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

N-grams are a sequence of n words that occur together in a text. They are an essential tool in natural language processing, used for language modeling, speech recognition, and text prediction. Unsmoothed N-grams are a type of N-gram model that does not use any smoothing techniques to handle unknown words. In this article, we will explore Unsmoothed N-grams and their applications in NLP.

#### What are Unsmoothed N-grams? 

Unsmoothed N-grams are a type of N-gram model that calculates the probability of a word sequence by simply counting the number of times it appeared in the training corpus. For example, if we have a bigram model that counts the number of times the word 'the' appears after the word 'in,' the probability of the bigram 'in the' is calculated as follows:

P(the|in) = count(in the) / count(in)

Where count(in the) is the number of times the bigram 'in the' appears in the training corpus, and count(in) is the number of times the word 'in' appears in the training corpus.

#### Advantages of Unsmoothed N-grams

- Simple and easy to implement
- Good for small datasets
- Can capture local dependencies between words

#### Disadvantages of Unsmoothed N-grams

- Not suitable for large datasets
- Cannot handle unknown words
- Can lead to zero probabilities for unseen n-grams, resulting in inaccurate language modeling

#### Mnemonics and Learning Tricks

- To remember the formula for calculating the probability of a bigram in Unsmoothed N-grams, use the phrase "count of bigram divided by count of first word". For example, "P(the|in) = count of in the / count of in the".
- To remember the advantages of Unsmoothed N-grams, use the acronym "SGC": Simple, Good for small datasets, Captures local dependencies.

#### Applications of Unsmoothed N-grams

- Language modeling
- Text prediction
- Speech recognition

#### Example

Let's say we have a corpus of four sentences:

- The cat in the hat
- The sun in the sky
- The cat on the mat
- The dog on the log

We want to calculate the probability of the bigram 'cat in' using Unsmoothed N-grams. We count the number of times the bigram 'cat in' appears in the corpus, which is 1. We also count the number of times the word 'cat' appears in the corpus, which is 2. Therefore, the probability of the bigram 'cat in' is:

P(in|cat) = count(cat in) / count(cat) = 1/2

#### Conclusion

Unsmoothed N-grams are a simple and easy-to-implement N-gram model that can be useful for small datasets and capturing local dependencies between words. However, they are not suitable for large datasets and cannot handle unknown words. It's important to understand the advantages and disadvantages of Unsmoothed N-grams before using them in NLP applications.