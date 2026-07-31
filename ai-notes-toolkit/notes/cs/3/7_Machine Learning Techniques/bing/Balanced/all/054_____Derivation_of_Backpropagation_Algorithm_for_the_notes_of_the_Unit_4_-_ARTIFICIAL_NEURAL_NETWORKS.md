# Derivation of Backpropagation Algorithm

Backpropagation, short for "backward propagation of errors," is an algorithm for supervised learning of artificial neural networks using gradient descent. Given an artificial neural network and an error function, the method calculates the gradient of the error function with respect to the neural network's weights.

The derivation of the backpropagation algorithm is based on the following steps :

- Define the network architecture, the activation functions, the error function, and the learning rate.
- Initialize the network weights randomly or with some heuristic method.
- For each training example, do the following:
  - Forward pass: compute the output of each layer from the input layer to the output layer, using the current weights and the activation functions.
  - Backward pass: compute the error of the output layer, and then propagate it backward to the previous layers, using the chain rule and the product rule of calculus.
  - Weight update: adjust the weights of each layer by subtracting a fraction of the gradient of the error function with respect to the weights, multiplied by the learning rate.

The forward pass is straightforward, so we will focus on the backward pass and the weight update. We will use the following notation:

- $L$: the number of layers in the network, including the input and output layers.
- $n_l$: the number of units in layer $l$, excluding the bias unit.
- $a_i^{(l)}$: the activation of unit $i$ in layer $l$.
- $z_i^{(l)}$: the weighted input of unit $i$ in layer $l$, before applying the activation function.
- $w_{ij}^{(l)}$: the weight from unit $j$ in layer $l-1$ to unit $i$ in layer $l$.
- $b_i^{(l)}$: the bias term for unit $i$ in layer $l$.
- $g$: the activation function, assumed to be the same for all units and layers.
- $g'$: the derivative of the activation function.
- $y_i$: the target value for unit $i$ in the output layer.
- $E$: the error function, assumed to be the sum of squared errors over all output units.
- $\alpha$: the learning rate, a positive scalar.

The error of the output layer can be computed as:

$$
\delta_i^{(L)} = \frac{\partial E}{\partial z_i^{(L)}} = \frac{\partial E}{\partial a_i^{(L)}} \frac{\partial a_i^{(L)}}{\partial z_i^{(L)}} = (a_i^{(L)} - y_i) g'(z_i^{(L)})
$$

The error of the hidden layers can be computed by propagating the error of the next layer backward, using the chain rule and the product rule:

$$
\delta_i^{(l)} = \frac{\partial E}{\partial z_i^{(l)}} = \sum_{j=1}^{n_{l+1}} \frac{\partial E}{\partial z_j^{(l+1)}} \frac{\partial z_j^{(l+1)}}{\partial z_i^{(l)}} = \sum_{j=1}^{n_{l+1}} \delta_j^{(l+1)} w_{ji}^{(l+1)} g'(z_i^{(l)})
$$

The weight update can be computed by subtracting a fraction of the gradient of the error function with respect to the weights, multiplied by the learning rate :

$$
w_{ij}^{(l)} := w_{ij}^{(l)} - \alpha \frac{\partial E}{\partial w_{ij}^{(l)}} = w_{ij}^{(l)} - \alpha \frac{\partial E}{\partial z_i^{(l)}} \frac{\partial z_i^{(l)}}{\partial w_{ij}^{(l)}} = w_{ij}^{(l)} - \alpha \delta_i^{(l)} a_j^{(l-1)}
$$

The bias update can be computed similarly, except that the input term is always 1:

$$
b_i^{(l)} := b_i^{(l)} - \alpha \frac{\partial E}{\partial b_i^{(l)}} = b_i^{(l)} - \alpha \frac