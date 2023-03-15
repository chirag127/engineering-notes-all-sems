### Derivation of Backpropagation Algorithm

Backpropagation is a supervised learning algorithm used for training artificial neural networks. It is based on the chain rule of calculus and is used to calculate the gradient of the loss function with respect to the weights of the network. The gradient is then used to update the weights in order to minimize the loss function. Here is the derivation of the backpropagation algorithm:

1. Let's consider a neural network with L layers, where the l-th layer has n_l neurons. The input to the network is denoted by x, and the output by y. The weights and biases of the network are denoted by w and b, respectively.

2. The output of the i-th neuron in the l-th layer is given by the activation function applied to the weighted sum of the inputs to the neuron, i.e., a_i^l = f(z_i^l), where z_i^l = sum_j(w_ij^l * a_j^(l-1) + b_i^l).

3. The loss function, which measures the difference between the predicted output and the true output, is denoted by C. The goal is to minimize this loss function by adjusting the weights and biases of the network.

4. To update the weights and biases, we need to calculate the gradient of the loss function with respect to the weights and biases. This is done using the chain rule of calculus. The partial derivative of the loss function with respect to the weight w_ij^l is given by: dC/dw_ij^l = (dC/da_i^l) * (da_i^l/dz_i^l) * (dz_i^l/dw_ij^l).

5. The first term, dC/da_i^l, is the derivative of the loss function with respect to the output of the i-th neuron in the l-th layer. This can be calculated using the chain rule, by propagating the error backwards from the output layer to the l-th layer.

6. The second term, da_i^l/dz_i^l, is the derivative of the activation function with respect to its input. This can be calculated directly, as the activation function is known.

7. The third term, dz_i^l/dw_ij^l, is the derivative of the weighted sum of the inputs to the neuron with respect to the weight. This is equal to the output of the j-th neuron in the (l-1)-th layer, i.e., a_j^(l-1).

8. By substituting the above expressions into the formula for the gradient, we obtain the backpropagation algorithm for updating the weights and biases of the network.
