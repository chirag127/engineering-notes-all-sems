### Derivation of Backpropagation Algorithm

Backpropagation, short for "backward propagation of errors," is an algorithm for supervised learning of artificial neural networks using gradient descent. Given an artificial neural network and an error function, the method calculates the gradient of the error function with respect to the neural network's weights.

The derivation of the backpropagation algorithm is based on the following steps :

- Define the network architecture, the activation functions, the error function, and the input and output data.
- Initialize the network weights randomly or with some heuristic method.
- For each input-output pair in the training data, do the following:
  - Forward propagation: compute the output of each neuron in the network, starting from the input layer and moving to the output layer, using the current weights and the activation functions.
  - Backward propagation: compute the error of each neuron in the network, starting from the output layer and moving to the input layer, using the output error and the chain rule of differentiation.
  - Weight update: adjust the weights of each neuron in the network, using the error, the learning rate, and the gradient descent rule.
- Repeat the above steps until the error function reaches a minimum or a stopping criterion is met.

The following sections will explain the mathematical details of each step.

#### Forward Propagation

Assume that the network has L layers, where the first layer is the input layer and the last layer is the output layer. Each layer l has n_l neurons, and each neuron j in layer l has an activation function f_l and a bias term b_lj. The input to the network is denoted by x, and the output by y. The output of neuron j in layer l is denoted by a_lj, and the weighted sum of inputs to neuron j in layer l is denoted by z_lj. The weight of the connection from neuron i in layer l-1 to neuron j in layer l is denoted by w_lji.

The forward propagation step can be summarized by the following equations:

- For the input layer, set a_1j = x_j for j = 1, ..., n_1.
- For each hidden layer l = 2, ..., L-1, compute z_lj = sum_i w_lji a_l-1i + b_lj and a_lj = f_l(z_lj) for j = 1, ..., n_l.
- For the output layer, compute z_Lj = sum_i w_Lji a_L-1i + b_Lj and a_Lj = f_L(z_Lj) for j = 1, ..., n_L.

#### Backward Propagation

Assume that the error function is denoted by E, and it is a function of the network output y and the target output t. The backward propagation step can be summarized by the following equations:

- For the output layer, compute the error term delta_Lj = E'(y_j, t_j) f_L'(z_Lj) for j = 1, ..., n_L, where E' and f_L' are the derivatives of E and f_L, respectively.
- For each hidden layer l = L-1, ..., 2, compute the error term delta_lj = sum_k w_l+1kj delta_l+1k f_l'(z_lj) for j = 1, ..., n_l, where f_l' is the derivative of f_l.
- For the input layer, compute the error term delta_1j = sum_k w_2kj delta_2k f_1'(z_1j) for j = 1, ..., n_1, where f_1' is the derivative of f_1.

#### Weight Update

Assume that the learning rate is denoted by alpha, and it is a positive constant that controls the step size of the gradient descent. The weight update step can be summarized by the following equations:

- For each layer l = 2, ..., L, update the weight w_lji by w_lji = w_lji - alpha delta_lj a_l-1i for i = 1, ..., n_l-1 and j = 1, ..., n_l.
- For each layer l = 2, ..., L, update the bias b_lj by b_lj = b_lj - alpha delta_lj for j = 1, ..., n_l.

The above derivation of the backpropagation algorithm is fairly straightforward. It follows from the use of the chain rule