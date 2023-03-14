Recurrent Neural Network Language Models (RNNLMs) are a type of neural network language models that use recurrent neural networks (RNNs) to model the sequential data such as sentences in natural language. RNNs are neural networks that have feedback loops in their hidden layers, allowing them to store and process previous information. This makes them suitable for modeling the dependencies and context in natural language.

The following diagram illustrates the basic architecture of a RNNLM:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Input Layer   |     |   Input Layer   |     |   Input Layer   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       V                      V                      V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Hidden Layer   |---->|  Hidden Layer   |---->|  Hidden Layer   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       V                      V                      V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Output Layer   |     |  Output Layer   |     |  Output Layer   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       V                      V                      V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Predicted Word |     |  Predicted Word |     |  Predicted Word |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The input layer takes one word at a time from the input sequence and encodes it as a one-hot vector or an embedding vector. The hidden layer computes a hidden state based on the current input and the previous hidden state. The output layer computes a probability distribution over the vocabulary based on the current hidden state. The predicted word is the word with the highest probability in the output layer. The hidden state is then passed to the next time step as the previous hidden state.

The RNNLM can be trained using backpropagation through time (BPTT), which is a variant of gradient descent that unrolls the RNN for a fixed number of time steps and computes the gradients with respect to the parameters. The objective function is usually the cross-entropy loss between the predicted words and the target words.

RNNLMs can capture long-range dependencies and context in natural language, but they also suffer from some drawbacks, such as the vanishing or exploding gradient problem, the difficulty of modeling rare words, and the high computational cost. Some variants and extensions of RNNLMs have been proposed to address these issues, such as long short-term memory (LSTM), gated recurrent unit (GRU), bidirectional RNN, neural Turing machine (NTM), and differentiable neural computer (DNC).