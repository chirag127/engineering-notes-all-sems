# Single Layer and Multilayer Feed Forward Networks

- A feed forward network is a type of artificial neural network (ANN) that consists of multiple layers of computational units, usually interconnected in a feed-forward way.
- Feed forward means that data and calculations flow in a single direction, from the input data to the outputs, without any feedback loops or cycles.
- Each unit in one layer has directed connections to the units of the subsequent layer, and applies an activation function to its weighted inputs.
- The activation function determines the output of the unit, and can be linear or nonlinear, such as sigmoid, tanh, ReLU, etc.
- The simplest feed forward network is one with a single input layer and an output layer of units, also called a single-layer feed forward network or a perceptron.
- A single-layer feed forward network can perform binary classification or regression tasks, depending on the activation function and the output format.
- A single-layer feed forward network can also be seen as a linear or logistic regression model, if the activation function is identity or logistic, respectively.
- A single-layer feed forward network has limited expressive power, as it can only learn linearly separable patterns or functions.
- To overcome this limitation, one or more intermediate layers of units can be added between the input and output layer, forming a multilayer feed forward network or a multilayer perceptron (MLP).
- A multilayer feed forward network can learn nonlinear and complex patterns or functions, by combining the outputs of the hidden layers in a hierarchical way.
- A multilayer feed forward network can perform various tasks, such as classification, regression, approximation, prediction, etc., depending on the activation function, the output format, and the loss function.
- A multilayer feed forward network can also be seen as a universal function approximator, as it can approximate any continuous function to any desired degree of accuracy, given enough hidden units and training data.
- A multilayer feed forward network is trained using a supervised learning algorithm, such as gradient descent, backpropagation, or stochastic gradient descent, which updates the weights of the connections based on the error between the actual and desired outputs.
- A multilayer feed forward network can suffer from overfitting, underfitting, local minima, vanishing or exploding gradients, and other challenges, which require careful design and regularization techniques to overcome.