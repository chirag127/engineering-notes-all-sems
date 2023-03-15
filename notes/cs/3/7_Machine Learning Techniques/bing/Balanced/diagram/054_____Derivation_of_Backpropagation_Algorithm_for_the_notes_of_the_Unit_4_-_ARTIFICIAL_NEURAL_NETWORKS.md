### Derivation of Backpropagation Algorithm

Backpropagation, short for "backward propagation of errors," is an algorithm for supervised learning of artificial neural networks using gradient descent. Given an artificial neural network and an error function, the method calculates the gradient of the error function with respect to the neural network's weights.

The derivation of the backpropagation algorithm is based on the following steps :

- Define the network architecture, the activation functions, the error function, and the input and output data.
- Initialize the network weights randomly or with some heuristic method.
- For each input-output pair in the training data, do the following:
  - Perform a forward pass through the network, computing the outputs of each layer and the final output.
  - Compute the error between the final output and the target output, and the gradient of the error function with respect to the final output.
  - Perform a backward pass through the network, computing the gradient of the error function with respect to each weight by applying the chain rule and the product rule of calculus.
  - Update each weight by subtracting a fraction of its gradient, where the fraction is determined by the learning rate parameter.
- Repeat the above steps until the error function reaches a minimum or a stopping criterion is met.

The following diagram illustrates the backpropagation algorithm for a simple network with one hidden layer and one output unit:

![Backpropagation diagram](https://www.cs.swarthmore.edu/~meeden/cs81/s10/BackPropDeriv_files/image002.gif)

The notation used in the diagram is as follows:

- $x_i$ are the input units, $h_j$ are the hidden units, and $y_k$ are the output units.
- $w_{ij}$ are the weights from input unit $i$ to hidden unit $j$, and $v_{jk}$ are the weights from hidden unit $j$ to output unit $k$.
- $b_j$ and $c_k$ are the bias terms for the hidden and output units, respectively.
- $f$ and $g$ are the activation functions for the hidden and output units, respectively.
- $t_k$ are the target values for the output units.
- $E$ is the error function, which is usually the sum of squared errors: $E = \frac{1}{2} \sum_k (t_k - y_k)^2$.

The forward pass computes the outputs of each layer as follows:

- $h_j = f(\sum_i w_{ij} x_i + b_j)$
- $y_k = g(\sum_j v_{jk} h_j + c_k)$

The backward pass computes the gradients of the error function with respect to each weight as follows:

- $\frac{\partial E}{\partial y_k} = -(t_k - y_k)$
- $\frac{\partial E}{\partial v_{jk}} = \frac{\partial E}{\partial y_k} \frac{\partial y_k}{\partial v_{jk}} = -(t_k - y_k) g'(\sum_j v_{jk} h_j + c_k) h_j$
- $\frac{\partial E}{\partial c_k} = \frac{\partial E}{\partial y_k} \frac{\partial y_k}{\partial c_k} = -(t_k - y_k) g'(\sum_j v_{jk} h_j + c_k)$
- $\frac{\partial E}{\partial h_j} = \sum_k \frac{\partial E}{\partial y_k} \frac{\partial y_k}{\partial h_j} = \sum_k -(t_k - y_k) g'(\sum_j v_{jk} h_j + c_k) v_{jk}$
- $\frac{\partial E}{\partial w_{ij}} = \frac{\partial E}{\partial h_j} \frac{\partial h_j}{\partial w_{ij}} = \sum_k -(t_k - y_k) g'(\sum_j v_{jk} h_j + c_k) v_{jk} f'(\sum_i w_{ij} x_i + b_j) x_i$
- $\frac{\partial E}{\partial b_j} = \frac{\partial E}{\partial h_j} \frac{\partial h_j}{\partial b_j} = \sum_k -(t_k - y_k) g'(\sum_j v_{jk} h_j + c_k) v_{jk}