### Unsmoothed N-grams for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

Unsmoothed N-grams are a type of statistical language model used in Natural Language Processing (NLP) that calculate the probability of a word or sequence of words occurring in a text based on the frequency of their occurrence in a training corpus. 

Here are some key points to understand about Unsmoothed N-grams:

1. N-grams represent sequences of 'n' words in a text, where 'n' can be any positive integer. 
2. Unsmoothed N-grams are called 'unsmoothed' because they do not use any smoothing techniques to adjust the probabilities of rare or unseen words or sequences. 
3. The probability of an N-gram is calculated using the formula: P(w_n | w_1, w_2, ..., w_{n-1}) = count(w_1, w_2, ..., w_n) / count(w_1, w_2, ..., w_{n-1})
4. Unsmoothed N-grams suffer from the problem of zero probabilities, where words or sequences that are not present in the training corpus have a probability of zero, leading to poor performance in predicting unseen data.
5. Unsmoothed N-grams can be used for tasks such as language modeling, text classification, and machine translation. 
6. To overcome the problem of zero probabilities, smoothing techniques such as Laplace smoothing or Good-Turing smoothing can be applied to adjust the probabilities of rare or unseen words or sequences.

Some learning tricks and mnemonics for Unsmoothed N-grams include:

- Remember the formula for calculating the probability of an N-gram: P(w_n | w_1, w_2, ..., w_{n-1}) = count(w_1, w_2, ..., w_n) / count(w_1, w_2, ..., w_{n-1})
- Practice calculating the probabilities of N-grams on small text examples to get a better understanding of how they work.
- Remember that Unsmoothed N-grams do not adjust for rare or unseen words or sequences, which can lead to poor performance in predicting unseen data.
- Think about the limitations of Unsmoothed N-grams and the need for smoothing techniques to overcome these limitations. 

Overall, Unsmoothed N-grams are an important concept to understand in the field of Natural Language Processing, as they are used in a variety of language modeling and text analysis tasks. By understanding their strengths and limitations, we can better apply them to real-world problems and develop more accurate and effective NLP models.