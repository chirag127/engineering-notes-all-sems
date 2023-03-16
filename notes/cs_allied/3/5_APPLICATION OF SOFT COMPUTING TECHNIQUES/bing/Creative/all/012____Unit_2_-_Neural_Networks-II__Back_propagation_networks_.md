# Unit 2 - Neural Networks-II (Back propagation networks)

- Back propagation networks are a type of artificial neural networks that use a learning algorithm called backpropagation to train the network weights based on the error rate obtained in the previous iteration .
- Backpropagation is a process of propagating the error backward through the network layers, starting from the output layer to the input layer, and adjusting the weights accordingly to minimize the loss function .
- Backpropagation consists of two phases: forward propagation and backward propagation.
  - In forward propagation, the input data is fed to the network and the output is computed using the current weights. The output is then compared with the desired output (target) and the error is calculated.
  - In backward propagation, the error is multiplied by the derivative of the activation function at each node to obtain the error gradient. The error gradient is then used to update the weights by subtracting a fraction of it (learning rate) from the current weights.
- Backpropagation is repeated for a number of epochs (iterations) until the error is sufficiently low or the network converges.
- Backpropagation is widely used for training feedforward neural networks, such as multilayer perceptrons, convolutional neural networks, and recurrent neural networks.
- Backpropagation has some advantages and disadvantages as a learning algorithm .
  - Advantages:
    - It is a general and powerful method that can handle complex and nonlinear problems.
    - It can learn from both supervised and unsupervised data.
    - It can adapt to changing data and environments by updating the weights online.
  - Disadvantages:
    - It can be slow and computationally expensive, especially for large and deep networks.
    - It can get stuck in local minima or saddle points of the loss function, leading to suboptimal solutions.
    - It can suffer from overfitting or underfitting, depending on the network architecture, regularization, and hyperparameters.