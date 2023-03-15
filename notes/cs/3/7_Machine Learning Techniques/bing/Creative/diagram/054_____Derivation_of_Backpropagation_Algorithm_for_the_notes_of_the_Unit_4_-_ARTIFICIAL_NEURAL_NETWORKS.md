### Derivation of Backpropagation Algorithm

Backpropagation, short for "backward propagation of errors," is an algorithm for supervised learning of artificial neural networks using gradient descent. Given an artificial neural network and an error function, the method calculates the gradient of the error function with respect to the neural network's weights.

The derivation of the backpropagation algorithm is based on the following steps:

- Define the network architecture, the activation functions, the input and output vectors, and the error function.
- Initialize the network weights randomly or with some heuristic method.
- For each training example, perform a forward pass to compute the output of each neuron and the overall network output.
- For each training example, perform a backward pass to compute the error of each neuron and the partial derivatives of the error function with respect to the weights.
- Update the weights using the gradient descent rule: `w_ij = w_ij - alpha * dE/dw_ij`, where `w_ij` is the weight from neuron `i` to neuron `j`, `alpha` is the learning rate, and `dE/dw_ij` is the partial derivative of the error function with respect to `w_ij`.
- Repeat steps 3-5 until the error function reaches a minimum or some stopping criterion is met.

The key part of the derivation is the computation of the partial derivatives of the error function with respect to the weights. This can be done using the chain rule and the product rule of calculus. The chain rule states that if `f` and `g` are differentiable functions, then `d(f(g(x)))/dx = f'(g(x)) * g'(x)`. The product rule states that if `f` and `g` are differentiable functions, then `d(f(x) * g(x))/dx = f'(x) * g(x) + f(x) * g'(x)`.

The error function is usually defined as the sum of squared errors between the network output and the target output: `E = 1/2 * sum_k (y_k - t_k)^2`, where `y_k` is the output of the k-th output neuron, and `t_k` is the target output for the k-th output neuron. The partial derivative of the error function with respect to a weight `w_ij` can be written as `dE/dw_ij = dE/dy_j * dy_j/dnet_j * dnet_j/dw_ij`, where `y_j` is the output of the j-th neuron, `net_j` is the weighted sum of inputs to the j-th neuron, and `dnet_j/dw_ij = y_i` is the output of the i-th neuron. The term `dE/dy_j` is the error of the j-th neuron, and the term `dy_j/dnet_j` is the derivative of the activation function of the j-th neuron.

The backpropagation algorithm involves first calculating the derivatives at layer N, that is the last layer. These derivatives are an ingredient in the chain rule formula for layer N - 1, so they can be saved and re-used for the second-to-last layer. The algorithm can be summarized as follows:

- For each output neuron `j` in layer N, calculate `dE/dy_j = y_j - t_j`, and `dy_j/dnet_j = f'(net_j)`, where `f` is the activation function of the output layer. Then, calculate `dE/dnet_j = dE/dy_j * dy_j/dnet_j`.
- For each hidden neuron `j` in layer N - 1, calculate `dE/dnet_j = sum_k (dE/dnet_k * w_jk)`, where `k` ranges over the neurons in layer N, and `w_jk` is the weight from neuron `j` to neuron `k`. Then, calculate `dy_j/dnet_j = f'(net_j)`, where `f` is the activation function of the hidden layer.
- Repeat step 2 for each hidden layer, moving from layer N - 1 to layer 1.
- For each weight `w_ij` in the network, calculate `dE/dw_ij = dE/dnet_j * y_i`, where `y_i` is the output of the neuron `i` that connects to the weight `w_ij`.
- Update the weights using the gradient descent rule: `w_ij = w_ij - alpha * dE/dw_ij`.

The following diagram illustrates the backpropagation algorithm for a simple network with one hidden