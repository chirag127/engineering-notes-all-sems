### Activation Functions

Activation functions are an essential component of neural networks. They are used to introduce non-linearity into the network, allowing it to model complex data patterns. Here are some common activation functions used in neural networks:

1. **Sigmoid Function**: The sigmoid function maps any input value to a value between 0 and 1. It is commonly used in the output layer of a binary classification problem.

2. **Hyperbolic Tangent Function**: The hyperbolic tangent function, or tanh, maps any input value to a value between -1 and 1. It is similar to the sigmoid function, but is centered around 0.

3. **Rectified Linear Unit (ReLU)**: The ReLU function returns 0 for any negative input value and returns the input value itself for any non-negative input value. It is commonly used in the hidden layers of a neural network.

4. **Leaky ReLU**: The Leaky ReLU function is a variation of the ReLU function. It returns a small, non-zero value for negative input values, instead of 0. This can help prevent the "dying ReLU" problem, where a neuron becomes inactive and stops learning.

5. **Softmax Function**: The softmax function is commonly used in the output layer of a multi-class classification problem. It maps the input values to a probability distribution over the possible classes.

These are just a few examples of activation functions used in neural networks. The choice of activation function depends on the specific problem and architecture of the neural network. It is important to experiment with different activation functions to find the one that works best for the given problem.