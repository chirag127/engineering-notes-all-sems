### Derivation of Backpropagation Algorithm

Backpropagation, short for "backward propagation of errors," is an algorithm for supervised learning of artificial neural networks using gradient descent. Given an artificial neural network and an error function, the method calculates the gradient of the error function with respect to the neural network's weights.

The derivation of the backpropagation algorithm is based on the following steps  :

- Define the network architecture, the activation functions, the error function, and the learning rate.
- Initialize the network weights randomly or with some heuristic method.
- For each training example, do the following:
  - Forward pass: compute the output of each layer by applying the activation function to the weighted sum of the inputs from the previous layer.
  - Backward pass: compute the error of each layer by comparing the output with the target value (for the output layer) or by propagating the error from the next layer (for the hidden layers).
  - Weight update: adjust the weights of each layer by applying the gradient descent rule, which uses the error of the layer and the derivative of the activation function to compute the weight change.
- Repeat the above steps until the error function reaches a minimum or some stopping criterion is met.

The backpropagation algorithm involves first calculating the derivatives at layer N, that is the last layer. These derivatives are an ingredient in the chain rule formula for layer N - 1, so they can be saved and re-used for the second-to-last layer. The chain rule formula can be applied recursively to compute the derivatives for all the layers.

The derivation of the backpropagation algorithm can be illustrated with an example of a three-layer network, as shown in Figure 1.

![Figure 1: A three-layer network with two inputs, two hidden units, and one output.](https://www.cs.swarthmore.edu/~meeden/cs81/s10/BackPropDeriv_files/image002.gif)

Figure 1: A three-layer network with two inputs, two hidden units, and one output.

Let x1 and x2 be the inputs, h1 and h2 be the hidden units, y be the output, and t be the target value. Let w1, w2, w3, and w4 be the weights from the input layer to the hidden layer, and v1 and v2 be the weights from the hidden layer to the output layer. Let f be the activation function for both the hidden and the output layer, and E be the error function, which is the sum of squared errors over all the training examples.

The forward pass can be written as:

h1 = f(w1x1 + w2x2)

h2 = f(w3x1 + w4x2)

y = f(v1h1 + v2h2)

E = 1/2 (t - y)^2

The backward pass can be written as:

dE/dy = -(t - y)

dy/dv1 = f'(v1h1 + v2h2) * h1

dy/dv2 = f'(v1h1 + v2h2) * h2

dE/dv1 = dE/dy * dy/dv1

dE/dv2 = dE/dy * dy/dv2

dE/dh1 = dE/dy * dy/dh1

dE/dh2 = dE/dy * dy/dh2

dh1/dw1 = f'(w1x1 + w2x2) * x1

dh1/dw2 = f'(w1x1 + w2x2) * x2

dh2/dw3 = f'(w3x1 + w4x2) * x1

dh2/dw4 = f'(w3x1 + w4x2) * x2

dE/dw1 = dE/dh1 * dh1/dw1

dE/dw2 = dE/dh1 * dh1/dw2

dE/dw3 = dE/dh2 * dh2/dw3

dE/dw4 = dE/dh2 * dh2/dw4

The weight update can be written as:

v1 = v1 - alpha * dE/dv1

v2 = v2 - alpha * dE/dv2

w1 = w1 - alpha * dE/dw1

w2 = w2 - alpha * dE