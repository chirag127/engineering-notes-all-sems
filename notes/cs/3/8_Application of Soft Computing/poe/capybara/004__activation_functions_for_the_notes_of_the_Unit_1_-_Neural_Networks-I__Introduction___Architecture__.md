### Activation Functions

In neural networks, activation functions are used to introduce non-linearity in the output of a neuron. The choice of activation function plays a crucial role in determining the performance of the neural network. Here are some commonly used activation functions:

1. Sigmoid Function

   Sigmoid function is a non-linear activation function that maps any input value to a value between 0 and 1. It is widely used in the output layer of binary classification problems. However, it is not recommended for deep neural networks due to the vanishing gradient problem.

2. ReLU Function

   Rectified Linear Unit (ReLU) function is a non-linear activation function that maps any input value less than 0 to 0 and any input value greater than or equal to 0 to the same value. It is widely used in deep neural networks due to its simplicity and effectiveness.

3. Leaky ReLU Function

   Leaky ReLU function is a modification of the ReLU function that adds a small positive slope to negative input values. It is used to address the dying ReLU problem, which occurs when the gradient of the ReLU function becomes 0 for negative input values.

4. Tanh Function

   Hyperbolic Tangent (tanh) function is a non-linear activation function that maps any input value to a value between -1 and 1. It is widely used in the hidden layers of neural networks.

5. Softmax Function

   Softmax function is a non-linear activation function that maps any input value to a value between 0 and 1, which represents the probability of the input belonging to a particular class. It is widely used in the output layer of multi-class classification problems.

In conclusion, the choice of activation function depends on the problem at hand and the architecture of the neural network. It is important to experiment with different activation functions to find the one that gives the best performance.