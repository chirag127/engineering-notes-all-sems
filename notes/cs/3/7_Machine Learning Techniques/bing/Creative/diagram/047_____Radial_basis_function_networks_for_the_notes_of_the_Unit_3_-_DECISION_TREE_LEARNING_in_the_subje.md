### Radial basis function networks

- A radial basis function network (RBFN) is a type of supervised artificial neural network that uses radial basis functions (RBFs) as activation functions .
- RBFs are functions that depend only on the distance from a center point, and can be used to approximate any continuous function .
- RBFNs have three layers: an input layer, a hidden layer, and an output layer .
- The input layer consists of the input vector that is being classified or regressed.
- The hidden layer consists of RBF neurons, each with a center and a width parameter .
- The output layer consists of linear neurons that compute a weighted sum of the hidden layer outputs .
- The output of an RBF neuron is given by:

$$
y_i = \phi(||x - c_i||)
$$

where $y_i$ is the output of the $i$-th RBF neuron, $x$ is the input vector, $c_i$ is the center of the $i$-th RBF neuron, and $\phi$ is the RBF function .

- Common choices for the RBF function are the Gaussian function, the multiquadric function, and the inverse multiquadric function .
- The output of the RBFN is given by:

$$
y = \sum_{i=1}^n w_i y_i
$$

where $y$ is the output of the RBFN, $w_i$ is the weight of the $i$-th RBF neuron, and $n$ is the number of RBF neurons .

- The training of an RBFN involves two steps: determining the centers and widths of the RBF neurons, and determining the weights of the output layer .
- The centers and widths of the RBF neurons can be determined by various methods, such as k-means clustering, random selection, or orthogonal least squares .
- The weights of the output layer can be determined by solving a linear system of equations, using the pseudo-inverse method, or using gradient descent .
- RBFNs have several advantages, such as fast training, universal approximation, and local generalization  .
- RBFNs also have some disadvantages, such as the need to choose the number and location of the RBF neurons, the sensitivity to outliers, and the possibility of overfitting  .