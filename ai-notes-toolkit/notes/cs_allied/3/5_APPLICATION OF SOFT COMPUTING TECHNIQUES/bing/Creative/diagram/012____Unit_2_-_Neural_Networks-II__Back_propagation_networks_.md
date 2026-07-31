## Unit 2 - Neural Networks-II (Back propagation networks)

- Back propagation networks are a type of artificial neural networks that use a supervised learning algorithm to train the network weights based on the error rate obtained in the previous iteration .
- Back propagation networks consist of an input layer, one or more hidden layers, and an output layer. Each layer has a number of neurons that are connected by weighted links to the neurons in the next layer.
- The training process of back propagation networks involves two phases: forward propagation and backward propagation .
  - Forward propagation: The input data is fed to the input layer and passed through the hidden layers to the output layer. The output layer produces the predicted output based on the current weights and the activation function of each neuron.
  - Backward propagation: The predicted output is compared with the actual output (target) to calculate the error rate (loss function). The error rate is then propagated backward through the network layers to adjust the weights according to a learning rule (such as gradient descent).
- The goal of back propagation is to minimize the error rate by finding the optimal weights that make the network output as close as possible to the target output  .
- Back propagation is the most widely used algorithm for training feedforward neural networks, and it can be generalized to other types of neural networks and functions.