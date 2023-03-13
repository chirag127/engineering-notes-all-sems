The following is a detailed ASCII diagram for training a network for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning, based on the second search result.

Training a network involves defining a neural network parametrization, writing a backpropagation algorithm, and running a gradient-based optimizer.

The neural network parametrization is a function that maps an input x to an output y, using a set of parameters theta. The function can be composed of multiple layers, each with its own activation function and weights. For example, a two-layer neural network can be written as:

h_theta(x) = g2(W2 * g1(W1 * x + b1) + b2)

where g1 and g2 are activation functions, W1 and W2 are weight matrices, and b1 and b2 are bias vectors.

The backpropagation algorithm is a method to compute the gradient of the loss function J(theta) with respect to the parameters theta. The loss function measures how well the network predicts the correct output for a given input. For example, a common loss function for classification problems is the cross-entropy loss:

J(theta) = -1/m * sum(y * log(h_theta(x)) + (1 - y) * log(1 - h_theta(x)))

where m is the number of training examples, y is the true output, and h_theta(x) is the predicted output.

The backpropagation algorithm works by applying the chain rule of calculus to propagate the errors from the output layer to the input layer. For each layer, the algorithm computes the partial derivatives of the loss function with respect to the weights and biases, and updates them using a learning rate alpha. For example, for the two-layer neural network, the algorithm can be summarized as:

# Forward pass
z1 = W1 * x + b1
a1 = g1(z1)
z2 = W2 * a1 + b2
a2 = g2(z2)
J = -1/m * sum(y * log(a2) + (1 - y) * log(1 - a2))

# Backward pass
dJ_dz2 = a2 - y
dJ_dW2 = 1/m * dJ_dz2 * a1.T
dJ_db2 = 1/m * sum(dJ_dz2, axis=1, keepdims=True)
dJ_dz1 = W2.T * dJ_dz2 * g1'(z1)
dJ_dW1 = 1/m * dJ_dz1 * x.T
dJ_db1 = 1/m * sum(dJ_dz1, axis=1, keepdims=True)

# Update parameters
W1 = W1 - alpha * dJ_dW1
b1 = b1 - alpha * dJ_db1
W2 = W2 - alpha * dJ_dW2
b2 = b2 - alpha * dJ_db2

The gradient-based optimizer is a technique to find the optimal values of the parameters theta that minimize the loss function J(theta). The optimizer iterates over the training data and applies the backpropagation algorithm to update the parameters. For example, a common optimizer is the stochastic gradient descent (SGD), which randomly shuffles the training data and processes one example at a time. Other optimizers include mini-batch SGD, which processes a small batch of examples at a time, and adaptive methods, which adjust the learning rate based on the previous updates.

The following ASCII diagram illustrates the basic architecture of a two-layer neural network and the steps involved in training it:

    +------------------+       +------------------+       +------------------+
    |                  |       |                  |       |                  |
    |                  |       |                  |       |                  |
    |                  |       |                  |       |                  |
    |                  |       |                  |       |                  |
    |                  |       |                  |       |                  |
    |                  |       |                  |       |                  |
    |                  |       |                  |       |                  |
    |                  |       |                  |       |                  |
    |                  |       |                  |       |                  |
    |                  |       |                  |       |                  |
    |                  |       |                  |       |                  |
    |                  |       |                  |       |                  |
x > |     Input       | ----> |     Hidden       | ----> |     Output      | > y
    |     Layer       |       |     Layer        |       |     Layer