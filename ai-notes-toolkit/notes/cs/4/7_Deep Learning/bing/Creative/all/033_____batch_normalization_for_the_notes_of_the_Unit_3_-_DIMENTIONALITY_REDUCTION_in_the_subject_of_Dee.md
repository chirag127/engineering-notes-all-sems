# Batch Normalization for Deep Learning

- Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch  .
- This has the effect of stabilizing the learning process and dramatically reducing the number of training epochs required to train deep networks  .
- Batch normalization also provides some regularization effect, reducing the need for dropout or other techniques .
- Batch normalization can be applied to either the activations of a prior layer or the inputs directly.
- Batch normalization involves two steps:
  - First, the mean and standard deviation of the mini-batch are computed and used to normalize the inputs.
  - Second, the normalized inputs are scaled and shifted by two learnable parameters, gamma and beta, which control the mean and variance of the outputs  .
- Batch normalization can be implemented as a layer in a deep neural network, and is usually placed before the activation function of the layer .
- Batch normalization has several advantages, such as:
  - It reduces the internal covariate shift, which is the change in the distribution of layer inputs during training, caused by the updates of the previous layers.
  - It allows the use of higher learning rates, which can speed up the convergence and improve the performance .
  - It reduces the sensitivity to the initialization of the weights, which can simplify the choice of hyperparameters .
  - It acts as a regularizer, which can prevent overfitting and improve the generalization .