# Multilayer Perceptron Model

- A multilayer perceptron (MLP) is a type of artificial neural network that consists of multiple layers of neurons connected by weighted synapses.
- An MLP can learn nonlinear functions by using a nonlinear activation function in the hidden layers, such as sigmoid, tanh, or ReLU.
- An MLP can perform both regression and classification tasks, depending on the output layer activation function and the loss function used for training.
- An MLP can be trained using the backpropagation algorithm, which computes the gradients of the loss function with respect to the weights and biases of the network, and updates them using a learning rule such as gradient descent or stochastic gradient descent.
- An MLP can be represented by a directed acyclic graph, where each node is a neuron and each edge is a synapse. The input layer receives the features of the data, the output layer produces the predictions, and the hidden layers perform intermediate computations.
- An MLP can be expressed mathematically as follows:

  - Let $x$ be the input vector, $y$ be the output vector, $L$ be the number of layers, $n_l$ be the number of neurons in layer $l$, $w_{ij}^{(l)}$ be the weight of the synapse from neuron $i$ in layer $l-1$ to neuron $j$ in layer $l$, $b_j^{(l)}$ be the bias of neuron $j$ in layer $l$, and $f^{(l)}$ be the activation function of layer $l$.
  - Then, the output of neuron $j$ in layer $l$ is given by:

    $$z_j^{(l)} = \sum_{i=1}^{n_{l-1}} w_{ij}^{(l)} a_i^{(l-1)} + b_j^{(l)}$$

    $$a_j^{(l)} = f^{(l)}(z_j^{(l)})$$

  - The output of the network is given by:

    $$y = a^{(L)} = f^{(L)}(z^{(L)})$$

  - The loss function $J$ measures the discrepancy between the output $y$ and the target $t$. For example, for regression, the mean squared error (MSE) can be used:

    $$J = \frac{1}{2} \|y - t\|^2$$

  - For classification, the cross-entropy (CE) can be used:

    $$J = - \sum_{i=1}^{n_L} t_i \log y_i$$

  - The backpropagation algorithm computes the gradients of the loss function with respect to the weights and biases of the network using the chain rule. For example, for the output layer, the gradient is given by:

    $$\frac{\partial J}{\partial w_{ij}^{(L)}} = \frac{\partial J}{\partial z_j^{(L)}} \frac{\partial z_j^{(L)}}{\partial w_{ij}^{(L)}} = \delta_j^{(L)} a_i^{(L-1)}$$

    $$\frac{\partial J}{\partial b_j^{(L)}} = \frac{\partial J}{\partial z_j^{(L)}} \frac{\partial z_j^{(L)}}{\partial b_j^{(L)}} = \delta_j^{(L)}$$

    where $\delta_j^{(L)} = \frac{\partial J}{\partial z_j^{(L)}} = \frac{\partial J}{\partial y_j} \frac{\partial y_j}{\partial z_j^{(L)}} = (y_j - t_j) f'^{(L)}(z_j^{(L)})$ for MSE, and $\delta_j^{(L)} = \frac{\partial J}{\partial z_j^{(L)}} = \frac{\partial J}{\partial y_j} \frac{\partial y_j}{\partial z_j^{(L)}} = (y_j - t_j)$ for CE.

  - For the hidden layers, the gradient is given by:

    $$\frac{\partial J}{\partial w_{ij}^{(l)}} = \frac{\partial J}{\partial z_j^{(l)}} \frac{\partial z_j^{(l)}}{\partial w_{ij}^{(l)}} = \delta_j^{(l)} a_i^{(l-1)}$$