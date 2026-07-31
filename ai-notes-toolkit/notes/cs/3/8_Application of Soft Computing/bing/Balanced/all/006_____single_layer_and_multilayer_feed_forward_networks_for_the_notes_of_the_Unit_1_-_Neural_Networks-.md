# Single Layer and Multilayer Feed Forward Networks

- A feed forward neural network is an artificial neural network where the information flows only in one direction, from input to output.
- A feed forward neural network consists of three main parts: an input layer, one or more hidden layers, and an output layer.
- Each layer consists of one or more computational units, called neurons, that perform some mathematical operations on the inputs and produce outputs.
- Each neuron in one layer has directed connections to the neurons of the subsequent layer, and each connection has a weight that determines the strength of the signal.
- The output of a neuron is usually passed through an activation function, such as a sigmoid function, to introduce non-linearity and to limit the range of the output.

## Single Layer Feed Forward Network

- A single layer feed forward network is the simplest type of feed forward neural network, where there is only one layer of neurons between the input and output layers.
- A single layer feed forward network can compute a linear or a nonlinear function of the inputs, depending on the choice of the activation function.
- A common choice of the activation function is the logistic function, which produces a continuous output between 0 and 1.
- With this choice, the single layer network is identical to the logistic regression model, widely used in statistical modeling.
- A single layer feed forward network can be used for binary classification problems, where the output is either 0 or 1, depending on the input features.
- A single layer feed forward network can also be used for regression problems, where the output is a continuous value, such as the price of a house or the age of a person.
- A single layer feed forward network can be trained using gradient descent or other optimization algorithms, by minimizing a loss function that measures the difference between the actual and predicted outputs.

## Multilayer Feed Forward Network

- A multilayer feed forward network is a more complex type of feed forward neural network, where there are one or more hidden layers of neurons between the input and output layers.
- A multilayer feed forward network can compute more complex and nonlinear functions of the inputs, by combining the outputs of the hidden layers.
- A multilayer feed forward network can be used for more challenging classification and regression problems, where a single layer network may not be able to capture the underlying patterns or relationships in the data.
- A multilayer feed forward network can also be used for other tasks, such as image recognition, natural language processing, speech recognition, and so on, by using different types of neurons and activation functions.
- A multilayer feed forward network can be trained using backpropagation, which is an extension of gradient descent, that updates the weights of the network by propagating the errors from the output layer to the hidden layers.