### Artificial Neuron and its model

- An artificial neuron is a mathematical function that is inspired by the structure and function of biological neurons, which are the basic units of the nervous system.
- An artificial neuron is also called a node or a unit in an artificial neural network, which is a computational model that mimics the learning and processing abilities of the brain.
- An artificial neuron receives one or more inputs, which can be numerical values or signals from other artificial neurons, and computes an output based on a weighted sum of the inputs and a non-linear activation function.
- The weights are adjustable parameters that determine the strength and direction of the influence of each input on the output. The activation function is a mathematical function that maps the weighted sum to a desired output range, such as 0 or 1, or -1 or 1, or any continuous interval.
- The activation function can also introduce non-linearity to the artificial neuron, which enables it to model complex phenomena that are not linearly separable, such as XOR logic or image recognition.
- The most common activation functions are sigmoid, tanh, ReLU, and softmax, but there are many other types and variations of activation functions that can be used depending on the task and the data.
- An artificial neuron can be represented graphically as a circle or a rectangle with input arrows and an output arrow, or mathematically as a function of the form:

  `y = f(w1x1 + w2x2 + ... + wnxn + b)`

  where `y` is the output, `f` is the activation function, `w` are the weights, `x` are the inputs, and `b` is the bias term, which is an additional parameter that shifts the weighted sum by a constant value.

- An artificial neuron can be modeled at different levels of abstraction, from the biological level, which considers the electrochemical processes and the spiking behavior of the neuron, to the logical level, which considers the neuron as a binary or discrete unit that performs logical operations, to the computational level, which considers the neuron as a continuous or analog unit that performs numerical computations.

- The artificial neuron model was first proposed by Warren McCulloch and Walter Pitts in 1943, and later refined by Frank Rosenblatt, who developed the perceptron, one of the earliest and simplest types of artificial neural networks, in 1958. Since then, many variations and extensions of the artificial neuron model have been developed, such as the radial basis function neuron, the adaptive linear neuron, the stochastic neuron, and the spiking neuron.