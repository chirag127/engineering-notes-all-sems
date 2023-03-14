### Backpropagation for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning

- Backpropagation is a method of computing the partial derivatives of a loss function with respect to the parameters of a neural network.
- Backpropagation is based on the chain rule of calculus, which allows us to propagate the error from the output layer to the hidden layers and the input layer .
- Backpropagation consists of two phases: forward propagation and backward propagation.
  - In forward propagation, the input data is passed through the network and the output is computed. The output is then compared with the target value to calculate the loss function.
  - In backward propagation, the loss function is differentiated with respect to each parameter of the network, starting from the output layer and moving backwards. The gradients are then used to update the parameters using a gradient descent algorithm.
- Backpropagation is a key technique for training deep neural networks, as it allows us to adjust the weights and biases of the network according to the error signal.
- Backpropagation can be implemented using various algorithms, such as stochastic gradient descent, mini-batch gradient descent, momentum, RMSprop, Adam, etc.
- Backpropagation can be visualized as a flow of information from the output layer to the input layer, where each node receives a signal from its downstream nodes and passes it to its upstream nodes after multiplying it by the corresponding weight and applying the derivative of the activation function.
- Backpropagation can be summarized by the following steps:
  - Initialize the network parameters randomly.
  - For each training example:
    - Perform forward propagation and compute the output and the loss function.
    - Perform backward propagation and compute the gradients of the loss function with respect to each parameter.
    - Update the parameters using the gradients and a learning rate.
  - Repeat until convergence or a maximum number of iterations.

- A possible mnemonic for remembering the steps of backpropagation is: **F**orward, **B**ackward, **U**pdate, **R**epeat, or **F**B**U**R.