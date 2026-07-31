### Backpropagation and regularization for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning

- Backpropagation is a widely used method for calculating derivatives inside deep feedforward neural networks.
- Backpropagation efficiently computes the gradient of the loss function with respect to the network weights, which can be used to update the weights using gradient descent or other optimization algorithms .
- Backpropagation consists of two phases: a forward pass and a backward pass.
  - In the forward pass, the input is propagated through the network layers and the output is compared with the target to compute the loss.
  - In the backward pass, the loss is propagated back through the network layers using the chain rule of calculus, and the partial derivatives of the loss with respect to each weight are computed.
- Backpropagation can fail in some cases, such as vanishing gradients, exploding gradients, or saddle points.
  - Vanishing gradients occur when the lower layers of the network have very small gradients, which makes them learn very slowly or not at all.
  - Exploding gradients occur when the upper layers of the network have very large gradients, which makes them unstable and prone to overshooting the optimal values.
  - Saddle points occur when the loss function has flat regions where the gradient is zero, which makes the network stuck and unable to escape.
- Regularization is any modification we make to a learning algorithm that is intended to reduce its generalization error but not its training error.
- Regularization is one of the central concerns of the field of machine learning, as it helps to avoid overfitting and improve generalization performance.
- Regularization can be applied in different ways, such as adding a penalty term to the loss function, adding noise to the inputs or outputs, using dropout or batch normalization, or using early stopping .
  - Adding a penalty term to the loss function, such as L1 or L2 regularization, makes the network prefer simpler or sparser models that have smaller weights.
  - Adding noise to the inputs or outputs, such as Gaussian noise or label smoothing, makes the network more robust to variations and uncertainties in the data.
  - Using dropout or batch normalization, which randomly drop out or normalize some units or features during training, makes the network less dependent on specific activations or inputs and more diverse and flexible .
  - Using early stopping, which stops the training when the validation error stops improving, prevents the network from overfitting to the training data and memorizing noise .