## Unit 2 - Neural Networks-II (Back propagation networks)

- Back propagation networks are a type of artificial neural networks that use a learning algorithm called backpropagation to train the network weights based on the error rate obtained in the previous iteration .
- Backpropagation is a process that involves taking the error rate of a forward propagation (i.e., the prediction of the network output based on the input) and feeding this loss backward through the network layers to fine-tune the weights.
- Backpropagation is based on the chain rule of calculus, which allows us to compute the gradient of a loss function with respect to all the weights in the network by applying the product rule repeatedly.
- The gradient of the loss function is a vector that points in the direction of the steepest ascent of the loss function, which means that subtracting the gradient from the weights will move them towards the direction of the steepest descent, or the minimum of the loss function.
- The steps of the backpropagation algorithm are as follows:
  - Initialize the network weights randomly.
  - For each training example:
    - Perform a forward pass to compute the network output and the loss function.
    - Perform a backward pass to compute the gradient of the loss function with respect to each weight using the chain rule.
    - Update the weights by subtracting a fraction of the gradient, called the learning rate, from the current weights.
  - Repeat the above steps for a fixed number of iterations, called epochs, or until the loss function reaches a desired value or stops decreasing.
- Backpropagation is the essence of neural network training, as it allows the network to learn from its own errors and adjust its weights accordingly to improve its performance .