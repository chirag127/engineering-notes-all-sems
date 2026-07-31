### Solution for the notes of the Unit 2 - Neural Networks-II (Back propagation networks) in the subject of APPLICATION OF SOFT COMPUTING TECHNIQUES

- Back propagation networks are a type of artificial neural networks that use a supervised learning algorithm to produce a desired output .
- The algorithm adjusts the weights of the connections between the nodes in the network according to a feedback signal that measures the error rate of a forward propagation .
- The goal of back propagation is to minimize the error or loss function, which is the difference between the actual output and the desired output .
- The steps of back propagation are as follows :
  - Initialize the network with random weights and biases.
  - Feed the input data to the network and compute the output for each layer using an activation function.
  - Compare the output of the network with the desired output and calculate the error or loss function.
  - Propagate the error backward from the output layer to the hidden layers, using the chain rule of differentiation to compute the gradients of the loss function with respect to the weights and biases.
  - Update the weights and biases of the network using a learning rate and the gradients, using an optimization algorithm such as gradient descent or stochastic gradient descent.
  - Repeat the process until the error or loss function is minimized or a convergence criterion is met.
- Back propagation networks can be used for various applications such as classification, regression, pattern recognition, image processing, natural language processing, etc .