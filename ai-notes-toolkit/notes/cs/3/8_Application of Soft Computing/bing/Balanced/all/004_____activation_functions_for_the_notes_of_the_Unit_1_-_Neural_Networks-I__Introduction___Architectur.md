# Activation Functions

- Activation functions are mathematical equations that determine the output of a neural network model.
- Activation functions also have a major effect on the neural network’s ability to converge and the convergence speed, or in some cases, activation functions might prevent neural networks from converging in the first place.
- Activation functions are functions used in a neural network to compute the weighted sum of inputs and biases, which is in turn used to decide whether a neuron can be activated or not.
- Activation functions manipulate the presented data and produce an output for the neural network that contains the parameters in the data.
- Activation functions shape the outputs of artificial neurons and, therefore, are integral parts of neural networks in general and deep learning in particular.
- Some activation functions, such as logistic and relu, have been used for many decades.
- Activation functions can take many forms, but they are usually found as one of the following functions:
  - Linear: f(x) = x
  - Binary: f(x) = 1 if x > 0, 0 otherwise
  - Sigmoid: f(x) = 1 / (1 + exp(-x))
  - Tanh: f(x) = (exp(x) - exp(-x)) / (exp(x) + exp(-x))
  - ReLU: f(x) = max(0, x)
  - Leaky ReLU: f(x) = max(0.01x, x)
  - Softmax: f(x) = exp(x) / sum(exp(x))
- Activation functions have different properties and advantages, such as non-linearity, differentiability, monotonicity, range, and saturation.
- Activation functions are chosen based on the type of problem, the architecture of the network, and the desired output.
- Activation functions are essential for neural networks to learn complex patterns and perform non-linear transformations.