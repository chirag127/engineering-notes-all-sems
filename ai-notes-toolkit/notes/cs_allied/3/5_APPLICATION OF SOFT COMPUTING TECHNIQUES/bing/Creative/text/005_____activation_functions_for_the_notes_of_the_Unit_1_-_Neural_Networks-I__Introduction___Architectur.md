### Activation Functions

- Activation functions are mathematical equations that determine the output of a neural network model.
- Activation functions also have a major effect on the neural network’s ability to converge and the convergence speed, or in some cases, activation functions might prevent neural networks from converging in the first place.
- Activation functions shape the outputs of artificial neurons and, therefore, are integral parts of neural networks in general and deep learning in particular.
- Activation functions decide whether a neuron should be activated or not, based on the input values.
- Activation functions can be linear or nonlinear, depending on whether they have a constant or variable slope.
- Some common activation functions are:
  - Sigmoid: A nonlinear function that maps any input value to a value between 0 and 1. It is useful for binary classification problems and has a smooth gradient.
  - Tanh: A nonlinear function that maps any input value to a value between -1 and 1. It is similar to sigmoid but has a steeper gradient and is centered at zero.
  - ReLU: A nonlinear function that maps any input value to a value greater than or equal to zero. It is simple and fast to compute and has a sparse output.
  - Leaky ReLU: A nonlinear function that maps any input value to a value greater than or equal to zero, except for negative values which are multiplied by a small constant. It is a variation of ReLU that avoids the problem of dying neurons.
  - Softmax: A nonlinear function that maps any input value to a probability distribution over a set of classes. It is useful for multi-class classification problems and has a smooth gradient.
- Some factors to consider when choosing an activation function are:
  - The type and complexity of the problem.
  - The range and distribution of the input and output values.
  - The computational efficiency and stability of the function.
  - The gradient and its effect on the learning process.