## Unit 2 - Neural Networks-II (Back propagation networks)

- Back propagation networks are a type of artificial neural networks that use a learning algorithm called backpropagation to train the network weights based on the error rate obtained in the previous iteration .
- Backpropagation is a process that involves taking the error rate of a forward propagation (i.e., the prediction of the network output given the input) and feeding this loss backward through the network layers to fine-tune the weights.
- Backpropagation is based on the chain rule of calculus, which allows us to compute the gradient of a loss function with respect to all the weights in the network by applying the product rule repeatedly.
- The gradient of the loss function is a vector that points in the direction of the steepest ascent of the loss function, and thus the negative gradient points in the direction of the steepest descent of the loss function.
- The goal of backpropagation is to update the network weights in the opposite direction of the gradient, so that the loss function is minimized and the network output is closer to the desired output.
- The steps of backpropagation are as follows:
  - Initialize the network weights randomly.
  - For each epoch (i.e., iteration over the training data):
    - For each input-output pair in the training data:
      - Perform forward propagation to compute the network output and the loss function.
      - Perform backward propagation to compute the gradient of the loss function with respect to each weight in the network.
      - Update the network weights by subtracting a small fraction of the gradient (called the learning rate) from the current weights.
    - Evaluate the network performance on the validation data and check for convergence or overfitting.
  - Return the final network weights.