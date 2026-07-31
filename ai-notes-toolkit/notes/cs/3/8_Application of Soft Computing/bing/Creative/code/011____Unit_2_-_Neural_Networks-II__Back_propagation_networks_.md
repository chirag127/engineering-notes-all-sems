# Unit 2 - Neural Networks-II (Back propagation networks)

- Back propagation networks are a type of artificial neural networks that use a learning algorithm called backpropagation to train the network weights based on the error rate obtained in the previous iteration .
- Backpropagation is a short form for “backward propagation of errors.” It is a standard method of training artificial neural networks.
- Backpropagation involves two phases: forward propagation and backward propagation .
  - In forward propagation, the input data is fed to the network and the output is computed. The output is then compared with the desired output (target) and the error is calculated .
  - In backward propagation, the error is propagated back through the network layers and the weights are updated according to a rule that minimizes the error .
- Backpropagation requires the activation functions of the network to be differentiable, since it uses the chain rule of calculus to compute the gradients of the error with respect to the weights .
- Backpropagation can be applied to any feedforward network, as well as to some recurrent networks and other types of networks.
- Backpropagation is the essence of neural network training, as it allows the network to learn from its own mistakes and improve its performance .