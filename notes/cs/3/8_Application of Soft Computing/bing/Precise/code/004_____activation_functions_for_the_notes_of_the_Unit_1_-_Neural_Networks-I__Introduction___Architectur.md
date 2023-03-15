### Activation Functions

Activation functions are used in artificial neural networks to introduce non-linearity into the model. They are applied to the output of a neuron, or node, in the network and determine whether the neuron should be activated or not. Some common activation functions used in neural networks are:

1. **Sigmoid Function:** The sigmoid function maps any input value to a value between 0 and 1. It is commonly used in the output layer of a binary classification problem.

2. **Hyperbolic Tangent Function:** The hyperbolic tangent function, or tanh, maps any input value to a value between -1 and 1. It is similar to the sigmoid function but has a steeper gradient.

3. **Rectified Linear Unit (ReLU):** The ReLU function returns 0 for any negative input value and returns the input value itself for any non-negative input value. It is commonly used in the hidden layers of a neural network.

4. **Leaky ReLU:** The Leaky ReLU function is a variation of the ReLU function that returns a small, non-zero value for negative input values. This can help prevent the "dying ReLU" problem, where a neuron can become inactive and stop updating during training.

5. **Softmax Function:** The softmax function is used in the output layer of a multi-class classification problem. It maps the input values to a probability distribution over the possible classes.

These are some of the commonly used activation functions in neural networks. The choice of activation function can depend on the specific problem and the architecture of the neural network. It is important to experiment with different activation functions to find the best fit for the problem at hand.