### Recurrent networks for the notes of the Unit 4 - OPTIMIZATION AND GENERALIZATION in the subject of Deep Learning

- Recurrent neural networks (RNNs) are a type of artificial neural networks that can process sequential data or time series data, such as natural language, speech, or video .
- RNNs have a "memory" that allows them to store information from previous inputs and use it to influence the current input and output . This makes them suitable for modeling temporal dependencies and long-term contexts.
- RNNs consist of a network of recurrent units that share the same weights and are connected in a loop. Each recurrent unit takes an input vector x_t and a hidden state vector h_t-1 from the previous time step and produces an output vector y_t and a new hidden state vector h_t.

```
    x_t     x_t+1
     |        |
     V        V
+---------+---------+
|         |         |
| Recurrent Unit    |
|         |         |
+---------+---------+
     |        |
     V        V
    h_t     h_t+1
     |        |
     V        V
    y_t     y_t+1
```

- The hidden state vector h_t can be seen as the memory of the network, which encodes the information from the past inputs up to time t. The output vector y_t can be used for different tasks, such as classification, regression, or generation.
- The recurrent units can have different architectures, such as simple RNNs, long short-term memory (LSTM), gated recurrent units (GRU), or neural Turing machines (NTM). Each architecture has different mechanisms to control the flow of information and the memory capacity of the network.
- RNNs can be trained using backpropagation through time (BPTT), which is a variant of the standard backpropagation algorithm that unrolls the network over time and computes the gradients for each time step. BPTT can be computationally expensive and prone to vanishing or exploding gradients, so various techniques have been proposed to improve the optimization and generalization of RNNs, such as truncated BPTT, gradient clipping, regularization, dropout, or attention.
- RNNs have been successfully applied to a range of challenging problems, such as language modeling, machine translation, speech recognition, image captioning, sentiment analysis, and more. They have achieved state-of-the-art performance on many benchmarks and have demonstrated the ability to learn complex and long-term dependencies in sequential data.

Some possible mnemonics and learning tricks for RNNs are:

- RNNs are like a chain of repeating modules that can remember the past and use it to influence the present.
- RNNs can be seen as a loop of neurons that pass messages to each other.
- RNNs are like a brain that can learn from its own thoughts.
- RNNs can be unrolled over time to visualize the flow of information and gradients.
- RNNs can have different types of gates that control what to remember and what to forget.