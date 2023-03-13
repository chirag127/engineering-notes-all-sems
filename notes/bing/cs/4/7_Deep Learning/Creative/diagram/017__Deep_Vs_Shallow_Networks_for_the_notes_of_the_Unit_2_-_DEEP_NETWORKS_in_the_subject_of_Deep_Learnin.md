The following is a detailed ASCII diagram for Deep Vs Shallow Networks for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning.

### Deep Vs Shallow Networks

A shallow network is a neural network that has only one hidden layer between the input and the output layers. A deep network is a neural network that has more than one hidden layer. Both types of networks can approximate any function, but deep networks can do so more efficiently and accurately than shallow networks .

The diagram below illustrates the basic architecture of a shallow network and a deep network. Each circle represents a neuron, and each line represents a connection with a weight. The input layer receives the data, the hidden layer(s) process the data, and the output layer produces the prediction.

Shallow Network:

    Input Layer     Hidden Layer     Output Layer
    +---------+     +---------+      +---------+
    | x1      |-----| h1      |------| y1      |
    +---------+     +---------+      +---------+
    | x2      |-----| h2      |------| y2      |
    +---------+     +---------+      +---------+
    | x3      |-----| h3      |------| y3      |
    +---------+     +---------+      +---------+
    | x4      |-----| h4      |------| y4      |
    +---------+     +---------+      +---------+

Deep Network:

    Input Layer     Hidden Layer 1   Hidden Layer 2   Output Layer
    +---------+     +---------+      +---------+      +---------+
    | x1      |-----| h1      |------| h5      |------| y1      |
    +---------+     +---------+      +---------+      +---------+
    | x2      |-----| h2      |------| h6      |------| y2      |
    +---------+     +---------+      +---------+      +---------+
    | x3      |-----| h3      |------| h7      |------| y3      |
    +---------+     +---------+      +---------+      +---------+
    | x4      |-----| h4      |------| h8      |------| y4      |
    +---------+     +---------+      +---------+      +---------+

The main advantage of deep networks over shallow networks is that they can create deep representations, meaning that at every layer, the network learns a new, more abstract representation of the input . For example, in image recognition, the first layer may detect edges, the second layer may detect shapes, the third layer may detect objects, and so on. These representations can capture more complex and nonlinear patterns in the data, leading to better performance.

Another advantage of deep networks is that they can be much more efficient in terms of computation and number of parameters than shallow networks. For the same level of accuracy, deep networks can use fewer neurons and connections than shallow networks, because they can exploit the hierarchical structure of the data . This reduces the memory and computational requirements, as well as the risk of overfitting.