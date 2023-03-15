### Single Layer and Multilayer Feed Forward Networks

- A feed forward network is a type of artificial neural network in which data and calculations flow in a single direction, from the input layer to the output layer, without any feedback loops.
- A single layer feed forward network consists of only two layers: an input layer and an output layer of neurons (also called perceptrons).
- A multilayer feed forward network consists of more than two layers: an input layer, one or more hidden layers, and an output layer of neurons.
- The hidden layers are internal to the network and have no direct connection with the external inputs or outputs.
- Each neuron in one layer has directed connections to the neurons of the subsequent layer, forming a fully connected network.
- The neurons in each layer apply an activation function to their weighted inputs to produce their outputs, which are then fed to the next layer.
- A common choice of activation function is the sigmoid function, which has a continuous and differentiable output between 0 and 1.
- The advantage of multilayer feed forward networks over single layer networks is that they can learn more complex and nonlinear functions, and can approximate any continuous function to any desired degree of accuracy.
- The disadvantage of multilayer feed forward networks is that they are more difficult to train and require more computational resources.
- The most common learning algorithm for multilayer feed forward networks is the backpropagation algorithm, which uses gradient descent to adjust the weights of the network based on the error between the actual and desired outputs.