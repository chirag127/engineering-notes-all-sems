
### Smoothing for the Notes of the Unit 2 - WORD LEVEL ANALYSIS in the Subject of Natural Language Processing

Smoothing is a technique used in Natural Language Processing (NLP) to improve the accuracy of language models. It is applied when the data is sparse, meaning that there are many unseen words in the corpus. Smoothing is used to reduce the effect of data sparsity by assigning a small probability to all unseen words.

There are several methods of smoothing, including Laplace Smoothing, Good-Turing Smoothing, Kneser-Ney Smoothing and Katz Smoothing.

**Laplace Smoothing**

Laplace Smoothing is also known as “add-one smoothing” because it adds one to the count of each word in the corpus. This is done to prevent zero-frequency words from having zero probability. The probability of a word is calculated as follows: 

P(w) = (C(w) + 1) / (N + V)

Where C(w) is the count of the word in the corpus, N is the total number of words in the corpus, and V is the number of different words in the corpus.

**Good-Turing Smoothing**

Good-Turing Smoothing is a method of smoothing that assigns a higher probability to words that appear more frequently in the corpus. The probability of a word is calculated as follows:

P(w) = (C(w) + 1) / (N + V)

Where C(w) is the count of the word in the corpus, N is the total number of words in the corpus, and V is the number of different words in the corpus.

**Kneser-Ney Smoothing**

Kneser-Ney Smoothing is a method of smoothing that assigns a higher probability to words that appear more frequently in the corpus. The probability of a word is calculated as follows:

P(w) = max(C(w) - d, 0) / N + (d * P(w|w-1))

Where C(w) is the count of the word in the corpus, N is the total number of words in the corpus, and d is a discounting parameter.

**Katz Smoothing**

Katz Smoothing is a method of smoothing that assigns a higher probability to words that appear more frequently in the corpus. The probability of a word is calculated as follows:

P(w) = max(C(w) - d, 0) / N + (d * P(w|w-1))

Where C(w) is the count of the word in the corpus, N is the total number of words in the corpus, and d is a discounting parameter.

Smoothing is an important technique in NLP and can be used to improve the accuracy of language models. It is important to choose the right smoothing method for the task at hand.