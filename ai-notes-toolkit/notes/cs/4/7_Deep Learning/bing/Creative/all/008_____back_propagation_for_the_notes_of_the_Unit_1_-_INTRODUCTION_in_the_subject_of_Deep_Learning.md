# Backpropagation

Backpropagation is a method for calculating the gradients of the parameters of a deep feedforward neural network. It is based on the chain rule of differentiation and allows us to update the weights of the network in a way that minimizes the loss function. Backpropagation is an essential part of many supervised learning algorithms for training neural networks, such as stochastic gradient descent.

## Backpropagation Formula

Let us consider a multilayer feedforward neural network with N layers, where each layer consists of a linear transformation followed by a nonlinear activation function. The output of the network is denoted by y_hat, and the target output is denoted by y. The loss function is denoted by L(y, y_hat), which measures the discrepancy between the target and the prediction.

The goal of backpropagation is to compute the partial derivatives of the loss function with respect to each weight and bias in the network, denoted by dL/dw_ij and dL/db_i, where w_ij is the weight connecting the j-th neuron in the previous layer to the i-th neuron in the current layer, and b_i is the bias of the i-th neuron in the current layer.

The backpropagation algorithm consists of two steps: forward pass and backward pass.

### Forward pass

In the forward pass, we compute the output of each layer by applying the linear transformation and the activation function. We also store the intermediate values for later use in the backward pass. For example, for the i-th neuron in the l-th layer, we have:

z_i^(l) = sum_j w_ij^(l) * a_j^(l-1) + b_i^(l)

a_i^(l) = f(z_i^(l))

where z_i^(l) is the pre-activation value, a_i^(l) is the post-activation value, and f is the activation function. The output of the network is given by:

y_hat = a_N

### Backward pass

In the backward pass, we compute the gradients of the loss function with respect to each parameter by applying the chain rule of differentiation. We start from the output layer and propagate the errors backwards to the input layer. For example, for the i-th neuron in the l-th layer, we have:

dL/da_i^(l) = dL/dz_i^(l) * f'(z_i^(l))

dL/dz_i^(l) = sum_k dL/dz_k^(l+1) * w_ik^(l+1)

dL/dw_ij^(l) = dL/dz_i^(l) * a_j^(l-1)

dL/db_i^(l) = dL/dz_i^(l)

where dL/da_i^(l) is the gradient of the loss function with respect to the post-activation value, dL/dz_i^(l) is the gradient of the loss function with respect to the pre-activation value, and f' is the derivative of the activation function. The gradient of the loss function with respect to the output of the network is given by:

dL/da_N = dL/dy_hat

## Backpropagation Example

Let us consider a simple example of a neural network with one input layer, one hidden layer, and one output layer. The input layer has one neuron, the hidden layer has two neurons, and the output layer has one neuron. The activation function is the sigmoid function, and the loss function is the mean squared error. The network is shown below:

![Neural network example](https://i.imgur.com/4Z4w4Zf.png)

Suppose the input is x = 0.5, the target output is y = 0.8, and the initial weights and biases are:

w_11^(1) = 0.1

w_12^(1) = 0.2

w_21^(1) = 0.3

w_22^(1) = 0.4

w_11^(2) = 0.5

w_21^(2) = 0.6

b_1^(1) = 0.7

b_2^(1) = 0.8

b_1^(2) = 0.9

We can apply the forward pass and the backward pass to compute the output and the gradients of the network.

### Forward pass

We start by computing the output of the input layer, which is simply the input itself:

a_1^(0) = x = 0.5