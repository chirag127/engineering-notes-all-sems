### Multilayer networks for the notes of the Unit 4 - ARTIFICIAL NEURAL NETWORKS in the subject of Machine Learning Techniques

- A multilayer network is an artificial neural network that contains more than one layer of artificial neurons or nodes .
- The layers of a multilayer network are typically divided into three types: input layer, hidden layer(s), and output layer.
- The input layer receives the input data and passes it to the first hidden layer. The hidden layer(s) perform some computation on the input data and pass it to the next layer. The output layer produces the final output of the network.
- Each node in a layer is connected to every node in the next layer, and each connection has a weight associated with it. The weights are the parameters of the network that are learned during the training process .
- Each node also has an activation function that determines the output of the node based on the weighted sum of its inputs. The activation function can be linear or nonlinear, such as sigmoid, tanh, ReLU, etc .
- A multilayer network can be represented by a directed graph, where the nodes are the neurons and the edges are the connections. The following diagram is an example of a multilayer network with one input layer, two hidden layers, and one output layer:

```
  Input layer     Hidden layer 1    Hidden layer 2    Output layer
    x1  o--------o  h1  o--------o  h3  o--------o  y1  o
        |        |     |        |     |        |
    x2  o--------o  h2  o--------o  h4  o--------o  y2  o
```

- A multilayer network can learn complex nonlinear functions that a single-layer network cannot. It can also approximate any continuous function to any desired degree of accuracy, given enough hidden nodes and appropriate activation functions.
- A multilayer network can be trained using various algorithms, such as gradient descent, backpropagation, stochastic gradient descent, etc. The goal of the training is to minimize the error between the network output and the desired output for a given set of input data.
- A multilayer network can be used for various applications, such as classification, regression, clustering, dimensionality reduction, etc. It can also be combined with other techniques, such as convolutional layers, recurrent layers, dropout, etc., to form more advanced models.