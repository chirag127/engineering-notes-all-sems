### Artificial Neuron and its Model

- An artificial neuron is a mathematical function conceived as a model of biological neurons, a neural network.
- Artificial neurons are elementary units in an artificial neural network that receive one or more inputs and produce an output.
- Artificial neurons are modeled after the hierarchical arrangement of neurons in biological sensory systems, such as the visual system.
- The basic structure of an artificial neuron consists of three components:
  - Input: A set of values representing the excitatory and inhibitory signals from other neurons or external sources.
  - Weight: A set of parameters that determine the strength and direction of the connection between the input and the output.
  - Activation function: A mathematical function that transforms the weighted sum of the inputs into the output value, representing the neuron's firing rate or action potential.
- The output of an artificial neuron can be either binary (0 or 1), continuous (a real number), or discrete (a finite set of values).
- The activation function can be linear, nonlinear, or threshold-based, depending on the desired behavior and complexity of the artificial neuron.
- Some common activation functions are:
  - Sigmoid: A smooth, nonlinear function that maps any input value to a value between 0 and 1, with a steep slope around 0.5. It is often used for classification or probability estimation tasks.
  - Hyperbolic tangent: A smooth, nonlinear function that maps any input value to a value between -1 and 1, with a steep slope around 0. It is similar to the sigmoid function, but has a wider range and is symmetric around the origin. It is often used for regression or approximation tasks.
  - Rectified linear unit (ReLU): A piecewise linear function that maps any positive input value to itself, and any negative input value to 0. It is simple, fast, and sparse, meaning that it produces many zero outputs. It is often used for deep learning or feature extraction tasks.
  - Step: A threshold-based function that maps any input value above a certain threshold to 1, and any input value below or equal to the threshold to 0. It is used for binary classification or decision making tasks.