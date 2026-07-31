### Activation function for the notes of the Unit 4 - ARTIFICIAL NEURAL NETWORKS in the subject of Machine Learning Techniques

- An activation function is a function used in artificial neural networks which outputs a small value for small inputs, and a larger value if its inputs exceed a threshold.
- If the inputs are large enough, the activation function "fires", otherwise it does nothing.
- Activation functions are an essential part of an artificial neural network. They enable a neural network to be built by stacking layers on top of each other, glued together with activation functions.
- Activation functions shape the outputs of artificial neurons and, therefore, are integral parts of neural networks in general and deep learning in particular.
- Some activation functions, such as logistic and relu, have been used for many decades. But with deep learning becoming a mainstream research topic, new activation functions have been proposed and studied.
- In artificial neural networks, the activation function of a node defines the output of that node given an input or set of inputs.
- A standard integrated circuit can be seen as a digital network of activation functions that can be "ON" (1) or "OFF" (0), depending on input.
- Some common types of activation functions are:
  - Linear: f(x) = x
  - Sigmoid: f(x) = 1 / (1 + exp(-x))
  - Tanh: f(x) = (exp(x) - exp(-x)) / (exp(x) + exp(-x))
  - ReLU: f(x) = max(0, x)
  - Leaky ReLU: f(x) = max(0.01x, x)
  - Softmax: f(x) = exp(x) / sum(exp(x))