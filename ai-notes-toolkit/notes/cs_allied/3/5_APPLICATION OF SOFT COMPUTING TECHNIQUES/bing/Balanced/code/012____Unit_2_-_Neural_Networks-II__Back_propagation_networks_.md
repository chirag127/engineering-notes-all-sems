## Unit 2 - Neural Networks-II (Back propagation networks)

- Back propagation networks are a type of artificial neural networks that use a learning algorithm called backpropagation to train the network weights based on the error rate obtained in the previous iteration .
- Backpropagation is a process that involves taking the error rate of a forward propagation (i.e., the prediction of the network output given the input) and feeding this loss backward through the network layers to fine-tune the weights.
- Backpropagation is based on the chain rule of calculus, which allows us to compute the gradient of a loss function with respect to all the weights in the network by applying the product rule repeatedly.
- The steps of backpropagation are as follows:
  - Initialize the network weights randomly.
  - For each training example, perform the following substeps:
    - Forward propagation: feed the input to the network and compute the output.
    - Error computation: calculate the difference between the output and the desired target.
    - Backward propagation: propagate the error backward through the network and update the weights using a learning rate.
  - Repeat the above steps for a fixed number of epochs or until the error is minimized.
- Backpropagation is the essence of neural network training as it allows the network to learn from its own mistakes and improve its performance over time .