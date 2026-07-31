### Backpropagation and regularization for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning

- Backpropagation is a widely used method for calculating derivatives inside deep feedforward neural networks.
- Backpropagation forms an important part of a number of supervised learning algorithms for training feedforward neural networks, such as stochastic gradient descent.
- Backpropagation algorithm is key to supervised learning of deep neural networks and has enabled the recent surge in popularity of deep learning algorithms since the early 2000s.
- Backpropagation formula for a multilayer feedforward neural network with N layers:

```
# For the output layer:
delta_N = y - a_N # the error term
dL/dw_N = a_N-1^T * delta_N # the derivative of the loss with respect to the weights
dL/db_N = delta_N # the derivative of the loss with respect to the biases

# For the hidden layers:
delta_l = (delta_l+1 * w_l+1^T) * f'(z_l) # the error term
dL/dw_l = a_l-1^T * delta_l # the derivative of the loss with respect to the weights
dL/db_l = delta_l # the derivative of the loss with respect to the biases
```

- Where y is the target output, a_l is the activation of layer l, w_l is the weight matrix of layer l, b_l is the bias vector of layer l, z_l is the weighted input of layer l, f is the activation function, and L is the loss function.

- Backpropagation can fail in some cases, such as exploding gradients, vanishing gradients, and dead ReLU units.
- Exploding gradients occur when the magnitude of the gradients becomes very large, causing the weights to update too much and the network to diverge.
- Vanishing gradients occur when the magnitude of the gradients becomes very small, causing the weights to update too little and the network to stagnate.
- Dead ReLU units occur when the weighted sum for a ReLU unit falls below 0, causing the unit to output 0 activation and stop learning.
- Regularization is any modification we make to a learning algorithm that is intended to reduce its generalization error but not its training error.
- Regularization is one of the central concerns of the field of machine learning, rivaled in its importance only by optimization.
- Regularization methods for neural networks include weight decay, dropout, early stopping, batch normalization, data augmentation, and noise injection.
- Weight decay is a technique that adds a penalty term to the loss function that is proportional to the sum of the squared weights, which encourages the network to learn smaller weights and prevent overfitting.
- Dropout is a technique that randomly drops out some units and their connections during training, which forces the network to learn redundant representations and prevent co-adaptation of features.
- Early stopping is a technique that stops the training process when the validation error starts to increase, which prevents the network from overfitting to the training data.
- Batch normalization is a technique that normalizes the inputs of each layer to have zero mean and unit variance, which helps prevent exploding gradients, speed up convergence, and improve generalization.
- Data augmentation is a technique that artificially increases the size and diversity of the training data by applying random transformations, such as cropping, flipping, rotating, or adding noise, which helps the network learn invariant features and prevent overfitting.
- Noise injection is a technique that adds random noise to the inputs, outputs, or weights of the network, which helps the network learn robust features and prevent overfitting.