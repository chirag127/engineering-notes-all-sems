# Language Models

- A language model is an artificial intelligence system that has been trained to predict the next word or words in a text based on the preceding words.
- Language models are useful for various natural language processing tasks, such as speech recognition, machine translation, text summarization, text generation, and question answering.
- Language models can be classified into two broad categories: statistical language models and neural language models.

## Statistical Language Models

- Statistical language models use probability theory and statistics to estimate the likelihood of a word or a sequence of words in a given text.
- Statistical language models can be further divided into subtypes based on the number of words they consider in the context: unigram, bigram, trigram, n-gram, and exponential language models.

### Unigram Language Model

- A unigram language model assumes that each word in a text is independent of the other words, and assigns a probability to each word based on its frequency in the training data.
- A unigram language model can be written as:

P(w<sub>1</sub>, w<sub>2</sub>, ..., w<sub>n</sub>) = P(w<sub>1</sub>) * P(w<sub>2</sub>) * ... * P(w<sub>n</sub>)

- A unigram language model is simple and fast to compute, but it ignores the word order and the context, and therefore produces poor results for complex texts.

### N-gram Language Model

- An n-gram language model assumes that each word in a text depends on the previous n-1 words, and assigns a probability to each word based on its frequency in the n-gram context in the training data.
- An n-gram language model can be written as:

P(w<sub>1</sub>, w<sub>2</sub>, ..., w<sub>n</sub>) = P(w<sub>1</sub>) * P(w<sub>2</sub> | w<sub>1</sub>) * ... * P(w<sub>n</sub> | w<sub>n-1</sub>, ..., w<sub>n-n+1</sub>)

- An n-gram language model is more accurate and realistic than a unigram language model, but it requires a large amount of training data and memory to store the n-gram probabilities, and it suffers from data sparsity and out-of-vocabulary issues.

### Exponential Language Model

- An exponential language model is a generalization of the n-gram language model, where the probability of each word is a weighted combination of features that depend on the context.
- An exponential language model can be written as:

P(w<sub>i</sub> | w<sub>i-1</sub>, ..., w<sub>i-n+1</sub>) = exp(∑<sub>j</sub>λ<sub>j</sub>f<sub>j</sub>(w<sub>i</sub>, w<sub>i-1</sub>, ..., w<sub>i-n+1</sub>)) / Z(w<sub>i-1</sub>, ..., w<sub>i-n+1</sub>)

- Where f<sub>j</sub> are the features, λ<sub>j</sub> are the weights, and Z is the normalization factor.
- An exponential language model is more flexible and expressive than an n-gram language model, but it is more difficult to estimate the parameters and to compute the probabilities.

## Neural Language Models

- Neural language models use artificial neural networks to learn the representations and the dependencies of words in a text.
- Neural language models can be further divided into subtypes based on the architecture and the training method of the neural network: feedforward neural network language model, recurrent neural network language model, transformer language model, and large language model.

### Feedforward Neural Network Language Model

- A feedforward neural network language model is a neural network that takes a fixed number of previous words as input, and outputs a probability distribution over the vocabulary for the next word.
- A feedforward neural network language model can be written as:

P(w<sub>i</sub> | w<sub>i-1</sub>, ..., w<sub>i-n+1</sub>) = softmax(W<sub>2</sub>h + b<sub>2</sub>)

- Where h =