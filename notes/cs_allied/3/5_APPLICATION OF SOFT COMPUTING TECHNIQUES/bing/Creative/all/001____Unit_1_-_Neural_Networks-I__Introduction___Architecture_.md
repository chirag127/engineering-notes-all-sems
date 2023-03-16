# Unit 1 - Neural Networks-I (Introduction & Architecture)

## Introduction

- Neural networks are computational models that are inspired by the structure and function of biological neurons and the brain.
- Neural networks can learn from data and perform tasks such as classification, regression, clustering, dimensionality reduction, etc.
- Neural networks are composed of artificial neurons or nodes that are connected by weighted links or synapses.
- Neural networks can be trained using various algorithms that adjust the weights and biases of the nodes based on the input-output pairs or the error signals.

## Architecture

- The architecture of a neural network refers to the number, type, and arrangement of the nodes and links in the network.
- The architecture determines the complexity and capacity of the network to learn and generalize from data.
- The most common architecture is the feedforward neural network, where the nodes are organized in layers and the links are directed from one layer to the next.
- The feedforward neural network consists of an input layer, one or more hidden layers, and an output layer.
- The input layer receives the input data and passes it to the first hidden layer. The hidden layers perform nonlinear transformations on the input and pass it to the next layer. The output layer produces the output of the network.
- The number of nodes in the input and output layers depends on the dimensionality of the input and output data. The number of hidden layers and nodes depends on the complexity of the problem and the amount of data available.
- The nodes in each layer are usually fully connected to the nodes in the next layer, meaning that each node receives input from all the nodes in the previous layer and sends output to all the nodes in the next layer.
- The nodes in each layer can also have different activation functions, such as sigmoid, tanh, ReLU, etc., that determine the output of the node given the input.
- The links in the network have weights and biases that are the parameters of the network. The weights represent the strength of the connection between two nodes, and the biases represent the threshold or offset of the node.
- The weights and biases are initialized randomly or using some heuristic methods, and then updated during the training process using gradient-based optimization algorithms, such as gradient descent, backpropagation, etc.