# Language Modeling

- Language modeling is the task of estimating the probability of a given sequence of words occurring in a sentence  .
- Language models are trained on large collections of text data, called corpora, to learn the patterns and regularities of natural language.
- Language models can be used for various natural language processing applications, such as speech recognition, machine translation, text summarization, text generation, etc.
- Language models can be classified into two main types: **n-gram models** and **neural models**.

## N-gram models

- N-gram models are based on the assumption that the probability of a word depends only on the previous n-1 words, where n is a fixed integer.
- N-gram models use the **chain rule of probability** to decompose the probability of a word sequence into the product of conditional probabilities of each word given its n-1 predecessors.
- N-gram models are estimated by counting the frequencies of n-grams in the training corpus and applying smoothing techniques to deal with unseen or rare n-grams.
- N-gram models are simple and fast to compute, but they suffer from data sparsity and lack of generalization.

## Neural models

- Neural models are based on the idea of using neural networks to learn distributed representations of words and sentences, called **embeddings**.
- Neural models use the **softmax function** to compute the probability of a word given its context, which can be either the previous words, the surrounding words, or the whole sentence.
- Neural models are trained by optimizing a **loss function** that measures the discrepancy between the predicted probabilities and the true probabilities of the words in the training corpus.
- Neural models are more expressive and flexible than n-gram models, but they require more computational resources and data to train.