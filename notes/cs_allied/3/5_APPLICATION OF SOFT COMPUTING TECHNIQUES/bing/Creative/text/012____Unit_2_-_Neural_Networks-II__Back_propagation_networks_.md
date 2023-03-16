## Unit 2 - Neural Networks-II (Back propagation networks)

- Back propagation networks are a type of artificial neural networks that use a learning algorithm called backpropagation to train the network weights based on the error rate obtained in the previous iteration .
- Backpropagation is a process of propagating the error backward through the network layers, starting from the output layer to the input layer, and adjusting the weights accordingly  .
- Backpropagation consists of two phases: forward propagation and backward propagation.
  - In forward propagation, the input data is fed to the network and the output is computed using the current weights. The output is then compared with the desired output (target) and the error is calculated.
  - In backward propagation, the error is multiplied by the derivative of the activation function at each node to obtain the error gradient. The error gradient is then used to update the weights by subtracting a fraction of it from the current weights. This fraction is called the learning rate and it controls how fast the network learns.
- Backpropagation is repeated for a number of epochs (iterations) until the network converges to a minimum error or a satisfactory performance.
- Backpropagation is widely used for training feedforward neural networks, such as multilayer perceptrons, convolutional neural networks, and recurrent neural networks.
- Backpropagation can also be generalized to other types of neural networks and functions, such as radial basis function networks, autoencoders, and deep belief networks.