### Derivation of Backpropagation Algorithm

Backpropagation, short for "backward propagation of errors," is an algorithm for supervised learning of artificial neural networks using gradient descent. Given an artificial neural network and an error function, the method calculates the gradient of the error function with respect to the neural network's weights.

The derivation of the backpropagation algorithm is based on the following steps:

- Define the network architecture, the activation functions, the input and output vectors, and the error function.
- Apply the forward pass to compute the output of each layer and the final output of the network.
- Apply the backward pass to compute the error term for each layer and the partial derivatives of the error function with respect to the weights.
- Update the weights using the gradient descent rule.

The following notation is used for the derivation:

- $L$ is the number of layers in the network, excluding the input layer.
- $n_l$ is the number of units in layer $l$, excluding the bias unit.
- $a_i^{(l)}$ is the activation of unit $i$ in layer $l$.
- $z_i^{(l)}$ is the weighted input of unit $i$ in layer $l$, i.e., $z_i^{(l)} = \sum_{j=0}^{n_{l-1}} w_{ji}^{(l)} a_j^{(l-1)}$.
- $w_{ji}^{(l)}$ is the weight from unit $j$ in layer $l-1$ to unit $i$ in layer $l$.
- $b_i^{(l)}$ is the bias term for unit $i$ in layer $l$, i.e., $w_{0i}^{(l)}$.
- $x$ is the input vector, i.e., $a^{(0)}$.
- $y$ is the output vector, i.e., $a^{(L)}$.
- $t$ is the target vector.
- $E$ is the error function, e.g., mean squared error: $E = \frac{1}{2} \sum_{i=1}^{n_L} (t_i - y_i)^2$.
- $f$ is the activation function, e.g., sigmoid: $f(z) = \frac{1}{1 + e^{-z}}$.
- $f'$ is the derivative of the activation function, e.g., sigmoid: $f'(z) = f(z) (1 - f(z))$.
- $\delta_i^{(l)}$ is the error term for unit $i$ in layer $l$, i.e., the partial derivative of the error function with respect to $z_i^{(l)}$.

The derivation of the backpropagation algorithm is as follows:

- Forward pass:

  - For each layer $l = 1, \dots, L$:

    - For each unit $i = 1, \dots, n_l$:

      - Compute the weighted input: $z_i^{(l)} = \sum_{j=0}^{n_{l-1}} w_{ji}^{(l)} a_j^{(l-1)}$.

      - Compute the activation: $a_i^{(l)} = f(z_i^{(l)})$.

- Backward pass:

  - For the output layer $l = L$:

    - For each unit $i = 1, \dots, n_L$:

      - Compute the error term: $\delta_i^{(L)} = \frac{\partial E}{\partial z_i^{(L)}} = \frac{\partial E}{\partial y_i} \frac{\partial y_i}{\partial z_i^{(L)}} = (y_i - t_i) f'(z_i^{(L)})$.

  - For each hidden layer $l = L-1, \dots, 1$:

    - For each unit $i = 1, \dots, n_l$:

      - Compute the error term: $\delta_i^{(l)} = \frac{\partial E}{\partial z_i^{(l)}} = \sum_{j=1}^{n_{l+1}} \frac{\partial E}{\partial z_j^{(l+1)}} \frac{\partial z_j^{(l+1)}}{\partial z_i^{(l)}} = \sum_{j=1}^{n_{l+1}} \delta_j^{(l+