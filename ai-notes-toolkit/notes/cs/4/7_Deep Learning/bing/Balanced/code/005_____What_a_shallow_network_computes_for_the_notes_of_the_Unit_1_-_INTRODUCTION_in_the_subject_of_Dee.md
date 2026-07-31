### What a shallow network computes

- A shallow network is a neural network that has only one hidden layer between the input and the output layers.
- A shallow network can be seen as a function that maps an input vector x to an output vector y, using a set of parameters w and b.
- The output of a shallow network can be written as:

```
y = f(w^T x + b)
```

where f is a nonlinear activation function, such as sigmoid, tanh, or ReLU.

- A shallow network can compute a variety of functions, depending on the choice of the activation function and the parameters.
- Some examples of functions that a shallow network can compute are:

  - Linear regression: If f is the identity function, then the network performs a linear transformation of the input, and can be used for regression tasks.
  - Logistic regression: If f is the sigmoid function, then the network outputs a probability between 0 and 1, and can be used for binary classification tasks.
  - Multiclass classification: If f is the softmax function, then the network outputs a probability distribution over K classes, and can be used for multiclass classification tasks.
  - XOR: If f is a nonlinear function, such as tanh or ReLU, then the network can learn to compute the XOR function, which is not linearly separable.
  - Universal approximation: If f is a nonlinear function, such as tanh or ReLU, then the network can approximate any continuous function on a compact domain, given enough hidden units and appropriate parameters, according to the universal approximation theorem.