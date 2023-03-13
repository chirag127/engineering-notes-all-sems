### Language Modeling

- Language modeling is the task of estimating the probability of a sequence of words or symbols, such as a sentence or a document.
- Language models are useful for various natural language processing applications, such as speech recognition, machine translation, text summarization, text generation, etc.
- A language model can be formalized as a function that assigns a probability to any sequence of words or symbols, denoted by P(w_1, w_2, ..., w_n), where w_i is the i-th word or symbol in the sequence.
- A language model can be evaluated by its perplexity, which is a measure of how well the model predicts a test set of sequences. Perplexity is defined as the inverse of the geometric mean of the probabilities assigned by the model to each word or symbol in the test set, denoted by PP(w_1, w_2, ..., w_n) = (P(w_1, w_2, ..., w_n))^-1/n.
- A lower perplexity indicates a better language model, as it means the model assigns higher probabilities to the observed sequences.
- There are different types of language models, such as n-gram models, neural network models, and transformer models, which differ in how they estimate the probability of a sequence of words or symbols.