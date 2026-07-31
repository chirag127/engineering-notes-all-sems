### Activation Functions

Activation functions are an essential component of neural networks. They are used to introduce non-linearity into the model, allowing the network to learn complex relationships between the input and output data.

Some common activation functions used in neural networks are:

1. **Sigmoid Function**: The sigmoid function maps any input value to a value between 0 and 1. It is commonly used in the output layer of binary classification problems.

2. **Hyperbolic Tangent Function**: The hyperbolic tangent function, or tanh, maps any input value to a value between -1 and 1. It is similar to the sigmoid function, but has a steeper gradient.

3. **Rectified Linear Unit (ReLU)**: The ReLU function returns 0 for any negative input value and returns the input value itself for any non-negative input value. It is commonly used in the hidden layers of neural networks.

4. **Leaky ReLU**: The Leaky ReLU function is a variation of the ReLU function that returns a small, non-zero value for negative input values. This can help prevent the "dying ReLU" problem, where a neuron becomes inactive and stops learning.

5. **Softmax Function**: The softmax function is commonly used in the output layer of multi-class classification problems. It maps the input values to a probability distribution over the output classes.

These are just a few examples of the many activation functions that can be used in neural networks. The choice of activation function can have a significant impact on the performance of the model, and it is important to choose an appropriate function for the specific problem at hand.