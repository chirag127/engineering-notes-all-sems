A shallow network is a neural network that has only one hidden layer between the input and output layers. It can learn simple patterns and features from the input data, but it may not be able to capture complex and abstract representations. A deep network is a neural network that has multiple hidden layers, each of which can learn new and higher-level features from the previous layer. A deep network can learn more complex and abstract patterns and features from the input data, but it may also require more data, computation and training time.

The following diagram illustrates the basic architecture of a shallow network and a deep network using ASCII characters. Each circle represents a neuron, and each line represents a connection with a weight. The input layer has three neurons, and the output layer has two neurons. The shallow network has one hidden layer with four neurons, and the deep network has three hidden layers with four, three and two neurons respectively.

Shallow network:

    Input layer         Hidden layer        Output layer
    +---+---+---+       +---+---+---+---+   +---+---+
    | x | x | x | ----> | x | x | x | x |-->| x | x |
    +---+---+---+       +---+---+---+---+   +---+---+
    | 1 | 2 | 3 |       | 4 | 5 | 6 | 7 |   | 8 | 9 |
    +---+---+---+       +---+---+---+---+   +---+---+

Deep network:

    Input layer         Hidden layer 1      Hidden layer 2      Hidden layer 3      Output layer
    +---+---+---+       +---+---+---+---+   +---+---+---+      +---+---+           +---+---+
    | x | x | x | ----> | x | x | x | x |-->| x | x | x |----->| x | x |---------->| x | x |
    +---+---+---+       +---+---+---+---+   +---+---+---+      +---+---+           +---+---+
    | 1 | 2 | 3 |       | 4 | 5 | 6 | 7 |   | 8 | 9 | 10|      | 11| 12|           | 13| 14|
    +---+---+---+       +---+---+---+---+   +---+---+---+      +---+---+           +---+---+