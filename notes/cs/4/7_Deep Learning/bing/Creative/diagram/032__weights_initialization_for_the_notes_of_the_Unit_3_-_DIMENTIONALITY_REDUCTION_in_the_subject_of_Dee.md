Weight initialization is a procedure to set the weights of a neural network to small random values that define the starting point for the optimization (learning or training) of the neural network model. Different weight initialization techniques have been proposed for different activation functions and network architectures. Some of the common techniques are:

- **Xavier initialization**: This technique is suitable for nodes that use the sigmoid or tanh activation functions. It initializes the weights by drawing random values from a uniform distribution in the range [-a, a], where a = sqrt(6 / (n_in + n_out)), and n_in and n_out are the number of inputs and outputs of the node, respectively .
- **Normalized Xavier initialization**: This technique is a variation of the Xavier initialization that normalizes the weights by dividing them by the square root of the fan-in (n_in). This helps to reduce the variance of the weights and improve the convergence of the network.
- **He initialization**: This technique is suitable for nodes that use the ReLU activation function. It initializes the weights by drawing random values from a normal distribution with mean zero and standard deviation sqrt(2 / n_in), where n_in is the number of inputs of the node .

The following diagram illustrates the basic architecture of a neural network with three layers and the corresponding weight initialization techniques for each layer:

```
    Input layer                Hidden layer               Output layer
    (sigmoid activation)       (tanh activation)          (ReLU activation)
    Xavier initialization      Normalized Xavier          He initialization
                               initialization

    x1  o----------------------o  h1
        |                      |  |
        |                      |  |
        |                      |  |
        |                      |  |
    x2  o----------------------o  h2
        |                      |  |
        |                      |  |
        |                      |  |
        |                      |  |
    x3  o----------------------o  h3
        |                      |  |
        |                      |  |
        |                      |  |
        |                      |  |
    x4  o----------------------o  h4
        |                      |  |
        |                      |  |
        |                      |  |
        |                      |  |
        |                      |  o  y
        |                      |  |
        |                      |  |
        |                      |  |
        |                      |  |
    x5  o----------------------o  h5
```