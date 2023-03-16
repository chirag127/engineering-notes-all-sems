# Activation Functions

- Activation functions are mathematical equations that determine the output of a neural network model.
- Activation functions also have a major effect on the neural network’s ability to converge and the convergence speed, or in some cases, activation functions might prevent neural networks from converging in the first place.
- Activation functions decide whether a neuron should be activated or not, based on the input values.
- Activation functions shape the outputs of artificial neurons and, therefore, are integral parts of neural networks in general and deep learning in particular.
- Some common types of activation functions are:
  - Linear: The output is proportional to the input. It is simple and fast, but it cannot handle complex problems and it has no threshold.
  - Sigmoid: The output is a value between 0 and 1. It is smooth and nonlinear, but it can suffer from vanishing gradient problem and it is computationally expensive.
  - Tanh: The output is a value between -1 and 1. It is similar to sigmoid, but it is centered around zero. It can also suffer from vanishing gradient problem and it is computationally expensive.
  - ReLU: The output is either 0 or the input value. It is simple and nonlinear, but it can handle complex problems and it has a threshold. It can suffer from dying ReLU problem and it is not differentiable at zero.
  - Leaky ReLU: The output is either a small negative value or the input value. It is similar to ReLU, but it avoids the dying ReLU problem. It is not differentiable at zero.
  - Softmax: The output is a vector of values between 0 and 1 that sum up to 1. It is used for multi-class classification problems. It is smooth and nonlinear, but it can suffer from numerical instability and it is computationally expensive.