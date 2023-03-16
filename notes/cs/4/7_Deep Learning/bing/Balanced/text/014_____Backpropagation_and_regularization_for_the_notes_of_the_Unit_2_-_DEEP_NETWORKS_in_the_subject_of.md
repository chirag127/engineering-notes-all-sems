### Backpropagation and regularization for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning

- Backpropagation is a method of training neural networks by computing the gradients of the loss function with respect to the weights and biases, and updating them in the opposite direction of the gradient.
- Backpropagation consists of two phases: forward propagation and backward propagation.
- In forward propagation, the input data is fed to the network and the output is computed by applying the activation functions and the weights and biases at each layer.
- In backward propagation, the error or loss is calculated by comparing the output with the target or desired output, and the gradients are computed by applying the chain rule of differentiation.
- The gradients are then used to update the weights and biases by subtracting a fraction of the gradient, called the learning rate, from the current values.
- The process of forward and backward propagation is repeated for each batch of data until the loss is minimized or the network converges to a satisfactory performance.
- Regularization is a technique of preventing overfitting, which is a situation where the network performs well on the training data but poorly on the test or unseen data.
- Overfitting occurs when the network learns the noise or irrelevant features of the data, and fails to generalize to new or different data.
- Regularization aims to reduce the complexity or capacity of the network, by adding a penalty term to the loss function, which depends on the magnitude or norm of the weights and biases.
- Regularization can be of two types: L1 and L2 regularization.
- L1 regularization, also known as Lasso, adds the absolute value of the weights to the loss function, and encourages the network to have sparse or zero weights for some features.
- L2 regularization, also known as Ridge, adds the square of the weights to the loss function, and encourages the network to have small or low weights for all features.
- Regularization can also be achieved by other methods, such as dropout, batch normalization, early stopping, data augmentation, etc.