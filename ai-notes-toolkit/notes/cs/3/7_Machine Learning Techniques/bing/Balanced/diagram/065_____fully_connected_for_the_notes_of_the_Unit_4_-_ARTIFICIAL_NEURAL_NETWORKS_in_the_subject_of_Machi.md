### Fully Connected Neural Network

A fully connected neural network is a type of artificial neural network where the architecture is such that all the nodes, or neurons, in one layer are connected to the neurons in the next layer. A fully connected layer is a function from ℝ m to ℝ n, where each output dimension depends on each input dimension. A fully connected neural network consists of a series of fully connected layers.

Some points to note about fully connected neural networks are:

- The major advantage of fully connected networks is that they are “structure agnostic” i.e. there are no special assumptions about the input data, such as spatial or temporal relationships.
- The major disadvantage of fully connected networks is that they are computationally expensive and prone to overfitting, as they have a large number of parameters and do not exploit any structure in the input data.
- Fully connected networks are often used as the final layers of a neural network, after some feature extraction layers such as convolutional or recurrent layers.
- Fully connected networks are also called dense networks or multilayer perceptrons (MLPs).

A simple example of a fully connected neural network with one input layer, two hidden layers, and one output layer is shown below:

![Fully connected neural network](https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Colored_neural_network.svg/300px-Colored_neural_network.svg.png)

: Fully Connected vs Convolutional Neural Networks, https://medium.com/swlh/fully-connected-vs-convolutional-neural-networks-813ca7bc6ee5
: Fully connected neural network | Radiology Reference Article, https://radiopaedia.org/articles/fully-connected-neural-network?lang=us
: Fully Connected Deep Networks - TensorFlow for Deep Learning, https://www.oreilly.com/library/view/tensorflow-for-deep/9781491980446/ch04.html
: Fully-Connected Neural Network - GM-RKB, https://www.gabormelli.com/RKB/Fully-Connected_Neural_Network
: Fully Connected Layer vs. Convolutional Layer: Explained, https://builtin.com/machine-learning/fully-connected-layer