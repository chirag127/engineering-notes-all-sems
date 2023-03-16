### What a shallow network computes

- A shallow network is a neural network that has only one hidden layer between the input and output layers.
- A shallow network can be seen as a function that maps an input vector x to an output vector y, using a weight matrix W and a bias vector b.
- A shallow network computes y = f(Wx + b), where f is a nonlinear activation function applied element-wise to the vector Wx + b.
- A shallow network can learn to approximate any continuous function on a compact domain, given enough hidden units and appropriate activation functions, according to the universal approximation theorem.
- A shallow network can also be interpreted as a linear classifier that projects the input vector x to a lower-dimensional space, where the classes are more separable, and then applies a decision boundary based on the activation function f.