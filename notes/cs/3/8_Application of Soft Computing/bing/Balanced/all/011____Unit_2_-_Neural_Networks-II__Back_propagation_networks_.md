# Unit 2 - Neural Networks-II (Back propagation networks)

- Back propagation networks are a type of artificial neural networks that use a learning algorithm called backpropagation to train the network weights based on the error rate obtained in the previous iteration .
- Backpropagation is a process that involves taking the error rate of a forward propagation (i.e., the prediction of the network output given the input) and feeding this loss backward through the network layers to fine-tune the weights.
- Backpropagation is based on the chain rule of calculus, which allows us to compute the gradient of a loss function with respect to all the weights in the network .
- The gradient is a vector that points in the direction of the steepest ascent of the loss function, and by updating the weights in the opposite direction, we can minimize the loss function and improve the network performance.
- The steps of backpropagation are as follows:
  - Initialize the network weights randomly.
  - For each training example, perform the following substeps:
    - Forward propagation: feed the input to the network and compute the output.
    - Backward propagation: calculate the error between the output and the target, and propagate it back through the network to update the weights.
  - Repeat the above steps for a fixed number of epochs (i.e., iterations over the entire training set) or until the error is sufficiently low.