### Radial basis function networks

- A radial basis function network (RBFN) is a type of supervised artificial neural network that uses radial basis functions (RBFs) as activation functions .
- RBFs are functions that depend only on the distance from a center point, and can be used to approximate any continuous function .
- RBFNs have a three-layer architecture: an input layer, a hidden layer, and an output layer   .
- The input layer consists of the input vector that is being classified or approximated.
- The hidden layer consists of RBF neurons, each with a center and a width parameter   .
- The output layer consists of linear neurons that compute a weighted sum of the hidden layer outputs   .
- The output of an RBF neuron is given by:

![output of an RBF neuron](https://latex.codecogs.com/png.latex?%5Cphi%28x%29%20%3D%20e%5E%7B-%5Cfrac%7B%5Cleft%5C%7C%20x-c%20%5Cright%5C%7C%5E2%7D%7B2%5Csigma%5E2%7D%7D)

where x is the input vector, c is the center, and σ is the width of the RBF   .

- The output of the RBFN is given by:

![output of the RBFN](https://latex.codecogs.com/png.latex?y%28x%29%20%3D%20%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20w_i%20%5Cphi_i%28x%29)

where n is the number of hidden neurons, w_i are the output weights, and ϕ_i are the RBFs   .

- RBFNs can be used for both classification and regression problems, by choosing the appropriate number and type of output neurons  .
- RBFNs have several advantages, such as:
  - They can approximate any continuous function with arbitrary accuracy  .
  - They have a simple and intuitive structure, with only two types of parameters: the centers and widths of the RBFs, and the output weights   .
  - They have a faster learning speed than other neural networks, as the output weights can be computed by a linear least squares method, and the centers and widths can be determined by clustering algorithms or other heuristics  .
- RBFNs also have some disadvantages, such as:
  - They may suffer from the curse of dimensionality, as the number of RBF neurons may grow exponentially with the input dimension  .
  - They may overfit the data, especially if the RBFs are too narrow or too many  .
  - They may be sensitive to outliers, as the RBFs are influenced by the distance from the center  .