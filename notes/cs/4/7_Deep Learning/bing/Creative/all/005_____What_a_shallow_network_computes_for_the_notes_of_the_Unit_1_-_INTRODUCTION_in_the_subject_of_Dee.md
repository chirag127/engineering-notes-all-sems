# What a shallow network computes

- A shallow network is a neural network that has only one hidden layer between the input and the output layers.
- A shallow network can be seen as a function that maps an input vector x to an output vector y, using a weight matrix W and a bias vector b.
- The output of a shallow network can be computed as y = f(Wx + b), where f is an activation function that applies element-wise to the vector Wx + b.
- The activation function f can be linear or nonlinear, such as sigmoid, tanh, ReLU, etc.
- A shallow network can learn to approximate any continuous function on a compact domain, according to the universal approximation theorem, if the hidden layer has enough units and the activation function is nonlinear.
- A shallow network can also be seen as a linear transformation followed by a nonlinear transformation, or as a feature extractor followed by a classifier or regressor.
- A shallow network can be trained using gradient-based methods, such as gradient descent, stochastic gradient descent, or variants thereof, by minimizing a loss function that measures the discrepancy between the network output and the desired output.
- A shallow network can be used for various tasks, such as classification, regression, clustering, dimensionality reduction, etc., depending on the choice of the activation function and the loss function.