### Backpropagation and regularization for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning

- Backpropagation is a widely used method for calculating derivatives inside deep feedforward neural networks. It is based on the chain rule of calculus, which allows us to compute the gradient of a loss function with respect to any parameter of the network by propagating the error backwards from the output layer to the input layer.
- Backpropagation forms an important part of a number of supervised learning algorithms for training neural networks, such as stochastic gradient descent (SGD). SGD updates the parameters of the network by subtracting a small fraction of the gradient from the current values, thus moving towards the direction of steepest descent in the loss function.
- Backpropagation can be used to train neural networks with multiple layers, also known as deep neural networks. Deep neural networks can learn complex and nonlinear patterns from large and high-dimensional datasets, such as images, text, speech, etc. However, they also pose some challenges, such as overfitting, vanishing or exploding gradients, and computational complexity.
- Overfitting occurs when a neural network learns the training data too well and fails to generalize to new and unseen data. This can result in a high variance and a low bias in the model, meaning that the model is sensitive to small changes in the input and has a low error on the training data but a high error on the test data.
- Regularization is any modification we make to a learning algorithm that is intended to reduce its generalization error but not its training error. Regularization is one of the central concerns of the field of machine learning, rivaled in its importance only by optimization. Regularization methods aim to prevent overfitting by constraining the complexity of the model or adding some noise to the learning process.
- Some common regularization methods for deep neural networks are:

  - Weight decay: This method adds a penalty term to the loss function that is proportional to the squared norm of the weights. This encourages the weights to be small and reduces the variance of the model. Weight decay can be implemented by multiplying the weights by a factor slightly less than 1 after each update.
  - Dropout: This method randomly drops out some units and their connections during the training process, creating a thinned network. This reduces the co-adaptation of features and forces the network to learn more robust and independent representations. Dropout can be implemented by multiplying the outputs of each unit by a binary mask that is sampled from a Bernoulli distribution with a given probability.
  - Weight constraint: This method imposes a hard or soft constraint on the norm of the weights, such as clipping or projecting them to a predefined range. This prevents the weights from growing too large and causing numerical instability or overfitting. Weight constraint can be implemented by applying a clipping or projection function to the weights after each update.

- A modern recommendation for regularization is to use early stopping with dropout and a weight constraint. Early stopping is a simple but effective technique that stops the training process when the validation error starts to increase, thus avoiding overfitting to the training data. Early stopping can be implemented by monitoring the validation error after each epoch and saving the best model so far.

: https://machinelearningmastery.com/introduction-to-regularization-to-reduce-overfitting-and-improve-generalization-error/

: https://arxiv.org/abs/2202.05089

: https://learner-cares.medium.com/explain-the-concept-of-backpropagation-and-how-it-is-used-in-neural-networks-7f6d9a91d6f

: https://deepai.org/machine-learning-glossary-and-terms/backpropagation

: https://machinelearningmastery.com/best-advice-for-configuring-backpropagation-for-deep-learning-neural-networks/