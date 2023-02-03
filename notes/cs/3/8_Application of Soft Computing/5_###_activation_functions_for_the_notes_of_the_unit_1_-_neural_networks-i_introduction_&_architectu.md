### activation functions for the notes of the Unit 1 - Neural Networks-I (Introduction & Architecture) in the subject of Application of Soft Computing

Activation functions are mathematical functions used in artificial neural networks to introduce non-linearity into the network. They are applied element-wise to the output of each neuron and determine the output of the neuron. Popular activation functions include:

1. Sigmoid: The sigmoid function maps any input to the range of 0 and 1, making it useful for binary classification problems.

2. Tanh: The hyperbolic tangent function maps any input to the range of -1 and 1, making it useful for multiclass classification problems.

3. ReLU: The rectified linear unit function returns the input if it is positive, and returns 0 if it is negative. It is widely used in deep learning due to its simplicity and computational efficiency.

4. Leaky ReLU: This is a variant of the ReLU function that allows for a small gradient when the input is negative, avoiding the "dying ReLU" problem.

5. Softmax: The softmax function is used in the output layer of a neural network for multiclass classification problems. It maps the outputs of the neurons to a probability distribution over the classes.

The choice of activation function depends on the problem being solved and the architecture of the network. Activation functions play a crucial role in the training and performance of neural networks, and their design can significantly impact the network's ability to learn and generalize to new data.
