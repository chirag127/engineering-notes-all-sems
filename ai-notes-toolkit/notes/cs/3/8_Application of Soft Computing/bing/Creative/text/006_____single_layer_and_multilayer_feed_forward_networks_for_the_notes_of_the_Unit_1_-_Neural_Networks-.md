### Single Layer and Multilayer Feed Forward Networks

- A feed forward network is a type of artificial neural network in which data and calculations flow in a single direction, from the input layer to the output layer, without any feedback loops.
- A single layer feed forward network consists of only two layers: an input layer and an output layer of neurons (also called perceptrons or units).
- A multilayer feed forward network consists of more than two layers: an input layer, one or more hidden layers, and an output layer of neurons.
- The hidden layers are internal to the network and have no direct connection to the external inputs or outputs.
- Each neuron in one layer has directed connections (also called weights or synapses) to the neurons of the subsequent layer.
- The neurons in each layer apply an activation function to their weighted inputs to produce their outputs.
- A common choice of activation function is the sigmoid function, which has a continuous and differentiable output between 0 and 1.
- The output of the network is determined by the values of the weights and the activation functions.
- The network can learn to approximate any function by adjusting the weights based on the training data and a learning algorithm.
- A common learning algorithm is the backpropagation algorithm, which uses the gradient descent method to minimize the error between the network output and the desired output for each training example.
- The network can generalize to new inputs that are not in the training data by finding a suitable representation of the input-output mapping in the hidden layers.