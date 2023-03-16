### Backpropagation and regularization for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning

- Backpropagation is a widely used method for calculating derivatives inside deep feedforward neural networks.
- Backpropagation efficiently computes the gradient of the loss function with respect to the network weights, which can be used to update the weights using gradient descent or other optimization algorithms .
- Backpropagation consists of two phases: a forward pass and a backward pass.
  - In the forward pass, the input is propagated through the network layers and the output is compared with the target to compute the loss.
  - In the backward pass, the loss is propagated back through the network layers and the partial derivatives of the loss with respect to each weight are computed using the chain rule.
- Backpropagation can fail in some cases, such as vanishing gradients, exploding gradients, or saddle points.
  - Vanishing gradients occur when the lower layers of the network have very small gradients, which makes them learn very slowly or not at all.
  - Exploding gradients occur when the upper layers of the network have very large gradients, which makes them unstable or diverge.
  - Saddle points occur when the loss function has flat regions or plateaus, which makes the gradient zero or very small and prevents the network from finding a better solution.
- Regularization is any modification we make to a learning algorithm that is intended to reduce its generalization error but not its training error.
- Regularization is one of the central concerns of the field of machine learning, as it helps to avoid overfitting and improve the performance of the network on unseen data.
- There are many types of regularization techniques, such as weight decay, dropout, batch normalization, data augmentation, early stopping, etc.
  - Weight decay adds a penalty term to the loss function that depends on the magnitude of the weights, which encourages the network to use smaller weights and reduce the complexity of the model.
  - Dropout randomly drops out some units or connections in the network during training, which prevents the network from relying too much on specific features and reduces the co-adaptation of units.
  - Batch normalization normalizes the inputs of each layer to have zero mean and unit variance, which reduces the internal covariate shift and improves the stability and speed of training.
  - Data augmentation applies random transformations to the input data, such as rotation, scaling, cropping, flipping, etc, which increases the diversity and size of the training data and reduces the overfitting to specific patterns.
  - Early stopping stops the training process when the validation error stops decreasing or starts increasing, which prevents the network from overfitting to the training data and saves computational resources.