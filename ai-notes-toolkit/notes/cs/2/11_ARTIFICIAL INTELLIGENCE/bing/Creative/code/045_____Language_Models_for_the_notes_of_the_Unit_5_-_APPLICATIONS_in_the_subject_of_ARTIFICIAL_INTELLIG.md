# Language Models

- A language model is an AI model that has been trained to predict the next word or words in a text based on the preceding words.
- Language models are useful for various natural language processing tasks, such as speech recognition, machine translation, text summarization, text generation, etc.
- Language models can be classified into two categories: statistical and neural.

## Statistical Language Models

- Statistical language models use probability theory to estimate the likelihood of a word or a sequence of words in a given text.
- Statistical language models can be further divided into three types: unigram, n-gram, and exponential.

### Unigram Language Model

- A unigram language model assumes that each word in a text is independent of the other words, and assigns a probability to each word based on its frequency in the training data.
- A unigram language model can be written as:

P(w1, w2, ..., wn) = P(w1) * P(w2) * ... * P(wn)

- where P(wi) is the probability of word wi in the vocabulary.
- A unigram language model is simple and fast to compute, but it ignores the context and the order of the words, and often produces nonsensical sentences.

### N-gram Language Model

- An n-gram language model assumes that each word in a text depends on the previous n-1 words, and assigns a probability to each word based on its frequency in the training data as part of an n-gram.
- An n-gram is a sequence of n words, such as "the cat", "a big dog", etc.
- An n-gram language model can be written as:

P(w1, w2, ..., wn) = P(w1) * P(w2 | w1) * ... * P(wn | wn-1, ..., w1)

- where P(wi | wi-1, ..., wi-n+1) is the conditional probability of word wi given the previous n-1 words.
- An n-gram language model can capture the context and the order of the words, but it suffers from data sparsity and scalability issues, as the number of possible n-grams grows exponentially with n and the vocabulary size.

### Exponential Language Model

- An exponential language model is a generalization of the n-gram language model, where the probability of each word is computed as a weighted sum of features that depend on the previous words.
- An exponential language model can be written as:

P(wi | wi-1, ..., w1) = exp(sum_j (lambda_j * f_j(wi, wi-1, ..., w1))) / Z(wi-1, ..., w1)

- where lambda_j are the weights, f_j are the features, and Z is a normalization factor.
- An exponential language model can overcome the data sparsity and scalability issues of the n-gram language model, by using fewer and more informative features, but it requires more complex optimization methods to estimate the weights.

## Neural Language Models

- Neural language models use neural networks to learn the probability distribution of words in a text, based on the preceding words.
- Neural language models can be further divided into three types: feedforward, recurrent, and transformer.

### Feedforward Language Model

- A feedforward language model is a neural network that takes as input a fixed-size window of n-1 words, and outputs a probability distribution over the vocabulary for the next word.
- A feedforward language model can be written as:

P(wi | wi-1, ..., wi-n+1) = softmax(W * h + b)

- where W and b are the output layer parameters, h is the hidden layer activation, and softmax is a function that normalizes the output to sum to one.
- A feedforward language model can learn more complex features than the n-gram language model, but it still has a limited context size and cannot capture long-term dependencies.

### Recurrent Language Model

- A recurrent language model is a neural network that takes as input one word at a time, and outputs a probability distribution over the vocabulary for the next word, while maintaining a hidden state that encodes the history of the previous words.
- A recurrent language model can be written as:

P(wi | wi-1, ..., w1) = softmax(W * h_i + b)

h_i = f(U * wi + V * h_i-1)

- where W, b, U, and V are the network parameters, h_i is the hidden state