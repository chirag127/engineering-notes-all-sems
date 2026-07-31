## Unit 2 - Neural Networks-II (Back propagation networks)

- Back propagation networks are a type of artificial neural networks that use a learning algorithm called backpropagation to train the network weights based on the error rate obtained in the previous iteration .
- Backpropagation is a process of propagating the error backward through the network layers, starting from the output layer to the input layer, and adjusting the weights accordingly .
- Backpropagation consists of two phases: forward propagation and backward propagation.
  - In forward propagation, the input data is fed to the network and the output is computed using the current weights. The output is then compared with the desired output (target) and the error is calculated.
  - In backward propagation, the error is propagated back to the previous layers using the chain rule of differentiation. The weights are updated by subtracting a fraction of the gradient of the error with respect to the weights. This fraction is called the learning rate.
- Backpropagation is repeated for a number of epochs (iterations) until the error is minimized or a convergence criterion is met.
- Backpropagation is widely used for training feedforward neural networks, such as multilayer perceptrons, convolutional neural networks, and recurrent neural networks.
- Backpropagation can also be generalized to other types of neural networks and functions, such as radial basis function networks, autoencoders, and deep belief networks.