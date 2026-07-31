# Architecture for the notes of the Unit 2 - Neural Networks-II (Back propagation networks) in the subject of Application of Soft Computing

- A back propagation network is a type of artificial neural network that uses a supervised learning algorithm to produce a desired output  .
- The algorithm adjusts the weights of the connections between the nodes in the network according to a feedback signal that indicates the error between the actual output and the desired output  .
- The feedback signal is propagated backward through the network, hence the name back propagation.
- The back propagation algorithm consists of two phases: forward propagation and backward propagation   .
- In forward propagation, the input data is fed to the input layer of the network and passed through the hidden layers to the output layer, where the output is computed   .
- In backward propagation, the error between the actual output and the desired output is calculated and propagated back through the network, updating the weights of the connections according to a learning rule   .
- The learning rule is usually based on the gradient descent method, which aims to minimize the error function by adjusting the weights in the direction of the negative gradient   .
- The back propagation algorithm can be applied to any feedforward neural network with differentiable activation functions.
- The back propagation algorithm can learn complex nonlinear mappings between the input and the output, and can generalize well to unseen data   .
- The back propagation algorithm has some limitations, such as the possibility of getting stuck in local minima, the difficulty of choosing the optimal learning rate and the number of hidden layers and nodes, and the problem of overfitting   .