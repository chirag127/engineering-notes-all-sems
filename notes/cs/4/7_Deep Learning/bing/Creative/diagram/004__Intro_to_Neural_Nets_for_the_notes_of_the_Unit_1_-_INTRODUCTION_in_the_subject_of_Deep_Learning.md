A neural network is a computational model that consists of artificial neurons arranged in layers and connected by weights. A neural network can learn from data and perform tasks such as classification, regression, clustering, etc. A neural network can be represented by a diagram that shows the input layer, the hidden layer(s), and the output layer, as well as the connections between them. The following diagram illustrates the basic architecture of a neural network:

```
    Input layer         Hidden layer        Output layer
    +---------+         +---------+         +---------+
    | x1      |         | h1      |         | y1      |
    +---------+         +---------+         +---------+
    | x2      |         | h2      |         | y2      |
    +---------+         +---------+         +---------+
    | x3      |         | h3      |         | y3      |
    +---------+         +---------+         +---------+
    | x4      |         | h4      |         | y4      |
    +---------+         +---------+         +---------+

    +---------+         +---------+         +---------+
    | x1      |-------->| h1      |-------->| y1      |
    +---------+         +---------+         +---------+
    | x2      |-------->| h2      |-------->| y2      |
    +---------+         +---------+         +---------+
    | x3      |-------->| h3      |-------->| y3      |
    +---------+         +---------+         +---------+
    | x4      |-------->| h4      |-------->| y4      |
    +---------+         +---------+         +---------+

    +---------+         +---------+         +---------+
    | x1      |---w1--->| h1      |---w5--->| y1      |
    +---------+         +---------+         +---------+
    | x2      |---w2--->| h2      |---w6--->| y2      |
    +---------+         +---------+         +---------+
    | x3      |---w3--->| h3      |---w7--->| y3      |
    +---------+         +---------+         +---------+
    | x4      |---w4--->| h4      |---w8--->| y4      |
    +---------+         +---------+         +---------+
```

The input layer consists of the input variables (x1, x2, x3, x4) that are fed to the network. The hidden layer consists of the hidden neurons (h1, h2, h3, h4) that process the input data and apply an activation function. The output layer consists of the output variables (y1, y2, y3, y4) that are the predictions or classifications of the network. The weights (w1, w2, w3, w4, w5, w6, w7, w8) are the parameters that determine how much each connection contributes to the output. The weights are learned by the network through a process called training, which involves adjusting the weights based on the error between the actual and desired output. A neural network can have more than one hidden layer, and each layer can have a different number of neurons. The more layers and neurons, the more complex the network and the more expressive its function. However, this also increases the risk of overfitting, which means that the network memorizes the training data and fails to generalize to new data. Therefore, a balance between complexity and simplicity is needed to achieve good performance.