### Language Models

- A language model is an AI model that has been trained to predict the next word or words in a text based on the preceding words.
- Language models are useful for various natural language processing tasks, such as speech recognition, machine translation, text summarization, text generation, and question answering.
- Language models can be classified into two categories: statistical language models and neural language models.

#### Statistical Language Models

- Statistical language models use probability theory and statistics to estimate the likelihood of a word or a sequence of words in a given text.
- Statistical language models can be further divided into three types: unigram, n-gram, and exponential.

##### Unigram Language Model

- A unigram language model assumes that each word in a text is independent of the other words, and assigns a probability to each word based on its frequency in the training data.
- A unigram language model can be written as:

$$P(w_1, w_2, ..., w_n) = \prod_{i=1}^n P(w_i)$$

- where $w_i$ is the $i$-th word in the text, and $P(w_i)$ is the probability of the word $w_i$.
- A unigram language model is simple and easy to compute, but it ignores the context and the order of the words, and therefore produces poor results for long and complex texts.

##### N-gram Language Model

- An n-gram language model assumes that each word in a text depends on the previous $n-1$ words, and assigns a probability to each word based on its frequency in the training data along with its preceding $n-1$ words.
- An n-gram language model can be written as:

$$P(w_1, w_2, ..., w_n) = \prod_{i=1}^n P(w_i | w_{i-n+1}, ..., w_{i-1})$$

- where $w_i$ is the $i$-th word in the text, and $P(w_i | w_{i-n+1}, ..., w_{i-1})$ is the conditional probability of the word $w_i$ given the previous $n-1$ words.
- An n-gram language model captures the context and the order of the words, and therefore produces better results than a unigram language model, but it suffers from data sparsity and scalability issues, as the number of possible n-grams grows exponentially with the size of the vocabulary and the value of $n$.

##### Exponential Language Model

- An exponential language model is a generalization of the n-gram language model, where the probability of each word is computed as a weighted sum of features that depend on the previous words.
- An exponential language model can be written as:

$$P(w_i | w_{i-n+1}, ..., w_{i-1}) = \frac{\exp(\sum_{k=1}^K \lambda_k f_k(w_i, w_{i-n+1}, ..., w_{i-1}))}{\sum_{w \in V} \exp(\sum_{k=1}^K \lambda_k f_k(w, w_{i-n+1}, ..., w_{i-1}))}$$

- where $w_i$ is the $i$-th word in the text, $V$ is the vocabulary, $K$ is the number of features, $\lambda_k$ is the weight of the $k$-th feature, and $f_k(w_i, w_{i-n+1}, ..., w_{i-1})$ is the value of the $k$-th feature for the word $w_i$ and its preceding $n-1$ words.
- An exponential language model allows more flexibility and expressiveness than an n-gram language model, but it is more difficult to estimate the optimal values of the weights and the features, and it is more computationally expensive to evaluate.

#### Neural Language Models

- Neural language models use artificial neural networks to learn the probability distribution of words in a text based on the preceding words.
- Neural language models can be further divided into three types: feedforward, recurrent, and transformer.

##### Feedforward Neural Language Model

- A feedforward neural language model is a type of neural network that takes the previous $