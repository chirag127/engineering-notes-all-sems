### Architecture for the notes of the Unit 2 - Neural Networks-II (Back propagation networks) in the subject of Application of Soft Computing

- A back propagation network is a type of artificial neural network that uses a supervised learning algorithm to produce a desired output .
- The algorithm adjusts the weights of the connections between the nodes in the network according to a feedback signal that indicates the error rate of a forward propagation .
- The goal of back propagation is to minimize the error or loss function of the network by updating the weights in the opposite direction of the gradient .
- The basic architecture of a back propagation network consists of three layers: an input layer, a hidden layer and an output layer .
- The input layer receives the input data and passes it to the hidden layer. The hidden layer performs some nonlinear transformations on the input data and passes it to the output layer. The output layer produces the output of the network and compares it with the desired output .
- The error or difference between the actual output and the desired output is then propagated back through the network, starting from the output layer to the hidden layer and then to the input layer .
- The weights of the connections are updated according to a learning rule that depends on the error and the gradient of the activation function of each node .
- The process of forward propagation and back propagation is repeated until the error of the network is reduced to an acceptable level or a predefined number of iterations is reached .