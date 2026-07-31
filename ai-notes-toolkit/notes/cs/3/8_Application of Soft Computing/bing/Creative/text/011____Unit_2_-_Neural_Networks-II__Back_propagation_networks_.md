## Unit 2 - Neural Networks-II (Back propagation networks)

- Backpropagation is a process involved in training a neural network  .
- It involves taking the error rate of a forward propagation and feeding this loss backward through the neural network layers to fine-tune the weights .
- Backpropagation is the essence of neural net training . It is the method of fine-tuning the weights of a neural network based on the error rate obtained in the previous epoch (i.e., iteration).
- Proper tuning of the weights allows you to reduce error rates and make the model reliable by increasing its generalization.
- Backpropagation is also known as "backward propagation of errors" . It is a standard method of training artificial neural networks.
- Backpropagation can be applied to any feedforward artificial neural network, and also to other types of artificial neural networks with some modifications.
- The backpropagation algorithm consists of the following steps:
  - Initialize the network weights randomly.
  - Perform a forward pass through the network and compute the output and the error for each training example.
  - Perform a backward pass through the network and compute the gradients of the error with respect to each weight using the chain rule.
  - Update the weights using a learning rate and the gradients.
  - Repeat the forward and backward passes for a number of epochs until the error is minimized or a stopping criterion is met.