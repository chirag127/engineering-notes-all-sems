Backpropagation is a method of training a neural network by adjusting the weights of the connections based on the error between the desired and the actual output. It consists of two phases: forward propagation and backward propagation. In forward propagation, the input data is fed to the network and the output is computed. In backward propagation, the error is calculated and propagated back to the previous layers, and the weights are updated using a gradient descent algorithm. The following diagram illustrates the basic architecture of a backpropagation neural network:

```
    Input layer      Hidden layer     Output layer
    +---------+      +---------+      +---------+
    | x1      |      | h1      |      | y1      |
    |         |----->|         |----->|         |
    +---------+      +---------+      +---------+
    | x2      |      | h2      |      | y2      |
    |         |----->|         |----->|         |
    +---------+      +---------+      +---------+
    | x3      |      | h3      |      | y3      |
    |         |----->|         |----->|         |
    +---------+      +---------+      +---------+
    | x4      |      | h4      |      | y4      |
    |         |----->|         |----->|         |
    +---------+      +---------+      +---------+
```

Each connection has a weight associated with it, which is initialized randomly at the beginning of the training. The output of each node is calculated by applying an activation function to the weighted sum of the inputs. For example, the output of h1 is given by:

```
h1 = f(w1x1 + w2x2 + w3x3 + w4x4)
```

where f is the activation function and w1, w2, w3, and w4 are the weights of the connections from the input layer to h1.

The error of the network is measured by a loss function, which compares the desired output (d1, d2, d3, d4) with the actual output (y1, y2, y3, y4). For example, the loss function can be the mean squared error:

```
L = 1/4 * ((d1 - y1)^2 + (d2 - y2)^2 + (d3 - y3)^2 + (d4 - y4)^2)
```

The goal of the training is to minimize the loss function by adjusting the weights of the connections. This is done by using the gradient descent algorithm, which updates the weights in the opposite direction of the gradient of the loss function with respect to the weights. For example, the weight w1 is updated by:

```
w1 = w1 - alpha * dL/dw1
```

where alpha is the learning rate and dL/dw1 is the partial derivative of the loss function with respect to w1.

The gradient of the loss function with respect to the weights can be computed by using the chain rule. This is where the backpropagation algorithm comes in. It starts from the output layer and calculates the error of each node and the gradient of the loss function with respect to the weights of the connections from that node. Then, it propagates the error and the gradient back to the previous layer, and repeats the process until it reaches the input layer. For example, the error of y1 is given by:

```
e1 = d1 - y1
```

and the gradient of the loss function with respect to w5 (the weight of the connection from h1 to y1) is given by:

```
dL/dw5 = e1 * f'(h1) * x1
```

where f' is the derivative of the activation function.

The backpropagation algorithm can be summarized by the following steps:

1. Initialize the weights randomly.
2. Repeat until convergence or a maximum number of iterations:
    - For each input-output pair in the training data:
        - Perform forward propagation and compute the output and the loss.
        - Perform backward propagation and compute the error and the gradient for each node and weight.
        - Update the weights using the gradient descent algorithm.