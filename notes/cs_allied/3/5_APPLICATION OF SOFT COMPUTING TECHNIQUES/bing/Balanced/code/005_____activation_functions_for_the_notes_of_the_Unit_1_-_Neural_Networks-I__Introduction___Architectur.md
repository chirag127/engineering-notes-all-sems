### Activation functions for the notes of the Unit 1 - Neural Networks-I (Introduction & Architecture) in the subject of APPLICATION OF SOFT COMPUTING TECHNIQUES

- Activation functions are mathematical equations that determine the output of a neural network model.
- Activation functions also have a major effect on the neural network’s ability to converge and the convergence speed, or in some cases, activation functions might prevent neural networks from converging in the first place.
- Activation functions shape the outputs of artificial neurons and, therefore, are integral parts of neural networks in general and deep learning in particular.
- Activation functions decide whether a neuron should be activated or not. This means that they will decide whether the neuron’s input to the network is important or not in the process of prediction using simpler mathematical operations.
- Activation functions output a small value for small inputs, and a larger value if its inputs exceed a threshold. If the inputs are large enough, the activation function \"fires\", otherwise it does nothing.
- Some common types of activation functions are:
  - Linear: The output is proportional to the input. It is simple and fast, but it cannot handle complex problems and it has no threshold.
  - Logistic (or Sigmoid): The output is between 0 and 1. It is smooth and nonlinear, but it can suffer from vanishing gradient problem and it is computationally expensive.
  - Hyperbolic tangent (or Tanh): The output is between -1 and 1. It is similar to logistic, but it is symmetric and has a steeper slope.
  - Rectified linear unit (or ReLU): The output is 0 for negative inputs and equal to the input for positive inputs. It is simple and fast, but it can suffer from dying ReLU problem and it is not differentiable at 0.
  - Leaky ReLU: The output is a small negative value for negative inputs and equal to the input for positive inputs. It is similar to ReLU, but it avoids the dying ReLU problem and it is differentiable everywhere.
  - Softmax: The output is a probability distribution over a set of classes. It is useful for multiclass classification, but it can suffer from numerical instability and it is computationally expensive.