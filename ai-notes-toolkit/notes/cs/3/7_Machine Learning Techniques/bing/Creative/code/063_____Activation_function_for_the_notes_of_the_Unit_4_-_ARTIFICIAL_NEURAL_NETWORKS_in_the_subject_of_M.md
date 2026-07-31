# Activation function for the notes of the Unit 4 - ARTIFICIAL NEURAL NETWORKS in the subject of Machine Learning Techniques

- An activation function is a function used in artificial neural networks which outputs a small value for small inputs, and a larger value if its inputs exceed a threshold.
- The purpose of the activation function is to introduce non-linearity into the output of a neuron, which enables a neural network to learn complex patterns and perform various tasks .
- Some common types of activation functions are:
  - Linear: The output is proportional to the input, such as `f(x) = x`. This function is simple and fast, but it cannot capture non-linear relationships and it has no threshold for firing.
  - Logistic (or Sigmoid): The output is bounded between 0 and 1, such as `f(x) = 1 / (1 + exp(-x))`. This function is smooth and differentiable, but it can suffer from vanishing gradients and saturation problems .
  - Hyperbolic tangent (or Tanh): The output is bounded between -1 and 1, such as `f(x) = (exp(x) - exp(-x)) / (exp(x) + exp(-x))`. This function is similar to logistic, but it is centered around zero and has a steeper slope .
  - Rectified linear unit (or ReLU): The output is either zero or the input, such as `f(x) = max(0, x)`. This function is simple and efficient, but it can suffer from dying neurons and sparsity problems .
  - Leaky rectified linear unit (or Leaky ReLU): The output is either a small fraction of the input or the input, such as `f(x) = max(0.01x, x)`. This function is a variation of ReLU, but it avoids the dying neuron problem by allowing a small gradient for negative inputs .
  - Exponential linear unit (or ELU): The output is either an exponential function of the input or the input, such as `f(x) = x if x > 0 else alpha * (exp(x) - 1)`. This function is another variation of ReLU, but it avoids the sparsity problem by having a smooth and non-zero gradient for negative inputs .
  - Softmax: The output is a normalized probability distribution over a set of classes, such as `f(x_i) = exp(x_i) / sum(exp(x_j)) for j in 1..n`. This function is often used as the final layer of a neural network for classification tasks, as it can produce a confidence score for each class .
- The choice of activation function depends on the type and complexity of the problem, the architecture and size of the neural network, and the computational and memory resources available . There is no definitive rule for selecting the best activation function, but some general guidelines are:
  - Use non-linear activation functions to enable the neural network to learn non-linear patterns and perform complex tasks .
  - Use activation functions that are differentiable or have a subgradient, to enable the neural network to use gradient-based optimization methods such as backpropagation .
  - Use activation functions that are computationally efficient and avoid numerical instability, such as overflow or underflow .
  - Use activation functions that are suitable for the range and distribution of the input and output values, and avoid saturation or dead zones .
  - Experiment with different activation functions and compare their performance and behavior on the given problem .