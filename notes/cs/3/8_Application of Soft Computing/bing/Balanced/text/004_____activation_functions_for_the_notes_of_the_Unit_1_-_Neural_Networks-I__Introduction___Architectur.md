### Activation Functions

- Activation functions are mathematical equations that determine the output of a neural network model.
- Activation functions also have a major effect on the neural network’s ability to converge and the convergence speed, or in some cases, activation functions might prevent neural networks from converging in the first place.
- Activation functions decide whether a neuron should be activated or not, based on the input values.
- Activation functions shape the outputs of artificial neurons and, therefore, are integral parts of neural networks in general and deep learning in particular.
- Some examples of activation functions are:
  - Linear: The output is proportional to the input. It is simple and fast, but it cannot handle non-linear problems and it has no threshold.
  - Logistic (or Sigmoid): The output is between 0 and 1. It is smooth and differentiable, but it can suffer from vanishing gradient problem and it is computationally expensive.
  - Hyperbolic Tangent (or Tanh): The output is between -1 and 1. It is also smooth and differentiable, but it can also suffer from vanishing gradient problem and it is computationally expensive.
  - Rectified Linear Unit (or ReLU): The output is 0 if the input is negative, and equal to the input if the input is positive. It is simple and fast, and it can handle non-linear problems, but it can suffer from dying ReLU problem and it is not differentiable at 0.
  - Leaky ReLU: The output is a small negative value if the input is negative, and equal to the input if the input is positive. It is similar to ReLU, but it avoids the dying ReLU problem, and it is slightly differentiable at 0.
  - Softmax: The output is a vector of values between 0 and 1 that sum up to 1. It is useful for multi-class classification problems, but it is computationally expensive and it can suffer from numerical instability.