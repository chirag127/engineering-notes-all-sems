# Solution for the notes of the Unit 2 - Neural Networks-II (Back propagation networks) in the subject of Application of Soft Computing

- Neural networks are computational models that can learn from data and perform tasks such as classification, regression, clustering, etc.
- Back propagation is a learning algorithm that adjusts the weights and biases of a neural network based on the error between the desired output and the actual output.
- The main steps of back propagation are:
  - Forward propagation: the input data is fed to the network and the output is computed by applying the activation functions to the weighted sums of the inputs at each layer.
  - Error computation: the error or loss is calculated by comparing the output with the target value, usually using a cost function such as mean squared error or cross entropy.
  - Backward propagation: the error is propagated back to the previous layers by applying the chain rule of differentiation to find the gradients of the cost function with respect to the weights and biases.
  - Weight update: the weights and biases are updated by subtracting a fraction of the gradients, called the learning rate, from the current values. This process is repeated until the error is minimized or a stopping criterion is met.
- The advantages of back propagation are:
  - It can learn complex nonlinear functions and generalize well to unseen data.
  - It can be applied to various network architectures and activation functions.
  - It can be combined with other optimization techniques such as momentum, regularization, dropout, etc.
- The disadvantages of back propagation are:
  - It can be slow and computationally expensive, especially for large and deep networks.
  - It can get stuck in local minima or saddle points, where the gradients are zero or very small.
  - It can suffer from the vanishing or exploding gradient problem, where the gradients become too small or too large to be useful.
  - It can overfit the data if the network is too complex or the training data is too noisy or scarce.