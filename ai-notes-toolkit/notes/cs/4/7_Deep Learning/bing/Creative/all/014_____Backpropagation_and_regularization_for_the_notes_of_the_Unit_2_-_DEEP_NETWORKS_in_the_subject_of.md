# Backpropagation and regularization for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning

## Backpropagation
- Backpropagation is a widely used method for calculating derivatives inside deep feedforward neural networks.
- Backpropagation forms an important part of a number of supervised learning algorithms for training feedforward neural networks, such as stochastic gradient descent.
- Backpropagation efficiently computes the gradient of the loss function with respect to the network weights, by applying the chain rule of calculus.
- Backpropagation consists of two phases: a forward pass and a backward pass.
  - In the forward pass, the input is propagated through the network layers and the output is compared with the target to compute the loss.
  - In the backward pass, the error is propagated back through the network layers and the weights are updated according to the gradient.
- Backpropagation is key to supervised learning of deep neural networks and has enabled the recent surge in popularity of deep learning algorithms since the early 2000s.

## Regularization
- Regularization is any modification we make to a learning algorithm that is intended to reduce its generalization error but not its training error.
- Regularization is one of the central concerns of the field of machine learning, rivaled in its importance only by optimization.
- Regularization helps to avoid overfitting, which is a common problem in deep learning neural networks, where the model learns the noise or the specific patterns of the training data, rather than the underlying function.
- Regularization techniques can be applied at different levels of the learning process, such as the data, the model, the objective function, or the optimization algorithm.
- Some common regularization techniques for deep learning neural networks are :
  - Data augmentation: generating more training data by applying transformations to the existing data, such as rotation, scaling, cropping, flipping, etc.
  - Weight decay: adding a penalty term to the objective function that depends on the magnitude of the weights, such as L1 or L2 regularization.
  - Dropout: randomly dropping out some units or connections in the network during training, to reduce the co-adaptation of features and increase the robustness of the model.
  - Batch normalization: normalizing the inputs of each layer to have zero mean and unit variance, to reduce the internal covariate shift and speed up the training.
  - Early stopping: stopping the training when the validation error starts to increase, to prevent overfitting and save computational resources.