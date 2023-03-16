### Backpropagation

Backpropagation is a method for calculating the gradients of the parameters of a deep feedforward neural network. It is based on the chain rule of calculus, which allows us to compute the derivative of a function with respect to its inputs by using the derivatives of the function with respect to its outputs and the derivatives of the outputs with respect to the inputs.

Backpropagation forms an important part of many supervised learning algorithms for training neural networks, such as stochastic gradient descent. By using backpropagation, we can update the weights of the network in a way that minimizes the loss function, which measures the discrepancy between the network's predictions and the true labels.

The main steps of backpropagation are:

- Perform a forward pass through the network, computing the outputs of each layer given the inputs and the weights.
- Compute the loss function at the output layer, comparing the network's predictions with the true labels.
- Perform a backward pass through the network, computing the gradients of the loss function with respect to each weight by using the chain rule and the gradients of each layer's output with respect to its input.
- Update the weights of the network by subtracting a fraction of the gradients, called the learning rate, from the current weights.

The following diagram illustrates the backpropagation algorithm for a simple neural network with one hidden layer and one output layer:

![Backpropagation diagram](https://miro.medium.com/max/1400/1*FceBJSJ7j8jHjb4TmLV0Ew.png)

The notation used in the diagram is:

- x: the input vector
- y: the true label vector
- z: the output vector of the network
- W: the weight matrix of the network
- b: the bias vector of the network
- a: the activation function of the network
- L: the loss function of the network
- E: the total error of the network
- d: the partial derivative symbol
- delta: the gradient symbol

The equations used in the diagram are:

- z = a(Wx + b): the forward pass equation
- E = L(y, z): the loss function equation
- delta_z = dE/dz = dL/dz: the gradient of the error with respect to the output
- delta_W = dE/dW = delta_z * x^T: the gradient of the error with respect to the weight matrix
- delta_b = dE/db = delta_z: the gradient of the error with respect to the bias vector
- delta_x = dE/dx = W^T * delta_z: the gradient of the error with respect to the input
- W = W - alpha * delta_W: the weight update equation
- b = b - alpha * delta_b: the bias update equation

where alpha is the learning rate, a small positive number that controls the size of the weight updates.

Backpropagation can be generalized to networks with multiple hidden layers by applying the chain rule repeatedly, starting from the output layer and moving backwards to the input layer. The gradients of each layer's weights and biases are computed by multiplying the gradients of the previous layer's outputs with the derivatives of the current layer's outputs with respect to its inputs. The following diagram shows an example of backpropagation for a network with two hidden layers:

![Backpropagation diagram 2](https://miro.medium.com/max/1400/1*FpMz2sQrhqXU3rDDHgiwbg.png)

The notation used in the diagram is:

- x: the input vector
- y: the true label vector
- z: the output vector of the network
- W1, W2, W3: the weight matrices of the network
- b1, b2, b3: the bias vectors of the network
- a1, a2, a3: the activation functions of the network
- L: the loss function of the network
- E: the total error of the network
- d: the partial derivative symbol
- delta: the gradient symbol
- h1, h2: the hidden layer vectors

The equations used in the diagram are:

- h1 = a1(W1x + b1): the forward pass equation for the first hidden layer
- h2 = a2(W2h1 + b2): the forward pass equation for the second hidden layer
- z = a3(W3h2 + b3): the forward pass equation for the output layer
- E = L(y, z): the loss function