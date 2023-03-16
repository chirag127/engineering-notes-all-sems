# Architecture for the notes of the Unit 2 - Neural Networks-II (Back propagation networks) in the subject of APPLICATION OF SOFT COMPUTING TECHNIQUES

- A back propagation network is a type of artificial neural network that uses a supervised learning algorithm to produce a desired output .
- The algorithm adjusts the weights of the connections between the nodes in the network according to a feedback signal that indicates the error between the actual output and the desired output .
- The feedback signal is propagated backward through the network, hence the name back propagation.
- The back propagation algorithm consists of two phases: forward propagation and backward propagation.
- In forward propagation, the input data is fed to the input layer of the network, and the output of each layer is computed by applying an activation function to the weighted sum of the inputs from the previous layer.
- The output of the final layer is compared with the desired output to calculate the error.
- In backward propagation, the error is propagated backward through the network, and the weights are updated by applying a learning rule that depends on the error and the activation function.
- The process of forward and backward propagation is repeated until the error is minimized or a predefined criterion is met.
- The architecture of a back propagation network consists of three main components: input layer, hidden layer(s), and output layer .
- The input layer consists of nodes that receive the input data and pass it to the hidden layer(s) .
- The hidden layer(s) consist of nodes that perform nonlinear transformations on the inputs from the previous layer and pass the outputs to the next layer .
- The output layer consists of nodes that produce the final output of the network and compare it with the desired output to calculate the error .
- The number of nodes in the input and output layers depends on the dimensionality of the input and output data, respectively .
- The number of hidden layers and nodes in each hidden layer can vary depending on the complexity of the problem and the design choice .
- The activation function for each node can be chosen from a variety of functions, such as sigmoid, tanh, ReLU, etc .
- The learning rule for updating the weights can be chosen from a variety of methods, such as gradient descent, momentum, adaptive learning rate, etc .
- The back propagation network can be used for various applications, such as classification, regression, function approximation, pattern recognition, etc .