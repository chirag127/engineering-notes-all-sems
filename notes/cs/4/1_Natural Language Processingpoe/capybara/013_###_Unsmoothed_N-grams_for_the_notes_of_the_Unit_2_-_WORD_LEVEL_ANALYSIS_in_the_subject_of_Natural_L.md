### Unsmoothed N-grams for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

N-grams are the contiguous sequences of n items from a given sample of text or speech. N-grams are commonly used in Natural Language Processing (NLP) to model the probability of the next word in a sequence. In this regard, unsmoothed N-grams are one of the simplest models that can be used to predict the next word in a sequence.

Here are some points to help you understand the concept of unsmoothed N-grams in detail:

- Unsmoothed N-grams are based on the frequency of occurrence of n-grams in the training data. The probability of the next word in a sequence is calculated by dividing the frequency of the n-gram by the frequency of the (n-1)-gram that precedes it.

- For example, if we have a sentence "I love to eat pizza", the unsmoothed bigram model would calculate the probability of the word 'pizza' as the frequency of the bigram 'eat pizza' divided by the frequency of the unigram 'eat'.

- Unsmoothed N-grams suffer from the problem of zero probability. This means that if a particular n-gram is not present in the training data, its probability will be zero. This can lead to poor performance of the model when dealing with unseen data.

- One way to overcome the problem of zero probability is through smoothing techniques such as Laplace smoothing, which adds a small constant to the frequency of each n-gram to avoid zero probabilities.

- Some Mnemonics and learning tricks for unsmoothed N-grams include remembering that these models are based on the frequency of occurrence of n-grams in the training data, and that they suffer from the problem of zero probability. It is important to keep in mind that unsmoothed N-grams are one of the simplest models used in NLP, and more sophisticated models such as smoothed N-grams, neural networks, and deep learning models are used to improve the accuracy of language models.

In conclusion, unsmoothed N-grams are a simple yet effective model used in NLP to predict the next word in a sequence. However, they suffer from the problem of zero probability and can lead to poor performance when dealing with unseen data. Smoothing techniques such as Laplace smoothing can be used to overcome this problem. Remembering the basic concepts and limitations of unsmoothed N-grams can be helpful in understanding more complex models used in NLP.