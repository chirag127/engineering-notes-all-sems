## Unit 2 - Neural Networks-II (Back propagation networks)

- Back propagation networks are a type of artificial neural networks that use a learning algorithm called backpropagation to train the network weights based on the error rate obtained in the previous iteration .
- Backpropagation is a process that involves taking the error rate of a forward propagation (i.e., the prediction of the network output given the input) and feeding this loss backward through the network layers to fine-tune the weights .
- Backpropagation consists of two phases: forward phase and backward phase.
  - In the forward phase, the network takes the input and computes the output using the current weights. The output is then compared with the desired output (i.e., the target or label) to calculate the error or loss function.
  - In the backward phase, the network computes the gradient of the loss function with respect to each weight using the chain rule of differentiation. The gradient indicates how much each weight contributes to the error and in which direction it should be adjusted to reduce the error.
  - The network then updates the weights by subtracting a fraction of the gradient, called the learning rate, from the current weights. The learning rate controls how fast the network learns from the error.
- Backpropagation is repeated for a number of epochs (i.e., iterations) until the network converges to a minimum error or a satisfactory performance.
- Backpropagation is the essence of neural network training as it allows the network to learn from its own mistakes and improve its generalization ability .