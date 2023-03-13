### Statistical LM for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

A statistical language model (LM) is a probability distribution over sequences of words. It assigns a probability to every possible sentence or text in a given language. A statistical LM can be used for various natural language processing (NLP) tasks, such as speech recognition, machine translation, text summarization, etc.

One of the simplest and most widely used statistical LMs is the n-gram model, which approximates the probability of a word given its previous n-1 words. For example, a bigram model (n=2) estimates the probability of a word given its previous word, while a trigram model (n=3) estimates the probability of a word given its previous two words.

The following diagram illustrates the basic architecture of a n-gram model:

```
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  Word 1        |    |  Word 2        |    |  Word 3        |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       V                     V                     V
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  P(Word 1)     |    |  P(Word 2|     |    |  P(Word 3|     |
|                |    |  Word 1)       |    |  Word 1,       |
+----------------+    +----------------+    |  Word 2)       |
                                            |                |
                                            +----------------+
```

The probability of a word is computed by using the counts of the n-grams in a large corpus of text. For example, the probability of the word "dog" given the previous word "the" can be estimated by dividing the number of times "the dog" appears in the corpus by the number of times "the" appears in the corpus. Similarly, the probability of the word "barked" given the previous two words "the dog" can be estimated by dividing the number of times "the dog barked" appears in the corpus by the number of times "the dog" appears in the corpus.

The probability of a sentence or a text can be obtained by multiplying the probabilities of the words in the sequence. For example, the probability of the sentence "the dog barked" can be computed by multiplying the probabilities of the words "the", "dog", and "barked" given their previous words:

P(the dog barked) = P(the) * P(dog|the) * P(barked|the dog)

However, n-gram models have some limitations, such as data sparsity, out-of-vocabulary words, and lack of semantic and syntactic information. Therefore, more advanced statistical LMs have been developed, such as neural network LMs, which use deep learning techniques to learn the probability distribution over words.