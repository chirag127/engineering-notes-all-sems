# Activation Functions

- Activation functions are mathematical equations that determine the output of a neural network model.
- Activation functions also have a major effect on the neural network’s ability to converge and the convergence speed, or in some cases, activation functions might prevent neural networks from converging in the first place.
- Activation functions are functions used in a neural network to compute the weighted sum of inputs and biases, which is in turn used to decide whether a neuron can be activated or not.
- Activation functions manipulate the presented data and produce an output for the neural network that contains the parameters in the data.
- Activation functions shape the outputs of artificial neurons and, therefore, are integral parts of neural networks in general and deep learning in particular.
- Activation functions can be linear or nonlinear, depending on whether they have a constant or variable slope.
- Some activation functions, such as logistic and relu, have been used for many decades, while others, such as swish and mish, have been proposed more recently.
- Some of the most common activation functions are:

  - Sigmoid: A nonlinear function that maps any input to a value between 0 and 1. It is useful for binary classification and probability estimation.
  - Tanh: A nonlinear function that maps any input to a value between -1 and 1. It is similar to sigmoid but has a steeper slope and is centered at zero.
  - ReLU: A linear function that maps any positive input to itself and any negative input to zero. It is simple, fast, and widely used in deep learning.
  - Leaky ReLU: A variant of ReLU that maps any negative input to a small fraction of itself, instead of zero. It helps to avoid the problem of dying neurons that do not activate.
  - Swish: A nonlinear function that maps any input to itself multiplied by the sigmoid of itself. It is smooth, self-gated, and has been shown to perform better than ReLU in some cases.
  - Mish: A nonlinear function that maps any input to itself multiplied by the tanh of the softplus of itself. It is smooth, self-regularized, and has been shown to perform better than swish in some cases.

- Activation functions are essential for neural networks to learn complex and nonlinear patterns from the data.
- Activation functions should be chosen based on the type of problem, the type of data, and the desired output.