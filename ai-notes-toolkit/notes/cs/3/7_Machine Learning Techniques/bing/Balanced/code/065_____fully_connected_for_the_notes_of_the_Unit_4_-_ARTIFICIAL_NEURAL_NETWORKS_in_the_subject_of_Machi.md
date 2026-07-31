### Fully Connected Neural Network

A fully connected neural network is a type of artificial neural network where the architecture is such that all the nodes, or neurons, in one layer are connected to the neurons in the next layer. A fully connected layer is a function from ℝ m to ℝ n, where each output dimension depends on each input dimension. A fully connected neural network consists of a series of fully connected layers.

Some points to note about fully connected neural networks are:

- The major advantage of fully connected networks is that they are “structure agnostic” i.e. there are no special assumptions about the input data, such as spatial or temporal relationships.
- The major disadvantage of fully connected networks is that they are very computationally expensive and prone to overfitting, as they have a large number of parameters and do not exploit any structure in the input data.
- Fully connected networks are often used as the final layers of a deep neural network, after some convolutional or recurrent layers, to produce the final output or classification.
- Fully connected networks are also called dense networks or multilayer perceptrons (MLPs).