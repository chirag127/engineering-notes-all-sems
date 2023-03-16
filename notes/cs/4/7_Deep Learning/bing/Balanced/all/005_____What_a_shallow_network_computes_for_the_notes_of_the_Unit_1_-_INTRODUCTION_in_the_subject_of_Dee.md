# What a shallow network computes

- A shallow network is a neural network that has only one hidden layer between the input and the output layers.
- A shallow network can be seen as a function that maps an input vector x to an output vector y, using a weight matrix W and a bias vector b.
- A shallow network computes the output y by applying a linear transformation to the input x, followed by a nonlinear activation function f, such as sigmoid, tanh, or ReLU.
- Mathematically, the output y of a shallow network can be written as:

  y = f(Wx + b)

- A shallow network can learn to approximate any continuous function, given enough hidden units and appropriate activation functions, according to the universal approximation theorem.
- However, a shallow network may require exponentially many hidden units to learn complex functions, and may suffer from overfitting or underfitting problems.
- A shallow network can be trained using gradient-based optimization methods, such as gradient descent, stochastic gradient descent, or backpropagation.
- A shallow network can be used for various tasks, such as regression, classification, clustering, dimensionality reduction, or feature extraction.