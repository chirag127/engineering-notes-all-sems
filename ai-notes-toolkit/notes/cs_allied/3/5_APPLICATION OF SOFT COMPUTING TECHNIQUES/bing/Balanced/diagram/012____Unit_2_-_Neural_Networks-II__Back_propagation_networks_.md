## Unit 2 - Neural Networks-II (Back propagation networks)

- Back propagation networks are a type of artificial neural networks that use a learning algorithm called backpropagation to train the network weights based on the error rate obtained in the previous iteration .
- Backpropagation is a process that involves taking the error rate of a forward propagation (i.e., the prediction of the network output given the input) and feeding this loss backward through the network layers to fine-tune the weights.
- Backpropagation is based on the chain rule of calculus, which allows us to compute the gradient of a loss function with respect to all the weights in the network .
- The gradient is a vector that points in the direction of the steepest ascent of the loss function, and by updating the weights in the opposite direction, we can minimize the loss function and improve the network performance.
- The steps of backpropagation are as follows:
  - Initialize the network weights randomly.
  - For each epoch (i.e., iteration over the training data):
    - For each input-output pair in the training data:
      - Perform forward propagation to compute the network output and the loss function.
      - Perform backward propagation to compute the gradient of the loss function with respect to each weight in the network.
      - Update the weights by subtracting a fraction of the gradient (called the learning rate) from the current weights.
    - Evaluate the network performance on the validation data and check for convergence or overfitting.
- Backpropagation is the essence of neural network training, as it allows the network to learn from its own errors and adjust its weights accordingly .