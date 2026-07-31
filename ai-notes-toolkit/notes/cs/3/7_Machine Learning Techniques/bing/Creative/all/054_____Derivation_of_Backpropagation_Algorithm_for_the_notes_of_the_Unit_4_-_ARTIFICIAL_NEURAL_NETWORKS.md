# Derivation of Backpropagation Algorithm

Backpropagation, short for "backward propagation of errors," is an algorithm for supervised learning of artificial neural networks using gradient descent. Given an artificial neural network and an error function, the method calculates the gradient of the error function with respect to the neural network's weights.

The derivation of the backpropagation algorithm is fairly straightforward. It follows from the use of the chain rule and product rule in differential calculus. Application of these rules is dependent on the differentiation of the activation function, one of the reasons the heaviside step function is not used (being discontinuous and thus, non-differentiable) .

The backpropagation algorithm involves first calculating the derivates at layer N, that is the last layer. These derivatives are an ingredient in the chain rule formula for layer N - 1, so they can be saved and re-used for the second-to-last layer .

The steps of the derivation are as follows:

- Assume a feedforward neural network with N layers, where the input layer is layer 1 and the output layer is layer N. Each layer has a set of neurons, each with a weight vector and a bias term. The activation function for each neuron is denoted by f.
- Let x be the input vector, y be the target output vector, and z be the actual output vector of the network. The error function is defined as E = 1/2 ||y - z||^2, where ||.|| denotes the Euclidean norm.
- The goal is to find the partial derivatives of E with respect to each weight and bias in the network, denoted by dE/dw and dE/db respectively. These derivatives will be used to update the weights and biases using gradient descent.
- To simplify the notation, let a^l_j denote the activation of the j-th neuron in the l-th layer, and w^l_jk denote the weight from the k-th neuron in the (l-1)-th layer to the j-th neuron in the l-th layer. Similarly, let b^l_j denote the bias of the j-th neuron in the l-th layer, and z^l_j denote the weighted input of the j-th neuron in the l-th layer, that is, z^l_j = sum_k w^l_jk a^(l-1)_k + b^l_j.
- Using the chain rule, we can write:

dE/dw^l_jk = dE/da^l_j * da^l_j/dz^l_j * dz^l_j/dw^l_jk

dE/db^l_j = dE/da^l_j * da^l_j/dz^l_j * dz^l_j/db^l_j

- The last term in each expression is easy to compute:

dz^l_j/dw^l_jk = a^(l-1)_k

dz^l_j/db^l_j = 1

- The second term in each expression is the derivative of the activation function:

da^l_j/dz^l_j = f'(z^l_j)

- The first term in each expression is the tricky part. It depends on whether the neuron is in the output layer or a hidden layer. For the output layer, we have:

dE/da^N_j = dE/dz^N_j * dz^N_j/da^N_j

Using the definition of E and z^N_j, we get:

dE/dz^N_j = -(y_j - z_j)

dz^N_j/da^N_j = w^N_jk

Therefore,

dE/da^N_j = -(y_j - z_j) w^N_jk

- For the hidden layers, we have to use the chain rule again:

dE/da^l_j = sum_k dE/da^(l+1)_k * da^(l+1)_k/dz^(l+1)_k * dz^(l+1)_k/da^l_j

Using the previous results, we get:

dE/da^l_j = sum_k dE/da^(l+1)_k * f'(z^(l+1)_k) * w^(l+1)_kj

- Putting everything together, we obtain the final formulas for the partial derivatives:

dE/dw^l_jk = dE/da^l_j * f'(z^l_j) * a^(l-1)_k

dE/db^