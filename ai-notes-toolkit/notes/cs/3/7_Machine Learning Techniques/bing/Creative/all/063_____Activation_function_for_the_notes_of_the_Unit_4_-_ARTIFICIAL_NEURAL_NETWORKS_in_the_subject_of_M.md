# Activation function

- An activation function is a function used in artificial neural networks that determines the output of a node or a neuron given an input or a set of inputs.
- Activation functions are essential for neural networks because they enable them to learn complex and non-linear patterns from the data.
- Activation functions also introduce non-linearity into the network, which allows it to approximate any function.
- Activation functions can be linear or non-linear, depending on whether they preserve or change the linearity of the input.
- Some examples of activation functions are:

  - Logistic or sigmoid function: It is a non-linear function that maps any input to a value between 0 and 1. It is often used for binary classification or as the final layer of a neural network .
  - Rectified linear unit (ReLU) function: It is a non-linear function that outputs the input if it is positive, and 0 otherwise. It is simple and efficient, and widely used for hidden layers of a neural network .
  - Hyperbolic tangent (tanh) function: It is a non-linear function that maps any input to a value between -1 and 1. It is similar to the sigmoid function, but has a steeper gradient and is centered at 0 .
  - Softmax function: It is a non-linear function that outputs a probability distribution over a set of classes. It is often used for multi-class classification or as the final layer of a neural network .

- The choice of activation function depends on the type of problem, the architecture of the network, and the desired properties of the output.
- Some of the properties of activation functions that affect their performance are:

  - Derivability: The activation function should be differentiable, or at least have a subgradient, to enable gradient-based optimization methods such as backpropagation.
  - Monotonicity: The activation function should be monotonic, or at least piecewise monotonic, to ensure the existence and uniqueness of a fixed point.
  - Range: The activation function should have a finite or bounded range, or at least avoid saturation or explosion, to prevent numerical instability and vanishing or exploding gradients.
  - Smoothness: The activation function should be smooth, or at least have a continuous first derivative, to facilitate optimization and generalization.
  - Sparsity: The activation function should induce sparsity, or at least have a non-zero output for a non-zero input, to enhance the representation power and interpretability of the network.
  - Symmetry: The activation function should be symmetric, or at least have a zero mean, to reduce the bias and variance of the network.

- Activation functions are an active area of research in artificial neural networks and deep learning, and new activation functions are constantly being proposed and evaluated.