### Activation Functions

- Activation functions are mathematical equations that determine the output of a neural network model.
- Activation functions also have a major effect on the neural network’s ability to converge and the convergence speed, or in some cases, activation functions might prevent neural networks from converging in the first place.
- Activation functions shape the outputs of artificial neurons and, therefore, are integral parts of neural networks in general and deep learning in particular.
- Activation functions decide whether a neuron should be activated or not, based on the input values.
- Activation functions can be linear or nonlinear, depending on whether they have a constant or variable slope.
- Some common activation functions are:
  - Sigmoid: A nonlinear function that maps any input value to a value between 0 and 1. It is often used for binary classification or probability estimation.
  - Tanh: A nonlinear function that maps any input value to a value between -1 and 1. It is similar to sigmoid but has a steeper slope and is centered at zero.
  - ReLU: A nonlinear function that maps any input value to a value greater than or equal to zero. It is the most widely used activation function in deep learning because it is simple, fast, and avoids the vanishing gradient problem.
  - Leaky ReLU: A nonlinear function that maps any input value to a value greater than or equal to a small constant. It is a variation of ReLU that allows a small amount of negative output to avoid the dying ReLU problem.
  - Softmax: A nonlinear function that maps a vector of input values to a vector of output values that sum up to one. It is often used for multi-class classification or probability distribution.