 Here is the markdown formatted notes on Recurrent Neural Networks for the given topic:

### Recurrent Neural Networks

1. Recurrent Neural Networks are a type of neural networks that make use of sequential information and have feedback connections which allow the network to persist its internal state.
2. They are widely used for tasks such as speech recognition, machine translation, predicting stochastic sequences, etc.
3. The basic architecture of a Recurrent Neural Network contains an input layer, hidden layer(s) and an output layer. The hidden layer receives feedback from its own previous outputs.
4. The hidden state (output) at any time t, ht, depends on the previous hidden state h_(t-1) and the current input xt. This can be represented as:
ht = f(ht-1, xt)
where f is an activation function like tanh or ReLU.
5. Backpropagation Through Time (BPTT) is used to train Recurrent Neural Networks by unfolding the network in time and applying standard backpropagation.
6. Some variants of Recurrent Neural Networks are Long Short Term Memory (LSTM) networks and Gated Recurrent Unit (GRU) networks which are better at learning long-term dependencies.
7. Recurrent Neural Networks have applications in time series prediction, machine translation, speech recognition, etc. due to their ability to use sequential information.

The notes cover the key points about Recurrent Neural Networks like their architecture, how they work using sequential information and feedback connections, training using BPTT and applications. The points are written in a formal tone with no emojis or external links as per the given requirements. Please let me know if you would like me to elaborate on any part or make any other changes to the notes.