# Recurrent networks

Recurrent networks are a type of artificial neural networks that can process sequential data or time series data. They have an internal memory that allows them to store information from previous inputs and use it to influence the current input and output. They are commonly used for tasks such as natural language processing, speech recognition, image captioning, and machine translation.

Some of the main concepts and algorithms related to recurrent networks are:

- **Recurrent neural network (RNN)**: The basic architecture of a recurrent network, where each hidden unit receives input from the current input and the previous hidden state. The output is computed from the current hidden state. The network is trained using backpropagation through time (BPTT), which involves unrolling the network over time and applying the chain rule to compute the gradients.

- **Long short-term memory (LSTM)**: A variant of RNN that can overcome the problem of vanishing or exploding gradients, which occurs when the network is trained over long sequences. LSTM introduces a memory cell and three gates (input, output, and forget) that control the flow of information in and out of the cell. LSTM can learn long-term dependencies and handle complex sequential data.

- **Gated recurrent unit (GRU)**: A simplified version of LSTM that has only two gates (reset and update) and no separate memory cell. GRU is computationally more efficient than LSTM and can achieve similar performance on some tasks.

- **Bidirectional RNN (BiRNN)**: A network that processes the input sequence from both directions (forward and backward) and concatenates the hidden states from both directions to form the output. BiRNN can capture both past and future context and improve the performance on tasks such as sequence labeling and sentiment analysis.

- **Echo state network (ESN)**: A network that has a large and randomly initialized recurrent layer (called the reservoir) and a trainable output layer. The reservoir acts as a dynamic memory that can generate rich temporal features from the input. The output layer is trained using linear regression or ridge regression. ESN is a type of reservoir computing, which is a framework for training recurrent networks with fixed weights.

- **Neural Turing machine (NTM)**: A network that combines a recurrent network with an external memory that can be read from and written to. The network learns to manipulate the memory using a controller (which can be an RNN or an LSTM) and a set of read and write heads. NTM can learn to perform algorithmic tasks such as copying, sorting, and addition.