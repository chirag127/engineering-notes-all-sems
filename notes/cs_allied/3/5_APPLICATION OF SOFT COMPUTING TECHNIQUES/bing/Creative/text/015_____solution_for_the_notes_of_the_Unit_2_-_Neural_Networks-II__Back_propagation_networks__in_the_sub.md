### Solution for the notes of the Unit 2 - Neural Networks-II (Back propagation networks) in the subject of APPLICATION OF SOFT COMPUTING TECHNIQUES

- Back propagation networks are a type of artificial neural networks that use a supervised learning algorithm to produce a desired output .
- The algorithm adjusts the weights of the connections between the nodes in the network according to a feedback signal, which is the difference between the actual output and the desired output .
- The feedback signal is propagated backwards through the network, hence the name back propagation.
- The goal of back propagation is to minimize the error or the loss function of the network .
- The steps of back propagation are as follows:
  - Initialize the network with random weights and biases.
  - Perform a forward pass to compute the output of the network for a given input.
  - Calculate the error or the loss function for the output using a predefined criterion, such as mean squared error or cross entropy.
  - Perform a backward pass to compute the gradients of the error with respect to the weights and biases of the network using the chain rule of differentiation.
  - Update the weights and biases of the network using a learning rate and an optimization technique, such as gradient descent or stochastic gradient descent.
  - Repeat the steps until the error or the loss function reaches a minimum or a predefined threshold.
- Back propagation networks can be used for various applications, such as classification, regression, image recognition, natural language processing, speech recognition, etc  .